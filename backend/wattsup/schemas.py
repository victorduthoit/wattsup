from pydantic import BaseModel
from enum import Enum

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
class ApplianceCreateResponse(Appliance):
    appliance: Appliance

class ApplianceUpdateResponse(ApplianceCreateResponse):
    pass

class OptimizedEnergyConsumption(BaseModel):
    appliances: list[Appliance]
    total_energy_abs: float
    total_energy_rel: float


class Category(BaseModel):
    id: CategoryName
    possible_duration: list[float]
    minimum_duration: float
    power_appliances: float