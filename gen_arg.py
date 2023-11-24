n = [10,100,1000,10000]
m = ['rn', 'rr', 'ls', 'lt']
a = ['1','3','5','7']
r = ['f','r','s']
with open('arguments.txt', 'a') as file:
    for n_ in n:
        for m_ in m:
            for a_ in a:
                for r_ in r:
                    if (n_>1000)and(r_=='r'):
                        continue
                    file.write(str(n_)+' ')
                    file.write('-m '+m_+' ')
                    file.write('-a '+a_+' ')
                    file.write('-r '+r_+'\n')
                    