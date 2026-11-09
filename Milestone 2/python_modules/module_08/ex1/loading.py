import sys
import importlib
from importlib.metadata import version, PackageNotFoundError

REQUIRED_PACKAGES: dict[str, str] = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready",
}


def check_dependencies() -> tuple[list[str], list[str]]:
    available: list[str] = []
    missing: list[str] = []

    for package_name, description in REQUIRED_PACKAGES.items():
        try:
            importlib.import_module(package_name)
            package_version = version(package_name)
            available.append(
                f"[OK] {package_name} ({package_version}) - "
                f"{description}"
            )
        except ImportError:
            missing.append(package_name)
        except PackageNotFoundError:
            missing.append(package_name)

    return available, missing


def print_dependencies(available: list[str], missing: list[str]) -> None:
    print("Checking dependencies:")

    for line in available:
        print(line)

    if missing:
        print("\nMissing dependencies:", ", ".join(missing))
        print("\nInstall with pip:")
        print(" pip install -r requirements.txt")
        print("\nOr install with Poetry:")
        print(" poetry install")
        sys.exit(1)


def generate_matrix_data(
    num_points: int = 1000, output_path: str = "matrix_analysis.png"
) -> None:
    import numpy as np
    import pandas as pd
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    rng = np.random.default_rng(seed=42)

    agent_id = rng.integers(low=1, high=1000, size=num_points)
    signal_strength = rng.normal(loc=50, scale=15, size=num_points)
    system_load = rng.uniform(low=0, high=100, size=num_points)

    df = pd.DataFrame({
        "agent_id": agent_id,
        "signal_strength": signal_strength,
        "system_load": system_load,
    })
    print(f"Processing {num_points} data points...")

    df["rolling_mean"] = df["signal_strength"].rolling(window=20).mean()
    summary = df["signal_strength"].describe()
    print(f"Mean: {summary['mean']:.4f}")
    print(f"Std deviation: {summary['std']:.4f}")
    print(f"Min: {summary['min']:.4f}")
    print(f"Max: {summary['max']:.4f}")

    print("\nGenerating visualization...")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df["signal_strength"], alpha=0.4, label="Signal strength")
    ax.plot(df["rolling_mean"], linewidth=2, label="Rolling mean")
    ax.set_title("Matrix Data Analysis")
    ax.set_xlabel("Data point index")
    ax.set_ylabel("Signal strength")
    ax.legend()
    fig.savefig(output_path, dpi=100, bbox_inches="tight")
    plt.close(fig)

    print("\nAnalysis complete!")
    print(f"Results saved to: {output_path}")


def compare_pip_poetry(available: list[str]) -> None:
    print("\nDependency management comparison:")
    print("-" * 40)

    print("Installed package versions:")
    for line in available:
        print(f" {line}")

    print("\npip:")
    print(" Config file: requirements.txt")
    print(" Lock file: none (versions can drift over time)")
    print(" Virtual env: managed manually (python -m venv)")

    print("\nPoetry:")
    print(" Config file: pyproject.toml")

    try:
        with open("poetry.lock"):
            print(" Lock file: poetry.lock (found, versions pinned)")
    except FileNotFoundError:
        print(" Lock file: poetry.lock (not found)")

    print(" Virtual env: managed automatically by Poetry")


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")

    available, missing = check_dependencies()
    print_dependencies(available, missing)

    generate_matrix_data()

    compare_pip_poetry(available)


if __name__ == "__main__":
    main()
    print("\nEnd of program")