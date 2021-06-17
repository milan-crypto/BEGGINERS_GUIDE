# Unit Tests

# This tests specific methods and logic in the code. This is the most granular type of test.
# The goal is to verify the the internal flow of the method, as well as make sure edge cases are being handled.

def func():
    return 1


def test_func():
    assert func() == 1


# Feature Tests

# This tests the functionality of the component.
# A collection of unit tests may or may not represent a feature test.
# The goal is to verify the component meets the requirements given for it.
# If you're thinking in terms of a work item, this would be testing a ticket as a whole.

class NewEndpoint:
    def on_get(req, resp):
        resp.body = "Hello World"

def test_new_endpoint():
    result = simulate_get("/newendpoint")
    assert result.body = "Hello World"


# Integration Tests

# This tests the entire application, end to end.
# The goal is to guarantee the stability of the application.
# When new code is added, integration tests should still pass with minimal effort.

class MySystem:
    external_system = ExternalSystemConnector()

    def handle_message(message):
        try:
            external_system.send_message(message)
            return True
        catch
        Exception as err:
        return False


def test_MySystem():
    system = MySystem()
    assert system.handle_message(good_message)
    assert not system.handle_message(bad_message)


# Performance Tests

# This tests the efficiency of a piece of code.
# The size of the code being tested can range from a method to the whole application.

import timeit

def func(i):
    return i * 2

def test_performance():
    assert 1 > timeit.timeit("[func(x) for x in range(20)]", number=5,
                              setup="from __main__ import func")