# WattsUp

## Content
Small applications to get to know the consumption of appliances of an household.

## Roadmap

Division of stages of the development:

- [x] specs: [functional specifications](./docs/specifications.md)
- [x] design
  - [x] UX: [use case](./docs/xp-use-case.png)
  - [x] UI: [mockup](./docs/frontend-mockup.png)
  - [x] data: [data model](./docs/datamodel.png)
  - [x] backend endpoints: [endpoint documentation](./docs/api-endpoints.md)
  - [x] optimisation docs: [optimisation pipeline](./docs/optimisation.md) 

- [x] development
  - [x] backend poc
  - [x] backend mvp
  - [x] create dummy backend states:
  - [x] front structure
  - [x] front api calls
  - [x] front final touch

- [ ] containerize
  - [x] dev
  - [ ] production (To test)
- [ ] deployment test
- [ ] user guide
  - [ ] 
- [ ] software quality
  - [ ] validation 
  - [ ] unit test

## Technology stack :

- Backend:
  - **API: fastapi** Small benchmark shows that it is easy to setup and easy to get started with
  - **DB: sqlite** easy to setup and appropriate for small projects
  - **ORM: sqlalchemy** from tutorial

- Frontend:
  - html/css/javascript (basic, easy to get started with)
  - chart.js for plots

## Code structure:
```
└── WattsUp/
    ├── backend/
    │   ├── .devcontainer        # container settings for development
    │   ├── wattsup/
    │   │   ├── data_ingestion   # module to ingest data directly (without API)
    │   │   ├── crud.py          # Create, Read, Update, Delete methods
    │   │   ├── database.py      # management of db
    │   │   ├── main.py          # entry script for fastapi
    │   │   ├── models.py        # definition of tables of db and their records
    │   │   ├── schemas.py       # validation schemas for api
    │   │   └── optimiser.py     # all computation of indicators
    │   ├── dockerfile           # backend docker file
    │   └── requirements.txt     # python library requirements for backend
    ├── frontend/
    │   ├── app.js               # dynamic of frontend and api calls
    │   ├── index.html           # statuc structure of fronted 
    │   └── style.css            # style of fronted
    └── docs                     # all project related doc
```

## User manual

1. clone repo: `git clone https://github.com/victorduthoit/wattsup.git`
2. open the project in vscode and launch devcontainer `ctr+maj+p -> Open folder in container`. Select `./backend`. Take a long time if first time image is created.
3. run `fastapi dev backend/wattsup/main.py`. A backend server is launched in local on port 8000
4. open the front on a live server: right click on `frontend/index.html` + `Open with Live Server`

### Prerequisite

### installation

### Usage

Example of data:
| Appliance       | Category | Power |
|:---------------:|:--------:|:-----:|
| Fridge          | F        | 2000  |
| Freezer         | F        | 2500  |
| Washing machine | A        | 1500  |
| Dishwasher      | A        | 2500  |
| Induction stove | A        | 3000  |
| TV              | L        |  500  |
| Small light     | L        |  100  |
| Big light       | L        |  800  |

## Project organisation

