#!/usr/bin/python
# -*- coding: utf-8 -*-
# test helloworld.py

def Hello(msg):
    print (msg)
    return msg

def test_Hello():
    assert Hello("Hello, World!") == "Hello, World!"