class EXTRACTCMD:
    def __init__(self, file1):
        self.cmdhist = []
        self.file = file1

    def readFile(self):
        with open(self.file) as fp:
            for line in fp:
                if "CMD:" in line:
                    newline = line.split("'")
                    if newline[1] not in self.cmdhist:
                        self.cmdhist.append(newline[1])

    def getcmdhist(self):
        return self.cmdhist


class EXTRACTSECTIONS:
    def __init__(self, file):
        self.sectiondata = {"Start of Crashinfo Collection": [], "Show Alignment": [], "Malloc and Free Traces": [],
                            "Stack Trace": [], "Context": [], "Stack Dump": [], "Process Level Info": [],
                            "Interrupt Level Stack Dump": [], "Interrupt Stack": [], "Register Memory Dump": [],
                            "show chunk failures": []}
        self.file = file

    def readSections(self):
        currentKey = ""
        with open(self.file) as fp:
            for line in fp:
                if line == "\n":
                    continue
                for key, value in self.sectiondata.items():
                    if "= " + key in line:
                        currentKey = key
                        continue
                if currentKey != "" and currentKey not in line:
                    self.sectiondata[currentKey].append(line)

    def returnDetails(self):
        return self.sectiondata