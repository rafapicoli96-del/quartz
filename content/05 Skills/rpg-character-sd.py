#!/usr/bin/env python3
"""
RPG Character Generator - Stable Diffusion Version
Generates epic Elden Ring-style character images locally
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
IMAGE_PATH = VAULT_PATH / "🎮-character.png"

print(f"[SD] Device: {DEVICE}")
print(f"[SD] MPS Available: {torch.backends.mps.is_available()}")

# ====== DATA EXTRACTION (same as before) ======

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

def get_status_and_aesthetic(hp):
    """Determine status and aesthetic parameters"""
    if hp >= 80:
        return {
            'status': '⚡ ASCENDED',
            'style': 'legendary golden warrior',
            'aura': 'golden divine light',
            'mood': 'triumphant, radiant, powerful'
        }
    elif hp >= 60:
        return {
            'status': '⚔️ VIGILANT',
            'style': 'strong silver-armored warrior',
            'aura': 'celestial blue glow',
            'mood': 'determined, watchful, ready'
        }
    elif hp >= 40:
        return {
            'status': '🛡️ BALANCED',
            'style': 'iron-armored warrior',
            'aura': 'purple mystical energy',
            'mood': 'neutral, focused, steady'
        }
    elif hp >= 20:
        return {
            'status': '⚠️ WEAKENED',
            'style': 'battered warrior with rusted armor',
            'aura': 'red corruption spreading',
            'mood': 'struggling, wounded, desperate'
        }
    else:
        return {
            'status': '💀 CURSED',
            'style': 'corrupted dark warrior consumed by shadow',
            'aura': 'deep purple void corruption',
            'mood': 'cursed, darkened, consumed'
        }

def generate_prompt(stats):
    """Generate Stable Diffusion prompt"""
    aesthetic = get_status_and_aesthetic(stats['hp'])

    prompt = f"epic fantasy warrior knight, {aesthetic['style']}, holding sword and shield, detailed armor, {aesthetic['mood']}, cinematic lighting, masterpiece, high quality"

    negative_prompt = "blurry, low quality, distorted, ugly, bad anatomy, watermark, text, mutation"

    return prompt.strip(), negative_prompt

# ====== MAIN ======

def main():
    print("[RPG-SD] Starting character generation with Stable Diffusion...")
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
    print(f"Level:  {stats['level']}")
    print(f"{'='*50}\n")

    # === Generate prompt ===
    print("✍️  Generating Stable Diffusion prompt...")
    prompt, negative_prompt = generate_prompt(stats)
    aesthetic = get_status_and_aesthetic(stats['hp'])

    print(f"Status: {aesthetic['status']}")
    print(f"Prompt: {prompt[:100]}...")
    print()

    # === Load model ===
    print(f"⏳ Loading Stable Diffusion model ({MODEL_ID})...")
    print("   (First time: downloading ~4GB, may take 5-10 minutes)")
    print()

    try:
        pipe = StableDiffusionPipeline.from_pretrained(
            MODEL_ID,
            torch_dtype=torch.float32,
            safety_checker=None
        )
        pipe = pipe.to(DEVICE)

        if DEVICE == "mps":
            pipe.enable_attention_slicing()

        print("✅ Model loaded!")
        print()

        # === Generate image ===
        print("🎨 Generating image (this takes 1-3 minutes on Mac)...")
        print("   Please wait...")
        print()

        with torch.no_grad():
            image = pipe(
                prompt,
                negative_prompt=negative_prompt,
                num_inference_steps=50,
                guidance_scale=7.5,
                height=512,
                width=512
            ).images[0]

        # === Save image ===
        print(f"💾 Saving image to {IMAGE_PATH}...")
        image.save(IMAGE_PATH)

        print(f"✅ Image saved!")
        print()
        print(f"{'='*50}")
        print(f"SUCCESS!")
        print(f"{'='*50}")
        print(f"Image: {IMAGE_PATH}")
        print(f"Stats: HP={stats['hp']}, Energy={stats['energy']}, Focus={stats['focus']}")
        print(f"Status: {aesthetic['status']}")
        print(f"{'='*50}")

    except Exception as e:
        print(f"❌ Error: {e}")
        print()
        print("Troubleshooting:")
        print("1. Make sure you have 8GB+ free disk space (for model download)")
        print("2. Check internet connection")
        print("3. Try again - first run always takes longer")

if __name__ == '__main__':
    main()
