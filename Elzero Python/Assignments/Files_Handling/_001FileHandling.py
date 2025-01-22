import os
#os.mkdir(r"C:\Users\DataCenter\Desktop\Python")
#open(r"C:\Users\DataCenter\Desktop\Python\assign.py","x")
for i in range(1,50):
    if i==25:
        ElzeroFile=open(fr"C:\Users\DataCenter\Desktop\Python\special-text.txt","w")
        ElzeroFile.write(f"{os.getcwd()}")
        ElzeroFile.write(f"{os.path.dirname(r"C:\Users\DataCenter\Desktop\Python\special-text.txt")}\n")
        ElzeroFile.write(f"{ElzeroFile.name}\n")
        ElzeroFile.write(f"{i}")
        continue
    ElzeroFile=open(fr"C:\Users\DataCenter\Desktop\Python\{i}.txt","w")
    ElzeroFile.write(f" Elzero Web School => {i}")
    
    