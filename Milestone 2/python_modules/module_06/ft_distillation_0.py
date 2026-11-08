from alchemy.potions import strength_potion, healing_potion


def main() -> None:
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print(f"Testing strength potion: {strength_potion()}")
    print(f"Testing healing potion: {healing_potion()}\n")


if __name__ == "__main__":
    main()
