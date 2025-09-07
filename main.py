# This entrypoint file to be used in development. Start by reading README.md
import sea_level_predictor

# Test your function by calling it here
print("Testing sea level predictor...")

try:
    # Test the plotting function
    ax = sea_level_predictor.draw_plot()
    print("✓ Sea level plot created successfully")
    print("Plot saved as 'sea_level_plot.png'")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("Make sure you have 'epa-sea-level.csv' in the same directory")

# Run unit tests automatically when available
if __name__ == "__main__":
    pass