from fastapi import FastAPI 
from models.product import Product

data = [
    Product(id=1, name="Tenis Nike Air", description="Calçados", price=199.99),
    Product(id=2, name="Jaqueta Adidas", description="Roupa", price=159.99),
    Product(id=3, name="Camiseta Puma", description="Roupa", price=129.99),
    Product(id=4, name="Sapato Reebok", description="Calçados", price=179.99),
    Product(id=5, name="Bolsa Nike", description="Acessório", price=89.99),
    Product(id=6, name="Chinelo Vans", description="Roupa", price=119.99),
    Product(id=7, name="Shorts Puma", description="Roupa", price=99.99),
    Product(id=8, name="Mochila Reebok", description="Acessório", price=69.99),
]

app = FastAPI()

@app.get("/")
def say_hello():
    return {"FastAPI": "Hello, World!"}

@app.get("/api/products")
def get_produtcs():
    return data


#@app.get("/{name}")
#def say_hi(name: str ):
#    return {"Hello": name}