import requests
import concurrent.futures
import time

# Function to get the current Unix timestamp in milliseconds
def current_unix_timestamp():
    return int(time.time() * 1000)

# Function to perform a single POST request
def make_post_request():
    # Get the current Unix timestamp
    view_completed_at = current_unix_timestamp()

    # Perform the final POST request
    post_url = "https://clownfish-app-f7unk.ondigitalocean.app/v2/tasks/claimAdsgramAdReward"
    post_data = {
        "viewCompletedAt": view_completed_at,
        "reference": 81
    }
    post_headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/json; charset=utf-8",
        "Origin": "https://miniapp.yesco.in",
        "Referer": "https://miniapp.yesco.in/",
        "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126", "Microsoft Edge WebView2";v="126"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",
        "Launch-Params": 'query_id=AAFphVRPAAAAAGmFVE97BXaa&user=%7B%22id%22%3A1330939241%2C%22first_name%22%3A%22Zero%22%2C%22last_name%22%3A%22%22%2C%22username%22%3A%22Daffa4040%22%2C%22language_code%22%3A%22en%22%2C%22allows_write_to_pm%22%3Atrue%7D&auth_date=1720062631&hash=c3a90a643af6b811a0917f71a9df5ea2f33a85fcd5cd715340f41659fb180389'
    }

    post_response = requests.post(post_url, headers=post_headers, json=post_data)

    if post_response.status_code == 200:
        print("POST request successful.")
    else:
        print(f"POST request failed. Status code: {post_response.status_code}")

    # Print the response content
    print(f"Response content: {post_response.text}")

    # Log the Unix timestamp at the end
    print(f"Unix timestamp at the end: {view_completed_at}")

# Number of concurrent requests to make
num_requests = 100000

while True:
    # Use ThreadPoolExecutor to run requests concurrently
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks
        futures = [executor.submit(make_post_request) for _ in range(num_requests)]

        # Wait for all tasks to complete
        for future in concurrent.futures.as_completed(futures):
            # Handle exceptions if any
            try:
                result = future.result()
            except Exception as e:
                print(f"Exception occurred: {e}")

    print("All requests completed. Waiting before starting again...")
    time.sleep(1)  # Wait for 60 seconds before starting again
