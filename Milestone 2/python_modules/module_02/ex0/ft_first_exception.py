def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    temp_str = ["25", "abc"]

    print("=== Garden Temperature ===\n")

    for temp in temp_str:
        try:
            print(f"Input data is '{temp}'")
            print(f"Temperature is now {input_temperature(temp)}°C\n")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
