import streamlit as st

# 60 pengetahuan tentang 17 Agustus
knowledge = [
    "Hari Kemerdekaan Indonesia diperingati setiap tanggal 17 Agustus.",
    "Proklamasi Kemerdekaan Indonesia dibacakan oleh Ir. Soekarno pada tahun 1945.",
    "Teks proklamasi ditulis oleh Soekarno dan Ahmad Soebardjo.",
    "Bendera Merah Putih pertama kali dikibarkan di Jalan Pegangsaan Timur 56, Jakarta.",
    "Upacara bendera adalah tradisi penting pada 17 Agustus.",
    "Lomba panjat pinang adalah salah satu lomba khas 17 Agustus.",
    "Lomba balap karung sering diadakan saat perayaan kemerdekaan.",
    "Lomba makan kerupuk menjadi favorit anak-anak.",
    "17 Agustus adalah hari libur nasional di Indonesia.",
    "Istana Merdeka menjadi pusat perayaan nasional.",
    "Presiden Indonesia memimpin upacara bendera di Istana Merdeka.",
    "Setiap daerah di Indonesia memiliki tradisi unik dalam merayakan 17 Agustus.",
    "Bendera Merah Putih dikibarkan di seluruh penjuru Indonesia.",
    "Pidato kenegaraan Presiden RI biasanya disampaikan sehari sebelum 17 Agustus.",
    "Teks proklamasi ditandatangani oleh Soekarno dan Mohammad Hatta.",
    "17 Agustus 1945 adalah tonggak sejarah bangsa Indonesia.",
    "Lagu Indonesia Raya dinyanyikan saat upacara bendera.",
    "Banyak sekolah mengadakan lomba dan upacara pada 17 Agustus.",
    "Dekorasi merah putih menghiasi jalan dan rumah warga.",
    "Banyak komunitas mengadakan pawai kemerdekaan.",
    "Bendera Merah Putih memiliki makna keberanian dan kesucian.",
    "17 Agustus menjadi momen refleksi perjuangan para pahlawan.",
    "Banyak film bertema kemerdekaan tayang di bulan Agustus.",
    "Karnaval kemerdekaan diadakan di berbagai kota.",
    "Banyak perusahaan mengadakan lomba untuk karyawan.",
    "Bendera Merah Putih harus dikibarkan dari pagi hingga sore.",
    "Banyak desa mengadakan lomba tarik tambang.",
    "Lomba lari membawa kelereng dengan sendok juga populer.",
    "Banyak warga membuat gapura bertema kemerdekaan.",
    "17 Agustus menjadi ajang mempererat persatuan.",
    "Banyak sekolah mengadakan lomba cerdas cermat kemerdekaan.",
    "Banyak keluarga berkumpul untuk merayakan kemerdekaan.",
    "Banyak organisasi pemuda aktif dalam perayaan 17 Agustus.",
    "Banyak daerah mengadakan lomba menghias sepeda.",
    "Banyak RT/RW mengadakan lomba memasak.",
    "Banyak anak-anak mengikuti lomba membawa bendera kecil.",
    "Banyak warga mengikuti lomba estafet air.",
    "Banyak komunitas mengadakan lomba fashion show kemerdekaan.",
    "Banyak sekolah mengadakan lomba pidato kemerdekaan.",
    "Banyak warga mengikuti lomba menangkap belut.",
    "Banyak desa mengadakan lomba memancing ikan.",
    "Banyak sekolah mengadakan lomba menggambar tema kemerdekaan.",
    "Banyak warga mengikuti lomba balap sandal.",
    "Banyak komunitas mengadakan lomba drama kemerdekaan.",
    "Banyak sekolah mengadakan lomba menulis puisi kemerdekaan.",
    "Banyak warga mengikuti lomba membawa bola dengan tali.",
    "Banyak desa mengadakan lomba tarik tambang antar RT.",
    "Banyak sekolah mengadakan lomba menyusun kata kemerdekaan.",
    "Banyak warga mengikuti lomba membawa air dengan gelas plastik.",
    "Banyak komunitas mengadakan lomba karaoke lagu kemerdekaan.",
    "Banyak sekolah mengadakan lomba membuat poster kemerdekaan.",
    "Banyak warga mengikuti lomba membawa koin dengan sumpit.",
    "Banyak desa mengadakan lomba lari karung berpasangan.",
    "Banyak sekolah mengadakan lomba membuat video kemerdekaan.",
    "Banyak warga mengikuti lomba membawa bola pingpong dengan sendok.",
    "Banyak komunitas mengadakan lomba menghias tumpeng kemerdekaan.",
    "Banyak sekolah mengadakan lomba membuat cerpen kemerdekaan.",
    "Banyak warga mengikuti lomba membawa telur dengan sendok.",
    "Banyak desa mengadakan lomba membawa air dengan botol.",
    "Banyak sekolah mengadakan lomba membuat vlog kemerdekaan."
]

