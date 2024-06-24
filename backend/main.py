from fastapi import FastAPI, Depends, HTTPException
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import schemas, crud, database
from initialize_data import initialize_category_data


app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Initialize the data
with SessionLocal() as db:
    initialize_category_data(db)


@app.post("/appliances", response_model=schemas.ApplianceCreateResponse)
def create_appliance(appliance: schemas.ApplianceCreate, db: Session = Depends(database.get_db)):
    return crud.create_appliance(db=db, appliance=appliance)

@app.get("/appliances/{appliance_id}", response_model=schemas.Appliance)
def read_appliance(appliance_id: int, db: Session = Depends(database.get_db)):
    db_appliance = crud.get_appliance(db, appliance_id=appliance_id)
    if db_appliance is None:
        raise HTTPException(status_code=404, detail="Appliance not found")
    return db_appliance

@app.get("/appliances", response_model=list[schemas.Appliance])
def read_appliances(db: Session = Depends(database.get_db)):
    return crud.get_appliances(db=db)

@app.put("/appliances/{appliance_id}", response_model=schemas.ApplianceCreateResponse)
def update_appliance(appliance_id: int, appliance: schemas.ApplianceCreate, db: Session = Depends(database.get_db)):
    return crud.update_appliance(db=db, appliance_id=appliance_id, appliance=appliance)

@app.delete("/appliances/{appliance_id}", response_model=schemas.ApplianceDeleteResponse)
def delete_appliance(appliance_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_appliance(db=db, appliance_id=appliance_id)

@app.get("/categories/{category_id}", response_model=schemas.Category)
def read_category(category_id: int, db: Session = Depends(database.get_db)):
    db_category = crud.get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="category not found")
    return db_category

@app.get("/categories", response_model=list[schemas.Category])
def read_categories(db: Session = Depends(database.get_db)):
    return crud.get_categories(db=db)

@app.get("/optimized/consumption/{total_expected_consumption}", response_model=schemas.OptimizedEnergyConsumption)
def compute_energy_consumption(total_expected_consumption: float, db: Session = Depends(database.get_db)):
    return crud.get_optimized_consumption(db=db, total_expected_consumption=total_expected_consumption)