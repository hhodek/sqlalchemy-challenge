#################################################
# Import Dependencies
#################################################
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session


#################################################
# Database Setup
#################################################
# Create engine to connect to SQLite database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect the database tables into classes
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session (link) from Python to the database
session = Session(engine)


#################################################
# Flask Setup
#################################################
# Create an instance of Flask
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

# Home route
@app.route("/")
def home():
    """Homepage"""
    return (
        f"Welcome to the Climate App API!<br/><br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;"
    )

# Precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the precipitation data for the last 12 months as JSON"""
    # Calculate the date one year from the last date in the dataset
    last_date = session.query(func.max(Measurement.date)).scalar()
    one_year_ago = dt.datetime.strptime(last_date, '%Y-%m-%d') - dt.timedelta(days=365)

    # Perform a query to retrieve the precipitation data
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).all()

    # Convert the query results to a dictionary using date as the key and prcp as the value
    precipitation_data = {date: prcp for date, prcp in results}

    return jsonify(precipitation_data)

# Stations route
@app.route("/api/v1.0/stations")
def stations():
    """Return a JSON list of stations from the dataset"""
    # Perform the query to retrieve the list of stations
    results = session.query(Station.station).all()

    # Convert the query results to a list
    station_list = [station[0] for station in results]

    return jsonify(station_list)

# Temperature Observations route
@app.route("/api/v1.0/tobs")
def tobs():
    """Return the temperature observations for the previous year for the most active station as JSON"""
    # Find the most active station
    most_active_station = session.query(Measurement.station, func.count(Measurement.station)).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).first()[0]

    # Calculate the date one year from the last date in the dataset
    last_date = session.query(func.max(Measurement.date)).scalar()
    one_year_ago = dt.datetime.strptime(last_date, '%Y-%m-%d') - dt.timedelta(days=365)

    # Perform a query to retrieve the temperature observations for the most active station
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == most_active_station).filter(Measurement.date >= one_year_ago).all()

    # Convert the query results to a list of dictionaries
    temperature_observations = [{"date": date, "tobs": tobs} for date, tobs in results]

    return jsonify(temperature_observations)

# Start route
@app.route("/api/v1.0/<start>")
def start_date(start):
    """Return the minimum, average, and maximum temperatures calculated from the given start date to the end of the dataset"""
    # Perform the query to calculate the TMIN, TAVG, and TMAX for dates greater than or equal to the start date
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()

    # Create a dictionary to store the temperature statistics
    temperature_stats = {
        "TMIN": results[0][0],
        "TAVG": results[0][1],
        "TMAX": results[0][2]
    }

    return jsonify(temperature_stats)

# Start-End route
@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    """Return the minimum, average, and maximum temperatures calculated from the given start date to the given end date"""
    # Perform the query to calculate the TMIN, TAVG, and TMAX for dates within the start-end range
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    # Create a dictionary to store the temperature statistics
    temperature_stats = {
        "TMIN": results[0][0],
        "TAVG": results[0][1],
        "TMAX": results[0][2]
    }

    return jsonify(temperature_stats)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)