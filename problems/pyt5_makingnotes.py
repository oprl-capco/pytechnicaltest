# PYT5 - Making Notes

# Given two strings, a note and a magazine page
# Determine if you can make the note using only the words on the magazine page

# The note and magazine will be requested as multiple query parameters,
# a JSON response body should be returned as shown:

# Example 1:

# Input:
# note - the quick fox
# magazine - the quick brown fox

# Output:
# {"canMakeNote": "True"}

# Example 2:

# Input:
# note - the quick brown fox
# magazine - the quick fox

# Output:
# {"canMakeNote": "False"}

# Your code must pass the unit test


from fastapi import FastAPI

app = FastAPI()


@app.get("/exercise/")
async def ransom_note(note: str, mag: str):
    pass
