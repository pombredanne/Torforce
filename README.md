Torforce
========
Bruteforces .onion domain names to discover hidden websites inside the TOR network.
if desired you are able to change the top level domain to something else than
'.onion'.


Usage
=====
The basic usage of the script is:

```
usage: torforce.py [-h] -n NUMBER_OF_LINKS [-t TOP_LEVEL_DOMAIN]

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBER_OF_LINKS, --number-of-links NUMBER_OF_LINKS
                        The amount of links the script should generate.
  -t TOP_LEVEL_DOMAIN, --top-level-domain TOP_LEVEL_DOMAIN
                        The top level domain to append to the generated URL,
                        by default it generates .onion links.
```
