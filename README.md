# E-Cart: A Flask-Based E-Commerce Platform

A simple e-commerce web application built with Flask, created as a Cloud Computing lab exercise. It covers user authentication, product browsing, a shopping cart, and checkout, with built-in performance monitoring and load-testing support.

## Features

- **Authentication** – Sign up and log in using JWT-based session tokens stored in cookies (`auth` module).
- **Product catalog** – Browse products and add new ones via a simple form (`products` module).
- **Shopping cart** – Add, remove, and clear items in a per-user cart (`cart` module).
- **Checkout** – Compute order totals and complete a purchase (`checkout` module).
- **Monitoring** – Integrated with [Flask-MonitoringDashboard](https://github.com/flask-dashboard/Flask-MonitoringDashboard) for request/performance metrics.
- **Load testing** – Includes a [Locust](https://locust.io/) setup for simulating traffic against the app.

## Tech Stack

- **Backend:** Python, Flask
- **Auth:** PyJWT, Flask-Login
- **Database:** SQLite (`auth.db`, `carts.db`, `products.db`)
- **Templates:** Jinja2
- **Monitoring:** Flask-MonitoringDashboard
- **Load Testing:** Locust

## Project Structure

```
CC-Lab3/
├── auth/           # Login and sign-up logic (JWT-based)
├── cart/           # Cart add/remove/get/delete logic
├── checkout/        # Checkout and payment completion logic
├── products/        # Product listing and creation logic
├── templates/        # Jinja2 HTML templates (login, signup, browse, cart, checkout, payment, etc.)
├── locust/           # Locust load-testing scripts
├── insert_product.py # Helper script to seed sample products
├── main.py           # Flask application entry point (routes)
└── requirements.txt   # Python dependencies
```

## Getting Started

### Prerequisites

- Python 3.9+
- pip

### Installation

```bash
git clone https://github.com/sandeepelayath/CC-Lab3.git
cd CC-Lab3
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Running the App

```bash
python main.py
```

The app runs in debug mode by default and will be available at `http://127.0.0.1:5000`.

### Seeding Sample Products (optional)

```bash
python insert_product.py
```

## Application Routes

| Route | Method(s) | Description |
|---|---|---|
| `/` | GET | Redirects to `/browse` |
| `/browse` | GET | Lists all products |
| `/product/<product_id>` | GET | View a single product |
| `/product` | GET, POST | Product creation form / handler |
| `/login` | GET, POST | Login page / authentication |
| `/register` | GET, POST | Sign-up page / account creation |
| `/cart` | GET | View current user's cart |
| `/cart/<id>` | POST | Add a product to the cart |
| `/cart/remove/<id>` | POST | Remove an item from the cart |
| `/cart/delete` | GET | Clear the entire cart |
| `/checkout` | GET, POST | View order total / proceed |
| `/payment` | GET | Complete checkout and show payment confirmation |

Authenticated routes read a JWT from the `token` cookie set at login and redirect to `/login` if it's missing.

## Load Testing

Locust scripts live in the `locust/` directory. With the app running, start Locust with:

```bash
locust -f locust/<your_locustfile>.py --host=http://127.0.0.1:5000
```

Then open `http://localhost:8089` to configure and launch a load test from the Locust web UI.

## Monitoring Dashboard

Flask-MonitoringDashboard is bound to the app automatically (`dashboard.bind(app)`) and stores metrics in `flask_monitoringdashboard.db`. Once the app is running, visit:

```
http://127.0.0.1:5000/dashboard
```

## Notes

- This project uses local SQLite databases for simplicity — no external database setup is required.
- Secrets (such as the JWT signing key) are hardcoded for lab/demo purposes and should be replaced with environment variables before any real-world use.

## License

No license specified. Add one if you intend to share or reuse this code beyond coursework.
