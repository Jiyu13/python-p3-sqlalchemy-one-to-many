from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

# country - cities
# Parent - children
# manager - employees


# one
class Customer(Base):

    __tablename__ = "customers"
    id = Column(Integer(), primary_key=True)
    # one get backref from many
    orders = relationship("order", backref="customer")



# many
class Order(Base):

    __tablename__ = "orders"
    id = Column(Integer(), primary_key=True)
    # ForeignKey column, constrains and join customer and order models
    customer_id = Column(Integer(), ForeignKey("customers.id"))