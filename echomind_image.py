import os
from pathlib import Path
import numpy as np
import imageio.v2 as imageio
import matplotlib.pyplot as plt
from skimage import io, img_as_float, color, transform, util
from skimage.restoration import inpaint

ASSETS = Path("assets")
ASSETS.mkdir(exist_ok=True)
DATA = Path("data")
IMG_PATH = DATA / "memory.jpg"

def load_image_or_make_demo():
    if IMG_PATH.exists():
        img = io.imread(str(IMG_PATH))
        print(f"Loaded: {IMG_PATH}")
    else:
        print("No data/memory.jpg found — generating a demo image.")
        # synthetic “memory” image: gradient + shapes
        h, w = 360, 540
        xx, yy = np.meshgrid(np.linspace(0,1,w), np.linspace(0,1,h))
        base = np.stack([xx, yy, 0.5*xx+0.5*yy], axis=-1)
        # add a few colored rectangles/circles
        img = base.copy()
        img[60:160, 80:240, :] = [0.8, 0.2, 0.2]
        img[180:300, 320:480, :] = [0.2, 0.6, 0.9]
        rr, cc = np.ogrid[:h, :w]
        circ = (rr-240)**2 + (cc-160)**2 <= 45**2
        img[circ] = [0.2, 0.9, 0.4]
        img = (img*255).astype(np.uint8)
    # fast karne k liye
    img = transform.resize(img, (360, 540), anti_aliasing=True, preserve_range=True).astype(np.uint8)
    return img

def make_mask(shape, holes=3, max_size=0.30):
    """Create a boolean mask with a few random rectangular 'memory gaps'."""
    h, w = shape[:2]
    mask = np.zeros((h, w), dtype=bool)
    rng = np.random.default_rng(42)
    for _ in range(holes):
        rh = int(rng.uniform(0.12, max_size) * h)
        rw = int(rng.uniform(0.10, max_size) * w)
        r0 = int(rng.uniform(0, h - rh))
        c0 = int(rng.uniform(0, w - rw))
        mask[r0:r0+rh, c0:c0+rw] = True
    return mask

def inpaint_rgb(img, mask):
    """Run biharmonic inpainting per channel (skimage expects grayscale or per-channel)."""
    img_float = img_as_float(img)
    result = np.zeros_like(img_float)
    for ch in range(img_float.shape[2]):
        result[..., ch] = inpaint.inpaint_biharmonic(img_float[..., ch], mask, channel_axis=None)
    # clip 
    result = np.clip(result, 0, 1)
    return (result*255).astype(np.uint8)

def save_side_by_side(original, masked, restored, outpath):
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    axes[0].imshow(original); axes[0].set_title("Original")
    axes[1].imshow(masked);   axes[1].set_title("Fragmented Memory (Masked)")
    axes[2].imshow(restored); axes[2].set_title("Reconstructed Memory (Inpainted)")
    for ax in axes: ax.axis("off")
    fig.tight_layout()
    fig.savefig(outpath, dpi=140)
    plt.close(fig)

def make_progress_gif(masked, restored, mask, outpath, frames=24):
    """Visualize 'memory recall' as gradual completion by blending restored regions into the masked image."""
    frames_list = []
    masked_f = masked.astype(np.float32) / 255.0
    restored_f = restored.astype(np.float32) / 255.0
    mask_f = mask.astype(np.float32)[..., None]  # broadcast over 3 channels
    for i in range(frames):
        alpha = i / (frames - 1)  # 0 -> 1
        # blend only inside the masked region
        blended = masked_f * (1 - mask_f) + ((1 - alpha) * masked_f + alpha * restored_f) * mask_f
        frame_u8 = (np.clip(blended, 0, 1) * 255).astype(np.uint8)
        frames_list.append(frame_u8)
    imageio.mimsave(outpath, frames_list, duration=0.06)  # ~15 fps

if __name__ == "__main__":
    
    img = load_image_or_make_demo()
    mask = make_mask(img.shape, holes=3, max_size=0.28)
    masked = img.copy()
    masked[mask] = 0  # black-out missing memory regions
    restored = inpaint_rgb(img, mask)

    io.imsave("assets/em_original.png", img)
    io.imsave("assets/em_masked.png", masked)
    io.imsave("assets/em_restored.png", restored)
    save_side_by_side(img, masked, restored, "assets/em_triptych.png")

    #gif recall
    make_progress_gif(masked, restored, mask, "assets/em_recall.gif")

    print("✅ Saved:")
    print("  assets/em_original.png")
    print("  assets/em_masked.png")
    print("  assets/em_restored.png")
    print("  assets/em_triptych.png")
    print("  assets/em_recall.gif")
    print("\nTip: Add em_triptych.png and em_recall.gif to your README.")
