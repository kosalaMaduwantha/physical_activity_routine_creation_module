# Diebtrek backend application

This project is a Flask application that demonstrates the use of the hexagonal architecture pattern. The application provides features for physical activity prediction, routine management. It includes a REST API for interacting with the application.

## Project Structure

The project has the following structure:

- `app/`: This directory contains the main application code.
  - `main.py`: This is the entry point of the Flask application.
  - `adapters/`: This directory contains the adapters for requests and responses.
    - `db/`: Contains database adapters.
    - `rest/`: Contains REST API adapters.
  - `domain/`: This directory contains the domain models and services of the application.
    - `api/`: Contains API-related domain models.
    - `services/`: Contains the business logic of the application.
    - `spi/`: Contains service provider interfaces.
  - `infrastructure/`: This directory contains the infrastructure code, including the database setup and repository.
- `tests/`: This directory contains the tests for the application.
- `config.py`: This file contains the configuration for the application.
- `requirements.txt`: This file lists all the Python dependencies that the project needs.

## Domain Features

The application includes the following domain features:

- **Physical Activity Prediction**: Predicts physical activities based on user data.
- **Routine Management**: Manages physical activity routines for users.
- **Machine Learning Model**: Uses a machine learning model to predict physical activities.
- **Physical Activity Routine**: Generates a physical activity routine using optimization problem solving method for users based on their data.
- 
## Hexagonal Architecture

Hexagonal architecture, also known as ports and adapters architecture, is an architectural pattern used to create loosely coupled application components that can be easily connected to their software environment by means of ports and adapters. The core idea is to isolate the business logic from the external world.

### Layers

1. **Domain Layer**: Contains the business logic and domain models.
2. **Application Layer**: Contains the application services that orchestrate the business logic.
3. **Adapters Layer**: Contains the adapters for interacting with external systems (e.g., databases, REST APIs).
4. **Infrastructure Layer**: Contains the infrastructure code, such as database setup and repositories.

## API Documentation

### Endpoints

#### Create Resource

- **URL**: `/api/resource`
- **Method**: `POST`
- **Request Body**: JSON object representing the resource data.
- **Response**: JSON object representing the created resource.
- **Status Codes**:
  - `201 Created`: Resource created successfully.
  - `400 Bad Request`: Invalid request data.

#### Get Resource

- **URL**: `/api/resource/<int:resource_id>`
- **Method**: `GET`
- **Response**: JSON object representing the resource.
- **Status Codes**:
  - `200 OK`: Resource retrieved successfully.
  - `404 Not Found`: Resource not found.

#### Predict Physical Activities

- **URL**: `/api/v1/physical_act_prediction`
- **Method**: `POST`
- **Request Body**: JSON object representing the user data.
- **Response**: JSON object representing the predicted physical activities.
- **Status Codes**:
  - `201 Created`: Prediction successful.
  - `500 Internal Server Error`: Prediction failed.

#### Get Physical Activities Routine Per Day

- **URL**: `/api/v1/physical_act_routine_per_day`
- **Method**: `POST`
- **Request Body**: JSON object representing the user data.
- **Response**: JSON object representing the physical activities routine per day.
- **Status Codes**:
  - `201 Created`: Routine retrieval successful.
  - `500 Internal Server Error`: Routine retrieval failed.

## Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/hexagonal-flask-app.git
```

2. Navigate to the project directory:

```bash
cd hexagonal-flask-app
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

To run the application, use the following command:

```bash
python app/main.py
```

The application will start running at `http://localhost:5000`.

## Running the Tests

To run the tests, use the following command:

```bash
python -m unittest discover tests
```

### Note: The documentation is incomplete and still in progress. 

