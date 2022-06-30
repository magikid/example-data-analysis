import pandas as pd

# Found here: https://stackoverflow.com/a/66015360
def scale_number(number):
    min = 48696
    max = 67291
    scale_factor = 80
    return int((number - min) / (max - min) * scale_factor)


def day_of_week_to_name(day_of_week):
    return [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ][day_of_week]


# First analysis
# Found here: https://realpython.com/python-histograms/#histograms-in-pure-python
def ascii_histogram(seq):
    print("Popular days:")
    for k in range(len(seq)):
        print("{0:10s} {1}".format(day_of_week_to_name(k), "+" * scale_number(seq[k])))
    print("\n")


# Second analysis
def most_popular_bike(data):
    popular_bike = data.groupby("Bike number").size().sort_values(ascending=False).head(1)
    print("Most popular bike: {0} with {1} rides\n".format(popular_bike.index[0], popular_bike.values[0]))


# Third analysis
def ride_length_stats(data):
    median = data["Total duration (ms)"].median()
    mean = round(data["Total duration (ms)"].mean(), 2)
    print("Ride length statistics:")
    print("Median ride length: {0}ms\nMean ride length: {1}ms\n".format(median, mean))

    if median < mean:
        print(
            "Since the mean is higher than the median, there were some rides that were really long."
        )
    elif median > mean:
        print(
            "Since the median is higher than the mean, there were some rides that were really short."
        )
    else:
        print(
            "The median and the mean are the same so all the ride lengths were evenly distributed."
        )


def read_csv():
    data = pd.read_csv("2015 Q1.csv", header=0)
    return data


def clean_data(data):
    cleaned_data = data.dropna(subset=["Subscription Type", "Start station", "End station"])
    cleaned_data = cleaned_data.astype(
        {
            "Total duration (ms)": "int32",
            "Start date": "datetime64",
            "End date": "datetime64",
            "Bike number": "string",
        }
    )
    return cleaned_data


def find_daily_popularity(data):
    most_popular_day = 0
    popular_start_days = [0, 0, 0, 0, 0, 0, 0]
    for (_, row) in data.iterrows():
        popular_start_days[row["Start date"].dayofweek] += 1
    for i in range(len(popular_start_days)):
        if popular_start_days[i] > most_popular_day:
            most_popular_day = popular_start_days[i]
            most_popular_day_name = day_of_week_to_name(i)
    print("Most popular day: {0}".format(most_popular_day_name))
    ascii_histogram(popular_start_days)


def analyze_data(data):
    find_daily_popularity(data)
    most_popular_bike(data)
    ride_length_stats(data)


raw_data = read_csv()
cleaned_data = clean_data(raw_data)
analyzed_data = analyze_data(cleaned_data)
