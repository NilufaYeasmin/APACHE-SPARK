# Hello and Welcome to my Portfolio Folder!

This repository contains the documents of PySpark projects that I completed as part of my Master of Data Science and Analytics program at Ryerson University.

## PySpark program to count Odd & Even from Integer List.
** integer_list - The input data file to count the Odd & Even number from Integer List

### Submit a job to find Odd & Even Count from spark cluster without using the shell
spark-submit --master yarn-client --executor-memory 512m --num-executors 3 --executor-cores 1 --driver-memory 512m Odd_Even_Count.py

### Commands on Pyspark Shell for Odd & Even : 
textFile = sc.textFile("integer_list.txt")
test = textFile.map(lambda x: x.strip())
ints = test.map(lambda x: int (x))
odd_rdd = ints.filter(lambda x: x % 2 != 0).count()
ints.take(10)
print(odd_rdd)
even_rdd = ints.filter(lambda x: x % 2 == 0).count()
print "even number -> %s" % (even_rdd)
print "even number -> %s\n" % (even_rdd)  +  "odd number -> %s" % (odd_rdd)
print(even_rdd)

## PySpark program to find Salary Sum Per Department from Dept Salary Input Data.
** dept_salary - The input data file to find Salary Sum Per Department from Dept Salary Input Data

### Submit a job to find Salary Sum Per Department from spark cluster without using the shell
spark-submit --master yarn-client --executor-memory 512m --num-executors 3 --executor-cores 1 --driver-memory 512m Dept_Average_Salary.py

### Inspecting the output
[root@sandbox lab]# hadoop fs -ls /user/root/dept_sum.txt    [dept_sum output file initialized from PySpark Script]

## PySpark program to find Top Word count from large text corpus
** shakespeare_100.txt - The input data file to count the occurences of each word 

### Submit a job to find Top Word count from spark cluster without using the shell
spark-submit --master yarn-client --executor-memory 512m --num-executors 3 --executor-cores 1 --driver-memory 512m Top_Words_Count.py

### Inspecting the output
[root@sandbox lab]# hadoop fs -ls /user/root/Top_word_count_result.txt     [output file initialized from PySpark Script]
