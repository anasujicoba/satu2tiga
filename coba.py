import streamlit as st

st.write("""
# Luas segitiga sama jenjang
sjdakskafakfka fhdafjadfkad faudbfadjfa dfajdfdafndaf adjfkfds
""")
alas = st.number_input("masukkan alas", 0)
tinggi = st.number_input("masukkan tinggi", 0)

hitung =st.button("hitung Luar")

if hitung:
    luas =0.5 * alas * tinggi
    st.success(f"luasnya adalah{luas}")
