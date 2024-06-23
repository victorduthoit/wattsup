from sqlalchemy.orm import Session
import models

def initialize_category_data(db: Session):
    # Check if the table is empty
    if not db.query(models.Category).first():
        db.add_all([
            models.Category(id="F", possible_duration=[6, 7, 8,], minimum_duration=6, power_appliances=0),
            models.Category(id="A", possible_duration=[1, 2, 3, 4,], minimum_duration=1, power_appliances=0),
            models.Category(id="L", possible_duration=list(range(4, 25)), minimum_duration=6, power_appliances=0),
        ])
        db.commit() 