#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 10:49:49 2018

@author: takamasa
"""

if __name__ == "__main__":
    print("スクリプト実行時に実行されるよ")

a = 2
if a%15==0:
    print("FizzBuzz")
elif a%5==0:
    print("Buzz")
elif a%3==0:
    print("Fizz")
else:
    print(a)