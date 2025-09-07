# Medical Data Visualizer

A comprehensive Python project for visualizing and analyzing medical examination data to explore relationships between cardiovascular disease, body measurements, blood markers, and lifestyle choices using matplotlib, seaborn, and pandas.

## Project Overview

This project analyzes medical examination data collected during patient checkups to identify patterns and correlations related to cardiovascular disease. The analysis focuses on understanding how various factors like BMI, blood pressure, cholesterol levels, glucose levels, and lifestyle choices (smoking, alcohol consumption, physical activity) relate to heart disease outcomes.

## Dataset Description

The dataset contains medical examination data with the following features:

### Objective Features (Factual Information)
| Feature | Variable | Type | Description |
|---------|----------|------|-------------|
| Age | `age` | int | Age in days |
| Height | `height` | int | Height in centimeters |
| Weight | `weight` | float | Weight in kilograms |
| Gender | `gender` | categorical | Gender code (1: Female, 2: Male) |

### Examination Features (Medical Results)
| Feature | Variable | Type | Description |
|---------|----------|------|-------------|
| Systolic Blood Pressure | `ap_hi` | int | Upper blood pressure value |
| Diastolic Blood Pressure | `ap_lo` | int | Lower blood pressure value |
| Cholesterol | `cholesterol` | categorical | 1: normal, 2: above normal, 3: well above normal |
| Glucose | `gluc` | categorical | 1: normal, 2: above normal, 3: well above normal |

### Subjective Features (Lifestyle Information)
| Feature | Variable | Type | Description |
|---------|----------|------|-------------|
| Smoking | `smoke` | binary | 0: No, 1: Yes |
| Alcohol Intake | `alco` | binary | 0: No, 1: Yes |
| Physical Activity | `active` | binary | 0: No, 1: Yes |

### Target Variable
| Feature | Variable | Type | Description |
|---------|----------|------|-------------|
| Cardiovascular Disease | `cardio` | binary | 0: No disease, 1: Disease present |

## Generated Features

The project creates additional calculated features:

- **BMI (Body Mass Index)**: Calculated from height and weight
- **Overweight**: Binary indicator (1 if BMI > 25, 0 otherwise)

## Visualizations

### 1. Categorical Plot (Figure 1)
- **Purpose**: Shows the relationship between lifestyle factors and cardiovascular disease
- **Features Analyzed**: cholesterol, glucose, smoking, alcohol, physical activity, overweight
- **Layout**: Side-by-side comparison of patients with and without cardiovascular disease
- **Chart Type**: Grouped bar chart showing counts of good vs bad outcomes
- **Output**: `catplot.png`

### 2. Correlation Heatmap
- **Purpose**: Displays correlations between all numerical variables
- **Features**: All medical and lifestyle variables
- **Data Cleaning**: Removes outliers and invalid measurements
- **Visualization**: Lower triangle heatmap with correlation coefficients
- **Output**: `heatmap.png`

## Project Structure

```
medical-data-visualizer/
│
├── medical_data_visualizer.py    # Main analysis and visualization script
├── main.py                      # Entry point for running analysis
├── medical_examination.csv      # Dataset file
├── catplot.png                  # Generated categorical plot
├── heatmap.png                  # Generated correlation heatmap
└── README.md                    # Project documentation
```

## Requirements

- Python 3.6+
- pandas
- matplotlib
- seaborn
- numpy

Install dependencies:
```bash
pip install pandas matplotlib seaborn numpy
```

## Usage

### Quick Start
```bash
# Run the complete analysis
python main.py
```

### Module Usage
```python
import medical_data_visualizer

# Generate categorical plot
fig1 = medical_data_visualizer.draw_cat_plot()

# Generate correlation heatmap  
fig2 = medical_data_visualizer.draw_heat_map()
```

## Data Processing Steps

### 1. Data Loading and Preparation
- Import medical examination data from CSV
- Validate data types and structure

### 2. Feature Engineering
- **BMI Calculation**: `weight (kg) / (height (m))²`
- **Overweight Classification**: BMI > 25 threshold
- **Binary Normalization**: Convert cholesterol and glucose to binary (normal vs abnormal)

### 3. Data Cleaning (for correlation analysis)
- Remove patients with diastolic pressure > systolic pressure
- Filter out height values below 2.5th percentile or above 97.5th percentile
- Filter out weight values below 2.5th percentile or above 97.5th percentile
- Remove physiologically impossible measurements

### 4. Statistical Analysis
- Calculate correlation matrix between all variables
- Generate summary statistics for different patient groups

## Key Insights

The visualizations help identify:

1. **Risk Factor Patterns**: How lifestyle choices correlate with cardiovascular disease
2. **Medical Marker Relationships**: Connections between blood pressure, cholesterol, and glucose
3. **Demographic Influences**: Age and gender effects on health outcomes
4. **Lifestyle Impact**: Effect of smoking, alcohol, and physical activity on heart health
5. **BMI Correlations**: Relationship between obesity and cardiovascular risk

## Technical Implementation

### Categorical Plot Features
- **Data Reshaping**: Uses `pd.melt()` for long-format data transformation
- **Grouping**: Groups by cardiovascular disease status and feature values
- **Visualization**: Seaborn catplot with bar chart representation
- **Comparison**: Side-by-side panels for disease vs no-disease groups

### Correlation Heatmap Features
- **Data Filtering**: Advanced outlier detection and removal
- **Correlation Calculation**: Pearson correlation coefficients
- **Masking**: Upper triangle mask for cleaner visualization
- **Annotation**: Correlation values displayed on heatmap
- **Color Scheme**: Diverging color map centered at zero

## Sample Output

### Categorical Plot Insights
- Compares good vs bad outcomes for each risk factor
- Separate analysis for patients with and without cardiovascular disease
- Clear visual representation of risk factor distributions

### Correlation Heatmap Insights
- Shows strength and direction of relationships between variables
- Identifies key predictors of cardiovascular disease
- Reveals unexpected correlations between lifestyle and medical factors

## Development and Testing

The project includes a sample dataset with 50 patients for development and testing purposes. This allows you to:

- Test the visualization functions
- Validate data processing steps  
- Ensure proper output generation
- Debug any issues before using full dataset

## Data Quality Assurance

- **Outlier Detection**: Statistical methods to identify unrealistic values
- **Range Validation**: Ensures measurements fall within physiological ranges  
- **Consistency Checks**: Validates relationships between related measurements
- **Missing Data Handling**: Proper treatment of incomplete records

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-visualization`)
3. Commit your changes (`git commit -am 'Add new medical visualization'`)
4. Push to the branch (`git push origin feature/new-visualization`)
5. Create a Pull Request

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Medical examination data analysis techniques
- Seaborn and matplotlib visualization libraries
- Pandas data manipulation capabilities
- Healthcare data science community
- Statistical analysis methodologies for medical data

## Future Enhancements

- **Machine Learning Integration**: Predictive models for cardiovascular risk
- **Interactive Visualizations**: Plotly-based dashboard
- **Advanced Statistics**: Hypothesis testing and confidence intervals
- **Time Series Analysis**: Longitudinal patient data tracking
- **Risk Scoring**: Composite cardiovascular risk calculator
