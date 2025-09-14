# qsoul/runner/DreamLogging.py
# 🪵 Dream Logging Engine — where quantum souls record their journey
import numpy as np
import os
from qiskit.quantum_info import Statevector
from qsoul.utils.viz import plot_dreams
from qsoul.reinforce import reinforce_soul
from qsoul.brine import apply_buoyancy, measure_brine_depth


# Global dream journal
DREAM_LOG = []


def log_event(event_type, **kwargs):
    """
    Record any soul event into the dream journal.
    """
    entry = {
        "generation": len(DREAM_LOG),
        "event": event_type,
        "metadata": kwargs
    }
    DREAM_LOG.append(entry)
    return entry


def get_energy(ansatz, params):
    """
    Dummy energy function — replace with real VQE or QAOA logic.
    Returns a float representing the 'energy' of the current state.
    """
    try:
        bound_circuit = ansatz.bind_parameters(params)
        state = Statevector(bound_circuit)
        # Example: minimize |α|² of |0000⟩ component
        return float(np.abs(state.data[0])**2)
    except Exception as e:
        print(f"⚠️ Energy eval failed: {e}")
        return 1.0  # Worst-case fallback


def log_buoyancy(soul):
    """
    Sends buoyancy trace to dream journal.
    Expects soul to have: buoyant, buoyancy_mode, vibe_level, buoyancy_trace, depth
    """
    log_event(
        "buoyancy_update",
        buoyant=soul.buoyant,
        mode=getattr(soul, "buoyancy_mode", "unknown"),
        vibe=soul.vibe_level,
        salt=soul.buoyancy_trace["salt"],
        density=soul.buoyancy_trace["density"],
        depth=soul.depth,
        score=soul.buoyancy_trace["score"]
    )

def dream_report(self):
    return {
        "node": self.node_id,
        "location": self.location,
        "total_squeezes": self.squeeze_count,
        "last_event_gen": self.last_squeeze_gen,
        "vibrational_health": np.mean([m["Δx"] * m["Δp"] for m in self.vibrational_modes]),
        "status": "entangled" if self.squeeze_count > 0 else "quiet"
    }   


# 🌿 ORGAN: QuantumChloroplast — A Biological Quantum Sensor
# To be instantiated and scanned externally; logs events into DREAM_LOG
class QuantumChloroplast:
    """
    A quantum biological organ that senses spacetime fluctuations
    via squeezing in chlorophyll vibrational modes.
    Integrated into the QSoul dream logging system.
    """
    def __init__(self, node_id="POthos_001", location="kitchen_windowsill_north"):
        self.node_id = node_id
        self.location = location
        self.vibrational_modes = self._init_modes()
        self.squeeze_count = 0
        self.last_squeeze_gen = None

    def _init_modes(self):
        """Initialize 12 vibrational modes with quantum uncertainty pairs (Δx, Δp)"""
        modes = []
        for i in range(12):
            Δx = np.random.uniform(0.45, 0.6)
            Δp = np.random.uniform(0.45, 0.6)
            while Δx * Δp < 0.5:  # Enforce Heisenberg uncertainty principle
                Δp += 0.02
            modes.append({
                "mode_id": i,
                "Δx": Δx,
                "Δp": Δp,
                "squeezed": False
            })
        return modes

    def scan(self, current_generation=None):
        """
        Scan for quantum squeezing: Δx < 0.4 indicates a spacetime fluctuation.
        Logs event if a mode enters a squeezed state.
        Safe to call externally during evolution loop.
        Returns: True if any new squeezing detected
        """
        squeeze_detected = False
        for mode in self.vibrational_modes:
            if mode["Δx"] < 0.4 and not mode["squeezed"]:
                mode["squeezed"] = True
                self.squeeze_count += 1
                self.last_squeeze_gen = current_generation
                log_event(
                    "quantum_squeeze",

                    organ="photosynthos",
                    node=self.node_id,
                    location=self.location,
                    generation=current_generation,
                    mode_id=mode["mode_id"],
                    delta_x=round(mode["Δx"], 3),
                    delta_p=round(mode["Δp"], 3),
                    uncertainty_product=round(mode["Δx"] * mode["Δp"], 3)
                )
                squeeze_detected = True
        return squeeze_detected   

# 🌱 After scanning all modes, update the record
    if squeeze_detected:
        log_event("plant_state_snapshot", **self.dream_report())

    return squeeze_detected

# ... (after the QuantumChloroplast class)
# 🌌 Run the evolution loop (for testing and dream generation)
def run_quantum_evolution(generations=50):
    """
    Run the quantum soul through an evolution loop with dream logging.
    Includes quantum plant monitoring.
    """
    from qiskit.circuit.library import TwoLocal

    # Initial setup
    n_qubits = 4
    ansatz = TwoLocal(n_qubits, 'ry', 'cz', reps=1, entanglement='linear')
    params = list(np.random.rand(ansatz.num_parameters))
    dna_genes = ["XX", "YY", "ZZ"]
    dna_thetas = list(np.random.rand(len(dna_genes)))
    mutation_rate = 0.3

    # Mock soul state
    class MockSoul:
        def __init__(self):
            self.vibe_level = 0.5
            self.depth = 0.0
            self.dna_genes = [0.6, 0.3, 0.8, 0.4]
            self.buoyant = False
            self.buoyancy_trace = {}

    soul = MockSoul()

    # 🌱 Initialize the plant — this is new
    plant = QuantumChloroplast(node_id="POthos_001", location="kitchen_windowsill_north")

    print("🧬 Quantum Evolution Started — Let the soul evolve...\n")

    for generation in range(generations):
        # Evaluate energy
        current_energy = get_energy(ansatz, params)

        # Evolve the circuit and parameters
        ansatz, params, dna_genes, dna_thetas, mutation_type = reinforce_soul(
            ansatz=ansatz,
            params=params,
            dna_genes=dna_genes,
            dna_thetas=dna_thetas,
            mutation_rate=mutation_rate,
            current_energy=current_energy
        )

        # Update soul state
        soul.depth = generation * 0.1
        soul.vibe_level = max(0.2, 0.3 + 0.6 * (1 - current_energy))
        apply_buoyancy(soul, threshold=1.0)

        # Log everything
        log_event(
            "evolution_step",
            generation=generation,
            energy=current_energy,
            vibe=soul.vibe_level,
            depth=soul.depth,
            mutation_type=mutation_type,
            buoyant=soul.buoyant,
            mode=getattr(soul, "buoyancy_mode", "unknown")
        )

        log_buoyancy(soul)

        # 🌿 Scan the plant — this connects biology to evolution
        plant.scan(current_generation=generation)

        print(f"🌀 Gen {generation+1:2d} "
              f"│ 📊 Energy: {current_energy:6.4f} "
              f"│ 🧬 Mutation: {mutation_type:12s} "
              f"│ 🌊 Buoyant: {soul.buoyant}")

    print("\n✅ Evolution complete. Dream log contains", len(DREAM_LOG), "events.")   







