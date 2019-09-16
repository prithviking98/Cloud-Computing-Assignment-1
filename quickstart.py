from pyspark.sql import SparkSession
from pyspark.sql.types import *

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

schemaUsers = StructType().add("userid",LongType()) \
	.add("age", IntegerType()) \
	.add("gender", StringType()) \
	.add("occupation", StringType()) \
	.add("zipcode", LongType())

schemaZipcodes = StructType().add("zipcode", LongType()) \
	.add("zipcodeType", StringType()) \
	.add("city", StringType()) \
	.add("state", StringType())

schemaMovies = StructType().add("movieID", LongType()) \
	.add("title", StringType()) \
	.add("releaseDate", StringType()) \
	.add("unknown", IntegerType()) \
	.add("action", IntegerType()) \
	.add("adventure", IntegerType()) \
	.add("animation", IntegerType()) \
	.add("children", IntegerType()) \
	.add("comedy", IntegerType()) \
	.add("crime", IntegerType()) \
	.add("documentary", IntegerType()) \
	.add("drama", IntegerType()) \
	.add("fantasy", IntegerType()) \
	.add("film_noir", IntegerType()) \
	.add("horror", IntegerType()) \
	.add("musical", IntegerType()) \
	.add("mystery", IntegerType()) \
	.add("romance", IntegerType()) \
	.add("sci_fi", IntegerType()) \
	.add("thriller", IntegerType()) \
	.add("war", IntegerType()) \
	.add("western", IntegerType()) \

schemaRatings = StructType().add("userID", LongType()) \
	.add("movieID", LongType()) \
	.add("rating", IntegerType()) \
	.add("timestamp", LongType())

Users = spark.read.csv("users.csv", schemaUsers, sep=",")
Zipcodes = spark.read.csv("zipcodes.csv", schemaZipcodes, sep=",")
Movies = spark.read.csv("movies.csv", schemaMovies, sep = ",")
Ratings = spark.read.csv("rating.csv", schemaRatings, sep = ",")

# Users.cache()
# Zipcodes.cache()
# Movies.cache()
# Ratings.cache()

Users.createOrReplaceTempView("Users")
Zipcodes.createOrReplaceTempView("Zipcodes")
Movies.createOrReplaceTempView("Movies")
Ratings.createOrReplaceTempView("Ratings")

Users.show()
Zipcodes.show()
Movies.show()
Ratings.show()

spark.sql("select userID from Ratings").show()

joinQuery = "SELECT {}.*, {}.* FROM {} INNER JOIN {} ON {}"
'''
# print(joinQuery.format("Users","Zipcodes", "Users.zipcode = Zipcodes.zipcode"))
# spark.sql(joinQuery.format("Users","Zipcodes", "Users.zipcode = Zipcodes.zipcode")).show()
df = spark.sql(joinQuery.format("Users","Zipcodes","Users","Zipcodes", "Users.zipcode = Zipcodes.zipcode"))
print(df.schema)
df.show()
# Users.join(Zipcodes, Users.zipcode == Zipcodes.zipcode)
'''

groupBy = "SELECT occupation, max(age) "\
	"FROM Users "\
	"GROUP BY occupation "\
	"HAVING max(age)>18"

gb = spark.sql(groupBy)
gb.show()
