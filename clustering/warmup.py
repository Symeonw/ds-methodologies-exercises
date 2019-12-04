import json

with open('./bayes.json') as f:
    bayes = json.load(f)

print(bayes)

for x in list(bayes)[0:1]:
    print (f"{x},{bayes[x]} ")


for x in list(bayes)[4:5]:
    if bayes[x] == True:
        print ("Active = True")
    else:
        if bayes[x] == False:
            print ("Active = False")

for x in list(bayes)[3:4]:
    print (f"{len(bayes[x])}")


for x in list(bayes)[1:2]:
    print (f"{len(bayes[x])}")

import pandas as import pd

for x in list(bayes)[3:4]:
    df = pd.DataFrame(bayes[x])

    df