#!/usr/bin/python3
"""
Test script
"""

import sys

# Correct module import syntax
number_of_subscribers = __import__('0-subs').number_of_subscribers

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass subreddit name")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
