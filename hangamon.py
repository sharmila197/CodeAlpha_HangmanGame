import streamlit as st
import random
import string

# Page configuration
st.set_page_config(
    page_title="Hangman Game",
    page_icon="🎮",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
.stApp {
    background-color: #111827;
    color: white;
}
h1 {
    text-align: center;
    color: #38bdf8;
}
.word {
    font-size: 35px;
    text-align: center;
    letter-spacing: 12px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Game words
WORDS = ["python", "coding", "school", "apple", "tiger"]

# Initialize game
def new_game():
    st.session_state.word = random.choice(WORDS)
    st.session_state.guessed = []
    st.session_state.game_over = False
    st.session_state.won = False

if "word" not in st.session_state:
    new_game()

# Game calculations
word = st.session_state.word
guessed = st.session_state.guessed

wrong_guesses = sum(
    1 for letter in guessed
    if letter not in word
)

remaining = 6 - wrong_guesses

# Check win or loss
if all(letter in guessed for letter in word):
    st.session_state.game_over = True
    st.session_state.won = True

if wrong_guesses >= 6:
    st.session_state.game_over = True
    st.session_state.won = False

# Heading
st.title("🎮 HANGMAN GAME")
st.markdown(
    "<p style='text-align:center;'>"
    "Guess the hidden word before you run out of lives!"
    "</p>",
    unsafe_allow_html=True
)

st.divider()

# Game status
col1, col2 = st.columns(2)

with col1:
    st.metric("❤️ Remaining Lives", remaining)

with col2:
    st.metric("❌ Wrong Guesses", wrong_guesses)

# Display hidden word
display_word = " ".join(
    letter if letter in guessed else "_"
    for letter in word
)

st.markdown(
    f"<div class='word'>{display_word}</div>",
    unsafe_allow_html=True
)

st.write("")

# Display guessed letters
if guessed:
    st.write("**Guessed Letters:**", " ".join(sorted(guessed)))
else:
    st.write("**Guessed Letters:** None")

st.divider()

# Guessing interface
st.subheader("🔤 Choose a Letter")

if not st.session_state.game_over:

    for row in ["ABCDEFGHIJ", "KLMNOPQRST", "UVWXYZ"]:

        cols = st.columns(len(row))

        for col, letter in zip(cols, row):

            with col:

                if st.button(
                    letter,
                    key=letter,
                    disabled=letter.lower() in guessed,
                    use_container_width=True
                ):

                    st.session_state.guessed.append(
                        letter.lower()
                    )

                    st.rerun()

# Game result
if st.session_state.game_over:

    st.divider()

    if st.session_state.won:

        st.success("🎉 Congratulations! You Won!")

    else:

        st.error("💀 Game Over! You Lost.")

    st.write("The correct word was:", word.upper())

    if st.button("🔄 Play Again", use_container_width=True):

        new_game()
        st.rerun()

# Footer
st.divider()

st.caption(
    "CodeAlpha Python Programming Internship | "
    "Hangman Game"
)