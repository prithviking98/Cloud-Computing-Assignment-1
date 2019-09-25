from schemas import *
from pyspark.sql import SparkSession
import shutil
import os

def join_handler(inputFile):
	print("handling join query")
	'''for join query, format of input
	line 1: query type //(group/join)
	line 2: table 1 name //(Users/Zipcodes/Movies/Ratings)
	line 3: table 2 name //(Users/Zipcodes/Movies/Ratings)
	line 4: column name for join
	line 5: condition 2 //only simple predicate on some column, lite for now
	eg-
	1)	join
		Users
		Zipcodes
		zipcode
		Users.age > 18

	2)	join
		Users
		Ratings
		userID
		Ratings.rating > 3
	'''

	spark = SparkSession \
		.builder \
		.appName("Python Spark SQL basic example") \
		.config("spark.some.config.option", "some-value") \
		.getOrCreate()

	table1Name = inputFile.readline().rstrip('\n')
	if table1Name == "Users":
		table1 = spark.read.csv("users.csv", schemaUsers, sep=",")
	elif table1Name == "Movies":
		table1 = spark.read.csv("movies.csv", schemaMovies, sep=",")
		table1.createOrReplaceTempView("Movies")
	elif table1Name == "Zipcodes":
		table1 = spark.read.csv("zipcodes.csv", schemaZipcodes, sep=",")
		table1.createOrReplaceTempView("Zipcodes")
	elif table1Name == "Ratings":
		table1 = spark.read.csv("rating.csv", schemaRatings, sep=",")
		table1.createOrReplaceTempView("Ratings")
	else:
		print("invalid table 1 name",table1Name)
		return
	table1.show()
	# print("table1 count",table1.select(table1["userID"]).count())

	table2Name = inputFile.readline().rstrip('\n')
	if table2Name == "Users":
		table2 = spark.read.csv("users.csv", schemaUsers, sep=",")
		table2.createOrReplaceTempView("Users")
	elif table2Name == "Movies":
		table2 = spark.read.csv("movies.csv", schemaMovies, sep=",")
		table2.createOrReplaceTempView("Movies")
	elif table2Name == "Zipcodes":
		table2 = spark.read.csv("zipcodes.csv", schemaZipcodes, sep=",")
		table2.createOrReplaceTempView("Zipcodes")
	elif table2Name == "Ratings":
		table2 = spark.read.csv("rating.csv", schemaRatings, sep=",")
		table2.createOrReplaceTempView("Ratings")
	else:
		print("invalid table 2 name")
		return
	table2.show()
	# print("table2 count",table2.count())


	column = inputFile.readline().rstrip('\n')

	'''
	joinQuery = "SELECT {}.*, {}.* "\
		"FROM {} "\
		"INNER JOIN {} "\
		"ON {}.{} = {}.{}"\
		"".format(table1Name, table2Name, table1Name, table2Name, table1Name, column, table2Name, column)
	'''
	joinQuery = "SELECT * "\
		"FROM {} "\
		"INNER JOIN {} "\
		"ON {}.{} = {}.{}"\
		"".format(table1Name, table2Name, table1Name, column, table2Name, column)
	print(joinQuery)

	result = spark.sql(joinQuery)
	# result = table1Name.join(table2, table1.zipcode == table2.zipcode)
	print(result.schema)
	# result.show()
	# if "output" in os.listdir():
	# 	shutil.rmtree("output") #removing previously made directory
	# result.coalesce(1).write.format("json").save("output")
