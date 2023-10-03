def format_sales(sales):
    sales_data = []
    for sale in sales:
        sales_data.append(
            {
                "id": sale.id,
                "sale_date": sale.created_at.strftime("%d-%m-%Y"),
                "products": [
                    {
                        "id": sale_product.product.id,
                        "name": sale_product.product.name,
                        "quantity": sale_product.quantity,
                        "price": sale_product.product.price
                    }
                    for sale_product in sale.sales_products
                ],
                "revenues": [
                    {
                        "id": revenue.id,
                        "amount": revenue.amount
                    }
                    for revenue in sale.revenues
                ]
            }
        )
    return sales_data
