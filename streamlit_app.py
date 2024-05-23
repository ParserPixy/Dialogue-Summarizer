import streamlit as st
from textSummarizer.pipeline.prediction import PredictionPipeline
import os
import time

def update_progress_bar(stages, progress_bar, status_text):
    for i, stage in enumerate(stages):
        status_text.text(stage)
        progress_bar.progress((i + 1) / len(stages))
        time.sleep(1)  # Simulating time-consuming stages

def summarize_dialogue(user_input):
    obj = PredictionPipeline()
    summary = obj.predict(user_input)
    summary = summary.replace("<n>", "")
    return summary

def main():
    st.title('Dialogue Summarizer')
    st.divider()

    user_input = st.text_area("Enter the dialogue", placeholder="Mark: Hi!\nJohhny: Hello!\nMark: Let's go swimming!\nJohnny: Sure!\nMark: I'll meet you at the pool.")

    stages = ["Ingesting data...", "Validating data...", "Transforming data...", "Training Model...", "Evaluating data..."]

    if st.button('Train model'):
        try:
            os.system("python main.py")  # Detects as command and executes
            st.success("Training Successful !!")
        except Exception as e:
            st.error(f"Error Occurred! {e}")
    
    if st.button('Summarize'):
        progress_bar = st.progress(0)
        status_text = st.empty()
        update_progress_bar(stages, progress_bar, status_text)
        summary = summarize_dialogue(user_input)
        progress_bar.empty()  # Clear the progress bar
        status_text.empty()  # Clear the status text

        st.success("Summarization completed!")
        st.divider()
        st.subheader("Summary:")
        st.info(summary)

if __name__ == "__main__":
    main()
