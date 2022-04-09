# youtube-search-wrapper
GO to google cloud console and create a new project        
IN the APIS sections go to library and add youtube data api v3      
After that go to credentials and generate an API key      
SET API_KEY variable in app.py to your api key     
Install requirements.txt and the run app.py      
Your search will be in the format --     
'your_hosting_ip/<max_results>/<search_query>'        
for example -      
'http://127.0.0.1:5000/10/best locations in the world/' -- IF i want to get 10 results and search for best locations in the world    

WHAT ITS GOING TO RETURN?    
- ITS GOING TO RETURN TITLE , DESCRIPTION , THUMBNAIL and VIDEO ID of the results    

FLAWS AND WARNINGS-    
you can only search for about 100 times a day due to youtube data api quota  
Playlists are not supported


