from pyspark import SparkConf, SparkContext  # import some Spark classes into the program

def makeTuple(line):
    words = line.split()
    return (words[0], int(words[1]))
def main(sc):
    textFile = sc.textFile("dept_salary.txt")
    wordList = textFile.map(lambda line: makeTuple(line))
    sumCount = wordList.combineByKey(lambda value: (value, 1),
                             lambda x, value: (x[0] + value, x[1] + 1),
                             lambda x, y: (x[0] + y[0], x[1] + y[1]))

    sumByKey = sumCount.map(lambda (label, (value_sum, count)): (label, value_sum))
    print sumByKey.collectAsMap()
    sumByKey.saveAsTextFile("/user/root/dept_sum.txt")


if __name__  == "__main__":
    conf = SparkConf().setAppName("MyApp")
    sc = SparkContext(conf = conf)
    main(sc)
    sc.stop()




#spark-submit --master yarn-client --executor-memory 512m --num-executors 3 --executor-cores 1 --driver-memory 512m deptAverage.py