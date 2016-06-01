import glob
import subprocess
import code
import csv
import os
if os.path.exists('output.csv'):
	os.remove("output.csv")
if os.path.exists("test.txt"):
	os.remove("test.txt")

l = glob.glob("./meshes/*.obj")

listOut = [['Name', 'Volume', 'SurfaceArea']]
for each in l:
    path_to_obj = each

    stringInput = "meshlabserver -i " + path_to_obj +  " -s ./geo.mlx > test.txt "

    subprocess.call(stringInput, shell=True)



    f = open('test.txt', 'r')
    x = f.readlines()
    vol = '----'
    surf = '----'
    for ii in x:
		if "Mesh Volume" in ii:
			vol = ii.split()[-1]
		if "Mesh Surface" in ii:
			surf = ii.split()[-1]
    
    
    rowOut = [each.split("\\")[-1], vol, surf]
    listOut.append(rowOut)


with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(listOut)
