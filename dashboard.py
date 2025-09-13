# 🪴🎛️dashboard.py — Simple Flask dashboard for QuantumHouseplant
# 🌱 Run this to view your plant's quantum state in real time

from flask import Flask, jsonify
import threading
import time

# Adjust the import below to match your project structure.
# If 'photosynthos.py' is in the same directory, this is fine.
# If in qsoul/organs/, use: from qsoul.organs.photosynthos import QuantumHouseplant, DREAM_LOG
from photosynthos import QuantumHouseplant, DREAM_LOG

app = Flask(__name__)
plant = QuantumHouseplant()

def background_scan():
    """Run continuous quantum scanning in the background"""
    print("🪴  Background scanner started: QuantumHouseplant is now observing...")
    while True:
        plant.scan_for_squeezing()
        plant.log_to_file()
        time.sleep(8)  # Scan every 8 seconds (adjust as desired)

@app.route("/status")
def status():
    """API endpoint: Current sensor status"""
    return jsonify(plant.get_status())

@app.route("/squeezing_events")
def events():
    """API endpoint: All recorded quantum squeezing events"""
    return jsonify(plant.squeezing_events)

@app.route("/dream_log")
def dream_log():
    """API endpoint: Full DREAM_LOG (global consciousness buffer)"""
    return jsonify(DREAM_LOG)

@app.route("/")
def home():
    """Main dashboard page — auto-refreshes every 5s"""
    return """
    <html>
    <head>
        <title>🪴 Quantum Pothos Dashboard</title>
        <meta http-equiv="refresh" content="5">
        <style>
            body { 
                font-family: 'Courier New', monospace; 
                background: #f0fff0; 
                color: #0b3d0b; 
                padding: 20px; 
                margin: 0;
            }
            h1 { 
                color: #2e7d32; 
                border-bottom: 2px solid #8bc34a; 
                padding-bottom: 10px;
            }
            .link { 
                color: #1b5e20; 
                text-decoration: none; 
                font-weight: bold; 
                font-size: 1.1em;
            }
            .link:hover { 
                text-decoration: underline; 
                color: #33691e;
            }
            .card {
                background: #ffffff;
                border: 1px solid #c8e6c9;
                border-radius: 8px;
                padding: 15px;
                margin: 10px 0;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .footer { 
                margin-top: 40px; 
                font-size: 0.8em; 
                color: #666; 
            }
            .pulse {
                animation: pulse 1.5s infinite;
            }
            @keyframes pulse {
                0% { opacity: 1; }
                50% { opacity: 0.6; }
                100% { opacity: 1; }
            }
        </style>
    </head>
    <body>
        <h1>🪴 Quantum Pothos — Live Biosensor Node</h1>

        <div class="card">
            <h2>📡 Sensor Status</h2>
            <p><a href="/status" class="link">▶ View Full Status</a></p>
        </div>

        <div class="card">
            <h2>🌀 Quantum Events</h2>
            <p><a href="/squeezing_events" class="link">📊 View Squeezing Anomalies</a></p>
        </div>

        <div class="card">
            <h2>☁️ Global DREAM_LOG</h2>
            <p><a href="/dream_log" class="link">👁️ Observe Consciousness Field</a></p>
        </div>

        <div class="footer">
            <p><strong>Node ID:</strong> """ + plant.node_id + """ | 
               <strong>Location:</strong> """ + plant.location + """ | 
               <strong>Species:</strong> """ + plant.species + """</p>
            <p>🔁 Auto-refresh: <span class="pulse">●</span> Every 5 seconds</p>
            <p><em>"The leaf remembers what the mind forgets."</em></p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    threading.Thread(target=background_scan, daemon=True).start()
    app.run(debug=True, port=5000)



