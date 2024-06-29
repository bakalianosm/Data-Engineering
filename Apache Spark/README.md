


# Apache Spark


In this directory I have two projects that use `Apache Spark` framework for distributed data processing for . In detail:

1. `RDD.ipynb` : This Python notebook leverages the PySpark `RDD API` to analyze a parallel corpus of transcriptions from the European Parliament, containing texts in Greek and English. It involves tasks such as:

    a. loading & preprocessing the text
    b  computing the 10 most frequent words in each language, and using the parallel corpus to mine translation pairs by pairing words found in lines of equal length in both languages.

2. `DataFrames_SQL.ipynb` : This Python notebook leverages the PySpark `DataFrames/SQL API` to analyze a dataset of [Los Angeles Parking Citations](https://www.kaggle.com/datasets/cityofLA/los-angeles-parking-citations), that has been preloaded into an `HDFS` cluster. 
 
The tasks that I have done are among other:
    a. loading, exploring and preprocessing the dataset
    b. finding the maximum fine amount
    c. finding the top 20 most frequent vehicle makes
    d. finding what’s the most frequent colour value for Toyotas


    

