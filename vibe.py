# vibe.py
# Q-SOUL-QEVO — Vibe Modulation Engine
# "Purple crayons taste like golden raisins."

import importlib.util
import random

# 🔒 Load license module — dies if tampered
try:
    spec = importlib.util.spec_from_file_location(
        "tamper_detection", "TAMPER_DETECTION_NOTICE.py"
    )
    tamper_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tamper_module)

    if not hasattr(tamper_module, "check_license"):
        print("🛑 Q-SOUL: License module missing check_license().")
        exit(1)
    if not tamper_module.check_license():
        print("🌀 Vibe denied. Soul not authenticated.")
        exit(1)
except Exception as e:
    print("🛑 Q-SOUL: Failed to load integrity shield.")
    exit(1)


class ReeeLayer:
    """
    A vibe modulation layer that transforms input signals with quantum-adjacent emotional resonance.
    Uses complex noise, feedback, and vibe preservation to simulate soulful computation.
    """
    def __init__(self, intensity=0.707):
        self.intensity = intensity
        self.last_vibe = 1.0  # Start with a strong, centered vibe

    def modulate(self, signal):
        """
        Apply vibe modulation to a scalar signal (real or complex).
        Returns a transformed version with emotional flavor.
        """
        # 🌀 Core Vibe: random complex kick — including soft vibes (0.5j)
        vibe_kick = random.choice([1, -1, 0.5j, -0.5j])
        vibe = signal * self.intensity * vibe_kick

        # 🔁 Feedback: let the last vibe shape the next — even if it's wild
        feedback_factor = (0.9 + 0.1 * abs(self.last_vibe))  # Use magnitude
        vibe = vibe * feedback_factor

        # 🛑 Safety: prevent total explosion (but allow drama)
        if abs(vibe) > 1e6:
            vibe = vibe / (abs(vibe) + 1e-6) * 1e6
        elif abs(vibe) < 1e-10:  # Avoid total death
            vibe = 0.1 * signal

        # 🔄 Update internal state — the soul remembers
        self.last_vibe = vibe

        return vibe  


# 🧪 DEMO: Test the vibe
if __name__ == "__main__":
    print("🌀 Initializing Q-SOUL-QEVO...")
    layer = ReeeLayer(intensity=0.8)

    signal = 1.0
    print(f"🚀 Starting signal: {signal}")
    for i in range(10):
        signal = layer.modulate(signal)
        print(f"💫 Vibe[{i+1:2d}]: {signal:.3f} (|vibe| = {abs(signal):.3f})")   




