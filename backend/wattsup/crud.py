from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
import pandas as pd

from wattsup import models
from wattsup import schemas
from wattsup.optimiser import Optimiser
from wattsup.database import get_engine


def create_appliance(db: Session, appliance: schemas.ApplianceCreate):
    """
    Create an appliance record and add it the databse

    Args:
        db (Session): database to add the appliance
        appliance (schemas.ApplianceCreate): appliance to add

    Returns:
        schemas.ApplianceCreateResponse: appliance and minimum total energy
    """
    db_appliance = models.Appliance(
        name=appliance.name,
        category=appliance.category,
        power=appliance.power,
    )
    db.add(db_appliance)
    db.commit()
    db.refresh(db_appliance)
    # add power to category
    add_category_power(db=db, 
                       category_id=appliance.category, 
                       net_power=appliance.power)
    # determine new minimum energy consumption
    minimum_energy_consumption = get_minimum_energy_consumption(db=db)
    response = {
        "minimum_total_energy": minimum_energy_consumption,
        "appliance": db_appliance,
    }
    return response

def get_appliance(db: Session, appliance_id: int):
    db_appliance = db.query(models.Appliance).filter(models.Appliance.id == appliance_id).first()
    if not db_appliance:
        raise HTTPException(status_code=404, detail="Appliance not found")
    return db_appliance

def update_appliance(db: Session, appliance_id: int, appliance: schemas.ApplianceCreate):

    db_appliance = get_appliance(db=db, appliance_id=appliance_id)
    # keep previous category and previous power
    prev_power = db_appliance.power
    prev_category = db_appliance.category

    # update appliance
    db_appliance.name = appliance.name
    db_appliance.category = appliance.category
    db_appliance.power = appliance.power
    db.commit()
    db.refresh(db_appliance)

    # remove previous power from previous category
    add_category_power(db=db, category_id=prev_category, net_power=-prev_power)
    # add new power to new category 
    add_category_power(db=db, category_id=appliance.category, net_power=appliance.power)

    # determine new minimum energy consumption
    minimum_energy_consumption = get_minimum_energy_consumption(db=db)

    # prepare response
    response = {
        "minimum_total_energy": minimum_energy_consumption,
        "appliance": db_appliance,
    }
    return response

def get_appliances(db: Session):
    db_appliances = db.query(models.Appliance).all()
    return db_appliances

def delete_appliance(db: Session, appliance_id:int):
    db_appliance = get_appliance(db=db, appliance_id=appliance_id)

    # keep previous category and previous power
    prev_power = db_appliance.power
    prev_category = db_appliance.category

    # remove appliance
    db.delete(db_appliance)
    db.commit()

    # remove previous power from previous category
    add_category_power(db=db, category_id=prev_category, net_power=-prev_power)

    # determine new minimum energy consumption
    minimum_energy_consumption = get_minimum_energy_consumption(db=db)

    # prepare response
    response = {
        "minimum_total_energy": minimum_energy_consumption,
    }
    return response

def get_category(db: Session, category_id: int):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category 

def get_categories(db: Session):
    db_categories = db.query(models.Category).all()
    return db_categories

def add_category_power(db: Session, category_id: int, net_power: float):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    db_category.power_appliances += net_power
    db.commit()
    db.refresh(db_category)

def get_minimum_energy_consumption(db: Session) -> float:
    minimum_energy = db.query(func.sum(models.Category.power_appliances * models.Category.minimum_duration)).scalar()
    return minimum_energy
    
def get_optimized_consumption(db: Session, total_expected_consumption: float):
    
    engine = get_engine()
    appliance_df = pd.read_sql('SELECT * FROM appliances', engine)
    category_df = pd.read_sql('SELECT * FROM categories', engine)

    determined_appliance_df = Optimiser.compute_optimal_consumption(appliance_df=appliance_df, 
                                                                      category_df=category_df,
                                                                      total_expected_consumption=total_expected_consumption)
    
