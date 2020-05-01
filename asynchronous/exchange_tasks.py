from datetime import datetime

from celery_app import app
from abstract_task.debug_task import DebugTask

""" 多任务多队列的意义在于: 
        在多台服务器上通过 -Q 参数开启指定的 worker, 将任务分发到不同的服务器上执行，减少服务器的压力，提高效率 
"""


@app.task(bind=True, base=DebugTask)
def case1(self):
    """
    任务没有绑定队列, 走默认队列
    :param self:
    :return:
    """
    # print(dir(self))
    # print("self.request", self.request)

    print('case1 >>> 任务交换机：{}，routing_key：{}'.format(
        self.request.delivery_info['exchange'],
        self.request.delivery_info['routing_key'],
    ))

    res = '任务执行成功: {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    return res


@app.task(bind=True)
def case2(self):
    """
    通过交换机 和 routing key 匹配走 infinite_worker 队列 (配置文件中配置)
    :param self:
    :return:
    """
    print('case2 >>> 任务交换机：{}，routing_key：{}'.format(
        self.request.delivery_info['exchange'],
        self.request.delivery_info['routing_key'],
    ))

    res = '任务执行成功: {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    return res


@app.task(bind=True)
def case3(self):
    """
    直接将任务绑定到 info 队列中
    :param self:
    :return:
    """
    print('case3 >>> 任务交换机：{}，routing_key：{}'.format(
        self.request.delivery_info['exchange'],
        self.request.delivery_info['routing_key'],
    ))

    res = '任务执行成功: {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    return res


@app.task(bind=True)
def case4(self):
    """
    通过 apply_async 方式调用, 指定发送到 project_logs 交换机下 routing key 为 error 的队列
    :param self:
    :return:
    """
    print('case4 >>> 任务交换机：{}，routing_key：{}'.format(
        self.request.delivery_info['exchange'],
        self.request.delivery_info['routing_key'],
    ))

    res = '任务执行成功: {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    return res


@app.task(bind=True)
def schedule(self):

    print('case1 >>> 任务交换机：{}，routing_key：{}'.format(
        self.request.delivery_info['exchange'],
        self.request.delivery_info['routing_key'],
    ))

    print(f'定时任务开始执行 {datetime.today()}')
