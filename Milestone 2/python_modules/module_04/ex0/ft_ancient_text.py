import sys
import typing


def ancient_text() -> None:
    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Usage: ft_ancient_text.py <file>\n")
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")

        file: typing.IO[str] | None = None
        try:
            file = open(sys.argv[1], 'r', encoding="utf-8")
            print("---\n")

            print(file.read())

            print(f"\n---\nFile '{sys.argv[1]}' closed.")
        except FileNotFoundError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}\n")
        except PermissionError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}\n")
        except OSError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}\n")
        finally:
            if file is not None:
                file.close()


if __name__ == "__main__":
    ancient_text()
