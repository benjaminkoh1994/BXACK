from fpdf import FPDF
import paramiko
import time
import difflib


class ssh:
    def __init__(self, ip, username, password, enablePw):
        self.ip = ip
        self.username = username
        self.password = password
        self.enablePw = enablePw

        
    def compareFiles(self):
        commandlist =['show running-config', 'show startup-config']
        runningconf=[]
        startcon = []
        try:
            remote_conn_pre = paramiko.SSHClient()
            remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            print("Please wait while we are connecting you...") 
            remote_conn_pre.connect(self.ip,port=22,username=self.username,password=self.password)       
            remote_conn = remote_conn_pre.invoke_shell()
            remote_conn.send("terminal length 0\n")
            time.sleep(.5)

            remote_conn.send("enable \n")
            time.sleep(.5)
            remote_conn.send(self.enablePw)
            time.sleep(.5)
            remote_conn.send("\n")
            
            output = remote_conn.recv(65535).decode(encoding='utf-8')
            
            for i in commandlist:
                print ("Executing " + i)
                remote_conn.send(i + ' \n')
                time.sleep(5)
                output = remote_conn.recv(65535).decode(encoding='utf-8')
                if i == 'show running-config':
                    for line in output.split("\n"):
                        runningconf.append(line)

                elif i == "show startup-config":
                    for line in output.split("\n"):
                        startcon.append(line)
            
            self.compareOutputs(runningconf, startcon)

              
            remote_conn_pre.close()
        except Exception as e:
            print(e)
            
    def compareOutputs(self, run, start):
        d = difflib.Differ()
        diff = d.compare(start, run)
        print ('\n'.join(diff))
        
 
    def sshConnection(self):
        commandlist =['show history all','show clock detail','show startup-config','show reload','show ip route','show cdp nei detail','show ip arp','show ip interface', 'show ip int brief','show tcp brief all','show sockets','show ip cache flow','show ip cef','show logging','show processes']
        try:
            remote_conn_pre = paramiko.SSHClient()
            remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            print("Please wait while we are connecting you...") 
            remote_conn_pre.connect(self.ip,port=22,username=self.username,password=self.password)       
            remote_conn = remote_conn_pre.invoke_shell()
            remote_conn.send("terminal length 0\n")
            time.sleep(.5)

            remote_conn.send("enable \n")
            time.sleep(.5)
            remote_conn.send(self.enablePw)
            time.sleep(.5)
            remote_conn.send("\n")
            
            output = remote_conn.recv(65535).decode(encoding='utf-8')
            
            for i in commandlist:
                print ("Executing " + i)
                remote_conn.send(i + ' \n')
                time.sleep(5)
                output = remote_conn.recv(65535).decode(encoding='utf-8')
                f = open(i + ".txt",'w')
                f.write(output)

            remote_conn_pre.close()
            self.makePDF(commandlist)
        except Exception as e:
            print(e)


    def makePDF(self, commandlist):
        print("Making PDF File Please wait.....")
        lineNumber =1;
        pdf = FPDF()
        pdf.add_page()
        for i in commandlist:
            opnTxt = open(i + ".txt","r")
            rline = opnTxt.readlines()
            pdf.set_font("Arial", 'B', size=14)
            pdf.cell(200, 15, txt=i, ln=lineNumber,align="C")
            lineNumber +=1
            for z in rline:
                pdf.set_font("Courier", size=9)
                if len(z)<100:
                    pdf.cell(200,3,txt=z,ln=lineNumber,align="L")
                    lineNumber +=1
                else:
                    pdf.cell(200,3,txt=z[1:90],ln=lineNumber,align="L")
                    print (z[1:100])
                    lineNumber +=1
                    pdf.cell(200,3,txt=z[90:],ln=lineNumber,align="L")
                    lineNumber +=1
        pdf.output('Combine.pdf','F')
       
