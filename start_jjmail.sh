#!/usr/bin/env bash

nohup celery -A jjmail_server worker -l info -f jjmail.log --pool=solo > /dev/null 2>&1 &
echo "jjmail服务已启动"
exit
