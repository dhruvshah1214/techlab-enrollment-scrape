# techlab-enrollment-scrape

## Setup
1. Create a new project in Google Cloud Console
2. Enable the Google Sheets API
3. Create a "SERVICE KEY" credential with Project Owner access.
4. Download the service key file and rename it to 'auth.json'. Move it to the same directory as the scrape.py script.
5. Go back to Google Cloud Console, select your project, click APIs & Services > Credentials.
   Click "Manage service accounts" on the right-hand side.
   Copy the "Service account ID" matching to the service account key you downloaded. This ID should look like an email.
6. Share all sheets with this service account ID email that you want the script to be able to access.
7. Edit the script with correct URLs for sheets.
8. Run script.
