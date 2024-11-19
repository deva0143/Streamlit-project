import streamlit as st

# Predefined list
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
game = st.number_input("press 1 for computer guessing or press 2 for user guessing",value=1)
if game==1:
    import streamlit as st
    import random

    # Predefined list of numbers
    a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Streamlit app
    def main():
        st.title("Computer Guessing Game")

        # Instructions for the user
        st.write("Please pick a number from the list below (but do not tell the computer):")
        st.write(a_list)

        # Create a form for user input
        number = st.number_input("Pick a number from the list:", min_value=1, max_value=10, step=1)

        if number != 0:
            # Game start button
            if st.button("Start Guessing Game"):
                # Initialize computer's guess variables
                low = 1
                high = 10
                attempts = 0
                correct = False

                # Start guessing loop
                while not correct:
                    attempts += 1
                    guess = random.randint(low, high)  # Computer randomly guesses a number between low and high
                    st.write(f"Computer guesses: {guess}")

                    # User feedback on the computer's guess
                    feedback = st.radio(
                        "Is the guess too high, too low, or correct?",
                        options=["Too low", "Too high", "Correct"]
                    )

                    if feedback == "Too low":
                        low = guess + 1  # Adjust the low bound
                    elif feedback == "Too high":
                        high = guess - 1  # Adjust the high bound
                    elif feedback == "Correct":
                        st.write(f"Yay! The computer guessed your number {guess} correctly in {attempts} attempts!")
                        correct = True
                        break  # Exit the loop if the guess is correct
                    else:
                        st.write("Please provide feedback.")
                        break

# Run the app
if __name__ == "__main__":
    main()

else:
    secret_number_index = 3  

    # Streamlit app
    def main():
        st.title("Guess the Secret Number Game")

        st.write("I have picked a secret number from this list:")
        st.write(a_list)

        # User input for guessing index
        guess_index = st.number_input("Enter your guess (index of the number):", min_value=0, max_value=len(a_list)-1, step=1)

        if st.button("Submit Guess"):
            # Check the user's guess
            if guess_index == secret_number_index:
                st.write(f"Congratulations! You've guessed the correct number: {a_list[guess_index]}!")
            else:
                st.write(f"Oops! The number at index {guess_index} is {a_list[guess_index]} and it's wrong. Try again!")

        # Option to restart the game
        if st.button("Restart Game"):
            st.write("Game has been reset. Try guessing again!")

# Run the app
if __name__ == "__main__":
    main()
