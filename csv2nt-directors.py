import string

outFile = open('directors.nt', 'w')

def writeToFile():
    global outFile
    count = 0

    for line in file('directors.csv', 'r'):
        if count > 0:
            linearray = line.split(',')
            directorname =  linearray[0]
            directorid = linearray[1]
            title = linearray[2][:-2]

            outFile.write("<http://data.linkedmdb.org/resource/director/" + directorid + ">" +
                " <http://data.linkedmdb.org/resource/movie/director_name> " +
                "\"" + directorname + "\" .\n")
            
        count += 1

    count = 0

    for line in file('directors.csv', 'r'):
        if count > 0:
            linearray = line.split(',')
            directorname =  linearray[0]
            directorid = linearray[1]
            title = linearray[2][:-2]

            outFile.write("<http://data.linkedmdb.org/resource/director/" + directorid + ">" +
                " <http://xmlns.com/foaf/0.1/made> " +
                "\"" + title + "\" .\n")

            
        count += 1

writeToFile()
outFile.close();



