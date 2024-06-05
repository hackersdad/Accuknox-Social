# My Django Project

This is a Django project containerized using Docker and using MySQL as the database.

## Features

- Django web application
- MySQL database
- Docker containerization

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Docker Compose

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Ensure Docker Daemon is Running (Windows):**

    - Open Docker Desktop and ensure it's running.
    - Or, open `services.msc` and start the `Docker Desktop Service`.

3. **Build the Docker image:**

    ```sh
    docker-compose build
    ```

4. **Run the Docker containers:**

    ```sh
    docker-compose up
    ```

5. **Apply the migrations:**

    ```sh
    docker-compose exec web python manage.py migrate
    ```

6. **Create a superuser (optional):**

    ```sh
    docker-compose exec web python manage.py createsuperuser
    ```

### Accessing the Application

Open your browser and go to `http://localhost:8000` to see your Django application running.

### Author

Avinash Pratap Singh