import re
from collections import Counter
import streamlit as st

# Judul Aplikasi
st.title("🔢 Pengelompok Keberulangan Angka Togel")
st.write(
    "Masukkan teks berisi angka 4D, 3D, atau 2D. Aplikasi akan menghitung total kemunculan angka tersebut."
)

# Area Input Teks
user_input = st.text_area(
    "Masukkan data angka di sini (Bebas format: spasi, koma, bintang, huruf, dll):",
    height=200,
)

if user_input:
    # Menggunakan regex untuk mengambil semua deretan angka dari teks
    all_numbers = re.findall(r"\d+", user_input)

    # Memisahkan angka berdasarkan panjang digitnya (4D, 3D, 2D)
    list_4d = [num for num in all_numbers if len(num) == 4]
    list_3d = [num for num in all_numbers if len(num) == 3]
    list_2d = [num for num in all_numbers if len(num) == 2]

    # Menghitung kemunculan setiap angka
    count_4d = Counter(list_4d)
    count_3d = Counter(list_3d)
    count_2d = Counter(list_2d)

    # Mencari jumlah kemunculan maksimal yang ada di data
    all_counts = list(count_4d.values()) + list(count_3d.values()) + list(count_2d.values())
    max_count = max(all_counts) if all_counts else 0

    st.subheader("📊 Hasil Analisis Data:")

    if max_count == 0:
        st.warning("Tidak ada angka valid yang ditemukan.")
    else:
        # Menampilkan hasil perulangan dari 1 sampai jumlah maksimal yang ditemukan
        for i in range(1, max_count + 1):
            # Menyaring angka yang muncul sebanyak 'i' kali
            res_4d = [num for num, count in count_4d.items() if count == i]
            res_3d = [num for num, count in count_3d.items() if count == i]
            res_2d = [num for num, count in count_2d.items() if count == i]

            # Jika ada angka yang muncul sebanyak 'i' kali, tampilkan hasilnya
            if res_4d or res_3d or res_2d:
                st.markdown(f"#### 🔴 **Keluar {i} kali :**")

                if res_4d:
                    # Menggabungkan hasil dengan tanda bintang (*)
                    st.text(f"4D: {'*'.join(res_4d)}")
                if res_3d:
                    st.text(f"3D: {'*'.join(res_3d)}")
                if res_2d:
                    st.text(f"2D: {'*'.join(res_2d)}")

                st.write("---")

