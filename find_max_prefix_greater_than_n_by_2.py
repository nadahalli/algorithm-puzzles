a = [
    'aaa',
    'aab',
    'aac',
    'abc',
    'abd',
    'abx',
    'abxa',
    'abxb',
    'abxd',
    'abxe',
    'abxf',
    'abxg',
    'abxh',
    'abxi',
    'abxj',
    'aby',
]

i = 0
n = len(a)
max_prefix = ''
max_prefix_count = 0

from collections import defaultdict

while True:
    counts = defaultdict(int)
    small_words = 0
    for word in a:
        if i >= len(word):
            small_words += 1
            continue
        if not word.startswith(max_prefix):
            continue
        counts[word[i]] += 1    
    if small_words == n:
        break
    max_count_letter = None
    max_count = 0
    for letter, count in counts.iteritems():
        if count > max_count:
            max_count_letter = letter
            max_count = count
    if max_count <= n/2:
        break
    else:
        max_prefix = max_prefix + max_count_letter
        max_prefix_count = max_count
    i += 1

print max_prefix, max_prefix_count
        
