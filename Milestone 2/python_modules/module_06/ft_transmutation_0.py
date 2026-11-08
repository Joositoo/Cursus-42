import alchemy.transmutation.recipes


def main() -> None:
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recypes.py directly: ")
    print(
        f"Testing lead to gold: "
        f"{alchemy.transmutation.recipes.lead_to_gold()}\n"
    )


if __name__ == "__main__":
    main()
