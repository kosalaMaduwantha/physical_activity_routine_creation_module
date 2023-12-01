# Hexagonal Flask Application

This is a sample project that demonstrates how to implement a hexagonal architecture in a Flask application. The application includes database operations.

## Project Structure

The project has the following structure:

- `app/`: This directory contains the main application code.
- `app/main.py`: This is the entry point of the Flask application.
- `app/adapters/`: This directory contains the adapters for requests and responses.
- `app/domain/`: This directory contains the domain models of the application.
- `app/services/`: This directory contains the business logic of the application.
- `app/infrastructure/`: This directory contains the infrastructure code, including the database setup and repository.
- `tests/`: This directory contains the tests for the application.
- `config.py`: This file contains the configuration for the application.
- `requirements.txt`: This file lists all the Python dependencies that the project needs.

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
python -m unittest tests/test_app.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)