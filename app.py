import streamlit as st
import time
from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes
from pathlib import Path

# Padding function
def pad(data):
    bs = Blowfish.block_size
    padding_len = bs - len(data) % bs
    return data + bytes([padding_len]) * padding_len

# Unpadding function
def unpad(data):
    padding_len = data[-1]
    return data[:-padding_len]

st.set_page_config(page_title="Blowfish File Encryption", layout="centered")

st.markdown("""
<style>
    .main {background-color: #111827; color: white;}
    .css-18e3th9 {padding: 2rem;}
    .stButton>button {background: #1f2937; color: white; border-radius: 8px; padding: 0.6rem 1rem;}
    .stFileUploader {color: white;}
</style>
""", unsafe_allow_html=True)

st.title("🔐 Blowfish File Encryption & Decryption")
st.write("Aplikasi sederhana untuk mengenkripsi dan mendekripsi file teks menggunakan algoritma Blowfish.")

mode = st.radio("Pilih Mode", ["Enkripsi", "Dekripsi"])
file = st.file_uploader("Pilih file .txt", type=["txt"])
key_input = st.text_input("Masukkan Key (min 4 byte)")

if file and key_input:
    key = key_input.encode()

    if len(key) < 4 or len(key) > 56:
        st.error("Key harus 4-56 karakter!")
    else:
        data = file.read()

        if st.button("Jalankan"):
            if mode == "Enkripsi":
                start_time = time.time()

                cipher = Blowfish.new(key, Blowfish.MODE_CBC)
                iv = cipher.iv
                padded_data = pad(data)
                encrypted = iv + cipher.encrypt(padded_data)

                exec_time = (time.time() - start_time) * 1000
                size_output = len(encrypted)

                output_path = f"encrypted_{file.name}"
                with open(output_path, "wb") as f:
                    f.write(encrypted)

                st.success("Enkripsi berhasil!")
                st.download_button("Download File Enkripsi", encrypted, file_name=output_path)
                st.write(f"Waktu eksekusi: **{exec_time:.2f} ms**")
                st.write(f"Ukuran ciphertext: **{size_output} bytes**")

            else:  # Dekripsi
                start_time = time.time()

                iv = data[:8]
                ciphertext = data[8:]
                cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv=iv)

                decrypted_padded = cipher.decrypt(ciphertext)
                decrypted = unpad(decrypted_padded)

                exec_time = (time.time() - start_time) * 1000

                output_path = f"decrypted_{file.name}"
                st.success("Dekripsi berhasil!")
                st.download_button("Download File Dekripsi", decrypted, file_name=output_path)
                st.write(f"Waktu eksekusi: **{exec_time:.2f} ms**")
