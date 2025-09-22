
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DECIMAL, Boolean, func
from sqlalchemy.orm import registry, sessionmaker, declarative_base, relationship

from HW_3_17082025.HW3_29082025 import Categories, Products

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
    category_id = Column(Integer,ForeignKey('categories.id'))

    categories = relationship("Categories", back_populates="products")

class Categories(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True )
    name = Column(String(100), nullable=False)
    description = Column(String(255))

    products = relationship("Products", back_populates="categories")

# Base.metadata.create_all(engine)
#
# session.add_all([
#     Categories(name="Электроника", description="Гаджеты и устройства."),
#     Categories(name="Книги", description="Печатные книги и электронные книги."),
#     Categories(name="Одежда", description="Одежда для мужчин и женщин."),
#                  ])
#
# categories = {c.name: c.id for c in session.query(Categories).all()}
# session.add_all([
#     Products(name="Смартфон", price=299.99, in_stock=True, category_id=categories["Электроника"]),
#     Products(name="Ноутбук", price=499.99, in_stock=True, category_id=categories["Электроника"]),
#     Products(name="Научно-фантастический роман", price=15.99, in_stock=True, category_id=categories["Книги"]),
#     Products(name="Джинсы", price=40.50, in_stock= True, category_id=categories["Одежда"]),
#     Products(name="Футболка", price=20.00, in_stock=True, category_id=categories["Одежда"]),
#
# ])
# session.commit()
"""
Задача 2: Чтение данных
Извлеките все записи из таблицы categories. Для каждой категории извлеките и выведите все связанные с ней продукты, включая их названия и цены.
"""
all_categories_list= session.query(Categories).all()

for c in all_categories_list:
    print(f" В карегории {c.name}:")
    for p in c.products:
        print(f" -- {p.name} : {p.price}")

print("-"*20)
"""
Задача 3: Обновление данных
Найдите в таблице products первый продукт с названием "Смартфон". Замените цену этого продукта на 349.99.
"""
smartphon_update=session.query(Products).filter(Products.name=="Смартфон").first()
if smartphon_update:
    smartphon_update.price=349.99
    session.commit()
    print(f"Цена {smartphon_update.name} выросла до {smartphon_update.price}.")

print("-"*20)

"""
Задача 4: Агрегация и группировка
Используя агрегирующие функции и группировку, подсчитайте общее количество продуктов в каждой категории.
"""
categories_groups=session.query(Categories.name, func.count(Products.id)).join(Products, Categories.id==Products.category_id).group_by(Categories.name).all()
for c in categories_groups:
    print(f" {c[0]} : {c[1]}")
print("-"*20)
"""
Задача 5: Группировка с фильтрацией
Отфильтруйте и выведите только те категории, в которых более одного продукта.
"""
categories_groups=session.query(Categories.name, func.count(Products.id)).join(Products, Categories.id==Products.category_id).group_by(Categories.name).having(func.count(Products.id)>1).all()
for c in categories_groups:
    print(f" {c[0]} : {c[1]}")

print("-"*20)
