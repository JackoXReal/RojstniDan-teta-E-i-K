import os
from flask import Flask, render_template_string

app = Flask(__name__)

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
            font-family: 'Segoe UI', sans-serif;
            /* Zamenjane barve: Roza/Vijolična gradient */
            background: linear-gradient(135deg, #f093fb, #f5576c);
            color: white;
            overflow: hidden;
        }

        .container {
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 20px;
        }

        .card {
            background: rgba(255,255,255,0.2);
            backdrop-filter: blur(14px);
            border-radius: 25px;
            padding: 40px 30px;
            max-width: 450px;
            box-shadow: 0 25px 50px rgba(0,0,0,0.2);
            animation: fadeIn 2s ease;
            border: 1px solid rgba(255,255,255,0.3);
        }

        h1 {
            font-size: 2.2em;
            margin-bottom: 10px;
            animation: float 3s ease-in-out infinite;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }

        h2 {
            font-weight: 400;
            margin-bottom: 25px;
            font-size: 1.4em;
        }

        p {
            font-size: 1.15em;
            line-height: 1.6;
        }

        .money {
            margin: 25px 0;
            font-size: 1.2em;
            font-weight: bold;
            color: #fff;
            background-color: rgba(0,0,0,0.1);
            padding: 10px;
            border-radius: 15px;
        }

        button {
            margin-top: 25px;
            padding: 15px 35px;
            font-size: 1.1em;
            border: none;
            border-radius: 30px;
            /* Zamenjana barva gumba */
            background: #ffffff;
            color: #f5576c;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }

        button:hover {
            background: #ffe2e6;
            transform: scale(1.08);
        }

        footer {
            margin-top: 30px;
            font-size: 1em;
            opacity: 0.9;
        }

        /* Animacije */
        @keyframes fadeIn {
            from { opacity: 0; transform: scale(0.9); }
            to { opacity: 1; transform: scale(1); }
        }

        @keyframes float {
            0% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0); }
        }

        /* Confetti */
        .confetti {
            position: absolute;
            width: 10px;
            height: 10px;
            background: red;
            top: -10px;
            animation: fall linear infinite;
        }

        @keyframes fall {
            to {
                transform: translateY(110vh) rotate(360deg);
            }
        }

        .music {
            margin-top: 15px;
            font-size: 0.95em;
            opacity: 0.85;
        }
    </style>
</head>
<body>

<audio id="bgMusic" src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"></audio>
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
            vasiot onuk Jacko 💙
        </footer>
    </div>
</div>

<script>
    function celebrate() {
        const music = document.getElementById("bgMusic");
        
        // Preverimo, če glasba obstaja, preden jo predvajamo
        if(music) {
            music.volume = 0.5;
            music.play().catch(error => console.log("Audio play failed (user interaction required or no source):", error));
        }

        // Množina v alert oknu
        alert("Ve sakam teti! ❤️ Srekjen 41-vi rodenden! 🎉");
        createConfetti();
    }

    // Confetti
    function createConfetti() {
        const colors = ['#ff0a54', '#ff477e', '#ff7096', '#ff85a1', '#fbb1bd', '#f9bec7'];
        
        for (let i = 0; i < 100; i++) {
            const conf = document.createElement("div");
            conf.classList.add("confetti");
            conf.style.left = Math.random() * 100 + "vw";
            // Uporabi roza/rdeče barve za konfete
            conf.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
            conf.style.animationDuration = (Math.random() * 3 + 2) + "s";
            document.body.appendChild(conf);

            setTimeout(() => conf.remove(), 5000);
        }
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
