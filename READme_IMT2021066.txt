-------Assignment 1 - IMT2021066 Yukta Arvind Rajapur-------

In IAS architechture there are mainly 2 cycles:
1) Fetch
2) Decode and Execute

On opening IMT2021066_1.py

-->A memory array m is defined as a list with 1000 storage space

-->Global variables PC,MAR,IBR,IR,MBR,MQ,AC are defined

-->address func() is defined as I have used it to convert decimal to binary in 40-bit instructions

-->fetch_execute() func mainly defined for IAS implementation, It does the fetch cycle common to all instructions and proceeds to decode the opcode and executes accordingly.PC is incremented at end of every cycle
	The following instructions have been included and have been used in programs that follow:
	-LOAD MX
	-STOR MX
	-LOAD MQ MX
	-LOAD MQ
	-ADD MX
	-SUB MX
	-MUL MX

--> In #main we have the driver code. A menu appears on running 1.py which displays the follows:

Enter the operation you want to perform
1-->Add 2 numbers
2-->Subtract 2 numbers
3-->Perimeter of isosceles triangle
4-->Subtraction of 2x2 matrix
5-->Multiplication of 2 numbers
6-->Total surface area of cuboid
choice: 

On inputting your choice(1-6), the chosen one excutes and displays the result in the terminal.
The program is designed to run only one program at a time, so you have to run it again to try another operation

--->Menu option 6 Calculates Total surface area of a cuboid which is the main assignment program implemented. This contains 15 instructions using more than 4 commands.(Jump not implemented as ma'am said it wasnt needed if your program obeys the rest of the requirements)

Rest of the options are simple calculation programs

-->For each operation, memory location and 40-bit instruction has been hardcoded into specific memory locations. Only input values can be decided by the user. The comments indicate the assembly instruction being implemented.For the larger series of instructions, fetch cycle is called by passing PC.

-->Test cases are in results.txt file 

-------END----------
