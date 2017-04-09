def find_obj(i,s):
    """There are 4 types of data supported: INT, BYTE STRING, LIST and
    DICTIONARY(map in java).

    Two are primitive type,INT and BYTE STRING.
    In other two composite types: We recursively add elements of both
    primitive and composite types."""

    if s[i]=='i': #THIS HANDLES INTEGER OBJECTS
        obj=""
        i+=1
        while s[i]!='e':
            obj+=s[i]
            i+=1
        return (int(obj),i+1)
    
    elif s[i]=='l':
        arr = []
        i+=1
        while s[i]!='e':
           obj,i = find_obj(i,s)
           arr.append(obj)
        return (arr,i+1)

    elif s[i]=='d': #HANDLES THE DICTIONARY
        dic = {}
        i+=1
        while s[i]!='e':
            key,i = find_obj(i,s)
            value,i = find_obj(i,s)
            dic[key] = value
        return (dic,i+1)

    else :
        #THIS MUST BE A BYTE STREAM
        obj = ""
        while s[i]!=':':
            obj+=s[i]
            i+1
        length = int(obj) #Length of byte stream
        i+=1
        #This is byte stream,NOT ASCII.
        
        byte = s[i:i+length]
        return (byte,i+1)
    
def parse_torrent(string):
    root = find_obj(0,string)
    return root
