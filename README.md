# Programming exercise 2024
## Explanation Solution
 - My idea is to get prices from all operators and compare them with each other to get the lowest price.
 - Because each telephone prefix will have a corresponding price, I chose the dictionary data type, because with a prefix, getting the price is very easy. And we will get price of longest prefix so I create for loop to get prefix with order longest to shortest from phone number.
 - Therefore, the algorithmic complexity of this solution will be O(m*n) with m is number operator and n is length of telephone number.
## Run instructions
1. Setup environment
 - Only need install Python.
2. Running Unit Test
```
python -m unittest
```
 - Currently, I add 2 test cases is can/cannot find price with provide list prices and phone number. You can add more test case or edit current test case to check.
