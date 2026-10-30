
import streamlit as st
from urllib.parse import quote

st.set_page_config(
    page_title="Ella's Kitchen Assistant",
    page_icon="🍲",
    layout="wide"
)


st.markdown("""
<style>
.stApp {
    background: #fff0f5 !important;
}

[data-testid="stAppViewContainer"] {
    background: #fff0f5 !important;
}

[data-testid="stMain"] {
    width: 100% !important;
}

.block-container {
    width: 100% !important;
    max-width: 100% !important;
    padding: 1rem !important;
    margin: 0 auto !important;
}

h1, h2, h3 {
    color: #c2185b !important;
}

.stButton button {
    background-color: #e75480;
    color: white;
    border-radius: 12px;
    width: 100%;
}

    width: 100%;
    max-width: 100%;
    padding: 1rem;
}

h1, h2, h3 {
    color: #c2185b;
}

.stButton button {
    background-color: #e75480;
    color: white;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

PHONE = "2349067662537"

menu = {
    "Jollof rice + chicken": 3000,
    "Fried rice + chicken": 3000,
    "Stew rice + beef or chicken": 3000,
    "Ogbono soup + eba": 2500,
    "Okra soup": 2500,
    "Egusi soup + 2 wraps of eba": 2500,
    "Small chin chin": 500,
    "Big chin chin": 1000,
    "Meat pie": 1000,
    "Chicken pie": 1500,
    "Small chops": 1000,
    "Brownies": 5000,
    "Bottle water": 300,
    "5 Alive": 1500,
    "Hollandia": 3000
}

st.title("💕 Ella's Kitchen")
st.subheader("Welcome to Ella's Kitchen Assistant!")
st.write("Delicious meals, made with love.")

st.divider()

st.header("🍲 Our Menu")

for food, price in menu.items():
    st.write(f"**{food}** — ₦{price:,}")

st.divider()

st.header("🛒 Place Your Order")

food = st.selectbox(
    "Choose your food",
    list(menu.keys())
)

quantity = st.number_input(
    "How many portions?",
    min_value=1,
    max_value=100,
    value=1
)

total = menu[food] * quantity

st.metric("Your total", f"₦{total:,}")

st.divider()

st.header("Your Details")

name = st.text_input("Your name")
address = st.text_input("Delivery address or pickup")

if st.button("Order through WhatsApp"):
    if name.strip() and address.strip():
        message = (
            f"Hello Ella's Kitchen! My name is {name}.\n"
            f"Order: {food}\n"
            f"Quantity: {quantity}\n"
            f"Total: ₦{total:,}\n"
            f"Delivery/Pickup: {address}\n"
            "Please confirm my order."
        )

        link = (
            f"https://wa.me/{PHONE}?text={quote(message)}"
        )

        st.success("Your order summary is ready!")
        st.link_button("Send order on WhatsApp", link)
    else:
        st.warning("Please enter your name and delivery details.")

st.caption("Thank you for choosing Ella's Kitchen ❤️")
st.divider()

st.divider()

st.header("🤖 Ella's Kitchen Chat")

st.write("Hi! Welcome to Ella's Kitchen. Ask me anything about our food!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input("Ask about our menu or prices...")

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    q = question.lower()
    reply = "Sorry, I don't know that yet. Please ask about our menu or prices."

    if "jollof" in q:
        reply = "Jollof rice with chicken costs ₦3,000."

    elif "fried rice" in q:
        reply = "Fried rice with chicken costs ₦3,000."

    elif "meat pie" in q:
        reply = "Yes! Meat pie costs ₦1,000."

    elif "chin chin" in q:
        reply = "Small chin chin is ₦500 and big chin chin is ₦1,000."

    elif "cheapest" in q:
        reply = "Our cheapest item is small chin chin at ₦500."

    elif "menu" in q or "price" in q:
        reply = "Here is our menu:\n" + "\n".join(
            f"{item}: ₦{price:,}"
            for item, price in menu.items()
        )

    elif "soup" in q:
        reply = "We offer Ogbono, Okra and Egusi soup. Each listed option costs ₦2,500."

    elif "hello" in q or "hi" in q:
        reply = "Hello! Welcome to Ella's Kitchen. What delicious meal can I help you find?"

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

    st.rerun()

st.write("Ask me about our menu, prices or ordering!")

question = st.text_input(
    "What would you like to know?"
)

if st.button("Ask Assistant"):
    q = question.lower().strip()

    if "cheapest" in q:
        cheapest = min(menu.values())
        items = [
            item for item, price in menu.items()
            if price == cheapest
        ]
        st.info(
            f"Our cheapest items are {', '.join(items)} "
            f"at ₦{cheapest:,}."
        )

    elif "with" in q and "₦" in q:
        import re
        amount = re.search(r"₦\s*([\d,]+)", q)

        if amount:
            budget = int(amount.group(1).replace(",", ""))
            affordable = [
                (item, price)
                for item, price in menu.items()
                if price <= budget
            ]

            if affordable:
                st.write("These items fit your budget:")
                for item, price in affordable:
                    st.write(f"{item}: ₦{price:,}")
            else:
                st.warning("No menu item fits that budget yet.")

    elif "jollof" in q:
        import re
        numbers = re.findall(r"\d+", q)
        quantity = int(numbers[0]) if numbers else 1
        total = 3000 * quantity

        st.success(
            f"{quantity} plate(s) of jollof rice "
            f"with chicken cost ₦{total:,}."
        )

    elif "meat pie" in q:
        st.info("Yes! Meat pie costs ₦1,000.")

    elif "fried rice" in q:
        st.info("Fried rice with chicken costs ₦3,000.")

    elif "menu" in q or "price" in q:
        for item, price in menu.items():
            st.write(f"{item}: ₦{price:,}")

    else:
        st.info(
            "I can help with our menu, prices, "
            "budgets and food orders. Ask me anything!"
        )
        st.warning(
            "Sorry, I don't know that yet. "
            "Please contact us on WhatsApp for help."
)
