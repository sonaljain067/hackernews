from requests.exceptions import ConnectionError, HTTPError
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException 
from time import strftime, localtime
from dotenv import load_dotenv 
import requests
import os 

load_dotenv()

app = FastAPI() 
origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins)
    

@app.get("/")
def hackerNewsAPI(): 
    try: 
        data = []

        # fetching top stories 
        url = os.environ["HACKERNEWS_API_URL"]
        topStoriesRes = requests.get(os.environ["TOPSTORIES_API_URL"]).json()

        # extracting top 10 from them 
        firstTenStories = topStoriesRes[0:10]
        
        # API calls for story details  
        for story in firstTenStories: 
            url = f'{os.environ["HACKERNEWS_API_URL"]}/item/{story}.json?print=pretty'
            storyData = requests.get(url).json() 
            time = strftime('%Y-%m-%d %I:%M:%S %p', localtime(storyData["time"]))
        
            extractedData = {
                "time": time, 
                "title": storyData["title"],
                "author": storyData["by"],
                "url": storyData.get("url", ""),
                "score": storyData["score"]
            }
            data.append(extractedData)
        return data 
    
    #server unreachable or down 
    except (HTTPError) as e:  #ConnectionError, 
        raise HTTPException(status_code=503, detail='Hackernews API might be down or unreachable.') 
        # raise HTTPError(status_code=503, detail='Hackernews API might be down or unreachable.') 
