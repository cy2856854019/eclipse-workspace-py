'''
Created on 2018年12月3日

@author: cy
'''
import pymysql
from twisted.enterprise import adbapi #异步进行数据库处理
from pymysql import cursors

class MysqlTools(object):

    def __init__(self, host='127.0.0.1', user='root', password='123456',
                 database=None, port=3306,charset='utf8mb4'):
        self._conn = pymysql.connect(host=host, 
                                     user=user, 
                                     password=password,
                                     database=database, 
                                     port=port,charset=charset)
        self._cursor = self._conn.cursor()
        
    def createDB(self, db_name='JianShu', character='utf8mb4'):
        sql = '''
            create database if not exists {} default character set {};
        '''.format(db_name, character)
        self._edit(sql)
    
    def dropDB(self, db_name):
        sql = '''
            drop database if exists {};
        '''.format(db_name)
        self._edit(sql)
    
    def createTable(self, db_name='JianShu', table_name='Article'):
        sql = '''
            create table if not exists {}.{} (
            id int primary key auto_increment,
            title varchar(255),
            avatar varchar(255),
            athour varchar(255) ,
            url varchar(255),
            artile_id varchar(255),
            publish_time varchar(255) ,
            content longtext
            )
        '''.format(db_name, table_name)
        self._edit(sql)
        
    def insert(self, item):
#         sql = '''
#         insert into spider3.users(age, name, password) values
#         (18, "zhangsan", "san"),
#         (18, "lisi", "si");
#         '''
        
        sql = """
        insert into JianShu.Article(
            title,avatar,athour,url,artile_id, publish_time, content
          ) 
          values(%s,%s,%s,%s,%s,%s,%s);
        """
        try:
            self._cursor.execute(sql,(item['title'],item['avatar'],item['athour'],item['url'],item['artile_id'],item['publish_time'],item['content']))
            self._conn.commit()
        except Exception as e:
            self._conn.rollback()# 出错 回滚到执行上述sql语句之前
            print('error, msg: ', e)
        
#         self._edit_commit(sql)
    
    def delete(self, sql):
#         sql = '''
#         delete from spider3.users where id=6;
#         '''
        self._edit_commit(sql)
    
    def update(self, sql):
#         sql = '''
#             update spider3.users set id=4 where id=1;
#         '''
        self._edit_commit(sql)
    
    def select_one(self,sql):
        try:
            self._cursor.execute(sql)
            reuslt = self._cursor.fetchone()
            return reuslt
        except Exception as e:
            self._conn.rollback()# 出错 回滚到执行上述sql语句之前
            print('cursor.execute error, msg: ', e)
        
    def select_all(self, sql):
        try:
            self._cursor.execute(sql)
            reuslt = self._cursor.fetchall()
            return reuslt
        except Exception as e:
            self._conn.rollback()# 出错 回滚到执行上述sql语句之前
            print('cursor.execute error, msg: ', e)
            
    def select_many(self, sql):
#         sql = '''
#         select from spdier3.users 
#         '''
        try:
            self._cursor.execute(sql)
            reuslt = self._cursor.fetchmany(4)#查找前四条
            return reuslt
        except Exception as e:
            self._conn.rollback()# 出错 回滚到执行上述sql语句之前
            print('cursor.execute error, msg: ', e)
       
    def _edit(self, sql):
        try:
            self._cursor.execute(sql)
        except Exception as e:
            self._conn.rollback()# 出错 回滚到执行上述sql语句之前
            print('cursor.execute error, msg: ', e)
    
    def _edit_commit(self, sql):
        try:
            self._cursor.execute(sql)
            '''
            对表单数据有改变时（增删改），一定要执行commit 不然是提交不到数据库的
            '''
            self._conn.commit()
        except Exception as e:
            self._conn.rollback()# 出错 回滚到执行上述sql语句之前
            print('_edit_commit error, msg: ', e)
        
    def __del__(self):
        self._cursor.close()
        self._conn.close()
        
class MysqlTools_Twisted(object):
#使用twisted异步处理
    def __init__(self, host='127.0.0.1', user='root', password='123456',
                 database=None, port=3306,charset='utf8'):
        params = {
            'host':host, 
            'user':user, 
            'password':password,
            'database':database, 
            'port':port,
            'charset':charset,
            'cursorclass' : cursors.DictCursor,
            }
        self.dbpool = adbapi.ConnectionPool('pymysql', **params)
    
    def insert_item(self, item):
        defer = self.dbpool.runInteraction(self._insert, item)
        defer.addErrback(self._errback, item)
    
    def _errback(self, error, item):
        print('='*10 + ' error ' + '='*10)
        print(error)
        print('+'*10 + ' error ' + '+'*10)
        print(item['content'])
        print('='*10 + ' error ' + '='*10)
        
    def _insert(self, cursor, item):
        sql = """
                insert into JianShu.Article(
                    title,avatar,athour,url,artile_id, publish_time, content
                  ) 
                  values(%s,%s,%s,%s,%s,%s,%s);
                """
        cursor.execute(sql,(item['title'],item['avatar'],item['athour'],item['url'],item['artile_id'],item['publish_time'],item['content']))
    
        
if __name__ == '__main__':
    mysqltool = MysqlTools()
    mysqltool.createDB()
    mysqltool.createTable('spider3', 'users')
        