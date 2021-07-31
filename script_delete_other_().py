import os
import re
filelist=os.listdir()
for filename in filelist:
    match = re.search(r' \((.+)\)',filename)
    if match:
        filename_new=re.sub(r' \((.+)\)',"",filename)
        print(filename_new)
        #以下リネーム
        os.rename(filename,filename_new)
