# Quera Cashing Project

This project implements a Restful API for a cash management 
system using Django and Django Rest Framework.
The system empowers users to effectively manage their cash flow by offering 
features for transaction creation, updating, balance tracking,
and report generation.

## Features

- ### User Authentication:
  - Users can register and authenticate using a username and password.
  - Only authenticated users have access to the API endpoints.
- ### Transaction Management:
  - Create, retrieve, update, and delete transactions.
  - Filter and sort transactions based on different criteria (e.g., date, category).
- ### Balance Tracking:
  - The system automatically tracks the user's balance based on transactions.
  - Balance updates dynamically whenever a new transaction is created or updated.
- ### Report generation:
  - Users can generate reports to analyze their cash flow for any range of time.

- ### Testing:
  - Develop comprehensive unit tests and integration tests.
  - Follow best practices for testing, including creating test cases for different scenarios.
- ### Dockerization
- Dockerize the application for easy deployment and portability.
- warning: Due to the sanctions imposed on Iran, dockerization may not work properly.


## Getting Started

These instructions will help you set up the project on your local machine for development purposes.

### Prerequisites

- Python (version 3.10)
- Django (version 4.2.7)
- Django Rest Framework (version 3.14.0)
- ...



### Installation

1. Clone the repository:

```bash
   git clone https://github.com/your-username/safahan.git
   cd safahan
  ```
2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or
.\venv\Scripts\activate  # Windows
```


3. Install the project dependencies:

```bash
pip install -r requirements.txt
```
4. Apply database migrations:

```bash
python manage.py migrate
```


5. Run the development server:


```bash
python manage.py migrate
```
The application should now be accessible at `http://localhost:8000/`.


```