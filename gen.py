import sys

start = 0
mode = 'w'

if len (sys.argv) > 1:
    start = int (sys.argv [1])
    mode = 'a'

f = open ('outp', mode)

try:
    for i in range (start, 256):
        c = input (str (i) + ": ")
        f.write ('    "enchantment.level.')
        f.write (str (i))
        f.write ('": "')
        f.write (c)
        f.write ('",\n')
except KeyboardInterrupt: pass
