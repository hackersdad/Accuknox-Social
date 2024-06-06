# My Django Project

This is a Django project containerized using Docker and using MySQL as the database.
NOte: Database is not containerised
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

3. **Make DB Up and running on port 3306 with the help of sql file provided :**


4. **Build the Docker image:**

    ```sh
    docker-compose build
    ```

5. **Run the Docker containers:**

    ```sh
    docker-compose up
    ```

### Accessing the Application

Open your browser and go to `http://localhost:8000` to see your Django application running.

### Author

Avinash Pratap Singh