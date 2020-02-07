from celery import Celery
from kombu import Queue, Exchange

app = Celery(
    broker='amqp://MincoX:mincoroot@49.232.19.51:5672//',
    backend='redis://49.232.19.51:63791/2'
)


class Config:
    CELERY_IMPORTS = (
        'asynchronous.failed_retry_tasks',  # 任务失败重试
        'asynchronous.exchange_tasks',  # 多任务，多队列
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

    # 配置队列
    CELERY_QUEUES = (
        Queue('default', Exchange('default'), routing_key='default'),
        Queue('infinite_worker', Exchange('infinite_worker'), routing_key='infinite_worker'),
        Queue('info', Exchange('project_logs', type='direct'), routing_key='info'),
        Queue('error', Exchange('project_logs', type='direct'), routing_key='error'),
    )
    CELERY_DEFAULT_QUEUE = 'default'
    CELERY_DEFAULT_EXCHANGE = 'default'
    CELERY_DEFAULT_ROUTING_KEY = 'default'

    # 任务绑定
    #   将任务绑定到交换机上，需要指明 routing_key，根据 routing_key 进行路由
    #   将任务直接绑定到队列中可以不指明 routing_key
    CELERY_ROUTES = {
        # 将任务绑定到交换机上，需要指明 routing_key，根据 routing_key 进行路由
        'asynchronous.exchange_tasks.case2':
            {
                'exchange': 'infinite_worker',
                'routing_key': 'infinite_worker'
            },
        # 将任务直接绑定到队列中可以不指明 routing_key
        'asynchronous.exchange_tasks.case3':
            {
                'queue': 'info',
            },
    }


app.config_from_object(Config)
