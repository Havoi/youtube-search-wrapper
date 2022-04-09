import requests
import json
from flask import Flask,jsonify
app = Flask(__name__)
API_ROUTE  = 'https://youtube.googleapis.com/youtube/v3/search'
API_KEY = 'your google console api key here'

@app.route('/<results>/<query>/<API_KEY>')
def main(query,results,key):
    
        
    
        
    response = req(query,results,key)
    
    titles = []
    ids = []
    imgs = []
    descriptions = []
    for x in response['items']:
        
        titles.append(x['snippet']['title']) 
        descriptions.append(x['snippet']['description']) 
        try:  
            ids.append(x['id']['videoId'])
        except:
            ids.append("playlist:"+x['id']['playlistId'])
        imgs.append(x['snippet']['thumbnails']['high']['url'])
    # print(titles,ids,imgs)
    data = []
    for x in range(0,len(titles)):
        temp = []
        temp.append(titles[x])
        temp.append(descriptions[x])
        temp.append(ids[x])
        temp.append(imgs[x])
        data.append(temp)

    return jsonify(data)
    
        
def req(query , max_results,key):
    response = requests.get(f'{API_ROUTE}?part=snippet&q={query}&maxResults={max_results}&key={key}')
    response = response.text
    
    response = json.loads(response)
    
    print(response)
    return response
    

if __name__ == "__main__":
    
    app.run()
   