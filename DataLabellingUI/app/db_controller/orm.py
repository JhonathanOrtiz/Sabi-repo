from .tables import DefaultProducts, FullDescribedProducts, LastProduct
from .base import Base, engine, Session
from sqlalchemy import func

Base.metadata.create_all(engine)
session = Session()

def update_last_product(number):
    session.query(LastProduct).filter(LastProduct.number == number).update({LastProduct.number: number + 1})
    session.commit()
    return get_most_recent_default_product()
  
def get_last_product():
    current_last_product = session.query(LastProduct).filter(LastProduct.last_product_id == 1).first()
    if current_last_product == None:
        last_product = LastProduct(last_product_id=1, number=1)
        session.add(last_product)
        session.commit()
        return get_last_product()
    return {"product_id": current_last_product.number }

# Obtener el producto mostrado
def get_most_recent_default_product():
    current_id = get_last_product()['product_id']
    current_default_product = session.query(DefaultProducts).filter(DefaultProducts.product_id==current_id).first()
    return {"product_id": current_default_product.product_id,
            "product": current_default_product.product,
            "owner": current_default_product.owner}

def _delete_default_product(product_id):
    try:
        session.query(DefaultProducts).filter(DefaultProducts.product_id==product_id).delete()
        session.commit()
        return {"status": "OK"}
    except:
        return {"status": "failure"}

def get_full_described_product_dict(product, category, brand, 
                                    sub_category, synonymous, 
                                    owner, description):
    return {
        "product": product,
        "category": category,
        "brand": brand,
        "sub_category": sub_category,
        "synonymous": synonymous,
        "description": description,
        "owner": owner
    }    

def add_full_described_product(full_described_product_dict):
    try:
        fd_product = FullDescribedProducts(**full_described_product_dict)
        session.add(fd_product)
        session.commit()
        return {"status": "OK"}
    except:
        return {"status": "failure"}

# Confirmar
def full_product_transformation(default_product_dict, full_described_product_dict):
    status = add_full_described_product(full_described_product_dict)
    if status['status'] == "OK":
        current_product_id = default_product_dict['product_id']
        _delete_default_product(current_product_id)
        update_last_product(current_product_id)
        return {"status": "OK"}
    else:
        return {"status": "failure"}

# Saltar
def pass_product_transformation(default_product_dict):
    serial_number = default_product_dict["product_id"]
    return update_last_product(serial_number)





