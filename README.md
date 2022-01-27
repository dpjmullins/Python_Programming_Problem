# Python Programming Problem

## Problem setup
Consider a discrete grid of size n × n. Here is an example for n = 5.

   j -> 
      1  2  3  4  5  
i    +--+--+--+--+--+
|  1 |  |  |  |  |  |
v    +--+--+--+--+--+
   2 |  |  |  |  |  |
     +--+--+--+--+--+
   3 |  |  |  |  |  |
     +--+--+--+--+--+
   4 |  |  |  |  |  |
     +--+--+--+--+--+
   5 |  |  |  |  |  |
     +--+--+--+--+--+
     
We define the following operations:

Operations (1) and (2)
Inside the grid, we may delete horizontal or vertical borders:

(1) Vertical:
delete_v (i, j):
    remove border to the right of row i and column j
In the example above, delete_v(2, 3) yields the following result:

   j -> 
      1  2  3  4  5  
i    +--+--+--+--+--+
|  1 |  |  |  |  |  |
v    +--+--+--+--+--+
   2 |  |  |     |  |
     +--+--+--+--+--+
   3 |  |  |  |  |  |
     +--+--+--+--+--+
   4 |  |  |  |  |  |
     +--+--+--+--+--+
   5 |  |  |  |  |  |
     +--+--+--+--+--+

(2) Horizontal
delete_h (i, j):
    remove border below row i and column j
Continuing from above, applying, delete_h(4, 3) gives:

   j -> 
      1  2  3  4  5  
i    +--+--+--+--+--+
|  1 |  |  |  |  |  |
v    +--+--+--+--+--+
   2 |  |  |     |  |
     +--+--+--+--+--+
   3 |  |  |  |  |  |
     +--+--+--+--+--+
   4 |  |  |  |  |  |
     +--+--+  +--+--+
   5 |  |  |  |  |  |
     +--+--+--+--+--+

Operation (3)
We may also remove and intersection:

delete_isec (i, j):
    remove intersection to the bottom and right of row i and column j

Applying delete_isec (2, 3) gives:

   j -> 
      1  2  3  4  5  
i    +--+--+--+--+--+
|  1 |  |  |  |  |  |
v    +--+--+--+--+--+
   2 |  |  |     |  |
     +--+--+     +--+
   3 |  |  |     |  |
     +--+--+--+--+--+
   4 |  |  |  |  |  |
     +--+--+  +--+--+
   5 |  |  |  |  |  |
     +--+--+--+--+--+

Exercise:
Given n, implement a data structure / representation with which we can:
a. initialize a complete grid of size n with all borders present,
b. execute operations (1), (2), (3) as defined above (e.g. provide a function for each operation), and
c. can print the value of all borders in the format shown above.
