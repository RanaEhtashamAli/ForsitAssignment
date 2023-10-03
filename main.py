import sys
from inspect import getsourcefile
from os import path
from dotenv import dotenv_values

from fastapi import FastAPI
current_dir = path.dirname(path.abspath(getsourcefile(lambda: 0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
from app.user.routes import router as user_routes
from app.products.routes import router as product_routes
from app.sales.routes import router as sale_routes
from app.revenue.routes import router as revenue_routes

app = FastAPI()

config = dotenv_values(".env")


app.include_router(user_routes, prefix="/user", tags=["user"])
app.include_router(product_routes, prefix="/product", tags=["product"])
app.include_router(sale_routes, prefix="/sale", tags=["sale"])
app.include_router(revenue_routes, prefix="/revenue", tags=["revenue"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
