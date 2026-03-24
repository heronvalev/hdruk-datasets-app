# HDR UK Dataset Metadata App

A small Flask web application built for the HDR UK Junior Full Stack Software Engineer technical test.

The app fetches dataset metadata from the provided HDR UK JSON source and exposes only the following fields for each dataset:

- title
- description
- accessServiceCategory
- accessRights

## Project structure

- `main.py` - creates the Flask app and defines the HTML and JSON routes
- `services.py` - fetches the source JSON and transforms each dataset into the required four fields
- `templates/index.html` - renders the dataset metadata in an HTML table
- `static/styles.css` - provides the page and table styling
- `requirements.txt` - lists the Python dependencies needed to run the app
- `README.md` - explains the project setup and usage

## Features

- HTML table view at `/`
- JSON API endpoint at `/api/datasets`
- Normalisation of missing values
- Conditional rendering of `accessRights` as a clickable link in the frontend when appropriate

## Tech Stack

- Python
- Flask
- Requests
- HTML / CSS

## Setup

Clone the repository and move into the project folder:

```powershell
git clone https://github.com/heronvalev/hdruk-datasets-app.git
cd hdruk-datasets-app
```

Create and activate a virtual environment:

```powershell
python -m venv .venv
```

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Run the app:

```powershell
python main.py
```

## Routes

- `/` - displays the dataset metadata in an HTML table
- `/api/datasets` - returns the dataset metadata as JSON

## Notes

- The source data is fetched directly from the HDR UK JSON URL provided in the task.
- Missing values are normalised to `Not provided`.
- Some `accessRights` values in the source data are not valid URLs, so the frontend only renders them as links when they appear to be link-like.

