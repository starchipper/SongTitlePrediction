import csv

file1 = "../train.csv"
file2 = "../test.csv"
file3 = "../development.csv"

def convert(f):
    csvFile = f
    file = open(csvFile, "r")
    csvRead = csv.reader(file, delimiter = ",")
    titlesList = []
    lyrics = []

    for row in csvRead:
        if row[3] != "text":
            titlesList.append(row[1])
            lyrics.append(row[3])

    newtitleslist = []
    for ii in range(0, len(titlesList)):
        titles = str(titlesList[ii].lower())
        newtitles = titles.replace('\n', " ").replace(',', " ").replace('.', " ").replace('?', " ").replace('!', " ")\
            .replace('\'', " ").replace('\"', " ").replace(':', " ").replace(';', " ").replace('(', " ").replace(')', " ")\
            .replace('[', " ").replace(']', " ").replace('_', " ")
        newtitleslist.append(newtitles)

    newcsv = open(f, "w")
    with newcsv:
        writer = csv.writer(newcsv)
        for jj in range(0, len(newtitleslist)):
            title = str(newtitleslist[jj])
            songlyric = str(lyrics[jj])
            datarow = [[title, songlyric]]
            writer.writerows(datarow)

convert(file1)
convert(file2)
convert(file3)
    
    