
# simpler way to count objects
from collections import Counter

words =  ['red', 'blue', 'red', 'green', 'blue', 'blue']

cnt = Counter(words)

top = Counter(words).most_common(10)
print(top)

