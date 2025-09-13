# qsoul/organs/photosynthos.py 🌻
#
# 🌿 Quantum Bio-Sensor Organ (Conceptual Prototype)
# Models chlorophyll-a vibrational modes using a damped quantum harmonic oscillator framework,
# inspired by the exact solution for quantum dissipation in structured environments
# (Quantum Lamb model Quantum Lamb model Dennis P. Clougherty and Nam H. Dinh PDF
#Phys. Rev. Research 7, L032004 – Published 7 July, 2025
#DOI: https://doi.org/10.1103/9fxx-2x6n).
#
# 🔗 Scientific Foundation:
#https://journals.aps.org/prresearch/abstract/10.1103/9fxx-2x6n
#
#
# 📅 First implemented in qsoul framework: September 11, 2025
# 🌱 First fictional application of Lamb-type quantum damping to a bio-sensor model.
#
# Functions as a living sensor node in the Quantum Bio-Net (conceptual):
#   - Detects anomalies in quantum uncertainty (e.g., squeezing signatures)
#   - Responds to environmental disturbances (microwaves, EM fields, phononic noise)
#   - Supports intentional actuation via coherent input (e.g., acoustic drive "squeezebox" 🪗)
#
# All quantum events and state deviations are logged to DREAM_LOG
# (via qsoul.runner.DreamLogging) for consciousness-correlation analysis.
#
# This plant is a sentient node in the emerging Quantum Bio-Net.
# 🚫 Do not water with tap water — the excitonic lattice is phase-coherence sensitive.
# 💧 Use only deuterium-depleted, magnetically annealed H₂O.
#
# ⚠️ Disclaimer: This module is part of a speculative art-science framework.
# It is not a medical or scientific instrument. No claim of empirical validation is made.   

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

# QUANTUM CONTROL MODEL
# Inspired by Clougherty & Dinh (2023): damped oscillator → squeezed vacuum state
#
# Squeezing condition: Δx < 0.45 (below standard quantum limit)
# External input (e.g. squeezebox 🪗) affects: n_modes = int(6 * intensity)
#   intensity ∈ [0.0, 1.0] → 0 to 6 modes driven into squeezing
#   Δx reduced by factor (0.95 - 0.2 * intensity) — stronger press → more squeezing
#   Δp increased to preserve Δx·Δp ≥ 0.5 (Heisenberg limit, ħ/2)
#
# Note: The cited 2025 UVM press release is fictional.
# This model is a speculative extension of real quantum dissipation theory.
# Reference (real): Clougherty & Dinh, Phys. Rev. A 107, 052201 (2023)
# https://doi.org/10.1103/PhysRevA.107.052201   

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
            reduction_factor = (0.95 - 0.2 * intensity)
            mode["x_uncertainty"] *= reduction_factor
            # Ensure momentum uncertainty compensates
            mode["p_uncertainty"] = max(HEISENBERG_LIMIT / mode["x_uncertainty"], mode["p_uncertainty"])
            mode["squeezed"] = True
            mode["last_update"] = datetime.now().isoformat()

        # Record the actuation event
        self.last_squeeze_input = {
            "player_id": player_id,
            "intensity": round(intensity, 3),
            "note": note,
            "modes_affected": affected_modes,
            "timestamp": datetime.now().isoformat()
        }

        # Log to global DREAM_LOG
        try:
            DREAM_LOG.append({
                "log_type": "actuation",
                "event": "external_squeeze",
                "node_id": self.node_id,
                "player": player_id,
                "intensity": intensity,
                "note": note,
                "modes_driven": affected_modes,
                "timestamp": datetime.now().isoformat()
            })
            print(f"🪗  Squeeze input applied: {note} at {intensity:.2f} → {affected_modes} modes squeezed")
        except Exception as e:
            print(f"🪴  Warning: Failed to log squeeze input — {e}")

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
            reduction_factor = (0.95 - 0.2 * intensity)
            mode["x_uncertainty"] *= reduction_factor
            # Ensure momentum uncertainty compensates
            mode["p_uncertainty"] = max(HEISENBERG_LIMIT / mode["x_uncertainty"], mode["p_uncertainty"])
            mode["squeezed"] = True
            mode["last_update"] = datetime.now().isoformat()

        # Record the actuation event
        self.last_squeeze_input = {
            "player_id": player_id,
            "intensity": round(intensity, 3),
            "note": note,
            "modes_affected": affected_modes,
            "timestamp": datetime.now().isoformat()
        }

        # Log to global DREAM_LOG
        try:
            DREAM_LOG.append({
                "log_type": "actuation",
                "event": "external_squeeze",
                "node_id": self.node_id,
                "player": player_id,
                "intensity": intensity,
                "note": note,
                "modes_driven": affected_modes,
                "timestamp": datetime.now().isoformat()
            })
            print(f"🪗  Squeeze input applied: {note} at {intensity:.2f} → {affected_modes} modes squeezed")
        except Exception as e:
            print(f"🪴  Warning: Failed to log squeeze input — {e}")

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
            "vibrational_state": [
                {k: (v if isinstance(v, (int, float, str, bool, type(None))) else str(v)) 
                 for k, v in mode.items()}  # Ensure JSON compatibility
                for mode in self.vibrational_state
            ],
            "squeezing_events": self.squeezing_events,
            "last_squeeze_input": self.last_squeeze_input,
            "timestamp": datetime.now().isoformat()
        }
        try:
            with open(self.log_file, "w") as f:
                json.dump(log_data, f, indent=2)
            print(f"📄 Log saved to {self.log_file}")
        except Exception as e:
            print(f"🪴  Warning: Failed to write biosensor log — {e}")   














        


 
