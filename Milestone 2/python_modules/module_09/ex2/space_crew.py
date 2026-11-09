from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, model_validator, ValidationError


class Rank(str, Enum):
    """Allowed crew ranks."""
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """A single crew member. Used as a nested model inside SpaceMission."""
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    """Mission with a list of CrewMember and safety rules."""
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validation_rules(self) -> "SpaceMission":
        # Runs only if every field (and every nested CrewMember) is valid
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        if not any(
            m.rank in (Rank.COMMANDER, Rank.CAPTAIN) for m in self.crew
        ):
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )
        if self.duration_days > 365:
            experienced = sum(1 for m in self.crew if m.years_experience >= 5)
            if experienced * 2 < len(self.crew):
                raise ValueError(
                    "Long missions (> 365 days) need 50% experienced crew "
                    "(5+ years)"
                )
        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")

        return self

    def describe(self) -> None:
        """Print the mission and its crew in a readable format."""
        print(f"Mission: {self.mission_name}")
        print(f"ID: {self.mission_id}")
        print(f"Destination: {self.destination}")
        print(f"Duration: {self.duration_days} days")
        print(f"Budget: ${self.budget_millions}M")
        print(f"Crew size: {len(self.crew)}")
        print("Crew members:")
        for m in self.crew:
            print(f"- {m.name} ({m.rank.value}) - {m.specialization}")


def build_mission_data(sarah_rank: str) -> dict[str, object]:
    """Build the mission data. Only Sarah's rank changes between demos."""
    return {
        "mission_id": "M2024_MARS",
        "mission_name": "Mars Colony Establishment",
        "destination": "Mars",
        "launch_date": "2026-03-15T08:00:00",
        "duration_days": 900,
        "budget_millions": 2500.0,
        "crew": [
            {
                "member_id": "CM001",
                "name": "Sarah Connor",
                "rank": sarah_rank,
                "age": 45,
                "specialization": "Mission Command",
                "years_experience": 12,
            },
            {
                "member_id": "CM002",
                "name": "John Smith",
                "rank": "lieutenant",
                "age": 38,
                "specialization": "Navigation",
                "years_experience": 8,
            },
            {
                "member_id": "CM003",
                "name": "Alice Johnson",
                "rank": "officer",
                "age": 29,
                "specialization": "Engineering",
                "years_experience": 3,
            },
        ],
    }


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 41)

    valid_mission = SpaceMission.model_validate(
        build_mission_data("commander")
    )
    print("Valid mission created:")
    valid_mission.describe()

    print("\n" + "=" * 41)
    print("Expected validation error:")
    try:
        SpaceMission.model_validate(build_mission_data("officer"))
    except ValidationError as e:
        print(e.errors()[0]["msg"].removeprefix("Value error, "))


if __name__ == "__main__":
    main()
