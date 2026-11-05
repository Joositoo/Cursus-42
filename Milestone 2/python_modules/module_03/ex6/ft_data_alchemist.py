import random


def data_alchemist() -> None:
    upper = {
        "a": "A", "b": "B", "c": "C", "d": "D", "e": "E",
        "f": "F", "g": "G", "h": "H", "i": "I", "j": "J",
        "k": "K", "l": "L", "m": "M", "n": "N", "o": "O",
        "p": "P", "q": "Q", "r": "R", "s": "S", "t": "T",
        "u": "U", "v": "V", "w": "W", "x": "X", "y": "Y",
        "z": "Z",
    }

    players = [
        'Alice', 'bob', 'Charlie', 'dylan',
        'Emma', 'Gregory', 'john', 'kevin',
        'Liam'
    ]

    all_capitalized_players = [
        upper[p[0]] + p[1:] if p[0] < "A" or p[0] > "Z" else p
        for p in players
    ]

    only_capitalized_players = [
        p for p in players if p[0] >= "A" and p[0] <= "Z"
    ]

    score_dict = {p: random.randint(1, 100) for p in all_capitalized_players}

    scores = [score_dict[p] for p in score_dict]
    average = round((sum(scores) / len(scores)), 2)

    high_scores = {
        p: score_dict[p]
        for p in score_dict
        if score_dict[p] > average
    }

    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {all_capitalized_players}")
    print(f"New list of capitalized names only: {only_capitalized_players}\n")
    print(f"Score dict: {score_dict}")
    print(f"Score average is {average}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    data_alchemist()
