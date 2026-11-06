def secure_archive(
        filename: str,
        action: str = "r",
        content: str = "") -> tuple[bool, str]:
    if action not in ["r", "w"]:
        return (False, "Invalid action. Use 'r' for read or 'w' for write.")

    if action == "r":
        try:
            with open(filename, action, encoding="utf-8") as file:
                text = file.read()
        except FileNotFoundError as e:
            return (False, f"{e}")
        except PermissionError as e:
            return (False, f"{e}")
        except OSError as e:
            return (False, f"{e}")
        return (True, text)
    else:
        try:
            with open(filename, action, encoding="utf-8") as file:
                file.write(content)
            return (True, "Content successfully written to file")
        except PermissionError as e:
            return (False, f"{e}")
        except OSError as e:
            return (False, f"{e}")


def main() -> None:
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(f"{secure_archive('non_existent_file.txt')}\n")

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(f"{secure_archive('innaccessible.txt')}\n")

    print("Using 'secure_archive' to read from a regular file:")
    print(f"{secure_archive('regular_file.txt')}\n")

    print("Using 'secure_archive' to write previous content to a new file:")
    print(
        f"{secure_archive('test.txt', 'w', 'Written content by the script.')}"
        "\n"
    )


if __name__ == "__main__":
    main()
