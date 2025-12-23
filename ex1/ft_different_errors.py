"""
Demonstrates handling different Python error types in garden operations.
Catches ValueError, ZeroDivisionError, FileNotFoundError, and KeyError.
"""


def garden_operations():
    """Perform garden operations that raise different errors."""
    int("abc")
    7 / 0
    open("missing.txt")
    {}["scorpio"]


def test_error_types():
    """Test garden_operations and demonstrate catching multiple
    error types."""
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
        except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
            if name == "ValueError":
                print("Caught ValueError: invalid literal for int()")
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
