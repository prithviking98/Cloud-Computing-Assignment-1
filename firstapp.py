from pyspark import SparkContext

sc = SparkContext("local", "first app")
file = "test.txt"
print(file)
text_file = sc.textFile(file).cache()
counts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)
print("counts collected")
print(counts)
counts.saveAsTextFile("counts")
