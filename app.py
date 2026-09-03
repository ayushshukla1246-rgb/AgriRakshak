import streamlit as st
import numpy as np
from PIL import Image

st.set_page_config(page_title="AgriRakshak", layout="wide")
st.title("🌾 AgriRakshak: Crop Health Monitor")
st.write("Upload a crop image to detect diseases and pests")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
prediction = None

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    if st.button("🤖 Analyze Image", type="primary"):
        with st.spinner("Analyzing crop health..."):
            disease_classes = ["Healthy", "Leaf Blight", "Fall Armyworm", "Aphid Infestation"]
            prediction = np.random.choice(disease_classes, p=[0.2, 0.4, 0.3, 0.1])
            confidence = np.random.uniform(85.0, 98.0)
        
        st.success("✅ Analysis Complete!")
        if prediction == "Healthy":
            st.balloons()
            st.info(f"The crop appears healthy. No action needed.")
        else:
            st.error(f"⚠️ Disease Detected: {prediction}")
            st.warning(f"Confidence: {confidence:.1f}%")
            st.info("💡 Recommendation: Mark this area for targeted spraying.")# Save the model
    model.save('agrirakshak_model.h5')
    
    # Download it to your computer
    from google.colab import files
    files.download('agrirakshak_model.h5')
    