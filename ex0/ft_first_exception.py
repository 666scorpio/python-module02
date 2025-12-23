def check_temperature(temp_str):
    try:
        temp = int(temp_str)
    except ValueError:
        return f"Error: '{temp_str}' is not a valid number"

    if temp < 0:
        return f"Error: {temp}°C is too cold for plants (min 0°C)"
    elif temp > 40:
        return f"Error: {temp}°C is too hot for plants (max 40°C)"
    else:
        return temp


def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    temps = ["25", "abc", "100", "-50"]
    for temp in temps:
        print(f"\nTesting temperature: {temp}")
        result = check_temperature(temp)
        if isinstance(result, int):
            print(f"Temperature {result}°C is perfect for plants!")
        else:
            print(result)
    print("All tests completed - program didn't crash!")


test_temperature_input()
