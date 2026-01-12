from pyzuh import Agents

if __name__ == "__main__":
    # Initialize the Wazuh client
    wazuh_client = Agents(api_url='your-wazuh-api-url', jwt_token='your-wazuh-jwt-token')
