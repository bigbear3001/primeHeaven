# primeHeaven

This is a little project to experiment with getting primes as fast as possible (for me at least)

Run this and record the time if you think you made an improvement (finding primes from 0 to 1,000,000):
```
time ./main.py
```

# Versions:
tested on AMD Ryzen 5900x, 64GB Ram, Ubuntu 20.04, Python 3.8.10
## 0.0.1
```
real    9m20,237s
user    9m20,098s
sys     0m0,020s
```
## 0.0.2
added KNOWN_PRIMES cache tuple
```
real    8m9,792s
user    8m7,836s
sys     0m1,788s
```
## 0.0.3
created a cache class that keeps track of min and max value
```
real    5m23,331s
user    5m21,369s
sys     0m1,900s
```
## 0.0.4
use a set instead of a dict as cache structure for faster `in` lookups
```
real    3m19,707s
user    3m19,429s
sys     0m0,224s
```