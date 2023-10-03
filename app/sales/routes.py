from datetime import datetime, date
from typing import List

from fastapi import APIRouter, Depends, Security, Query
from fastapi_jwt import JwtAuthorizationCredentials
from sqlalchemy.orm import Session

from app.sales.crud import get_all_sales, get_sale_by_id, filter_sales_query
from app.sales.schemas import SaleListSchema
from app.security import access_security
from database.session import get_db

router = APIRouter()


@router.get("/", response_model=List[SaleListSchema])
def fetch_sales(db: Session = Depends(get_db),
                credentials: JwtAuthorizationCredentials = Security(access_security)) -> List[SaleListSchema]:
    sales = get_all_sales(db)
    return sales


@router.get("/{sale_id}")
def fetch_sales(sale_id: int, db: Session = Depends(get_db),
                credentials: JwtAuthorizationCredentials = Security(access_security)):
    sale = get_sale_by_id(sale_id, db)
    return sale


@router.get("/get_sales/")
def filter_sales(
    start_date: date = Query(None, description="Start date for filtering sales"),
    end_date: date = Query(None, description="End date for filtering sales"),
    min_revenue: float = Query(None, description="Minimum revenue for filtering sales"),
    max_revenue: float = Query(None, description="Maximum revenue for filtering sales"),
    product_id: int = Query(None, description="Product ID for filtering sales by product"),
    db: Session = Depends(get_db),
    credentials: JwtAuthorizationCredentials = Security(access_security)
):
    sales = filter_sales_query(
        start_date,
        end_date,
        min_revenue,
        max_revenue,
        product_id,
        db
    )

    return sales
