from celery import Celery
from kombu import Queue, Exchange

app = Celery(
    broker='amqp://MincoX:mincoroot@49.232.19.51:5672//',
    backend='redis://49.232.19.51:63791/2'
)


class Config:
    CELERY_IMPORTS = (
        'asynchronous.failed_retry_tasks',  # 任务失败重试
    )
    CELERY_TIMEZONE = 'Asia/Shanghai'

    # 任务过期时间，不建议直接写86400，应该让这样的magic数字表述更明显
    CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
    # 单个任务的运行时间限制，否则会被杀死
    CELERY_TASK_TIME_LIMIT = 60
    # 每个worker执行了多少任务就会死掉，默认是无限的
    CELERY_MAX_TASKS_PER_CHILD = 200

    # 执行任务并发工作进程/线程/绿色线程数量， 默认值为 cpu 内核数
    CELERY_CONCURRENCY = 2
    # celery worker每次去redis取任务的数量，默认值就是4
    CELERY_PREFETCH_MULTIPLIER = 4

    # # 配置队列（settings.py）
    # CELERY_QUEUES = (
    #     Queue('default',
    #           Exchange('default'),
    #           routing_key='default'),
    #     Queue('for_task_collect',
    #           Exchange('for_task_collect'),
    #           routing_key='for_task_collect'),
    #     Queue('for_task_compute',
    #           Exchange('for_task_compute'),
    #           routing_key='for_task_compute'),
    # )
    # # 路由（哪个任务放入哪个队列）
    # CELERY_ROUTES = {
    #     'umonitor.tasks.multiple_thread_metric_collector':
    #         {
    #             'queue': 'for_task_collect',
    #             'routing_key': 'for_task_collect'
    #         },
    #     'compute.tasks.multiple_thread_metric_aggregate':
    #         {
    #             'queue': 'for_task_compute',
    #             'routing_key': 'for_task_compute'
    #         },
    #     'compute.tasks.test':
    #         {
    #             'queue': 'for_task_compute',
    #             'routing_key': 'for_task_compute'
    #         },
    # }


app.config_from_object(Config)
