import csv
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt


def main() -> None:
    path = Path(r"data\sitka_weather_2021_simple.csv")
    lines = path.read_text().splitlines()

    reader = csv.reader(lines)
    header_row = next(reader)

    # Extract dates and high temperatures
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], r"%Y-%m-%d")
        high = int(row[4])
        dates.append(current_date)
        highs.append(high)

    # Plot the high temperatures
    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots()
    ax.plot(dates, highs, color="red")

    # Format plot
    ax.set_title("Daily High Temperatures, 2021", fontsize=24)
    ax.set_xlabel("", fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(labelsize=16)

    plt.show()


if __name__ == "__main__":
    main()
