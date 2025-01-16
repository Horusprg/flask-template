# Flask Template

A complete Flask template to quickly start the development of scalable and well-organized web applications.

## Features
- Ready-to-use Docker configuration.
- Modular and well-organized file structure.
- Support for unit testing with `pytest`.
- Separate configurations for development and production environments.
- Easy dependency management with `requirements.txt`.
- Predefined example route and controller.

## Project Structure
```
flask_template/
|-- service/
|   |-- app/
|       |-- __init__.py        # Application initialization
|       |-- routes/            # Routes definitions
|       |-- models/            # Model definitions
|       |-- utils/             # Utility functions
|       |-- templates/         # HTML files (template rendering)
|       |-- static/            # Static files (CSS, JS, images)
|   |-- tests/
|       |-- test_app.py            # Unit tests
|-- Dockerfile                 # Docker configuration
|-- docker-compose.yml         # Docker services configuration
|-- requirements.txt           # Project dependencies
|-- config.py                  # Project configurations
|-- run.py                     # Application entry point (development)
```

## Setup and Execution

### Requirements
Make sure you have the following installed:
- Docker and Docker Compose
- Python 3.11 or higher

### How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/flask-template.git
   cd flask-template
   ```

#### Using Docker
2. Start the application using Docker:
   ```bash
   docker-compose up --build -d
   ```

3. Access the application in your browser at [http://localhost](http://localhost).

#### Python Debugger
2. Set up the virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Run the run.py:
   ```bash
   python run.py
   ```

4. Access the application in your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000) or [http://{your-ip-address}](http://{your-ip-address}).

## Running Tests
1. Ensure dependencies are installed:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the tests:
   ```bash
   pytest
   ```

## Contributions
Contributions are welcome! Feel free to open issues or submit pull requests.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

