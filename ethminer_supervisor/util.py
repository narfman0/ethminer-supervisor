# -*- coding: utf-8 -*-
from datetime import datetime
import subprocess


SERVICE_CMD = ['service', 'ethminer', 'status']


def check():
    for line in get_ethminer_service_output():
        time = parse_time(line)
        if time and is_old_time(time):
            print('Found old time {}'.format(time))


def get_ethminer_service_output():
    proc = subprocess.Popen(SERVICE_CMD, stdout=subprocess.PIPE)
    while True:
        line = proc.stdout.readline()
        if line:
            yield line
        else:
            break


def parse_time(line):
    line_segments = line.split(' ')
    if len(line_segments) > 3:
        try:
            line_date = ' '.join(line_segments[:3])
            return datetime.strptime(line_date, "%b %d %H:%M:%S")
        except ValueError:
            print('Line doesnt have a valid time, skipping')
    return None


def is_old_time(time, delta_seconds=60*4):
    return (datetime.now() - time).total_seconds() > delta_seconds
