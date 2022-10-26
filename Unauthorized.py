import ftplib
import re
import socket
from concurrent.futures import ThreadPoolExecutor
import alist as alist
import pymysql
import threadpool
from kazoo.client import KazooClient
from pymongo import MongoClient
import requests



def redis(ip):
    try:
        socket.setdefaulttimeout(10)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 6379))
        s.send(bytes("INFO\r\n", 'UTF-8'))
        recv = s.recv(1024).decode()
        if "redis_version" in recv:
            print(ip + ":6379 存在redis未授权")
        # else:
        #    print(ip + ":6379 不存在redis未授权")

        with open('success.txt', 'a') as f:  # 设置文件对象
            print(ip + ":6379 存在redis未授权", file=f)
    except Exception as e:
        pass


def rsync(ip):
    try:
        socket.setdefaulttimeout(10)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 873))
        s.send(bytes("", 'UTF-8'))
        recv = s.recv(1024).decode()
        if "RSYNCD" in recv:
            print(ip + ":873 存在rsync未授权")
        # else:
        #    print(ip + ":873 不存在rsync未授权")
        with open('success.txt', 'a') as f:  # 设置文件对象
            print(ip + ":873 存在rsync未授权", file=f)
    except Exception as e:
        pass


def zookeeper(ip):
    try:
        socket.setdefaulttimeout(10)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 2181))
        s.send(bytes("envi\r\n",'UTF-8'))
        recv = s.recv(1024).decode()
        if "Environment" in recv:
            print(ip + ":2181 存在zookeeper未授权")
            with open('success.txt', 'a') as f:  # 设置文件对象
                print(ip + ":2181 存在zookeeper未授权", file=f)
        # else:
        #    print(ip + ":2181 不存在zookeeper未授权")
    except Exception as e:
        pass


def memcache(ip):
    try:
        socket.setdefaulttimeout(10)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 11211))
        s.send(bytes("stats\r\n",'UTF-8'))
        recv = s.recv(1024).decode()
        if "version" in recv:
            print(ip + ":11211 存在memcache未授权")
            with open('success.txt', 'a') as f:  # 设置文件对象
                print(ip + ":11211 存在memcache未授权", file=f)
    except Exception as e:
        pass


def mongo(ip):
    try:
        conn = MongoClient(ip,27017)
        dbname = conn.list_database_names()
        print(ip + ":27017 存在mongoDB未授权")
    # else:
    #   print(ip + ":27017 不存在mongoDB未授权")
        with open('success.txt', 'a') as f:  # 设置文件对象
            print(ip + ":27017 存在mongoDB未授权", file=f)
    except Exception as e:
        pass


def ftp(ip):
    try:
        f = ftplib.FTP()
        f.connect(ip,21)
        #f.connect(ip, 21)
        f.login('anonymous','')
        print(ip + ":21 存在FTP未授权")
        with open('success.txt', 'a') as f:  # 设置文件对象
            print(ip + ":21 存在FTP未授权", file=f)
    except Exception as e:
        pass


def mysql(ip):
    try:
        conn = pymysql.connect(host=ip,user='root',password="",charset='utf8',autocommit=True)
        print(ip + "：3306 存在mysql空口令")
        with open('success.txt','a') as f:#设置文件对象
            print(ip +":3306存在mysql空口令",file=f)
    except Exception as e:
        pass


def Elasticsearch(ip):

    try:
        url = "http://" + ip + ":9200" + "/_cat"
        response = requests.get(url,timeout=5)
        if "_cat/master" in response.content.decode():
            print(ip + ":9200 存在Elasticsearch未授权")
            with open('success.txt', 'a') as f:  # 设置文件对象
                print(ip + ":9200 存在Elasticsearch未授权", file=f)
    #else:
    #    print(ip + ":9200 不存在Elasticsearch未授权")
    except Exception as e:
        pass


def Hadoop(ip):
    try:
        url = "http://" + ip + ":8088/cluster"
        response =  requests.get(url,timeout=5)
        if "Cluster" in response.content.decode():
            print(ip + ":8088 存在Hadoop未授权")
            with open('success.txt', 'a') as f:  # 设置文件对象
                print(ip + ":8088 存在Hadoop未授权", file=f)
        # else:
        #    print(ip + ":50070 不存在Hadoop未授权")
    except Exception as e:
        pass


def kibana(ip):
    try:
        url = "http://" + ip + "/app/kibana"
        response = requests.get(url,timeout=5)
        if "/app/kibana" in response.content.decode():
            print(url + "存在kibanan未授权")
            with open('success.txt','a') as f: #设置文件对象
                print(url + "存在kibanan未授权",file=f)
        #else
        #  print(url + "不存在kibana未授权")
    except Exception as e:
        pass


