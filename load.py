import sys
import urllib.request
import traceback
from datetime import datetime


# file = '/Users/walkerrowe/Downloads/03-24-2020.csv'

def main():
    
    file = sys.argv[1]

    print("processing file ", file)

    import postgresql
    db = postgresql.open('pq://walker:livres@walkercodetutorials.codes:5432/virus')

    ps=db.prepare("INSERT INTO coronavirusgeo( provincestate , countryregion,  lastupdate,  latitude, longitude,  confirmed,  deaths , recovered ) VALUES ($1, $2, $3, $4, $5, $6, $7, $8);")


    i = 0
    with open(file) as f:
         for x in f:
            if i == 0:
                i = i + 1
            else:
                l = x.split(",")
                provincestate =   l[2]
                if provincestate == "":  
                    countryregion =   l[3]  
                    try:
                        lastupdate =   datetime.strptime(l[4], '%Y-%m-%d %H:%M:%S')
                        latitude = l[5] 
                        longitude =  l[6] 
                        confirmed = l[7]
                        deaths = l[8]
                        recovered = l[9]
                        print(provincestate , countryregion,  lastupdate,  latitude, longitude,  confirmed,  deaths , recovered)
                        ps(provincestate , countryregion,  lastupdate,  latitude, longitude,  confirmed,  deaths , recovered) 
                        i = i + 1
                    except:
                       print(provincestate , countryregion,  lastupdate,  latitude, longitude,  confirmed,  deaths , recovered)
                       traceback.print_exc()

    print("done records added = ", i)
    
if __name__== "__main__":
  main()

