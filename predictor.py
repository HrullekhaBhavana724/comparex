def predict_price(current_price):

    if current_price >= 80000:
        return {
            "prediction": current_price - 2000,
            "advice": "📉 Price may decrease soon. Waiting could save money."
        }

    elif current_price >= 50000:
        return {
            "prediction": current_price - 1000,
            "advice": "💰 Small price drop expected. Wait if possible."
        }

    else:
        return {
            "prediction": current_price + 500,
            "advice": "🔥 Price is already low. Buying now is recommended."
        }