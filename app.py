import streamlit as st
import numpy as np
import joblib

st.title("📉 LSTM Zaman Serisi Tahmin Motoru")
scaler = joblib.load('price_scaler.pkl')

g1 = st.number_input("5 Gün Önce:", value=145.0)
g2 = st.number_input("4 Gün Önce:", value=146.0)
g3 = st.number_input("3 Gün Önce:", value=149.2)
g4 = st.number_input("2 Gün Önce:", value=148.5)
g5 = st.number_input("Dün:", value=150.0)

if st.button("Tahmin Et"):
    input_data = np.array([g1, g2, g3, g4, g5]).reshape(-1, 1)
    scaled_input = scaler.transform(input_data)
    # Basit bir LSTM trend simülasyonu
    tahmin = scaled_input.mean() * 1.05 
    final_price = scaler.inverse_transform([[tahmin]])[0][0]
    st.metric("Yarınki Tahmini Fiyat", f"${final_price:.2f}")