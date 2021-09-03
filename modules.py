# This function reads my file
def readFile(databasePath):
    with open(databasePath, "r") as myFakeDB:
        # Read my file and split by row ("\n")
        info = myFakeDB.read().split("\n")
        # headers: name of the columns
        headers = info[0].split("\t")
        # data: data from my temperature probe
        data = [row.split("\t") for row in info[1:]]
    return (headers, data)

# This function converts the plain text file to a JSON
def plainFileToJSON(headers, data):
    resultJSON = []
    for row in data:
        tempDict = {}
        tempDict[headers[0]] = row[0]
        tempDict[headers[1]] = row[1]
        resultJSON.append(tempDict)
    return(resultJSON)

# This function calls both "readFile()" and "plainFileToJSON()"
# to return a JSON file
def readTxtToJSON(databasePath):
    headers, data = readFile(databasePath)
    myJSON = plainFileToJSON(headers, data)
    return(myJSON)