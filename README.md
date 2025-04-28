Steps to Get YouTube API Key:
1. Go to Google Cloud Console
Visit: https://console.cloud.google.com/

2. Create a New Project
Click on the project dropdown (top bar, near the Google Cloud logo).
Click "New Project".
Give your project a name (example: YoutubeAPIProject).
Click Create.

3. Enable YouTube Data API v3
Inside your project, go to APIs & Services → Library.
In the search bar, type YouTube Data API v3.
Click on it → Press Enable.

4. Create Credentials
Go to APIs & Services → Credentials (sidebar).
Click "+ Create Credentials" → API key.
It will immediately generate an API key.

5. (Optional) Restrict Your API Key (Recommended)
After creating the API key, click Restrict key.
Set:
Application restrictions: e.g., "None", "HTTP referrers" (if using in a website), or "IP addresses" (for backend).
API restrictions: Choose YouTube Data API v3.
This makes it more secure so no one else can steal your key.

#Now replace this API key in the code
