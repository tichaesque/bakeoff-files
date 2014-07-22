import string
import re

outFile = open('actors.nt', 'w')

def writeToFile():
    global outFile
    count = 0

    for line in file('actors.csv', 'r'):
        if count > 0:
            linearray = line.split(',')
            if len(linearray) > 3 and linearray[0][0] == "\"":
                actorid =  linearray[2]
                actorname = linearray[0] + linearray[1]
                actorname = actorname[1:-1]
            else:
                actorid =  linearray[1]
                actorname = linearray[0]

            outFile.write("<http://data.linkedmdb.org/resource/actor/" + actorid + ">" +
                " <http://data.linkedmdb.org/resource/movie/actor_name> " +
                "\"" + actorname + "\" .\n")
            
        count += 1

    count = 0
    
    for line in file('actors.csv', 'r'):
        if count > 0:
            linearray = line.split(',')
            if len(linearray) > 3 and linearray[len(linearray)-1][-1:] == "\"":
                actorid =  linearray[1]
                title = linearray[2] + linearray[3][:-2]
            elif len(linearray) > 3 and linearray[0][0] == "\"":
                actorid =  linearray[2]
                title =  linearray[3]
            else:
                actorid =  linearray[1]
                title = linearray[2][:-2]

            outFile.write("<http://data.linkedmdb.org/resource/actor/" + actorid + ">" +
                " <http://data.linkedmdb.org/resource/movie/performance> " +
                "\"" + title + "\" .\n")
            
        count += 1

    

writeToFile()
outFile.close();


