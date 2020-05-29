import re
import itertools

lines = list()
pluralsList = list()
stringArrayList = list()
integerArrayList = list()
finalStringList = list()

xmlEncodingTag = "<?xml version=\"1.0\" encoding=\"utf-8\"?>"
resourcesStartTag = "<resources>"
resourcesEndTag = "</resources>"

isPluralData = False
isStringArray = False
isIntegerArray = False
key = ""

filename = "strings.xml"

def readResourceFile():    
    with open(filename) as file:
        for line in file:
            line = line.strip()

            if len(line) == 0:
                continue
    
            if line.startswith("<plurals"):
                isPluralData = True
                pluralsList.append(line)
                continue
            
            if line.startswith("</plurals"):
                isPluralData = False
                pluralsList.append(line)
                continue

            if line.startswith("<string-array"):
                isStringArray = True
                stringArrayList.append(line)
                continue

            if line.startswith("</string-array"):
                isStringArray = False
                stringArrayList.append(line)
                continue
            
            if line.startswith("<integer-array"):
                isIntegerArray = True
                integerArrayList.append(line)
                continue

            if line.startswith("</integer-array"):
                isIntegerArray = False
                integerArrayList.append(line)
                continue

            if line.startswith("<item") | line.startswith("</item"):
                if isPluralData:
                    pluralsList.append(line)
                elif isStringArray:
                    stringArrayList.append(line)
                elif isIntegerArray:
                    integerArrayList.append(line)
                continue

            try:
                key = re.search('<string name=\"(.+?)\"', line).group(1)
            except AttributeError:
                print "Markers not found for line: " + line
                continue
                
            newLine = {"key": key, "line": line}
            lines.append(newLine)

def sortResourceFileAndReturnList():
    sortedLines = sorted(lines, key = lambda k: k["key"])
    stringList = [sortedLine["line"] for sortedLine in sortedLines]
    finalStringList = list(itertools.chain([xmlEncodingTag], [resourcesStartTag], stringList, [''],  pluralsList, [''], stringArrayList, [''], integerArrayList, [resourcesEndTag]))
    return finalStringList

def writeResourceFile(finalStringList):
    with open('sorted.xml', 'w+') as writeFile:
        for sortLine in finalStringList:
            writeFile.write(sortLine + '\n')

def main():
    readResourceFile()
    finalStringList = sortResourceFileAndReturnList()
    writeResourceFile(finalStringList)

if __name__ == "__main__":
    main()