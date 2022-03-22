import json
import requests
from flask import Flask, Response, request

from ingredients import Ingredients
from country import Country
from game import Game
from product import Product
from users import Users
from books import Books
from post import Post

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

    return Response(lista_serializada, mimetype="application/json")
@app.route("/getuser")
def getuser():
    wallapop_url2 =f"https://jsonplaceholder.typicode.com/users"
    retorno = requests.get(wallapop_url2)
    usuarios = []
    for usuario in retorno.json():
        usuarios.append(Users(name=usuario["name"], username=usuario["username"], email=usuario["email"]))
    print("usuario")
    lista_usuarios= [u.to_dictr() for u in usuarios]
    lista_serializadausuario = json.dumps(lista_usuarios)

    return Response(lista_serializadausuario, mimetype="application/json")

@app.route("/getcountry")
def getcountry():
    wallapop_url3 =f"https://restcountries.com/v3.1/all"
    retorno = requests.get(wallapop_url3)
    paises = []
    for pais in retorno.json():
        p = pais["name"]
        paises.append(Country(name=p["common"]))
    print("pais")
    lista_paises= [a.to_dictr() for a in paises]
    lista_serializadapais = json.dumps(lista_paises)

    return Response(lista_serializadapais, mimetype="application/json")

@app.route("/getgames")
def getgames():
    wallapop_url4 = f"https://www.freetogame.com/api/games"
    retorno = requests.get(wallapop_url4)
    games = []
    for game in retorno.json():
        games.append(Game(title=game["title"]))
    print("games")
    lista_games= [a.to_dictr() for a in games]
    lista_serializadagames = json.dumps(lista_games)

    return Response(lista_serializadagames, mimetype="application/json")


@app.route("/getingredients")
def getingredients():
    wallapop_url5 = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?f=a"
    retorno = requests.get(wallapop_url5)
    ingredients = []
    for ingredient in retorno.json().get("drinks"):
        ingredients.append(Ingredients(strCategory=ingredient["strCategory"]))
    lista_ingredients= [a.to_dictr() for a in ingredients]
    lista_serializadaingredients = json.dumps(lista_ingredients)

    return Response(lista_serializadaingredients, mimetype="application/json")


@app.route("/getbooks")
def getbooks():
    wallapop_url6 =f"https://jsonplaceholder.typicode.com/todos/"
    retorno = requests.get(wallapop_url6)
    libros = []
    for libro in retorno.json():
        libros.append(Books(title=libro["title"]))
    lista_libros= [a.to_dictr() for a in libros]
    lista_serializadalibro = json.dumps(lista_libros)

    return Response(lista_serializadalibro, mimetype="application/json")

@app.route("/getpost")
def getpost():
    wallapop_url7 =f"https://jsonplaceholder.typicode.com/posts"
    retorno = requests.get(wallapop_url7)
    posts = []
    for post in retorno.json():
        posts.append(Post(title=post["title"],body=post["body"]))
    lista_posts= [a.to_dictr() for a in posts]
    lista_serializadapost = json.dumps(lista_posts)

    return Response(lista_serializadapost, mimetype="application/json")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
