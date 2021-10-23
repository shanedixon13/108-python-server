from mock_data import mock_data


me = {
    "firstname":"Shane",
    "lastname":"Dixon",
     "email":"shanedixon13@gmail.com",
    "age":25,
    "hobbies":[],
    "address":{
        "street":"Bradley Ln",
        "city":"Lonoke"
    }

}

print(me["firstname"]+" "+me["lastname"])

print(me["address"]["city"])

#modify existing
me["age"]=26

#create new
me["new"]=1
print(me)




#list
names=[]

names.append("Shane")
names.append("Jake")
names.append("Guillermo")

print(names)

#get elements
print(names[0])
print(names[2])


#for loop
for name in names:  #variable can be named anything
    print(name)


ages = [12,32,456,10,23,678,4356,2,46,789,23,67,13]
#find the youngest
x=ages[0]
for age in ages:
    if age<x:
        x=age
print(x)

#print the title of every product
for item in mock_data:
    print(item["title"])