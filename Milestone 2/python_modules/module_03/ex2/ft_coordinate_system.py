import math


def get_distance(
        start: tuple[float, float, float],
        finish: tuple[float, float, float]) -> float:
    x_start, y_start, z_start = start
    x_finish, y_finish, z_finish = finish
    return (
        math.sqrt(
            (x_finish - x_start)**2 +
            (y_finish - y_start)**2 +
            (z_finish - z_start)**2
            )
    )


def get_len(lst: list[str]) -> int:
    i = 0
    for n in lst:
        i += 1
    return i


def get_player_pos() -> tuple[float, float, float]:
    text = ""
    parts: list[str] = []
    current = ""
    valid = False

    while not valid:
        parts = []
        current = ""
        i = 0
        try:
            text = (
                input("Enter new coordinates as floats in format 'x,y,z': ")
            )
            for c in text:
                if c == ",":
                    parts += [current]
                    current = ""
                else:
                    current += c
            parts += [current]
            if get_len(parts) != 3:
                print("Invalid syntax")
            else:
                values: list[float] = []
                while i < get_len(parts):
                    values += [float(parts[i])]
                    i += 1
                valid = True

        except ValueError as e:
            print(f"Error on parameter '{parts[i]}': {e}")
        except BaseException:
            print("\nInput interrupted, please try again")

    return (values[0], values[1], values[2])


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")

    coordinates = get_player_pos()
    x, y, z = coordinates
    print(f"Got a first tuple: {coordinates}")
    print(f"It includes: X={x}, Y={y}, Z={z}")
    print(
        f"Distance to center: "
        f"{round(get_distance(coordinates, (0.0, 0.0, 0.0)), 4)}\n"
    )

    print("Get a second set of coordinates")
    second_coordinates = get_player_pos()
    print(
        f"Distance between the 2 sets of coordinates: "
        f"{round(get_distance(coordinates, second_coordinates), 4)}\n"
    )


if __name__ == "__main__":
    main()
