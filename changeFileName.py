import os
files=os.listdir(os.getcwd())
for f in files:
    if f.startswith("10you") and len(f)>14:
        os.rename(f,f[14:])
        print(f," changed")

