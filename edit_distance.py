def edit(s1, s2):
    # Lookup memoized storage
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)
    if s1[0] == s2[0]:
        cost = 0
    else:
        cost = 1
    return min(edit(s1, s2[1:]) + 1, edit(s1[1:], s2) + 1, edit(s1[1:], s2[1:]) + cost)

print edit('test', 'tesse')
