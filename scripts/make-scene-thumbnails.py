#!/usr/bin/env python3
"""Build scene-based Gaertner thumbnails: take real frames from the video
and cover the burned-in caption pill with a cream label in the video's own
label style (cream box, dark bold text, thin dark border)."""
import os
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.expanduser(
    "~/workspace/goals/claude-2d-animation-work/files")
FRAMES = os.path.join(BASE, "scene-frames")

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
CREAM = (251, 243, 220)
DARK = (34, 26, 20)


def add_label(img, box, text, size, color=DARK):
    d = ImageDraw.Draw(img)
    d.rounded_rectangle(box, radius=34, fill=CREAM, outline=DARK, width=4)
    font = ImageFont.truetype(FONT, size)
    bbox = d.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    cx = (box[0] + box[2]) / 2
    cy = (box[1] + box[3]) / 2
    d.text((cx - tw / 2 - bbox[0], cy - th / 2 - bbox[1]),
           text, font=font, fill=color)


jobs = [
    # (source frame, output name, label box, text, font size)
    ("frame-5s.png",
     "kelrix-day1-gaertner-thumbnail-scene-option26-hook.png",
     (100, 1445, 980, 1575), "SEPT. 1945", 64),
    ("frame-30s.png",
     "kelrix-day1-gaertner-thumbnail-scene-option27-card.png",
     (110, 1420, 970, 1625), "NEW NAME. NEW LIFE.", 54),
    ("frame-44s.png",
     "kelrix-day1-gaertner-thumbnail-scene-option28-wanted.png",
     (150, 1400, 930, 1620), "HE HID FOR 40 YEARS", 56),
    # Second batch — more scenes from the video
    ("frame-23s.png",
     "kelrix-day1-gaertner-thumbnail-scene-option29-map.png",
     (350, 1000, 730, 1105), "WHY HE RAN", 48),
    ("frame-58s.png",
     "kelrix-day1-gaertner-thumbnail-scene-option30-surrender.png",
     (190, 1420, 890, 1575), "40 YEARS LATE", 60),
    ("frame-16s.png",
     "kelrix-day1-gaertner-thumbnail-scene-option31-train.png",
     (80, 1405, 1000, 1625), "ONE TRAIN. NO TURNING BACK.", 46),
]

for src, out, box, text, size in jobs:
    img = Image.open(os.path.join(FRAMES, src)).convert("RGB")
    assert img.size == (1080, 1920), img.size
    add_label(img, box, text, size)
    img.save(os.path.join(BASE, out))
    print("saved", out)
