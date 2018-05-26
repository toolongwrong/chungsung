class Split_String:
    def __init__(self):
        self.string =[];
    def split_String_Method(self,String):
        self.string = String.split(" ");
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

        

