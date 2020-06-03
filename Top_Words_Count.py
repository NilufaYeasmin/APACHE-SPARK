from pyspark import SparkConf, SparkContext




def main(sc):
    textFile = sc.textFile("shakespeare_100.txt")
    wordList = textFile.flatMap(lambda line: line.split())
    wordCount = wordList.map(lambda word: (word,1))
    counts = wordCount.reduceByKey(lambda v1, v2: v1+v2)
    output = counts.map(lambda (k, v): (v, k)).sortByKey(False)
    output.saveAsTextFile("/user/root/Top_word_count_result.txt")
    #print(output.max(lambda x: x[10]))
    #print(topK)


if __name__  == "__main__":
    conf = SparkConf().setAppName("MyApp")
    sc = SparkContext(conf = conf)
    main(sc)
    sc.stop()

#spark-submit --master yarn-client --executor-memory 512m --num-executors 3 --executor-cores 1 --driver-memory 512m Topcount.py