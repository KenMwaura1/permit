# Hospital System

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Description

A Django project for managing a hospital system using [Permit.io](https://app.permit.io/) for authorization. The project includes a RESTful API for managing patients, doctors, and appointments. The API is secured using ABAC (Attribute-Based Access Control) and RBAC (Role-Based Access Control) policies. The project also includes a PDP (Policy Decision Point) microservice for evaluating access control policies. 

## Features

- ABAC (Attribute-Based Access Control)
- CRUD operations
- RESTful API
- User authentication
- Role-based access control
- ReBAC (Relationship-Based Access Control)

## Installation

1. Clone the repository: `git clone https://github.com/KenMwaura1/permit.git`
2. Cd into the project directory: `cd hsystem`
3. Install the dependencies: `pip install -r requirements.txt`
4. Apply database migrations: `python manage.py migrate` or `python manage.py migrate --run-syncdb` || `python manage.py makemigrations hsystem` || `python manage.py migrate`
5. Start the development server: `python manage.py runserver 5000`

## Run your local PDP Microservice container

If you do not have Docker installed as of yet, click [here](https://docs.docker.com/get-docker/) to install Docker.

### Pull the container 

Run the following command to pull the PDP Microservice container:

```bash
docker pull permitio/pdp-v2:latest
```

### Run the container

Remember to replace <YOUR_API_KEY> with the Secret Key you obtained from your dashboard.

```bash

docker run -it -p 7766:7000 --env PDP_DEBUG=True --env PDP_API_KEY=<YOUR_API_KEY> permitio/pdp-v2:latest

```


## Usage

1. Create a superuser: `python manage.py createsuperuser`
2. Access the admin panel: `http://localhost:5000/admin/`
3. Access the API: `http://localhost:5000/api/`
4. Access the documentation: `http://localhost:5000/docs/` 

## Contributing

Contributions are welcome! Please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

- Author: Kennedy Mwaura

- GitHub: [Your GitHub Profile](https://github.com/KenMwaura1)