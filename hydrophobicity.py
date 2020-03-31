import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter1d



hyd = { 'A': 1.8,'R':-4.5,'N':-3.5,'D':-3.5,'C': 2.5,
       'Q':-3.5,'E':-3.5,'G':-0.4,'H':-3.2,'I': 4.5,
       'L': 3.8,'K':-3.9,'M': 1.9,'F': 2.8,'P':-1.6,
       'S':-0.8,'T':-0.7,'W':-0.9,'Y':-1.3,'V': 4.2 }

red_dict = {
    "L": "L",
    "V": "L",
    "I": "L",
    "M": "L",
    "C": "C",
    "A": "A",
    "G": "G",
    "S": "S",
    "T": "T",
    "P": "P",
    "F": "F",
    "Y": "F",
    "W": "W",
    "E": "E",
    "D": "D",
    "N": "N",
    "Q": "Q",
    "K": "K",
    "R": "K",
    "H": "H",
}
      

my_prot = str(input("Protein sequence: "))
red_prot = ""

for j in range(len(my_prot)):
    red_prot = red_prot + red_dict[my_prot[j]]

hydlist = []
resnum = []
for i in range(len(red_prot)):
    
    hydlist.append(hyd[red_prot[i]])
    resnum.append(i+1)
    
    
print(hydlist)
print(resnum)

plt.xlabel("Residue Number")
plt.ylabel("Hydrophobicity")
#ysmoothed = gaussian_filter1d(hydlist, sigma=1)
#plt.plot(resnum, ysmoothed)
ysmoothed2 = gaussian_filter1d(hydlist, sigma=2)
plt.plot(resnum, ysmoothed2)
#ysmoothed3 = gaussian_filter1d(hydlist, sigma=3)
#plt.plot(resnum, ysmoothed3)

plt.grid(True)
plt.show()

