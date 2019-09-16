from group_handler import group_handler
from join_handler import join_handler
'''
spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
'''


#reading query parameters from input file
with open("input.txt","r") as inputFile:
	queryType = inputFile.readline().rstrip('\n')
	if queryType == "group":
		group_handler(inputFile)
	elif queryType == "join":
		join_handler(inputFile)
	else:
		print("invalid query type",queryType)


