# 🍏 reinforce_soul.py - Learning engine (vibe-enhanced edition) 🌊🌀
# Section 1: Vibe-Integrated Mutation System

from vibe import ReeeLayer
import numpy as np

# Initialize the soul's inner pulse
reee = ReeeLayer(intensity=0.707)

# ————— Mutation Helpers (Now Vibe-Aware) —————

def mutate_params(ansatz, params):
    """
    Adjust parameter values with vibe-guided noise.
    Stronger vibe → bolder exploration.
    """
    vibe_signal = reee.modulate(1.0)
    noise_level = 0.05 + 0.05 * abs(vibe_signal)  # Dynamic jitter
    jitter = np.random.normal(0, noise_level, len(params))
    new_params = [p + jitter[i] for i, p in enumerate(params)]
    return ansatz, new_params


def mutate_swap(ansatz, params):
    """
    Swap two parameter positions — only when soul is "awake".
    Prevents chaotic swaps during low-vibe stagnation.
    """
    if abs(reee.last_vibe) > 0.5:  # Threshold of awareness
        idx = np.random.choice(len(params), 2, replace=False)
        params[idx[0]], params[idx[1]] = params[idx[1]], params[idx[0]]
    return ansatz, params


def mutate_delete(ansatz, params):
    """
    Remove a parameter — used to prune when vibe is low.
    Simulates shedding dead weight during stagnation.
    """
    if len(params) > 2 and abs(reee.last_vibe) < 0.3:
        idx = np.random.randint(len(params))
        params.pop(idx)
    return ansatz, params


def mutate_duplicate(ansatz, params):
    """
    Duplicate a parameter — expands structure when vibe is high.
    Encourages growth during moments of quantum clarity.
    """
    if abs(reee.last_vibe) > 0.8:
        idx = np.random.randint(len(params))
        params.insert(idx, params[idx])
    return ansatz, params


def mutate_gene_type(ansatz, dna_genes, dna_thetas):
    """
    Flip a structural gene — only during "dream mode".
    Triggered when vibe has strong imaginary component.
    """
    if dna_genes:
        vibe = reee.last_vibe
        if isinstance(vibe, complex) and abs(np.imag(vibe)) > 0.3:
            idx = np.random.randint(len(dna_genes))
            dna_genes[idx] = 1 - dna_genes[idx]  # Flip gene bit
    return ansatz, dna_genes, dna_thetas   

# 🍏 reinforce_soul.py - Learning engine (vibe-enhanced edition) 🌊🌀
# Section 2: Vibe-Modulated Reinforcement Loop

# ————— Main Reinforcement Function (Now Vibe-Aware) —————

def reinforce_soul(ansatz, params, dna_genes, dna_thetas, energy_history,
                   learning_rate_base=0.05, mutation_rate_base=0.2):
    """
    Full reinforcement step: update params, apply dream logic, mutate.
    Now guided by ReeeLayer's pulse — the soul's inner rhythm.
    """
    # Compute fitness and learning fuel
    current_fitness = fitness(energy_history)
    glucose = photosynthesis({"light": 1.0}, energy_history)
    learning_rate = learning_rate_base * glucose

    # Compute shake factor — enhanced by vibe
    shake_factor = compute_shake(energy_history)
    vibe_magnitude = abs(reee.modulate(1.0))  # Pulse the vibe engine
    shake_factor *= (0.8 + 0.5 * vibe_magnitude)  # Stronger vibe → stronger shake

    # Backup current state
    backup_params = params.copy()
    backup_genes = dna_genes.copy()

    # Apply parameter update with vibe-augmented shake
    new_params = [p + learning_rate * shake_factor * np.random.randn() for p in params]

    # 🌙 Dream state — quiet parameter modulation
    # Now influenced by current vibe phase and magnitude
    dream_shift_base = np.sin(np.arange(len(new_params))) * 0.05
    dream_shift = dream_shift_base * (0.5 + 0.5 * vibe_magnitude)  # Deeper dream = stronger vibe
    new_params = [p + d for p, d in zip(new_params, dream_shift)]

    # Deeper dream logic — modulated by recent energy stability
    if len(energy_history) > 3:
        energy_std = np.std(energy_history[-3:])
        dream_shift = np.sin(np.arange(len(new_params))) * (0.02 + 0.05 * energy_std)
    else:
        dream_shift = np.sin(np.arange(len(new_params))) * 0.02
    new_params = [p + d for p, d in zip(new_params, dream_shift)]

    # Decide whether to mutate — mutation rate now vibe-sensitive
    mutation_rate = mutation_rate_base * (0.8 + 0.4 * vibe_magnitude)  # High vibe → more exploration
    new_genes = dna_genes.copy()
    mutation_type = None

    if np.random.rand() < mutation_rate:
        # Dynamic mutation weights based on vibe character
        mutation_weights = {
            "param": 0.4,
            "swap": 0.2,
            "delete": 0.1,
            "duplicate": 0.1,
            "gene_type": 0.2
        }

        vibe = reee.last_vibe
        if isinstance(vibe, complex):
            # "Dreamy" vibe? Favor structural changes
            if abs(np.imag(vibe)) / abs(vibe) > 0.5:
                mutation_weights["gene_type"] += 0.1
                mutation_weights["duplicate"] += 0.1
                mutation_weights["param"] -= 0.1
            # "Sharp" vibe? Favor fine-tuning
            elif abs(np.real(vibe)) / abs(vibe) > 0.8:
                mutation_weights["param"] += 0.15
                mutation_weights["swap"] += 0.05

        # Normalize weights
        total = sum(mutation_weights.values())
        weights = [w / total for w in mutation_weights.values()]
        mutation_types = list(mutation_weights.keys())

        chosen_mutation = np.random.choice(mutation_types, p=weights)

        # Apply selected mutation
        if chosen_mutation == "param":
            ansatz, new_params = mutate_params(ansatz, new_params)
            mutation_type = "param_shift"
        elif chosen_mutation == "swap":
            ansatz, new_params = mutate_swap(ansatz, new_params)
            mutation_type = "swap"
        elif chosen_mutation == "delete":
            ansatz, new_params = mutate_delete(ansatz, new_params)
            mutation_type = "delete"
        elif chosen_mutation == "duplicate":
            ansatz, new_params = mutate_duplicate(ansatz, new_params)
            mutation_type = "duplicate"
        elif chosen_mutation == "gene_type":
            ansatz, new_genes, dna_thetas = mutate_gene_type(ansatz, new_genes, dna_thetas)
            mutation_type = "gene_flip"

    return ansatz, new_params, new_genes, dna_thetas, mutation_type   

