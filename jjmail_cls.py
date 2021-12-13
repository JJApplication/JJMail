# -*- coding: utf-8 -*-
# Time: 2020-10-27 5:48
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: jjmail_cls.py

'''
jjmail class
'''
from celery import Celery

class jjmail_cls:
    celery  =  None

    def __init__(self):
        self.celery = Celery('jjmail',
                include=['jjmail.task1',
                         'jjmail.task2',
                         'jjmail.task3',
                         'jjmail.task4',
                         'jjmail.task5']
                )
        self.celery.config_from_object("jjmail.celery_conf")
