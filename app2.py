import os
from flask import Flask, render_template_string, send_from_directory

app = Flask(__name__)

# Potrebno za pravilno predvajanje glasbe na Renderju
@app.route('/music.mp3')
def serve_music():
    return send_from_directory('.', 'music.mp3')

HTML = """
<!DOCTYPE html>
<html lang="mk">
<head>
    <meta charset="UTF-8">
    <title>Srekjen Rodenden Teti 🎉</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow-x: hidden;
        }

        .container {
            width: 100%;
            padding: 20px;
            box-sizing: border-box;
            z-index: 2;
        }

        .card {
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            border-radius: 30px;
            padding: 50px 30px;
            max-width: 450px;
            margin: 0 auto;
            box-shadow: 0 20px 40px rgba(0,0,0,0.25);
            animation: fadeIn 1.5s ease-out;
            border: 1px solid rgba(255, 255, 255, 0.3);
            text-align: center;
        }

        h1 {
            font-size: 2.5em;
            margin-bottom: 15px;
            animation: float 3s ease-in-out infinite;
            text-shadow: 2px 4px 8px rgba(0,0,0,0.2);
        }

        h2 {
            font-weight: 400;
            margin-bottom: 30px;
            font-size: 1.5em;
            opacity: 0.95;
        }

        p {
            font-size: 1.2em;
            line-height: 1.7;
            margin-bottom: 20px;
        }

        button {
            margin-top: 15px;
            padding: 16px 40px;
            font-size: 1.2em;
            border: none;
            border-radius: 50px;
            background: #ffffff;
            color: #f5576c;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 10px 20px rgba(0,0,0,0.15);
        }

        button:hover {
            background: #ffffff;
            transform: translateY(-3px) scale(1.05);
            box-shadow: 0 15px 25px rgba(0,0,0,0.2);
        }

        button:active {
            transform: translateY(0);
        }

        .music {
            margin-top: 25px;
            font-size: 0.9em;
            opacity: 0.8;
            letter-spacing: 1px;
        }

        footer {
            margin-top: 40px;
            font-size: 1.1em;
            border-top: 1px solid rgba(255,255,255,0.2);
            padding-top: 20px;
        }

        /* Konfeti stil */
        .confetti {
            position: fixed;
            z-index: 1;
            top: -10px;
            user-select: none;
            pointer-events: none;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-15px); }
        }

        @keyframes fall {
            0% { transform: translateY(0) rotate(0deg); opacity: 1; }
            100% { transform: translateY(100vh) rotate(720deg); opacity: 0; }
        }
    </style>
</head>
<body>

<audio id="bgMusic" src="/music.mp3"></audio>

<div class="container">
    <div class="card">
        <h1>🎂 Srekjen Rodenden Teti!</h1>
        <h2>Denes polnite 41 godini 🥳</h2>

        <p>
            Vi posakuvam mnogu zdravje, srekja i ubavi momenti.<br>
        </p>

        <button onclick="celebrate()">Kliknete ovde ❤️</button>

        <div class="music">
            🎶 Muzika vo pozadina
        </div>

        <footer>
            So mnogu ljubov,<br>
            <strong>vasiot onuk Jacko 💙</strong>
        </footer>
    </div>
</div>

<script>
    function celebrate() {
        const music = document.getElementById("bgMusic");
        
        if(music) {
            music.volume = 0.5;
            music.play().catch(e => console.log("Audio Error:", e));
        }

        alert("Ve sakam teti! ❤️ Srekjen 41-vi rodenden! 🎉");
        
        for(let i=0; i<100; i++) {
            createConfetti();
        }
    }

    function createConfetti() {
        const colors = ['#ff0a54', '#ff477e', '#ff7096', '#ff85a1', '#fbb1bd', '#f9bec7', '#ffd700'];
        const conf = document.createElement("div");
        conf.classList.add("confetti");
        
        // Naključne lastnosti
        const size = Math.random() * 10 + 5 + "px";
        conf.style.width = size;
        conf.style.height = (Math.random() > 0.5 ? size : (Math.random() * 5 + 2 + "px")); // Različne oblike
        conf.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        conf.style.left = Math.random() * 100 + "vw";
        conf.style.borderRadius = Math.random() > 0.5 ? "50%" : "2px";
        
        // Animacija
        const duration = Math.random() * 3 + 2;
        conf.style.animation = `fall ${duration}s linear forwards`;
        
        document.body.appendChild(conf);
        setTimeout(() => conf.remove(), duration * 1000);
    }
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


