# JVM Reverse Engineering


```
Javap is a tool bundled with JDK releases that can disassemble compiled classes. Example usage:

(p = show private members, v = verbose)

javap -v -p HelloWorld.class
```

## simple_hello_world
```bash
javap Main                      
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
Compiled from "SecretSourceFile.java"
class Main {
  Main();
  public static void main(java.lang.String[]);
}


javap -c Main 
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
Compiled from "SecretSourceFile.java"
class Main {
  Main();
    Code:
       0: aload_0
       1: invokespecial #1                  // Method java/lang/Object."<init>":()V
       4: return

  public static void main(java.lang.String[]);
    Code:
       0: iconst_0
       1: istore_1
       2: getstatic     #2                  // Field java/lang/System.out:Ljava/io/PrintStream;
       5: ldc           #3                  // String Hello World
       7: invokevirtual #4                  // Method java/io/PrintStream.println:(Ljava/lang/String;)V
      10: iinc          1, 2
      13: return
}

```


## crack_a_password_protected_application
```bash
javap -c -v  PasswordProtectedApplication > code.txt
2 = String             #22            // yxvF2ho95ANJVCX

```

## Basic_String_Obfuscation
```bash
javap -c BasicStringObfuscation > code.txt

java Decompiled givemepassword
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
aSc2mRT7C6fKql6RD
Incorrect

```

## Advance strings obfuscation
```bash
java -jar BasicStringObfuscation-obf.jar passowrd


```