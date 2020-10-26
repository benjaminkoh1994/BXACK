from fpdf import FPDF
from ssh import *
from extract import *

if __name__ == '__main__':
    while True:
        print("Option A: Collect Cisco Forensic Evidence")
        print("Option B: Analyze Cisco Forensic Evidence")
        userOption = input("Please choose an option: ").lower()
        if userOption == "a":
            while True:
                userIP = input("Remote Host: ")
                username = input("Username: ")
                password = input("Password: ")
                enablePw = input("Enable Password: ")
                sshConnection(userIP, username, password, enablePw)
                userExit = input("Do you wish to continue? ").lower()
                if userExit == "yes" or userExit == "y":
                    continue
                else:
                    break

        elif userOption == "b":
            while True:
                try:
                    fileName = input("File-Path: ")
                    # extract CMD
                    extracter = EXTRACTCMD(fileName)
                    extracter.readFile()
                    # extract sections
                    extractSect = EXTRACTSECTIONS(fileName)
                    extractSect.readSections()
                    sectionDict = extractSect.returnDetails()
                    break
                except Exception as e:
                    print(e)
                    continue

            while True:
                try:
                    print("===========================================", "Menu List",
                          "=======================================")
                    print("Option 1: Commands History")
                    print("Option 2: Show start of Crash Info Collection")
                    print("Option 3: Show Alignment")
                    print("Option 4: Show Malloc and Free Traces")
                    print("Option 5: Show Stack Trace")
                    print("Option 6: Show Context")
                    print("Option 7: Show Stack Dump")
                    print("Option 8: Show process level info")
                    print("Option 9: Show Interrupt Level Stack Dump")
                    print("Option 10: Show Interrupt Stack")
                    print("Option 11: Show Register Memory Dump")
                    print("Option 12: Show chunk failures")
                    print("Option 13: Merge and Output file")
                    print("Option 14: Exit")
                    userInput = int(input("Choose an Option: "))
                except ValueError:
                    print("Please enter a valid option\n")
                    continue

                if userInput == 1:
                    print("===========================================", "Commands History",
                          "=======================================")
                    for line in extracter.getcmdhist():
                        print(line)
                elif userInput == 2:
                    print("===========================", "Start of Crash Info Collection",
                          "=============================")
                    for line in sectionDict["Start of Crashinfo Collection"]:
                        print(line)
                elif userInput == 3:
                    print("===========================", "Show Alignment", "=============================")
                    for line in sectionDict["Show Alignment"]:
                        print(line)
                elif userInput == 4:
                    print("===========================", "Malloc and Free Traces", "=============================")
                    for line in sectionDict["Malloc and Free Traces"]:
                        print(line)
                elif userInput == 5:
                    print("===========================", "Stack Trace", "=============================")
                    for line in sectionDict["Stack Trace"]:
                        print(line)
                elif userInput == 6:
                    print("===========================", "Context", "=============================")
                    for line in sectionDict["Context"]:
                        print(line)
                elif userInput == 7:
                    print("===========================", "Stack Dump", "=============================")
                    for line in sectionDict["Stack Dump"]:
                        print(line)
                elif userInput == 8:
                    print("===========================", "Process Level Info", "=============================")
                    for line in sectionDict["Process Level Info"]:
                        print(line)
                elif userInput == 9:
                    print("===========================", "Interrupt Level Stack Dump", "=============================")
                    for line in sectionDict["Interrupt Level Stack Dump"]:
                        print(line)
                elif userInput == 10:
                    print("===========================", "Interrupt Stack", "=============================")
                    for line in sectionDict["Interrupt Stack"]:
                        print(line)
                elif userInput == 11:
                    print("===========================", "Register Memory Dump", "=============================")
                    for line in sectionDict["Register Memory Dump"]:
                        print(line)
                elif userInput == 12:
                    print("===========================", "chunk failures", "=============================")
                    for line in sectionDict["show chunk failures"]:
                        print(line)
                elif userInput == 13:
                    Path = input("Enter a file path: ")
                    try:
                        # create PDF file
                        number = 1
                        pdf = FPDF()
                        pdf.add_page()
                        pdf.set_font("Arial", 'B', size=14)
                        pdf.cell(200, 15, txt="Commands History", ln=number, align="C")
                        number += 1
                        for line in extracter.getcmdhist():
                            pdf.set_font("Arial", size=10)
                            pdf.cell(200, 5, txt="#" + line, ln=number, align="L")
                            number += 1

                        for key, value in sectionDict.items():
                            pdf.set_font("Arial", 'B', size=14)
                            pdf.cell(200, 15, txt=key, ln=number, align="C")
                            number += 1
                            for v in value:
                                pdf.set_font("Arial", size=10)
                                pdf.cell(200, 5, txt=v, ln=number, align="L")
                                number += 1
                        pdf.output(Path+".pdf")
                        print("File had been saved.")
                    except Exception as e:
                        print("File unable to save due to ", e)
                elif userInput == 14:
                    break
                else:
                    print("Please enter a valid option [1 to 14].")
        else:
            print("Please choose a valid option. (A or B)")
            continue







