import sys


def command_quest() -> None:
    i = 1

    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    if len(sys.argv) < 2:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(sys.argv) - 1}")
        while i < len(sys.argv):
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1

    print(f"Total arguments: {len(sys.argv)}\n")


if __name__ == "__main__":
    command_quest()
