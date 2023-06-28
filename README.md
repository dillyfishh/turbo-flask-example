# turbo-flask-example
This is a simple Flask application that demonstrates asynchronous file upload progress updates using Turbo-Flask.

## Features

- Unique session IDs for each user.
- Simulates file upload process with progress updates.
- Progress updates are sent to the client using Turbo-Flask's push functionality.

## Dependencies

- Python 3.6+
- Flask
- Turbo-Flask
- UUID

## Installation

1. Clone this repository:
```
[https://github.com/dillyfishh/PythonFileRenamer.git](https://github.com/dillyfishh/turbo-flask-example.git)
```
2. Install the necessary packages:
```
pip install -r requirements.txt
```
3. Run the application:
```
flask --app main.py
```

## Usage

- Visit the application in your web browser at `http://localhost:5000`.
- Each user is assigned a unique session ID upon visiting the site.
