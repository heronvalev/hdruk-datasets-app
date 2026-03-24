"""
main.py
-------
Creates the Flask application and defines the routes for:
- the HTML page showing dataset metadata in a table
- the JSON API endpoint returning the same cleaned dataset data
"""

from flask import Flask, jsonify, render_template

from services import get_transformed_datasets, is_url


# Create the Flask application instance.
app = Flask(__name__)

# Turn off alphabetic sorting for JSON response
app.json.sort_keys = False

# Frontend endpoint for dataset metadata table.
@app.route("/")
def index():
    datasets = get_transformed_datasets()
    return render_template("index.html", datasets=datasets, is_url=is_url)

# API endpoint to return the dataset as a JSON
@app.route("/api/datasets")
def api_datasets():
    datasets = get_transformed_datasets()
    return jsonify(datasets)

# Run the Flask development server.
if __name__ == "__main__":
    app.run(debug=True)