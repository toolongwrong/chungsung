class Split_String:
    def __init__(self):
        from konlpy.tag import Kkma
        from konlpy.utils import pprint
        self.string =[];
        self.kkma = Kkma()
    def split_String_Method(self,String):
        self.string = self.kkma.pos(String)
        return self.string

class Insert_db:
    def __init__(self,list_value,ID,PW,URL,DBTABLE):
        self.value = list_value
        self.ID = ID
        self.PW = PW
        self.URL = URL
        self.DBTABLE = DBTABLE
    def connect_database(self):
        import os
        import sys
        os.system('pip install --upgrade pip')
        os.system('pip install PyMySQL')
        import pymysql
        self.conn = pymysql.connect(host =self.URL,user=self.ID, password = self.PW,db=self.DBTABLE,charset='utf8')
    def insert_data(self,sql):
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        self.curs.execute(sql)
        self.conn.close()


import first_setting
import os
os.system('rm -r __pycache__')    
with open("test2.txt",mode = "r",encoding="utf-8") as open_file:
    list_String = []
    string_commend = Split_String()
    while True:
        k = open_file.readline()
        if not k : break
        list_String.append(string_commend.split_String_Method(k))
for i in list_String:
    print(i)

