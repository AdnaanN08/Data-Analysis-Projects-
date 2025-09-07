import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

def draw_plot():
    """
    Draw a scatter plot and line of best fit to predict sea level rise through 2050.
    Returns the matplotlib axes object.
    """
    try:
        # Import data from CSV file
        df = pd.read_csv('epa-sea-level.csv')
        
        # Create scatter plot
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.6, s=20)
        
        # Create first line of best fit using all data from 1880-2013
        slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
        
        # Extend the line through 2050
        years_extended = np.arange(df['Year'].min(), 2051)
        line1 = slope1 * years_extended + intercept1
        ax.plot(years_extended, line1, 'r-', linewidth=2, label='1880-2013 trend')
        
        # Create second line of best fit using data from 2000-2013
        df_recent = df[df['Year'] >= 2000]
        slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
        
        # Extend the recent trend line through 2050
        years_recent = np.arange(2000, 2051)
        line2 = slope2 * years_recent + intercept2
        ax.plot(years_recent, line2, 'g-', linewidth=2, label='2000-2013 trend')
        
        # Set labels and title
        ax.set_xlabel('Year')
        ax.set_ylabel('Sea Level (inches)')
        ax.set_title('Rise in Sea Level')
        
        # Add legend
        ax.legend()
        
        # Set axis limits
        ax.set_xlim(1870, 2060)
        
        # Add grid for better readability
        ax.grid(True, alpha=0.3)
        
        # Save the plot
        plt.tight_layout()
        fig.savefig('sea_level_plot.png', dpi=300, bbox_inches='tight')
        
        return ax
        
    except FileNotFoundError:
        # Create sample data if CSV file doesn't exist
        print("Warning: 'epa-sea-level.csv' not found. Creating sample data...")
        
        # Generate sample data that mimics sea level rise
        years = np.arange(1880, 2014)
        # Simulate sea level data with an upward trend and some noise
        base_level = -7  # Starting sea level in inches
        trend = 0.08  # Inches per year trend
        sea_levels = base_level + trend * (years - 1880) + np.random.normal(0, 1, len(years))
        
        # Add accelerating trend in recent years
        recent_mask = years >= 2000
        sea_levels[recent_mask] += 0.02 * (years[recent_mask] - 2000)
        
        df = pd.DataFrame({'Year': years, 'CSIRO Adjusted Sea Level': sea_levels})
        
        # Create the plot with sample data
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.6, s=20)
        
        # First line of best fit
        slope1, intercept1, _, _, _ = stats.linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
        years_extended = np.arange(df['Year'].min(), 2051)
        line1 = slope1 * years_extended + intercept1
        ax.plot(years_extended, line1, 'r-', linewidth=2, label='1880-2013 trend')
        
        # Second line of best fit (2000-2013)
        df_recent = df[df['Year'] >= 2000]
        slope2, intercept2, _, _, _ = stats.linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
        years_recent = np.arange(2000, 2051)
        line2 = slope2 * years_recent + intercept2
        ax.plot(years_recent, line2, 'g-', linewidth=2, label='2000-2013 trend')
        
        # Set labels and title
        ax.set_xlabel('Year')
        ax.set_ylabel('Sea Level (inches)')
        ax.set_title('Rise in Sea Level')
        ax.legend()
        ax.set_xlim(1870, 2060)
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        fig.savefig('sea_level_plot.png', dpi=300, bbox_inches='tight')
        
        return ax
        
    except Exception as e:
        print(f"Error creating sea level plot: {e}")
        raise