#coding=utf8
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib,os,time,re,socket
from HReConf.dataConfig import *
from email.utils import formatdate
from HReLib import sendNotice
import sys
reload(sys)  # 默认编码设置为utf-8
sys.setdefaultencoding('utf-8')

class sendEmail(object):
    def send_mail(self,subject,startTime,endTime,developer,tester,environment=reqUrlTest.ENVIRONMENT,server=EmailInFo.SMTPSERVER,userName=EmailInFo.USERNAME,passWord=EmailInFo.PASSWORD,fro=EmailInFo.SENDER,to=EmailInFo.RECEIVER,toPhone=["13510689423"]):
        msg = MIMEMultipart()
        msg['From'] = fro
        requiredDataList = self.getText(environment,startTime,endTime,developer,tester,toPhone)
        context = requiredDataList[0]
        testResult = requiredDataList[1]

        #测试通过，则不发送邮件通知2017-05-15修改
        if testResult == "通过":
            return 0

        environmentFlag = "[" + environment + "]"
        resultFlag = "------------[" + testResult + "]"
        subject = environmentFlag + subject + resultFlag
        if not isinstance(subject,unicode):
            subject = subject.decode("utf8")
        msg['Subject'] = subject
        msg['To'] = ";".join(to)
        msg['Date'] = formatdate(localtime=True)


        #msg.attach(MIMEText(self.getText(),'plain','utf8'))
        msg.attach(MIMEText("<html>" + context + "</html>",'html','utf8'))

        files = self.getFiles()

        for singleFile in files:
            #octet-stream为二进制数据
            att = MIMEText(open(singleFile,'rb').read(),'base64','utf8')
            att["Content-Type"] = "application/octet-stream"
            att["Content-Disposition"] = 'attachment;filename="%s"' %os.path.basename(singleFile)
            msg.attach(att)

        smtp = smtplib.SMTP()
        smtp.connect(server)
        smtp.login(userName,passWord)
        smtp.sendmail(fro,to,msg.as_string())
        smtp.quit()

    def getFiles(self):
        #定义一个list来存放所有的png文件（即用例执行结果图表）
        files = []
        listDir = os.listdir("..//report")
        for i in listDir:
            if re.match(".*txt",i):
                files.append("..//report//"+i)

            if re.match(".*png",i):
                files.append("..//report//"+i)
        return files

    def getSummaryText(self,fileName):
        total_pass = 0
        total_fail = 0
        with open(fileName) as fileOpen:
            list_data = fileOpen.readlines()
        for i in list_data:
            i = i.strip()
            if re.search("<\[PASS\]>",i):
                total_pass = total_pass + 1
            elif re.search(r"<\[FAIL\]>",i):
                total_fail = total_fail + 1
        return total_pass,total_fail


    def getText(self,environment,startTime,endTime,developer,tester,toPhone):
        ip = socket.gethostbyname(socket.gethostname())
        try:
            passNum = 0
            failNum = 0
            #存放所有失败的测试用例
            list_text = []
            files = self.getFiles()
            for i in files:
                if i.split("/")[-1] == reqUrlTest.FINALFILE.split("/")[-1]:
                    with open(i) as dataFile:
                        allData = dataFile.readlines()
                        for allData_i in allData:
                            if re.search(r"<\[FAIL\]>",allData_i):
                                list_text.append(allData_i.strip())
                    total_pass,total_fail = self.getSummaryText(i)
                    passNum = passNum + total_pass
                    failNum = failNum + total_fail

            total = passNum + failNum
            passRate = round(float(passNum)/total,2)
            passRate = passRate*100
            if failNum > 0 :
                result = "不通过"
                summaryText = "===================概述==================="+"<br>"+ "【运行机器】====【" + ip + "】<br>" + "【所属环境】====【" + environment + "】<br>" + "【开始时间】====【" + startTime + "】<br>" + "【结束时间】====【" + endTime + "】<br>" + "【测试人员】====【" + tester + "】<br>" + "【开发人员】====【" + developer + "】<br>" +\
                          "|总数|=|" + str(total) + "|-|成功|=|" + str(passNum) + "|-|失败|=|" + str(failNum) +"|" + "<font color=\"#FF0000\">" + "-|通过率|=|" + str(passRate) + "%</font>|" +"<br>" +\
                          "<span style=\"font-size:30px;font-weight:bolder;background:red\">" + "|测试结论|-|"+ result +"|" + "</span><br>" + "===================END==================="+"<br>"+"<br>"+"<br>"

                #将异常接口进行解析，用table来修饰
                tableStringStart = "<table border=4 style=\"font-size:12px;align:center\">"
                tableStringEnd = "</table>"
                tableSubject = "<tr bgcolor=red><th>接口序号</th><th>接口名称</th><th>执行时间</th><th>统计结果</th><th>返回结果</th></tr>"
                #接口序号从1开始
                index = 0

                #定义发送短信的内容的列表
                noticeList = []

                for list_text_i in list_text:
                    index = index + 1
                    requireList = list_text_i.split("[")
                    interfaceName = requireList[0]
                    executeTime = requireList[1].split("]")[0]
                    summary = requireList[2].split("]")[0]

                    #新增短信发送
                    if re.search(BugLevel.critical,interfaceName):
                        noticeList.append(executeTime+" "+interfaceName+" "+summary)

                    textResult = requireList[2].split("<---->返回结果为:")[-1]
                    textResult = textResult.replace("<","[").replace(">","]")
                    tableSubject = tableSubject + "<tr><td align=\"center\">"+ str(index) + "</td><td>" + interfaceName+"</td><td>"+executeTime+"</td><td>"+summary+"</td><td>"+textResult+"</td></tr>"

                text = summaryText + tableStringStart + tableSubject + tableStringEnd

                #如果为测试环境，则不管是否为空，都不发送短信
                if str(reqUrlTest.CHECKCODEFLAG) != "0":
                    #如果noticeList不为空，则需要发送短信给相关责任人
                    if noticeList:
                        listString = "\n" + "\n".join(noticeList)
                        #发送多个联系人
                        for person in toPhone:
                            try:
                                sendNotice.sendNotice(person,listString)
                            except:
                                print "发送短息给联系人[",person,"]失败...."
                    else:
                        print "不需要发送短信给相关责任人..........."


            else:
                result = "通过"
                summaryText = "===================概述==================="+"<br>"+ "【运行机器】====【" + ip + "】<br>" + "【所属环境】====【" + environment + "】<br>" + "【开始时间】====【" + startTime + "】<br>" + "【结束时间】====【" + endTime + "】<br>" + "【测试人员】====【" + tester + "】<br>" + "【开发人员】====【" + developer + "】<br>" +\
                          "|总数|=|" + str(total) + "|-|成功|=|" + str(passNum) + "|-|失败|=|" + str(failNum) + "|" + "<font color=\"#009100\">" + "-|通过率|=|" + str(passRate) + "%</font>|" +"<br>" +\
                          "<span style=\"font-size:30px;font-weight:bolder;background:green\">" + "|测试结论|-|"+result+"|" + "</span><br>" + "===================END==================="+"<br>"+"<br>"+"<br>"
                text = summaryText
            #以前的方式
            #text = summaryText + "<br>".join(list_text)
            return text,result
        except:
            text = "自动化测试"
            return text,"不通过"

if __name__ == "__main__":
    subject = DayHRe.SUBJECT
    tester = DayHRe.MODULETESTER
    developer = DayHRe.MODULEDEVELOPER
    startTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    endTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    #sendEmail().send_mail(subject,startTime,endTime,developer,tester,to=ORG.RECEIVER)
    sendEmail().send_mail(subject,startTime,endTime,developer,tester)




