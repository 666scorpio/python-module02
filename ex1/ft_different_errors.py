def garden_operations():
    int("abc")
    7 / 0
    open("missing.txt")
    {}["scorpio"]

def test_error_types():
    operations = [
            lambda: int("abc"),
            lambda: 7 / 0,
            lambda: open("missing.txt"),
            lambda: {}["scorpio"]
    ]

    for op in operations:
        try:
            op()
        except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError) as error:
            print(error)

test_error_types()

