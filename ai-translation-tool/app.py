import streamlit as st
from deep_translator import GoogleTranslator

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Translator",
    page_icon="🌍",
    layout="centered"
)

# ---------------- UI HEADER ----------------
st.markdown("""
    <h1 style='text-align:center; color:#4F8BF9;'>🌍 AI Language Translator</h1>
    <p style='text-align:center;'>Fast • Smart • Multi-language Translation Tool</p>
""", unsafe_allow_html=True)

st.divider()

# ---------------- INPUT SECTION ----------------
text = st.text_area("✍️ Enter text to translate:", height=150)

# Language options
languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Arabic": "ar",
    "Chinese": "zh-cn",
    "Japanese": "ja"
}

col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox("From Language", list(languages.keys()), index=0)

with col2:
    target_lang = st.selectbox("To Language", list(languages.keys()), index=1)

# ---------------- TRANSLATE BUTTON ----------------
if st.button("🚀 Translate"):

    if text.strip() == "":
        st.warning("⚠️ Please enter text to translate!")
    else:
        try:
            with st.spinner("Translating... please wait"):

                translated = GoogleTranslator(
                    source=languages[source_lang],
                    target=languages[target_lang]
                ).translate(text)

            st.success("✅ Translation Completed!")

            # OUTPUT BOX
            st.markdown("### 📌 Result:")
            st.text_area("Translated Text", translated, height=150)

        except Exception as e:
            st.error(f"❌ Error occurred: {str(e)}")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("<p style='text-align:center;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)