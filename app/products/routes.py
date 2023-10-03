from typing import List

from fastapi import APIRouter, Depends, Security, HTTPException
from fastapi_jwt import JwtAuthorizationCredentials
from sqlalchemy.orm import Session

from app.products.crud import get_all_products, get_product_by_id, create_inventory_history
from app.products.schemas import ProductListSchema, ProductQuantityUpdateIn, ProductInventoryHistoryListSchema
from app.security import access_security
from database.session import get_db

router = APIRouter()


@router.get("/", response_model=List[ProductListSchema])
def fetch_products(db: Session = Depends(get_db),
              credentials: JwtAuthorizationCredentials = Security(access_security)) -> List[ProductListSchema]:
    products = get_all_products(db)
    return products


@router.post("/update-inventory/{product_id}/")
def update_product_inventory(product_id, product_data: ProductQuantityUpdateIn, db: Session = Depends(get_db),
              credentials: JwtAuthorizationCredentials = Security(access_security)):
    product = get_product_by_id(product_id, db)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found.")
    create_inventory_history(product_id, product.inventory.quantity, product_data.quantity_to_add, db)
    product.inventory.quantity += product_data.quantity_to_add

    db.commit()
    return {"message": "Product quantity updated."}


@router.post("/inventory-history/{product_id}/", response_model=List[ProductInventoryHistoryListSchema])
def get_inventory_history(product_id, db: Session = Depends(get_db),
              credentials: JwtAuthorizationCredentials = Security(access_security)) -> List[ProductInventoryHistoryListSchema]:
    product = get_product_by_id(product_id, db)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found.")
    product_history = product.inventory_history
    history_response = [ProductInventoryHistoryListSchema(product_name=history.product.name,
                                                          quantity_change=history.quantity_change,
                                                          new_quantity=history.new_quantity)
                        for history in product_history]

    return history_response
