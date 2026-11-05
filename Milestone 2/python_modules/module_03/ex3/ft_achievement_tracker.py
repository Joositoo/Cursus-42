import random


def gen_player_achievements() -> set[str]:
    achievements: list[str] = [
        "Crafting Genius", "World Savior", "Master Explorer",
        "Collector Supreme", "Untouchable", "Boss Slayer",
        "Strategist", "Speed Runner", "Survivor",
        "Treasure Hunter", "First Steps", "Sharp Mind",
        "Unstoppable", "Hidden Path Finder",
    ]

    return set(random.sample(achievements, random.randint(6, 12)))


def main() -> None:
    alice_achievements = gen_player_achievements()
    bob_achievements = gen_player_achievements()
    charlie_achievements = gen_player_achievements()
    dylan_achievements = gen_player_achievements()

    all_achievements = (
        alice_achievements.union(bob_achievements)
        .union(charlie_achievements)
        .union(dylan_achievements))

    common_achievements = (
        alice_achievements.intersection(bob_achievements)
        .intersection(charlie_achievements)
        .intersection(dylan_achievements))

    print("=== Achievement Tracker System ===\n")
    print(f"Player Alice: {alice_achievements}")
    print(f"Player Bob: {bob_achievements}")
    print(f"Player Charlie: {charlie_achievements}")
    print(f"Player Dylan: {dylan_achievements}\n")
    print(f"All distinct achievements: {all_achievements}\n")

    print(
        f"Common achievements: {common_achievements}\n")

    others = (
            bob_achievements
            .union(charlie_achievements)
            .union(dylan_achievements)
        )
    print(f"Only Alice has: {alice_achievements.difference(others)}")

    others = (
            alice_achievements
            .union(charlie_achievements)
            .union(dylan_achievements)
        )
    print(f"Only Bob has: {bob_achievements.difference(others)}")

    others = (
            alice_achievements
            .union(bob_achievements)
            .union(dylan_achievements)
        )
    print(f"Only Charlie has: {charlie_achievements.difference(others)}")

    others = (
            alice_achievements
            .union(bob_achievements)
            .union(charlie_achievements)
        )
    print(f"Only Dylan has: {dylan_achievements.difference(others)}\n")

    print(
        f"Alice is missing: "
        f"{all_achievements.difference(alice_achievements)}"
    )
    print(
        f"Bob is missing: "
        f"{all_achievements.difference(bob_achievements)}"
    )
    print(
        f"Charlie is missing: "
        f"{all_achievements.difference(charlie_achievements)}"
    )
    print(
        f"Dylan is missing: "
        f"{all_achievements.difference(dylan_achievements)}"
    )


if __name__ == "__main__":
    main()
