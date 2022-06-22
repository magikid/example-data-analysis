import pandas as pd

def ascii_histogram(seq):
    for k in sorted(seq):
        print('{0:5d} {1}'.format(k, '+' * seq[k]))

def read_csv():
    data = pd.read_csv('2015 Q1.csv', header=0)
    return data

def clean_data(data):
    cleaned_data = data.astype({
        'Total duration (ms)': 'int64',
        'Start date': 'datetime64',
        'Start station': 'string',
        'End date': 'datetime64',
        'End station': 'string',
        'Bike number': 'string',
        'Subscription Type': 'string',
    })
    cleaned_data = cleaned_data.dropna(subset=['Bike number', 'Subscription Type'])
    return cleaned_data

def analyze_data(data):
    days = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for (_, row) in data.iterrows():
        days[row['Start date'].dayofweek] += 1
    print(days)
    ascii_histogram(days)


raw_data = read_csv()
cleaned_data = clean_data(raw_data)
analyzed_data = analyze_data(cleaned_data)
