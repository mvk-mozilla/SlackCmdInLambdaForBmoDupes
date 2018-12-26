import json
import os
from urllib import request #, urlopen
from urllib import parse
from urllib.parse import parse_qs

#https=require('https')
#qs=require('querystring')
ACCESS_TOKEN=os.environ['BOT_TOKEN']
BMO_URL="https://bugzilla.mozilla.org/rest/bug/possible_duplicates"

def lambda_handler(event, context):
    print("Hi CLoudWatch!")
    print ("I am a handler")
    #text = event.get('type', 'No event given')
#    tokenized = nltk.word_tokenize(text)
    # TODO implement
    
    
    if ('body' in event):
        eventBody= parse_qs(event.get('body'))
    else:
        eventBody=event
        for key in event.keys():
            print (key)
    #evntJson=json.dumps(parse.parse_qs(event))
    process (eventBody)
    '''return {
        'statusCode': 200,
        'body': json.dumps(event),#json.dumps('I got a body for u and it comes from an S3 ZIP!!!\n Plus I\'ve been testing. My event is '+json.dumps(event)), #err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        }
        #'body': json.dumps('Hello from Lambda!')
    }'''

def process (event):
    response_url=event.get('response_url')[0]
    channel= event.get('channel_id')[0]
    bmoText= event.get('text', ['sample'])[0].encode('utf8')
    print (response_url)
    reqParams=parse.urlencode({"summary": bmoText})
    bmo_req=BMO_URL+"?"+reqParams
    bmoJson=callBmo(bmo_req)
    
    bmoMsg=formatSlackMessage(bmoJson)
    
    message={ 
        'token': ACCESS_TOKEN,
        'channel':channel,
        'text': bmoMsg
        };
    #query= querystring.stringify(message);
    print ("Calling back with this:"+json.dumps(message));
    postJson=json.dumps(message).encode('utf8')
    
    #12-21  THIS WORKS FROM SLACK!!! Now to get the actual bmo dupes post
    req=request.Request(response_url, data=postJson,headers={'content-type': 'application/json'});
    resp=request.urlopen(req);
    print (resp);

def callBmo(bmoReq):
    print ("Calling BMO: "+bmoReq)
    bmoJson=json.load(request.urlopen(bmoReq))
    return bmoJson
    
def formatSlackMessage(bmoJson):
    #<li><a href="https://bugzilla.mozilla.org/bug/${dupe.id}" target="_blank">${dupe.id}</a> (${dupe.status}
    # ${dupe.resolution}) Version ${dupe.version}:  ${dupe.summary}</li>`
    bmoMsg=''
    for bmoDupe in bmoJson['bugs']:
        bmoMsg+="https://bugzilla.mozilla.org/bug/"+str(bmoDupe.get("id"))
        bmoMsg+=bmoDupe.get("summary")+"\n"
    
    return bmoMsg
    

if __name__ == "__main__":

    lambda_handler({'text':'event test'}, '')
