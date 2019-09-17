from pyspark.sql import SparkSession

spark = SparkSession \
		.builder \
		.appName("Python Spark SQL basic example") \
		.config("spark.some.config.option", "some-value") \
		.getOrCreate()
valuesA = [('Pirate',1),('Monkey',2),('Ninja',3),('Spaghetti',4)]
TableA = spark.createDataFrame(valuesA,['name','id'])
TableA.createOrReplaceTempView("ta")

valuesB = [('Rutabaga',1),('Pirate',2),('Ninja',3),('Darth Vader',4)]
TableB = spark.createDataFrame(valuesB,['name','id'])
TableB.createOrReplaceTempView("tb")

TableA.show()
TableB.show()

ta = TableA.alias('ta')
tb = TableB.alias('tb')

# inner_join = ta.join(tb, ta.name == tb.name)
inner_join = spark.sql("select * from ta inner join tb on ta.name = tb.name")
inner_join.show()
print(inner_join.count())