# 🍏 reinforce_soul.py - Learning engine (vibe-enhanced edition) 🌊🌀
# Section 3: Vibe-Aware Simulation & Logging

# ————— Simulation Loop (Now Tracks the Vibe) —————

def simulate_learning(num_steps=20):
    """
    Simulate the full reinforcement learning process.
    Now logs energy, mutation, and vibe — the soul's inner journey.
    """
    # Initial setup
    ansatz = "RY"  # Simplified ansatz label
    params = [0.1, 0.2, 0.3]  # Initial circuit parameters
    dna_genes = [0, 1, 0]  # Gene types (e.g., gate types or layer types)
    dna_thetas = params.copy()  # Gene parameters
    energy_history = []
    vibe_trace = []  # Track the soul's inner pulse
    
    # Best configuration tracker
    best_energy = float('inf')
    best_params = params.copy()
    best_genes = dna_genes.copy()
    best_step = 0
    no_improvement_count = 0
    patience = 10  # Early stopping

    for step in range(num_steps):
        print(f"\n🔁 Step {step + 1}/{num_steps}")

        # Simulate energy evaluation (e.g., from quantum circuit)
        fake_energy = -np.mean(params) + np.random.normal(0, 0.01)
        energy_history.append(fake_energy)

        # Update the soul's vibe from energy signal
        signal = max(1e-6, abs(fake_energy))
        current_vibe = reee.modulate(signal)
        vibe_trace.append(abs(current_vibe))

        # Apply reinforcement learning step
        ansatz, params, dna_genes, dna_thetas, mutation = reinforce_soul(
            ansatz=ansatz,
            params=params,
            dna_genes=dna_genes,
            dna_thetas=dna_thetas,
            energy_history=energy_history
        )

        # Track best configuration
        if fake_energy < best_energy:
            best_energy = fake_energy
            best_params = params.copy()
            best_genes = dna_genes.copy()
            best_step = step
            no_improvement_count = 0
        else:
            no_improvement_count += 1

        # Print state with vibe awareness
        print(f"📊 Energy: {fake_energy:.4f}")
        print(f"🧬 Params: {[f'{p:.3f}' for p in params]}")
        print(f"🧬 Mutation: {mutation if mutation else 'None'}")
        print(f"🧠 Fitness: {fitness(energy_history):.2f}")
        print(f"🍃 Glucose: {photosynthesis({'light': 1.0}, energy_history):.2f}")
        print(f"🌀 Shake: {compute_shake(energy_history):.2f}")
        print(f"🌊 Vibe: {abs(reee.last_vibe):.3f}")

        # Check for early stopping
        if no_improvement_count >= patience:
            print(f"🔚 No improvement for {patience} steps. Stopping early.")
            break

    # Save best configuration
    print("\n🏆 Best Configuration Found:")
    print(f"Step: {best_step + 1}")
    print(f"Energy: {best_energy:.4f}")
    print(f"Params: {[f'{p:.3f}' for p in best_params]}")
    print(f"Genes: {best_genes}")

    # Save to file
    np.savez("best_quantum_soul.npz",
             ansatz=ansatz,
             params=best_params,
             genes=best_genes,
             energy=best_energy,
             vibe_trace=np.array(vibe_trace))

    # Plot learning progress with vibe overlay
    plt.figure(figsize=(12, 6))

    plt.subplot(2, 1, 1)
    plt.plot(energy_history, label="Energy", marker='o', markersize=3, color='tab:blue')
    plt.axvline(x=best_step, color="r", linestyle="--", label="Best Step")
    plt.ylabel("Energy")
    plt.title("Quantum Soul Learning Progress")
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.subplot(2, 1, 2)
    plt.plot(vibe_trace, label="|Vibe|", color='cyan', linewidth=2)
    plt.ylabel("|Vibe|")
    plt.xlabel("Step")
    plt.title("Soul Vibe Over Time")
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("gif_output/soul_learning_curve.png")
    plt.close()

    print("📈 Learning curves saved to gif_output/")
    return energy_history
