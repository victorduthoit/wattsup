from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas, crud, database

app = FastAPI()

@app.post("/appliances", response_model=schemas.ApplianceResponse)
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

@app.put("/appliances/{appliance_id}", response_model=schemas.ApplianceResponse)
def update_appliance(appliance_id: int, appliance: schemas.ApplianceCreate, db: Session = Depends(database.get_db)):
    return crud.update_appliance(db=db, appliance_id=appliance_id, appliance=appliance)

@app.delete("/appliances/{appliance_id}", response_model=schemas.MinEnergyConsumption, status_code=204):
def delete_appliance(appliance_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_appliance(db=db, appliance_id=appliance_id)

@app.get("/optimized/consumption/{total_expected_consumption}", response_mode=schemas.OptimizedEnergyConsumption)
def compute_energy_consumption(total_expected_consumption: float, db: Session = Depends(database.get_db)):
    return crud.get_optimized_consumption(db=db, total_expected_consumption=total_expected_consumption)