import  pandas as pd
import numpy as np

Data = [

    {"name" : "sunny", "age": 28, "city": "bhopal"},
    {"name" : "abhi", "age": 27, "city": "delhi"},
    {"name" : "ram", "age": 48, "city": "pune"},
    {"name" : "shyam", "age": 38, "city": "banglore"},
    {"name" : "mohan", "age": 32, "city": "banglore"}
]

Data = pd.DataFrame(Data)

Data.to_csv("data/data.csv", index=False)