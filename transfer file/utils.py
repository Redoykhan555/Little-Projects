import os,os.path,time,threading,time
from sortedcontainers import SortedDict

chunk = 4096


#WHAT HAPPENS WHEN A FILE IS DELETED WHILE TRANSFER IS RUNNING?

def ulta_dic(dic):
    """Given start value 20,find out which file ontains this byte.
    We have reversed the dictionary,with gradually added keys.
    Log(n) look-up of desired file should now be possible."""
    
    other = SortedDict()
    tot = 0
    for k,v in dic.items():
        tot+=v
        if tot not in dic:
            other[tot]=k
    return other

def search(path,base):
    cur = base+"/"+path
    ans=SortedDict()
    if os.path.isfile(cur):
        ans[path] = os.stat(base+"/"+path).st_size
        return ans
    li = os.listdir(cur)
    for f in li:
        ans.update(search(path+"/"+f,base))
    return ans


class OffsetManager:
    """Because we need to cache i.e maintain state for calc_offset function.
    Classes are there to bind function and data together,so here we go.

    This is for server. Client will have to overwrite check_key to populate
    cache by asking dict from server.

    We need a mechanism to ensure cache size doesn't grow out of it's limit."""

    def __init__(self):
        self.cache={}
        self.lock = threading.Lock()

    def check_key(self,path):
        if path not in self.cache:
            arr=path.split('/')
            print("Searching for: ",arr[-1]," ",'/'.join(arr[:-1]))
            temp = search(arr[-1],'/'.join(arr[:-1]))
            self.cache[path] = (temp,ulta_dic(temp))
            print("DIC size: ",len(temp))
        
    def calc_offset(self,path,i,chunk_sz):
        """Returns the file name and offset(as tuple) for a given chunk position.
        To facilitate concurrent execution,path and chunk_sz is also
        required.
        Otherwise,we'd have to maintain state for each connection.Which
        might be a headache once threads come to play."""
        i=int(i)
        chunk_sz=int(chunk_sz)
        if os.path.isfile(path):
            return (path,i*chunk_sz)

        self.lock.acquire()
        self.check_key(path) #Don't know if it is THREAD SAFE
        self.lock.release()
        
        dic,other = self.cache[path]

        chunk_start = int(i)*int(chunk_sz)
        owner_ind = other.bisect_right(chunk_start)
        owner_key = other.iloc[owner_ind]
        file = other[owner_key]

        file_start=0
        if owner_ind!=0:
            file_start = other.iloc[owner_ind-1]

        return (file,chunk_start-file_start)

    def next_file(self,path,file):
        dic,other=self.cache[path] #ASSUMING CACHE HAVE THAT 'PATH' AS KEY
        ind = dic.index(file)+1
        if ind==len(dic):
            return ""
        return dic.iloc[ind]

class ServerOffsetManager(OffsetManager):
    

    def get_dict(self,path):
        self.lock.acquire()
        self.check_key(path) #Don't know if it is THREAD SAFE
        self.lock.release()
        dic,other=self.cache[path]
        return dic
        

class ClientOffsetManager(OffsetManager):
    def check_key(self,path):
        if path not in self.cache:
            print("IT SHOULD BE PRESENT U DAMN STUPID")
            return self.cache[path] #To get the error
        
        
        





