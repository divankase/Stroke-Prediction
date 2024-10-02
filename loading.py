import streamlit as st

# Function to show the loading page with heart rate animation
def show_loading_page():
    # CSS for heart rate animation
    heart_rate_animation = """
    <style>
    .heart {
        font-size: 100px;
        color: red;
        animation: heartbeat 1.5s infinite alternate;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        height: 40vh; /* Height for heart animation */
    }

    @keyframes heartbeat {
        0% {
            transform: scale(1);
        }
        100% {
            transform: scale(1.2);
        }
    }
    </style>
    <div class="heart">
        <div>🫀</div>
    </div>
    """

    st.markdown(heart_rate_animation, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([11.5, 4, 11.5])  # Three columns with proportions

    with col2:  # Use the middle column for centering
        if st.button("Get Start"):
            # Set a flag in the session state to indicate loading is done
            st.session_state['loaded'] = True

# Check if loading is done, otherwise show the loading page
if 'loaded' not in st.session_state:
    show_loading_page()
else:
    # Import and show the main page for Stroke Prediction
    import app  # Ensure 'app.py' is in the same directory
    app.show_main_page()
