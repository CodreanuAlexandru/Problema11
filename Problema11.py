with open('Lista.txt','r')as f:
    z=list(eval(f.read()))
if len(z)<10:
    print('Primele 5 element:',z[:5])
    b=[]
    for i in range(1,len(z)+1):
        b.append(z[i-2*i])
    print('Lista inversa:',b)
    c=sorted(z)
    c.sort(reverse=True)
    print('Lista descrescatoare:',c)
    for i in range(len(z)):
        if z[i]%2==0:
            print('Element par:',z[i])
    z=list(eval(f.read()))
    print('Media aritmetica:',sum(z)/len(z))
    for i in range(len(z)):
        if z[i]%2==1:
            print('Elemente impare:',z[i])
    x1=int(input('Introduceti x1:'))
    y1=int(input('Introduceti y1:'))
    for i in range(len(z)):
        if z[i]>x1 and z[i]%y1!=0:
            print('Elemente mai mari ca x si indivizibil la y',z[i])
    x2=int(input('Introduceti x2:'))
    y2=int(input('Introduceti y2:'))
    for i in range(len(z)):
        if z[i]>x2 and z[i]<y2:
            print('Elementele intre x si y:',z[i])
    for i in range(len(z)):
        if z[i]<0 and z[i]%2!=0:
            print('Elementul',z[i],'are indexul',z.index(z[i])) 
    for i in range(len(z)):
        if abs(z[i])>9 and abs(z[i])<100:
            print('Elementul',z[i],'are indexul',z.index(z[i]))
    r=z
    r[0]=min(z)
    print('Lista cu primul element egal cu minimul listei:',r)
    a=z.index(min(z))
    b=z[0]
    z[a]=b
    print('Lista cu minimul listei egal cu primul element:',z)
    n=[]
    for i in range(len(z)):
        if z[i]%2==0:
            n.append(z[i])
    print('Lista elementelor pare:',n)
    n=[]
    for i in range(len(z)):
        if z[i]%3==0:
            n.append(z[i])
    print('Lista elementelor divizibile la 3:',n)
    a=1
    m=0
    mn=[]
    for i in range(len(z)):
        while a<z[i]:
            if z[i]%a==0:
                m+=1
                if m<5:
                    mn.append(z[i])
    print('Lista elementelor cu maxim 4 divizori:',mn)
else:
    print('Numar prea mare de elemente')