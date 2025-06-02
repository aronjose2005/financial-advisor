from financial_advisor import generate_financial_advice
from blockchain_transactions import record_transaction
from market_sentiment import fetch_market_news, analyze_market_sentiment

def main():
    # Fetch and analyze market sentiment
    news_text = fetch_market_news()
    print(f"Market News: {news_text}")
    sentiment_score = analyze_market_sentiment(news_text)
    print(f"Market Sentiment Score: {sentiment_score}")

    # Generate financial advice
    user_input = "Should I invest in tech stocks now?"
    advice = generate_financial_advice(user_input, sentiment_score)
    print(f"Financial Advice: {advice}")

    # Record transaction on blockchain
    transaction_data = f"User Query: {user_input}, Advice: {advice}"
    tx_hash = record_transaction(transaction_data)
    print(f"Transaction Recorded on Blockchain, Transaction Hash: {tx_hash}")

if __name__ == "__main__":
    main()
