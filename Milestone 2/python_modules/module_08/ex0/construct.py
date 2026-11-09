import sys
import os
import site


def show_info() -> None:
    paths: list[str] = site.getsitepackages()    

    if sys.prefix != sys.base_prefix:
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}\n")
        print("SUCCESS: You're in an isolated environment!")
        print(
            "Safe to install packages without "
            "affecting the global system.\n"
        )
        print("Package installation path:")
        print(paths[0])
    else:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("Global package location:")
        print(paths[0])
        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")


def main() -> None:
    show_info()


if __name__ == "__main__":
    main()
