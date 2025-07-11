import csv
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt


def main() -> None:
    path = Path(r"data\sitka_weather_2021_simple.csv")
    lines = path.read_text().splitlines()

    reader = csv.reader(lines)
    header_row = next(reader)

    # Extract dates, and high and low temperatures
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], r"%Y-%m-%d")
        high = int(row[4])
        low = int(row[5])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

    # Plot the high and low temperatures
    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots()
    ax.plot(dates, highs, color="red", alpha=0.5)
    ax.plot(dates, lows, color="blue", alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

    # Format plot
    ax.set_title("Daily High and Low Temperatures, 2021\nSitka, AK, US", fontsize=20)
    ax.set_xlabel("", fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(labelsize=16)

    # Set the range for the y-axis, so the plot is easier to compare to
    # the Death Valley one
    ax.set(ylim=(0, 140))

    plt.show()


if __name__ == "__main__":
    main()
