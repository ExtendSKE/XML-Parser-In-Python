import xml.etree.ElementTree as ET
import subprocess as SP

path = SP.getoutput('pwd') #Finding Path
tree = ET.parse('E4XSample.bpel')
root = tree.getroot()
tag_file = open('tags.txt','r')
tags=[]
list_found_tag =[]
dict= {}
for i in tag_file:
    i=i[:-1]
    if len(i) !=0:
        tags.append(i)
tag_file.close()
def finding_tags(root,tags):  #finding all tags which are present in source-code
    if root is None:
        return
    for i in root:
        #print(i.tag)
        for j in tags:
            j = j[1:]
            j= j [:-1]
            index = i.tag.find(j)
            #print(index)
            if index!=-1:
                try:
                    index = list_found_tag.index(j)
                except ValueError:
                    index = -1
                #print(index)
                if index == -1:
                    list_found_tag.append(j)
        finding_tags(i,tags)
    return

#for i in root:
    #print(i.tag)
finding_tags(root,tags)
#print(list_found_tag)
source_code_file = open('E4XSample.bpel','r') ##Reading SOurce-code Finding Starting & ending Line no. and column no.
#print(list_found_tag)
data = []
for i in source_code_file:
    data.append(i)
source_code_file.close()
line_no = 0
index1 = 0
tmp_index =0
for j in list_found_tag:
    tmp_list = []
    line_no =0
    #print(j)
    for i in data:
        i=i[:-1]
        #print(i)
        if len(i)!=0:
            line_no = line_no +1
            index = i.find(j)
            #print(index)
            if index!=-1:
                if i.find('/') ==-1:
                    if(i.find('>')==-1):
                        #print(j)
                        try :
                            index1 = data.index(i+"\n")
                            tmp_index = index1
                        except ValueError:
                            index1 =-1
                        flag =0
                        while index1!=len(data):
                            if data[index1].find('>')!=-1:
                                flag =1
                                break
                            else:
                                index1 = index1+1;
                        #print(index1)
                        if flag ==1:
                            tmp_list.append("begin_line:"+str(line_no)+" begin_column:"+str(index)+"   end_line:"+str(line_no+index1-tmp_index)+"  end_column:"+str(data[index1].find('>')))
                        else:
                            tmp_list.append("begin_line:"+str(line_no)+" begin_column:"+str(index))
                    else:
                        tmp_list.append("begin_line:"+str(line_no)+" begin_column:"+str(index))
                else:
                    if len(tmp_list)%2==0:
                        tmp_list("begin_line:"+str(line_no)+" begin_column:"+str(index)+"   end_line:"+str(line_no)+"  end_column:"+str(index))
                    else:
                        tmp_list.append("end_line:"+str(line_no)+"  end_column:"+str(index-1))

    dict[j]=tmp_list
dict_out=open('output.txt','w')     ##Writing dictionary in output file
dict_out.write("File_Path : "+path+"/ \n")  #path of file
for i in list_found_tag:
    dict_out.write(i+": "+str(dict[i])+"\n")
dict_out.close()
#print(dict)
