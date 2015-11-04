#!/usr/bin/python3
import requests
import json
import google 
def get_google_results(query):
    print("query=%s"%query)
    results=google.search(query, num=3, stop=3)
    response=[]
    for result in results:
        print("\t site=%s"%result)
        response.append(result)
    return response
def get_candidates(filename):
    with open(filename,'r') as f:
        positions=json.loads(f.read())
    candidates=[]
    for position in positions:
        for candidate in position["candidates"]:
            candidates.append(candidate["name"])
    return candidates
if __name__ == '__main__':
    candidates=get_candidates('election2015.json')
    print("candidates retrieved")
    results=[]
    for candidate in candidates:
        query="%s monroe county"%candidate  
        sites=get_google_results(query)
        results.append({
            'name': candidate,
            'sites': sites,
        })
    with open('sites.json', 'w') as f:
        f.write(json.dumps(results))
        
