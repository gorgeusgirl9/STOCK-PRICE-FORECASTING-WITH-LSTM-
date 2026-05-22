# 📉 Stock Price Forecasting with LSTM (Zaman Serisi Tahmini)

https://huggingface.co/spaces/gorgeus/STOCK_PRICE_FORECASTING_WITH_LSTM






Bu proje, finansal varlıkların geçmiş fiyat hareketlerini kronolojik olarak analiz ederek gelecekteki fiyat trendlerini tahmin eden bir **Derin Öğrenme (Deep Learning) / Zaman Serisi** projesidir.

---

## 📊 Mühendislik Özeti (Eksiklikler ve Çözümler)

### 🚨 Orijinal Verideki Eksikler ve Problemler
* **Zaman Akış İhlali (Data Leakage):** Zaman serilerinde rastgele veri bölme (random split) yapılması, gelecekteki fiyatların eğitim setine sızarak modelin "geleceği görmesine" neden oluyordu.
* **Ardışık Bağımlılığın İhmali:** Klasik modeller (Random Forest, Regresyon vb.) veriyi bağımsız satırlar olarak gördüğü için zaman içindeki momentumu ıskalıyordu.
* **Gradyan Patlaması:** Finansal verilerdeki yüksek oynaklık (volatility), normalize edilmediğinde derin öğrenme modelinin gradyanlarını bozuyordu.

### 🛠️ Uygulanan Mühendislik Çözümleri
* **Kronolojik Bölme (Time Series Split):** Veri karıştırılmadan, zaman akışına sadık kalarak %80 eğitim, %20 test olacak şekilde bölündü.
* **Kayan Pencere (Sliding Window) Mühendisliği:** Geçmiş 5 günün fiyat verileri girdi (X), 6. günün fiyatı hedef (y) olacak şekilde paketlendi.
* **Min-Max Normalizasyonu:** Veriler `[0, 1]` aralığına normalize edildi ve tahmin sonrası orijinal finansal ölçeğe (inverse transform) döndürüldü.
* **LSTM Mimarisi:** Zaman serilerindeki uzun ve kısa vadeli dalgalanmaları (forget & input gates) yönetebilen **LSTM** mimarisi kullanıldı.

---

## 📈 Teknik Detaylar
* **Problem Türü:** Zaman Serisi Regresyonu / Sequential Deep Learning
* **Seçilen Algoritma:** LSTM (Long Short-Term Memory) Network
* **Kritik Metrik:** Root Mean Squared Error (RMSE)

## 🚀 Canlı Uygulama
Proje, **Hugging Face Spaces** üzerinde **Streamlit** mimarisi kullanılarak canlıya taşınmıştır. Kullanıcının girdiği 5 günlük geçmiş trende göre, derin öğrenme hafıza kapısı simülasyonuyla yarınki fiyat hedefini hesaplayan interaktif finansal dashboard'a aşağıdan erişebilirsiniz.

> **Canlı Uygulama:** 

---
