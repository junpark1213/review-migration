import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env.local')

API_KEY = os.getenv("API_KEY")
ENV = os.getenv("ENV")
API_VERSION = "20250419"
BASE_URL = "https://api.yextapis.com/v2/accounts/me"

DESTINATION_ENTITY_ID = "1336245976-2f68451e33062b97be8e12b9fba4a4ff0452cca3"

REVIEW_IDS_TO_MOVE = [
    1536067367, 1536067366, 1536067368, 1536067363, 1536067364, 1536067369,
    1536067365, 1529616050, 1529616051, 1529616053, 1529616049, 1529616052,
    1520685482, 1520685485, 1520685483, 1520685476, 1520685481, 1520685478,
    1520685480, 1520685477, 1520685484, 1520685479
]

def move_review_to_new_entity(review_id, new_entity_id):
    """
    Moves a single review by updating its locationId.
    """
    print(f"  -> Moving review ID {review_id} to entity {new_entity_id}...")
    
    update_url = f"{BASE_URL}/reviews/{review_id}"
    
    params = {
        "api_key": API_KEY,
        "v": API_VERSION
    }
    
    payload = {
        "locationId": new_entity_id
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    if (ENV == "PROD"):
        try:
            response = requests.put(update_url, params=params, data=json.dumps(payload), headers=headers)
            response.raise_for_status()
            
            print(f"  -> Successfully moved review ID {review_id}.")
            return True

        except requests.exceptions.RequestException as e:
            print(f"  -> FAILED to move review ID {review_id}. Error: {e}")
            if 'response' in locals() and response.text:
                print(f"     API Response: {response.text}")
            return False
    elif (ENV == "DEV"):
        print(f"Would have ran this url {update_url}")
        print(f"With these params {params}")
        print(f"Body: {payload}")
        print(f"headers: {headers}")
        print("---"*50)
        return True
    else:
        print("UNKNOWN ENV")
        sys.exit(1)
    


def main():
    """
    Main function to execute the review migration process.
    """
    if not API_KEY:
        print("Error: API_KEY not found in .env.local file.")
        print("Please create a .env.local file and add the line: API_KEY='your_key_here'")
        return

    print("--- Starting Yext Review Migration Script ---")
    
    print("\n" + "="*50)
    print(f"Preparing to move {len(REVIEW_IDS_TO_MOVE)} reviews from the predefined list.")
    print(f"These reviews will be moved to destination entity: {DESTINATION_ENTITY_ID}")
    print("="*50 + "\n")
    
    proceed = input("Do you want to proceed with the migration? (yes/no): ").lower()
    
    if proceed != 'yes':
        print("Migration cancelled by user.")
        return

    print("\n--- Beginning Migration Process ---")
    success_count = 0
    failure_count = 0

    success_list = []
    failure_list = []

    

    for review_id in REVIEW_IDS_TO_MOVE:
        if move_review_to_new_entity(review_id, DESTINATION_ENTITY_ID):
            success_count += 1
            success_list.append(review_id)
        else:
            failure_count += 1
            failure_list.append(review_id)

            

    print("\n--- Migration Complete ---")
    print(f"Successfully moved: {success_count} reviews.")
    print(f"Failed to move: {failure_count} reviews.")
    print("--------------------------")

if __name__ == "__main__":
    main()