
# bisect use insertion sort , highly eneffcient

import bisect
import random

# Use a constant see to ensure that we see
# the same pseudo-random numbers each time
# we run the loop.
random.seed(1)

# Generate 20 random numbers and
# insert them into a list in sorted
# order.
l = []
for i in range(1, 20):
    r = random.randint(1, 100)
    position = bisect.bisect(l, r)
    bisect.insort(l, r)
    print(l)


  head_map_back = {}
  head_map_back[1] = "<h1>"
  head_map_back[2] = "<h2>"
  head_map_back[3] = "<h3>"
  head_map_back[4] = "<h4>"
  head_map_back[5] = "<h5>"
  head_map_back[6] = "<h6>"