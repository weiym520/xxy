# -*- coding: utf-8 -*-
import mysql.connector
from mysql.connector import Error


class MysqlOperation():
   """
   对数据库进行操作，比如新增库、表，查询表数据
   """
   def __snipeit_mysql(self,host,user,password,database):
      """
      创建私有方法，在被导入其他模块时便不会被直接的调用，省却了加载模块时开启连接数据库的开销
      :param host: 数据库主机IP
      :param user: 数据库用户名
      :param password: 数据库密码
      :param database: 数据库名
      :return:"""
      try:
        # 创建数据库连接
        self.db = mysql.connector.connect(
           host = host,
           user = user,
           password = password,
           database = database
        )
        if self.db.is_connected():
           print("数据库连接成功！")
           return self.db
      except Error as e:
        print(f"连接失败: {e}")


   def ec(self,selelect,name):
      """
      判断数据库或者是数据表是否存在，存在则返回Ture
      :param selelect: 查询sql语句
      :param name: 表名或者是库名
      :return:
      """
      # 创建游标对象
      self.cursor.execute(selelect)
      data_name = self.cursor.fetchall()
      self.flag = False
      for i in data_name:
         if name in i:
            self.flag = True
            break
      return self.flag

   def operation(self):
      """
      创建表或者库
      :return:
      """
      self.db = MysqlOperation().__snipeit_mysql("192.168.181.12", "root", "123456", "snipeit")
      # self.cursor = self.db.cursor()
      # 创建一个名为"mydatabase"的新数据库
      self.cursor = self.db.cursor()
      mydatabase_flag = MysqlOperation().ec("show databases","mydatabase")
      if mydatabase_flag == False:
            self.cursor.execute("CREATE DATABASE mydatabase")
      # 创建一个名为"customers"的新数据
      tabase_flag = MysqlOperation().ec("show tables","customers")
      if tabase_flag == False:
         self.cursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
     # 关闭游标和数据库连接
      self.cursor.close()
      self.db.close()

   def select_mysql(self,table_name,CustomFields_name):
      """
      :param table_name: 数据库表的名字
      :param CustomFields_name: 待查询的数据
      :return:
      """
      self.db = MysqlOperation().__snipeit_mysql("192.168.181.12", "root", "123456", "snipeit")
      # self.cursor = self.db.cursor()
      self.cursor = self.db.cursor()
      # 使用snipeit 的数据库查询数据
      sql = "SELECT name FROM '" + table_name.replace("'", "") + "' WHERE name = '" + CustomFields_name + "'"
      self.cursor.execute(sql.replace("'", "",2))
      # print(sql.replace("'", "",2))
      res = self.cursor.fetchone()
      self.db.commit()
      # # 关闭游标和数据库连接
      self.cursor.close()
      self.db.close()
      print("数据库已经关闭！")
      return res[0]
      # print("resualt ：",res[0])




if __name__=="__main__":
    conn_test = MysqlOperation()
    conn_test.select_mysql('custom_fieldsets','CustomFields_XxyWym00011761151552.5342155')

