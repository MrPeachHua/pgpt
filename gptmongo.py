from datetime import datetime

from pymongo import MongoClient
import pytz

host = '111.67.201.205'   # 你的ip地址
client = MongoClient(host, 27017)  # 建立客户端对象
db = client["gpt"]  # 连接mydb数据库，没有则自动创建
myset = db["gpt_content"]   # 使用test_set集合，没有则自动创建

# 下面是遍历查询数据
# for i in myset.find():
#     print(i)
def insertOneGpt(title, content, remote_addr):
    dtime = pytz.timezone('Asia/Shanghai').localize(datetime.now())  # 给datetime指定时区
    myset.insert_one({"title": title, "content": content, "createTime":dtime, "remoteAddr": remote_addr})  # 插入一条数据，如果没出错那么说明连接成功