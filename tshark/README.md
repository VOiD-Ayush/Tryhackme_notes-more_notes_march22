# Tshark

```bash
To read a file with TShark, we will use the -r switch. This will display a summary line of each packet similar to tcpdump output and is useful to identify high-level information about the capture.

tshark -r dns.cap



When paired with wc -l, we can quickly identify how many packets are in a capture.

tshark -r dns.cap | wc -l

We can utilize Wireshark display filters (which are DIFFERENT than bpf syntax) to narrow down what packets are displayed. If were interested in DNS A records only, we can use the dns.qry.type == 1 display filter to narrow down our packets. Display filters are added using the -Y switch. Our command below will show all of the A records in our capture, including responses.

tshark -r dns.cap -Y "dns.qry.type == 1"

tshark -r dnsexfil.pcap -Y "dns.qry.type == 1" | grep response | cut -d "A" -f 2 | cut -d "." -f1 > enc


```