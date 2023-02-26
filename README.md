# ConwaysGameOfLife-Multithreading


Problem:
You are tasked with creating a Python program capable of executing the first 100 steps of a modified cellular life
simulator. This simulator will receive the path to the input file as an argument containing the starting cellular
matrix. The program must then simulate the next 100 time-steps based on the algorithm discussed on the next
few pages. The simulation is guided by a handful of simplistic rules that will result in a seemingly complex
simulation of cellular organisms.

Below is an example starting cellular matrix consisting of 10 rows and 20 columns.

-----+--+-+----+----
---++-----+-----+---
-------++---+--++---
+--------++++---++++
+----++--+--++--++++
+------+----+--+---+
+-------------++---+
+----------+--+----+
-+--------------+---
----+-++-------+---+


Directions:
Develop a program capable of accepting the following command line arguments:

• -i <path_to_input_file>
o Purpose: This option retrieves the file path to the starting cellular matrix.
o Input Type: String
o Validation: Entire file path must exist, otherwise error.
o Required: Yes


• -o <path_to_output_file>
o Purpose: This option retrieves the file path for the final output file.
o Input Type: String
o Validation: The directories in the file path must exist, otherwise error.
o Required: Yes


• -t <int>
o Purpose: This option retrieves the number of threads to spawn.
o Input Type: Unsigned Integer
o Validation: Must be a positive integer > 0, otherwise error.
o Required: No
o Default Value: 1



Example executions:
• python3 ConwaysGameOfLife.py -i inputFile.txt -o timeStep100.txt -t 36
    o Sets input file to “inputFile.txt”
    o Sets output file to “timeStep100.txt”
    o Sets thread count to 36

• python3 ConwaysGameOfLife.py -o myOutput.txt -i myInput.txt
    o Sets input file to “myInput.txt”
    o Sets output file to “myOutput.txt”
    o Sets thread count to 1 (default when not specified)



Input/Output Files:

Valid input and output files must abide by the following rules:

1) The matrix may only contain the following symbols:
    a. Hyphens ‘-’ to signify currently “dead” cells.
    b. Plus signs ‘+’ to signify currently “alive” cells.
    c. End of Line Characters marking the end of each row.
2) The matrix may not contain any spaces, commas, or other delimiters between symbols.
3) The matrix must separate rows with a line break.
4) The final row does not require a line break but may include one.
5) Files containing any other symbols beyond those listed in #1 are considered invalid.



Processing the Matrix:
Using this starting cellular matrix, your program should then simulate the next 100 steps of a simulation that
uses the following rules to dictate what occurs during each time step:

1) Any position in the matrix with a hyphen ‘-’ is considered “dead” during the current time step.
2) Any position in the matrix with a plus sign ‘+’ is considered “alive” during the current time step.
3) If an “alive” square has two, four, or six living neighbors, then it will be “alive” in the next time step.
4) If a “dead” square has a prime number of living neighbors, then it continues to be “alive” in the next
time step.
5) Every other square dies or remains dead, causing it to be “dead” in the next time step.
For this program, a neighbor is defined as any cell that touches the current cell, meaning each current cell,
regardless of position, has 8 neighboring cells. Cells located at the edge should “wrap around” the matrix to find
their other neighbors. The two examples below show the neighbors (N) for a given cell (C) with example #1
showing a cell in the middle of a matrix and example #2 showing a cell on an edge to demonstrate the “wrap
around” effect.

 Neighbor Example #1        Neighbor Example #2
 
  0 1 2 3 4 5                 0 1 2 3 4 5
0                           0 N       N N
1   N N N                   1
2   N C N                   2
3   N N N                   3
4                           4 N       N N
5                           5 N       N C



Your solution will accept the starting matrix (Time Step 0) as a file from the command line and then simulate
steps 1 through 100. The final matrix (Time Step 100) will then be written to an output file whose name and
path is dictated by a separate command line argument. These files must contain a copy of your matrix with each
row of the matrix printed on separate lines and no characters in between the columns. Example files are
provided as part of the project.

Example time steps for a 6 x 6 matrix

Starting Matrix
(Time Step 0)         Time Step 1         Time Step 2

  0 1 2 3 4 5         0 1 2 3 4 5         0 1 2 3 4 5
0 - + - - - -       0 + - - - - -       0 + + - - - +
1 - - - - - -       1 - - - - - -       1 - - - - - -
2 - - - - - -   →   2 - - - - - -   →   2 - - - - + -
3 - - - - + -       3 - - - + - +       3 + - + - - -
4 - - - - + -       4 - - - + - +       4 - - + - + +
5 + - - - - -       5 - + - - - +       5 - - + - + +



Additional Rules and Hints

Program Output:
Your program may print as much information as you wish to the screen during execution. Your output file should only
contain the matrix generated at time step 100 with no other extraneous information.


Multithreading:
Your solution must also make use of the multiprocessing module and spawn a total number of threads
equivalent to the number specified by the user in the -t option. Keep in mind that your program running
normally would be considered running serially, in other words on a single thread. Failure to make use of proper
multithreading using the multiprocessing module in Python will result in your solution being treated as entirely
incorrect.


Note: Please refer pdf file for these matrices, .md has formatting problems I can't solve. 
