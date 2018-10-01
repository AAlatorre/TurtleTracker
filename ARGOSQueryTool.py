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

    #Adds values to dictionaries
    dateDict[recordID] = obsDateTime
    locationDict[recordID] = (obsLat, obsLon)
    
# Indicate script is complete
print ("Finished")
