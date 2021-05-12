import csv
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
with open('data.csv') as csvfile:
    csvrows = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csvrows:
        filename = row[0]
        url = str(row[4])
        print(url)
        result = requests.get(url, stream=True, headers=headers)
        print(result)
        if result.status_code == 200:
            image = result.content
            open(filename+'.png','wb').write(image)