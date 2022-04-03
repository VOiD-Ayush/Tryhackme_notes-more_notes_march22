public class 0 {
   public static String c = 1.a(5, 78);

   public static void main(String[] args) {
      if (args.length >= (1) {
         Object var10002 = null;
         String var1 = 1.a(0, 100);

         try {
            var1 = args[(int)-753045066L ^ -753045066];
         } 
         catch (IndexOutOfBoundsException var3) {
            throw var3;
         }

         var10002 = null;
         if (c(1.a(1, 95)).equals(var1)){
            System.out.println(1.a(2, 2));
         } 
         else{
            System.out.println(1.a(3, 38));
         }

      } else {
         System.out.println(1.a(4, 87));
      }
   }

   public static String c(String args) {
      char[] var1 = args.toCharArray();
      char[] var2 = new char[var1.length];

      for(int var3 = 0; var3 < var2.length; ++var3) {
         char var4 = var1[var3];
         var2[var3] = (char)(var4 ^ var3 & (2));
      }

      return new String(var2);
   }
}
