import typing
import abc


class DataProcessor(abc.ABC):
    def __init__(self, name: str) -> None:
        self.name = name
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


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class DataStream:
    def __init__(self) -> None:
        self.proc_list: list[DataProcessor] = []
        print("Initialize Data Stream...")

    def register_processor(self, proc: DataProcessor) -> None:
        self.proc_list.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        if len(self.proc_list) == 0 or len(stream) == 0:
            return
        for item in stream:
            processed = False
            for proc in self.proc_list:
                if proc.validate(item):
                    proc.ingest(item)
                    processed = True
                    break

            if not processed:
                print(
                    f"DataStream error - "
                    f"Can't process element in stream: {item}"
                )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.proc_list:
            exported_data: list[tuple[int, str]] = []

            i = 0
            while i < nb:
                if len(proc.dict) == 0:
                    break

                exported_data.append(proc.output())
                i += 1

            if len(exported_data) > 0:
                plugin.process_output(exported_data)

    def print_processor_statistics(self) -> None:
        print("\n=== DataStream Statistics ===")
        if len(self.proc_list) == 0:
            print("No processor found, no data")
            return

        for proc in self.proc_list:
            print(
                f"{proc.name}: total {proc.count + 1} "
                f"items processed, remaining {len(proc.dict)} on processor")


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values: list[str] = []

        for _, value in data:
            values.append(value)

        print("CSV Output:")
        print(",".join(values))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        lines: list[str] = []

        for key, value in data:
            lines.append(f'"item_{key}": "{value}"')

        print("JSON Output: ")
        print("{" + ", ".join(lines) + "}")


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===\n")

    data_stream = DataStream()
    data_stream.print_processor_statistics()

    batch_of_data: list[typing.Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING", "log_message":
                "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]

    second_batch: list[typing.Any] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {"log_level": "NOTICE", "log_message":
                "Certificate expires in 10 days"},
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print("\nRegistering Processors\n")
    numeric_processor = NumericProcessor("Numeric Processor")
    text_processor = TextProcessor("Text Processor")
    log_processor = LogProcessor("Log Processor")
    data_stream.register_processor(numeric_processor)
    data_stream.register_processor(text_processor)
    data_stream.register_processor(log_processor)

    print(f"Send first batch of data on stream: {batch_of_data}")
    data_stream. process_stream(batch_of_data)
    data_stream.print_processor_statistics()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    data_stream.output_pipeline(3, CSVExportPlugin())
    data_stream.print_processor_statistics()

    print(f"\nSend another batch of data: {second_batch}")
    data_stream.process_stream(second_batch)
    data_stream.print_processor_statistics()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    data_stream.output_pipeline(5, JSONExportPlugin())
    data_stream.print_processor_statistics()


if __name__ == "__main__":
    main()
