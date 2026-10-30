
import streamlit as st
from urllib.parse import quote

st.set_page_config(
    page_title="Ella's Kitchen Assistant",
    page_icon="🍲",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background-color: #fff0f5;
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
