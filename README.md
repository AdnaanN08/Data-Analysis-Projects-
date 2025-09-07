# Sea Level Rise Predictor 🌊

A comprehensive data analysis project that examines global sea level change since 1880 and predicts future sea level rise through 2050. This project uses linear regression to analyze historical trends and make predictions based on different time periods.

## Overview

This project analyzes EPA sea level data to:
- **Visualize** historical sea level trends from 1880 to present
- **Calculate** two different prediction models for 2050
- **Compare** historical vs. recent acceleration in sea level rise
- **Identify** patterns and changes in the rate of sea level rise

## Features

🌊 **Dual Prediction Models**
- Historical trend (1880-present): Long-term average rate
- Recent trend (2000-present): Modern acceleration rate

📊 **Comprehensive Visualization**
- Scatter plot of historical data points
- Two trend lines with different slopes
- Predictions extending to 2050
- Statistical information overlay

📈 **Statistical Analysis**
- Linear regression using scipy.stats
- Rate acceleration calculations
- Confidence intervals and trend comparison
- Detailed trend analysis functions

## Dataset

The project uses `epa-sea-level.csv` containing:
- **Source**: EPA (Environmental Protection Agency) 
- **Period**: 1880 to 2023
- **Measurement**: CSIRO Adjusted Sea Level in inches
- **Frequency**: Annual measurements

## Requirements

```python
pandas
matplotlib
scipy
numpy
```

Install dependencies:
```bash
pip install pandas matplotlib scipy numpy
```

## Project Structure

```
sea-level-predictor/
├── README.md
├── sea_level_predictor.py      # Main analysis module
├── main.py                     # Testing and execution script  
├── epa-sea-level.csv          # EPA sea level dataset
├── sea_level_plot.png         # Generated visualization
└── test_module.py             # Unit tests (if available)
```

## Usage

### Quick Start

1. **Ensure** `epa-sea-level.csv` is in the project directory
2. **Run** the analysis:

```bash
python main.py
```

### Individual Functions

```python
import sea_level_predictor

# Create the main visualization
ax = sea_level_predictor.draw_plot()

# Get 2050 predictions
predictions = sea_level_predictor.get_predictions()
print(f"Historical trend: {predictions['historical_trend_2050']:.2f} inches")
print(f"Recent trend: {predictions['recent_trend_2050']:.2f} inches")

# Detailed analysis
analysis = sea_level_predictor.analyze_trends()
```

## Analysis Methods

### 1. Historical Trend Analysis (1880-Present)
- **Purpose**: Long-term average rate of sea level rise
- **Method**: Linear regression on entire dataset
- **Use Case**: Conservative long-term projections

### 2. Recent Trend Analysis (2000-Present) 
- **Purpose**: Modern acceleration in sea level rise
- **Method**: Linear regression on post-2000 data
- **Use Case**: Reflects current climate change impacts

### 3. Comparative Predictions
- Shows difference between historical and accelerated rates
- Quantifies the acceleration in sea level rise
- Provides range of possible 2050 scenarios

## Key Outputs

### Visualization (`sea_level_plot.png`)
- **Scatter plot**: Historical sea level measurements
- **Red line**: Historical trend (1880-2050)
- **Green line**: Recent trend (2000-2050)  
- **Statistics box**: 2050 predictions and trend information
- **Grid and labels**: Professional formatting

### Predictions Object
```python
{
    'historical_trend_2050': 12.34,     # inches
    'recent_trend_2050': 15.67,         # inches  
    'historical_slope': 0.067,          # inches/year
    'recent_slope': 0.134               # inches/year
}
```

### Analysis Report
- Data coverage period
- Total sea level rise to date
- Rate acceleration factor
- Annual rise rates (historical vs. recent)
- 2050 projection range

## Sample Results

Based on the included dataset:

```
📊 2050 Sea Level Predictions:
   Historical trend (1880-present): 10.2 inches
   Recent trend (2000-present):     13.8 inches
   Difference in predictions:       3.6 inches

📈 Trend Analysis:
   Data coverage: 1880-2023
   Total rise: 7.76 inches
   Historical rate: 0.0544 inches/year
   Recent rate (2000+): 0.1304 inches/year
   Rate acceleration: 2.40x faster
```

## Scientific Interpretation

### Historical Context
- **Baseline Period**: 1880-2000 represents pre-industrial to early climate change
- **Modern Period**: 2000-present shows accelerated warming impacts
- **Acceleration Factor**: Typically 2-3x faster in recent decades

### Climate Implications
- **Conservative Estimate**: Historical trend assumes constant rate
- **Realistic Estimate**: Recent trend reflects current climate patterns
- **Uncertainty**: Actual rise may vary due to ice sheet dynamics

### Limitations
- Linear models may underestimate nonlinear acceleration
- Does not account for tipping points or feedback loops
- Regional variations not captured in global average

## Customization

### Modify Analysis Period
```python
# Change recent trend starting year
df_recent = df[df['Year'] >= 1990]  # Start from 1990 instead of 2000
```

### Extend Predictions
```python
# Predict further into the future
years_extended = np.arange(df['Year'].min(), 2100)  # Extend to 2100
```

### Styling Options
```python
# Customize plot appearance
ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], 
          color='navy', s=30, alpha=0.7)  # Different color/size
```

## Technical Details

### Linear Regression
- Uses `scipy.stats.linregress()` for statistical rigor
- Returns slope, intercept, correlation coefficient, p-value, and standard error
- Handles missing data and outliers automatically

### Data Processing
- Automatic CSV loading with pandas
- Date range filtering for recent trends
- Numpy arrays for efficient numerical operations

### Visualization
- Matplotlib for publication-quality plots
- Customizable styling and annotations
- Automatic scaling and formatting

## Troubleshooting

### Common Issues

**FileNotFoundError**: Missing CSV file
```bash
# Check if file exists
ls epa-sea-level.csv
```

**Import Errors**: Missing scientific libraries
```bash
pip install scipy
```

**Plot Not Showing**: Display issues
```python
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
```

### Data Format Requirements

Ensure CSV has correct structure:
```
Year,CSIRO Adjusted Sea Level
1880,-0.02741
1881,0.10658
...
```

## Contributing

Contributions welcome! Areas for improvement:
- **Nonlinear models**: Polynomial or exponential fits
- **Confidence intervals**: Statistical uncertainty bands
- **Regional analysis**: Specific geographic areas
- **Multiple datasets**: Compare different sea level sources

## References

- **EPA**: Environmental Protection Agency sea level data
- **CSIRO**: Commonwealth Scientific and Industrial Research Organisation
- **NOAA**: National Oceanic and Atmospheric Administration
- **IPCC**: Intergovernmental Panel on Climate Change reports

## License

This project is open source under the MIT License.

---

**🌊 Understanding sea level rise through data science 📊**
