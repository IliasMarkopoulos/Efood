Part 1 answer is in the part1.sql file

In order to run part 2 (clustering) firstly the modeling dataset needs to be created
This is done by running the sql code 'Clustering_Dataset.sql'
bq-results-20210628-215130-vimdrod198gt.csv is the modeling dataset after running the above code.

The clustering is done with clustering_efood.py code
This code reads as an input the above csv file and creates tables and graphs within python with the main output. 
An excel file with the segments and the original data is also created
