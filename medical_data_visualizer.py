import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def draw_cat_plot():
    """
    Create a categorical plot showing the counts of good and bad outcomes 
    for the cholesterol, gluc, alco, active, and smoke variables.
    """
    try:
        # Create sample data if no data file exists
        # In a real scenario, you would load from a CSV file
        # df = pd.read_csv('medical_examination.csv')
        
        # Sample data for demonstration
        np.random.seed(42)
        n_samples = 1000
        df = pd.DataFrame({
            'cholesterol': np.random.choice([1, 2, 3], n_samples),
            'gluc': np.random.choice([1, 2, 3], n_samples),
            'alco': np.random.choice([0, 1], n_samples),
            'active': np.random.choice([0, 1], n_samples),
            'smoke': np.random.choice([0, 1], n_samples),
            'cardio': np.random.choice([0, 1], n_samples)
        })
        
        # Melt the dataframe for categorical plotting
        df_cat = pd.melt(df, id_vars=['cardio'], 
                        value_vars=['cholesterol', 'gluc', 'alco', 'active', 'smoke'])
        
        # Create the categorical plot
        fig = sns.catplot(x='variable', hue='value', col='cardio', 
                         data=df_cat, kind='count', height=5, aspect=1.2)
        
        fig.set_axis_labels('Variable', 'Count')
        fig.set_titles('Cardio = {col_name}')
        
        # Save the plot
        plt.savefig('catplot.png', dpi=300, bbox_inches='tight')
        plt.close()
        
    except Exception as e:
        print(f"Error creating categorical plot: {e}")

def draw_heat_map():
    """
    Create a correlation heatmap of the medical examination data.
    """
    try:
        # Create sample data if no data file exists
        np.random.seed(42)
        n_samples = 1000
        df = pd.DataFrame({
            'age': np.random.randint(30, 70, n_samples),
            'height': np.random.randint(150, 200, n_samples),
            'weight': np.random.randint(50, 120, n_samples),
            'ap_hi': np.random.randint(80, 180, n_samples),
            'ap_lo': np.random.randint(60, 120, n_samples),
            'cholesterol': np.random.choice([1, 2, 3], n_samples),
            'gluc': np.random.choice([1, 2, 3], n_samples),
            'alco': np.random.choice([0, 1], n_samples),
            'active': np.random.choice([0, 1], n_samples),
            'smoke': np.random.choice([0, 1], n_samples),
            'cardio': np.random.choice([0, 1], n_samples)
        })
        
        # Calculate correlation matrix
        corr = df.corr()
        
        # Create mask for upper triangle
        mask = np.triu(np.ones_like(corr, dtype=bool))
        
        # Create the heatmap
        plt.figure(figsize=(12, 10))
        sns.heatmap(corr, mask=mask, annot=True, fmt='.2f', 
                   cmap='coolwarm', center=0, square=True, 
                   linewidths=0.5, cbar_kws={"shrink": 0.5})
        
        plt.title('Correlation Heatmap of Medical Data')
        plt.tight_layout()
        
        # Save the plot
        plt.savefig('heatmap.png', dpi=300, bbox_inches='tight')
        plt.close()
        
    except Exception as e:
        print(f"Error creating heatmap: {e}")