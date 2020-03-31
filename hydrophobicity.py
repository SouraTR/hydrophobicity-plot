import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter1d

print("asd")

hyd = { 'A': 1.8,'R':-4.5,'N':-3.5,'D':-3.5,'C': 2.5,
       'Q':-3.5,'E':-3.5,'G':-0.4,'H':-3.2,'I': 4.5,
       'L': 3.8,'K':-3.9,'M': 1.9,'F': 2.8,'P':-1.6,
       'S':-0.8,'T':-0.7,'W':-0.9,'Y':-1.3,'V': 4.2 }


my_prot = str(input("Protein sequence: "))

hydlist = []
resnum = []

for i in range(len(my_prot)):
    hydlist.append(hyd[my_prot[i]])
    resnum.append(i+1)

print(hydlist, resnum)

plt.xlabel("Residue Number")
plt.ylabel("Hydrophobicity")

ysmoothed = gaussian_filter1d(hydlist, sigma=2)
plt.plot(resnum, ysmoothed)

plt.grid(True)
plt.show()

