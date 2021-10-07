# Your answers in snippets2.py must pass these tests
# Do not modify the unit tests

import snippets2


def test_snip6():
    user = snippets2.User("admin", "manager")
    assert snippets2.snip6(user) is True
    assert snippets2.snip6(None) is False


def test_snip7():
    assert snippets2.snip7() == [2, 4, 6, 8]