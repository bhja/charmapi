Assign the refresh token to the env variable CHARM_API_REFRESH_TOKEN and get started with running the tool. 
Rerun the script to see the refresh token works as expected. 3 endpoints have been added to this script to show the expected results

1. The endpoint given below lists the sp_monthly_listeners for all the artists . it also takes filters. Right now the script fetchs by country code US.
   (https://api.chartmetric.com/apidoc/#api-Artist-getArtistListByStats)
2. There is another endpoint which gives the details of the city the listeners belong to.
   (https://api.chartmetric.com/apidoc/#api-Artist-GetWherePeopleListenInsights)
   
<img width="1680" alt="Screenshot 2025-01-15 at 2 32 46 PM" src="https://github.com/user-attachments/assets/6bb49f72-ddf6-484a-bf4c-d1de8ece46f9" />
