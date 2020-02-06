import time

from celery_app import app
from abstract_task.debug_task import DebugTask

""" celery 任务失败，自动重试
"""


@app.task(bind=True, max_retries=5, default_retry_delay=30, base=DebugTask)
def case1(self, **kwargs):
    """ max_retries: 任务最大重试次数
    default_retry_delay: 任务失败重试时间间隔，优先级低于 countdown
    """
    retries = self.request.retries
    print('第{}次任务重试'.format(retries).center(100, '*')) if retries != 0 else ''

    try:
        print('任务开始执行: {}'.center(100, '*').format(kwargs.get("CTIME")))
        res = 2 / 0
        print('任务执行结束'.center(100, '*'))

        return res

    except ZeroDivisionError as exc:
        # 重写任务重试的时间间隔，countdown 优先级高于 default_retry_delay
        raise self.retry(exc=exc, countdown=3)


@app.task(bind=True, autoretry_for=(IndexError,), retry_kwargs={'max_retries': 3, 'countdown': 5})
def case2(self, **kwargs):
    """ 版本 4.0 中的新功能
    autoretry_for: 针对指定异常自动重试任务
    retry_kwargs: 任务重试参数
        max_retries： 最大重试次数
        countdown： 每一次失败重复执行的时间间隔
    """
    retries = self.request.retries
    print('第{}次任务重试'.format(retries).center(100, '*')) if retries != 0 else ''

    print('任务开始执行: {}'.center(100, '*').format(kwargs.get("CTIME")))
    ls = []
    res = ls[0]
    print('任务执行结束'.center(100, '*'))

    return res


@app.task
def case3(**kwargs):
    """
    重试策略, 使用 apply_async 方式调用，传入 retry_policy 重试策略
    :param kwargs:
    :return:
    """
    """ retry : 定时如果任务失败后, 是否重试, 默认为 False
    retry_policy : 重试策略.
    　　max_retries : 最大重试次数, 默认为 3 次, None 值意味着一直重试
    　　interval_start : 重试等待的时间间隔秒数, 默认为 0 表示直接重试不等待.
    　　interval_step : 每次重试让重试间隔增加的秒数, 可以是数字或浮点数, 默认为 0.2
    　　interval_max : 重试间隔最大的秒数, 即 通过 interval_step 增大到多少秒之后, 就不在增加了, 可以是数字或者浮点数, 默认为 0.2.
    """
    print('任务开始执行: {}'.center(100, '*').format(kwargs.get("CTIME")))
    res = 2 / 0
    print('任务执行结束'.center(100, '*'))

    return res
