import datetime as dt

from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

mt = Base.classes.measurement
st = Base.classes.station

session = Session(engine)


app = Flask(__name__)


@app.route("/api/v1.0/stations")
def stations():
    station = dict(engine.execute("SELECT station, name FROM station").fetchall())

    return jsonify(station)

@app.route("/api/v1.0/precipitation")
def precipitation():
    prec = dict(engine.execute('SELECT date, prcp FROM measurement').fetchall())

    return jsonify(prec)


@app.route("/api/v1.0/tobs")
def temperature():
    most_active_station_id = "USC00519281"

    most_active_last_date = dt.datetime.strptime(
        session.query(mt.date, mt.tobs).filter(mt.station == most_active_station_id).order_by(mt.date.desc()).all()[0][0],
        '%Y-%m-%d %H:%M:%S')
    most_active_first_date = most_active_last_date - dt.timedelta(days=365)

    temp_page_result = dict(
        session.query(mt.date, mt.tobs).filter(mt.station == most_active_station_id, mt.date > most_active_first_date).all())

    return jsonify(temp_page_result)


@app.route("/api/v1.0/<start_data>")
def start_page(start_data):
    start_date = str(start_data)

    tobs_max = engine.execute(f'SELECT MAX(measurement.tobs) FROM measurement WHERE measurement.date>{start_date}') \
                        .fetchall()[0][0]
    tobs_min = engine.execute(f'SELECT MIN(measurement.tobs) FROM measurement WHERE measurement.date>{start_date}') \
                        .fetchall()[0][0]
    tobs_avg = round(engine.execute(f'SELECT AVG(measurement.tobs) FROM measurement WHERE measurement.date>{start_date}') \
                        .fetchall()[0][0], 2)
    return jsonify({"Avg": tobs_avg, "Max": tobs_max, "Min": tobs_min})


@app.route("/api/v1.0/<start_date>/<end_date>")
def startend_page(start, end):
    start_date = start
    end_date = end

    all_dates = [x[0] for x in engine.execute('SELECT measurement.date FROM measurement').fetchall()]
    date_max_valid = engine.execute('SELECT MAX(measurement.date) FROM measurement').fetchall()[0][0]
    date_min_valid = engine.execute('SELECT MIN(measurement.date) FROM measurement').fetchall()[0][0]


    if dt.datetime.strptime(start, '%Y-%m-%d %H:%M:%S') and dt.datetime.strptime(end, '%Y-%m-%d %H:%M:%S') in [
        dt.datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S') for x in all_dates]:
        tobs_max = session.query(mt.tobs).filter(mt.date >= start_date, mt.date <= end_date) \
                    .order_by(mt.tobs.desc()).first()[0]
        tobs_min = session.query(mt.tobs).filter(mt.date >= start_date, mt.date <= end_date) \
                    .order_by(mt.tobs.asc()).first()[0]
        tobs_avg = round(session.query(func.avg(mt.tobs)).filter(mt.date >= start_date, mt.date <= end_date) \
                      .order_by(mt.tobs.desc()).all()[0][0], 2)

        return jsonify({"Avg": tobs_avg, "Max": tobs_max, "Min": tobs_min})
    else:
        return f'your range must be between {date_min_valid} and {date_max_valid}'

@app.route("/")
def index():
    route_dict = {
        "Lists the precipitation by date": "/api/v1.0/precipitation",
        "Lists station names and their ID's": "/api/v1.0/stations",
        "Lists the last year of temperature data for the most active station": "/api/v1.0/tobs",
        "Returns the Average, Minimum and Maximum Temperature for all dates including and beyond the start date ": "/api/v1.0/<start_data>",
        "Returns the Average, Minimum and Maximum Temperature for the date range": "/api/v1.0/<start_date>/<end_date>",
    }

    return jsonify(route_dict)



if __name__ == "__main__":
    app.run(debug=True)