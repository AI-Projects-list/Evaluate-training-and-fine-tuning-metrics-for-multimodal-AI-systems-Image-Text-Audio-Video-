import streamlit as st
import pandas as pd
import numpy as np
import os

# Load or simulate log data (replace with actual log file reads)
def load_logs():
    data = {
        'epoch': list(range(1, 11)),
        'image_accuracy': np.random.uniform(0.6, 0.95, 10),
        'image_loss': np.random.uniform(0.2, 1.2, 10),
        'text_bleu': np.random.uniform(0.2, 0.9, 10),
        'text_perplexity': np.random.uniform(10, 60, 10),
        'audio_wer': np.random.uniform(5, 30, 10),
        'video_map': np.random.uniform(0.4, 0.9, 10),
        'video_fps': np.random.uniform(8, 25, 10),
    }
    return pd.DataFrame(data)

def status_label(metric, value):
    if metric == "image_accuracy":
        return "OK" if value > 0.85 else "NOK"
    elif metric == "image_loss":
        return "OK" if value < 1.0 else "NOK"
    elif metric == "text_bleu":
        return "OK" if value > 0.7 else "NOK"
    elif metric == "text_perplexity":
        return "OK" if value < 20 else "NOK"
    elif metric == "audio_wer":
        return "OK" if value < 10 else "NOK"
    elif metric == "video_map":
        return "OK" if value > 0.75 else "NOK"
    elif metric == "video_fps":
        return "OK" if value > 15 else "NOK"
    return "Unknown"

# Streamlit UI
st.title("🧠 Multimodal AI Evaluation Dashboard")
st.write("Evaluate and visualize fine-tuning metrics across modalities (Image, Text, Audio, Video)")

df = load_logs()
epoch = st.slider("Select Epoch", 1, len(df), 10)
data = df[df.epoch == epoch].squeeze()

st.subheader(f"📈 Evaluation at Epoch {epoch}")

cols = st.columns(4)
with cols[0]:
    st.metric("Image Accuracy", f"{data.image_accuracy:.2f}", status_label("image_accuracy", data.image_accuracy))
    st.metric("Image Loss", f"{data.image_loss:.2f}", status_label("image_loss", data.image_loss))
with cols[1]:
    st.metric("Text BLEU", f"{data.text_bleu:.2f}", status_label("text_bleu", data.text_bleu))
    st.metric("Text Perplexity", f"{data.text_perplexity:.2f}", status_label("text_perplexity", data.text_perplexity))
with cols[2]:
    st.metric("Audio WER", f"{data.audio_wer:.2f}%", status_label("audio_wer", data.audio_wer))
with cols[3]:
    st.metric("Video mAP", f"{data.video_map:.2f}", status_label("video_map", data.video_map))
    st.metric("Video FPS", f"{data.video_fps:.2f}", status_label("video_fps", data.video_fps))

st.subheader("📊 Trends Over Epochs")
st.line_chart(df.set_index("epoch")[["image_accuracy", "text_bleu", "video_map"]])
st.line_chart(df.set_index("epoch")[["image_loss", "text_perplexity", "audio_wer"]])
