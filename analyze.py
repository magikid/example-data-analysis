import pandas as pd

# Found here: https://stackoverflow.com/a/66015360
def scale_number(number):
    min = 48696
    max = 67291
    scale_factor = 20
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


# Found here: https://realpython.com/python-histograms/#histograms-in-pure-python
def ascii_histogram(seq):
    for k in range(len(seq)):
        print("{0:10s} {1}".format(day_of_week_to_name(k), "+" * scale_number(seq[k])))


def read_csv():
    data = pd.read_csv("2015 Q1.csv", header=0)
    return data


def clean_data(data):
    cleaned_data = data.astype(
        {
            "Total duration (ms)": "int64",
            "Start date": "datetime64",
            "Start station": "string",
            "End date": "datetime64",
            "End station": "string",
            "Bike number": "string",
            "Subscription Type": "string",
        }
    )
    cleaned_data = cleaned_data.dropna(subset=["Bike number", "Subscription Type"])
    return cleaned_data


def analyze_data(data):
    days = [0, 0, 0, 0, 0, 0, 0]
    for (_, row) in data.iterrows():
        days[row["Start date"].dayofweek] += 1
    ascii_histogram(days)


raw_data = read_csv()
cleaned_data = clean_data(raw_data)
analyzed_data = analyze_data(cleaned_data)
