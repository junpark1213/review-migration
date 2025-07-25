# Reviews Migration Script

Uses the reviews Management API to transfer reviews from one entity to the other.
By using the Update (PUT) endpoint: https://hitchhikers.yext.com/docs/managementapis/reviews/reviewmanagement#operation/updateReview
we are able to update the locationId associated with the review to a desired locationId.

## Installation / How to run

1. Install python dependencies

```
python3 -m pip install requests python-dotenv
```

2. Create .env.local file and add these variables

```
API_KEY="<YOUR API KEY HERE>"
ENV="<DEV or PROD>"
```

- Run in PROD to make actual requests to the API, DEV will only print what requests would have ran

3. Run python script

```
python3 script.py
```

4. Confirmation input required for security in command line

## Monitor

You'll be able to see which reviews failed and ran successfully in the terminal output.
A count of reviews and list of successful vs failed will be shown at the end when running in PROD
