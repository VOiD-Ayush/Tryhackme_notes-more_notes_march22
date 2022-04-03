#include <stdio.h> 
#include <stdlib.h>

int main(int argc, char *argv[])
{
 FILE *kf;
 size_t ks, n, i;
 long pos;
 unsigned char *key;
 unsigned char buf;
 if (argc != 2) {
 fprintf (stderr, "Usage: %s <key>\a\n", argv[0]);
 exit(1);
 }
 kf = fopen(argv[1], "rb");
 fseek(kf, 0L, SEEK_END);
 pos = ftell(kf);
 ks = (size_t) pos;
 fseek(kf, 0L, SEEK_SET);
 key = (unsigned char *) malloc(ks);
 fread(key, 1, ks, kf);
 fclose(kf);
 freopen(NULL, "rb", stdin);
 freopen(NULL, "wb", stdout);
 i = 0;
 while ((n = fread(&buf,1,1,stdin)) != 0L) {
 buf = buf ^ key[i % (ks-1)];
 fwrite(&buf,1,1,stdout);
 i++;
 }
 free((void*)key);
 exit(0);
}