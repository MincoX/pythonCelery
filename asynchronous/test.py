import time

from celery_app import app
from abstract_task.debug_task import DebugTask


@app.task(base=DebugTask)
def test1():
    """
    测试任务过期时间
    :return:
    """
    print('任务开始执行！'.center(100, '*'))
    time.sleep(20)
    print('任务执行结束！'.center(100, '*'))


@app.task
def test2():
    """
    :return:
    """
    print('任务开始执行！'.center(100, '*'))
    time.sleep(3)
    print('任务执行结束！'.center(100, '*'))
