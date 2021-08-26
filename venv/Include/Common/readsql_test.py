import pymysql
from Config.ReadConfig import ReadConfig

class Read_sql():
    def __init__(self,database=None):
        dbtest = ReadConfig(database)
        self.host = dbtest.get_db('host')
        self.username = dbtest.get_db('username')
        self.password = dbtest.get_db('password')
        self.port = dbtest.get_db('port')
        self.database = dbtest.get_db('database')
    def sqlExecute(self,sql):
        conn = pymysql.connect(
            host=self.host,
            port=int(self.port),
            user=self.username,
            password=self.password,
            database=self.database,
            charset='utf8'
        )
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        data = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return data

if __name__ == '__main__':
    sql = "select count(1) from motherbaby_post"
    read_sql = Read_sql('DORIS_TEST')
    print(read_sql.sqlExecute(sql))

    # print(code[0]['num'])
