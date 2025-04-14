import streamlit as st
import random

# Page setup
st.set_page_config(page_title="Rock, Paper, Scissors", page_icon="✊✋✌️", layout="centered")

# Background style with gradient and transition
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #d0f0ff, #e6f7ff);
            transition: background 0.5s ease-in-out;
        }
        .stButton>button {
            width: 100%;
            font-size: 18px;
            background-color: #00aaff;
            color: white;
            border-radius: 12px;
            padding: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background-color: #008fcc;
            transform: scale(1.05);
        }
        .result-text {
            animation: fadeIn 0.8s ease-in-out;
        }
        @keyframes fadeIn {
            from {opacity: 0; transform: translateY(10px);}
            to {opacity: 1; transform: translateY(0);}
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
    <div class='choice-card'>
        <h1 style='text-align: center; color: #007acc;'>✊ Rock, Paper, Scissors ✋</h1>
        <p style='text-align: center; font-size: 18px;'>Choose your move and see if you can beat the computer!</p>
    </div>
""", unsafe_allow_html=True)

# Choices
choices = ["Rock", "Paper", "Scissors"]
user_choice = st.selectbox("🎯 Your Choice:", choices)

# Function to determine winner
def determine_winner(user, computer):
    if user == computer:
        return "It's a tie! 🤝"
    elif (
        (user == "Rock" and computer == "Scissors") or
        (user == "Paper" and computer == "Rock") or
        (user == "Scissors" and computer == "Paper")
    ):
        return "🎉 You win! 🎉"
    else:
        return "💻 Computer wins! 💻"

# 3D-style game board
st.markdown("<div class='choice-card'>", unsafe_allow_html=True)

# Play button
if st.button("Play 🎮"):
    computer_choice = random.choice(choices)
    st.markdown(f"**🖥️ Computer chose:** `{computer_choice}`")
    result = determine_winner(user_choice, computer_choice)
    st.markdown(f"<h3 class='result-text' style='text-align: center;'>{result}</h3>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
<hr style='border: 1px solid #b3d9ff;'>
<p style='text-align: center; font-size: 14px;'>Developed by Sabila Aleem ❤</p>
""", unsafe_allow_html=True)



