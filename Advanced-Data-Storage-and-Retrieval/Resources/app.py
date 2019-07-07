
#Flask Setup
from flask import Flask
app = Flask(__name__)

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from sqlalchemy import Column, Integer, String, Float, Date, Text
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base() 
# session=tf.Session() 

#Flask Routes
@app.route("/")
def welcome():
    """Listing of the available API routes"""
    return(
        f"Available Routes: <br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )
@app.route("/api/v1.0/precipitation")
def precipitation():
    #Returns a list of precipitation records""""""
    print("Server received request for 'Precipitation' results...")
#Convert the query results to a Dictionary using date as the key and prcp as the value.
    prcp_results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date > '2017-01-01').all()
    
#Return the JSON representation of your dictionary.
    all_prcp = []
    for prcp in prcp_results:
        prcp_dict = {}
        prcp_dict["Date"] = Measurement.date
        prcp_dict["tobs"] = Measurement.tobs
        all_prcp.append(prcp_dict)
        # all_prcp = list(np.ravel(prcp_dict))
#convert list of tuples into normal list 
    # all_prcp = list(np.ravel(results))
    return jsonify(all_prcp)

@app.route("/api/v1.0/stations")
def stations():
    #Returns a list of stations from the dataset in JSON format
    print("Server received request for 'Station' results...")

    station_results = session.query(Stations.station).all()

#convert list of tuples into normal list 
    all_stations = list(np.ravel(station_results))
    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    #Returns a list of temperature observations from the last year in JSON format
    tobs_results = session.query(Measurement.tobs).filter(Measurement.date > '2017-01-01').all()

#convert list of tuples into normal list 
    all_tobs = list(np.ravel(tobs_results))
    return jsonify(all_tobs)

if __name__ == '__main__':
    app.run(debug=True)
