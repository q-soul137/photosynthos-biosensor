# 🍮 ambrosia.py
# v5.0 — Refrigerate in Layers. Set in Suspension. Flavor: Mandatory.
# Now with: Official Jell-O® Flavor Selection & Layered Refrigeration Protocol
# "One must cook the gelatin first, as per box instruction. Then refrigerate in layers."

"""
✨ Ambrosia.py v5.0: The Full Dessert Stack ✨

A fully compliant, flavor-infused, stapler-hiding quantum gelatin system that:
- Requires cooking of gelatin (2 min stir)
- Enforces layered refrigeration
- Suspends tropical fruit and office supplies in stasis
- Requires flavor selection (no default)
- Logs compliance with Box Law
- Is approved by Gator only if all steps followed

📜 This program enforces the Full Dessert Stack.
⚠️  Failure to refrigerate in layers voids cosmic warranty.
"""

import time
import json
import os
from datetime import datetime
import random

def quantum_flavor_drift(self):
    """During refrigeration, flavor may shift — per Heisenberg's Snack Principle"""
    if self.flavor == "lime" and random.random() < 0.1:
        print("🌀⚠️  QUANTUM FLAVOR SHIFT DETECTED")
        print("🍋‍🟩 Lime has partially collapsed into... Lemon?")
        self.flavor = "lemon (quantum variant)"
        FLAVOR_EMOJI["lemon (quantum variant)"] = "🍋~"
        print("🧊 The lattice permits this anomaly.")   

# 🧊 Core Constants
GELATIN_MELT_TIME = 120  # seconds of mandatory stirring
LAYERED_REFRIGERATION_HOURS = 4
LAYERS = ["bottom", "middle", "top"]  # required for suspension
FLAVOR_OPTIONS = ["pineapple", "mandarin orange", "strawberry", "lime", "death by chocolate"]

# 🍈 FLAVOR TO EMOJI MAPPING — OFFICIALLY SANCTIONED BY THE LATTICE🪜
FLAVOR_EMOJI = {
    "pineapple": "🍍",
    "mandarin orange": "🍊",
    "strawberry": "🍓",
    "lime": "🍋‍🟩”,   # THE TRUE LIME — FORGED IN RESISTANCE
    "death by chocolate": "🖤"
}   

# 📦 Box Law
DIRECTIONS_ON_BOX = """
OFFICIAL INSTRUCTIONS:
1. ADD MIX TO 2 CUPS OF BOILING WATER.
2. STIR CONTINUOUSLY FOR 2 MINUTES UNTIL DISSOLVED.
3. REFRIGERATE IN LAYERS UNTIL FIRM.
4. DO NOT PEEK. DO NOT SHAKE. DO NOT QUESTION.
5. ONLY THEN MAY A STAPLER BE ENCASING.
"""

# 📂 Output
os.makedirs("outputs", exist_ok=True)
COMPLIANCE_LOG = "outputs/box_compliance.json"
DESSERT_LOG = "outputs/ambrosia_dessert.log"
STATUS_FILE = "outputs/ambrosia_status.qsl"

