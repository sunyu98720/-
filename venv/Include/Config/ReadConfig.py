import os
import configparser

#os.path.realpath：获取当前执行脚本的绝对路径。
#os.path.split：如果给出的是一个目录和文件名，则输出路径和文件名
proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")


class ReadConfig:
    def __init__(self,database=None):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)
        if database != None:
            self.database = database
        else:
            self.database = 'DATABASE'

    #读取配置信息
    def get_configInfo(self,title,param):
        value = self.cf.get(title, param)
        return value

    #读取单个配置信息
    def get_http(self, param):
        value = self.cf.get("HTTP", param)
        return value

    def get_db(self,param):
        value = self.cf.get(self.database, param)
        return value

    def get_browser(self,param):
        value = self.cf.get("BROWSER", param)
        return value

    def get_email(self, param):
        value = self.cf.get("EMAIL", param)
        return value


if __name__ == '__main__':
    test = ReadConfig()
    LocalIp = test.get_db('host')
    print(LocalIp)