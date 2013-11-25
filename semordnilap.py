#!/usr/bin/env python 


import sys

####This function will reverse the give word and return the reversed word"
def rev_word(word):
    r_word = word[: :-1]
    return r_word



#### This function will do the following
# read a file
# save in a list called lst_word
# iterrate through each element of list lst_word
# then call the function rev_word
# rev_word is use for returning the reversed of given word
# then reversed word is check in lst_word
# if it is present then the reversed word is removef through lst_word
# so that it will not occur after because its pair is already found 
# pair is captured by yield  so that at last it can be use for  giving result 


def semordnilap(filename):

    try:
        f = open(filename)
	lst_word = f.read().split()

	for word in  lst_word:
	    r_word = rev_word(word)

	    if r_word in lst_word:
	        lst_word.remove(r_word)
	        yield word , r_word

	    else:
	        #yield word, "not paired"
                pass
	else:
	    yield " Now dictionary is over"
         

    except:        
	yield " this file is not in a valid file "
             
    finally:
        f.close()
        yield " file is closed"



if __name__ =="__main__":

    if len(sys.argv) < 2 or len(sys.argv) > 2:
	print " python semordnilap filename"
	print " file name according to u "
	sys.exit(-1)

    else:
        pair_word = semordnilap(sys.argv[1])
   
        for pair   in pair_word:
            print pair
        sys.exit(0)
	        
    

    




