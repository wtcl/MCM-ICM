
with open("./dangerindex.txt",'r',encoding='utf-8') as f:
    lines=f.readlines()
    for line in lines:
        line=''.join(line.split(' ')[1:]).replace("-","-").replace("*","*")
        if line[:3]=='for':
            line=line[:3]+' '+line[3:]
        with open("./newdanger.txt","a",encoding='utf-8') as ff:
            ff.write(line)