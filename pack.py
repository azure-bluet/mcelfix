fcon = open ('outp') .read ()
fcon = fcon [:-2]
fcon += '\n'
f = open ('assets/minecraft/lang/en_us.json', 'w')
f.write ('{\n')
f.write (fcon)
f.write ('}\n')
f.close ()
