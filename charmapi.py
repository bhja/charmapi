import json
from datetime import date
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
#print(json.dumps(r.json(),indent=4))
with open('sp_listener_monthly_for_all_by_us.json', 'w', encoding='utf-8') as f:
    json.dump(r.json(), f, ensure_ascii=False, indent=4)
print("End of the monthly listeners")
spotify_artist_id='0du5cEVh5yTK9QJze8zA0C'
print("******Proceed to fetch the details of the artist views for spotify by city ")
print("fetch the charm artist id for a spotify artist Bruno Mars", f'{spotify_artist_id}' )
r=requests.get(url=f"https://api.chartmetric.com/api/artist/spotify/{spotify_artist_id}/get-ids?limit=1",headers=headers)
response=r.json()
print(json.dumps(response,indent=4))
print("Fetching the metrics by day for an artist")
charm_id=response["obj"][0]['cm_artist']
print(f'{charm_id}')
today=str(date.today())
r=requests.get(url=f"https://api.chartmetric.com/api/artist/{charm_id}/where-people-listen?since=2025-01-01&until={today}",headers=headers)
response = r.json()
with open('sp_listener_monthly_by_artist.json', 'w', encoding='utf-8') as f:
    json.dump(response, f, ensure_ascii=False, indent=4)

