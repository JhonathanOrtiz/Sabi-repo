from .base import Base
from sqlalchemy import Column, String, Integer

class DefaultProducts(Base):

    __tablename__ = 'products_default'

    product_id = Column(Integer, primary_key=True)
    product = Column(String(255))
    owner = Column(String(255))

    def __repr__(self):
        return f"<DefaulProduct {self.product_id}, {self.product}>"

class FullDescribedProducts(Base):

    __tablename__ = 'full_described_product'

    described_product_id = Column(Integer, primary_key=True)
    category = Column(String(255))
    brand = Column(String(255))
    product = Column(String(255))
    sub_category = Column(String(255))
    description = Column(String(255))
    synonymous = Column(String(255))
    owner = Column(String(255))

    def __repr__(self):
        return f"<FullDescribedProduct {self.described_product_id}, {self.product} from {self.owner}>"

class LastProduct(Base):

    __tablename__ = 'last_product'

    last_product_id = Column(Integer, primary_key=True)
    number = Column(Integer)


