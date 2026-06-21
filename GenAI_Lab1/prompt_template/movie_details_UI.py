import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import re

load_dotenv()

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CineExtract",
    page_icon="🎬",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #0d0d0f;
    color: #e8e4dc;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 1.5rem 4rem; max-width: 760px; }

.hero {
    text-align: center;
    padding: 2.5rem 0 1.5rem;
    border-bottom: 1px solid #2a2a2f;
    margin-bottom: 2rem;
}
.hero-eyebrow {
    font-size: 0.72rem;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #c8a96e;
    margin-bottom: 0.6rem;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2.4rem, 6vw, 3.8rem);
    font-weight: 900;
    line-height: 1.05;
    color: #f5f0e8;
    letter-spacing: -0.02em;
    margin: 0 0 0.5rem;
}
.hero-title span { color: #c8a96e; }
.hero-sub {
    font-size: 0.88rem;
    color: #7a7880;
    font-weight: 300;
}

.stTextArea textarea {
    background: #16161a !important;
    border: 1px solid #2e2e36 !important;
    border-radius: 6px !important;
    color: #e8e4dc !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.93rem !important;
    line-height: 1.65 !important;
    caret-color: #c8a96e;
    transition: border-color 0.2s;
}
.stTextArea textarea:focus {
    border-color: #c8a96e !important;
    box-shadow: 0 0 0 2px rgba(200,169,110,0.12) !important;
}
.stTextArea label {
    font-size: 0.78rem !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
    color: #7a7880 !important;
    margin-bottom: 0.4rem !important;
}

.stButton button {
    background: #c8a96e !important;
    color: #0d0d0f !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.85rem !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
    border: none !important;
    border-radius: 4px !important;
    padding: 0.65rem 2rem !important;
    width: 100% !important;
    cursor: pointer !important;
    transition: background 0.2s, transform 0.1s !important;
}
.stButton button:hover {
    background: #d9bc86 !important;
    transform: translateY(-1px) !important;
}
.stButton button:active { transform: translateY(0) !important; }

.results-header {
    font-size: 0.72rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #c8a96e;
    margin: 2.2rem 0 1rem;
    display: flex;
    align-items: center;
    gap: 0.8rem;
}
.results-header::after {
    content: '';
    flex: 1;
    height: 1px;
    background: #2a2a2f;
}

.field-grid { display: grid; gap: 0.75rem; }
.field-card {
    background: #16161a;
    border: 1px solid #2a2a2f;
    border-radius: 6px;
    padding: 0.85rem 1.1rem;
    display: flex;
    flex-direction: column;
    gap: 0.2rem;
    transition: border-color 0.2s;
}
.field-card:hover { border-color: #3a3a44; }
.field-label {
    font-size: 0.68rem;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: #c8a96e;
    font-weight: 600;
}
.field-value {
    font-size: 0.94rem;
    color: #e8e4dc;
    line-height: 1.5;
    font-weight: 400;
}
.field-value.not-specified {
    color: #4a4850;
    font-style: italic;
}
.stAlert { border-radius: 6px !important; }
</style>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-eyebrow">AI-Powered Information Extraction</div>
  <h1 class="hero-title">Cine<span>Extract</span></h1>
  <p class="hero-sub">Paste any movie description — get clean, structured data instantly.</p>
</div>
""", unsafe_allow_html=True)

# ── Model & Prompt ────────────────────────────────────────────────────────────
@st.cache_resource
def get_chain():
    llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")
    prompt = ChatPromptTemplate.from_messages([
        ("system", (
            "You are an expert data extraction assistant. Your task is to extract key "
            "information from the provided paragraph about a movie and format it into a "
            "clean, structured list.\n\n"
            "Extract the following details:\n"
            "- Movie Title:\n"
            "- Release Year:\n"
            "- Director:\n"
            "- Main Cast:\n"
            "- Setting/Era:\n"
            "- Core Themes:\n"
            "- Box Office/Critical Reception:\n"
            "- IMDb Rating:\n"
            "- Key Highlights/Awards:\n\n"
            "If a specific detail is not mentioned in the text, mark it as 'Not specified'."
        )),
        ("human", "Extract Information from this paragraph: {paragraph}"),
    ])
    return prompt, llm

# ── Fields ────────────────────────────────────────────────────────────────────
FIELDS = [
    ("Movie Title", "movie_title"),
    ("Release Year", "release_year"),
    ("Director", "director"),
    ("Main Cast", "main_cast"),
    ("Setting/Era", "setting_era"),
    ("Core Themes", "core_themes"),
    ("Box Office/Critical Reception", "box_office"),
    ("IMDb Rating", "imdb_rating"),
    ("Key Highlights/Awards", "highlights"),
]

def extract_raw_text(content):
    """Safely convert model response content to a plain string."""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for block in content:
            if isinstance(block, dict):
                parts.append(block.get("text", ""))
            else:
                parts.append(str(block))
        return "\n".join(parts)
    return str(content)

def parse_response(text):
    """Parse model output into a dict keyed by field name."""
    result = {}
    lines = text.splitlines()
    for label, key in FIELDS:
        found = None
        for line in lines:
            clean = re.sub(r"[*_`]", "", line).strip().lstrip("- ").strip()
            if re.match(rf"{re.escape(label)}\s*:", clean, re.IGNORECASE):
                parts = re.split(rf"{re.escape(label)}\s*:", clean, maxsplit=1, flags=re.IGNORECASE)
                if len(parts) > 1 and parts[1].strip():
                    found = parts[1].strip()
                break
        result[key] = found if found else "Not specified"
    return result

# ── UI ────────────────────────────────────────────────────────────────────────
paragraph = st.text_area(
    "Movie Raw Data",
    placeholder="Paste a movie description, review, Wikipedia blurb, or any raw text about a film…",
    height=160,
)

extract_btn = st.button("Extract Information")

if extract_btn:
    if not paragraph.strip():
        st.warning("Please paste some movie text before extracting.")
    else:
        try:
            prompt, llm = get_chain()
            with st.spinner("Extracting movie details…"):
                final_prompt = prompt.invoke({"paragraph": paragraph})
                response = llm.invoke(final_prompt)
                raw = extract_raw_text(response.content)

            parsed = parse_response(raw)

            st.markdown('<div class="results-header">Extracted Details</div>', unsafe_allow_html=True)
            st.markdown('<div class="field-grid">', unsafe_allow_html=True)

            for label, key in FIELDS:
                value = parsed.get(key, "Not specified")
                value_class = "field-value not-specified" if value.lower() == "not specified" else "field-value"
                st.markdown(
                    f'<div class="field-card">'
                    f'<div class="field-label">{label}</div>'
                    f'<div class="{value_class}">{value}</div>'
                    f'</div>',
                    unsafe_allow_html=True,
                )

            st.markdown('</div>', unsafe_allow_html=True)

            with st.expander("View raw model output"):
                st.text(raw)

        except Exception as e:
            st.error(f"Something went wrong: {e}")