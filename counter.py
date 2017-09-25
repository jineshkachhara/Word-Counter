"""
Created on Thu Jan 26 10:58:38 2017

@author: Jinesh
"""

#define a new function
def run(path):
    freq={} # new dictionary
	
    fin=open(path) # open a connection to the file ; open -> name, parameter, return value
    for line in fin: # read the file line by line 
        # lower() converts all the letters in the string to lower-case
        # strip() removes blank space from the start and end of the string
        # split(c) splits the string on the character c and returns a list of the pieces. For example, "A1B1C1D".split('1')" returns [A,B,C,D] 
        
        words=line.lower().strip().split(' ')
       
        # use for to go over all the words in the list 
        for word in words: # for each word in the line
            if word in freq: #if word is in dictionay 
                freq[word] = freq[word] + 1 # then increase its count by 1
            else:
                freq[word] = 1 #else just increase the count 1 as it is the 1st time occurance
    fin.close() #close the connection to the text file 
   
    return (max(freq, key = freq.get)) # return the value

# use the function 
print(run('textfile'))