def dockerapi(ip):
    try:
        url = "http://" + ip + ":2375/version"
        response = requests.get(url,timeout=5)
        if "ApiVersion" in response.content.decode():
            print(ip + ":2375 存在dockerapi未授权")
            with open('success.txt', 'a') as f:  # 设置文件对象
                print(ip + ":2375 存在dockerapi未授权", file=f)
        # else:
        #    print(ip + ":50070 不存在Hadoop未授权")
    except Exception as e:
        pass


def Jenkins(ip):
    try:
        url = "http://" + ip +":8080/manange"
        response = requests.get(url,timeout=5)
        if "Build History" in response.content.decode():
            print(url + "存在Jenkins未授权")
            with open('success.txt','a')as f: #设置文件对象
                print(url + "发现Jenkins未授权",file=f)
        #else:
        #    print(url + "不存在Jenkins未授权")
    except Exception as e:
        pass


def CouchDB(ip):
    try:
        url = 'http://' + ip + ':5984' + '/_utils/'
        response = requests.get(url, timeout=5)
        if 'couchdb-logo' in response.content.decode():
            print(ip + ":5984 CouchDB未授权")
            with open('success.txt', 'a') as f:  # 设置文件对象
                print(url + ":5984 CouchDB未授权", file=f)
        # else:
        #    print(url + "不存在CouchDB未授权")
    except Exception as e:
        pass


def jboss(ip):
    try:
        url = 'http://' + ip + ':8080/jmx-console'
        response = requests.get(url,timeout=5)
        if 'JMX Agent View' in response.content.decode():
            print(ip + ":8080 存在jboss未授权")
            with open('success.txt','a') as f:#设置文件对象
                print(ip + ":8080存在jboss未授权",file=f)
        # else:
        #    print(url + "不存在jboss未授权")
    except Exception as e:
        pass


def activeMQ(ip):
    try:
        url = "http://" + ip + ":8161"
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0.1 Safari/604.3.5",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate",
            "Authorization": "Basic YWRtaW46YWRtaW4="
        }
        response = requests.get(url,headers=headers)
        if "Broker" in response.content.decode():
            print(url + " 存在activeMQ未授权")
            with open('success.txt', 'a') as f:  # 设置文件对象
                print(url + "存在activeMQ未授权", file=f)
        # else:
        #    print(url + "不存在activeMQ未授权")
    except Exception as e:
        pass


def Druid(ip):
    try:
        url = "http://" + ip + ":9300/druid/index.html"
        response = requests.get(url,timeout=5)
        if 'Stat' in response.content.decode():
            print(url + " 存在druid未授权")
            with open('success.txt', 'a') as f:  # 设置文件对象
                 print(url + "存在druid未授权", file=f)
        # else:
        #    print(url + "不存在druid未授权")
    except Exception as e:
        pass

def ERLib(ip):
    try:
        url = "http://" + ip + ":8099"
        response = requests.get(url,timeout=5)
        if "View" in response.content.decode():
            print(url + "存在ERLib未授权")
            with open("success.txt",'a') as f: #设置文件对象
                print(url + "存在ERLib未授权", file=f)
        # else:
        #    print(url + "不存在ERLib未授权")
    except Exception as e:
        pass


def swaggerapi(ip):
    try:
        url = "http://" + ip +":8080/swagger-ui.html"
        response = requests.get(url,timeout=5)
        if "Api" in response.content.decode():
            print(url + "存在SwaggerApi未授权")
            with open("success.txt", 'a') as f:  # 设置文件对象
                print(url + "存在SwaggerApi未授权", file=f)
        # else:
        #    print(url + "不存在SwaggerApi未授权")
    except Exception as e:
        pass


if __name__ == '__main__':
    #print("请输入ip：")
    #ip = input()
    f = open('hosts.txt','r')
    with ThreadPoolExecutor(2000) as pool:
        for ip in  f.readlines():
            ip = ip.strip()
            pool.submit(redis,ip)
            pool.submit(mongo,ip)
            pool.submit(ftp,ip)
            pool.submit(zookeeper,ip)
            pool.submit(Elasticsearch,ip)
            pool.submit(Hadoop,ip)
            pool.submit(kibana,ip)
            pool.submit(memcache,ip)
            pool.submit(dockerapi,ip)
            pool.submit(Jenkins,ip)
            pool.submit(CouchDB,ip)
            pool.submit(mysql,ip)
            pool.submit(jboss,ip)
            pool.submit(rsync,ip)
            pool.submit(activeMQ,ip)
            pool.submit(Druid,ip)
            pool.submit(ERLib,ip)
            pool.submit(swaggerapi,ip)


