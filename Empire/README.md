# Empire 

> VOiD | Wednesday 01 December 2021 03:47:27 PM UTC

My IP : 10.8.253.221
Target IP : 


## Installation
```bash
Installing Empire

We can begin by installing Empire on our device. Follow the instructions below to install Empire.

1. cd /opt
2. git clone https://github.com/BC-SECURITY/Empire/
3. cd /opt/Empire
4. ./setup/install.sh

Installing Starkiller
Once Empire is installed we can install the GUI for Empire known as Starkiller.

1. cd /opt
2. Download an up to date version of Starkiller from the BC-Security Github repo - https://github.com/BC-SECURITY/Starkiller/releases 
3. chmod +x starkiller-0.0.0.AppImage

Starting Empire

Once both Empire and Starkiller are installed we can start both servers. Being by starting Empire with the instructions below.

1. cd /opt/Empire
2. ./empire --rest

Starting Starkiller

Once Empire is started follow the instructions below to start Starkiller.

1. cd /opt
2. ./starkiller-0.0.0.AppImage
3. Login to Starkiller
Default Credentials

	Uri: 127.0.0.1:1337

	User: empireadmin

	Pass: password123


Once you have logged into Starkiller you should be greeted with the Listeners menu, once you have Starkiller or Empire ready move on to Task 3 to get familiar with the menu.
```

