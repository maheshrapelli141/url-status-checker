import csv
import requests

with open('inputs/urls.csv', 'r') as file:
    reader = csv.reader(file)
    with open('outputs/result.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in reader:
            url = row[0]
            print('checking url: ',url)
            try:
                response = requests.get(url)
            except requests.exceptions.TooManyRedirects:
                writer.writerow([url,301])
            except requests.exceptions.ConnectionError:
                writer.writerow([url,404])
            except:
                writer.writerow([url,'unknown'])


                
