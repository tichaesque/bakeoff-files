import string

outFile = open('actors.nt', 'w')

def writeToFile():
    global outFile
    count = 0

    for line in file('actors.csv', 'r'):
        if count > 0:
            linearray = line.split(',')
            actorname =  linearray[0]
            actorid = linearray[1]
            title = linearray[2][:-2]

            outFile.write("<http://data.linkedmdb.org/resource/actor/" + actorid + ">" +
                " <http://data.linkedmdb.org/resource/movie/actor_name> " +
                "\"" + actorname + "\" .\n")
            
        count += 1

    count = 0
    
    for line in file('actors.csv', 'r'):
        if count > 0:
            linearray = line.split(',')
            actorname =  linearray[0]
            actorid = linearray[1]
            title = linearray[2][:-2]

            outFile.write("<http://data.linkedmdb.org/resource/actor/" + actorid + ">" +
                " <http://data.linkedmdb.org/resource/movie/performance> " +
                "\"" + title + "\" .\n")
            
        count += 1

    

writeToFile()
outFile.close();


