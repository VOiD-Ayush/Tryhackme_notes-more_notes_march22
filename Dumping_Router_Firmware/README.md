# Dumping Router Firmware

## 
```bash
extracting the zip
7z x FW_WRT1900ACSV2_2.0.3.201002_prod.zip


step 1 : running strings on the image

Linksys WRT1900ACS Router
 -- System halted
Attempting division by 0!
Uncompressing Linux...
decompressor returned an error
...

step 2 : binwalk

Mounting the Filesystem

In this section, we will begin to go over how to mount the file system. Note, if you are doing this with any other file system and it is not in the Little Endian format, you will need to convert it from Big Endian to little Endian using a tool called jffs2dump. But here is my fairly concise guide to mounting the filesystem:

Step 1. If /dev/mtdblock0 exists, remove file/directory and re-create the block device

rm -rf /dev/mtdblock0
mknod /dev/mtdblock0 b 31 0
Step 2. Create a location for the jffs2 filesysystem to live
mkdir /mnt/jffs2_file/
Step 3. Load required kernel modules
modprobe jffs2
modprobe mtdram
modprobe mtdblock
Step 4. Write image to /dev/mtdblock0
dd if=/opt/Dumping-Router-Firmware-Image/_FW_WRT1900ACSV2_2.0.3.201002_prod.img.extracted/600000.jffs2 of=/dev/mtdblock0

dd if=./600000.jffs2 of=/dev/mtdblock0

Step 5. Mount file system to folder location
mount -t jffs2 /dev/mtdblock0 /mnt/jffs2_file/
Step 6. Lastly, move into the mounted filesystem.
cd /mnt/jffs2_file/


```