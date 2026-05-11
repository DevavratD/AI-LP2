def pizza_bot():
    # 1. KNOWLEDGE BASE: Prices and Info
    menu = {
        "pizza": "We have Margherita, Pepperoni, and Veggie pizzas.",
        "size": "Available sizes: Small ($8), Medium ($12), Large ($16).",
        "toppings": "Extra toppings: Cheese, Mushrooms, Olives, and Jalapenos.",
        "delivery": "Delivery takes 30-45 minutes depending on your location.",
        "offer": "Buy 1 Large pizza and get a Garlic Bread free!",
        "bye": "Enjoy your meal! Your order is being processed."
    }

    print("--- 🍕 Welcome to Pizza Hub Support ---")
    print("How can I help you? (Ask about: Menu, Size, Toppings, Delivery, or Offers)")

    while True:
        # 2. USER INPUT
        user_input = input("\nYou: ").lower().strip()

        # Exit Condition
        if "bye" in user_input or "order" in user_input:
            print("Bot:", menu["bye"])
            break

        # 3. RULE MATCHING (Inference Engine)
        found = False
        for keyword in menu:
            if keyword in user_input:
                print("Bot:", menu[keyword])
                found = True
                break
        
        # 4. FALLBACK
        if not found:
            print("Bot: I'm not sure about that. Would you like to see our 'menu' or check 'delivery' times?")

# Run the Chatbot
if __name__ == "__main__":
    pizza_bot()