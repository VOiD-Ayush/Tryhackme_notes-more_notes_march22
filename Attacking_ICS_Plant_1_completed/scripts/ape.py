#!/usr/bin/env python3

import sys
import time
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.exceptions import ConnectionException

ip = sys.argv[1]
client = ModbusClient(ip, port=502)
client.connect()
while True:
  client.write_register(1, 1)  # inlet
  client.write_register(2, 0)  # machine on off
  client.write_register(3, 1)  # 
  client.write_register(4, 1)  # 
  client.write_register(6, 1)  # 
  client.write_register(9, 1)  #
  client.write_register(8, 2000)  # 

