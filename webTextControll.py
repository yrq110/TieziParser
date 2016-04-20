# -*- coding: utf-8 -*-
import sys
import re
import urllib2
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time
import ui_webTextDialog
#import bfs_urlList
class WebTextDialog(QDialog,ui_webTextDialog.Ui_WebTextDialog):
    def __init__(self, url, parent=None):
        super(WebTextDialog, self).__init__(parent)
        self.url=url
        self.setupUi(self)
        self.urlButton.setFocusPolicy(Qt.NoFocus)
        self.updateUi()
        self.urlButton.clicked.connect(self.getURL)
        self.tableWidget.setColumnCount(1)
        
    @pyqtSignature("QString")
    def on_urlEdit_textEdited(self, text):
        self.url = str(self.urlEdit.text())
        self.updateUi()
        print self.url
    
    @pyqtSlot()    
    def getURL(self):
        str = ""
        self.mainTextBrowser.text=str
        baseURL = self.url
        seeLZ = 0
        floorTag = 1
        tag_sum = 0 
        tag_count = 0
        bdtb = BDTB(baseURL,seeLZ,floorTag)
        text,text_tag,text_user=bdtb.start()
        for item in text:
            for van in item:
                self.mainTextBrowser.append(van.decode('utf-8'))
                self.mainTextBrowser.append('--------------------------------------')
        for td in text_user:
            for tr in td:
                tag_sum += 1
        self.tableWidget.setRowCount(tag_sum)
        self.tableWidget.setHorizontalHeaderLabels(["tag"])
        for td in text_user:
            for tr in td:
                self.newItem = QTableWidgetItem(tr.decode('utf-8'))
                self.tableWidget.setItem(tag_count,1,self.newItem)
                tag_count+=1
                
       # startURL = self.url   
       # parser = URLList()  
       # parser.start_a(startURL)
        #getURLList(startURL,parser)
        #if parser.URLqueue.empty() == False:  
           # start = time.clock()
           # url = parser.URLqueue.get()  
           # print url  
           # bdtb = BDTB(url,seeLZ,floorTag)

        
    def updateUi(self):
        enable = not self.urlEdit.text().isEmpty() 
        self.urlButton.setEnabled(enable)
	

    
class Tool:
    removeImg = re.compile('<img.*?>| {7}|')
    removeAddr = re.compile('<a.*?>|</a>')
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    replaceTD= re.compile('<td>')
    replacePara = re.compile('<p.*?>')
    replaceBR = re.compile('<br><br>|<br>')
    removeExtraTag = re.compile('<.*?>')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePara,"\n    ",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        return x.strip()
 
 
class BDTB:
    def __init__(self,baseUrl,seeLZ,floorTag):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz='+str(seeLZ)  
        self.tool = Tool()
        self.file = None
        self.floor = 1
        self.defaultTitle = u"output"
        self.floorTag = floorTag

    def getPage(self,pageNum):
        try:
            url = self.baseURL+ self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read().decode('utf-8')
        except urllib2.URLError, e:
            #if hasattr(e,"reason"):
            #print u"连接失败,错误原因",e.reason
            return None

    def getTitle(self,page):
        pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>',re.S)
        result = re.search(pattern,page)
        if result:
            return result.group(1).strip()
        else:
            return None

    def getOtherTag(self,page):
        pattern = re.compile('<em>(.*?)</em>',re.S)
        result = re.findall(pattern,page)
        tag_contents = []
        for item in result:
            tag_content = "\n"+self.tool.replace(item)+"\n"
            tag_contents.append(tag_content.encode('utf-8'))
        return tag_contents
    
    def getUserName(self,page):
        pattern = re.compile('<a data-field=.*?blank">(.*?)</a>',re.S)
        result = re.findall(pattern,page)
        user_contents = []
        for item in result:
            user_content = "\n"+self.tool.replace(item)+"\n"
            user_contents.append(user_content.encode('utf-8'))
        return user_contents
        
    def getPageNum(self,page):
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
        result = re.search(pattern,page)
        if result:
            return result.group(1).strip()
        else:
            return None

    def getContent(self,page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        items = re.findall(pattern,page)
        contents = []
        for item in items:
            content = "\n"+self.tool.replace(item)+"\n"
            contents.append(content.encode('utf-8'))
        return contents
 
    #def setFileTitle(self,title):
        #if title is not None:
        #    self.file = open(title + ".txt","w+")
        #else:
        #    self.file = open(self.defaultTitle + ".txt","w+")
 
    def writeData(self,contents):
        #allText = []
        for item in contents:
            if self.floorTag == '1':
                floorLine = "\n" + str(self.floor) + u"floor\n"
                print floorLine.decode('utf-8')
                #self.file.write(floorLine)
            #self.file.write(item)
            #print item.decode('utf-8')
            #allText.append(item)
            #self.mainTextBrowser.append(item)
            self.floor += 1
        #return allText
 
    def start(self):
        text = []
        text_tag = []
        text_user = []
        indexPage = self.getPage(1)
        pageNum = self.getPageNum(indexPage)
        title = self.getTitle(indexPage)
        #self.setFileTitle(title)
        if pageNum == None:
            print "URL已失效，请重试"
            return
        try:
            print "该帖子共有" + str(pageNum) + "页"
            for i in range(1,int(pageNum)+1):
                print "正在处理第" + str(i) + "页数据"
                page = self.getPage(i)
                contents = self.getContent(page)
                tag_contents = self.getOtherTag(page)
                user_contents = self.getUserName(page)
                text.append(contents)
                text_tag.append(tag_contents)
                text_user.append(user_contents)
                self.writeData(contents)
            return text,text_tag,text_user
            return text
        except IOError,e:
            print "异常，原因" + e.message
        finally:
            print "任务完成"
 


if __name__ == "__main__":
    import sys
    url=u'http://www.baidu.com'
    app = QApplication(sys.argv)
    form = WebTextDialog(url)
    form.show()
    app.exec_()
    
    
