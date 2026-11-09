from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError


class ContactType(str, Enum):
    """Allowed contact types (str mixin lets Pydantic accept "radio")."""
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """Alien contact report with field limits and business rules."""
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def check_rules(self) -> "AlienContact":
        # Runs after every field has passed its own Field() checks.
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if (self.contact_type == ContactType.TELEPATHIC
                and self.witness_count < 3):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        if self.signal_strength > 7 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )

        return self

    def describe(self) -> None:
        """Print the report in a readable format."""
        print(f"ID: {self.contact_id}")
        print(f"Type: {self.contact_type.value}")
        print(f"Location: {self.location}")
        print(f"Signal: {self.signal_strength}/10")
        print(f"Duration: {self.duration_minutes} minutes")
        print(f"Witnesses: {self.witness_count}")
        if self.message_received:
            print(f"Message: '{self.message_received}'")


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")

    valid_contact_report = AlienContact.model_validate({
        "contact_id": "AC_2024_001",
        "timestamp": "2024-01-15T10:30:00",
        "location": "Area 51, Nevada",
        "contact_type": ContactType.RADIO,
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": 5,
        "message_received": "Greetings from Zeta Reticuli"
    })
    print("Valid contact report:")
    valid_contact_report.describe()

    print("\n======================================")
    print("Expected validation error:")
    try:
        invalid_contact_report = AlienContact.model_validate({
            "contact_id": "AC_2024_002",
            "timestamp": "2024-01-15T10:30:00",
            "location": "Area 51, Nevada",
            "contact_type": ContactType.TELEPATHIC,
            "signal_strength": 8.5,
            "duration_minutes": 45,
            "witness_count": 1,
            "message_received": "Greetings from Zeta Reticuli"
        })
        invalid_contact_report.describe()
    except ValidationError as e:
        print(e.errors()[0]["msg"].removeprefix("Value error, "))


if __name__ == "__main__":
    main()
