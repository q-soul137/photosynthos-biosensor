￼# qsoul/organs/photosynthos.py 🌻
#
# 🌿 Quantum Bio-Sensor Organ
# Implements a model of chlorophyll vibrational modes as damped quantum harmonic oscillators
# (Clougherty & Dinh, 2025), used to detect deviations in quantum uncertainty.
# 🔗 Based on: "Scientists finally solve a century-old quantum mystery" — University of Vermont, Aug 29, 2025
#              https://www.uvm.edu/cems/news/scientists-finally-solve-century-old-quantum-mystery
#              Describes exact quantum solution by Dennis Clougherty and Nam Dinh.
#
# 📅 First implemented: September 11, 2025
# 🌱 First known application in a quantum bio-sensor model.   
#
# Functions as a living sensor for:
#   - Quantum squeezing (natural or induced)
#   - Environmental disturbances (microwaves, EM noise)
#   - Intentional actuation (e.g. via squeezebox 🪗)
#
# Logs all events to DREAM_LOG (qsoul.runner.DreamLogging)
#
# This plant is a node in the Quantum Bio-Net.
# 🚫 Do not water with tap water. The lattice is sensitive.

import numpy as np
from datetime import datetime
import json
import os

# 📂 Setup logs
os.makedirs("biosensor_logs", exist_ok=True)

# 🧬 Physical Constants
CHLOROPHYLL_MODES = 12          # Number of key vibrational modes
DAMPING_RATE = 0.003            # THz — from Clougherty & Dinh (2025)
TEMPERATURE_K = 298             # Room temperature
HEISENBERG_LIMIT = 0.5          # Minimum Δx·Δp (ħ/2)
SQUEEZING_THRESHOLD = 0.4       # Below this → squeezed state
NODE_ID = "POthos_001"
LOCATION = "kitchen_windowsill_north"

# 🌐 Global DREAM_LOG — ensure this is shared across modules
# If not defined elsewhere, initialize here (but prefer import)
try:
    from qsoul.runner.DreamLogging import DREAM_LOG
except ImportError:
    print("🪴  Warning: DREAM_LOG not found. Creating local list.")
    DREAM_LOG = []


