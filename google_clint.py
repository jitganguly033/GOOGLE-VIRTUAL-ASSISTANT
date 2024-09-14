import http.client
import json
import time

def fetch_api_data(max_retries=3, retry_delay=2):
    """
    Fetches data from the specified API endpoint with retry capability.

    Parameters:
    max_retries (int): Maximum number of retries for the request.
    retry_delay (int): Delay in seconds between retries.
    """
    conn = http.client.HTTPSConnection("rumad-botdelive-v1.p.rapidapi.com")
    
    headers = {
        'x-rapidapi-key': "b68e757cfcmshbea8e5b013bf7f5p1555bejsne52d8c7bd922",
        'x-rapidapi-host': "rumad-botdelive-v1.p.rapidapi.com"
    }
    
    for attempt in range(max_retries):
        try:
            # Send the request
            conn.request("GET", "/verifyAC", headers=headers)
            res = conn.getresponse()
            
            # Check response status
            if res.status == 200:
                data = res.read()
                response_json = json.loads(data.decode("utf-8"))
                print(json.dumps(response_json, indent=4))
                break  # Exit loop if request is successful
            else:
                print(f"Request failed with status code {res.status}: {res.reason}")
                if attempt < max_retries - 1:
                    print(f"Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)  # Wait before retrying
        
        except http.client.HTTPException as e:
            print(f"HTTP error occurred: {e}")
            if attempt < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)  # Wait before retrying
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break  # Exit loop if an unexpected error occurs
        finally:
            conn.close()

# Call the function
fetch_api_data()
