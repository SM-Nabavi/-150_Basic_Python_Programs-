# Program 22

Write a Python Program to Find LCM.

**Least Common Multiple (LCM):**
LCM, or Least Common Multiple, is the smallest multiple that is exactly divisible by two or more numbers.

**Greatest Common Divisor (GCD) - Subtraction Method:**
GCD can be found by repeatedly subtracting the smaller number from the larger number until both numbers become equal:

$$GCD(a, b) = \begin{cases} 
a & \text{if } a = b \\
GCD(a-b, b) & \text{if } a > b \\
GCD(a, b-a) & \text{if } b > a 
\end{cases}$$

Example with 48 and 18:

48 > 18 → 48 - 18 = 30<br>
30 > 18 → 30 - 18 = 12<br>
18 > 12 → 18 - 12 = 6<br>
12 > 6 → 12 - 6 = 6<br>
6 = 6 → GCD = 6<br>

Formula:

For two numbers a and b, the LCM can be found using the formula:

$$LCM(a, b) = \frac{|a \cdot b|}{GCD(a, b)}$$
For more than two numbers, you can find the LCM step by step, taking the LCM of pairs of numbers at a time until you reach the last pair.

Note: GCD stands for Greatest Common Divisor.

## Output example *main.py*
```
Enter the number 1: 5
Enter the number 2: 11
L.C.M 5 and 11 is 55.
```