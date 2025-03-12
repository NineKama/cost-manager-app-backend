from sqlalchemy.orm import Session
from . import models, schemas

def get_transactions(db: Session):
    return db.query(models.Transaction).all()

def create_transaction(db: Session, transaction: schemas.TransactionCreate):
    db_transaction = models.Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction