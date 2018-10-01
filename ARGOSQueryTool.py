# ARGOSQueryTool.py
#
# Description: Parses a line of ARGOS tracking data 
#
# Created by: Andrea Alatorre-Troncoso (aa449@duke.edu)
# Created on: Sept, 2018

# Create a variable pointing to the file with no header
fileName = "SaraNoHeader.txt"

# Open the file as a read-only file object
fileObj = open(fileName, 'r')

# Read in all lines in the text file into a list variable
lineStrings = fileObj.readlines()
print("There are {} records in the file".format(len(lineStrings)))

#Close the file object
fileObj.close()

#Create empty dictionaries
dateDict = {}
locationDict = {}
try:
    #Loop with While loop
    for lineString in lineStrings:

        # Use the split command to parse the items in lineString into a list object
        lineData = lineString.split("\t")

        # Assign variables to specfic items in the list
        recordID = lineData[0]              # ARGOS tracking record ID
        obsDateTime = lineData[2]           # Observation date and time (combined)
        obsDate = obsDateTime.split()[0]    # Observation date - first item in obsDateTime list object
        obsTime = obsDateTime.split()[1]    # Observation time - second item in obsDateTime list object
        obsLC = lineData[3]                 # Observation Location Class
        obsLat = lineData[5]                # Observation Latitude
        obsLon = lineData[6]                # Observation Longitude

        #Filter out bad data
        if obsLC in("1","2","3"):

            #Adds values to dictionaries
            dateDict[recordID] = obsDate
            locationDict[recordID] = (obsLon, obsLat)
        
    # Indicate script is complete
    print ("Finished")

    #Ask user for a date, specifying the format
    userDate = input("Enter a date (M/D/YYYY):")

    #Check the date
    if not "/" in userDate:
        print("Wrong format, duh")
        
    #Create empty key list
    keyList = []

    #Loop through the date dictionary
    for k, v in dateDict.items():
        #See if the date (value) matches the user date
        if v == userDate:
            keyList.append(k)

    #Loop through each key and report the associated date location        
    for key in keyList:
        theDate = dateDict[key]
        theLocation = locationDict[key]
        theLat = theLocation[0]
        theLon = theLocation[1]
        print("Record {0}: Sara was seen at {1}N-{2}W, on {3}".format(key,theLat,theLon,theDate))

except Exception as e:
    print(e)