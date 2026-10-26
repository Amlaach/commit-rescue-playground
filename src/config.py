import os

ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
PORT = int(os.getenv("PORT", "8000"))
