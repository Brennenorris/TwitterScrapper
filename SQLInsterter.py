cursor = connection.cursor()

# Example data to insert
data = ("tweet_id_value", "tweet_text_value", ...)

# SQL query to insert data
insert_query = "INSERT INTO twitter_data (tweet_id, tweet_text, ...) VALUES (%s, %s, ...)"

# Execute the query
cursor.execute(insert_query, data)

# Commit the changes
connection.commit()

# Close the cursor and the connection
cursor.close()
connection.close()
