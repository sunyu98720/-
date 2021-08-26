import unittest
from Common.readsql_test import Read_sql
from time import time, sleep
from numpy import *
import threading
from concurrent.futures import ThreadPoolExecutor, wait
import jsonpath
import pandas as pd
import xlrd
import openpyxl
from pandas import DataFrame
from pyhive import hive

class MyTestCase(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.dorisDrive = Read_sql('DORIS_TEST')
        cls.a = 0

    def ten_time(self, sql, times):


        time_list = []
        print('执行sql:', sql)
        print('执行次数:', times)
        for i in range(times):
            start_time = time()
            self.dorisDrive.sqlExecute(sql)
            end_time = time() - start_time
            time_list.append(end_time)
        avg_time = mean(time_list)
        print('平均耗时:', avg_time)

    def test_count(self):
        sql = 'SELECT count(1) from test_sy a join test_sy_1 b on a.id = b.id '
        self.ten_time(sql,5)

    def tes_regexp(self):
        sql = "select * from motherbaby_post where content regexp '奶粉' limit 10 "
        self.ten_time(sql, 3)

    def tes_demo_threading(self):
        threads = []
        t1 = threading.Thread(target=self.tes_count)
        t2 = threading.Thread(target=self.tes_regexp)
        threads.append(t1)
        threads.append(t2)
        # threads.append(watchThread)
        print(threads)
        for i in threads:
            i.setDaemon(True)
            i.start()
        for t in threads:
            t.join()

    def test_thread_pool(self):
        sqls = []
        for i in range(5):
            create_table = "create table test_sy_" + str(i) + " like test_sy"
            print("开始建表:",create_table)
            self.dorisDrive.sqlExecute(create_table)
            insert_talbe = "insert into test_sy_" + str(i) + " select * from motherbaby_post where month >= '2019-01-01' and content REGEXP '奶粉|配方.{0,1} 奶|美赞|mead johnson|[^西]安婴儿|蓝臻|安婴宝|(打.{0,4})安儿宝|安儿健|美素|惠氏(.{0,4}(海藻|妈妈|孕|爱乐维|叶酸|DHA|dha))|爱儿复|铂臻|爱儿素|启赋|illuma|雅培|喜康宝|喜康力|labbott|贝因美|牛栏|nutrilon|诺优能|飞鹤|爱他美|德爱|爱宝美|小安素|菁智|菁挚|雀巢.{0,5}(水解|110|无乳糖|FM85|fm85)|圣元|优博|能恩|力多精|纽康特|钮康特|纽太特|肽敏舒|多美滋|恩敏舒|蔼儿舒|霭尔舒|葛儿舒|可瑞康|母乳.{0,2}(强化剂|添加剂|补充剂)|佳贝艾特|澳优|海普诺凯|(喝|买).{0,2}(a|A)2|伊利|金领冠|星阶优护|超级飞帆|星飞帆|御宝|尤爱倍特|伊卡蓓尔|雅士利|eleva|喜安智|完达山|托菲尔|天赋力|特福芬|topfer|topfer|太子乐|施恩|诗幼乐|圣元|森永|森宝|semper|森宝|三元|人之初|启赋|配方.{0,1}奶|欧比佳|欧贝嘉|纽瑞滋|纽贝滋|亲舒|friso|frisolac|美术佳儿|力多精|乐博|蓝臻|莱那珂|可瑞乐|可瑞康|karicare|康敏金|君乐宝|乐钙[^片]|舒适成长|金领冠|佳思敏|吉特士|ultima|欢恩宝|海普诺凯|冠军宝贝|歌德乳|高原之宝|斐婴宝|菲思力|法兰贝尔|多乐特|聪尔壮|铂臻|倍滋曼|倍冠|贝因美|贝唯他|贝欧莱|贝贝羊|伴宝乐|百立乐|澳佑宝|澳优|澳仕卡牛|安琪儿|安纽希|安满|安吉兰德|爱优素|爱怡乐|爱睿惠|爱瑞嘉|爱普安|爱美乐|爱可丁|爱荷美|爱恩思|爱达力|爱必达|爱蔼舒|艾宝欣|蔼儿舒|hero.{0,1}baby|天赋力|aptamil|德爱|akara|(爱|健|幼|学)儿乐|恩美力'"
            sqls.append(insert_talbe)
        start_time = time()
        print("开始执行数据插入")
        executor = ThreadPoolExecutor(max_workers=5)  # 建立线程池
        task_all = [executor.submit(self.ten_time,sql,1) for sql in sqls]
        wait(task_all)
        print("执行完毕结束时间:",time() - start_time)

        print("开始验证数据正确性")
        for i in range(5):
            sql = "select count(1) from test_sy_" + str(i)
            print("执行sql:",sql)
            Numbers = self.dorisDrive.sqlExecute(sql)[0]['count(1)']
            print(Numbers)
            self.assertEqual(60436058, Numbers, "建表数据不一致")

        print("对比完成,通过对比,开始清理表数据!")
        for j in range(5):
            drop_sql = "drop table test_sy_" + str(j)
            self.dorisDrive.sqlExecute(drop_sql)

    def test_show_tables(self):
        import os
        os.getcwd()
        sql_nums = []
        sql = "show tables"
        res_dim = self.dorisDrive.sqlExecute(sql)
        dim_list = jsonpath.jsonpath(res_dim,'$..Tables_in_dwd')
        for i in dim_list:
            s = {}
            sql1 = "select count(1) from {} ".format(i)
            s['数据源'] = i
            s['doris'] = self.dorisDrive.sqlExecute(sql1)[0]['count(1)']
            sql_nums.append(s)
        pd.DataFrame(sql_nums).to_excel('res.xlsx')

    def test_show_talbes_1(self):
        import json
        sql = 'show tables'
        sqls = []
        res_dim = self.dorisDrive.sqlExecute(sql)
        dim_list = jsonpath.jsonpath(res_dim, '$..Tables_in_dim')
        for i in dim_list:
            sql1 = "select count(1) as num from prod_platform_dim.{}".format(i)
            sqls.append(sql1)
        print(json.dumps(sqls))
    def test_read_txt(self):
        with open("test.txt",encoding="utf-8") as f:
            data = f.readlines()
            for i in data:
                s = i.split("\n")
                j = s[0].split("结果：")
                print(j[1])




if __name__ == '__main__':
    unittest.main()
