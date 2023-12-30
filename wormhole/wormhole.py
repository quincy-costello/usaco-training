'''
ID: quincy.3
TASK: wormhole
LANG: PYTHON3
'''
from itertools import product

infile = open("wormhole.in", "r")
portals = [ tuple(int(coord) for coord in infile.readline().split()) for i in range(int(infile.readline())) ]
infile.close()

nexts = {}
for portal in portals:
    closest = 1_000_000_001
    for portal1 in portals:
        if portal[1] == portal1[1] and portal1[0] > portal[0] and portal1[0] < closest:
            closest = portal1[0]
    if closest != 1_000_000_001:
        nexts[portal] = closest
    else:
        nexts[portal] = False

'''
set of pairings                  -- pairings
    set of pairs                 -- pairing
        set of 2 portals         -- pair
            tuple of x, y coords -- portal
'''

def get_pairings(portals):
    pairings = set()

    if len(portals) > 0:
        min_portal = min(portals)
    count = 0
    for portal in portals:
        count += 1
        #print(count)
        if portal != min_portal:
            pair = frozenset([min_portal, portal])

            copy = list(portals)
            copy.remove(min_portal)
            copy.remove(portal)
            sub_pairings = get_pairings(copy)

            for sub_pairing in sub_pairings:
                pairing = set(sub_pairing)
                pairing.add(pair)
                pairing = frozenset(pairing)
                pairings.add(pairing)
            if len(sub_pairings) <= 0:
                # print(pair)
                pairings = frozenset([frozenset([pair])])

    return pairings

"""
def get_pairings(portals):
    # Making set of pairs of portals
    pairs = set()
    for pair in product(portals, repeat=2): # iterating over pairs (as sets) of portals
        pair = frozenset(pair)
        if len(pair) == 2:
            pairs.add(pair)
    pairs = frozenset(pairs)

    pairings = set()
    for pairing in product(pairs, repeat=int(len(portals)/2)):
        pairing = frozenset(pairing)

        if len(pairing) == len(portals)/2:
            valid = True
            for pair in pairing:
                for portal in pair:
                    for other_pair in pairing:
                        if other_pair != pair:
                            if portal in other_pair:
                                valid = False
                                break
                    if not valid:
                        break
                if not valid:
                    break
            if valid:
                pairings.add(pairing)

    return frozenset(pairings)
"""

def mainloop():
    pairings = get_pairings(portals)

    cow_coords = ()
    num_loops = 0
    has_loop = False
    for pairing in pairings: # Looping through pairings
        for portal in portals: # Looping through starting positions
            cow_coords = portal # tuple
            original_coords = cow_coords # tuple
            while True: # Looping until wormhole loop found
                for pair in pairing: # If cow is on a portal, teleport cow to other corresponding portal
                    if cow_coords in pair:
                        cow_coords = tuple(pair)[tuple(pair).index(cow_coords)-1] # Genius way of switching to the other portal
                        break

                nextx = nexts[cow_coords]
                if nextx == False:
                    has_loop = False
                    break

                cow_coords = (nextx, cow_coords[1])

                if cow_coords == original_coords:
                    has_loop = True
                    break

            if has_loop:
                has_loop = False
                num_loops += 1
                break
    return num_loops

outfile = open("wormhole.out", "w")
print(mainloop(), file=outfile)
outfile.close()