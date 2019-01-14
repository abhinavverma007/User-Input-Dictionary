import json
from difflib import get_close_matches


data=json.load(open("data.json"))

def givemeaning(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        ans=input("Did you mean %s instead? Enter Y for Yes and N for No:" % get_close_matches(word,data.keys())[0])
        if ans=="Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif ans=="N":
             return "Word does not exist as per now."
        else:
            return "Please check your entry."
            
    
    else:
        return "Word does not exist as per now."
    

enter=input("Enter a word\n")
enter=enter.lower()
output=givemeaning(enter)

if type(output)==list:
    for item in output:
        print(item+"\n")
        
else:
    print(output)
