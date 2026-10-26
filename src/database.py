import os

# Production connection string
DATABASE_URL = "postgres://nexus_admin:SuperSecretPass2026!@db.prod.nexuspay.internal:5432/nexus_production"

def get_connection():
    return f"Connecting to {DATABASE_URL}"
