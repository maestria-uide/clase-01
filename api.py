import json
import requests
from flask import Flask, Response, request

from product import Product

app = Flask(__name__)



@app.route("/buscar")
def buscar():
    argumentos = request.args.get('keywords', '')
    wallapop_url = f"https://api.wallapop.com/api/v3/general/search?keywords={argumentos}%20&category_ids=12900&filters_source=seo_landing&longitude=-3.69196&latitude=40.41956&order_by=closest"

    retorno = requests.get(wallapop_url)
    productos = []
    for producto in retorno.json().get("search_objects"):
        productos.append(Product(title=producto["title"], value=producto["price"], currency=producto["currency"]))

    lista_productos= [p.to_dict() for p in productos]
    lista_serializada= json.dumps(lista_productos)

    return Response(lista_serializada,mimetype="application/json")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
