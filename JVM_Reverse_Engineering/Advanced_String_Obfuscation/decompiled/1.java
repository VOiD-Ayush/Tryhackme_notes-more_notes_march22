public final class 1 {
   private static final String[] a = new String[12];

   static {
      a[0] = "";
      a[2] = "[>T\u05f7\u05885\t\u0006הי68\u0001ךמRh\u0003\u05ccրG0\u0006\u058dא0\u001a";
      a[4] = "AmB\u05cb\u058cav\u0011";
      a[6] = "KHSז֛pCS\u05cd";
      a[8] = "R;Uט֚gw@\u05cbֆt>Tל\u05c9cw@ט֚q _\u05cb\u058d";
      a[10] = "[/T\u0ee7ຸ5\u0018\u0006ໄ\u0ee96)\u0001໊\u0eeeRy\u0003ໜະG!\u0006ຝ\u0ee00\u000b";
   }

   public static String a(int var0, int var1) {
      String var10000 = null;
      if (c.3 != 0) {
         var10000 = null;
         throw null;
      } else {
         Object var3 = null;
         Thread var4 = null;
         StackTraceElement[] var5 = null;
         int var6 = 0;
         int var7 = 0;
         char[] var8 = null;
         char[] var9 = null;
         int var10 = 0;
         byte var2 = 0;

         while(true) {
            while(true) {
               while(true) {
                  while(true) {
                     while(true) {
                        while(true) {
                           while(true) {
                              switch(var2) {
                              case 0:
                              case 6:
                                 var10000 = a[var0 * 2 + 1];
                                 if (var10000 != null) {
                                    return var10000;
                                 }

                                 var2 = 2;
                                 continue;
                              case 1:
                                 return a[var0 * 2 + 1] = new String(var9);
                              case 2:
                                 var4 = Thread.currentThread();
                                 var2 = 3;
                                 continue;
                              case 3:
                                 var5 = var4.getStackTrace();
                                 var2 = 4;
                                 continue;
                              case 4:
                                 var6 = var5[2].getClassName().hashCode();
                                 var2 = 5;
                                 continue;
                              case 5:
                                 var7 = var5[2].getMethodName().hashCode();
                                 var2 = 7;
                                 continue;
                              case 7:
                                 var8 = a[var0 * 2].toCharArray();
                                 var9 = new char[var8.length];
                                 var2 = 8;
                                 continue;
                              case 8:
                                 var10 = 0;
                                 break;
                              default:
                                 YourMum var11 = (YourMum)null;
                                 var9[var10] = (char)(var8[var10] ^ var10);
                                 ++var10;
                              }

                              while(var10 < var8.length) {
                                 int var12;
                                 switch(var10 % 5) {
                                 case 0:
                                    var12 = var8[var10] ^ 2;
                                    break;
                                 case 1:
                                    var12 = var8[var10] ^ var1;
                                    break;
                                 case 2:
                                    var12 = var8[var10] ^ var6;
                                    break;
                                 case 3:
                                    var12 = var8[var10] ^ var7;
                                    break;
                                 case 4:
                                    var12 = var8[var10] ^ var7 + var6;
                                    break;
                                 case 5:
                                    var12 = var8[var10] ^ var10;
                                    break;
                                 default:
                                    throw null;
                                 }

                                 var9[var10] = (char)var12;
                                 ++var10;
                              }

                              var2 = 1;
                           }
                        }
                     }
                  }
               }
            }
         }
      }
   }
}
