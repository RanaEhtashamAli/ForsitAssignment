import sys
from contextlib import contextmanager
import random
from inspect import getsourcefile
from os import path

import click
current_dir = path.dirname(path.abspath(getsourcefile(lambda: 0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])

from app.products.models import Product, Inventory, InventoryHistory
from app.revenue.models import Revenue
from app.sales.models import Sale, SalesProduct
from database.session import get_db


@click.command()
def populate_db():
    with contextmanager(get_db)() as session:
        try:
            products = [
                Product(
                    name=f"Product {i}",
                    description=f"Description {i}",
                    price=random.uniform(1.0, 100.0)
                )
                for i in range(1, 201)
            ]
            session.add_all(products)

            sales = [Sale() for _ in range(1, 201)]
            session.add_all(sales)

            sales_products = []
            for sale in sales:
                for _ in range(1, 21):
                    product = random.choice(products)
                    quantity = random.randint(1, 10)
                    sales_product = SalesProduct(sale=sale, product=product, quantity=quantity)
                    sales_products.append(sales_product)
            session.add_all(sales_products)

            revenues = [Revenue(sale=sale) for sale in sales]
            session.add_all(revenues)

            inventories = [Inventory(product=product, quantity=random.randint(1, 100)) for product in products]
            session.add_all(inventories)

            inventory_histories = []
            for i in range(200):
                product = random.choice(products)
                quantity_change = random.randint(1, 10)
                current_quantity = random.randint(1, 100)
                new_quantity = current_quantity + quantity_change

                history_record = InventoryHistory(
                    product=product,
                    quantity_change=quantity_change,
                    new_quantity=new_quantity
                )

                inventory_histories.append(history_record)
            session.add_all(inventory_histories)

            session.commit()

            print("Data populated successfully.")
        # except Exception as e:
        #     print(f"Error: {e}")
        finally:
            session.close()

if __name__ == '__main__':
    populate_db()
