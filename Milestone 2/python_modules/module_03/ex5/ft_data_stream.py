import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
            "run", "eat", "sleep", "grab", "move",
            "climb", "swim", "release", "use"
        ]

    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
        events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index = random.randint(0, len(events) - 1)
        selected = events[index]

        new_list = []
        for i in range(len(events)):
            if i != index:
                new_list += [events[i]]
        events[:] = new_list

        yield selected


def main() -> None:
    print(("=== Game Data Stream Processor ==="))

    events = gen_event()
    for i in range(1000):
        name, action = next(events)
        print(f"Event {i}: Player {name} did action {action}")

    events_for_list = gen_event()
    list_of_tuples = []
    for i in range(10):
        list_of_tuples += [next(events_for_list)]
    print(f"Built list of 10 events: {list_of_tuples}")

    for event in consume_event(list_of_tuples):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {list_of_tuples}")


if __name__ == "__main__":
    main()
