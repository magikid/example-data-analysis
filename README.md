# example-analysis

This project is here to servce as an example of a Data Analysis 1 project for Code Kentucky students.  It includes data from 2015Q1 about bike rentals in Washington D.C.  This data is analyzed several different ways to determine the most popular bike, which days are most popular, and show some simple statistics about the data.

## Setup

1. Clone the project and move into its directory
```bash
git clone https://github.com/magikid/example-data-analysis.git && cd example-data-analysis
```

2. Install the needed packages (if you have anaconda, this step is optional)
```bash
pip install -r requirements.txt
```

3. Run the script
```bash
python analysis.py
```

## Features used
### Read data in
I used `pandas.read_csv` function to read my CSV file.

### Manipulate and clean your data
I created my own function to clean the data by setting the field types and dropping a column that I didn't need.

### Analyze your data
I have three functions marked by comments that are doing analysis of the data.  One function creates a histogram.  One function finds the most popular bike.  One function finds the mean and median of the ride lengths.

### Visualize your data
Each of my analyses print out their results to the console.  One of them prints out a histogram of the data.  This area still needs work.

### Interpret your data and graphical output
I have included the interpretation in the output for the ride length statistics.
