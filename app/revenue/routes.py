from datetime import date, timedelta

from fastapi import APIRouter, Query, Depends

from sqlalchemy.orm import Session
from database.session import get_db

router = APIRouter()


@router.get("/revenue/daily")
def analyze_daily_revenue(
        start_date: date = Query(None, description="Start date for analyzing daily revenue"),
        end_date: date = Query(None, description="End date for analyzing daily revenue"),
        db: Session = Depends(get_db)
):
    if not start_date or not end_date:
        return {"error": "Both start_date and end_date are required for daily analysis."}

    daily_revenue = calculate_revenue(db, start_date, end_date)
    return {"daily_revenue": daily_revenue}


@router.get("/revenue/weekly")
def analyze_weekly_revenue(
        start_date: date = Query(None, description="Start date for analyzing weekly revenue"),
        end_date: date = Query(None, description="End date for analyzing weekly revenue"),
        db: Session = Depends(get_db)
):
    if not start_date or not end_date:
        return {"error": "Both start_date and end_date are required for weekly analysis."}

    end_of_week = end_date + timedelta(days=(6 - end_date.weekday()))

    weekly_revenue = calculate_revenue(db, start_date, end_of_week)
    return {"weekly_revenue": weekly_revenue}


@router.get("/revenue/monthly")
def analyze_monthly_revenue(
        start_date: date = Query(None, description="Start date for analyzing monthly revenue"),
        end_date: date = Query(None, description="End date for analyzing monthly revenue"),
        db: Session = Depends(get_db)
):
    if not start_date or not end_date:
        return {"error": "Both start_date and end_date are required for monthly analysis."}

    end_of_month = end_date.replace(day=1) + timedelta(days=-1)

    monthly_revenue = calculate_revenue(db, start_date, end_of_month)
    return {"monthly_revenue": monthly_revenue}


@router.get("/revenue/annual")
def analyze_annual_revenue(
        start_date: date = Query(None, description="Start date for analyzing annual revenue"),
        end_date: date = Query(None, description="End date for analyzing annual revenue"),
        db: Session = Depends(get_db)
):
    if not start_date or not end_date:
        return {"error": "Both start_date and end_date are required for annual analysis."}

    start_of_year = end_date.replace(month=1, day=1)
    end_of_year = end_date.replace(month=12, day=31)

    annual_revenue = calculate_revenue(db, start_of_year, end_of_year)
    return {"annual_revenue": annual_revenue}
