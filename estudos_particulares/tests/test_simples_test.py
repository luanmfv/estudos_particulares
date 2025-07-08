def my_function(x: int) -> int:
    return x * 2

def test_my_function_returns_double_the_input():
    actual_result = my_function(x=5)

    assert actual_result == 10
