# Functional Specifications
- **FUN 1**: The user shall be able to define appliances of the household 

  - **FUN 1.1**: Appliances shall be defined by: name, category and power (in W).
  
  - **FUN 1.2**: Applicances' categories shall be limited to the following: "L", "F", "A"

- **FUN 2**: The user shall be able to give its email

- **FUN 3**: The user shall be able to define the target daily total consumption of the appliances

  - **FUN 3.1**: The user shall be notitifed if the total connsumption defined is:
    - higher than 75kWh 
    - inferior to the minimum consumption possible given **FUN 5.X**

- **FUN 4**: Given total consumption and appliances defined in **FUN 1** and **FUN 3**, the application shall determine the daily consumption of each appliance and the resulting total consumption name "total optimized consumption".
- **FUN 5**: Consumption of appliances defined by **FUN 4** shall comply with all the specifications **FUN 5.X**
  - **FUN 5.1**: the total optimized consumption shall be inferior to the total consumption defined by the user
  - **FUN 5.2**: For each category X of appliances, the total duration ON of the appliances of the category X shall be among a set defined by the following table:
      | category | acceptable time |
      |:--------:|:---------------:|
      | F        | {6h, 7h, 8h}    |
      | A        | {1h, 2h, 3h, 4h}|
      | L        | {4h to 24h}     |

  - **FUN 5.3**: For each category X of appliances, all the appliances of category X shall the same amount of duration ON during the day
- **FUN 6**: The total optimized consumption shall correspond to the one closest to the total consumption defined by the user while complying with **FUN 5.X**
- **FUN 7**: The application shall display
  - the total optimized connsumption
  - the consumption of each appliances in kWh
  - the consumption of each appliances in percent respect to total optimized consumption

# Technical specifications

- **TEC 1**: The cartesian combinations of acceptable time of categories shall be inferior to 1000. As defined in specification **FUN 5.2**, the total number of combinations is $3 \times 4 \times 21 = 252$