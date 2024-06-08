import test_integration

def run_pytests():
    result = test_integration.main(["-v", "test_integration.py"])
    return result

if __name__ == "__main__":
    run_pytests()
