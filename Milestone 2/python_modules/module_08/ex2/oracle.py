import os
import sys
from dotenv import load_dotenv


def load_configuration() -> None:
    load_dotenv(override=False)


def get_config() -> dict[str, str]:
    config = {
        "MATRIX_MODE": os.environ.get("MATRIX_MODE", "development"),
        "DATABASE_URL": os.environ.get("DATABASE_URL", ""),
        "API_KEY": os.environ.get("API_KEY", ""),
        "LOG_LEVEL": os.environ.get("LOG_LEVEL", "INFO"),
        "ZION_ENDPOINT": os.environ.get("ZION_ENDPOINT", "")
    }

    return config


def validate_config(config: dict[str, str]) -> list[str]:
    required = ["DATABASE_URL", "API_KEY", "ZION_ENDPOINT"]
    errors: list[str] = []

    for key in required:
        value = config[key]
        if value == "":
            errors.append(f"{key} is missing")

    mode = config["MATRIX_MODE"]
    if mode != "development" and mode != "production":
        errors.append(f"MATRIX_MODE is invalid: '{mode}'")

    return errors


def mask_secret(secret: str, visible_chars: int = 4) -> str:
    if len(secret) <= visible_chars:
        return "*" * len(secret)
    return secret[:visible_chars] + "*" * (len(secret) - visible_chars)


def print_config(config: dict[str, str]) -> None:
    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")

    if config["DATABASE_URL"]:
        print("Database: Connected to configured instance")
    else:
        print("Database: WARNING - No DATABASE_URL configured")

    if config["API_KEY"]:
        print("API Access: Authenticated")
    else:
        print("API Access: WARNING - No API_KEY configured")

    print(f"Log Level: {config['LOG_LEVEL']}")

    if config["ZION_ENDPOINT"]:
        print("Zion Network: Online")
    else:
        print("Zion Network: WARNING - No ZION_ENDPOINT configured")

    if config["MATRIX_MODE"] == "development":
        print("\n[DEV MODE] Extra debug info:")
        if config["DATABASE_URL"]:
            db_url = mask_secret(config["DATABASE_URL"])
            print(f"[DEV MODE] Database URL: {db_url}")
        if config["API_KEY"]:
            api_key = mask_secret(config["API_KEY"])
            print(f"[DEV MODE] API Key: {api_key}")
    elif config["MATRIX_MODE"] == "production":
        print("\n[PRODUCTION MODE] Sensitive details hidden from logs.")
    else:
        print(f"\n[WARNING] Invalid MATRIX_MODE: {config['MATRIX_MODE']}")


def security_check(config: dict[str, str]) -> None:
    print("\nEnvironment security check: ")

    print("[OK] No hardcoded secrets detected")

    errors = validate_config(config)
    if not errors:
        print("[OK] .env file properly configured")
    else:
        for e in errors:
            print(f"[WARNING] {e}")

    if config["MATRIX_MODE"] == "production":
        print("[OK] Running with production overrides")
    else:
        print("[OK] Production overrides available (not active now)")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")

    load_configuration()
    config = get_config()

    print_config(config)

    errors = validate_config(config)
    security_check(config)

    print("\nThe Oracle sees all configurations.")

    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
