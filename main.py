#!/usr/bin/python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

bzz_scale = 1e16
bzz_count = 1.25e24 / bzz_scale

init_supply = 66208125 * bzz_scale
current_supply = 66208125 * bzz_scale

def f(x):
    return x + x * pow(x / 6.25 / 1e23, 31)

def DAI(x):
    return (f(current_supply + x * bzz_scale) - f(current_supply)) / 1e18

def calc(mint):
    global current_supply
    current_supply = init_supply + mint * bzz_scale
    return DAI(1)

def draw(top):
    x = np.arange(0, top)
    y = calc(x)
    plt.title("Price Calculation")
    plt.xlabel("Token Mint")
    plt.ylabel("Token Price (DAI)")
    plt.figure()
    plt.plot(x, y)

maxv = bzz_count - init_supply / bzz_scale
tops = [maxv / 1e4, maxv / 1e3, maxv / 1e2, maxv / 1e1, maxv]
for top in tops:
    draw(top)
plt.show()