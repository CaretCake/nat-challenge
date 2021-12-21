# OptiChange

A Flask python API backend with a React frontend that lets you calculate the optimal (fewest) number of coins for whatever amount of money you need. Submission for NAT challenge.

- [OptiChange](#optichange)
- [Getting Started](#getting-started)
  - [Install & Setup](#install--setup)
    - [Flask Backend](#flask-backend)
    - [React Frontend](#react-frontend)
  - [Get it Running](#get-it-running)
    - [Flask Backend](#flask-backend-1)
    - [React Frontend](#react-frontend-1)
  - [Test](#test)
    - [Flask Backend](#flask-backend-2)
- [Future Improvements / TODOs](#future-improvements--todos)

# Getting Started

## Install & Setup

### Flask Backend
```
cd nat-challenge
python setup.py install
```

### React Frontend
```
cd nat-challenge/client/optimal-coins
npm install
```

## Get it Running

### Flask Backend
```
cd nat-challenge
python api/routes.py
```

### React Frontend
```
cd nat-challenge/client/optimal-coins
npm start
```

## Test

### Flask Backend
```
cd nat-challenge
python setup.py test
```

# Future Improvements / TODOs
* input validation on dollar amount input to React form
* display error message to user when api call fails/returns 400