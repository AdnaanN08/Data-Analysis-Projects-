import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
def load_and_clean_data():
    """Load and clean the freeCodeCamp forum pageviews data"""
    # Import data
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
    
    # Clean data by filtering out days when page views were in top 2.5% or bottom 2.5%
    lower_percentile = df['value'].quantile(0.025)
    upper_percentile = df['value'].quantile(0.975)
    
    df_clean = df[(df['value'] >= lower_percentile) & (df['value'] <= upper_percentile)]
    
    return df_clean

def draw_line_plot():
    """Draw line chart showing daily freeCodeCamp Forum page views"""
    # Load and clean data
    df = load_and_clean_data()
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(15, 5))
    
    # Draw line plot
    ax.plot(df.index, df['value'], color='red', linewidth=1)
    
    # Set title and labels
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    
    # Format the plot
    plt.xticks(rotation=0)
    plt.tight_layout()
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    """Draw bar chart showing average daily page views for each month grouped by year"""
    # Load and clean data
    df = load_and_clean_data().copy()
    
    # Extract year and month from the date index
    df['year'] = df.index.year
    df['month'] = df.index.month
    
    # Group by year and month and calculate mean
    df_bar = df.groupby(['year', 'month'])['value'].mean().unstack()
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Create bar plot
    df_bar.plot(kind='bar', ax=ax, width=0.8)
    
    # Set title and labels
    ax.set_title('Average Daily Page Views by Month')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    
    # Set month labels for legend
    month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    ax.legend(labels=month_labels, title='Months', loc='upper left')
    
    # Format x-axis
    ax.set_xticklabels(df_bar.index, rotation=0)
    
    plt.tight_layout()
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    """Draw box plots showing distribution of page views by year and month"""
    # Load and clean data
    df_box = load_and_clean_data().copy()
    df_box.reset_index(inplace=True)
    
    # Extract year and month
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    
    # Create figure with two subplots
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))
    
    # Year-wise box plot (Trend)
    sns.boxplot(data=df_box, x='year', y='value', ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    
    # Month-wise box plot (Seasonality)
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(data=df_box, x='month', y='value', order=month_order, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    
    plt.tight_layout()
    
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

# Main execution for testing
if __name__ == "__main__":
    # Test the functions
    print("Creating line plot...")
    draw_line_plot()
    print("Line plot saved as 'line_plot.png'")
    
    print("Creating bar plot...")
    draw_bar_plot()
    print("Bar plot saved as 'bar_plot.png'")
    
    print("Creating box plots...")
    draw_box_plot()
    print("Box plots saved as 'box_plot.png'")
    
    print("All visualizations completed!")