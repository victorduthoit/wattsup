from sqlalchemy.orm import Session
import pandas as pd

from wattsup import models, crud, schemas

TEST_DATA_APPLIANCES_V1 = "/mnt/test_data/appliances_1.csv"
SCHEMA_CSV = {
    "name": str,
    "category": str,
    "power": float
}

def initialize_test_appliances_data(db: Session):
    """
    Add appliances defined in appliance test data

    Args:
        db (Session): database in which appliances should be loaded
    """
    # Check if the table is empty
    if not db.query(models.Appliance).first():
        df = pd.read_csv(TEST_DATA_APPLIANCES_V1, usecols=SCHEMA_CSV.keys(), dtype=SCHEMA_CSV)
        for appliance in df.to_dict(orient="records"):
            crud.create_appliance(db=db, appliance=schemas.ApplianceBase(**appliance))