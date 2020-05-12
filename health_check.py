#!/usr/bin/env python3

from emails import generate_email, send_email
import psutil, shutil
import socket

cpu_usage = psutil.cpu_percent()
_, used,_ = shutil.disk_usage('/')
memory = psutil.virtual_memory()

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print(host_name, host_ip)

