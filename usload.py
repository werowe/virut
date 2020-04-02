import sys
import urllib.request
import traceback
from datetime import datetime



def main():
    
    file = sys.argv[1]

    print("processing file ", file)

    import postgresql
    db = postgresql.open('pq://walker:livres@walkercodetutorials.codes:5432/virus')

    ps=db.prepare("INSERT INTO world( fips ,  admin2 , state,   country,   last_update,  lat,  long , confirmed , deaths , recovered , active ,   combined_key ) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12);")


    i = 0
    with open(file) as f:
         for x in f :
            if i == 0:
                i = i + 1
            else:

                l = x.split(",") 

                try:               
                    fips = l[0]  
                    admin2 = l[1]  
                    state = l[2]
                    country= l[3]   
                    last_update = datetime.strptime(l[4], '%Y-%m-%d %H:%M:%S')
                    lat = l[5] 
                    long = l[6]
                    confirmed = l[7] 
                    deaths = l[8] 
                    recovered = l[9]
                    active = l[10]
                    combined_key = l[11]
                    if state == 'South Carolina':
                        print(fips ,  admin2 , "state=",state,   country,   last_update,  lat,  long , confirmed , deaths , recovered , active ,   combined_key)
                    i = i + 1
                    ps(fips ,  admin2 , state,   country,   last_update,  lat,  long , confirmed , deaths , recovered , active ,   combined_key)
                except:
                    print(fips ,  admin2 , "state=",state,   country,   last_update,  lat,  long , confirmed , deaths , recovered , active ,   combined_key)
                    traceback.print_exc()

    print("done records added = ", i)
    
if __name__== "__main__":
  main()

