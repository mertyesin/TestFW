#!/usr/bin/env python
import pytest
from selenium import webdriver

def test_google():
	driver = webdriver.Chrome()
	driver.get("http://demo.guru99.com/test/newtours/index.php")

def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4