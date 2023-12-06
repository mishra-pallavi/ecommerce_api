from flask import Blueprint, jsonify

product_bp = Blueprint("product", __name__)

@product_bp.route("/products", methods=["GET"])
def get_products():
    # Logic to retrieve and return products from the database
    products = [{"id": 1, "name": "Product 1"}, {"id": 2, "name": "Product 2"}]
    return jsonify(products)

# Additional routes and controller logic can be added here
