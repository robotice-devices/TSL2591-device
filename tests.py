
#!/usr/bin/env python

import quick2wire.i2c as i2c

address = 0x39
xad = 0x0A
bus_number = 0

with i2c.I2CMaster(bus_number) as bus:    
    read_results = bus.transaction(
        i2c.writing_bytes(address, xad),
        i2c.reading(address, 1)
    )
