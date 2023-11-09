**SQL_Alchemy-Challenge - Climate Analysis and Flask API Design**

This challenge involves analysing a climate database using Python, SQLAlchemy ORM queries, Pandas, and Matplotlib. After whihc the project requires the designing process of a Flask API based on the queries that were developed.

**Requirements**

Download the 2 CSV files and sqlite file provided in the Resources folder.

1. Python v3.10.9
2. Install SQL Alchemy
3. Install Numpy
4. Install Pandas
5. Install Datetime
6. Install Matplotlib

**Part 1: Analys and Explore the Climate Data**

In this section, we analysed and explored the climate data using Python, Pandas, and Matplotlib. The following tasks were performed:

- Perform a precipitation analysis and a station analysis.
- For the precipitation analysis:
- Find the most recent date in the dataset.
- Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.
- Load the query results into a Pandas DataFrame.
- Sort the DataFrame values by "date".
- Plot the results using the DataFrame plot method.
- Use Pandas to print the summary statistics for the precipitation data.
- Design a query to calculate the total number of stations in the dataset.
- Design a query to find the most-active stations.
- Using the most-active station id, calculate the lowest, highest, and average temperatures.
- Design a query to get the previous 12 months of temperature observation (TOBS) data.
- Filter by the station that has the greatest number of observations.
- Query the previous 12 months of TOBS data for that station.
- Plot the results as a histogram with bins=12.

**Part 2: Design Your Climate App**

In this section, we design a Flask API based on the queries developed in Part 1. The following routes were created:

1. Start at the homepage.
2. List all the available routes.
   
JSON List for:

1. /api/v1.0/precipitation
2. /api/v1.0/stations
3. /api/v1.0/tobs
4. /api/v1.0/
5. /api/v1.0/ and /api/v1.0//
   

**References**

Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, https://doi.org/10.1175/JTECH-D-11-00103.1Links to an external site., measurements converted to metric in Pandas.
