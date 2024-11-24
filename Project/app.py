from flask import Flask, render_template
import matplotlib.pyplot as plt
import os

# Initialize the Flask app
app = Flask(__name__)

# Ensure the static directory exists
if not os.path.exists('static'):
    os.makedirs('static')

@app.route('/')
def index():
    # Render the homepage where users can initiate the analysis
    return render_template('index.html')

@app.route('/results')
def results():
    # Generate and save the analysis image
    plt.figure(figsize=(10, 6))
    # Example plot, replace with your actual AQI analysis code
    plt.plot([1, 2, 3], [4, 5, 6], marker='o', label='AQI Example')  # Example data
    plt.title("Seasonal AQI Plot")
    plt.xlabel("Time")
    plt.ylabel("AQI")
    plt.legend()
    plt.grid(True)
    plt.savefig('static/seasonal_aqi.png')  # Save plot to static folder
    plt.close()

    # Render the results page, passing the path to the analysis image
    return render_template('results.html', image_url='seasonal_aqi.png')

if __name__ == "__main__":
    app.run(debug=True)
