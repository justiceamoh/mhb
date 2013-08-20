from string import rstrip

new_mhb = open('../mhb_list.txt','a')  ## remember to change to 'a'
old = open('../list.txt')
lines = old.readlines()
mhb = []
for line in lines:
    num = raw_input(line,)
    if len(num) == 1:
        s = '   '
    elif len(num) == 2:
        s = '  '
    elif len(num) == 3:
        s = ' '
    else:
        print 'number error'
        break
    mhb.append(num+s+line)


for i in mhb:
    new_mhb.write(i)

new_mhb.flush()
new_mhb.close()
old.flush()
old.close()
