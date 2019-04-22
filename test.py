#!/usr/bin/env python3
"""tests for max_rep.py"""

from subprocess import getstatusoutput, getoutput
import os
import random
import re
import string
import max_rep

prg = "./max_rep.py"

# --------------------------------------------------
def test_usage():
    """usage"""
    rv1, out1 = getstatusoutput(prg)
    assert rv1 > 0
    assert re.match("usage", out1, re.IGNORECASE)

# --------------------------------------------------

def bad_usage():

    rv2, out2 = getstatusoutput("{} -w 275 -r foo".format(prg))
    assert rv2 > 0
    assert re.match('the value given "foo" is not a digit', out2, re.IGNORECASE)

    rv3, out3 = getstatusoutput("{} -w 0 -r 5".format(prg))
    assert rv3 > 0
    assert out3 == "This is not a valid weight for an average human..."

# --------------------------------------------------

def good_usage():

    rv3, out3 = getstatusoutput("{} -w 275 -r 5".format(prg))
    assert rv3 > 0
    assert re.match('Based upon your 5 reps at a weight of 275 lbs, your 1 rep max is 320.83 lbs\nHappy Lifting', out3, re.IGNORECASE)








