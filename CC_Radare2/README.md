# Radare2

## Command Line Options 
```bash
1 > What flag to you set to analyze the binary upon entering the r2 console (equivalent to running aaa once your inside the console) 
	> -A

2 > How do you enable the debugger?     
	> -d

3 > How do you open the file in write mode?
	> -w

4 >	How do you enter the console without opening a file   
	> - 
```


## Analyzation
```bash
Analyzation commands start from a

1 > What command "Analyzes Everything" (all functions and their arguments: Same as running with radare with -A)
	> aaa

2 > What command does basic analysis on functions?
	> af

3 > How do you list all functions?
	> afl

4 > How many functions are in the example1 binary?
	> 12
5 > What is the name of the secret function in the example1 binary?
	> secret_func
```


## Information
```bash
Information commands start from i



1 > What command shows all the information about the file that youre in?
	> ia   

2 > How do you get every string that is present in the binary?
	> izz

3 > What if you want the address of the main function?
	> iM    

4 > What character do you add to the end of every command to get the output in JSON format?
	> j

5 > How do you get the entrypoint of the file?
	> ie

6 > What is the secret string hidden in the example2 binary?
	> izz goodjob    


```


## Navigating Through Memory
```bash
s is the command that is used to navigate through the memory of your binary. With it and its variations you can you can get information about where you are in the binary as well as move to different points in the binary.


Note: For user created functions that arent main, you will have to add sym. before them for example sym.user_func



1 > How do you print out the the current memory address your located at in the binary?
	> s

2 > What command do you use to go to a specific point in memory with the syntax <command> <address>?
	> s

3 > What command would you run to go 5 bytes forward?
	> s+5

4 > What about 12 bytes backward?
	> s- 12

5 > How do you undo the previous seek?
	> s--

6 > How would go to the memory address of the main function?
	> s main

7 > What if you wanted to go to the address of the rax register?
	> sr rax
```

## Printing
```bash
p is a command that shows data in a myriad of formats. The command is useful for when you want to get information about what is happening in memory, and get some of the data thats contained in memory as well. With the p command it is also useful to know about the @ symbol in radare. The @ symbol is used to specify that something is an address in memory, for example if you wanted to specify you were talking about the memory address of the main function you would use <command>@main



1 > How would you print the hex output of where you currently are in memory?
	> px

2 > How would you print the disassembly of where youre currently at in memory?
	> pd

3 > What if you wanted the disassembly of the main function?
	> pd @ main

4 > What command prints out the emoji hexdump? (this is not useful at all I just find it funny)
	> pxe

5 > What if you decided you were too good for rows and you wanted the disassembly in column format?
	> pC
```


##  The Mid-term
```bash
Congrats on getting to this point, you now know enough to pass the mid-term exam. The questions in this task will all be related to commands that were in previous tasks so if you skipped one, I recommend going back and doing it. As you probably guessed from the file name all exercises in this task will be done using the midterm binary file.


```

## Debugging
```bash
Recall that in the task "Command Line Options" you learned that the -d flag has radare enter debug mode. Debug mode allows you to set breakpoints and offers a lot of options to not only navigate through your binary, but to analyze the data that goes in and out of the registers as well.
Answer the questions below

1 > How do you set a breakpoint?
	> db

2 > What command is used to print out the values of all the registers?
	> dr
3 > How do you run through the program until the program either ends or you hit the next breakpoint?
	> dc

4 > What if you want to step through the binary one line at a time?
	> ds

5 > How do you go forth 2 lines in the binary?
	> ds 5

6 > How do you list out the indexes and memory addresses of all breakpoints?
	> dbi
Go back through all previous binaries and mess around with debug mode

```


## Visual Mode
```bash
While visual mode is by no means necessary and wont inherently teach you anything new about the binary youre currently running. It allows the assembly to more human readable and provides a lot of options to enhance the visual appeal of radare and can definitely improve efficiency. Therefore I would state its a valuable tool that you should know how to use. All commands involving visual mode start with v




1 > How do you enter "graph mode" which allows everything to be organized in nice readable boxes?(A personal favorite of mine. Also note that the second character is uppercase)
	> vV

2 > What character do you press to run normal radare commands inside visual mode?
	> :

3 > How do you go back to the regular radare shell(leaving visual mode)?
	> q

4 > What if you want to step through the binary inside Visual mode?
	> s

5 > How do you add a comment?
	> ;
```

## Write Mode
```bash
Occasionally you might end up in a situation where a task is impossible to solve with the current instructions. For example take this code 

int val = 4;

if(val == 5){

printf("%s","You win!");

}


You will never be able to get it to print out You win! because under normal circumstances val will never be set equal to 5. This is where write mode comes in, it allows you to change instructions so you can get certain conditions to execute. All commands involving write mode start with w


Answer the questions below

1 > How do you write a string to the current memory address.
	> w

2 > What command lists all write changes?
	> wc

3 > What command modifies an instruction at the current memory address?
	> wa

Get the example4 binary to show the You win! message

```


