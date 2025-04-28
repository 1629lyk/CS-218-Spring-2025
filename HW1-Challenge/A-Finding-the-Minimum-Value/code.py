import sys
input = sys.stdin.readline # faster way to read data compared to just base input()
import math

def r_ternary_search(func, l_ts, r_ts, e = 1e-8):
       if r_ts - l_ts < e:
              return func((l_ts + r_ts) / 2)
       
       mid1 = l_ts + (r_ts - l_ts) / 3
       mid2 = r_ts - (r_ts - l_ts) / 3
       
       if func(mid1) < func(mid2):
              return r_ternary_search(func, l_ts, mid2, e)
       else:
              return r_ternary_search(func, mid1, r_ts, e)

def main():
       a = float(input())
       func = lambda x: (x**2) / (math.log(x) + a*x)
       min_val = r_ternary_search(func, 1.0000001, 1.9999999)
       print(f"{min_val:.9f}") # 9 decimal places
 
if __name__ == "__main__":
    main()