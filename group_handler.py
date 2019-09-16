from schemas import *
from pyspark.sql import SparkSession
import shutil

def group_handler(inputFile):
	print("handling group query")
	'''expected input
	line 1: query type //already read
	line 2: table name
	line 3: comma separated columns list (no trailing comma)
	line 4: FUNC(COLUMN1) //just like that in text format
	line 5: X
	eg-
		group
		Users
		age, gender
		COUNT(age)
		18
	'''
	spark = SparkSession \
		.builder \
		.appName("Python Spark SQL basic example") \
		.config("spark.some.config.option", "some-value") \
		.getOrCreate()

	tableName = inputFile.readline().rstrip('\n')

	if tableName == "Users":
		table = spark.read.csv("users.csv", schemaUsers, sep=",")
		table.createOrReplaceTempView("Users")
	elif tableName == "Movies":
		table = spark.read.csv("movies.csv", schemaMovies, sep=",")
		table.createOrReplaceTempView("Movies")
	elif tableName == "Zipcodes":
		table = spark.read.csv("zipcodes.csv", schemaZipcodes, sep=",")
		table.createOrReplaceTempView("Zipcodes")
	elif tableName == "Ratings":
		table = spark.read.csv("rating.csv", schemaRatings, sep=",")
		table.createOrReplaceTempView("Ratings")
	else:
		print("invalid table name")
		return

	table.show()
	columns = inputFile.readline().rstrip('\n')
	func = inputFile.readline().rstrip('\n')
	x = inputFile.readline().rstrip('\n')

	groupByQuery = "SELECT {}, {} "\
	"FROM {} "\
	"GROUP BY {} "\
	"HAVING {}>{}".format(columns, func, tableName, columns, func, x)
	result = spark.sql(groupByQuery)
	result.show()
	shutil.rmtree("output") #removing previously made directory
	result.coalesce(1).write.format("json").save("output")
