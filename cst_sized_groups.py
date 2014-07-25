"""
Iterate on integers [start, start+size[ with groups of size gsizemax,
all containing gsize = gsizemax elements, except for the last group
containing gsize elements with 1 <= gsize <= gsizemax elements.

For example, with start=5, size=10 and gsizemax=3:

       [ (5,6,7), (8,9,10),  (11,12,13), (14),]
gstart    5        8          11          14
gsize     3        3           3           1

>>> for gstart, gsize in groups(start=5, size=10, gsizemax=3):
...     print gstart, gsize
5 3
8 3
11 3
14 1
"""    

def groups_number(size, gsizemax):
    return (size + gsizemax - 1) / gsizemax

def group_start(igroup, start, size, gsizemax):
    return start + igroup * gsizemax

def group_size(start, size, gsizemax, gstart):
    return min(start + size - gstart, gsizemax)

def groups(start, size, gsizemax):
    ngroups = groups_number(size, gsizemax)
    for igroup in range(ngroups):
        gstart = group_start(igroup, start, size, gsizemax)
        gsize = group_size(start, size, gsizemax, gstart)
        yield gstart, gsize

if __name__ == '__main__':
    import doctest
    doctest.testmod()
