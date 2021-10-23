from re import DEBUG
from flask import Flask, abort, render_template, request
from mock_data import mock_data
import json

app = Flask(__name__) #two umderscore(double) (magic methods,functions,variables)
coupon_codes=[
    {
        "code":"qwerty",
        "discount":10
    }
]


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


@app.route("/about/email")
def email():
    return me["email"]

@app.route("/about/address")
def address():
    return me["address"]["street"]+" " + me["address"]["city"]

@app.route("/test")
def simple_test():
    return "Hello There"




    ########################################################
    ############## API Methods
    ########################################################


@app.route("/api/catalog") #method by default is get
def get_catalog():
    #returns the catalog as JSON string
    return json.dumps(mock_data)


@app.route("/api/catalog", methods=["post"])
def save_product():
    # get request paylaod
    #import request
    product=request.get_json()

    #data validation
    #1 title exists and is longer than 5 charactors
    #validate that the title exists in the dictionary, if nor abort 400
    if not "title" in product or len(product["title"])<5:
        return abort(400, "Title is required and should contain at least five charactors")
        #400=bad request

    #validate price exists and is above zero
    if not 'price' in product:
            return abort(400, "Price is required")

    if not isinstance(product["price"], float) and not isinstance(product["price"],int):
        return abort(400, "Price should a valid number")

    if product['price'] <= 0:
        return abort(400,"Price should be greater than 0")


         #save the product
    mock_data.append(product)

    product["_id"]= len(product["title"])
    
    #return the saved product
    return json.dumps(product)
    


    return "testing"

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

    
##################################################################
##################Coupon Codes####################################
##################################################################

#POST to /api/couponCodes
@app.route("/api/couponCodes", methods=["post"])
def save_coupon():
    couponCode=request.get_json()
    
    #validations

    #save
    coupon_codes.append(couponCode)
    couponCode["_id"]=couponCode["code"]
    return json.dumps(couponCode)



#GET to /api/couponCodes
@app.route("/api/couponCodes")
def get_coupon_codes():
    return json.dumps(coupon_codes)


#get coupon by its code
@app.route("/api/couponCodes/<code>")
def get_coupon(code):
    for coupon in coupon_codes:
        if code==coupon["code"]:
            return json.dumps(coupon)

    return abort(404)

#start the server
#debug true will restart the server on manipulation
app.run(debug=True)