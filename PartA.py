import re
import time
import sys
#open files and put split by space and remove usual symbols and lowercase each word and put into each list. and then use set() to find common words
#and return the size of set

# time complexity O(n+m)
def tokenize(file1, file2):
    symbols = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~•"""
    with open (file1) as f1:
        if f1.closed:
            print(f"The file {file1} is closed.")
  
            

        s1 = f1.read().replace('\n',' ')
        s1 = re.sub(r'[{}]'.format(symbols),'',s1)

        list1 = s1.lower().split()
    with open (file2) as f2:
        if f2.closed:
            print(f"The file {file2} is closed.")
 
            
        s2 = f2.read().replace('\n',' ')
        s2 = re.sub(r'[{}]'.format(symbols),'',s2)
        list2 = s2.lower().split()
    com = set(list1) & set(list2)
    return len(com)


start_time = time.time()
file1 = sys.argv[1]
file2 = sys.argv[2]
print (tokenize(file1,file2))
print("Process finished --- %s seconds ---" % (time.time() - start_time))