# 60 pertanyaan tentang 17 Agustus
questions = [
    "Kapan Hari Kemerdekaan Indonesia diperingati?",
    "Siapa yang membacakan teks proklamasi kemerdekaan Indonesia?",
    "Di mana teks proklamasi pertama kali dibacakan?",
    "Apa warna bendera Indonesia?",
    "Apa makna warna merah pada bendera Indonesia?",
    "Apa makna warna putih pada bendera Indonesia?",
    "Apa saja lomba yang sering diadakan saat 17 Agustus?",
    "Apa tujuan diadakan lomba panjat pinang?",
    "Apa lagu kebangsaan Indonesia?",
    "Siapa saja yang menandatangani teks proklamasi?",
    "Apa arti penting 17 Agustus bagi bangsa Indonesia?",
    "Apa saja tradisi unik di daerahmu saat 17 Agustus?",
    "Mengapa upacara bendera penting diadakan?",
    "Apa isi dari teks proklamasi kemerdekaan?",
    "Siapa saja pahlawan nasional yang berperan dalam kemerdekaan?",
    "Apa saja lomba yang diadakan di sekolah saat 17 Agustus?",
    "Apa yang dilakukan Presiden pada 17 Agustus?",
    "Apa saja dekorasi yang biasa dipasang saat 17 Agustus?",
    "Apa tujuan diadakan pawai kemerdekaan?",
    "Apa saja lomba yang diadakan di lingkungan rumahmu?",
    "Mengapa 17 Agustus menjadi hari libur nasional?",
    "Apa saja lomba yang diadakan di kantor saat 17 Agustus?",
    "Apa saja lomba yang diadakan di desa saat 17 Agustus?",
    "Apa saja lomba yang diadakan di komunitasmu?",
    "Apa saja lomba yang diadakan di RT/RW saat 17 Agustus?",
    "Apa saja lomba yang diadakan di sekolah dasar saat 17 Agustus?",
    "Apa saja lomba yang diadakan di SMP/SMA saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk anak-anak saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk dewasa saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk keluarga saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk ibu-ibu saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk bapak-bapak saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk remaja saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk balita saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk lansia saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk guru saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk murid saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk pegawai saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk mahasiswa saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk dosen saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk komunitas pemuda saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk komunitas wanita saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk komunitas pria saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk komunitas anak-anak saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk komunitas dewasa saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk komunitas keluarga saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk komunitas ibu-ibu saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk komunitas bapak-bapak saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk komunitas remaja saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk komunitas balita saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk komunitas lansia saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk komunitas guru saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk komunitas murid saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk komunitas pegawai saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk komunitas mahasiswa saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk komunitas dosen saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk komunitas pemuda wanita saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk komunitas pemuda pria saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk komunitas pemuda anak-anak saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk komunitas pemuda dewasa saat 17 Agustus?",
    "Apa saja lomba yang diadakan untuk komunitas pemuda keluarga saat 17 Agustus?"
]

st.title("Chatbot Sederhana 17 Agustus")
st.write("Selamat datang di Chatbot 17 Agustus! Tanyakan apa saja tentang Hari Kemerdekaan Indonesia.")

st.subheader("Contoh pertanyaan yang bisa Anda ajukan:")
for q in questions[:10]:
    st.write(f"- {q}")

user_input = st.text_input("Masukkan pertanyaan Anda:")

if user_input:
    response = None
    for item in knowledge:
        if user_input.lower() in item.lower():
            response = item
            break
    if response:
        st.success(response)
    else:
        st.info("Maaf, pengetahuan belum tersedia. Silakan coba pertanyaan lain.")
