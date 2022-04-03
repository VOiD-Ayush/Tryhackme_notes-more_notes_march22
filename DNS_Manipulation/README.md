# DNS_Manipulation 

> VOiD | Wednesday 17 November 2021 06:41:49 PM IST

My IP : 10.8.253.221
Target IP : 


## TASK
``` 
The order.pcap file has suspecious queries. Use the ~/dns-exfil-infil/packetyGrabber.py to decode
the data and answer the questions accrodingly.

IDENTIFY THE DOMAIN NAME USED TO EXFILTRATE DATA
use the following command to see all DNS Queries
tshark -r order.pcap -T fields -e dns.qry.name
(ignore the .localdomain part)

Use the packetyGrabber.py located in ~/dns-exfil-infil/ folder to decode the DNS queries to a plain-text file.
python3 ~/dns-exfil-infil/packetyGrabber.py

IGNORE THE EXCEPTION THROWN AT THE END OF SCRIPT
```


