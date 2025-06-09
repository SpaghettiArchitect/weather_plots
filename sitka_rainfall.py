import csv
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt


def main() -> None:
    # Load the file's dataset
    path = Path(r"data\sitka_weather_2021_full.csv")
    lines = path.read_text().splitlines()

    # Extract dates and daily rainfalls
    csv_reader = csv.DictReader(lines)
    dates, total_rainfall = [], []
    for row in csv_reader:
        current_date = datetime.strptime(row["DATE"], r"%Y-%m-%d")
        daily_rainfall = float(row["PRCP"])
        dates.append(current_date)
        total_rainfall.append(daily_rainfall)

    # Plot the daily rainfall
    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots()
    ax.plot(dates, total_rainfall)

    # Format the plot
    title = "Daily Rainfall for Sitka, US, 2021"
    ax.set_title(title, fontsize=24)
    ax.set_xlabel("", fontsize=14)
    fig.autofmt_xdate()
    ax.set_ylabel("Amount (mm)", fontsize=14)
    ax.tick_params(labelsize=14)

    plt.show()


if __name__ == "__main__":
    main()
