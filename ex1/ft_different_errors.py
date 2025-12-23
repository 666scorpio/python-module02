def garden_operations():
    int("abc")
    7 / 0
    open("missing.txt")
    {}["scorpio"]

def test_error_types():
    operations = {
        "ValueError": lambda: int("abc"),
        "ZeroDivisionError": lambda: 7 / 0,
        "FileNotFoundError": lambda: open("missing.txt"),
        "KeyError": lambda: {}["scorpio"]
    }
    print("=== Garden Error Types Demo ===")
    for name, op in operations.items():
        try:
            print(f"\nTesting {name}...")
            op()
        except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError) as error:
            if name == "ValueError":
                print ("Caught ValueError: invalid literal for int()")
            elif name == "ZeroDivisionError":
                print("Caught ZeroDivisionError: division by zero")
            elif name == "FileNotFoundError":
                print("Caught FileNotFoundError: No such file 'missing.txt'")
            elif name == "KeyError":
                print("Caught KeyError: 'missing\\_plant'")
    print("\nTesting multiple errors together...")
    try:
        int("abc")
        7 / 0
        open("missing.txt")
        {}["scorpio"]
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


test_error_types()
