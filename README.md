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
## 0.0.5
keep a separate list for index based returning of prime ranges
```
real    2m4,931s
user    2m4,687s
sys     0m0,224s
```
## 0.0.6
test divisors only up to the sqrt of the possible prime
```
real    0m1,526s
user    0m1,497s
sys     0m0,028s
```
updated number to test for the first 100 000 000 primes in batches of 100000
```
real    9m6,634s
user    9m5,551s
sys     0m0,988s
```
## 0.0.7
add a fastpath: if decimal integer is ending in 5 it is not a prime (except 5 itself)
```
real    8m30,763s
user    8m29,745s
sys     0m0,936s
```
## 0.0.8
add fermat primality test as fastpath for composite numbers
```
real    4m57,187s
user    4m55,881s
sys     0m1,252s
```