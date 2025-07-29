import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(
    page_title="Simple AI Agent",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS for enhanced styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Product+Sans:wght@300;400;500;700&display=swap');
    
    * {
        font-family: 'Product Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }
    
    .main-container {
        position: relative;
        padding-top: 1rem;
    }
    
    .github-corner {
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 999;
        background: transparent;
        transition: transform 0.3s ease;
    }
    
    .github-corner:hover {
        transform: scale(1.1);
    }
    
    .github-logo {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
        transition: all 0.3s ease;
        filter: brightness(1);
    }
    
    .github-logo:hover {
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.5);
        transform: rotate(5deg);
    }
    
    /* Dark mode styles */
    @media (prefers-color-scheme: dark) {
        .github-logo {
            filter: invert(1) brightness(1.2);
            box-shadow: 0 4px 12px rgba(255, 255, 255, 0.2);
        }
        
        .github-logo:hover {
            box-shadow: 0 6px 20px rgba(255, 255, 255, 0.3);
            filter: invert(1) brightness(1.4);
        }
    }
    
    /* Streamlit dark mode detection */
    [data-testid="stAppViewContainer"][data-theme="dark"] .github-logo {
        filter: invert(1) brightness(1.2);
        box-shadow: 0 4px 12px rgba(255, 255, 255, 0.2);
    }
    
    [data-testid="stAppViewContainer"][data-theme="dark"] .github-logo:hover {
        box-shadow: 0 6px 20px rgba(255, 255, 255, 0.3);
        filter: invert(1) brightness(1.4);
    }
    
    /* Light mode styles (default) */
    [data-testid="stAppViewContainer"][data-theme="light"] .github-logo {
        filter: brightness(1);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
    }
    
    [data-testid="stAppViewContainer"][data-theme="light"] .github-logo:hover {
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.5);
        filter: brightness(1);
    }
    
    .main-header {
        text-align: center;
        padding: 3rem 0 1rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #667eea 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        font-family: 'Product Sans', sans-serif;
        letter-spacing: -0.02em;
    }
    
    .subtitle {
        text-align: center;
        color: #555;
        font-size: 1.3rem;
        margin-bottom: 0.5rem;
        font-weight: 500;
        font-family: 'Product Sans', sans-serif;
    }
    
    .powered-by {
        text-align: center;
        color: #888;
        font-size: 1rem;
        margin-bottom: 3rem;
        font-style: italic;
        font-weight: 400;
        font-family: 'Product Sans', sans-serif;
    }
    
    .chat-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 0 1rem;
    }
    
    .stChatMessage {
        padding: 1.2rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        font-family: 'Product Sans', sans-serif;
    }
    
    .stSpinner {
        text-align: center;
    }
    
    .stChatInput {
        font-family: 'Product Sans', sans-serif;
    }
    
    .header-section {
        text-align: center;
        margin-bottom: 2rem;
        padding: 2rem 1rem;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.05) 0%, rgba(118, 75, 162, 0.05) 100%);
        border-radius: 20px;
        margin: 2rem 1rem;
    }
</style>
""", unsafe_allow_html=True)

# GitHub Corner with PNG logo
st.markdown("""
<a href="https://github.com/omsudhamsh/simple-ai-agent" class="github-corner" aria-label="View source on GitHub" title="View on GitHub" target="_blank">
    <img src="data:image/png;base64,{}" class="github-logo" alt="GitHub">
</a>
""".format(
    __import__('base64').b64encode(
        open('Source/25231.png', 'rb').read()
    ).decode()
), unsafe_allow_html=True)

# Main content container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Header section with improved styling
st.markdown("""
<div class="header-section">
    <h1 class="main-header">🤖 Simple Chat AI Agent</h1>
    <p class="subtitle">Level 1 - Conversational AI Assistant</p>
    <p class="powered-by">✨ Powered by Gemini 1.5 Flash</p>
</div>
""", unsafe_allow_html=True)

try:
    # Try to get API key from Streamlit secrets first (for deployment)
    if hasattr(st, 'secrets') and 'GEMINI_API_KEY' in st.secrets:
        api_key = st.secrets["GEMINI_API_KEY"]
    # Fallback to environment variable (for local development)
    elif os.getenv('GEMINI_API_KEY'):
        api_key = os.getenv('GEMINI_API_KEY')
    else:
        st.error("🔑 **API Key Missing!** Please set your GEMINI_API_KEY in one of the following ways:")
        st.markdown("""
        **For Streamlit Cloud deployment:**
        - Add `GEMINI_API_KEY` in the app's secrets section
        
        **For local development:**
        - Create `.streamlit/secrets.toml` file with: `GEMINI_API_KEY = "your-key"`
        - Or set environment variable: `GEMINI_API_KEY=your-key`
        
        **Get your API key:** [Google AI Studio](https://makersuite.google.com/app/apikey)
        """)
        st.stop()
    
    genai.configure(api_key=api_key)
    
except FileNotFoundError:
    st.error("🔧 **Configuration Issue:** The `secrets.toml` file was not found. Please create it and add your GEMINI_API_KEY.")
    st.info("💡 **Tip:** Copy `.streamlit/secrets.example.toml` to `.streamlit/secrets.toml` and add your API key.")
    st.stop()
except KeyError:
    st.error("🔑 **Missing API Key:** Your `GEMINI_API_KEY` is not set in the `secrets.toml` file. Please add it.")
    st.stop()
except Exception as e:
    st.error(f"❌ **Setup Error:** {e}")
    st.stop()


model = genai.GenerativeModel('gemini-1.5-flash-latest')

if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat container with enhanced styling
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("🤖 Thinking..."):
        try:
            response = model.generate_content(prompt)
            ai_response = response.text
            st.session_state.messages.append({"role": "assistant", "content": ai_response})
            with st.chat_message("assistant"):
                st.markdown(ai_response)
        except Exception as e:
            st.error(f"❌ An error occurred: {e}")

st.markdown('</div>', unsafe_allow_html=True)  # Close chat-container
st.markdown('</div>', unsafe_allow_html=True)  # Close main-container