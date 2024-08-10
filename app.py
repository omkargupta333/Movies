import streamlit as st

# Set the page title and icon
st.set_page_config(page_title="Omkar Mix Movies", page_icon="🎬", layout="centered")

# Main UI layout
st.title("Welcome to Omkar Mix Movies! 🎥🍿")

# Add some spacing
st.write(" ")

# Note about trending and latest movies
st.markdown("""
    <div style="background-color:#f0f0f5; padding: 20px; border-radius: 8px; border: 1px solid #ddd; margin-bottom: 30px;">
        <h2 style="color: #2a9d8f;">Trending and Latest Movies 🌟</h2>
        <p style="color: #333;">
            Discover the most popular and recently released movies all in one place. Enjoy our curated selection of the latest hits and trending favorites! 🎬🔥
        </p>
    </div>
    """, unsafe_allow_html=True)

# Button to trigger the redirect
if st.button("Go to Omkar Mix Movies"):
    st.balloons()  # Show balloons effect
    st.write("Redirecting...")
    st.markdown(f'<meta http-equiv="refresh" content="0; url=https://goku.sx/home" />', unsafe_allow_html=True)

# Add some spacing
st.write(" ")

# Persistent session state to check if user returns
if 'visited' not in st.session_state:
    st.session_state['visited'] = False

# If the user leaves and returns, show the welcome message again
if st.session_state['visited']:
    st.title("Welcome Back to Omkar Mix Movies! 🎉")
    st.write("We're glad to have you back. 😊")
else:
    st.session_state['visited'] = True
