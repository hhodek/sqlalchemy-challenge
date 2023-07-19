# SQL Alchemy Challenge

## Climate Analysis (climate_starter.ipynb)
The climate analysis is performed using Python, SQLAlchemy, Pandas, and Matplotlib. The following steps are covered in the analysis:

1. Connect to the SQLite database using SQLAlchemy's create_engine() function.
2. Reflect the database tables using automap_base() to create class references.
3. Create a session to link Python to the database.
4. Perform a precipitation analysis by querying the last 12 months of precipitation data and plotting the results using Pandas and Matplotlib.
5. Conduct a station analysis to determine the most active stations and retrieve temperature observations for the most active station.
6. Calculate temperature statistics for the most active station, including the lowest, highest, and average temperatures.


## Flask API Development (app.py)
The Flask API is developed to provide access to the climate data through various routes. The API is created using Flask and interacts with the SQLite database. The following routes are implemented:

1. Home route (/): Displays a landing page with available routes.
2. Precipitation route (/api/v1.0/precipitation): Returns the precipitation data for the last 12 months as JSON.
3. Stations route (/api/v1.0/stations): Returns a JSON list of all the stations in the dataset.
4. Temperature Observations route (/api/v1.0/tobs): Returns the temperature observations for the previous year for the most active station as JSON.
5. Start route (/api/v1.0/<start>): Accepts a start date parameter and returns the minimum, average, and maximum temperatures from the given start date to the end of the dataset.
6. Start-End route (/api/v1.0/<start>/<end>): Accepts start and end dates parameters and returns the minimum, average, and maximum temperatures within the specified date range.


## Usage
1. Ensure that the required dependencies, including Python, Flask, SQLAlchemy, Pandas, and Matplotlib, are installed.
2. Place the SQLite database file (hawaii.sqlite) in the appropriate directory.
3. Run the climate_analysis.ipynb Jupyter Notebook to perform the climate analysis and generate the necessary code.
4. Run the Flask app by executing the app.py file.
5. Access the available routes through the provided endpoints using an API testing tool or web browser.

## Credits
Referenced class materials and ChatGPT

