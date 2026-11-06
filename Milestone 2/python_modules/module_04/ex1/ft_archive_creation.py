import sys
import typing


def archive_creation() -> None:
    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Usage: ft_archive_creation.py <file>\n")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{sys.argv[1]}'")

        file: typing.IO[str] | None = None
        try:
            file = open(sys.argv[1], 'r', encoding="utf-8")
            print("---\n")

            text = file.read()
            print(text)

            print(f"\n---\nFile '{sys.argv[1]}' closed.\n")

            print("Transform data:\n---\n")
            new_str = ""
            for c in text:
                if c != "\n":
                    new_str += c
                else:
                    new_str += "#\n"
            if (len(new_str) > 0 and new_str[len(new_str) - 1] != "\n"):
                new_str += "#\n"
            print(f"{new_str}\n---")

            try:
                file_name = input("Enter new file name (or empty): ")
            except BaseException:
                print("\nInvalid argument.\nNot saving data.")
                return
            if file_name == "":
                print("Not saving data.")
            else:
                new_file: typing.IO[str] | None = None
                try:
                    print(f"Saving data to '{file_name}'")
                    new_file = open(file_name, "w", encoding="utf-8")
                    new_file.write(new_str)
                    print(f"Data saved in file '{file_name}'\n")
                except PermissionError as e:
                    print(f"Error opening file '{file_name}': {e}")
                    print("Not saving data.")
                except OSError as e:
                    print(f"Error opening file '{file_name}': {e}")
                    print("Not saving data.")
                finally:
                    if new_file is not None:
                        new_file.close()
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
    archive_creation()
