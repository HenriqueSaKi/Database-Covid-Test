#calling the lib
import sqlite3

#connecting with database, if not exists, it'll be created
c = sqlite3.connect('teste_covid.db')

con = c.cursor()

#Creating table, if you prefer, you can use the command "CREATE TABLE IF NOT EXISTS" for don't execute the command, if the table already exists
#con.execute('''CREATE TABLE cadastro_pacientes_covid (ID, name, occupation, test_result)''')

#Inserting manually, values into table
#con.execute("INSERT INTO cadastro_pacientes_covid VALUES (3, 'Peter', 'Baby', 'Negative')")

#After insert values, you can select according to your preference. At this case bellow, I called all tables
con.execute("SELECT * FROM cadastro_pacientes_covid")

#fechall or fechone, is used to print on screen the result of the command "Select"
print (con.fetchall())

#Save changes in db
c.commit()

#Close db connection
c.close()
