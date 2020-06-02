from pyspark import SparkConf, SparkContext

def main(sc):
    textFile = sc.textFile("integer_list.txt")
    test = textFile.map(lambda x: x.strip())
    ints = test.map(lambda x: int(x))
    even_rdd = ints.filter(lambda x: x % 2 == 0).count()
    odd_rdd = ints.filter(lambda x: x % 2 != 0).count()
    print ("even number -> %s\n" % (even_rdd)  +  "odd number -> %s" % (odd_rdd))
    


if __name__  == "__main__":
    conf = SparkConf().setAppName("MyApp")
    sc = SparkContext(conf = conf)
    main(sc)
    sc.stop()


#spark-submit --master yarn-client --executor-memory 512m --num-executors 3 --executor-cores 1 --driver-memory 512m OddEvenCount.py