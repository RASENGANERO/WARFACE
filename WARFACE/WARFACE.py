#import requests
#from bs4 import BeautifulSoup
#import os
#import xlsxwriter
#import pandas as pd
#import time
#p=requests.get('http://api.warface.ru/achievement/catalog').json()
#p=[str(a['name']) for a in p]

#def replaced(s):
#    for v in range(len(s)):
#        s[v]=str(s[v]).replace('Ⅰ','I').replace('Ⅱ','II').replace('Ⅲ','III')
#    return s

#def set_count(s):
#    q=s
#    fed=[]
#    for v in range(len(q)):
#        r=str(q[v]).split(' ')
#        r=[a for a in r if str(a).isdigit()==True]
#        if len(r)==0:
#            fed.append(1)
#        else:
#            fed.append(r[0])
#    return fed

#def src(s1,k):
#    s=requests.get(s1)
#    s=BeautifulSoup(s.text,'html.parser').find_all('img')#'div',{'class':'floatnone'})#[2::]
#    #s=[a.get_text() for a in s]
#    s=[a.get('src') for a in s]
#    s=[a for a in s if str(a).startswith('https://')==True]# and str(a).endswith('.png')==True]
#    del s[0]
#    #print(s[0])

#    b=requests.get(s1)
#    b=BeautifulSoup(b.text,'html.parser').find_all('td')[2::]
#    b=[a.get_text() for a in b]
#    b=[a for a in b if str(a).endswith('\n\n')==True]
     
    

    


#    ced=requests.get(s1)
#    ced=BeautifulSoup(ced.text,'html.parser').find_all('span')[1::]
#    ced=[a.get_text() for a in ced]
#    ced=[a for a in ced if str(a).startswith(k+', связанные с')!=True]
    
        

#    ced=replaced(ced)
#    b=replaced(b)
#    del b[0]
#    ced=[a for a in ced if str(a)!='Мета-достижения']
#    ced=[a for a in ced if str(a)!='Эмблемы']
#    ced=[a for a in ced if str(a)!='\xa0']
#    ced=[a.replace(': ',' ').replace('"','').replace(':',' ').replace('?','') for a in ced]

#    ced=list(filter(None,ced))
#    b=list(filter(None,b))
#    b=[str(a).replace(': ',' ').replace('"','').replace(':',' ').replace('\xa0',' ')\
#        .replace(' 0','0').replace('\n','').replace('?','').replace(' 5','5').strip() for a in b]
    
#    if k=="Значки":del b[622]
    
#    for v in range(len(b)):
#        if k=="Нашивки" or k=="Жетоны":
#            if str(b[v]).startswith('Флаг')!=True:# or str(b[v]).endswith('флаг')!=True:
#                b[v]=str(b[v]).replace(ced[v],'').strip()
#            if ced[v]=='Пацифистский флаг':
#                b[v]=str(ced[v])
#        if k=="Значки":
#            if str(b[v]).find('Знак «')!=-1:
#                b[v]='Знак «'+str(ced[v])+'»'
#            else:
#                b[v]=str(b[v]).replace(ced[v],'').strip()
#            if str(b[v])=='Значок а':
#                b[v]='Знак '+str(ced[v])+'a'
#            if str(b[v]).startswith(ced[v])==True:
#                b[v]=str(b[v]).replace(ced[v],'')
        


#    lk=[]
#    count=set_count(b)
#    type=[k]*len(b)
#    b=[str(a).replace('«','').replace('»','') for a in b]
#    for v in range(len(b)):lk.append([str(ced[v]),str(b[v]),str(count[v]),str(type[v])])
#    df=pd.DataFrame(lk)
#    writer = pd.ExcelWriter('D:/Projects/WARFACE/WARFACE/'+k+'/'+k+'.xlsx')
#    df.to_excel(writer,sheet_name=k,index=False)
#    writer.save()
#    #for v in range(len(ced)):
#    #    sed=requests.get(s[v])
#    #    f=open('D:/Projects/WARFACE/WARFACE/'+k+'/'+str(v+1)+'.'+str(ced[v]).replace('?','')+'.png','wb')
#    #    f.write(sed.content)
#    #    f.close()
#    #    print('Скачано : ',v+1,' из ',len(ced))
#    #    time.sleep(1.5)
#    #for v in range(len(b)):
#    #    print(b[v],'     ',v)
#            # not in 
    
        


