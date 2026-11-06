import typing
import abc


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self.count: int = -1
        self.dict: dict[int, str] = {}

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        ...

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        for key in self.dict:
            first_key = key
            first_data = self.dict[key]
            break
        self.dict.pop(first_key)
        return first_key, first_data


class NumericProcessor(DataProcessor):
    def ingest(self, data: int | float | list[int | float]) -> None:
        if self.validate(data):
            print(f"Processing data: {data}")
            if isinstance(data, int | float):
                self.count += 1
                self.dict[self.count] = str(data)
            elif isinstance(data, list):
                for i in data:
                    self.count += 1
                    self.dict[self.count] = str(i)
        else:
            raise ValueError("Improper numeric data")

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, int | float):
            return True
        elif isinstance(data, list):
            for i in data:
                if not isinstance(i, int | float):
                    return False
            return True
        return False


class TextProcessor(DataProcessor):
    def ingest(self, data: str | list[str]) -> None:
        if self.validate(data):
            print(f"Processing data: {data}")
            if isinstance(data, str):
                self.count += 1
                self.dict[self.count] = data
            elif isinstance(data, list):
                for i in data:
                    self.count += 1
                    self.dict[self.count] = str(i)
        else:
            raise Exception("Invalid data")

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            for i in data:
                if not isinstance(i, str):
                    return False
            return True
        return False


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            for k in data.keys():
                if not isinstance(k, str):
                    return False
            for v in data.values():
                if not isinstance(v, str):
                    return False
            return True
        elif isinstance(data, list):
            for i in data:
                if not isinstance(i, dict):
                    return False
                for k in i.keys():
                    if not isinstance(k, str):
                        return False
                for v in i.values():
                    if not isinstance(v, str):
                        return False
            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if self.validate(data):
            print(f"Processing data: {data}")
            if isinstance(data, dict):
                self.count += 1
                message = ": ".join(data.values())
                self.dict[self.count] = message
            else:
                for log in data:
                    self.count += 1
                    message = ": ".join(log.values())
                    self.dict[self.count] = message

        else:
            raise Exception("Invalid data")


def numeric_procesor_tests() -> None:
    numeric_processor = NumericProcessor()

    print("Testing Numeric Processor...")
    print(f"Trying to validate input '42': {numeric_processor.validate(42)}")
    print(
        f"Trying to validate input 'Hello': "
        f"{numeric_processor.validate('Hello')}"
        )

    try:
        string = "foo"
        numeric_processor.ingest(string)
    except ValueError as e:
        print(
            f"Test invalid ingestion of string '{string}' "
            f"without prior validation:\nGot exception: {e}"
        )

    numeric_processor.ingest([1, 2, 3, 4, 5])

    print("Extracting 3 values...")
    i = 0
    while i < 3:
        key, value = numeric_processor.output()
        print(f"Numeric value {key}: {value}")
        i += 1


def text_processor_tests() -> None:
    text_processor = TextProcessor()

    print("\nTesting Text Processor...")
    print(f"Trying to validate input '42': {text_processor.validate(42)}")
    text_processor.ingest(["Hello", "Nexus", "World"])
    print("Extracting 1 value...")
    key, value = text_processor.output()
    print(f"Text value {key}: {value}")


def log_processor_tests() -> None:
    log_processor = LogProcessor()

    print("\nTesting Log Processor...")
    print(
        f"Trying to validate input 'Hello': "
        f"{log_processor.validate('Hello')}"
    )

    logs = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    log_processor.ingest(logs)

    print("Extracting 2 values...")
    i = 0
    while i < 2:
        key, value = log_processor.output()
        print(f"Log entry {key}: {value}")
        i += 1


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")
    numeric_procesor_tests()
    text_processor_tests()
    log_processor_tests()


if __name__ == "__main__":
    main()
