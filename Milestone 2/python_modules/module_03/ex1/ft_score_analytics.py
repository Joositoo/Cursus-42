import sys


def show_analytics(scores: list[int]) -> None:
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}\n")


def score_analytics() -> None:
    i = 1
    scores: list[int] = []

    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print(
            "No scores provided. Usage: python3 "
            "ft_score_analytics.py <score1> <score2> ...\n"
        )
    else:
        while i < len(sys.argv):
            try:
                scores += [int(sys.argv[i])]
            except ValueError:
                print(f"Invalid parameter: '{sys.argv[i]}'")
            i += 1

        if len(scores) == 0:
            print(
                "No scores provided. Usage: python3 "
                "ft_score_analytics.py <score1> <score2> ..."
            )
        else:
            show_analytics(scores)


if __name__ == "__main__":
    score_analytics()
