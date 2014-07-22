import string
import re

outFile = open('directors.nt', 'w')

def writeToFile():
    global outFile
    count = 0

    for line in file('directors.tsv', 'r'):
        if count > 0:
            linearray = line.split('\t')
            directorname =  linearray[0]
            directorid = re.findall(r"['\"](.*?)['\"]", linearray[1])[0]

            outFile.write("<http://data.linkedmdb.org/resource/director/" + directorid + ">" +
                " <http://data.linkedmdb.org/resource/movie/director_name> " +
                directorname + " .\n")
            
        count += 1

    count = 0

    for line in file('directors.tsv', 'r'):
        if count > 0:
            linearray = line.split('\t')
            title = linearray[2][:-2]
            directorid = re.findall(r"['\"](.*?)['\"]", linearray[1])[0]

            outFile.write("<http://data.linkedmdb.org/resource/director/" + directorid + ">" +
                " <http://xmlns.com/foaf/0.1/made> " +
                title + "\" .\n")

            
        count += 1

writeToFile()
outFile.close();



