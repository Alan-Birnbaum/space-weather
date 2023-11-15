import pandas as pd

#df = pd.read_json('https://www.atmos.albany.edu/student/abirnbaum/integral-protons-plot-1-day.json')
df = pd.read_json('https://services.swpc.noaa.gov/json/goes/primary/integral-protons-plot-1-day.json')
df = df.tail(4)
string=[]
flux = df['flux'].to_list()
energy = df['energy'].to_list()
#flux[i] = str(round(flux[i], 3))
                
#for i in range(0, len(flux)):
#    string.append(flux[i] + energy[i])
    
with open("proton_flux.txt", mode="wt") as f:
    for i in range(0, len(flux)):
        protonSTR = f"{flux[i]:.3f} {energy[i]}"
        f.write(protonSTR)
        f.write("\n")