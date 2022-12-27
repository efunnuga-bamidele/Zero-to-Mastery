from collections import Counter, defaultdict, OrderedDict
import datetime
from array import array

li = [1,2,3,4,5,6,7,7]

print(Counter(li))

dictionary = defaultdict(lambda: 'does not exist', {'a': 1, 'b' : 2})
print(dictionary['c'])

print(datetime.date.today())

arr = array('i', [1,2,3])

print(arr[0])