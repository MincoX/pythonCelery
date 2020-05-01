from datetime import datetime

from abstract_task.debug_task import DebugTask
from asynchronous import failed_retry_tasks, exchange_tasks

CTIME = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    # ########################## 失败任务重试测试 ##########################
    # failed_retry_tasks.case1.delay(**{'CTIME': CTIME})
    # failed_retry_tasks.case2.delay()
    # failed_retry_tasks.case3.apply_async(
    #     **{'CTIME': CTIME},
    #     retry=True,
    #     retry_policy={
    #         'max_retries': 3,
    #         'interval_start': 0,
    #         'interval_step': 0.2,
    #         'interval_max': 0.2,
    #     }
    # )
    # ########################## 失败任务重试测试 ##########################
    # ########################## 多任务，多队列 ############################
    # 将任务绑定到交换机上，需要指明 routing_key，根据 routing_key 进行路由
    # 将任务直接绑定到队列中可以不指明 routing_key
    # case1 走默认队列
    # exchange_tasks.case1.delay()
    # case2 通过交换机 和 routing key 匹配走 infinite_worker 队列
    # exchange_tasks.case2.delay()
    # # case3 走 info 队列，直接将任务绑定到 info 队列中
    # exchange_tasks.case3.delay()
    # exchange_tasks.case4.apply_async(
    #     exchange='project_logs',
    #     routing_key='error',
    # )
    # ########################## 多任务，多队列 ############################
    # ########################## 测试配置文件 ############################
    # from asynchronous import test

    # test.test1.delay()
    # test.test2.apply_async(
    #     base=DebugTask
    # )
    # ########################## 测试配置文件 ############################
    pass
