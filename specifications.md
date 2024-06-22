# Functional Specifications
- **SPEC 1**: The user shall be able to define appliances of the household 

- **SPEC 1.1**: Appliances shall be defined by: name, category and capacity (in W).

- **SPEC 2**: The user shall be able to give its email

- **SPEC 3**: The user shall be able to define the target daily total consumption of the appliances

- **SPEC 3.1**: The user shall be notitifed if the total connsumption defined is:
  - higher than 75kWh 
  - inferior to the minimum consumption possible given **SPEC 5.X**

- **SPEC 4**: Given total consumption and appliances defined in **SPEC 1** and **SPEC 3**, the application shall determine the daily consumption of each appliance and the resulting total consumption name "total optimized consumption".
- **SPEC 5**: Consumption of appliances defined by **SPEC 4** shall comply with all the specifications **SPEC 5.X**
- **SPEC 5.1**: the total optimized consumption shall be inferior to the total consumption defined by the user
- **SPEC 5.2**: For each category X of appliances, the total duration ON of the appliances of the category X shall be among a set defined by the following table:
    | category | acceptable time |
    |:--------:|:---------------:|
    | F        | {6h, 7h, 8h}    |
    | A        | {1h, 2h, 3h, 4h}|
    | L        | {4h to 24h}     |

- **SPEC 5.3**: For each category X of appliances, all the appliances of category X shall the same amount of duration ON during the day
- **SPEC 6**: The total optimized consumption shall correspond to the one closest to the total consumption defined by the user while complying with **SPEC 5.X**
- **SPEC 7**: The application shall display
  - the total optimized connsumption
  - the consumption of each appliances in kWh
  - the consumption of each appliances in percent respect to total optimized consumption


