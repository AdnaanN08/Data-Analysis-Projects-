# This entrypoint file to be used in development.
import medical_data_visualizer

# Test your function by calling it here
print("Creating categorical plot...")
medical_data_visualizer.draw_cat_plot()
print("Categorical plot saved as 'catplot.png'")

print("\nCreating correlation heatmap...")
medical_data_visualizer.draw_heat_map()
print("Heatmap saved as 'heatmap.png'")

print("\nBoth visualizations have been created successfully!")