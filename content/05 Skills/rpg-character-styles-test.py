#!/usr/bin/env python3
"""
RPG Character Generator - Style Tester
Generates all 7 visual styles for comparison
"""

import os
import json
import re
import torch
from datetime import datetime
from pathlib import Path
from diffusers import StableDiffusionPipeline

# ====== CONFIG ======
VAULT_PATH = Path("/Users/rafa/Desktop/RAFA AI BRAIN")
MODEL_ID = "runwayml/stable-diffusion-v1-5"
DEVICE = "mps" if torch.backends.mps.is_available() else "cpu"

print(f"[SD] Device: {DEVICE}")

# ====== STYLES ======

STYLES = {
    "1_elden_ring": {
        "name": "Elden Ring",
        "emoji": "⚔️",
        "prompt": "epic fantasy warrior knight, detailed medieval armor, holding sword and shield, celestial blue glow, cinematic lighting, masterpiece"
    },
    "2_cyberpunk": {
        "name": "Cyberpunk",
        "emoji": "🤖",
        "prompt": "cyber samurai warrior, high-tech neon armor, glowing neon blue and pink, futuristic samurai, holding plasma sword, dark cyberpunk city background, cinematic"
    },
    "3_dark_souls": {
        "name": "Dark Souls",
        "emoji": "💀",
        "prompt": "dark fantasy warrior, corrupted armor, gothic medieval, sinister aura, red and purple darkness, holding cursed sword, ominous lighting, masterpiece"
    },
    "4_anime": {
        "name": "Anime/Manga",
        "emoji": "⚡",
        "prompt": "anime style epic warrior, vibrant colors, dynamic pose, detailed anime art, glowing aura, dramatic lighting, manga illustration, high quality"
    },
    "5_norse": {
        "name": "Norse/Viking",
        "emoji": "🪓",
        "prompt": "viking warrior, nordic armor, bronze and gold, runes and mythology, holding axe and shield, ice blue glow, norse mythology, epic pose"
    },
    "6_celestial": {
        "name": "Celestial/Divino",
        "emoji": "✨",
        "prompt": "celestial divine warrior, angelic armor, glowing golden light, radiant aura, heavenly glow, holy warrior, white and gold colors, masterpiece"
    },
    "7_steampunk": {
        "name": "Steampunk",
        "emoji": "⚙️",
        "prompt": "steampunk warrior, mechanical armor with gears, copper and bronze, steam effects, goggles and machinery, industrial aesthetic, Victorian steampunk"
    }
}

# ====== DATA EXTRACTION ======

def read_file(path):
    """Read a file from vault"""
    full_path = VAULT_PATH / path
    if full_path.exists():
        with open(full_path, 'r', encoding='utf-8') as f:
            return f.read()
    return None

def extract_tasks_status(content):
    """Extract task completion"""
    lines = content.split('\n')
    urgent_pending = 0
    week_pending = 0

    for line in lines:
        if '🔴' in line and '❌' in line:
            urgent_pending += 1
        elif '🟡' in line and '❌' in line:
            week_pending += 1

    return {'urgent_pending': urgent_pending, 'week_pending': week_pending}

def extract_habits(today_content, recent_journal):
    """Extract habit completion"""
    all_content = (today_content or '') + (recent_journal or '')

    habits = {
        'morning_routine': bool(re.search(r'acordou|Acordou|rotina matinal', all_content, re.IGNORECASE)),
        'meditation': bool(re.search(r'meditação|breathwork|🧘', all_content, re.IGNORECASE)),
        'youtube': 'YouTube' not in recent_journal if recent_journal else True,
        'work_real': '🟢 Trabalho' in all_content,
    }
    return habits

def extract_energy_drains(content):
    """Find energy drains"""
    drains = []
    if 'FIFA' in content or 'avoidance' in content.lower():
        drains.append('gaming')
    if 'cerveja' in content or 'álcool' in content.lower():
        drains.append('alcohol')
    if 'lactose' in content or 'escondidinho' in content:
        drains.append('food_fail')
    if 'Claude/Obsidian' in content and '8h' in content:
        drains.append('busywork')
    return drains

def extract_journal_quality(content):
    """Rate journal quality"""
    markers = ['insight', 'aprendizado', 'padrão', 'identidade', '💭', '👨‍🦳']
    count = sum(1 for m in markers if m in content.lower())
    return min(count / 2, 5)

# ====== STAT CALCULATION ======

