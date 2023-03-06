from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

# Email - user account
# Country - capital city
# Order - order data

class Order(Base):

    __tablename__ = "orders"

    id = Column(Integer(), primary_key=True)



class OrderMetadata(Base):

    __tablename__ = "orders_metadata"

    id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey("orders.id"))


    order = relationship("Order", 
        backref=backref("order_metadata", uselist=False))