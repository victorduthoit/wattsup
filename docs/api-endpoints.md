# Index
<!-- vscode-markdown-toc -->
* 1. [Resources](#1-resources)
* 2. [API Endpoints](#2-api-endpoints)
  * 2.1. [Appliances Management](#AppliancesManagement)
    * 2.1.1. [Create Appliance](#CreateAppliance)
    * 2.1.2. [Get Appliance](#GetAppliance)
    * 2.1.3. [Update Appliance](#UpdateAppliance)
    * 2.1.4. [Delete Appliance](#DeleteAppliance)
    * 2.1.5. [List Appliances](#ListAppliances)
  * 2.2. [household total energy optimisation](#householdtotalenergyoptimisation)
    * 2.2.1. [Get Optimized Consumption](#GetOptimizedConsumption)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

## 1. <a name='Resources'></a> Resources
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
  - possible_duration_operating
  - miminum_duration_operaring

## 2. <a name='APIEndPoint'></a> API Endpoints
Endpoints to handle CRUD operations on resources and computations:

###  1. <a name='AppliancesManagement'></a>Appliances Management

####  1.1. <a name='CreateAppliance'></a>Create Appliance
**Endpoint**: `POST /appliances`
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
    "id": 1,
    "name": "freezer",
    "power": "2500",
    "usagePattern": "F"
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

####  1.2. <a name='GetAppliance'></a>Get Appliance

**Endpoint**: `GET /appliances/{id}`
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

####  1.3. <a name='UpdateAppliance'></a>Update Appliance

**Endpoint**: `PUT /appliances/{id}`
**Description**: Updates an existing appliance.
**Request Body**:
```
{
    "id": 1,
    "name": "freezer",
    "power": "2500",
    "usagePattern": "F"
}
```
**Response**: Similar to Create Appliance.

####  1.4. <a name='DeleteAppliance'></a>Delete Appliance

**Endpoint**: `DELETE /appliances/{id}`
**Description**: Deletes an appliance by ID.
**Response**: 204 No Content

####  1.5. <a name='ListAppliances'></a>List Appliances

**Endpoint**: `GET /appliances`
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

###  2. <a name='householdtotalenergyoptimisation'></a>household total energy optimisation

####  2.1. <a name='GetOptimizedConsumption'></a>Get Optimized Consumption

**Endpoint**: `GET /optimized/consumption/{total_expected_consumption}`
**Description**: Calculates the optimized consumption for the household.
**Response**:
```
{
    "appliances" : [...] // similar to list appliances
    "total_energy_abs": 34.5  // in kilowatt-hours (kWh)
    "total_energy_rel": 0.9623 // in percent relative to the expected total consumption
}
```


####  2.1. <a name='GetMinEnergy'></a>Get Optimized Consumption

**Endpoint**: `GET /min/energy`
**Description**: Calculates the optimized consumption for the household.
**Response**:
```
30123
```
