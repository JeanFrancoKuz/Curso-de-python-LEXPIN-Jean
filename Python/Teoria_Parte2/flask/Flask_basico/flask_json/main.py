from flask import Flask, request, jsonify, abort

app = Flask(__name__)

#creemos datos simulados para los productos

products_db = {
    1: {"id": 1, "name": "Laptop", "price": 1200, "category": "Electronics"},
    2: {"id": 2, "name": "Smartphone", "price": 800, "category": "Electronics"},
    3: {"id": 3, "name": "Coffee Maker", "price": 150, "category": "Home Appliances"},
    4: {"id": 4, "name": "Blender", "price": 100, "category": "Home Appliances"},
    5: {"id": 5, "name": "Headphones", "price": 200, "category": "Electronics"},}

@app.route("/api/products/<int:product_id>")
def get_product(product_id):
  product =products_db.get(product_id)
  if product:
    #Si el producto existe, lo devolvemos como JSON
    return jsonify(product)
  else:
    abort(404,description = "Product not found")


if __name__ == '__main__':
    #Ejecutamos nuestra aplicacion
    app.run(debug=True)