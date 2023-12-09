#!/bin/python3

import math
import os
import random
import re
import sys
from collections import namedtuple
from bisect import bisect_left

Place = namedtuple('Place', 'lat, long, height, points')

chunkplaces = {}  # places get inserted into lists contained here, grouped by keys of their locations
chunkvals = {}  # holds values

giant = False


def getkey(place, off_lat=0, off_long=0):
    return ((place.lat // d_lat + off_lat) * 200011) + place.long // d_long + off_long  # unique for n<=200000


def recordvalue(place, val):
    if val < 0:
        return  # not worth going here; no need to track
    key = getkey(place)
    if key not in chunkplaces:
        chunkplaces[key] = []
        chunkvals[key] = []
    if giant:
        if len(chunkvals[key]) == 0:
            chunkvals[key].append(-val)
            chunkplaces[key].append(place)
        else:
            if val < -chunkvals[key][0]:
                return
            else:
                chunkvals[key][0] = -val
                chunkplaces[key][0] = place
    else:
        i = bisect_left(chunkvals[key], -val)
        chunkplaces[key].insert(i, place)
        chunkvals[key].insert(i, -val)


def getbestinchunk(place, key, best):
    # find best suitable match in chunk
    if key not in chunkvals:
        return 0
    for i, (cand, val) in enumerate(zip(chunkplaces[key], chunkvals[key])):
        if -val < best:
            return 0
        if abs(place.lat - cand.lat) <= d_lat \
                and abs(place.long - cand.long) <= d_long:
            return -val
    return 0


def getbest(place):
    # find best match in this and neighboring chunks, then pick the best
    best = 0  # always have the option to stop here
    for i in [0, 1, -1]:
        for j in [0, 1, -1]:
            key = getkey(place, i, j)
            ret = getbestinchunk(place, key, best)
            if ret > best:
                best = ret
    return best


def calculatevalue(place):
    val = place.points + getbest(place)
    recordvalue(place, val)
    return val


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    d_lat = int(first_multiple_input[1])
    d_long = int(first_multiple_input[2])

    places = []
    if d_lat == 200000:
        giant = True

    for n_itr in range(n):
        second_multiple_input = input().rstrip().split()

        latitude = int(second_multiple_input[0])
        longitude = int(second_multiple_input[1])
        height = int(second_multiple_input[2])
        points = int(second_multiple_input[3])

        places.append(Place(latitude, longitude, height, points))

    places.sort(key=lambda p: -p.height)  # compute highest first
    best = 0

    for p in places:
        ret = calculatevalue(p)
        if ret > best:
            best = ret

    print(best)
