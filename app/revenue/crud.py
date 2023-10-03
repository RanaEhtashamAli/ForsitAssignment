from datetime import date

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.revenue.models import Revenue
from app.sales.models import Sale


def calculate_revenue(
        db: Session,
        start_date: date,
        end_date: date,
):
    total_revenue = (
            db.query(Revenue)
            .join(Revenue.sale)
            .filter(Sale.sale_date >= start_date)
            .filter(Sale.sale_date <= end_date)
            .with_entities(func.sum(Revenue.amount))
            .scalar() or 0.0
    )
    return total_revenue
