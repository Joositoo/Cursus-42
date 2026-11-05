def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)

    if 0 <= temp_int and temp_int <= 40:
        return temp_int
    elif temp_int < 0:
        raise ValueError(f"{temp_int}°C is too cold for plants (min 0°C)")
    else:
        raise ValueError(f"{temp_int}°C is too hot for plants (max 40°C)")


def test_temperature() -> None:
    temp_str = ["25", "abc", "100", "-50"]

    print("=== Garden Temperature Checker ===\n")

    for temp in temp_str:
        try:
            print(f"Input data is '{temp}'")
            print(f"Temperature is now {input_temperature(temp)}°C\n")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
