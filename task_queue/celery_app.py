from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery_config import CeleryConfig

# Configurations
c_app = Celery()
c_app.config_from_object(CeleryConfig)

if __name__ == '__main__':
    c_app.start()
