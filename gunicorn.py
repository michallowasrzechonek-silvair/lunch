#!python

import logging

import lunch  # noqa

# Gunicorn config variables
logconfig_dict = {
    "version": 1,
    "disable_existing_loggers": False,
    #  "filters": {"correlation_id": {"()": CorrelationIdFilter}},
    "formatters": {
        "text": {
            "()": logging.Formatter,
            "fmt": (
                "%(asctime)s.%(msecs)03d"
                " %(name)-30s"
                " %(levelname)-6s"
                " %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "()": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "text",
            #  "filters": ["correlation_id"],
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console"],
    },
    "loggers": {
        "gunicorn": {"level": logging.INFO},
    },
}

workers = 1
bind = "localhost:8888"
errorlog = "-"
worker_tmp_dir = "/dev/shm"
accesslog = "-"
graceful_timeout = 120
timeout = 120
keepalive = 1

logger = logging.getLogger("gunicorn")
