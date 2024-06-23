from pydantic import BaseModel
from enum import Enum

VALID_CATEGORY = ["L", "F", "A"]

class CategoryName(str, Enum):
    """
    Names of appliance category
    """
    f: str = "F"
    l: str = "L"
    a: str = "A"

class ApplianceBase(BaseModel):
    name: str
    category: CategoryName
    power: float

class ApplianceCreate(ApplianceBase):
    pass

class Appliance(ApplianceBase):
    id: int
    duration: float | None
    consumption: float | None

class ApplianceMinEnergyConsumption(BaseModel):
    appliance: Appliance
    minimum_total_energy: float

class MinEnergyConsumption(BaseModel):
    minimum_total_energy: float

class OptimizedEnergyConsumption(BaseModel):
    appliances: list[Appliance]
    total_energy_abs: float
    total_energy_rel: float