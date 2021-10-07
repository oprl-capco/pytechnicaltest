# PYT4 - Case Converter

# An application is specified so that a given string can
# be converted from "snake_case" to "CamelCase" and vice versa.

# For example:
# from "this_method"
# to "ThisMethod"

# Or from "ThisMethod"
# to "this_method"

# The client can specify in the query string what method of conversion they want
# and also what word they would like to convert.

# Using this information, complete the "to_camel" and the "to_snake" function.
# The output should be a JSON response body as follows:

# Example 1

# Input: "this_method"
# Output: {"CamelCase": "ThisMethod"}

# Example 2

# Input: "ThisMethod"
# Output: {"snake_case": "this_method"}

# Your code must pass the unit tests in tests/test_pyt4_caseconverter.py


from fastapi import FastAPI

app = FastAPI()

# Write your code below this line


@app.get("/exercise/camel/{word}")
async def to_camel(word: str):
    pass


@app.get("/exercise/snake/{word}")
async def to_snake(word: str):
    pass
