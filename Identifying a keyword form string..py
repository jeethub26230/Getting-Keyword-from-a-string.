# Identifying a Key word from a string
import time
# kwlist is a function present in Keyword module which consists all the keywords.

from keyword import kwlist

st=input("Enter your string : ")
print("Loading...")
time.sleep(5)

if st in kwlist:
    print("The word " +st,"is a Keyword")
else:
    print("The word " +st, "is not a keyword")
