from products import dao


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data: dict) -> "Product":
        return Product(data['id'], data['name'], data['description'], data['cost'], data['qty'])


def list_products() -> list[Product]:
    try:
        products = dao.list_products()
        return [Product.load(product) for product in products]
    except Exception as e:
        print(f"Error listing products: {e}")
        return []


def get_product(product_id: int) -> Product:
    try:
        return Product.load(dao.get_product(product_id))
    except Exception as e:
        print(f"Error fetching product with ID {product_id}: {e}")
        raise


def add_product(product: dict):
    if not all(key in product for key in ['id', 'name', 'description', 'cost', 'qty']):
        raise ValueError("Invalid product data. Missing required fields.")
    try:
        dao.add_product(product)
    except Exception as e:
        print(f"Error adding product: {e}")
        raise


def update_qty(product_id: int, qty: int):
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    try:
        dao.update_qty(product_id, qty)
    except Exception as e:
        print(f"Error updating quantity for product ID {product_id}: {e}")
        raise
