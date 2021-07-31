import os
filelist=os.listdir()
for filename in filelist:
    if filename[0]=="[" :
        filename_sp=filename.split(']',1)
        filename_sp=filename_sp[1].lstrip(" ")
        print(filename_sp)
        #以下リネーム
        os.rename(filename,filename_sp)
