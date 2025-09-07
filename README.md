# Demographic Data Analyzer

A Python project that analyzes demographic data from the 1994 Census database using Pandas to extract meaningful insights about income, education, work patterns, and demographics.

## Project Overview

This project analyzes the famous "Adult" dataset (also known as "Census Income" dataset) from the UCI Machine Learning Repository. The dataset contains demographic information extracted from the 1994 Census database and is commonly used for machine learning tasks to predict whether a person earns over $50,000 per year.

## Dataset Description

The dataset contains the following columns:
- **age**: Age of the individual
- **workclass**: Type of employment (Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked)
- **fnlwgt**: Final weight (sampling weight assigned by Census Bureau)
- **education**: Education level (Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool)
- **education-num**: Number of years of education
- **marital-status**: Marital status
- **occupation**: Type of occupation
- **relationship**: Relationship status
- **race**: Race (White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black)
- **sex**: Gender (Female, Male)
- **capital-gain**: Capital gains
- **capital-loss**: Capital losses
- **hours-per-week**: Hours worked per week
- **native-country**: Country of origin
- **salary**: Income level (<=50K, >50K)

## Analysis Questions

The project answers the following demographic questions:

1. **Race Distribution**: How many people of each race are represented in the dataset?
2. **Gender Analysis**: What is the average age of men?
3. **Education Statistics**: What percentage of people have a Bachelor's degree?
4. **Income vs Education**: 
   - What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
   - What percentage of people without advanced education make more than 50K?
5. **Work Hours Analysis**:
   - What is the minimum number of hours a person works per week?
   - What percentage of people who work the minimum hours earn more than 50K?
6. **Geographic Income Analysis**: Which country has the highest percentage of people earning >50K?
7. **Occupation Analysis**: What is the most popular occupation for high earners (>50K) in India?

## Project Structure

```
demographic-data-analyzer/
│
├── demographic_data_analyzer.py    # Main analysis script
├── main.py                        # Entry point for testing
├── adult.data.csv                 # Dataset file
├── sample_adult_data.csv          # Sample dataset for testing
└── README.md                      # Project documentation
```

## Requirements

- Python 3.6+
- pandas

Install dependencies:
```bash
pip install pandas
```

## Usage

1. **Download the Dataset**:
   - Option 1: Use the provided sample dataset (`sample_adult_data.csv`) and rename it to `adult.data.csv`
   - Option 2: Download the full dataset from [Kaggle](https://www.kaggle.com/datasets/uciml/adult-census-income)
   - Option 3: Get it from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/2/adult)

2. **Run the Analysis**:
   ```bash
   python main.py
   ```

3. **Use as a Module**:
   ```python
   import demographic_data_analyzer
   
   # Get results as a dictionary
   results = demographic_data_analyzer.calculate_demographic_data(print_data=False)
   
   # Print results to console
   demographic_data_analyzer.calculate_demographic_data(print_data=True)
   ```

## Sample Output

```
Number of each race:
White                 27816
Black                  3124
Asian-Pac-Islander     1039
Amer-Indian-Eskimo      311
Other                   271
Name: race, dtype: int64

Average age of men: 39.4
Percentage with Bachelors degrees: 16.4%
Percentage with higher education that earn >50K: 46.5%
Percentage without higher education that earn >50K: 17.4%
Min work time: 1 hours/week
Percentage of rich among those who work fewest hours: 10.0%
Country with highest percentage of rich: Iran
Highest percentage of rich people in country: 41.9%
Top occupations in India: Prof-specialty
```

## Key Features

- **Efficient Data Processing**: Uses pandas for fast data manipulation and analysis
- **Statistical Insights**: Provides percentage calculations and demographic breakdowns
- **Country-wise Analysis**: Identifies geographic patterns in income distribution
- **Education Impact**: Analyzes correlation between education level and income
- **Work Pattern Analysis**: Examines relationship between work hours and earnings

## Technical Implementation

- **Data Loading**: Reads CSV data using pandas
- **Data Filtering**: Uses boolean indexing for efficient data selection
- **Aggregation**: Employs groupby operations for statistical analysis
- **Precision**: All percentages rounded to 1 decimal place for clarity

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-analysis`)
3. Commit your changes (`git commit -am 'Add new analysis'`)
4. Push to the branch (`git push origin feature/new-analysis`)
5. Create a Pull Request

## License

This project is open source and available under the MIT License.

## Data Source

The original dataset is from the UCI Machine Learning Repository:
- **Creator**: Barry Becker
- **Donor**: Ronny Kohavi and Barry Becker
- **Source**: 1994 Census database
- **Citation**: Dua, D. and Graff, C. (2019). UCI Machine Learning Repository. Irvine, CA: University of California, School of Information and Computer Science.

## Acknowledgments

- UCI Machine Learning Repository for providing the dataset
- The pandas development team for the excellent data analysis library
- The Python community for continuous support and development
