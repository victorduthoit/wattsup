from fastapi import HTTPException
from sqlalchemy.orm import Session
import models, schemas


def create_appliance(db: Session, appliance: schemas.ApplianceCreate):
    db_appliance = models.Appliance(
        name=appliance.name,
        category=appliance.category,
        power=appliance.power,
    )
    db.add(db_appliance)
    db.commit()
    db.refresh(db_appliance)
    return db_appliance

def update_appliance(db: Session, appliance_id: int, appliance: schemas.ApplianceCreate):
    db_appliance = db.query(models.Appliance).filter(models.Appliance.id == appliance_id).first()
    if not db_appliance:
        raise HTTPException(status_code=404, detail="Appliance not found")
    db_appliance.name = appliance.name
    db_appliance.category = appliance.category
    db_appliance.power = appliance.power
    db.commit()
    db.refresh(db_appliance)
    return db_appliance

def get_appliance(db: Session, appliance_id: int):
    db_appliance = db.query(models.Appliance).filter(models.Appliance.id == appliance_id).first()
    return db_appliance

def get_appliances(db: Session):
    db_appliance = db.query(models.Appliance).all()
    return db_appliance

def delete_appliance(db: Session, appliance_id:int):
    db_appliance = db.query(models.Appliance).filter(models.Appliance.id == appliance_id).first()
    if not db_appliance:
        raise HTTPException(status_code=404, detail="Appliance not found")
    db.delete(db_appliance)
    db.commit()
    return None

def get_optimized_consumption(db: Session, total_expected_consumption: float):
    pass