#!/usr/bin/python

import logging

logger = logging.getLogger("robotice.sensor.tsl2591")

def get_data(sensor):
    """
    Get the luminosity readings.
    """

    name = sensor.get('name')
    bus = 1

    luminosity = 0
 
    values = [
        ('%s.luminosity' % name, luminosity, ),
    ]
    return values
