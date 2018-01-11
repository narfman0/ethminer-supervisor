# -*- coding: utf-8 -*-
from datetime import datetime
from time import sleep
import logging
import subprocess


SERVICE_CMD = ['service', 'ethminer', 'status']
SERVICE_STOP = ['service', 'ethminer', 'stop']
SERVICE_START = ['service', 'ethminer', 'start']
logger = logging.getLogger(__name__)


def check():
    has_recent = False
    for line in get_ethminer_service_output():
        time = parse_time(line)
        if time:
            if is_old_time(time):
                logger.debug('Found old time {}'.format(time))
            else:
                logger.debug('Found recent time {}'.format(time))
                has_recent = True
    if not has_recent:
        logger.info("No recent times found for ethminer!")
    else:
        logger.info("Ethminer recent status time found :)")
    return has_recent


def restart():
    logger.info('Restarting ethminer...')
    subprocess.Popen(SERVICE_STOP)
    sleep(1)
    subprocess.Popen(SERVICE_START)
    logger.info('Ethminer restarted')


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
            logger.debug('Line doesnt have a valid time, skipping')
    return None


def is_old_time(time, delta_seconds=60*4):
    return (datetime.now() - time).total_seconds() > delta_seconds
