# from collections import deque

gain = [44,32,-9,52,23,-50,50,33,-84,47,-14,84,36,-62,37,81,-36,-85,-39,67,-63,64,-47,95,91,-40,65,67,92,-28,97,100,81]

def prefixSum(arr, element):
    return sum(arr[:arr.index(element)+1])

def largestAltitude(gain) -> int:
    altitude_arr = [0]
    for element in gain:
        altitude_arr.append(prefixSum(gain,element))
    return max(altitude_arr)

print(largestAltitude(gain))