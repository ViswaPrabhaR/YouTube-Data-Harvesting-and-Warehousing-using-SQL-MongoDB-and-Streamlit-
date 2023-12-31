**Project Title**: YouTube Data Harvesting and Warehousing using SQL, MongoDB and Streamlit

**Skills**: Python scripting, Data Collection, MongoDB, Streamlit, API integration, Data Management using MongoDB and SQL

**Domain**: Social Media (Youtube Data Analysis)

**_This project consists of the following components:_**

**Streamlit:** A user-friendly user interface (UI) created with the Streamlit library. Streamlit is a great choice for building data visualization and analysis tools quickly and easily.

**YouTube API Integration:** Integration with the YouTube API to retrieve video and channel information by entering the channel ID.

**MongoDB:** The data that was retrieved from Youtube is stored in a MongoDB database, It is used for storing unstructured data.

**SQL:** Migrate data from the MongoDB to SQL database.

**Data Analysis:** Using Streamlit, provide the user with a few query options. From that menu, choose a question to analyse the data and display the results in a table.

**Introduction**

The goal of the YouTube Data Harvesting and Warehousing project, we will explore how to extract data from various YouTube channels using the Google API and analyze it using Python. 

_We will cover the following key concepts:_

**•	Setting up the Google API credentials**

**•	Connecting to a MongoDB database**

**•	Connecting to a MySQL database**

**•	Extracting channel, video, playlist, and comment data from YouTube**

**•	Storing the extracted data in MongoDB**

**•	Migrating the data from MongoDB to MySQL**

**•	Performing SQL queries on the extracted data**

_**Key Concepts**_

**Google API Credentials**

To access the YouTube API, you need to set up credentials. You can obtain an _**API key**_ from the Google Cloud Console. Make sure to enable the _**YouTube Data API v3**_ for your project and generate an API key. Once you have the API key, you can use it to authenticate your requests to the YouTube API.

**Connecting to MongoDB**

We will use the pymongo library to connect to a MongoDB database. First, install the _**pymongo library**_ using _**pip install pymongo**_. Then, import the library and establish a connection to your MongoDB server using the **_pymongo.MongoClient()_** function. You can specify the connection URL and the database name. Once connected, you can access the collections and perform operations.

**Connecting to MySQL**

We will use the mysql.connector library to connect to a MySQL database. First, install the _**mysql-connector-python**_ library using _**pip install mysql-connector-python**_. Then, import the library and establish a connection to your MySQL server using the _**mysql.connector.connect()**_ function. You can specify the host, user, password, database, and authentication plugin. Once connected, you can execute SQL queries and fetch the results.

**Extracting Data from YouTube**

We will use the Google API client library for Python to interact with the YouTube API. First, install the _**google-api-python-client**_ library using _**pip install google-api-python-client**_. Then, import the necessary modules and create a YouTube object using the _**build()**_ function. You need to pass the API key and the API version as parameters. Once you have the YouTube object, you can make requests to the YouTube API to retrieve channel, video, playlist, and comment data.

**Storing Data in MongoDB**

After extracting the data from YouTube, we can store it in a MongoDB database. We will create a connection to the MongoDB server using the _**pymongo.MongoClient()**_ function. Then, we can access the desired database and collection. We will define functions to extract channel, video, playlist, and comment data from YouTube and store them in the MongoDB collection.

**Migrating Data from MongoDB to MySQL**

To migrate the data from MongoDB to MySQL, we will use the pandas library to convert the MongoDB data into _**pandas DataFrames**_. We will define functions to extract the data from MongoDB and create DataFrames. Then, we can use the _**create_engine()**_ function from the sqlalchemy library to create an engine for the MySQL database. We will establish a connection to the MySQL server using the _**mysql.connector.connect()**_ function. Finally, we can use the _**to_sql()**_  method of the DataFrame to insert the data into MySQL tables.

**Performing SQL Queries**

Once the data is stored in the MySQL database, we can perform SQL queries to analyze the data. We will define functions to execute SQL queries and fetch the results. We can use SQL queries to answer questions.

**Conclusion**

In this project, we have explored how to extract data from YouTube using the Google API and analyze it using Python. We have covered the key concepts of setting up the Google API credentials, connecting to MongoDB and MySQL, extracting data from YouTube, storing data in MongoDB, migrating data from MongoDB to MySQL, and performing SQL queries on the extracted data. By using these techniques, you can extract and analyze YouTube data to gain valuable insights.


