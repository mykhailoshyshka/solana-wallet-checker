import requests

class SolanaWalletChecker:
    def __init__(self, rpc_url="https://api.mainnet-beta.solana.com"):
        self.rpc_url = rpc_url

    def get_wallet_activity(self, wallet_address):
        """
        Fetches the recent transaction history for a given Solana wallet address.
        
        :param wallet_address: Solana wallet address (str)
        :return: List of recent transactions or an error message
        """
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getSignaturesForAddress",
            "params": [wallet_address]
        }

        try:
            response = requests.post(self.rpc_url, json=payload)
            response.raise_for_status()
            data = response.json()

            if "result" in data:
                return data["result"]
            else:
                return f"Error: {data.get('error', {}).get('message', 'Unknown error')}"
        except requests.exceptions.RequestException as e:
            return f"Request failed: {e}"

    def is_wallet_active(self, wallet_address):
        """
        Checks if a wallet has recent activity.
        
        :param wallet_address: Solana wallet address (str)
        :return: Boolean indicating activity status
        """
        activity = self.get_wallet_activity(wallet_address)
        if isinstance(activity, list) and len(activity) > 0:
            return True
        return False

if __name__ == "__main__":
    # Replace with a Solana wallet address for testing
    wallet_address = input("Enter a Solana wallet address to check: ")

    checker = SolanaWalletChecker()
    activity_status = checker.is_wallet_active(wallet_address)

    if activity_status:
        print(f"The wallet {wallet_address} is active.")
    else:
        print(f"The wallet {wallet_address} has no recent activity.")
