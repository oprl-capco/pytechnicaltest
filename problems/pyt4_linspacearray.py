# PYT4 - Linearly Spaced Arrays

# An array server creates a linearly spaced array according to a client's request.
# This means that the array would return evenly spaced numbers over a specified interval.

# Three parameters would be required to carry this out:

# start - what value must the array start
# stop - what value must the array stop
# size - the size of the array

# So for example, start = 1, stop = 4 and size = 4
# should generate an array as shown:

# [1, 2, 3, 4]

# You must also take into account floating variables
# start = 1, stop = 2 and size = 5

# [1.0, 1.25, 1.5, 1.75, 2.0]

# Using this information, implement the linspace_array function

# Your code must pass the unit tests in tests/test_pyt4_linspacearray.py


from fastapi import FastAPI

app = FastAPI()

# Write your code below this line


@app.get("/exercise/{start}/{stop}/{size}")
async def linspace(start: int, stop: int, size: int):
    pass

