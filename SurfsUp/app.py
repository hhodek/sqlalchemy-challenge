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
engine = create_engine("sqlite://hawaii.sqlite")

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
