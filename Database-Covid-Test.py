import sqlite3

class sqlite_database(): 
    def  __init__ (self):
        pass
            
    def createTable(self,con):
        con.execute('''CREATE TABLE IF NOT EXISTS register_covid_patient (ID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, occupation TEXT, age INTEGER, test TEXT)''')
    
    def insertValues(self,con):
        name = input("Name: ")
        occupation = input("Occupation: ")
        age = int(input("Age: "))
        test = input("Test Result: ")
        con.execute("INSERT INTO register_covid_patient VALUES (?, ?, ?, ?, ?)", (ID, name, occupation, age, test))
        con.rowcount
    
    def callDbDatas(self,con):
        con.execute("SELECT * FROM register_covid_patient")
    
    def printAllDatas(self,con):
        con.execute("SELECT * FROM register_covid_patient")
        print(con.fetchall())

    def saveDatas(self, c):
        c.commit()
    
    def closeConnection(self, c):  
        c.close()
    
        
if __name__ == '__main__':
    value = 0
    c = sqlite3.connect('NewTabCovid_R01.db')
    con = c.cursor()
    database = sqlite_database()
    database.createTable(con)
    answer = input("Would you like to register a new patient? (Y/N) ")
    ID = 0
    while(answer == 'Y'):
        ID = ID + 1
        database.insertValues(con)
        database.saveDatas(c)
        answer = input("Would you like to register a new patient? (Y/N) ")

    database.printAllDatas(con)
    database.closeConnection(c)
