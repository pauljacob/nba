import os
import myFunc
import mysql.connector

#dirPath = "D:\\Google Drive\\pauljacob.dataanalyst\\ahgain2\\202003txt"
dirPath = "D:\\Google Drive\\pauljacob.dataanalyst\\ahgain3\\201910txt"
fileList = os.listdir(dirPath)
print(fileList)


mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="87Wadf^JAFOIUYf*89s7R7q@96A3ryusDF#9e98dfyA%3",
        database="testdb"
    )

mycursor = mydb.cursor()
mycursor.execute("DROP DATABASE nbadb")
mycursor.execute("CREATE DATABASE nbadb")
mycursor.execute("DROP TABLE nba_boxscores")

sqlFormula = "CREATE TABLE nba_boxscores (player_number VARCHAR(20), first_name VARCHAR(20), last_name VARCHAR(20), " \
              "POS VARCHAR(20), MIN VARCHAR(20), FG VARCHAR(20), FGA VARCHAR(20), 3P VARCHAR(20),  " \
              "3PA VARCHAR(20), FT VARCHAR(20), FTA VARCHAR(20), OR_ VARCHAR(20), DR VARCHAR(20),  " \
              "TOT VARCHAR(20), A VARCHAR(20), PF VARCHAR(20), ST VARCHAR(20), TO_ VARCHAR(20),  " \
              "BS VARCHAR(20), PM VARCHAR(20), PTS VARCHAR(20), DATE VARCHAR(20)," \
              " HOME_TEAM VARCHAR(20), VISITOR_TEAM VARCHAR(20), TEAM VARCHAR(20))"
mycursor.execute(sqlFormula)
#fff = "INSERT INTO nba_boxscores values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
#          " %s, %s, %s, %s, %s, %s)"


for txtFile in fileList:
    #dvhList = []
    #dvhList.append(myFunc.getDateVisitorHomeInfo(txtFile))
    #print("dvhList: " + str(dvhList))

    #print("date: " + date)
    #print("visitor: " + visitor)
    #print("home: " + home)

    filePath = dirPath + '\\' + txtFile
    print("filePath: " + str(filePath))
    colonLines = myFunc.getColonLines(filePath)
    print("myFunc.getColonLines(): " + str(colonLines))
    #print("colonLines[3]: " + str(colonLines[3]))
    print(myFunc.getPlayerStats(filePath, 9, colonLines))

    myFunc.insertAllPlayerScoresIntoDb(filePath, txtFile, mycursor, mydb)

    #break






