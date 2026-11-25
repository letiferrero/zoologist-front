import streamlit as st

"""
# Zoologist front
"""

st.markdown(
    """
Remember that there are several ways to output content into your web page...

Either like the title above by just creating a string (or an f-string) starting. Or like this paragraph using the `st.` function.
"""
)

# Collect the penguin characteristics required by the model
island = st.selectbox("Island", ["Biscoe", "Dream", "Torgersen"])

# Collect the penguin's measurements
bill_length_mm = st.number_input("Bill length (mm)", value=51.9)
bill_depth_mm = st.number_input("Bill depth (mm)", value=19.5)
flipper_length_mm = st.number_input("Flipper length (mm)", value=206.0)
body_mass_g = st.number_input("Body mass (g)", value=3950.0)

# Let the user select the penguin's sex
sex = st.selectbox("Sex", ["Male", "Female"])

"""
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Of course... The `requests` package 💡

What are the steps to follow in order to call an API ?

1. Which url will you use? Save it in a variable so you can easily change it later...

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
"""
