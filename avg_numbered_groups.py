"""
Iterate on integers [start, start+size[ with ngroups groups containing
n or n-1 elements.

For example, with start=5, size=10 and ngroups=4:

       [ (5,6), (7,8,9), (10,11) ,(12,13,14),]
gstart    5      7        10       12       
gsize     2      3         2        3       

>>> for gstart,gsize in groups(start=5, size=10, ngroups=4):
...     print gstart, gsize
5 2
7 3
10 2
12 3
"""

def group_start(start,size,igroup,ngroups):
    return start + size * igroup / ngroups

def group_end(start,size,igroup,ngroups):
    return start + size * (igroup+1) / ngroups

def group_size(start,size,igroup,ngroups):
    gstart = group_start(start,size,igroup,ngroups)
    gend = group_end(start,size,igroup,ngroups)
    return gend - gstart

def groups(start,size,ngroups):
    for igroup in range(ngroups):
        gstart = group_start(start,size,igroup,ngroups)
        gsize = group_size(start,size,igroup,ngroups)
        yield gstart, gsize

if __name__ == '__main__':
    import doctest
    doctest.testmod()
