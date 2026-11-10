from consts import DEFAULT_UNIVERSAL_SET

def get_intersection(A: tuple, B: tuple) -> tuple:
    C = []
    for a in A:
        if a in B: C.append(a)
    return tuple(C)


def get_union(A: tuple, B: tuple) -> tuple:
    C = list(A)
    for b in B:
        if b not in C: C.append(b)
    return tuple(C)


def get_difference(A: tuple, B: tuple) -> tuple:
    C = list(A)
    for b in B:
        if b in C: C.remove(b)
    return tuple(C)


def get_symmetric_difference(A: tuple, B: tuple) -> tuple:
    return get_union(get_difference(A, B), get_difference(B, A))


def get_complement(A: tuple, U: tuple = None) -> tuple:
    if U is None: U = DEFAULT_UNIVERSAL_SET
    return get_difference(U, A)


def get_projection(A: tuple, mode: int = 0) -> tuple[bool, tuple]:
    B = []
    for a in A:
        if type(a) is not tuple or len(a) != 2: 
            if mode == 1: continue
            else:
                if type(a) is tuple and a[0] not in B: B.append(a[0])
                elif a not in B: B.append(a)
            continue
        if a[mode] not in B: B.append(a[mode])
    return True, tuple(B) 


def get_composition(A: tuple, B: tuple) -> tuple[bool, tuple]:
    C = []
    for a in A:
        if type(a) is not tuple or len(a) != 2: return False, ()
        for b in B:
            if type(b) is not tuple or len(b) != 2: return False, ()
            if a[1] == b[0] and (a[0], b[1]) not in C: C.append((a[0], b[1]))
    return True, tuple(C)


def get_inversion(A: tuple) -> tuple[bool, tuple]:
    C = []
    for a in A:
        if type(a) is not tuple or len(a) != 2: return False, ()
        if (a[1], a[0]) not in C: C.append((a[1], a[0]))
    return True, tuple(C)