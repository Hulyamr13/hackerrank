#!/bin/python3

import math
import os
import random
import re
import sys

import requests


#
# Complete the 'ipTracker' function below.
#
# URL for cut and paste
# https://jsonmock.hackerrank.com/api/ip?ip=<ip>
#
# The function is expected to return a STRING.
# The function accepts a singe parameter ip.
# In case of no ip record, return string 'No Result Found'
#

def ipTracker(ip):
    # Write your code here
    url = f"https://jsonmock.hackerrank.com/api/ip?ip={ip}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data['total'] > 0:
            return data['data'][0]['country']
        else:
            return 'No Result Found'
    else:
        return 'No Result Found'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ip = input()

    result = ipTracker(ip)

    fptr.write(str(result) + '\n')

    fptr.close()
