# -*- coding: utf-8 -*-

import random
import re

D = 4 #numero de hash
bits = 8 # numero de bits
seed = 16 #numero de semillas en cada hash

agregados = []
semillas = []
for d in range(D):
    semillas.append([])
    for s in range(seed):
        bin_ = re.sub(r'^0b', r'%s%s' %(bits, "'b"), bin(random.randint(0,255)) ) #En formato systemverilog
        dif = 3+bits-len(bin_)
        if dif>0:
            bin_ = re.sub(r"8'b", r"8'b"+"0"*dif, bin_)
        while bin_ in agregados:
            bin_ = re.sub(r'^0b', r'%s%s' %(bits, "'b"), bin(random.randint(0,255)) ) #En formato systemverilog
            dif = 3+bits-len(bin_)
            if dif>0:
                bin_ = re.sub(r"8'b", r"8'b"+"0"*dif, bin_)
        agregados.append(bin_)
        semillas[d].append(bin_)
            
print "//seeds: mas significativas a menos significativas"
semillas_sim = [] # Solo para simulacion   
check = set() # Solo para verificacion
for d in range(D):
    
    semillas_sim.append([])
    
    seed = "q"+str(d)+" = {"
    for s in semillas[d]:
        seed+=s+', '
        
        check.add( s )
        semillas_sim[d].append( re.sub(r"^8'", r'0', s) ) #formato bin python
        
    seed = re.sub(r'\, $', r'};', seed)
    print seed
    
    
    

