#!/usr/bin/python

# PySpark-extractWords-v1.py
# Submit as the command below:
# spark-submit --jars "spark-csv_2.10-1.4.0.jar,commons-csv-1.4.jar" PySpark-extractWords-v1.py
# 2017-03-10; insilicoscientist[at]gmail.com

'''script to count word frequency from NIH grant abstracts; 
   bacterial names are condensed and normalized'''

# SparkConf: Configuration for a Spark application. Used to set various Spark parameters as key-value pairs.
# SparkContext: Main entry point for Spark functionality. A SparkContext represents the connection to a Spark cluster, 
# and can be used to create RDD and broadcast variables on that cluster.
from pyspark import SparkConf, SparkContext
conf = SparkConf()
sc = SparkContext(conf = conf)

# pyspark.sql will be used for dataframe conversion
from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)

import re
def removePunctuation(text):
	#return re.sub('[^a-z| |0-9]', '', text.strip().lower())
	return re.sub('[^a-z| |0-9|-]', '', text.strip().lower())
	#return re.compile(r'[-.?!,":;()|0-9]')
	#return re.sub("^\d+\s|\s\d+\s|\s\d+$", " ", s) # delete free standing digits
"""Removes punctuation, changes to lowercase, and strips leading and trailing spaces.
Only spaces, letters, and numbers should be retained.  Other characters should be
eliminated. (e.g. it's becomes its)
"""

# Delete free standing digits
def removeDigits(text):
    return re.sub("^\d+\s|\s\d+\s|\s\d+$", "", text.strip()) 
    # return re.sub("^\d+\s|\s\d+\s|\s\d+$|\"|\'|.?!,\(\)", "", text.strip().lower()) 

##Read the CSV file and do substitutions
import csv
def substituteNames(text):
	with open('./bacteria_names_data_with_headerRow.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			#print(row['name'], row['name_joined'])	
			return re.sub(row['name'], row['name_joined'], text.strip())
	
#rdd1 = sc.textFile('file:///home/mahasena/w01/nih.txt').map(removePunctuation1)
#rdd1 = sc.textFile('file:///home/mahasena/w01/nih.txt').map(removePunctuation2)
#rdd1 = sc.textFile('file:///home/mahasena/w02/nih2016.csv').map(removePunctuation1).map(removePunctuation2)
#rdd1 = sc.textFile('file:///home/mahasena/w01/nih.txt').map(removePunctuation1).map(removePunctuation2).map(removePunctuation3)
rdd1 = sc.textFile('file:///afs/crc.nd.edu/user/k/kmahasen/spark_install/test/RePORTER_PRJABS_C_FY2016.csv').map(substituteNames).map(removePunctuation).map(removeDigits)

## Total word count
#rdd1.flatMap(lambda x: x.split()).count() 

# Unique word count
#rdd1.flatMap(lambda x: x.split()).distinct().count() 

# More processing
#results1 = rdd1.flatMap(lambda x: x.split()).map(lambda x: (x,1)).reduceByKey(lambda x,y: x+y).map(lambda x: (x[1],x[0])).sortByKey(False)
#results1.take(5)

##### Stopword work begins ####
# load stopwords from a text file
stopwords = set(line.strip() for line in open('./stopwords.txt', "r"))

# Broadcast this list to all worker processes in the cluster
stopwords_bc = sc.broadcast(stopwords)

# Create two accumulators for counting processed words
stopword_count = sc.accumulator(0)
regular_count = sc.accumulator(0)

## Make a "filter_word" function to call later
def filter_words(w):
     if w in stopwords_bc.value:
         stopword_count.add(1)
         return False
     else:
         regular_count.add(1)
         return True
### Stopword work ends ####


## Extract specific words: work begins ###
extractWords = set(line.strip() for line in open('./bacteria_names_data_combinedName_lowerCase.csv', "r"))
extractWords_bc = sc.broadcast(extractWords)
extractWords_count = sc.accumulator(0)
regular_count = sc.accumulator(0)

       
def extract_words(w):
     if w in extractWords_bc.value:
         extractWords_count.add(1)
         return True
     else:
         regular_count.add(1)
         return False
## Extract specific words: work ends ###

wordCount = rdd1.flatMap(lambda x: x.split()).filter(filter_words).map(lambda x: (x,1)).reduceByKey(lambda x,y: x+y).map(lambda x: (x[1],x[0])).sortByKey(False)
extractWords = rdd1.flatMap(lambda x: x.split()).filter(extract_words).map(lambda x: (x,1)).reduceByKey(lambda x,y: x+y).map(lambda x: (x[1],x[0])).sortByKey(False)

## Save processed file; just if needed to have a look later
#rdd1.saveAsTextFile('file:///home/mahasena/w04/RePORTER_PRJABS_C_FY2016_rdd_out.csv')

# Create a data frame from the rdd
df1 = sqlContext.createDataFrame(wordCount, ['Count', 'Word'])

## Write the data; this will be written as split files with as many number as the nodes processing the data
#df1.write.format('com.databricks.spark.csv').options(header='true').save('file:///home/mahasena/w04/nih-data-wordcount-2016')

## Write the data as single file
df1.coalesce(1).write.format('com.databricks.spark.csv').options(header='true').save('file:///afs/crc.nd.edu/user/k/kmahasen/spark_install/test/RePORTER_PRJABS_C_FY2016_wordCount.csv')

### Write extract words
## Write 
df2 = sqlContext.createDataFrame(extractWords, ['Count', 'Word'])

## Write the data; this will be written as split files with as many number as the nodes processing the data
#df1.write.format('com.databricks.spark.csv').options(header='true').save('file:///home/mahasena/w04/nih-data-wordcount-2016')

## Write the data as single file
df2.coalesce(1).write.format('com.databricks.spark.csv').options(header='true').save('file:///afs/crc.nd.edu/user/k/kmahasen/spark_install/test/RePORTER_PRJABS_C_FY2016_extractWords.csv')

