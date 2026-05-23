import streamlit as st
from textblob import TextBlob
from spellchecker import SpellChecker
import re

# =========================
# SPELL CHECKER SETUP
# =========================
spell = SpellChecker()

# =========================
# PAGE SETTINGS
# =========================
st.set_page_config(
    page_title="Auto Correct Engine",
    page_icon="🧠",
    layout="centered"
)

# =========================
# PROJECT TITLE
# =========================
st.title("🎓 BHARATVERSITY INTERNSHIP PROJECT (DATA SCIENCE)")

st.header("🔍 Auto-Correct Engine for Sentences/Paragraphs")


st.markdown("---")


st.write("Paste any sentence or paragraph below to automatically correct spelling and basic grammar mistakes.")


text_input = st.text_area(
    "✍️ Enter your text here:",
    height=250,
    placeholder="Example: She dont no how to writte proper English."
)


if st.button("✅ Correct Text"):

    if text_input.strip():


        words = re.findall(r'\b\w+\b', text_input)

        corrected_words = []
        mistakes = []


        for word in words:

            corrected = spell.correction(word)

            if corrected is None:
                corrected = word

            corrected_words.append(corrected)

            if word.lower() != corrected.lower():
                mistakes.append((word, corrected))


        corrected_sentence = " ".join(corrected_words)


        blob = TextBlob(corrected_sentence)

        final_text = str(blob.correct())


        st.subheader("✅ Corrected Text")

        st.success(final_text)



        if mistakes:

            st.subheader("⚠️ Misspelled Words Found")

            shown = set()

            for wrong, correct in mistakes:

                if wrong not in shown:

                    shown.add(wrong)

                    st.write(f"❌ {wrong}  →  ✅ {correct}")

        else:
            st.success("🎉 No spelling mistakes found!")

    else:
        st.warning("⚠️ Please enter some text.")