import random
from itertools import product
import argparse

# Author:   Daxda
# Date:     26.04.2014
#
# Description:
# Bruteforces a defined amount of randomly generated URLs to discover .onion sites.
# Alternatively you are able to modify the top level domain to something other
# than '.onion'.

def main(args):
    domain = ".onion"
    if args.top_level_domain:
        if args.top_level_domain[0] != ".":
            domain = "." + args.top_level_domain
        else:
            domain = args.top_level_domain
    for _ in range(0, args.number_of_links):
        alpha = list("1eFGHIJKLM2NOP6QRs5tuvabcdw3xyzABC7DE4fghijklm8no0pqrST9UVWXYZ")
        random.shuffle(alpha)
        random.shuffle(alpha)
        random.shuffle(alpha)
        print "http://" + "".join(alpha)[:16] + domain

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number-of-links", type=int, required=True,
                        help="The amount of links the script should generate.")
    parser.add_argument("-t", "--top-level-domain", required=False,
                        help="The top level domain to append to the generated URL,"+\
                             " by default it generates .onion links.")
    args = parser.parse_args()
    main(args)
