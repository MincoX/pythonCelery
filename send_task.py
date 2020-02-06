from datetime import datetime

from asynchronous.failed_retry_tasks import case1, case2, case3

CTIME = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    # ########################## 失败任务重试测试 ##########################
    case1.delay(**{'CTIME': CTIME})
    # case2.delay()
    # case3.apply_async(
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
