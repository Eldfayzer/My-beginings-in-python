import requests
with open("dataset_24476_3.txt","r",encoding="utf-8") as f:
    lst=[int(x) for  x in f.readlines()]
    for num in lst:
        
        site = f"http://numbersapi.com/{num}/math"
        params = {
        
            "json" : "true"
        }

        res = requests.get(site,params)
        if res.json()["found"]:
            print("Interesting")
        else:
            print("Boring")
#This code accepts a list of numbers from a file .txt in the form: 1 number on 1 line and outputs "Interesting" if there is some interesting fact about this number and "Boring" if not.