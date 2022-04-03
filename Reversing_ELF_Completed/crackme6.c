int my_secure_test(char *param_1)

{
  int returning_variable;
  
  if ((*param_1 == '\0') || (*param_1 != '1')) {
    returning_variable = 0xffffffff;
  }
  else {
    if ((param_1[1] == '\0') || (param_1[1] != '3')) {
      returning_variable = 0xffffffff;
    }
    else {
      if ((param_1[2] == '\0') || (param_1[2] != '3')) {
        returning_variable = 0xffffffff;
      }
      else {
        if ((param_1[3] == '\0') || (param_1[3] != '7')) {
          returning_variable = 0xffffffff;
        }
        else {
          if ((param_1[4] == '\0') || (param_1[4] != '_')) {
            returning_variable = 0xffffffff;
          }
          else {
            if ((param_1[5] == '\0') || (param_1[5] != 'p')) {
              returning_variable = 0xffffffff;
            }
            else {
              if ((param_1[6] == '\0') || (param_1[6] != 'w')) {
                returning_variable = 0xffffffff;
              }
              else {
                if ((param_1[7] == '\0') || (param_1[7] != 'd')) {
                  returning_variable = 0xffffffff;
                }
                else {
                  if (param_1[8] == '\0') {
                    returning_variable = 0;
                  }
                  else {
                    returning_variable = 0xffffffff;
                  }
                }
              }
            }
          }
        }
      }
    }
  }
  return returning_variable;
}
