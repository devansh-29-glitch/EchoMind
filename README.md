
“The fence jumped over the dog.”

Yes, that’s right.

It’s the sentence EchoMind remembered, not what actually happened, but what it thought happened.

Just like your brain, it tried to fill in the blanks….. and got it charmingly wrong.

# 🧠 Project EchoMind - Simulating Memory Reconstruction

### 🌌 What is EchoMind?

EchoMind is an AI simulation of human memory reconstruction, inspired by the hippocampal pattern completion process in neuroscience.

>In simple terms:
your brain doesn’t store memories like hard drives do, it rebuilds them every time you recall them.
EchoMind mimics that. It takes fragmented memories, incomplete text or missing image regions,
and reconstructs what it thinks was there.

Sometimes it’s right.
Sometimes it’s… a fence jumping over a dog. 🐶

---

### 🧩 Phase 1 — Textual Memory Reconstruction

The system receives a partial memory:

"the _ jumped over the _"


It searches its “hippocampal associations” and tries to recall the full event.

Result:

🧠 Reconstructed memory: "the fence jumped over the dog"


### Why this matters:
In neuroscience, this mirrors hippocampal attractor dynamics —
how a few neural cues can trigger the recall of an entire event,
even if some details are distorted.

The reconstruction curve above shows how “confidence” rises as the brain (or model) fills in the blanks.

---

### 🎨 Phase 2 — Visual Memory Reconstruction

Next, EchoMind simulates how the brain restores visual memories when some parts are missing.

It receives a corrupted or masked image (simulating forgotten regions)
and uses computational inpainting to rebuild the scene — as if your hippocampus were guessing what used to be there.

Each frame shows the memory becoming clearer :- an echo of how your brain reactivates old neural patterns during recall.

---

**Visualization of recall progress**

![Reconstruction Progress](assets/text_reconstruction_curve.png)

---

### 🧬 Why This Project Matters
Cognitive Concept	Computational Analogue
Hippocampal pattern completion	Image inpainting & probabilistic text reconstruction
Memory distortion	AI prediction bias
Recall confidence curve	Reconstruction loss / certainty graph
Neural association	Word & pixel co-occurrence mapping

EchoMind bridges cognitive neuroscience and AI, showing how “thinking” and “predicting”
might just be two sides of the same neural coin.

---

### 🧠 Run It Yourself (Interactive Demo)

You can try both simulations in Google Colab (no setup needed) :- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/devansh-29-glitch/EchoMind/blob/main/EchoMind_Demo.ipynb) 


In the notebook, you can reconstruct("the _ is running towards the _")


and watch your “brain” fill in the blanks.

Or upload any image to /data/memory.jpg
and watch it reconstruct the forgotten parts.

---

### ⚙️ Tech Behind the Mind

🆕 **Language Reconstruction:** Numpy + Probabilistic context fill

🖼️ **Image Reconstruction:** Scikit-image inpainting (Biharmonic method)

👀 **Visualization:** Matplotlib, ImageIO

📖 **Conceptual Base:** Hippocampal attractor models and memory completion theory

🧠 **GPT-2** — linguistic pattern completion

⚙️ **Google Colab** — one-click AO demonstration

---

### 🧠 Final Thought

Memory isn’t a photograph.
It’s a painting your mind keeps repainting —
and sometimes, the fence does jump over the dog.

---

### 👨‍💻 Created By

Devansh Sharma
Exploring the interface between **memory, cognition, and machine intelligence**.

---


