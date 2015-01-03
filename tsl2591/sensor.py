#!/usr/bin/python

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
