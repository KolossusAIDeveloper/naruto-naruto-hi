import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Hi", page_icon="👋", layout="centered")

THEME_KEY = "theme_hi_app"

# --- Theme CSS ---
theme_script = """
<script>
(function() {
    const THEME_KEY = 'theme_hi_app';
    function getTheme() {
        const saved = localStorage.getItem(THEME_KEY);
        if (saved) return saved;
        return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'dark';
    }
    function applyTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
    }
    const current = getTheme();
    applyTheme(current);
    localStorage.setItem(THEME_KEY, current);

    // Listen for theme change messages from Streamlit
    window.addEventListener('message', function(e) {
        if (e.data && e.data.type === 'set_theme') {
            applyTheme(e.data.theme);
            localStorage.setItem(THEME_KEY, e.data.theme);
        }
    });

    // Listen for OS preference changes (only if no saved preference)
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function(e) {
        if (!localStorage.getItem(THEME_KEY)) {
            applyTheme(e.matches ? 'dark' : 'light');
        }
    });
})();
</script>
"""

light_css = """
[data-theme="light"] {
    --bg-primary: #ffffff;
    --bg-secondary: #f0f2f6;
    --bg-card: #ffffff;
    --text-primary: #1a1a2e;
    --text-secondary: #4a4a6a;
    --text-muted: #8888a0;
    --border-color: #e0e0e8;
    --accent: #6c5ce7;
    --accent-hover: #5a4bd1;
    --accent-light: #eeebff;
    --shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    --toggle-bg: #e0e0e8;
    --toggle-dot: #ffffff;
    --gradient-start: #6c5ce7;
    --gradient-end: #a29bfe;
    --wave-color: #6c5ce7;
}

[data-theme="dark"] {
    --bg-primary: #0f0f1a;
    --bg-secondary: #1a1a2e;
    --bg-card: #1e1e32;
    --text-primary: #e8e8f0;
    --text-secondary: #b0b0c8;
    --text-muted: #6a6a8a;
    --border-color: #2a2a40;
    --accent: #7c6ff7;
    --accent-hover: #8f7fff;
    --accent-light: #1e1a3a;
    --shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    --toggle-bg: #3a3a55;
    --toggle-dot: #7c6ff7;
    --gradient-start: #7c6ff7;
    --gradient-end: #a29bfe;
    --wave-color: #7c6ff7;
}
"""

def inject_theme():
    # Read current theme from query params or default to dark
    theme = st.query_params.get("theme", "dark")
    
    toggle_css = f"""
    <style>
        {light_css}
        
        .stApp {{
            background-color: var(--bg-primary);
        }}
        
        .main-header {{
            text-align: center;
            padding: 2rem 0 0.5rem 0;
        }}
        
        .main-header h1 {{
            font-size: 5rem;
            font-weight: 800;
            margin: 0;
            background: linear-gradient(135deg, var(--gradient-start), var(--gradient-end));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: -2px;
        }}
        
        .main-header p {{
            color: var(--text-secondary);
            font-size: 1.2rem;
            margin-top: 0.5rem;
        }}
        
        .greeting-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 20px;
            padding: 2.5rem 2rem;
            text-align: center;
            box-shadow: var(--shadow);
            margin-top: 2rem;
            transition: transform 0.2s ease;
        }}
        
        .greeting-card:hover {{
            transform: translateY(-4px);
        }}
        
        .greeting-card .emoji {{
            font-size: 4rem;
            margin-bottom: 1rem;
        }}
        
        .greeting-card h2 {{
            color: var(--text-primary);
            font-size: 2rem;
            font-weight: 700;
            margin: 0.5rem 0;
        }}
        
        .greeting-card .message {{
            color: var(--text-secondary);
            font-size: 1.1rem;
            line-height: 1.6;
        }}
        
        .footer {{
            text-align: center;
            color: var(--text-muted);
            padding: 2rem 0;
            font-size: 0.9rem;
        }}
        
        /* Theme toggle */
        .theme-toggle-wrapper {{
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 0.5rem;
            margin-top: 1.5rem;
        }}
        
        .theme-toggle-wrapper span {{
            color: var(--text-secondary);
            font-size: 1.2rem;
        }}
        
        .theme-toggle {{
            position: relative;
            width: 56px;
            height: 28px;
            background: var(--toggle-bg);
            border-radius: 28px;
            cursor: pointer;
            border: none;
            outline: none;
            padding: 0;
            transition: background 0.3s ease;
        }}
        
        .theme-toggle .dot {{
            position: absolute;
            top: 3px;
            left: 3px;
            width: 22px;
            height: 22px;
            background: var(--toggle-dot);
            border-radius: 50%;
            transition: transform 0.3s ease;
            box-shadow: 0 1px 3px rgba(0,0,0,0.2);
        }}
        
        [data-theme="light"] .theme-toggle .dot {{
            transform: translateX(28px);
        }}
        
        /* Override Streamlit default styles */
        .stButton > button {{
            background: var(--accent) !important;
            color: #ffffff !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 0.6rem 1.5rem !important;
            font-weight: 600 !important;
            transition: background 0.2s ease !important;
        }}
        
        .stButton > button:hover {{
            background: var(--accent-hover) !important;
        }}
        
        /* Hide Streamlit default header/footer */
        header[data-testid="stHeader"] {{
            background: transparent !important;
        }}
        
        .stApp {{
            background: var(--bg-primary) !important;
        }}
        
        section[data-testid="stSidebar"] {{
            display: none;
        }}
        
        .stApp > header {{
            background: var(--bg-primary) !important;
        }}
        
        .block-container {{
            padding-top: 2rem;
            max-width: 700px;
        }}
        
        /* Style the "made with streamlit" */
        footer {{
            display: none;
        }}
        
        /* Override streamlit text colors */
        .stMarkdown, .stText, p, h1, h2, h3, h4, h5, h6, span, div {{
            color: var(--text-primary);
        }}
        
        /* Style streamlit's main container */
        .main .block-container {{
            background: var(--bg-primary);
        }}
        
        /* Radio buttons for theme (hidden) */
        div[data-testid="stRadio"] {{
            display: none;
        }}
    </style>
    {theme_script}
    """
    components.html(toggle_css, height=0)

def render_toggle():
    theme = st.query_params.get("theme", "dark")
    is_dark = theme == "dark"
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        # Using a button that toggles via query params
        new_theme = "light" if is_dark else "dark"
        emoji = "🌙" if is_dark else "☀️"
        label = f"{emoji}  Switch to {'Light' if is_dark else 'Dark'} Mode"
        if st.button(label, key="theme_toggle", use_container_width=True):
            st.query_params["theme"] = new_theme
            st.rerun()

def main():
    inject_theme()
    
    # Main header
    st.markdown("""
    <div class="main-header">
        <h1>Hi!</h1>
        <p>Welcome to your friendly greeting app</p>
    </div>
    """, unsafe_allow_html=True)
    
    render_toggle()
    
    # Greeting card
    st.markdown("""
    <div class="greeting-card">
        <div class="emoji">👋</div>
        <h2>Hello there!</h2>
        <p class="message">
            This is a simple Hi app built with Streamlit.<br>
            It features a beautiful light and dark theme<br>
            that persists across visits.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Name input
    name = st.text_input("What's your name?", placeholder="Enter your name here...")
    
    if name:
        st.markdown(f"""
        <div class="greeting-card">
            <div class="emoji">✨</div>
            <h2>Hi, {name}! 👋</h2>
            <p class="message">
                Glad to see you here! Hope you're having<br>
                an amazing day. 😊
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div class="footer">
        Built with ❤️ using Streamlit
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
