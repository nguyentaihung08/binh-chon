import streamlit as st

st.title("Bình chọn độ đẹp trai")
st.subheader("Ai Đẹp Trai Nhất Trong 5 Anh Này?")

ai_dep_nhat = st.radio(
    "Chọn một người:",
    ["Quốc Anh", "Phúc An", "Kim Thái", "Phan Đức", "Tài Hưng"]
)

if st.button("Xác Nhận"):
    st.success(f"Người đẹp trai nhất là: {ai_dep_nhat}")
