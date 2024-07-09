import eel
import json

@eel.expose                 
def initloader():
    #delete previous loaded list
    #
    jsonr = json.load(open('Message_APP\Data.JSON',"r"))
    print(jsonr[0]["Name"])
    for i in range(len(jsonr)):
        eel.addelm(jsonr[i]["Name"],jsonr[i]["FamilyName"])
    pass




@eel.expose  
def Save(jsdict):
    jsonr = json.load(open('Message_APP\Data.JSON',"r"))
    jsonr.append(jsdict)
    jsonf = open('Message_APP\Data.JSON',"w")
    js= json.dumps(jsonr)
    jsonf.write(js)
    jsonf.close()
    initloader()



    pass



eel.init('Message_APP\web')
eel.start('index.html')

