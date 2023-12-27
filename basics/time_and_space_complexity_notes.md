# [Time and Space Complexity!](https://www.youtube.com/watch?v=FPu9Uld7W-E&list=PLgUwDviBIf0oF6QL8m22w1hIDC1vJ_BHz&index=4)

## What is Time Complexity ?

 - This is how the interviewer will judge the code that we have written. 
 - Rate at which the time taken to run the code increases with respect to input size

## Why TC != Time Taken ?

 - The code can run in different time on different hardware. For example, old windows machine vs new macbook pro

## Big O Notation

 - Every piece of code takes time in terms of the Big-O Notation
 - O(time taken)
	 - Number of steps that the code will take

### Example

    // Program to print a text 5 times
    
    class Main {
      public static void main(String[] args) {
    
        int n = 5;
        // for loop  
        for (int i = 1; i <= n; ++i) {
          System.out.println("Java is fun");
        }
      }
    }

for every loop, the program is doing the following: 

 1. Increment
 2. Check
 3. Print

So there are a total of 3 steps being performed every time

In conclusion, this will be represented as **Big-O of 15** or **O(15)** or **O(3xN)**. 

## 3 Rules of Time Complexity

 1. Calculate with worst case scenario.  
 2. Avoid Constants -- when the input size is very large, the impact of constants is insignificant
 4. Avoid Lower Values  

## Best, Average, Worst Case

**BigO**: worst scenario  
**Theta**: average case scenario  
**Omega**: Best Case Scenario - When the program takes the least amount of time

Space Complexity:  SC is also calculated in BigO notation itself 

## Question 1
    class Main {
      public static void main(String[] args) {
   
        // for loop  
        for (int i = 0; i <= n; ++i) {
	        for (int j = 0; j < n; j++) {
		        some code here
		        }
        }
      }
    }
   
The outer loop is running for N times, and the inner loop is also running for N times. 

When i is 0, j goes from 0 to n. 
When i value increases to 1, j goes from 0 to n. So on and so forth. 

We can represent this as: NxN or N^2 iterations

## Question 2
    class Main {
      public static void main(String[] args) {
   
        // for loop  
        for (int i = 0; i < n; ++i) {
	        for (int j = 0; j <= i ; j++) {
		        some code here
		        }
        }
      }
    }

When i is 0, j runs for just one value -- 0. 
When i value increases to 1, j runs for 0 and 1. So on and so forth. 

We can represent this as: N^2/2 + N/2
But we don't consider the constants or small number so we can represent it as: N^2/2

## Space Complexity
### What is Space Complexity
- It is known as the memory space that our program takes in the computer
- Varies from machine to machine
- We will use the Big-O Notation

There are two spaces.  
 1. **Auxiliary Space**: The space taken to solve problem.
 2. **Input Space**: The space taken to store the solution.

## Example

`C=a+b` 
Where C is auxiliary Space.  
a and b are input space.  

In this case our space complexity would be **O(3)**.

If we are using an **array of N objects**, then our input space complexity is **O(N)**.

While coding, tampering the input for space complexity is wrong practice.

**Never change the Input** -- Data should not be touched
We cannot do **b = a + b**

## Number of Operations
On most servers, usually 1 second roughly equals 10^8 operations. 
