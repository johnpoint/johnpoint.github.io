import os

g = os.walk(".")

for path,dir_list,file_list in g:
    for file_name in file_list:
        if ".md" not in file_name:
            continue
        n=[]
        with open(file_name,"r+") as f:
            a=f.readlines()
            for i in range(0,len(a)):
                if i==1:
                    n.append("slug: "+file_name.replace(".md","")+"\n")
                n.append(a[i])
        os.remove(file_name)
        with open(file_name, "w") as ff:
            ff.writelines(n)