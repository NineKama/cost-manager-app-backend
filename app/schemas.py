from pydantic import BaseModel
from datetime import date

class TransactionBase(BaseModel):
    title: str
    price: float
    category: str
    date: date

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int

    class Config:
        orm_mode = True
