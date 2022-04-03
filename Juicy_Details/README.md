# Juicy Details


```bash
tools used : feroxbuster/2.2.1 sqlmap/1.5.2#stable Hydra Nmap

cat access.log | grep nmap | wc
     10     170    1755

cat access.log | grep -i  hydra | wc
    288    3744   33985

cat access.log | grep -i sqlmap | wc
     78    1014   21519
   
cat access.log | grep -i ferox | wc
      9     108    1097

```

feroxbuster nmap sqlmap hydra