# PYT2 - Name Server

# A simple name server stores a table in the form of a nested dictionary as demonstrated:

# {1: {"firstname" : "", "lastname" : ""},
#  2: {"firstname" : "", "lastname" : ""},
#  3: {"firstname" : "", "lastname" : ""}}

# A unique ID points to a record containing a person's first name and last name.

# The client should be able to perform the following operations on the dictionary:

# 1. A POST request that takes in a request parameter of the first name and last name
# then store it in a data structure. The ID, being the key for each record,
# should be incrementing in ascending order.

# 2. A GET request that should be able to query a user's ID from the dictionary and retrieve the record
# corresponding to the ID from it. An ID that is not present in the name server should return 404 code.

# Given these requirements, implement the name server.

# Your code must pass the unit test in tests/test_pyt2_nameserver

from fastapi import FastAPI, HTTPException

app = FastAPI()

table = {}

# Write your code below this line


@app.post("/exercise/")
def write(firstname: str, lastname: str):
    pass


@app.get("/exercise/{read_id}")
def read(read_id: int):
    pass