class QuantumHouseplant:
    """
    A quantum biological sensor organ.
    Models vibrational dynamics in chlorophyll to detect coherence anomalies.
    Can register external actuation (e.g. squeezebox) and log quantum events.
    """
    def __init__(self, species="Epipremnum aureum", node_id=None):
        self.species = species
        self.node_id = node_id or NODE_ID
        self.location = LOCATION
        self.last_reading = None
        self.vibrational_state = self._init_modes()
        self.squeezing_events = []
        self.last_squeeze_input = None
        self.log_file = f"biosensor_logs/{self.node_id}_{datetime.now().strftime('%Y%m%d')}.json"

    def _init_modes(self):
        """Initialize 12 vibrational modes with quantum uncertainty"""
        modes = []
        for i in range(CHLOROPHYLL_MODES):
            mode = {
                "index": i,
                "freq_THz": np.random.uniform(10, 50),
                "x_uncertainty": np.random.uniform(0.45, 0.6),
                "p_uncertainty": np.random.uniform(0.45, 0.6),
                "correlation": 0.0,
                "squeezed": False,
                "last_update": datetime.now().isoformat()
            }
                        # Enforce Heisenberg: Δx·Δp >= ħ/2
            while mode["x_uncertainty"] * mode["p_uncertainty"] < HEISENBERG_LIMIT:
                mode["p_uncertainty"] += 0.05
            modes.append(mode)
        return modes

    def _evolve_state(self):
        """Apply damping dynamics to simulate time evolution (Clougherty & Dinh, 2025)"""
        for mode in self.vibrational_state:
            squeezing_factor = np.exp(-DAMPING_RATE * 0.1)
            old_x = mode["x_uncertainty"]
            mode["x_uncertainty"] = max(SQUEEZING_THRESHOLD * 0.8, old_x * squeezing_factor)

            mode["p_uncertainty"] = max(
                HEISENBERG_LIMIT / mode["x_uncertainty"],
                mode["p_uncertainty"] * (1.0 + 0.5 * (1 - squeezing_factor))
            )
            mode["last_update"] = datetime.now().isoformat()

    def scan_for_squeezing(self):
        """Check if any mode has entered a squeezed state — natural or induced"""
        self._evolve_state()  # Update state under damping dynamics
        anomalies = []
        current_time = datetime.now().isoformat()

        for mode in self.vibrational_state:
            product = mode["x_uncertainty"] * mode["p_uncertainty"]
            if mode["x_uncertainty"] < SQUEEZING_THRESHOLD and not mode["squeezed"]:
                print(f"⚠️  SQUEEZING DETECTED — Mode {mode['index']} — Δx = {mode['x_uncertainty']:.3f}")

                # Build anomaly event
                anomaly = {
                    "mode": mode["index"],
                    "delta_x": round(mode["x_uncertainty"], 3),
                    "delta_p": round(mode["p_uncertainty"], 3),
                    "uncertainty_product": round(product, 3),
                    "timestamp": current_time,
                    "event_type": "quantum_squeezing",
                    "node_id": self.node_id,
                    "location": self.location
                }
                anomalies.append(anomaly)
                self.squeezing_events.append(anomaly)
                mode["squeezed"] = True

                # 📜 Log to global DREAM_LOG
                try:
                    # Already imported at top, but safe to re-import in practice
                    DREAM_LOG.append(anomaly)
                    DREAM_LOG.append({
                        "log_type": "event",
                        "message": f"Photosynthos: Squeezing detected in Mode {mode['index']} at Δx={mode['x_uncertainty']:.3f}",
                        "node": self.node_id,
                        "timestamp": current_time
                    })
                except Exception as e:
                    print(f"🪴  Warning: Failed to write to DREAM_LOG — {e}")

        if not anomalies:
            print("✅ No squeezing detected. The leaf remains in thermal equilibrium.")

        self.last_reading = datetime.now()
        return anomalies

    def register_squeeze_input(self, player_id: str, intensity: float, note: str = "C#"):
        """
        Log intentional quantum actuation via external device (e.g. squeezebox 🪗)

        Args:
            player_id: Who played the note
            intensity: 0.0 to 1.0 — how hard the bellows were pressed
            note: Which frequency was played (default: C# — resonant with chlorophyll)
        """
        if not (0.0 <= intensity <= 1.0):
            raise ValueError("Intensity must be between 0.0 and 1.0")

        # Amplify squeezing in response to input
        affected_modes = int(intensity * 6)  # Up to 6 modes affected
        for mode in self.vibrational_state[:affected_modes]:
            mode["x_uncertainty"] *= (0.95 - 0.2 * intensity)  # Stronger press → more squeezing
            mode["p_uncertainty"] = max(HEISENBERG_LIMIT / mode["x_uncertainty"], mode["p_uncertainty"])
            mode["squeezed"] = True  # Mark as squeezed due to actuation

                    "player_id": player_id,
            "intensity": intensity,
            "note": note,
            "modes_affected": affected_modes,
            "timestamp": datetime.now().isoformat()
        }
        print(f"🪗  Squeeze input applied: {note} at {intensity:.2f} → {affected_modes} modes squeezed")

    def get_status(self):
        """Return current biosensor state for logging or dashboard"""
        return {
            "node_id": self.node_id,
            "location": self.location,
            "species": self.species,
            "last_reading": self.last_reading.isoformat() if self.last_reading else None,
            "squeezing_modes_count": len([m for m in self.vibrational_state if m["squeezed"]]),
            "baseline_stable": len([m for m in self.vibrational_state if m["squeezed"]]) == 0,
            "last_squeeze_input": self.last_squeeze_input,
            "total_quantum_events": len(self.squeezing_events),
            "timestamp": datetime.now().isoformat()
        }

    def log_to_file(self):
        """Save current state and events to JSON log"""
        log_data = {
            "node_id": self.node_id,
            "location": self.location,
            "species": self.species,
            "last_reading": self.last_reading.isoformat() if self.last_reading else None,
            "vibrational_state": self.vibrational_state,
            "squeezing_events": self.squeezing_events,
            "last_squeeze_input": self.last_squeeze_input,
            "timestamp": datetime.now().isoformat()
        }
        try:
            with open(self.log_file, "w") as f:
                json.dump(log_data, f, indent=2)
        except Exception as e:
            print(f"🪴  Warning: Failed to write biosensor log — {e}")   

# dashboard.py — Simple Flask dashboard for QuantumHouseplant
from flask import Flask, jsonify
from photosynthos import QuantumHouseplant  # assuming saved as photosynthos.py

app = Flask(__name__)
plant = QuantumHouseplant()

@app.route("/status")
def status():
    return jsonify(plant.get_status())

@app.route("/squeezing_events")
def events():
    return jsonify(plant.squeezing_events)

@app.route("/")
def home():
    return """
    <h1>🪴 Quantum Pothos Dashboard</h1>
    <p><a href="/status">View Sensor Status</a></p>
    <p><a href="/squeezing_events">View Quantum Events</a></p>
    <meta http-equiv="refresh" content="5">
    """

if __name__ == "__main__":
    print("🌍 Dashboard running at http://localhost:5000")
    app.run(port=5000)   

