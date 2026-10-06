# Mini Order Sync API

A FastAPI-based application to receive order webhooks, process and persist orders, and synchronize them with external ERP systems.

## Project Structure

```text
mini-order-sync-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── security.py
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   └── models/
│   │       ├── __init__.py
│   │       └── order.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── order.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes/
│   │       ├── __init__.py
│   │       ├── webhooks.py
│   │       └── orders.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── order_service.py
│   │   └── erp_service.py
│   │
│   └── workers/
│       ├── __init__.py
│       └── sync_worker.py
│
├── tests/
│   ├── __init__.py
│   ├── test_validation.py
│   └── test_retry.py
│
├── alembic/
├── .env
├── .env.example
├── .gitignore
├── alembic.ini
├── pyproject.toml
└── README.md
```
