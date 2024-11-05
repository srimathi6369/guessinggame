import streamlit as st
import random

st.title("Number Guessing Game")
st.write("Try to guess the number I'm thinking of between 1 and 100!")

# Generate a random number if it hasn't been set yet
if "target_number" not in st.session_state:
    st.session_state.target_number = random.randint(1, 100)

# Create an input for user to enter their guess
user_guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

# Check if the user guessed the number correctly
if st.button("Check Guess"):
    if user_guess < st.session_state.target_number:
        st.write("Too low! Try a higher number.")
    elif user_guess > st.session_state.target_number:
        st.write("Too high! Try a lower number.")
    else:
        st.write("Congratulations! You guessed the correct number!")
        # Reset the game
        st.session_state.target_number = random.randint(1, 100)
        st.write("Game reset. Try guessing the new number!")