from datetime import datetime
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    """Basic station data. Field() sets the per-field constraints."""
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)

    def describe(self) -> None:
        print(f"ID: {self.station_id}")
        print(f"Name: {self.name}")
        print(f"Crew: {self.crew_size} people")
        print(f"Power: {self.power_level}%")
        print(f"Oxygen: {self.oxygen_level}%")
        if self.is_operational:
            print("Status: Operational")
        else:
            print("Status: Not operational")


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")

    valid_space_station = SpaceStation.model_validate({
        "station_id": "ISS001",
        "name": "International Space Station",
        "crew_size": 6,
        "power_level": 85.5,
        "oxygen_level": 92.3,
        "last_maintenance": "2024-01-15T10:30:00"
    })
    print("Valid station created:")
    valid_space_station.describe()

    print("\n========================================")
    print("Expected validation error:")
    try:
        invalid_space_station = SpaceStation(
                station_id="ISS002",
                name="International Space Station",
                crew_size=25,
                power_level=85.5,
                oxygen_level=92.3,
                last_maintenance=datetime(2024, 1, 15, 10, 30)
            )
        invalid_space_station.describe()
    except ValidationError as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
