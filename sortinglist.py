def hi(name):
    print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You', ]
sorted_girls = []
for name in girls:
    hi(name)
    if (len(sorted_girls)==0) :
        sorted_girls.append(name)
    else :

        for nextname in sorted_girls:
            hi(nextname)
            
    print('Next girl')
sortednames = []
