f=open("sites_sorted2.txt",'r')
f1=open("sites_sorted3.txt",'r')
f2=open("sites_sorted4.txt",'r')
f3=open("sites_sorted.txt",'r')
new_f=open("sites_all.txt","w+")
for line in f3:
    new_f.write(line)
for line in f:
    #line1=line.split()
    #if line1[0] != "#":
    new_f.write(line)
for line in f1:
    #line1 = line.split()
    new_f.write(line)
for line in f2:
    #line1 = line.split()
    new_f.write(line)

new_f.close()
f.close()
f1.close()
f2.close()