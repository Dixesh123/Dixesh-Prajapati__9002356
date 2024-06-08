import test
from main import combined_user_operation

def test_combined_user_operation():
    result = combined_user_operation(5, 3, "Deepo", "Mev", 18)
    assert result == (8, "Deepo Mev")

def test_combined_user_operation_with_different_name():
    result = combined_user_operation(10, 20, "Rako", "Charadu", 25)
    assert result == (30, "Rako Charadu")

def test_combined_user_operation_with_empty_name():
    result = combined_user_operation(7, 3, "", "", 50)
    assert result == (12, " ")
