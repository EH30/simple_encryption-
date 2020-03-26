#Created By: EH

class ecrypt:
    def encrypt(self, msg, key):
        msglist = list(msg)
        keylist = list(key)
        chrs_list = []
        output_list = []
        strs = ""
        
        for x in keylist:
            chrs_list.append(chr((ord(x)//15)))
        
        
        count = 0
        for i in msglist:
            if count >= len(chrs_list):
                count = 0
            
            output_list.append(chr(ord(i)+ ord(chrs_list[count])))
            count += 1
        
        
        for e in output_list:
            strs += e
        
        return strs
    
    
    def decrypt(self, msg, key):
        msglist = list(msg)
        keylist = list(key)
        chrs_list = []
        output_list = []
        strs = ""
        
        for x in keylist:
            chrs_list.append(chr((ord(x)//15)))
            
        
        count = 0
        for i in msglist:
            if count >= len(chrs_list):
                count = 0
            
            output_list.append(chr(ord(i)-ord(chrs_list[count])))
            count += 1
        
        
        for e in output_list:
            strs += e
        
        
        return strs