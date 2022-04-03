#include<stdio.h>

int main()
{
  int iVar1;
  int local_c;
  local_c = 1;
  while (local_c < 7){
      // iVar1 = atoi(*(char **)(param_2 + (long)local_c * 8));
    printf("%d\n",local_c);
      if (iVar1 != 7 - local_c) {
        puts("Hmm... I disagree!");
        // return 0;
      }
      local_c = local_c + 1;
    }
    puts("Now that, I can get behind!");
  return 0;
}
