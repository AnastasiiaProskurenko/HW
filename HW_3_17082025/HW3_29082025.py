from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DECIMAL, Boolean
from sqlalchemy.orm import registry, sessionmaker, declarative_base, relationship

Base = declarative_base()
engine = create_engine('sqlite:///my_database.db')

Session = sessionmaker(bind=engine)
session = Session()
Register = registry()

class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(DECIMAL(10,2), nullable=False)
    in_stock = Column(Boolean)
    category_id = Column(Integer,ForeignKey('category.id'))

    category = relationship("Categories", back_populates="products")

class Categories(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True )
    name = Column(String(100), nullable=False)
    description = Column(String(255))

    product = relationship("Products", back_populates="categories")

Base.metadata.create_all(engine)
