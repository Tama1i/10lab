#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == "__main__":
    # Определим универсальное множество
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = set("ahk")
    b = set("cdhpr")
    c = set("hiz")
    d = set("cgjvw")

    x = (a.union(b)).intersection(c)
    print(f"x = {x}")

    # Найдем дополнения множеств
    an = u.difference(a)
    bn = u.difference(b)

    y = (an.intersection(bn)).difference(c.union(d))
    print(f"y = {y}")