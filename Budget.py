
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost", 
    user = "root",
    password = "2mrTDTK8HhubTinUaEWh",
    database = "purchasetransaction"
)

mycursor = mydb.cursor()
#Database creation
#mycursor.execute("CREATE DATABASE purchaseTransaction")

#Check that database was created
#mycursor.execute("SHOW DATABASES")
#for x in mycursor:
#    print(x)

#print(mydb)

#Create table of transactions with date, category, and cost
#mycursor.execute("CREATE TABLE transactions (date DATE, category VARCHAR(255), cost DECIMAL(10,2)) ")

#Delete contents of table
mycursor.execute("DELETE FROM transactions")

#Insert into table
sql = "INSERT INTO transactions (date, category, cost) VALUES (%s, %s, %s)"
#data = '2023-03-04', 'clothing', 72.8

#mycursor.execute(sql, data)

#Insert multiple entries into table
data = [
    ('2023-03-04', 'clothing', 72.8), 
    ('2023-03-01', 'groceries', 34),
    ('2023-03-02', 'clothing', 63.8),
    ('2023-03-04', 'recreation', 140),
    ('2023-03-04', 'utilities', 164.23),
    ('2023-03-08', 'restaurant', 95),
    ('2023-03-12', 'restaurant', 34.56),
    ('2023-03-13', 'entertainment', 15.99),
    ('2023-03-19', 'groceries', 93.87),
    ('2023-03-21', 'groceries', 24.66)
]


mycursor.executemany(sql, data)
mydb.commit()
print(mycursor.rowcount, "transactions inserted")

#Load data from text file into table. Loading local data is disabled and would have to be changed on client and server
#mycursor.execute("LOAD DATA LOCAL INFILE '/TransactionsToImport.txt' INTO TABLE transactions")


#Print tables and print contents
#mycursor.execute("SHOW TABLES")
#for x in mycursor:
#    print(x)

#mycursor.execute("SELECT * FROM transactions")
#displayTable = mycursor.fetchall()
#for row in displayTable:
#    print(row)
#    print("\n")


#Print groceries entries
#sql = "SELECT * FROM transactions WHERE category = 'groceries'"
#mycursor.execute(sql)
#groceriesTable = mycursor.fetchall()
#for row in groceriesTable:
#    print(row)
#    print("\n")

# Print sum of entries of the specified category
def sumByCategory(category):
    sql = "SELECT SUM(cost) FROM transactions WHERE category = %s" #%s is a placeholder for a variable
    mycursor.execute(sql, (category,)) #the (,) around the string parameter is necessary
    totalGroceries = mycursor.fetchall()[0][0]
    print("You spent", totalGroceries , "on", category)

sumByCategory('groceries')
sumByCategory('clothing')
sumByCategory('recreation')
sumByCategory('restaurant')
sumByCategory('entertainment')

mycursor.close()
