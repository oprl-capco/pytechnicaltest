# PYT1 - Greeting

# Implement a REST API that takes in 'name' as a request parameter,
# then returns a JSON response body as shown: "{"greeting": "Hello, {name}!"}

# Your code must pass the unit test in tests/test_pyt1_greeting


from fastapi import FastAPI

app = FastAPI()

# Write your code below this line


@app.get("/exercise/{name}")
async def greeting(name):
    pass
