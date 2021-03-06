#!/usr/bin python3

"""
<Description of the programme>

Settings courtesy of ``tiangolo/uvicorn-gunicorn-docker``.

Author:        Pouria Hadjibagheri <pouria.hadjibagheri@phe.gov.uk>
Created:       22 Feb 2021
License:       MIT
Contributors:  Pouria Hadjibagheri
"""

# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python:
from json import dumps
from multiprocessing import cpu_count
from os import getenv

# 3rd party:

# Internal: 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Header
__author__ = "Pouria Hadjibagheri"
__copyright__ = "Copyright (c) 2021, Public Health England"
__license__ = "MIT"
__version__ = "0.0.1"
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("starting GUNICORN")

workers_per_core_str = "1"
# max_workers_str = getenv("MAX_WORKERS", cpu_count())
use_max_workers = None

# if max_workers_str:
#     use_max_workers = int(max_workers_str)

web_concurrency_str = getenv("WEB_CONCURRENCY", None)

host = getenv("HOST", "0.0.0.0")
port = getenv("GUNICORN_PORT", "5000")

use_bind = getenv("BIND", f"{host}:{port}")
use_loglevel = getenv("LOG_LEVEL", "info")
# JSON_LOGS = True if getenv("JSON_LOGS", "0") == "1" else False


cores = cpu_count()
workers_per_core = float(workers_per_core_str)
default_web_concurrency = workers_per_core * cores


# if web_concurrency_str:
#     web_concurrency = int(web_concurrency_str)
#     assert web_concurrency > 0
# else:
#     web_concurrency = max(int(default_web_concurrency), 2)
#
#     if use_max_workers:
#         web_concurrency = min(web_concurrency, use_max_workers)


accesslog_var = getenv("ACCESS_LOG", "-")
use_accesslog = accesslog_var or None
errorlog_var = getenv("ERROR_LOG", "-")
use_errorlog = errorlog_var or None
graceful_timeout_str = getenv("GRACEFUL_TIMEOUT", "45")
# timeout_str = getenv("TIMEOUT", "60")

reload = getenv("RELOAD", "0") == "1"

# Gunicorn config variables
loglevel = use_loglevel
workers = 2
bind = use_bind
errorlog = use_errorlog
worker_tmp_dir = "/dev/shm"
accesslog = use_accesslog
graceful_timeout = int(graceful_timeout_str)
# timeout = int(timeout_str)
proxy_protocol = True
secure_scheme_headers = {
    'X-FORWARDED-PROTO': 'https'
}


# For debugging and testing
log_data = {
    "loglevel": loglevel,
    "workers": workers,
    "bind": bind,
    # "graceful_timeout": graceful_timeout,
    # "timeout": timeout,
    "errorlog": errorlog,
    "accesslog": accesslog,
    # Additional, non-gunicorn variables
    "workers_per_core": workers_per_core,
    "use_max_workers": use_max_workers,
    "secure_scheme_headers": secure_scheme_headers,
    "proxy_protocol": proxy_protocol,
    "host": host,
    "port": port,
    "reload": reload
}

print(dumps(log_data))
