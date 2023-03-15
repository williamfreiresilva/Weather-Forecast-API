import requests

def get_news(country,api_key='83bac02b80354202bb771a814fa9ed67'):
  url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
  r = requests.get(url)
  content = r.json()
  articles = content['articles']
  results = []
  

  for article in articles:
    results.append(f"\nTITLE\n {article['title']} \n\nDESCRIPTION\n {article['description']} \n" + len(article['description'])*'_')
    '''
    for result in results:
      return result
    ''' 
  count = 0
  while count < (len(results) - 1):
    print(results[count])
    count = count + 1
    

print(get_news(country='us'))
