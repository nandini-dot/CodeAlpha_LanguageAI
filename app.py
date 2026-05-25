import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="LanguageAI",
    page_icon="🌐",
    layout="wide"
)

# ---------------- SESSION STATE ---------------- #

if "pasted_text" not in st.session_state:
    st.session_state.pasted_text = ""

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

/* Background */

.stApp {
    background-color:#111827 ;
    color: white;
}

/* Remove Streamlit Menu */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}



/* Hero Section */

.hero {
    text-align: center;
    padding-top: 20px;
    padding-bottom: 30px;
}

.hero h1 {
    font-size: 90px;
    font-weight: bold;
    color: white;
    line-height: 1.1;
}

.hero h2 {
    font-size: 80px;
    color: #D4145A;
    margin-top: 0px;
}

.hero-text {
    font-size: 20px;
    color: #dcdcdc;
    line-height: 1.8;
    width: 70%;
    margin: auto;
    font-weight: 400;
    padding-top: 10px;
}
/* Button */

.stButton>button {
    background: linear-gradient(90deg, #800020, #D4145A);
    color: white;
    border: none;
    border-radius: 12px;
    height: 3.2em;
    font-size: 18px;
    font-weight: bold;
    width: 100%;
}

/* Translator Box */

.translator-box {
    background-color: #0F0A19;
    padding: 30px;
    border-radius: 20px;
    border: 1px solid #4B0F2D;
    margin-top: 50px;
}

/* How It Works */

.steps {
    background-color: #0F0A19;
    padding: 25px;
    border-radius: 20px;
    border: 1px solid #4B0F2D;
    height: 100%;
}

.steps h2 {
    color: white;
    margin-bottom: 25px;
}

.step-item {
    margin-bottom: 30px;
}

.step-item h3 {
    color: #D4145A;
}

.step-item p {
    color: #D0D0D0;
    font-size: 17px;
}

/* Text Area */



/* Output Box */

.output-box {
    background-color: #161021;
    padding: 20px;
    border-radius: 15px;
    color: white;
    font-size: 22px;
    margin-top: 20px;
    border: 1px solid #4B0F2D;
}

/* Select Box */

div[data-baseweb="select"] {
    background-color: #161021 !important;
    border-radius: 10px !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- NAVBAR ---------------- #

st.markdown("""
<h1 style='text-align:center; color:white;'>
    Language<span style='color:#D4145A;'>AI</span>
</h1>
""", unsafe_allow_html=True)

# ---------------- HERO SECTION ---------------- #

st.markdown("""
<div class="hero">
    <h1>Instant Translation</h1>
    <h2>Powered By AI</h2>
<div class="hero-text">
    LanguageAI helps you translate text instantly into multiple languages
    with smart AI-powered translation and speech output.
</div>
</div>
""", unsafe_allow_html=True)

# ---------------- MAIN LAYOUT ---------------- #

col1, col2 = st.columns([1, 2])

# ---------------- LEFT SIDE ---------------- #

with col1:

    st.markdown("""
    <div class="steps">

    <h2>⚡ How It Works</h2>

    <div class="step-item">
        <h3>1. Enter Text</h3>
        <p>Type or paste the text you want to translate.</p>
    </div>

    <div class="step-item">
        <h3>2. Select Languages</h3>
        <p>Choose source and target languages.</p>
    </div>

    <div class="step-item">
        <h3>3. Translate</h3>
        <p>Click the translate button and let AI do the magic.</p>
    </div>

    <div class="step-item">
        <h3>4. Listen & Use</h3>
        <p>Play translated audio and use it anywhere.</p>
    </div>

    </div>
    """, unsafe_allow_html=True)

# ---------------- RIGHT SIDE ---------------- #

with col2:

    st.markdown('<div class="translator-box">', unsafe_allow_html=True)

    st.subheader("🌐 AI Translator")

    # Languages

    languages = {
        "English": "en",
        "Hindi": "hi",
        "Telugu": "te",
        "Tamil": "ta",
        "French": "fr",
        "German": "de",
        "Spanish": "es",
        "Japanese": "ja",
        "Chinese": "zh-cn"
    }

    # Paste Button

    if st.button("📋 Paste Text"):

        st.session_state.pasted_text = pyperclip.paste()

    # Input Text

    text = st.text_area(
        "Enter Text",
        value=st.session_state.pasted_text,
        height=180,
        placeholder="Type or paste your text here..."
    )

    # Language Selection

    c1, c2 = st.columns(2)

    with c1:
        source_lang = st.selectbox(
            "From",
            list(languages.keys())
        )

    with c2:
        target_lang = st.selectbox(
            "To",
            list(languages.keys())
        )

    # Translate Button

    if st.button("✨ Translate"):

        if text:

            translated = GoogleTranslator(
                source=languages[source_lang],
                target=languages[target_lang]
            ).translate(text)

            st.success("✅ Translation Completed!")

            # Output

            st.markdown(
                f"""
                <div class="output-box">
                {translated}
                </div>
                """,
                unsafe_allow_html=True
            )

            # Copy Button

            # Copy Section

            # Copy Section

            # Copy Button

            st.code(translated, language=None)
            
            

            tts = gTTS(translated)

            tts.save("voice.mp3")

            audio_file = open("voice.mp3", "rb")

            st.audio(audio_file.read(), format="audio/mp3")

        else:
            st.warning("⚠ Please enter some text.")

    st.markdown('</div>', unsafe_allow_html=True)