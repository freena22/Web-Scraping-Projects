import requests
from skimage import io

url = 'https://api.thecatapi.com/v1/images/search?limit=10&has_breeds=0&format=jsons' 
header = 'Content-Type: application/json' 
header = 'x-api-key: ****************************'

r = requests.get(url)
print(r.content)

for i in r.json():
     print(i)

# show the cat imges 

for i in r.json():
     print(i['url'])
     io.imshow(io.imread(i['url']))
     io.show()