#src('https://ru.warface.com/wiki/index.php/Значки',"Значки")
#src('https://ru.warface.com/wiki/index.php/Жетоны','Жетоны')
#src('https://ru.warface.com/wiki/index.php/Нашивки',"Нашивки")

##Ⅱ

##Прицельный ответ Ⅰ', 'Прицельный ответ Ⅱ
##'Смертельная буря Ⅰ', 'Смертельная буря Ⅱ'
##'I'
##print(p)
##s2=requests.get('http://api.warface.ru/user/achievements/?name=выафпфвапуккп&server=[1]').json()
##print(s2)

##Ⅲ












PATHSED='D:/Projects/WARFACE/WARFACE/'
import sys
from PyQt5 import Qt
from PyQt5.QtWidgets import (QWidget,QGridLayout,QApplication,QTableWidget,QHeaderView,QAbstractItemView,QTableWidgetItem,
                             QLabel)
from PyQt5.QtCore import *
from PyQt5 import *
from PyQt5.QtGui import *
import pandas as pd
import os
import requests
class IconDelegate(Qt.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(IconDelegate, self).initStyleOption(option, index)
        option.decorationSize = option.rect.size()

class WarfaceGUI(QWidget):
    
    def __init__(self,*args):
        super().__init__()
        self.initUI()


    def initUI(self):
        
        self.grid=QGridLayout()
        self.table=QTableWidget()
        self.setWindowTitle('Warface')
        
        self.create_table()

        self.achievement=["Значки","Жетоны","Нашивки"]


        self.image=list()
        self.data=list()


        
        #self.select()
        #self.set_table()
        
        self.achiv=self.set_value_achiv()
        

        self.grid.addWidget(self.table)
        self.setLayout(self.grid)

        self.setGeometry(250,250,1250,550)
        self.show()




    def set_value_achiv(self):
        achiv=requests.get('http://api.warface.ru/user/achievements/?name=выафпфвапуккп&server=[1]').json()
        all_achiv=requests.get('http://api.warface.ru/achievement/catalog').json()
        for v in range(len(achiv)):
            for q in range(len(all_achiv)):
                if achiv[v]['achievement_id']==all_achiv[q]['id']:
                    achiv[v]['name']=all_achiv[q]['name']
        return achiv
        #print(len(s2),len(p))

        #return 0

    def select(self):
        for v in range(len(self.achievement)):
            self.data.extend(self.get_data(self.achievement[v]+"/"+self.achievement[v]+".xlsx",self.achievement[v]))
            

    def get_data(self,path2,sp):
        lk=[]
        datas=pd.read_excel(PATHSED+path2,index_col=False)
        for v in range(len(datas.index)):
            s=datas.loc[v].tolist()
            lk.append([str(a) for a in s])
            p=PATHSED+"/"+sp+"/"+str(v+1)+'.'+s[0]+'.png'       
            self.image.append(p)
        return lk

        
    def create_table(self):
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(['Изображение','Название','Описание','Необходимо','Выполнено','Завершено'])
        
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table.verticalHeader().setVisible(False)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
   

    def setter_item(self,text,row,column):
        it = QTableWidgetItem(str(text))
        it.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.table.setItem(row,column,it)



    def set_table(self):
        delegate = IconDelegate(self.table)
        self.table.setItemDelegateForColumn(0, delegate) 
        for v in range(len(self.data)):
            
            self.table.insertRow(self.table.rowCount())
            self.setter_item(self.data[v][0],self.table.rowCount()-1,1)
            self.setter_item(self.data[v][1],self.table.rowCount()-1,2)
            self.setter_item(self.data[v][2],self.table.rowCount()-1,3)
            #self.setter_item(self.data[v][2],self.table.rowCount()-1,4)
            #self.setter_item(self.data[v][2],self.table.rowCount()-1,5)
            
            label = QLabel() 
            pixmap = QPixmap(self.image[v])
            label.setPixmap(pixmap)
            label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.table.setCellWidget(self.table.rowCount()-1, 0, label)
        
        self.table.resizeRowsToContents()
        self.table.resizeColumnsToContents()
        self.table.setColumnWidth(0,520)
        self.table.horizontalHeader().setSectionResizeMode(0,QHeaderView.Fixed)
        

if __name__=='__main__':
    app=QApplication(sys.argv)
    exe=WarfaceGUI()
    sys.exit(app.exec_())