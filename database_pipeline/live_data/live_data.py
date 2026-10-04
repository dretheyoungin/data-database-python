
import json

print("Bot: Initializing local cloud database simulator...")

# Simulated Live Internet Data Packet (Mock API Response)
mock_internet_packet = """
{
    "status": "success",
    "timestamp": "2026-10-03",
    "market_data": {
        "asset": "Bitcoin",
        "price_usd": "95420.50",
        "trend": "Bullish"
    }
}
"""

try:
    # Convert the raw internet string into a clean Python dictionary
    data = json.loads(mock_internet_packet)

    # Surgical data extraction
    asset_name = data["market_data"]["asset"]
    live_price = data["market_data"]["price_usd"]
    market_trend = data["market_data"]["trend"]
    time_fetched = data["timestamp"]

    print("\nBot: Success! Live network pipeline executed perfectly.")
    print(f"Tracking Asset: {asset_name}")
    print(f"Current Market Price: ${live_price} USD")
    print(f"Market Sentiment Trend: {market_trend}")
    print(f"Data Fetch Timestamp: {time_fetched}")

except Exception as e:
    print(f"Bot Error: Pipeline extraction failed. Details: {e}")