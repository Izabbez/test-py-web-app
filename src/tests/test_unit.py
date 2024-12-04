# test_unit.py
def add_numbers(a, b):
    return a + b

def test_add_numbers():
    result = add_numbers(2, 3)
    assert result == 5, f"Expected 5, but got {result}"
    print("Test passed: add_numbers(2, 3) returned 5 as expected.")

    result = add_numbers(-1, 1)
    assert result == 0, f"Expected 0, but got {result}"
    print("Test passed: add_numbers(-1, 1) returned 0 as expected.")


