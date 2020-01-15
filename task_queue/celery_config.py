class CeleryConfig:
    broker_url = 'redis://localhost'
    result_backend = 'redis;//localhost'
    task_serializer = 'json'
    task_routes = {
        # 'task.write_to_file': 'low-priority',
        # 'task.write_to_file': {'rate-limit': '10/m'},  # 10 tasks of this type can be processed in a minute (10/m)
    }
