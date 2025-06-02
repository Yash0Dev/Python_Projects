# FastAPI CRUD API

A simple RESTful API built with FastAPI that implements CRUD (Create, Read, Update, Delete) operations for items.

## Features

- Create new items
- Read all items or a specific item
- Update existing items
- Delete items
- Input validation using Pydantic models

## Requirements

- Python 3.7+
- FastAPI
- Pydantic

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install fastapi uvicorn
```

## Running the Application

To run the application, use the following command:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- Interactive API documentation (Swagger UI): `http://localhost:8000/docs`
- Alternative API documentation (ReDoc): `http://localhost:8000/redoc` 