# PYT1 - Greeting

# Implement a REST API that takes in 'name' as a request parameter,
# then returns a JSON response body as shown: "{"greeting": "Hello, {name}!"}

# Your code must pass the unit test


from fastapi import FastAPI

app = FastAPI()


@app.get("/exercise/{name}")
async def greeting_should_be(name):
    # Write code here
    pass
