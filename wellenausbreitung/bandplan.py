#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 14:14:03 2021

@author: michi
"""

bands = [160,
         80,
         40,
         30,
         20,
         17,
         15,
         12,
         10,
         6,
         2,
         0.7,
         0.23,
         0.03]

# f = c / lambda
c = 2.99e8

for band in bands:
    frequency = c / band
    print("{:>6.2f} m --> {:>9.3f} MHz".format(band, frequency * 1e-6))
