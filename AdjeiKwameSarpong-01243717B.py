import time
#!/usr/bin/env python
# _*_ coding: utf-8 -*-
"""
This code is to print simple
pattern stars in rows
"""
#Function for the stars
def star_format(num_stars):
    for i in range(1, num_stars + 1):
        print("*" * i)
        time.sleep(1)

if __name__ == "__main__":
   num_stars = int(input("Enter rows: "))
   print("=" * 20)
   star_format(num_stars)