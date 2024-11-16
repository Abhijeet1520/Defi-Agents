from typing import Any, Dict
from .client import OneInchClient

client = OneInchClient()

def swap_tokens(from_token: str, to_token: str, amount: int, recipient: str, slippage: float = 100) -> Dict[str, Any]:
    """
    Swap tokens using OneInchClient.
    """
    try:
        result = client.swap_tokens(from_token, to_token, amount, recipient, slippage)
        return result if result else {}
    except Exception as e:
        print(f"Error in swap_tokens action: {e}")
        return {}

def get_quote(from_token: str, to_token: str, amount: int) -> Dict[str, Any]:
    """
    Fetch quote details from the OneInchClient.
    """
    try:
        params = {
            "from_token": from_token,
            "to_token": to_token,
            "amount": amount
        }
        quote = client.get_quote(params)
        return quote if quote else {}
    except Exception as e:
        print(f"Error in get_quote action: {e}")
        return {}

def fetch_active_orders() -> Dict[str, Any]:
    """
    Fetch active orders using OneInchClient.
    """
    try:
        orders = client.fetch_active_orders()
        return orders if orders else {}
    except Exception as e:
        print(f"Error in fetch_active_orders action: {e}")
        return {}