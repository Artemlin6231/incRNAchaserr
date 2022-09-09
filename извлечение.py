f=open("sites.txt",'r')
new_f=open("sites_sorted.txt","w+")
for line in f:
    line1=line.split()
    if line1[0] != "#":
        new_f.write(line)
new_f.close()
f.close()