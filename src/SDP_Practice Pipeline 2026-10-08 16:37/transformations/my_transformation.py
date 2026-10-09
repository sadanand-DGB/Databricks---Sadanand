from pyspark import pipelines as dp
 
@dp.table
def trips_bronze():
    return spark.readStream.table(
        "samples.nyctaxi.trips"
    )
    
@dp.table
def trips_silver():
    return (
        spark.readStream
        .table("trips_bronze")
        .filter("trip_distance > 0")
    )
    
@dp.materialized_view
def trips_gold():
    return (
        spark.read.table("trips_silver")
        .groupBy("pickup_zip")
        .count()
    )
 
 