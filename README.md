# Time Series Visualizer

A comprehensive data visualization project that analyzes and visualizes freeCodeCamp forum page view data from 2016 to 2019. This project demonstrates time series analysis using Python's powerful data visualization libraries.

## Overview

This project creates three different types of visualizations to help understand patterns in daily page views:
- **Line Chart**: Shows daily page views over time to identify overall trends
- **Bar Chart**: Displays average monthly page views grouped by year to compare seasonal patterns
- **Box Plots**: Reveals data distribution patterns by year and month to identify outliers and seasonality

## Features

✅ **Data Cleaning**: Automatically filters outliers (top and bottom 2.5%)  
✅ **Multiple Visualization Types**: Line plots, bar charts, and box plots  
✅ **Trend Analysis**: Identifies yearly growth patterns  
✅ **Seasonality Detection**: Reveals monthly patterns in user activity  
✅ **Professional Styling**: Clean, publication-ready charts  

## Dataset

The project uses `fcc-forum-pageviews.csv` containing:
- **Date Range**: May 9, 2016 to December 3, 2019
- **Data Points**: Daily page view counts
- **Format**: CSV with `date` and `value` columns

## Requirements

```python
pandas
matplotlib
seaborn
numpy
```

Install dependencies:
```bash
pip install pandas matplotlib seaborn numpy
```

## Project Structure

```
time-series-visualizer/
├── README.md
├── time_series_visualizer.py    # Main visualization functions
├── main.py                      # Testing and execution script
├── fcc-forum-pageviews.csv     # Dataset file
├── line_plot.png               # Generated line chart
├── bar_plot.png                # Generated bar chart
└── box_plot.png                # Generated box plots
```

## Usage

### Quick Start

1. **Clone/Download** the project files
2. **Ensure** `fcc-forum-pageviews.csv` is in the project directory
3. **Run** the main script:

```bash
python main.py
```

### Individual Functions

```python
import time_series_visualizer

# Generate line plot
fig1 = time_series_visualizer.draw_line_plot()

# Generate bar chart
fig2 = time_series_visualizer.draw_bar_plot()

# Generate box plots
fig3 = time_series_visualizer.draw_box_plot()
```

## Visualizations

### 1. Line Plot (`draw_line_plot`)
- **Purpose**: Shows daily page view trends over time
- **Output**: `line_plot.png`
- **Features**: 
  - Clean time series line chart
  - Identifies growth patterns and anomalies
  - Title: "Daily freeCodeCamp Forum Page Views 5/2016-12/2019"

### 2. Bar Chart (`draw_bar_plot`)
- **Purpose**: Compares average monthly page views by year
- **Output**: `bar_plot.png`
- **Features**:
  - Grouped bars showing months within each year
  - Legend with month abbreviations (Jan-Dec)
  - Reveals seasonal patterns and yearly growth

### 3. Box Plots (`draw_box_plot`)
- **Purpose**: Shows data distribution and identifies outliers
- **Output**: `box_plot.png`
- **Features**:
  - Left plot: Year-wise distribution (trend analysis)
  - Right plot: Month-wise distribution (seasonality analysis)
  - Reveals data spread and seasonal variations

## Data Cleaning

The project automatically:
- Removes extreme outliers (values in top/bottom 2.5%)
- Handles missing or invalid dates
- Maintains data integrity for accurate analysis

## Key Insights

The visualizations help identify:
- **Growth Trends**: Overall increase in forum activity over time
- **Seasonal Patterns**: Higher activity during certain months (back-to-school periods)
- **Weekly Cycles**: Different patterns between weekdays and weekends
- **Outliers**: Unusual spikes or drops in activity

## Customization

### Modify Date Range
```python
# In load_and_clean_data function
df = df['2017-01-01':'2018-12-31']  # Filter specific date range
```

### Adjust Outlier Filtering
```python
# Change percentiles for outlier removal
lower_percentile = df['value'].quantile(0.05)  # 5% instead of 2.5%
upper_percentile = df['value'].quantile(0.95)  # 95% instead of 97.5%
```

### Color Schemes
```python
# Line plot color
ax.plot(df.index, df['value'], color='blue', linewidth=1)

# Bar plot colors (automatic colormap)
df_bar.plot(kind='bar', ax=ax, colormap='viridis')
```

## Technical Details

### Data Processing
- Uses `pandas` for efficient data manipulation
- Automatic date parsing and indexing
- Statistical outlier detection using quantiles

### Visualization Libraries
- **Matplotlib**: Core plotting functionality and customization
- **Seaborn**: Enhanced statistical visualizations and styling
- **Pandas**: Built-in plotting methods for quick data exploration

### Performance
- Efficient memory usage with data copying
- Optimized for datasets with 1000+ daily records
- Fast rendering for interactive exploration

## Troubleshooting

### Common Issues

**FileNotFoundError**: CSV file missing
```bash
# Ensure the CSV file is in the correct location
ls fcc-forum-pageviews.csv
```

**Import Errors**: Missing dependencies
```bash
pip install --upgrade pandas matplotlib seaborn
```

**Empty Plots**: Data filtering too aggressive
```python
# Check data after filtering
df = load_and_clean_data()
print(f"Data points after cleaning: {len(df)}")
```

### Data Format Issues

Ensure your CSV has the correct format:
```
date,value
2016-05-09,19736
2016-05-10,19755
...
```

## Contributing

Feel free to contribute improvements:
1. **Fork** the repository
2. **Create** a feature branch
3. **Add** your enhancements
4. **Submit** a pull request

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Data source: freeCodeCamp.org forum analytics
- Built for educational purposes and data science learning
- Demonstrates best practices in time series visualization

---

**Happy Data Visualizing! 📊**
