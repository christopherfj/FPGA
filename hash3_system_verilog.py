# -*- coding: utf-8 -*-

M = 16 #no. seeds; no. rows; no. inputs
L = 8 #no. bits

# inicializacion
code_h3 = "//multiplexores de entrada (operaciones AND)"
code_h3 += "\nlogic ["+str(L-1)+":0] "
for i in range(M-1):
    code_h3 += "m"+str(i)+", "
code_h3 += "m"+str(i+1)+";"+"\n" 

max_ = 0
min_ = 0    
for m in range(M):
    max_ = L*(m+1)-1
    code_h3 += "assign m"+str(m)+" = "+"sw["+str(m)+"]?"+"q["+str(max_)+":"+str(min_)+"]:0"+";"+"\n"
    min_ = L*(m+1)
    
code_h3+="\n//arbol de reduccion (operaciones XOR)\n"
if M>2:
    code_h3 += "logic ["+str(L-1)+":0] "
    for i in range(2, M-1):
        code_h3 += "o"+str(i)+", "
    code_h3 += "o"+str(i+1)+";"+"\n" 
    
    i = M-1
    for o in range( M-1, (M-1)/2, -1):
        code_h3 += "assign o"+str(o)+" = m"+str(i)+"^m"+str(i-1)+";"+"\n"
        i-=2
        
    last = o-1
    i = M-1
    level = M/2
    while o !=2:
        level/=2
        for o in range( last, 1, -1):
            code_h3 += "assign o"+str(o)+" = o"+str(i)+"^o"+str(i-1)+";"+"\n"
            i-=2
    
    code_h3 += "assign o = o3^o2;\n"
else:
    code_h3 += "assign o = m1^m0;\n"
    
print code_h3
