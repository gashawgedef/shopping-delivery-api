from sqlalchemy import create_engine, true
from sqlalchemy.orm import declarative_base,sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/shopping_delivery"
engine=create_engine('postgresql://postgres:postgres@localhost/shopping_delivery',echo=True)
Base=declarative_base()
Sessiion=sessionmaker()