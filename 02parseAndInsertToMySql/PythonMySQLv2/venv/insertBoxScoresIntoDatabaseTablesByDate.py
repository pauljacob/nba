import os
import myFunc2
import mysql.connector

dirPath2 = "D:\\Google Drive\\pauljacob.dataanalyst\\ahgain2\\202003txt"
fileList2 = os.listdir(dirPath2)

folder = "201910txt"
dirPath = "D:\\Google Drive\\pauljacob.dataanalyst\\ahgain3" + "\\" + folder
fileList = os.listdir(dirPath)
print(fileList)


mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="87Wadf^JAFOIUYf*89s7R7q@96A3ryusDF#9e98dfyA%3",
        database="testdb"
    )

mycursor = mydb.cursor()
mycursor.execute("DROP DATABASE IF EXISTS nbadb")
mycursor.execute("CREATE DATABASE nbadb")
#mycursor.execute("DROP TABLE nba_boxscores")

#tableAddText = "IF (EXISTS (SELECT * FROM nba_boxscores." + folder[:7] + "))" \


# someText = "CREATE TABLE IF NOT EXISTS t" + folder[0:6] + " (player_number VARCHAR(20), first_name VARCHAR(20), last_name VARCHAR(20), " \
#               "POS VARCHAR(20), MIN VARCHAR(20), FG VARCHAR(20), FGA VARCHAR(20), 3P VARCHAR(20),  " \
#               "3PA VARCHAR(20), FT VARCHAR(20), FTA VARCHAR(20), OR_ VARCHAR(20), DR VARCHAR(20),  " \
#               "TOT VARCHAR(20), A VARCHAR(20), PF VARCHAR(20), ST VARCHAR(20), TO_ VARCHAR(20),  " \
#               "BS VARCHAR(20), PM VARCHAR(20), PTS VARCHAR(20), DATE VARCHAR(20)," \
#               " HOME_TEAM VARCHAR(20), VISITOR_TEAM VARCHAR(20), TEAM VARCHAR(20))"
#print(type(someText))
#print(type("someText"))
#mycursor.execute(someText)

#mycursor.execute("IF (EXISTS (SELECT * FROM nba_boxscores." + folder[:7] + "))")

sqlFormula = "CREATE TABLE nba_boxscores (player_number VARCHAR(20), first_name VARCHAR(20), last_name VARCHAR(20), " \
              "POS VARCHAR(20), MIN VARCHAR(20), FG VARCHAR(20), FGA VARCHAR(20), 3P VARCHAR(20),  " \
              "3PA VARCHAR(20), FT VARCHAR(20), FTA VARCHAR(20), OR_ VARCHAR(20), DR VARCHAR(20),  " \
              "TOT VARCHAR(20), A VARCHAR(20), PF VARCHAR(20), ST VARCHAR(20), TO_ VARCHAR(20),  " \
              "BS VARCHAR(20), PM VARCHAR(20), PTS VARCHAR(20), DATE VARCHAR(20)," \
              " HOME_TEAM VARCHAR(20), VISITOR_TEAM VARCHAR(20), TEAM VARCHAR(20))"
#mycursor.execute(sqlFormula)
#fff = "INSERT INTO nba_boxscores values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
#          " %s, %s, %s, %s, %s, %s)"


for txtFile in fileList:
    someText = "CREATE TABLE IF NOT EXISTS t" + txtFile[0:8] + " (player_number VARCHAR(20), first_name VARCHAR(20), last_name VARCHAR(20), " \
                  "POS VARCHAR(20), MIN VARCHAR(20), FG VARCHAR(20), FGA VARCHAR(20), 3P VARCHAR(20),  " \
                  "3PA VARCHAR(20), FT VARCHAR(20), FTA VARCHAR(20), OR_ VARCHAR(20), DR VARCHAR(20),  " \
                  "TOT VARCHAR(20), A VARCHAR(20), PF VARCHAR(20), ST VARCHAR(20), TO_ VARCHAR(20),  " \
                  "BS VARCHAR(20), PM VARCHAR(20), PTS VARCHAR(20), DATE VARCHAR(20)," \
                  " HOME_TEAM VARCHAR(20), VISITOR_TEAM VARCHAR(20), TEAM VARCHAR(20))"
    print(txtFile[:8])
    mycursor.execute(someText)
    #dvhList = []
    #dvhList.append(myFunc2.getDateVisitorHomeInfo(txtFile))
    #print("dvhList: " + str(dvhList))

    #print("date: " + date)
    #print("visitor: " + visitor)
    #print("home: " + home)

    filePath = dirPath + '\\' + txtFile
    print("filePath: " + str(filePath))
    colonLines = myFunc2.getColonLines(filePath)
    print("myFunc2.getColonLines(): " + str(colonLines))
    #print("colonLines[3]: " + str(colonLines[3]))
    print(myFunc2.getPlayerStats(filePath, 9, colonLines))

    myFunc2.insertAllPlayerScoresIntoDb(filePath, txtFile, mycursor, mydb)

    #break

print(fileList)
print("DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")

for txtFile in fileList2:
    someText = "CREATE TABLE IF NOT EXISTS t" + txtFile[0:8] + " (player_number VARCHAR(20), first_name VARCHAR(20), last_name VARCHAR(20), " \
                  "POS VARCHAR(20), MIN VARCHAR(20), FG VARCHAR(20), FGA VARCHAR(20), 3P VARCHAR(20),  " \
                  "3PA VARCHAR(20), FT VARCHAR(20), FTA VARCHAR(20), OR_ VARCHAR(20), DR VARCHAR(20),  " \
                  "TOT VARCHAR(20), A VARCHAR(20), PF VARCHAR(20), ST VARCHAR(20), TO_ VARCHAR(20),  " \
                  "BS VARCHAR(20), PM VARCHAR(20), PTS VARCHAR(20), DATE VARCHAR(20)," \
                  " HOME_TEAM VARCHAR(20), VISITOR_TEAM VARCHAR(20), TEAM VARCHAR(20))"
    print(txtFile[:8])
    mycursor.execute(someText)
    #dvhList = []
    #dvhList.append(myFunc2.getDateVisitorHomeInfo(txtFile))
    #print("dvhList: " + str(dvhList))

    #print("date: " + date)
    #print("visitor: " + visitor)
    #print("home: " + home)

    filePath = dirPath2 + '\\' + txtFile
    print("filePath: " + str(filePath))
    colonLines = myFunc2.getColonLines(filePath)
    print("myFunc2.getColonLines(): " + str(colonLines))
    #print("colonLines[3]: " + str(colonLines[3]))
    print(myFunc2.getPlayerStats(filePath, 9, colonLines))

    myFunc2.insertAllPlayerScoresIntoDb(filePath, txtFile, mycursor, mydb)

    #break




