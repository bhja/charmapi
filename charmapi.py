import json

import requests
import os
print("Running Charm api calls")
refresh_token = os.getenv('CHARM_API_REFRESH_TOKEN')
data = {'refreshtoken':f'{refresh_token}'}
r= requests.post(url="https://api.chartmetric.com/api/token",data=data)
response=r.json()


access_token=response['token']
print("Retrieved the token")
headers = {
    'Authorization' : f'Bearer {access_token}'
}

print("fetch the spotify_monthly_listeners")
r=requests.get(url=f"https://api.chartmetric.com/api/artist/sp_monthly_listeners/list?min=500&max=10000&offset=0&code2=US",headers=headers)
print(json.dumps(r.json(),indent=4))
print("End of the monthly listeners")
spotify_artist_id='0du5cEVh5yTK9QJze8zA0C'
print("******Proceed to fetch the details of the artist views for spotify by city ")
print("fetch the charm artist id for a spotify artist Bruno Mars", f'{spotify_artist_id}' )
r=requests.get(url=f"https://api.chartmetric.com/api/artist/spotify/{spotify_artist_id}/get-ids",headers=headers)
print(r.json())
print("Fetching the metrics by day for an artist")
r=requests.get(url="https://api.chartmetric.com/api/artist/2975/where-people-listen",headers=headers)
response = r.json()
print(json.dumps(response,indent=4))


