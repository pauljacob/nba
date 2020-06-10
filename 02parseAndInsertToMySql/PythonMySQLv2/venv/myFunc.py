def getColonLines(filePath):
    colonLineList = [4, 6, 7]
    #print(filePath)
    fp = []
    for i in range(0,2):
        fp.append(open(filePath, 'r'))
        #print(i)
    #print("fp: " + str(fp))
    for i in range(0, 13):
        line = fp[0].readline()
    #print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    cnt = 13
    while line:
        line = fp[0].readline()
        cnt = cnt + 1
        lne = line.split(" ")
        if(lne[0].__contains__(":") == True):
            colonLineList.append(cnt)
        #print("cnt: " + str(cnt))
        #print(lne)
    return colonLineList

def getPlayerStats(filePath, startLine, colonLines):
    cnt = startLine
    fp = goToStartLine(filePath, startLine)
    if cnt == colonLines[3] or cnt == colonLines[5]:
        return 0
    else:
        line = fp.readline()
        return line.split()
        
def goToStartLine(filePath, startLine):
    fp = open(filePath, 'r')
    for i in range(0, startLine - 1):
        fp.readline()
    return fp


def getDateVisitorHomeInfo(txtFile):
    dvh = txtFile.split(".")[0].split("_")
    return dvh[0], dvh[1][0:3], dvh[1][3:6]

#def getCleanUpPlayerStats():


def insertAllPlayerScoresIntoDb(filePath, txtFile, mycursor, mydb):
    colonLines = getColonLines(filePath) #index 4 is 22. add 2 to 22 to get 24 as the beginning of home team player scores
    startLine = 9
    fp = goToStartLine(filePath, startLine)

    fff = "INSERT INTO nba_boxscores values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
          " %s, %s, %s, %s, %s, %s)"

    date, visitor, home = getDateVisitorHomeInfo(txtFile)
    for i in range(0, 5):
        lineList = fp.readline().split()
        print("lineList: " + str(lineList))
        lineList = correctNameInListFirstFive(lineList)
        print("lineList: " + str(lineList))
        lineList = lineList + [date, home, visitor, visitor]
        #lineList = tuple(lineList)
        print("lineList: " + str(lineList))
        mycursor.execute(fff, lineList)

    linesTraveled = 13
    fff = "INSERT INTO nba_boxscores values (%s, %s, %s, 'NA', %s , %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
          "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    visitorLinesRemaining = colonLines[3] - linesTraveled - 1
    print("visitorLinesRemaining: " + str(visitorLinesRemaining))
    for i in range(0, visitorLinesRemaining):
        lineList = fp.readline().split()
        lineList = correctNameInList(lineList)
        if(lineList[3] == 'DND' or lineList[3] == 'DNP' or lineList[3] == 'NWT'):
            fff = "INSERT INTO nba_boxscores values (%s, %s, %s, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', " \
          "'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', %s, %s, %s, %s)"
            lineList = lineList[0:3]
        lineList = lineList + [date, home, visitor, visitor]
        #lineList = tuple(lineList)
        print("lineList: " + str(lineList))
        mycursor.execute(fff, lineList)
    checkEntries(mycursor)

    fp = goToHomeLine(fp, colonLines, visitorLinesRemaining, linesTraveled)
    #print(fp.readline())
    fff = "INSERT INTO nba_boxscores values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
          " %s, %s, %s, %s, %s, %s)"
    for i in range(0, 5):
        lineList = fp.readline().split()
        print("lineList: " + str(lineList))
        lineList = correctNameInListFirstFive(lineList)
        print("lineList: " + str(lineList))
        lineList = lineList + [date, home, visitor, home]
        #lineList = tuple(lineList)
        print("lineList: " + str(lineList))
        mycursor.execute(fff, lineList)
    print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
    checkEntries(mycursor)

    fff = "INSERT INTO nba_boxscores values (%s, %s, %s, 'NA', %s , %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
          "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    homeLinesRemaining = colonLines[5] - colonLines[4] - 6
    for i in range(0, homeLinesRemaining - 1): #??????????????????????????????????????????
        lineList = fp.readline().split()
        lineList = correctNameInList(lineList)
        if(lineList[3] == 'DND' or lineList[3] == 'DNP' or lineList[3] == 'NWT'):
            fff = "INSERT INTO nba_boxscores values (%s, %s, %s, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', " \
          "'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', %s, %s, %s, %s)"
            lineList = lineList[0:3]
        print('YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY')
        lineList = lineList + [date, home, visitor, visitor]
        # lineList = tuple(lineList)
        print("lineList: " + str(lineList))
        mycursor.execute(fff, lineList)

    mydb.commit()
    return 0

#def naStatsCorrection():


def goToHomeLine(fp, colonLines, visitorLinesRemaining, linesTraveled):
    numLinesToGetToHome = colonLines[4] + 2 - visitorLinesRemaining - linesTraveled
    print("numLinesToGetToHome: " + str(numLinesToGetToHome))
    for i in range(0, numLinesToGetToHome - 1):
        fp.readline()
    return fp


def checkEntries(mycursor):
    mycursor.execute("Select * from nba_boxscores")
    for playerRowEntries in mycursor:
        print(playerRowEntries)

def correctNameInListFirstFive(lineList):
    if (lineList[4] == 'F' or lineList[4] == 'C' or lineList[4] == 'G'):
        lineList[2] = lineList[2] + ' ' + lineList[3]
        lineList.pop(3)
    return lineList


def correctNameInList(lineList):
    if (lineList[4] == 'F' or lineList[4] == 'C' or lineList[4] == 'G'):
        lineList[2] = lineList[2] + ' ' + lineList[3]
        lineList.pop(3)
    elif (lineList[4].__contains__(":") == True):
        lineList[2] = lineList[2] + ' ' + lineList[3]
        lineList.pop(3)
    elif (lineList[4] == 'DNP' or lineList[4] == 'DND' or lineList[4] == 'NWT'):
        lineList[2] = lineList[2] + ' ' + lineList[3]
        lineList.pop(3)
    return lineList






