import streamlit as st
import qrcode
from PIL import Image
import io

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Order QR Generator",
    page_icon="🔲",
    layout="centered"
)

# =====================================================
# UI
# =====================================================
st.title("🔲 Order QR Code Generator")

st.markdown(
    "Generate a QR code using an **Order ID**. "
    "This QR code can be scanned by the Parcel Delivery Tracking System."
)

# =====================================================
# INPUT
# =====================================================
order_id = st.text_input(
    "Enter Order ID",
    placeholder="e.g. CA-2015-105158"
)

# =====================================================
# QR GENERATION
# =====================================================
if order_id:
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    # Encode ONLY the order ID (plain text)
    qr.add_data(order_id.strip())
    qr.make(fit=True)

    qr_img = qr.make_image(
        fill_color="black",
        back_color="white"
    ).convert("RGB")

    st.image(qr_img, caption=f"QR Code for {order_id}")

    # =====================================================
    # DOWNLOAD BUTTON
    # =====================================================
    buf = io.BytesIO()
    qr_img.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="⬇️ Download QR Code",
        data=byte_im,
        file_name=f"{order_id}.png",
        mime="image/png"
    )

else:
    st.info("ℹ Please enter an Order ID to generate the QR code.")
