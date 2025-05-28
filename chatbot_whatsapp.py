from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def reply_whatsapp():
    incoming_msg = request.values.get("Body", "").lower()
    response = MessagingResponse()
    msg = response.message()

    if "apa itu teknik logistik" in incoming_msg:
        reply = "Teknik Logistik mempelajari aliran barang, informasi, dan sumber daya secara efisien."
    elif "mata kuliah" in incoming_msg:
        reply = "Mata kuliah: Manajemen Rantai Pasok, Sistem Transportasi, Pergudangan, dll."
    elif "prospek kerja" in incoming_msg:
        reply = "Lulusan bisa kerja di bidang logistik industri, transportasi, ekspor-impor, dll."
    elif "organisasi" in incoming_msg:
        reply = "Ada HMTL, BEM, dan UKM lainnya."
    elif "jadwal" in incoming_msg:
        reply = "Cek sistem informasi akademik kampus atau tanya dosen wali."
    elif "halo" in incoming_msg or "hai" in incoming_msg:
        reply = "Halo! Saya ChatBot Teknik Logistik. Mau tanya apa?"
    else:
        reply = "Maaf, saya belum mengerti. Coba tanya hal lain tentang Teknik Logistik."

    msg.body(reply)
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
