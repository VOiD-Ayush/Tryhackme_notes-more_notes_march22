# NahamStore 

> VOiD | Tuesday 18 January 2022 12:49:22 PM UTC

My IP : 10.8.253.221
Target IP : 10.10.206.27

## PORT 8000 [http]
```bash
http://nahamstore.thm:8000/robots.txt

User-agent: *
Disallow: /admin

```

## PORT 80 [http]
```bash
wfuzz -c -z file,/usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -u "http://nahamstore.thm/" -H "Host: FUZZ.nahamstore.thm" --hw 65

000000001:   301        7 L      13 W       194 Ch      "www"              
000000037:   301        7 L      13 W       194 Ch      "shop"         
000000254:   200        41 L     92 W       2025 Ch     "marketing"        
000000960:   200        0 L      1 W        67 Ch       "stock" 
```
