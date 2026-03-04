from pyzuh import Agents,authenticate_wazuh
import os

if __name__ == "__main__":
    api_url = "https://x.x.x.x:55000"
    os.environ["WAZUH_USERNAME"] = "wazuh"
    os.environ["WAZUH_PASSWORD"] = "wazuh"

    try:
        # Authenticate with Wazuh API
        token = authenticate_wazuh(api_url)
        print("Authentication successful.")
    except Exception as e:
        print("Authentication failed:", e)

    # Initialize the Wazuh client
    wazuh_client = Agents(api_url=api_url, jwt_token=token, ssl_verify=False)

    status = wazuh_client.list_agents(offset=1)

    print("End")
