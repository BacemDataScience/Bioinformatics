import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as pies
#filename=sys.argv[1]

#fh=open("",'r')

#file=fh.read()
file="ACCTAAAACGGGTTTCGGGCCCC"
x=file
c=0
a=0
g=0
t=0

for x in file:
    if "C" in x:
        c+=1
    elif "G" in x:
        g+=1
    elif "A" in x:
        a+=1
    elif "T" in x:
        t+=1

print ("C=%d, G=%d, A=%d, T=%d" %(c,g,a,t))

gc_content=(g+c)*100/(a+t+g+c)

print ("gc_content= %2.2f" %(gc_content))

#Part 2 : Plot


# Plot Nucleotides frequencies
height = [a, c, g, t]
bars = ('A', 'C', 'G', 'T')
y_pos = np.arange(len(bars))

# Create bars and choose color
plt.bar(y_pos, height, color=(0.5, 0.1, 0.5, 0.6))

# Add title and axis names
plt.title('GC Content')
plt.xlabel('Nucleotides')
plt.ylabel('Frequencies')


# Create names
plt.xticks(y_pos, bars)

# Show graphic
plt.savefig('Nuc_freq.png')
plt.show()


#Part 3 : Pie GC %

labels = 'GC%','AT%'
sizes = [ gc_content, 100-gc_content]



pies.pie(sizes, labels=labels, autopct='%1.2f%%', shadow=True, startangle=140)
pies.title('GC Content')

pies.savefig('GC_content.png')
pies.show()
