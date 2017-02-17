#!/usr/bin/python
#  coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formatdate
import sys


def send_mail_adv(from_add,to_add,hash_type):


    # 设置默认字符集为UTF8 不然有些时候转码会出问题
    default_encoding = 'utf-8'
    if sys.getdefaultencoding() != default_encoding:
        reload(sys)
        sys.setdefaultencoding(default_encoding)

    # 发送邮件的相关信息，根据你实际情况填写
    smtpHost = 'localhost'
    smtpPort = '25'
    sslPort = '587'
    # sslPort = '465'
    fromMail = from_add
    toMail = to_add
    username = 'guest1@test.mikemail.com'
    password = '11111111'

    # 邮件标题和内容
    subject = u'[Notice]hello'
    body = u'hello,this is a mail from ' + fromMail

    # 初始化邮件
    encoding = 'utf-8'
    mail = MIMEText(body.encode(encoding), 'plain', encoding)
    mail['Subject'] = Header(subject, encoding)
    mail['From'] = fromMail
    mail['To'] = toMail
    mail['Date'] = formatdate()

    try:
        if('Normal' == hash_type):
            # 连接smtp服务器，明文/SSL/TLS三种方式，根据你使用的SMTP支持情况选择一种
            # 普通方式，通信过程不加密
            smtp = smtplib.SMTP(smtpHost, smtpPort)
            smtp.ehlo()
            # smtp.login(username, password)

        if ('tls' == hash_type):
            # tls加密方式，通信过程加密，邮件数据安全，使用正常的smtp端口
            smtp = smtplib.SMTP(smtpHost,smtpPort)
            smtp.set_debuglevel(True)
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            # smtp.login(username,password)
        if ('ssl' == hash_type):
            # 纯粹的ssl加密方式，通信过程加密，邮件数据安全
            smtp = smtplib.SMTP_SSL(smtpHost,sslPort)
            smtp.ehlo()
            # smtp.login(username,password)
        # 发送邮件
        smtp.sendmail(fromMail, toMail, mail.as_string())
        smtp.close()
        print 'OK'
    except Exception as e:
        print e