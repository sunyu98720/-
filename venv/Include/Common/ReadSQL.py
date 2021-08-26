import pymysql
from Config.ReadConfig import ReadConfig

class Read_sql():
    def __init__(self,sql,database=None):
        dbtest = ReadConfig(database)
        self.host = dbtest.get_db('host')
        self.username = dbtest.get_db('username')
        self.password = dbtest.get_db('password')
        self.port = dbtest.get_db('port')
        self.database = dbtest.get_db('database')
        self.sql = sql
    def sqlExecute(self):
        conn = pymysql.connect(
            host=self.host,
            port=int(self.port),
            user=self.username,
            password=self.password,
            database=self.database,
            charset='utf8'
        )
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(self.sql)
        data = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return data

if __name__ == '__main__':
    sql = "select * from sys_log limit 10"
    read_sql = Read_sql(sql,'SCRM_DATABASE')
    print(read_sql.sqlExecute())

    # print(code[0]['num'])
