import json


data = {
    "user":{
        "name":"Francis",
        "age":27,
        "location":{
            "city":"Manila",
            "country":"Philippines"
        }
    }
}


print(data['user']['location']['city'])