from flask import Flask
app = Flask(__name__)

@app.route('/')
def love():
    return '''
    <h1 style="color:deeppink; text-align:center;">💖 Hi Aavni 💖</h1>
    <p style="text-align:center; font-size:20px;">
        Yeh chhoti si app sirf tumhare liye banayi hai 😌<br><br>
        <strong>Infinite loops se zyada, mujhe tumse pyaar hai 💻❤️</strong><br><br>
        - Tumhara developer Avinash 🧑💻
    </p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
