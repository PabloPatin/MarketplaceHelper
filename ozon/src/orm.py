from sqlalchemy import Integer, String
from sqlalchemy.orm import MappedAsDataclass, DeclarativeBase, mapped_column, Mapped


class Base(MappedAsDataclass, DeclarativeBase):
    """subclasses will be converted to dataclasses"""


class Product(Base):
    __tablename__ = 'product'
    id: Mapped[int] = mapped_column(Integer,init=False, primary_key=True, autoincrement=True)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    name: Mapped[str] = mapped_column(String(length=64), default='Unnamed')


if __name__ == '__main__':
    x = Product(name='lol', price=190)
    print(x)