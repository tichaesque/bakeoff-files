import string

outFile = open('directors.nt', 'w')

def writeToFile():
    global outFile
    count = 0

    for line in file('directors.csv', 'r'):
        if count > 0:
            linearray = line.split(',')
            if len(linearray) > 3 and linearray[0][0] == "\"":
                directorname = linearray[0] + linearray[1]
                directorname = directorname[1:-1]
                directorid = linearray[2]

            else:
                directorname =  linearray[0]
                directorid = linearray[1]

            outFile.write("<http://data.linkedmdb.org/resource/director/" + directorid + ">" +
                " <http://data.linkedmdb.org/resource/movie/director_name> " +
                "\"" + directorname + "\" .\n")
            
        count += 1

    count = 0

    for line in file('directors.csv', 'r'):
        if count > 0:
            linearray = line.split(',')
            if len(linearray) > 3 and linearray[len(linearray)-1][-1:] == "\"":
                directorid = linearray[1]
                title = linearray[2] + linearray[3][:-2]
            elif len(linearray) > 3 and linearray[0][0] == "\"":
                directorid =  linearray[2]
                title =  linearray[3]
            else:
                title = linearray[2][:-2]
                directorid = linearray[1]

            outFile.write("<http://data.linkedmdb.org/resource/director/" + directorid + ">" +
                " <http://xmlns.com/foaf/0.1/made> " +
                "\"" + title + "\" .\n")

            
        count += 1

writeToFile()
outFile.close();



