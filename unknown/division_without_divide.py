#!/usr/bin/python3
'''
Applied PEP8 (pycodestyle)

Author:       Aziz Furkan DAGLI
Date  :       03.01.2020
Description : This problem was asked by Nextdoor.
              Implement integer division without using the
              division operator. Your function should return a tuple of (dividend, remainder)
              and it should take two numbers, the product and divisor.
              For example, calling divide(10, 3) should return (3, 1) since the divisor is 3
              and the remainder is 1
              Bonus: Can you do it in O(log n) time?
'''

import sys


class Division():
    def __init__(self, product, divisor):
        if not divisor == 0:
            self.product = abs(product)
            self.divisor = abs(divisor)

            self.product_sign = self.num_sign(product)
            self.divisor_sign = self.num_sign(divisor)
            print(f"\n{product} {divisor}\n")
        else:
            print("ZeroDivisionError: division by zero")
            sys.exit(1)

    def num_sign(self,num):
        if num >= 0:
            return 1
        else:
            return -1

    def divide(self):
        div_result = 0
        while self.product >= self.divisor:
            self.product = self.product - self.divisor
            div_result = div_result + 1

        return (div_result*(self.product_sign*self.divisor_sign), self.product)


if __name__ == "__main__":
    product = -21
    divisor = 2
    instance = Division(product, divisor)
    tuple_result = instance.divide()
    print(tuple_result)
