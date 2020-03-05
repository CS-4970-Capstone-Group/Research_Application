import pymysql.cursors
#connect with the database
#db = pymysql.connect(host='127.0.0.1',user='root',passwd='12345678',db='GhostRiders',port=3306,charset='utf8')
#host: This is the IP address, because I am local here, so fill in 127.0.0.1, you can also fill in localhost.
#user: username, if you are also local, fill in root
#passwd: This is the password. Fill in the password you set.
#db: This is the database name
#port: This is the port, the local is generally 3306
#charset: This is the encoding method, which must be consistent with the encoding method of your database, or whether the connection fails
connect = pymysql.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='12345678',
    db='GhostRiders',
    charset='utf8'
)
# Get cursor
cursor = connect.cursor()

# Inster the data
sql = "INSERT INTO Subjects (subject_id) VALUES ( '%s')"
data = ('TRM101')
cursor.execute(sql % data)
connect.commit()
print('Successfully insterted', cursor.rowcount, 'data')

# Update the data
sql = "UPDATE Subjects SET age = %d WHERE subject_id = '%s' "
data = (62, 'TRM101')
cursor.execute(sql % data)
connect.commit()
print('Successfully updated', cursor.rowcount, 'data')

# Querying the data
sql = "SELECT age FROM Subjects WHERE subject_id = '%s' "
data = ('TRM101',)
cursor.execute(sql % data)
for row in cursor.fetchall():
    print("age:%d" % row)
print('Find out', cursor.rowcount, 'data')

# Deleting the data
sql = "DELETE FROM Subjects WHERE subject_id = '%s' LIMIT %d"
data = ('TRM101', 1)
cursor.execute(sql % data)
connect.commit()
print('Successfully deleted', cursor.rowcount, 'data')

# Close the connection
cursor.close()
connect.close()

