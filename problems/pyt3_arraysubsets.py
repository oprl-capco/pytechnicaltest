# PYT3 - Array Subsets

# Given an array a1 and a array a2 from a query parameter
# Identify whether a2 is a subset of a1
# Your output should be in the form of a JSON response body:
# {"isSubset" : "True"}

# Example 1:

# Input:
# a1 = [3, 4, 1, 5, 2]
# a2 = [3, 2, 5]

# Output:
# {"isSubset" : "True"}

# Example 2:

# Input:
# a1 = [3, 4, 1, 5, 2]
# a2 = [3, 8, 5]

# Output:
# {"isSubset" : "False"}

# Your code must pass the unit tests in tests/test_pyt3_arraysubsets.py


from fastapi import FastAPI

app = FastAPI()

# Write your code below this line


@app.get("/exercise/{a1}/{a2}")
async def array_subsets(a1, a2):
    a1 = list(map(int, a1.split(",")))
    a2 = list(map(int, a2.split(",")))

    # Do not change the two lines above
