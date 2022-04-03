public class Decompiled{
   private static final String correctPassword = "aRa2lPT6A6gIqm4RE";

   public static void main(String[] var0) {
      if (var0.length >= 1) {
         String var1 = var0[0];
         if (xor("aRa2lPT6A6gIqm4RE").equals(var1)) {
            System.out.println("Correct!");
         } else {
            System.out.println("Incorrect");
         }

      } else {
         System.out.println("Please provide a password");
      }
   }

   private static String xor(String var0) {
      char[] var1 = var0.toCharArray();
      char[] var2 = new char[var1.length];

      for(int var3 = 0; var3 < var2.length; ++var3) {
         char var4 = var1[var3];
         var2[var3] = (char)(var4 ^ var3 % 3);
      }
      System.out.println(var2);
      return new String(var2);
   }
}
    