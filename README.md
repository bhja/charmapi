Assign the refresh token to the env variable CHARM_API_REFRESH_TOKEN and get started with running the tool. 
Rerun the script to see the refresh token works as expected. 3 endpoints have been added to this script to show the expected results

1. The endpoint given below lists the sp_monthly_listeners for all the artists . it also takes filters. Right now the script fetchs by country code US.
   (https://api.chartmetric.com/apidoc/#api-Artist-getArtistListByStats)
2. There is another endpoint which gives the details of artist monthly listener by the city the listeners belong to .
   (https://api.chartmetric.com/apidoc/#api-Artist-GetWherePeopleListenInsights)

3. In this sample the artist Bruon Mar's spotify Id is passed to fetch charm_artist_id and then the count of listeners is retrieved by city
   
<img width="1680" alt="Screenshot 2025-01-15 at 2 32 46 PM" src="https://github.com/user-attachments/assets/6bb49f72-ddf6-484a-bf4c-d1de8ece46f9" />

NOTE : The refresh token does not change. So for any of the api calls. Use the refresh token and get the access token. If you are building an application , make sure you cache it and reuse the access token until is expires. 
Too many calls to get the access_token is not required when it can be reused. 
This script demonstrates the behavior of reuse. 
