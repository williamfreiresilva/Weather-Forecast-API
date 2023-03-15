import requests

# create a function that receives a coutry's acronym, not case sensitive, and your API key.
# API key should be insertid in the function as default
# get your API key at: https://newsapi.org
def get_news(country,api_key='<yout API key from: https://newsapi.org'):
  url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
  r = requests.get(url)
  content = r.json()
  articles = content['articles']
  results = []
  
  # loop through each article and append them to results[]
  for article in articles:
    results.append(f"\nTITLE\n {article['title']} \n\nDESCRIPTION\n {article['description']} \n" + len(article['description'])*'_')

  # if you return results, you won't get your escape characters to work
  # while loop to print each result individualy to make use of escape characters for aesthetics
  count = 0
  while count < (len(results) - 1):
    print(results[count])
    count = count + 1
    
# summon function for USA headlines
print(get_news(country='us'))
