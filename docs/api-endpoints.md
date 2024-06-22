<!-- vscode-markdown-toc -->
* 1. [2.1. Appliances Management](#AppliancesManagement)
	* 1.1. [2.1.1. Create Appliance](#CreateAppliance)
	* 1.2. [2.1.2. 2.1.2 Get Appliance](#GetAppliance)
	* 1.3. [2.1.3. 2.1.3 Update Appliance](#UpdateAppliance)
	* 1.4. [2.1.4. 2.1.4 Delete Appliance](#DeleteAppliance)
	* 1.5. [2.1.5. List Appliances](#ListAppliances)
* 2. [2.2. household total energy optimisation](#householdtotalenergyoptimisation)
	* 2.1. [2.2.1. 2.2.1 Get Optimized Consumption](#GetOptimizedConsumption)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->
# 1. Resources
Main resources that the API manage:
- Appliance: Represents an individual household appliance with properties:
  - name
  - category
  - power
  - consumption, *optional*
  - duration, *optional*
- User: Represents a user of the application with properties
  - email
- Category: Represents groups of appliances with properties:
  - name
  - possible duration operating
  - miminum duration operaring

# 2. API Endpoints
Endpoints to handle CRUD operations on resources and computations:

##  1. <a name='AppliancesManagement'></a>2.1. Appliances Management

###  1.1. <a name='CreateAppliance'></a>2.1.1. Create Appliance
**Endpoint**: `POST /api/v1/appliances`
**Description**: Adds a new appliance.
**Request Body**:
```
{
  "name": "freezer",
  "power": 2500,
  "category": "F"
}
```

**Response**:
- 201 created:
```
{
    "appliance": {
        "name": "freezer",
        "power": "2500",
        "usagePattern": "F"
    }
    "minimum_total_consumption": 7500
}
```
- 422 unprocessable entity
```
{
  "detail": [
    {
      "loc": ["body", "category"],
      "msg": "Invalid category: E. Valid patterns: ['F', 'L', 'A']",
      "type": "value_error"
    }
  ]
}
``` 

###  1.2. <a name='GetAppliance'></a>2.1.2. 2.1.2 Get Appliance

**Endpoint**: `GET /api/v1/appliances/{id}`
**Description**: Retrieves a specific appliance by ID.
**Response**:
```
{
  "id": 0,
  "name": "freezer",
  "power": "2500",
  "category": "F",
  "consumption": none,
  "duration": none,
}
```

###  1.3. <a name='UpdateAppliance'></a>2.1.3. 2.1.3 Update Appliance

**Endpoint**: `PUT /api/v1/appliances/{id}`
**Description**: Updates an existing appliance.
**Request Body**:
```
{
    "appliance": {
        "name": "freezer",
        "power": "3000",
        "usagePattern": "F"
    }
    "minimum_total_consumption": 9000
}
```
**Response**: Similar to Create Appliance.

###  1.4. <a name='DeleteAppliance'></a>2.1.4. 2.1.4 Delete Appliance

**Endpoint**: `DELETE /api/v1/appliances/{id}`
**Description**: Deletes an appliance by ID.
**Response**: 204 No Content
```
{
    "minimum_total_consumption": 4000
}
```
###  1.5. <a name='ListAppliances'></a>2.1.5. List Appliances

**Endpoint**: `GET /api/v1/appliances`
**Description**: Lists all appliances.
**Response**:
```
[
  {
    "id": 0,
    "name": freezer,
    "power": 3000,
    "category": "F",
    "consumption": 4500
    "duration": 1.5 
  },
  {
    "id": 0,
    "name": fridge,
    "power": 2000,
    "category": "F",
    "consumption": 3000
    "duration": 1.5 
  },
]
```

##  2. <a name='householdtotalenergyoptimisation'></a>2.2. household total energy optimisation

###  2.1. <a name='GetOptimizedConsumption'></a>2.2.1. 2.2.1 Get Optimized Consumption

**Endpoint**: `GET /api/v1/households/consumption/optimized/{total_expected_consumption}`
**Description**: Calculates the optimized consumption for the household.
**Response**:
```
{
    "appliances" : [...] // similar to list appliances
    "total_optimized_consumption_abs": 34.5  // in kilowatt-hours (kWh)
    "total_optimized_consumption_rel": 0.9623 // in percent relative to the expected total consumption
}
```
