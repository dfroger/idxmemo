"""
Iterate on integers [start, start+size[ with ngroups groups, all containing
gsize = gsizemax elements, except for the last group containing gsize
elements with 1 <= gsize <= gsizemax elements.

>>> for gstart,gsize in groups(start=5, size=10, ngroups=4):
...     print gstart,gsize
5 3
8 3
11 3
14 1
"""

def group_sizemax(size,ngroups):
    if ngroups == 1:
        return size
    else:
        return (size-1) / (ngroups-1)

def group_start(igroup, start, size, gsizemax):
    return start + igroup * gsizemax

def group_size(start, size, gsizemax, gstart):
    return min(start + size - gstart, gsizemax)

def groups(start, size, ngroups):
    gsizemax = group_sizemax(size,ngroups)
    for igroup in range(ngroups):
        gstart = group_start(igroup, start, size, gsizemax)
        gsize = group_size(start, size, gsizemax, gstart)
        yield gstart, gsize

if __name__ == '__main__':
    import doctest
    doctest.testmod()
