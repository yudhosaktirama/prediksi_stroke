import pickle
import streamlit as st
import numpy as np
import pandas as pd

model = pickle.load(open('stroke_model.sav','rb'))

st.title("Program Prediksi Penyakit Stroke")

df1 = pd.read_csv('data_baru.csv').dropna(ignore_index=True)

st.dataframe(df1)

st.write('Umur')
chart_umur = df1['age'].head(208)
chart_hipertensi = df1['hypertension'].head(208)
chart_jantung = df1['heart_disease'].head(208)
chart_bmi = df1['bmi'].head(208)
chart_gula_darah = df1['avg_glucose_level'].head(208)
st.line_chart(chart_umur)
st.write('Hipertensi')
st.scatter_chart(chart_hipertensi)

st.write('Penyakit Jantung')
st.scatter_chart(chart_jantung)

st.write('Kadar BMI')
st.line_chart(chart_bmi)

st.write('Rata-Rata Gula Darah')
st.line_chart(chart_gula_darah)


def validateTwo(listYangMau,item):
    if item == listYangMau[0]:
        return 1
    else:
        return 0

def validateTipeKerja(listTipeKerja,item):
    if item == listTipeKerja[0]:
        return 0
    elif item == listTipeKerja[1]:
        return 1
    elif item == listTipeKerja[2]:
        return 2
    elif item == listTipeKerja[3]:
        return 4
    else:
        return 3

def validateMerokok(listRokok,item):
    if item == listRokok[0]:
        return 0
    elif item == listRokok[1]:
        return 1
    elif item == listRokok[2]:
        return 2
    else:
        return 3

genderList = ['Perempuan','Laki-Laki']
hipertensiList = ['Ya','Tidak']
penyakit_jantung_list = ['Ya','Tidak']
menikah_list = ['Ya','Tidak']
tipeKerja_list = ['Wirausaha','Karyawan','Pegawai Negeri','Belum Bekerja','Masih Pelajar']
kediaman_list = ['Perkotaan','Pedesaaan']
merokok_list = ['Sebelumnya Pernah Merokok','Tidak Pernah Merokok','Merokok','Tidak Menjawab']

gender_text = ""
hipertensi_text = ""
penyakit_jantung_text = ""
menikah_text = ""
tipeKerja_text = ""
kediaman_text = ""
merokok_text = ""

col1,col2 = st.columns(2)

with col1:
    gender = st.selectbox("Pilih Gender",options=genderList)
    umur = st.number_input("Masukkan Umur Anda",min_value=0,max_value=100)
    hipertensi = st.selectbox("Apakah Anda terkena Hipertensi",options=hipertensiList)
    penyakit_jantung = st.selectbox("Apakah Anda Pernah Terkena Penyakit Jantung",options=penyakit_jantung_list)
    menikah = st.selectbox("Apakah Sudah Pernah Menikah",options=menikah_list)

with col2:
    tipeKerja = st.selectbox("Pilih Tipe Pekerjaan Yang Anda Lakukan",options=tipeKerja_list)
    kediaman = st.selectbox("Dimanakah Area Tempat Anda Tinggal",options=kediaman_list)
    glukosa = st.slider("Rata-Rata Gula Darah",min_value=0.00,max_value=300.00)
    bmi = st.slider("Kadar BMI",min_value=0.00,max_value=100.00)
    merokok = st.selectbox("Apakah Anda Merokok",options=merokok_list)

gender_text = validateTwo(genderList,gender)
hipertensi_text = validateTwo(hipertensiList,hipertensi)
penyakit_jantung_text = validateTwo(penyakit_jantung_list,penyakit_jantung)
menikah_text = validateTwo(menikah_list,menikah)
kediaman_text = validateTwo(kediaman_list,kediaman)
tipeKerja_text = validateTipeKerja(tipeKerja_list,tipeKerja)
merokok_text = validateMerokok(merokok_list,merokok)


# Membuat DataFrame dari data pengguna
input_df = pd.DataFrame(input_data)

# Menampilkan bar chart dengan data yang telah digabung
fig, ax = plt.subplots(figsize=(16, 10))

# Kolom-kolom yang ingin ditampilkan dalam grouped bar chart
columns_to_plot = ['gender', 'age', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'avg_glucose_level', 'bmi', 'smoking_status']

# Membuat grouped bar chart dengan warna yang berbeda
color_cycle = cycle(plt.rcParams['axes.prop_cycle'].by_key()['color'])
for i, col in enumerate(columns_to_plot):
    ax.bar(i, input_df[col].iloc[0], color=next(color_cycle), label=col)

# Menambahkan label dan judul
ax.set_ylabel('Values')
ax.set_xlabel('Categories')
ax.set_title('Grouped Bar Chart')
ax.set_xticks(range(len(columns_to_plot)))
ax.set_xticklabels(columns_to_plot)
ax.legend()



diagnosa = ''
if st.button('Prediksi Penyakit Stroke'):
    prediksi = model.predict(input_df.tail(1)[['gender', 'age', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'avg_glucose_level', 'bmi', 'smoking_status']])
    if prediksi[0] == 1:
        diagnosa = "Pasien Diduga Kuat Terkena Stroke"
    else:
        diagnosa = "Pasien Diduga Kuat Tidak Terkena Stroke"

st.success(diagnosa)
st.pyplot(fig)




