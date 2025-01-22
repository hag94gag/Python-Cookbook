from pathlib import Path
import re

pattern=re.compile(r"web",re.I)

#list all txt files in a path
folder=Path(r"C:\Users\DataCenter\Desktop\Python")

for f in folder.glob("*.txt"):
    with open (f,"r" ) as Nf:
        for line ,content in enumerate(Nf.readlines()):
        # content=Nf.read()
            result=re.search(pattern,content)
            if result:
                print(f"Searching in {f.name}")
                print(f"Match Found in line {line+1} as {result.group()}")

        
        
