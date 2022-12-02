#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Enter a sentence: ").lower()
    a = set(s.replace(' ', ''))
    vowels = set("aoueiy")
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    print('The total number of vowels in the sentence is = ', count)
