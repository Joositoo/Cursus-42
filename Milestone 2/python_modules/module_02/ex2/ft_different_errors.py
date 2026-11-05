def garden_operations(operation_number: int) -> None:
    match operation_number:
        case 0:
            int("abc")
        case 1:
            42 / 0
        case 2:
            open("/non/existent/file")
        case 3:
            "The perfect number is " + 42
        case _:
            return


def test_error_types() -> None:
    numbers = [0, 1, 2, 3, 4]

    print("=== Garden Error Types Demo ===")

    for n in numbers:
        print(f"Testing operation {n}...")
        try:
            garden_operations(n)
        except (
                ValueError,
                ZeroDivisionError,
                FileNotFoundError,
                TypeError
                ) as e:
            print(f"Caught {e.__class__.__name__}: {e}")
        else:
            print("Operation completed successfully")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
