class Split_String:
    def __init__(self):
        from konlpy.tag import Hannanum 
        from konlpy.utils import pprint
        self.string =[];
        self.hannanum = Hannanum()
    def split_String_Method(self,String):
        self.string = self.hannanum.pos(String)
        return self.string

class Insert_db:
    def __init__(self,ID,PW,URL,DBTABLE):
        self.ID = ID
        self.PW = PW
        self.URL = URL
        self.DBTABLE = DBTABLE
    def insert_tagging_N(self,string_value):
        try :
            conn = pymysql.connect(host =self.URL,user=self.ID, password = self.PW,db=self.DBTABLE,charset='utf8')
            sql2 = """select * from tagging where %s in (select N from tagging)"""
            curs = conn.cursor()
            curs.execute(sql2,(string_value))
            if curs.rowcount < 1 :
                print(string_value)
                sql = """insert into tagging(no,N) values (%s,%s)"""
                curs = conn.cursor()
                curs.execute(sql,(self.get_number(),string_value))
                conn.commit()
        finally :
            conn.close()
            return
    def insert_tagging_E(self,string_value):
        try :
            conn = pymysql.connect(host =self.URL,user=self.ID, password = self.PW,db=self.DBTABLE,charset='utf8')
            sql2 = """select * from tagging where %s in (select E from tagging)"""
            curs = conn.cursor()
            curs.execute(sql2,(string_value))
            if curs.rowcount < 1 :
                sql = """insert into tagging(no,E) values (%s,%s)"""
                curs = conn.cursor()
                curs.execute(sql,(self.get_number(),string_value))
                conn.commit()
        finally :
            conn.close()
            return
    def insert_tagging_P(self,string_value):
        try :
            conn = pymysql.connect(host =self.URL,user=self.ID, password = self.PW,db=self.DBTABLE,charset='utf8')
            sql2 = """select * from tagging where %s in (select P from tagging)"""
            curs = conn.cursor()
            curs.execute(sql2,(string_value))
            if curs.rowcount < 1 :
                sql = """insert into tagging(no,P) values (%s,%s)"""
                curs = conn.cursor()
                curs.execute(sql,(self.get_number(),string_value))
                conn.commit()
        finally :
            conn.close()
            return
    def insert_tagging_M(self,string_value):
        try :
            conn = pymysql.connect(host =self.URL,user=self.ID, password = self.PW,db=self.DBTABLE,charset='utf8')
            sql2 = """select * from tagging where %s in (select M from tagging)"""
            curs = conn.cursor()
            curs.execute(sql2,(string_value))
            if curs.rowcount < 1 :
                sql = """insert into tagging(no,M) values (%s,%s)"""
                curs = conn.cursor()
                curs.execute(sql,(self.get_number(),string_value))
                conn.commit()
        finally :
            conn.close()
            return
    def insert_tagging_I(self,string_value):
        try :
            conn = pymysql.connect(host =self.URL,user=self.ID, password = self.PW,db=self.DBTABLE,charset='utf8')
            sql2 = """select * from tagging where %s in (select I from tagging)"""
            curs = conn.cursor()
            curs.execute(sql2,(string_value))
            if curs.rowcount < 1 :
                sql = """insert into tagging(no,I) values (%s,%s)"""
                curs = conn.cursor()
                curs.execute(sql,(self.get_number(),string_value))
                conn.commit()
        finally :
            conn.close()
            return
    def insert_tagging_J(self,string_value):
        try :
            conn = pymysql.connect(host =self.URL,user=self.ID, password = self.PW,db=self.DBTABLE,charset='utf8')
            sql2 = """select * from tagging where %s in (select J from tagging)"""
            curs = conn.cursor()
            curs.execute(sql2,(string_value))
            if curs.rowcount < 1 :
                sql = """insert into tagging(no,J) values (%s,%s)"""
                curs = conn.cursor()
                curs.execute(sql,(self.get_number(),string_value))
                conn.commit()
        finally :
            conn.close()
            return
    def insert_tagging_X(self,string_value):
        try :
            conn = pymysql.connect(host =self.URL,user=self.ID, password = self.PW,db=self.DBTABLE,charset='utf8')
            sql2 = """select * from tagging where %s in (select X from tagging)"""
            curs = conn.cursor()
            curs.execute(sql2,(string_value))
            if curs.rowcount < 1 :
                sql = """insert into tagging(no,X) values (%s,%s)"""
                curs = conn.cursor()
                curs.execute(sql,(self.get_number(),string_value))
                conn.commit()
        finally :
            conn.close()
            return
    def get_number(self):
        try:
            self.conn = pymysql.connect(host =self.URL,user=self.ID, password = self.PW,db=self.DBTABLE,charset='utf8')
            self.curs = self.conn.cursor()
            sql = "select no from tagging order by no"
            self.curs.execute(sql)
            count = self.curs.rowcount
        finally:
            self.conn.close()
        return count+1
    def update_N(self):
        try :
            conn = pymysql.connect(host = self.URL,user=self.ID,password = self.PW, db=self.DBTABLE,charset ='utf8',autocommit=True)
            sql2 = "select N from tagging where N is not null"
            curs = conn.cursor()
            curs.execute(sql2)
            rows = curs.fetchall()
            tuple_a = ()
            list_a = ()
            curs2 = conn.cursor()
            for row in rows:
                print(row)
                k = int(input())
                tuple_a =(k,)+row
                sql = """update tagging set counting = %s where N = %s"""
                curs2.execute(sql,tuple_a)
        finally:
            conn.close()
    def update_P(self):
        try :
            conn = pymysql.connect(host = self.URL,user=self.ID,password = self.PW, db=self.DBTABLE,charset ='utf8',autocommit=True)
            sql2 = "select P from tagging where P is not null and counting = 0"
            curs = conn.cursor()
            curs.execute(sql2)
            rows = curs.fetchall()
            tuple_a = ()
            list_a = ()
            curs2 = conn.cursor()
            for row in rows:
                print(row)
                k = int(input())
                tuple_a =(k,)+row
                sql = """update tagging set counting = %s where P = %s"""
                curs2.execute(sql,tuple_a)
        finally:
            conn.close()
import first_setting
import os
# import pymysql

os.system('rm -r __pycache__')    

with open("380.txt",mode = "r",encoding="utf-8") as open_file:
    list_String = []
    string_commend = Split_String()
    while True:
        k = open_file.readline()
        if not k : break
        tuple_string  = string_commend.split_String_Method(k)
        for i in tuple_string:
            list_String.append(i)
list_String.append(('N','송제섭'))

# dbconnection = Insert_db("songmag","1234","localhost","OpenSW")

with open("test_string.txt","w") in open_file:
    for i in list_String:
        if 'N' in i[1] :
            open_file.write("N > " +i)
           # dbconnection.insert_tagging_N(i[0])
        if 'E' in i[1] :
            open_file.write("E > " +i)
            #dbconnection.insert_tagging_E(i[0])
        if 'P' in i[1] :
            open_file.write("P > " +i)
            #dbconnection.insert_tagging_P(i[0])
        if 'M' in i[1] :
            open_file.write("M > " +i)
            #dbconnection.insert_tagging_M(i[0])
        if 'I' in i[1] :
            open_file.write("I > " +i)
            #dbconnection.insert_tagging_I(i[0])
        if 'J' in i[1] :
            open_file.write("J > " +i)
            #dbconnection.insert_tagging_J(i[0])
        if 'X' in i[1] :
            open_file.write("X > " +i)
            #dbconnection.insert_tagging_X(i[0])

# dbconnection.update_P()
