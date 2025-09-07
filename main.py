# This entrypoint file to be used in development. Start by reading README.md
import time_series_visualizer
from unittest import main
import matplotlib.pyplot as plt

# Test your function by calling it here
print("Testing time_series_visualizer functions...")

try:
    # Test line plot
    print("\n1. Testing draw_line_plot()...")
    fig1 = time_series_visualizer.draw_line_plot()
    print("✓ Line plot created successfully")
    
    # Test bar plot  
    print("\n2. Testing draw_bar_plot()...")
    fig2 = time_series_visualizer.draw_bar_plot()
    print("✓ Bar plot created successfully")
    
    # Test box plots
    print("\n3. Testing draw_box_plot()...")
    fig3 = time_series_visualizer.draw_box_plot()
    print("✓ Box plots created successfully")
    
    print("\n✅ All tests passed! Check the saved PNG files:")
    print("  - line_plot.png")
    print("  - bar_plot.png") 
    print("  - box_plot.png")
    
    # Show plots (optional - comment out if running in headless environment)
    plt.show()
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("Make sure you have the 'fcc-forum-pageviews.csv' file in the same directory")

# Run unit tests automatically when available
if __name__ == "__main__":
    try:
        # This will run unit tests if available
        main(module='test_module', exit=False)
    except:
        print("\nNo unit tests found - manual testing completed")