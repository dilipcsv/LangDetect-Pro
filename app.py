import streamlit as st
from langdetect import detect, detect_langs
from langdetect.lang_detect_exception import LangDetectException

# ----------------------------------
# PAGE CONFIG
# ----------------------------------
st.set_page_config(
    page_title="LangDetect Pro",
    page_icon="🌍",
    layout="wide"
)

# ----------------------------------
# PREMIUM UI CSS
# ----------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(135deg,#0f172a,#111827,#1e293b);
    color: white;
}

.main-title {
    font-size: 42px;
    font-weight: 700;
    color: white;
    margin-bottom: 0;
}

.sub-title {
    color: #94a3b8;
    margin-top: -10px;
    margin-bottom: 20px;
}

.card {
    background: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 10px 24px rgba(0,0,0,0.25);
    backdrop-filter: blur(8px);
    border: 1px solid rgba(255,255,255,0.06);
}

.stButton>button {
    background: linear-gradient(90deg,#3b82f6,#8b5cf6);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 10px 24px;
    font-weight: 600;
}

textarea {
    border-radius: 14px !important;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------------
# LANGUAGE MAP
# ----------------------------------
LANGUAGE_MAP = {
    "en": "English",
    "fr": "French",
    "es": "Spanish",
    "de": "German",
    "hi": "Hindi",
    "te": "Telugu",
    "ta": "Tamil",
    "kn": "Kannada",
    "ml": "Malayalam",
    "zh-cn": "Chinese (Simplified)",
    "ja": "Japanese",
    "ko": "Korean",
    "ar": "Arabic",
    "ru": "Russian",
    "it": "Italian",
    "pt": "Portuguese"
}

def get_language_name(code):
    return LANGUAGE_MAP.get(code, code.upper())

# ----------------------------------
# HEADER
# ----------------------------------
st.markdown('<p class="main-title">🌍 LangDetect Pro</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Smart AI-powered Language Detection App</p>', unsafe_allow_html=True)

# ----------------------------------
# INPUT UI
# ----------------------------------
st.markdown("## ✍ Enter Text")

text = st.text_area(
    "Type or paste text below:",
    height=220,
    placeholder="Example: Bonjour tout le monde"
)

# ----------------------------------
# BUTTON
# ----------------------------------
if st.button("🔍 Detect Language"):

    if len(text.strip()) < 3:
        st.warning("Please enter longer text for better accuracy.")

    else:
        try:
            # Primary language
            lang_code = detect(text)
            lang_name = get_language_name(lang_code)

            # Confidence probabilities
            probs = detect_langs(text)

            st.success(f"✅ Primary Language Detected: {lang_name} ({lang_code})")

            st.markdown("## 📊 Confidence Scores")

            for item in probs:
                code = item.lang
                name = get_language_name(code)
                score = round(item.prob * 100, 2)

                st.progress(min(score / 100, 1.0))
                st.write(f"**{name} ({code})** — {score}%")

        except LangDetectException:
            st.error("Could not detect language. Please enter clearer text.")

# ----------------------------------
# SIDEBAR
# ----------------------------------
st.sidebar.title("⚙ Features")
st.sidebar.info("""
✅ Supports multiple languages  
✅ Confidence percentages  
✅ Clean modern UI  
✅ Fast AI-based NLP detection
""")

st.sidebar.markdown("---")
st.sidebar.caption("Built with Python + Streamlit")