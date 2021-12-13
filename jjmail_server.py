# -*- coding: utf-8 -*-
# Time: 2020-10-27 5:46
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: jjmail.py

'''
JJMail Service
统一api接口调用方式
'''
import sys, os
sys.path.append(os.path.dirname(os.getcwd()))

from jjmail_cls import jjmail_cls

jjmail = jjmail_cls().celery

