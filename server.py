from re import DEBUG
from flask import Flask, abort, render_template
from mock_data import mock_data
import json

app = Flask(__name__) #two umderscore(double) (magic methods,functions,variables)

me = {
    "firstname":"Shane",
    "lastname":"Dixon",
    "email":"shanedixon13@gmail.com",
    "age":"25",
    "hobbies":[],
    "address":{
        "street":"Bradley Ln.",
        "city":"Lonoke"
    }

}


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    #return the full name 
    return render_template("about.html")




    ########################################################
    ############## API Methods
    ########################################################


@app.route("/api/catalog")
def get_catalog():
    #returns the catalog as JSON string
    return json.dumps(mock_data)


## /api/categories
#return the list (string) of unique catagories
@app.route("/api/categories")
def get_categories():
    categories=[]
    for product in mock_data:
        if  product["category"] not in categories:
            categories.append(product["category"])
    return json.dumps(categories)


@app.route("/api/product/<id>")
def get_product(id):
    for product in mock_data:
        if product["_id"] == id:
         return json.dumps(product)
        
    return abort(404)#not found


@app.route("/api/catalog/<category>")
def get_category(category):
    products=[]
    for product in mock_data:
        if category.lower() == product["category"].lower():
            products.append(product)
    return json.dumps(products)



    #cheapest product
@app.route("/api/cheapest")
def get_cheapest():
    cheapest=mock_data[0]
    for product in mock_data:
        if product["price"] < cheapest["price"]:
            cheapest=product
    return json.dumps(cheapest)

    



@app.route("/about/email")
def email():
    return me["email"]

@app.route("/about/address")
def address():
    return me["address"]["street"]+" " + me["address"]["city"]

@app.route("/test")
def simple_test():
    return "Hello There"



#start the server
#debug true will restart the server on manipulation
app.run(debug=True)