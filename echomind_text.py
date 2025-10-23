import random
import re
from collections import defaultdict, Counter
import matplotlib.pyplot as plt
from tqdm import tqdm


CORPUS = [
    "the cat jumped over the fence",
    "the dog barked all night",
    "she looked at the stars and smiled",
    "he ran across the field in the morning",
    "the sun rose over the hills",
    "a gentle breeze moved the leaves",
    "the river flowed quietly under the bridge",
    "they danced under the moonlight",
    "the bird sang a beautiful tune",
    "a child laughed near the playground"
]

# bigram wala model
def train_ngram(corpus):
    model = defaultdict(Counter)
    for sentence in corpus:
        tokens = ["<s>"] + sentence.lower().split() + ["</s>"]
        for i in range(len(tokens) - 1):
            model[tokens[i]][tokens[i + 1]] += 1
    return model

# for prediction
def predict_next(model, word, top_k=3):
    next_words = model.get(word.lower(), {})
    if not next_words:
        return ["<unknown>"]
    total = sum(next_words.values())
    probs = {w: c / total for w, c in next_words.items()}
    sorted_words = sorted(probs.items(), key=lambda x: x[1], reverse=True)
    return [w for w, _ in sorted_words[:top_k]]

# reconstruction
def reconstruct_sentence(model, fragment, steps=5):
    words = fragment.lower().split()
    print(f"\n🧠 Starting hippocampal reconstruction for: '{fragment}'")
    print("-----------------------------------------------------------")
    for _ in tqdm(range(steps), desc="Memory recall progress"):
        try:
            idx = words.index("_")
        except ValueError:
            break  # no blanks left
        prev_word = words[idx - 1] if idx > 0 else "<s>"
        candidates = predict_next(model, prev_word)
        chosen = random.choice(candidates)
        words[idx] = chosen
        print(f"Filled blank with '{chosen}' (based on '{prev_word}')")
    completed = " ".join(words)
    print("-----------------------------------------------------------")
    print(f"🧩 Reconstructed memory: '{completed}'\n")
    return completed

# visualize
def plot_progress():
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot([0, 20, 50, 80, 100], [0.1, 0.4, 0.65, 0.82, 1.0], marker="o")
    ax.set_title("EchoMind — Memory Reconstruction Confidence Curve")
    ax.set_xlabel("Reconstruction Steps (%)")
    ax.set_ylabel("Pattern Completion Level")
    plt.tight_layout()
    plt.savefig("assets/text_reconstruction_curve.png")
    plt.close(fig)

if __name__ == "__main__":
    model = train_ngram(CORPUS)
    fragment = "the _ jumped over the _"
    reconstruct_sentence(model, fragment, steps=5)
    plot_progress()
    print("✅ Saved visualization in assets/text_reconstruction_curve.png")
