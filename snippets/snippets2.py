# Refactor the following snippets
# Run the test_snippets2 unit tests to ensure your refactored code
# passes the unit tests

# SNIP6

class User:
    def __init__(self, role, manager):
        self.role = role
        self.manager = manager


def snip6(user):
    if user:
        if user.role == "admin":
            if user.manager == "manager":
                return True
            else:
                return False
        else:
            return False
    else:
        return False


# SNIP7


def snip7():
    a1 = [1, 2, 3, 4]
    a2 = []
    for i in range(0, 4):
        x = a1[i] * 2
        a2.append(x)
    return a2
