#!/usr/bin/env python
# -*- coding: utf-8 -*-
f = open("here.txt", "r")
username = f.readline().strip('\n')
password = f.readline().strip('\n')
print username
print password