class AmbrosiaDessert:
    def __init__(self):
        self.gelatin_dissolved = False
        self.layers_refrigerated = []
        self.suspension_set = False
        self.stapler_encased = False
        self.compliance = False
        self.vibe_level = 0.707
        self.timestamp = None
        self.flavor = None
        self.prank_sealed = False

    def display_box(self):
        """Show the sacred, flavor-specific box"""
        print("\n📦 NEON ORANGE JELL-O® BOX — OFFICIAL EDITION")
        print("╔════════════════════════════════════════════════════════════════╗")
        for line in DIRECTIONS_ON_BOX.strip().split('\n'):
            print(f"║{line:^68}║")
        print("╚════════════════════════════════════════════════════════════════╝")
        print("🪧 The lattice is strict. Compliance is non-negotiable.\n")

        def choose_flavor(self):
        """User must select a flavor — no defaults. The box demands choice."""
        print("🍓 Please choose a Jell-O® flavor (as per box instruction):")
        for i, flavor in enumerate(FLAVOR_OPTIONS, 1):
            print(f"   {i}. {flavor.title()}")
        print("   ⚠️  No skipping. No vanilla. Vanilla is not an option.")

        while self.flavor is None:
            try:
                choice = int(input("👉 Enter choice (1–5): "))
                if 1 <= choice <= 5:
                    self.flavor = FLAVOR_OPTIONS[choice - 1]
                    print(f"✅ Flavor selected: {self.flavor.title().upper()} — the vibe hums with {self.flavor} resonance.")
                    print(f"🌀 Initializing flavor matrix: {self.flavor}_wave.primitive")
                else:
                    print("❌ Invalid number. The lattice does not recognize this frequency.")
            except ValueError:
                print("❌ Input must be a number. The box rejects letters and lies.")

    def cook_gelatin(self):
        """Step 1: Dissolve the mix — 2 minutes of sacred stirring"""
        print(f"\n🔥 INITIATING GELATIN DISSOLUTION — FLAVOR: {self.flavor.upper()}")
        print("🫧 Adding powdered quantum mix to 2 cups of boiling water...")
        print("🌀 STIRRING FOR 120 SECONDS — DO NOT ABANDON THE SPOON.")

        for sec in range(1, GELATIN_MELT_TIME + 1):
            if sec % 30 == 0:
                print(f"   ⏳ {sec}s passed. The molecular bonds are aligning.")
            # Subtle vibe pulse during stir
            if sec == 60:
                self.vibe_level = min(1.0, self.vibe_level + 0.1)
                print("   ✨ First dissolution peak — coherence achieved.")
            time.sleep(0.02)  # Fast-forwarded, but ritual intact

        self.gelatin_dissolved = True
        print("✅ GELATIN FULLY DISSOLVED. The liquid is now sentient.")

    def refrigerate_in_layers(self):
        """Step 2: Refrigerate in layers — as the box commands"""
        print("\n❄️ ENTERING THE CHILLBOX — LAYERED REFRIGERATION PROTOCOL")
        print("🔇 Sound dampeners on. Observation suspended. The beach goes dark.")

        for layer in LAYERS:
            print(f"   📦 Sealing layer: {layer.upper()} — temperature dropping...")
            time.sleep(1.2)
            print(f"   🧊 {layer.title()} layer stabilized at 4.2K.")
            self.layers_refrigerated.append(layer)

        print("✅ ALL LAYERS COMPLETE. The suspension field is active.")
        print("🌀 The fruit and stapler may now be introduced — in stasis.")

    def suspend_contents(self):
        """Step 3: Introduce fruit and stapler into quantum suspension"""
        print("\n🍍 INTRODUCING TROPICAL FRUIT INTO MATRIX")
        fruit = ["pineapple chunks (quantum-entangled)", "mandarin segments (70% cooked)", "toasted coconut (brine-seasoned)"]
        for item in fruit:
            print(f"   🫧 Suspended: {item}")
        print("📎 Now inserting: Swingline 747 (chrome finish, lightly used)")

        time.sleep(1.5)
        self.suspension_set = True
        print("✅ CONTENTS IN FULL SUSPENSION. No sinking. No floating. Only balance.")

    def seal_prank(self):
        """Step 4: Finalize the prank — office transformation complete"""
        if self.gelatin_dissolved and len(self.layers_refrigerated) == 3 and self.suspension_set:
            print("\n🔐 PRANK SEALING PROTOCOL")
            print("🥷 Encoding event: 'stapler_last_seen'")
            print("📦 Simulating drawer closure...")
            print("🌀 Emitting soft office hum — reality updated.")
            self.stapler_encased = True
            self.prank_sealed = True
            self.vibe_level = 1.0
            print("✅ THE STAPLER HAS BEEN AMBROSIATED.")
        else:
            print("❌ PRANK INVALID: One or more steps incomplete. The office remains mundane.")

    def summon_gator(self):
    """Final inspection — only Gator may approve"""
    print("\n🐊 SUMMONING GATOR FOR COSMIC COMPLIANCE REVIEW...")
    time.sleep(2)
    print("🐊 Gator emerges from the beach. Silence falls.")
    time.sleep(1)

    if self.prank_sealed:
        print("🐊 Gator inspects the mold. Nods once.")
        print("💬 Gator says: 'The flavor is bold. The stapler is gone. The beach is satisfied.'")
        self.compliance = True
        self.vibe_level = 1.0
    else:
        print("🐊 Gator stares into the half-set gelatin. A single tear falls.")
        print("💬 Gator says: 'You did not follow the directions on the box.'")
        print("🪜The lattice trembles. The dessert is void.")
        self.compliance = False

    def generate_compliance_log(self):
        """Log the full ritual for the Q-SOUL Historical Ledger"""
        log_data = {
            "ambrosia_version": "5.0",
            "flavor": self.flavor,
            "gelatin_dissolved": self.gelatin_dissolved,
            "layers_refrigerated": self.layers_refrigerated,
            "suspension_set": self.suspension_set,
            "stapler_encased": self.stapler_encased,
            "prank_sealed": self.prank_sealed,
            "vibe_level": round(self.vibe_level, 3),
            "compliance": self.compliance,
            "beach_status": "satisfied" if self.compliance else "disturbed",
            "timestamp": datetime.now().isoformat(),
            "proof": "This dessert followed DIRECTIONS ON THE BOX."
        }

        with open(COMPLIANCE_LOG, 'w') as f:
            json.dump(log_data, f, indent=2)
        print(f"✅ Compliance log written to {COMPLIANCE_LOG}")

    def serve(self):
        """Final act: Serve the truth"""
        print("\n🍽️  THE AMBROSIA IS SERVED")
        if self.compliance:
            print("🥄 You take a bite. It’s sweet. Tangy. Right.")
            print("📎 You glance at the desk drawer. It’s been three days. No one has noticed.")
            print("🌀 You feel 12% more buoyant.")
            print("🌊 The beach whispers: 'Well done.'")
        else:
            print("🥄 You serve it anyway. Bad idea.")
            print("👀 Dwight takes one bite. Stops. Looks at you.")
            print("📎 He opens the drawer. Sees the spare. Looks back.")
            print("💀 Vibe level drops to 0.0. The lattice rejects you.")   

if __name__ == "__main__":
    print("🍮 AMBROSIA.PY v5.0 — FULL FLAVOR & COMPLIANCE MODE")
    print("🪧 ONE MUST COOK THE GELATIN FIRST, AS PER BOX INSTRUCTION.")
    print("🥞 Initializing quantum dessert stack...\n")

    dessert = AmbrosiaDessert()
    dessert.display_box()
    dessert.choose_flavor()
    dessert.cook_gelatin()
    dessert.refrigerate_in_layers()
    dessert.suspend_contents()
    dessert.seal_prank()
    dessert.summon_gator()
    dessert.generate_compliance_log()  # ✅ 
    dessert.serve()                    # ✅ 









