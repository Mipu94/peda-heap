from __future__ import division, print_function, absolute_import, unicode_literals
import struct
import itertools
import idblib
from idblib import hexdump



def dumplist(id0, listname, dumper):
    """
    Lists are all stored in a similar way.
    """
    sroot = id0.nodeByName(listname)
    if not sroot:
        return
    structs={}
    for i in itertools.count():
        snode = id0.int(sroot, 'A', i)
        if not snode:
            break
        struct=dumper(id0, snode - 1,structs)
    return struct


def dumpstructmember(id0, spec):
    def i64(a, b): return a + (b << 32)
    if id0.wordsize == 8:
        f = i64(spec[0], spec[1]), i64(spec[2], spec[3]), i64(spec[4], spec[5]), spec[6], spec[7]
    else:
        f = spec
    nodeid = f[0] + id0.nodebase
    name = id0.name(nodeid)
    if f[2] <= id0.wordsize:
        return [name,f[2],1]
    else:
        return [name,1,f[2]]


def dumpstruct(id0, node,structs):
    """ dump all info for the struct defined by `node` """
    name = id0.name(node)
    packed = id0.blob(node, 'M')
    spec = idblib.idaunpack(packed)
    entsize = 5 if id0.wordsize == 4 else 8
    k=[]
    for i in range(spec[1]):
        member=dumpstructmember(id0, spec[entsize * i + 2:entsize * (i + 1) + 2])
        k.append(member)
    structs[name]=k
    return structs

def parse_idb(filename):
    try:
        with open(filename, "rb") as fh:
            id0 = idblib.IDBFile(fh).getsection(idblib.ID0File)
            structs=dumplist(id0, '$ structs', dumpstruct)
            return structs
    except Exception as e:
        print("ERROR: %s" % e)