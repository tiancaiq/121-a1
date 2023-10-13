import re 
import time
import sys

#open files and put split by space and remove usual symbols and lowercase each word and put into a list
#time-complexity O(m+n)
def tokenize(files):
    symbols = r"""!"#”“$%&'()*+,-./:;<=>?@[\]^_`{|}~™•"""
    with open (files) as file:
        if file.closed:
            print(f"The file {files} is closed.")
            

        s1 = file.read().replace('\n',' ')
        s1 = re.sub(r'[{}]'.format(symbols),'',s1)

        tokens = s1.lower().split()
   
    
    return tokens
# compute Word Frequencies by create a empty dict and itriate each word in list and the new word and num of word into dict. old words skip
# and increase num
# time complexity O(n^2)
def computeWordFrequencies(lists):
    freq = {}
  
    for word in lists:
        if word in freq : freq[word] = freq[word] +1
        else: freq[word] = 1
        
    return freq

#sort by number of word amount and then order and print 
# time complexity O(nlogn)
def prints(freq):
    sort = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
    for key, value in sort.items():
        print(f"{key}-{value}")
   
    

    

    
file = sys.argv[1]

start_time = time.time()
prints(computeWordFrequencies(tokenize(file)))
print("Process finished --- %s seconds ---" % (time.time() - start_time))
