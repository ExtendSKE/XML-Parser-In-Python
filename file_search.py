import os
import subprocess as sp
import fnmatch
output = []
def directory_search(path,extension):
    dirs = os.listdir(path)
    #print(dirs)
    if len(dirs)==0:
        return
    for file in dirs:
        index=file.find('~')
        if index ==-1:
            dec = os.path.isfile(path+"/"+file)
            #print(dec)
            if dec is True:
                if fnmatch.fnmatch(file,extension):
                    tmp = []
                    tmp.append(path+"/"+file)
                    tmp.append(file)
                    output.append(tmp)
                    #print(file)
            else:
                #print(file)
                directory_search(path+"/"+file,extension)
    return output
if __name__ == "__main__":
    path=sp.getoutput('pwd')
    extension ="*.bpel"
    print(directory_search(path,extension))
    '''
    Multiple Line Comment
    for i in output:
        for j in i:
            print(j," ")
        print()
    '''