def calculate_stats(vault_data):
    """Calculate RPG stats"""
    stats = {
        'hp': 60,
        'energy': 70,
        'focus': 50,
        'level': 1,
        'xp': 245,
    }

    if 'work_tasks' in vault_data:
        tasks = vault_data['work_tasks']
        stats['hp'] += tasks.get('urgent_pending', 0) * (-15)
        stats['hp'] += tasks.get('week_pending', 0) * (-8)

    if 'habits' in vault_data:
        habits = vault_data['habits']
        if habits.get('morning_routine'):
            stats['energy'] += 15
        if habits.get('meditation'):
            stats['energy'] += 10

    if 'energy_drains' in vault_data:
        drains = vault_data['energy_drains']
        if 'alcohol' in drains:
            stats['energy'] -= 20
        if 'food_fail' in drains:
            stats['energy'] -= 15
        if 'busywork' in drains:
            stats['energy'] -= 25

    if 'energy_drains' in vault_data:
        drains = vault_data['energy_drains']
        if 'gaming' in drains:
            stats['focus'] -= 20
        if 'busywork' in drains:
            stats['focus'] -= 30

    if 'habits' in vault_data and vault_data['habits'].get('youtube'):
        stats['focus'] += 10

    if 'journal_quality' in vault_data:
        stats['focus'] += vault_data['journal_quality'] * 3

    stats['hp'] = int(max(10, min(100, stats['hp'])))
    stats['energy'] = int(max(10, min(100, stats['energy'])))
    stats['focus'] = int(max(5, min(100, stats['focus'])))

    return stats

# ====== MAIN ======

def main():
    print("[RPG-STYLES] Generating all 7 character styles...")
    print()

    # === Read vault data ===
    print("📖 Reading vault data...")
    today_content = read_file("Today.md")
    work_content = read_file("Work — Tarefas Ativas.md")
    journal_14 = read_file("01 Journals/2026 Journals/04 April/2026-04-14.md")
    journal_13 = read_file("01 Journals/2026 Journals/04 April/2026-04-13.md")

    # === Extract metrics ===
    print("🔍 Extracting metrics...")
    vault_data = {
        'work_tasks': extract_tasks_status(work_content) if work_content else {},
        'habits': extract_habits(today_content, journal_14 or journal_13 or ''),
        'energy_drains': extract_energy_drains((journal_14 or journal_13 or '')),
        'journal_quality': extract_journal_quality((journal_14 or journal_13 or '')),
    }

    # === Calculate stats ===
    print("⚙️  Calculating stats...")
    stats = calculate_stats(vault_data)

    print(f"\n{'='*50}")
    print(f"CHARACTER STATS")
    print(f"{'='*50}")
    print(f"HP:     {stats['hp']:3d}/100")
    print(f"Energy: {stats['energy']:3d}/100")
    print(f"Focus:  {stats['focus']:3d}/100")
    print(f"{'='*50}\n")

    # === Load model ===
    print(f"⏳ Loading Stable Diffusion model...")
    pipe = StableDiffusionPipeline.from_pretrained(
        MODEL_ID,
        torch_dtype=torch.float32,
        safety_checker=None
    )
    pipe = pipe.to(DEVICE)

    if DEVICE == "mps":
        pipe.enable_attention_slicing()

    print("✅ Model loaded!\n")

    negative_prompt = "blurry, low quality, distorted, ugly, bad anatomy, watermark, text"

    # === Generate all styles ===
    print(f"{'='*60}")
    print("🎨 GENERATING ALL 7 STYLES (this will take ~15-20 minutes)")
    print(f"{'='*60}\n")

    results = {}

    for style_key, style_info in STYLES.items():
        print(f"{style_info['emoji']} {style_info['name'].upper()}...")
        print(f"   Prompt: {style_info['prompt'][:60]}...")

        try:
            with torch.no_grad():
                image = pipe(
                    style_info['prompt'],
                    negative_prompt=negative_prompt,
                    num_inference_steps=40,
                    guidance_scale=7.5,
                    height=512,
                    width=512
                ).images[0]

            # Save image
            image_path = VAULT_PATH / f"🎮-style-{style_key}.png"
            image.save(image_path)
            results[style_key] = str(image_path)

            print(f"   ✅ Saved to {image_path.name}\n")

        except Exception as e:
            print(f"   ❌ Error: {e}\n")
            results[style_key] = None

    # === Summary ===
    print(f"\n{'='*60}")
    print("✅ GENERATION COMPLETE!")
    print(f"{'='*60}\n")

    print("📸 Generated images:\n")
    for style_key, style_info in STYLES.items():
        status = "✅" if results[style_key] else "❌"
        print(f"  {status} {style_info['emoji']} {style_info['name']:20s} → 🎮-style-{style_key}.png")

    print(f"\n{'='*60}")
    print("🎯 NEXT STEP:")
    print("   Look at the 7 images and decide which style you like best!")
    print("   Then tell Claude which one you want (e.g., '3_dark_souls')")
    print(f"{'='*60}\n")

if __name__ == '__main__':
    main()
