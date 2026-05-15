#!/usr/bin/env python3
"""
RPG Character Generator for Rafa's Life - ELDEN RING STYLE
Reads vault data and generates epic character in Elden Ring aesthetic
"""

import os
import json
import re
from datetime import datetime, timedelta, date
from pathlib import Path

# ====== CONFIG ======
VAULT_PATH = Path("/Users/rafa/Desktop/RAFA AI BRAIN")

# ====== DATA EXTRACTION ======

def read_file(path):
    """Read a file from vault"""
    full_path = VAULT_PATH / path
    if full_path.exists():
        with open(full_path, 'r', encoding='utf-8') as f:
            return f.read()
    return None

def get_journal_path(days_ago=0):
    """Build vault-relative path to a recent journal file (dynamic, never hardcoded)"""
    MONTHS = {
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December",
    }
    target = datetime.now().date() - timedelta(days=days_ago)
    month_folder = f"{target.month:02d} {MONTHS[target.month]}"
    filename = f"{target.strftime('%Y-%m-%d')}.md"
    return f"01 Journals/{target.year} Journals/{month_folder}/{filename}"

def extract_performance_rating(content):
    """Extract performance rating from Today.md or journal"""
    match = re.search(r'\*\*Performance:\s*(\d+)/10\*\*', content)
    if match:
        return int(match.group(1))
    return None

def extract_tasks_status(content):
    """Extract task completion from Work — Tarefas Ativas.md"""
    # Count urgent tasks (🔴), this week (🟡), others
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
    """Extract habit completion from journal/today"""
    # Combine both sources
    all_content = (today_content or '') + (recent_journal or '')

    habits = {
        'morning_routine': bool(re.search(r'acordou|Acordou|rotina matinal', all_content, re.IGNORECASE)),
        'meditation': bool(re.search(r'meditação|breathwork|🧘', all_content, re.IGNORECASE)),
        'youtube': 'YouTube' not in recent_journal if recent_journal else True,
        'work_real': '🟢 Trabalho' in all_content,
    }
    return habits

def extract_energy_drains(content):
    """Find energy drains from journal"""
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
    """Rate the quality of journal (presence/autoconsciência)"""
    # Check for insight markers
    markers = ['insight', 'aprendizado', 'padrão', 'identidade', '💭', '👨‍🦳']
    count = sum(1 for m in markers if m in content.lower())
    return min(count / 2, 5)  # Max 5 levels

# ====== STAT CALCULATION ======

def calculate_stats(vault_data):
    """Calculate all RPG stats from vault data"""

    stats = {
        'hp': 60,
        'energy': 70,
        'focus': 50,
        'level': 1,
        'xp': 245,
        'updated': datetime.now().isoformat(),
    }

    # === HP Calculation ===
    # Base: 60
    # +10 per task completed
    # -15 per urgent task pending
    # -8 per week task pending

    if 'work_tasks' in vault_data:
        tasks = vault_data['work_tasks']
        stats['hp'] += tasks.get('urgent_pending', 0) * (-15)
        stats['hp'] += tasks.get('week_pending', 0) * (-8)

    # === ENERGY Calculation ===
    # Base: 70
    # +15 morning routine
    # +10 meditation
    # -20 alcohol
    # -15 food fail
    # -25 avoidance/busywork
    # +5 exercise

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

    # === FOCUS Calculation ===
    # Base: 50
    # +30 if work real > 70% of day
    # -30 if busywork > 75%
    # +10 if YouTube-free
    # +15 if high presence
    # -20 if gaming avoidance

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

    # Clamp values
    stats['hp'] = int(max(10, min(100, stats['hp'])))
    stats['energy'] = int(max(10, min(100, stats['energy'])))
    stats['focus'] = int(max(5, min(100, stats['focus'])))

    return stats

def generate_character_status(stats):
    """Generate ASCII/visual status"""
    hp_bar = '█' * (int(stats['hp']) // 10) + '░' * (10 - int(stats['hp']) // 10)
    energy_bar = '█' * (int(stats['energy']) // 10) + '░' * (10 - int(stats['energy']) // 10)
    focus_bar = '█' * (int(stats['focus']) // 10) + '░' * (10 - int(stats['focus']) // 10)

    # Determine overall status
    avg_stat = (stats['hp'] + stats['energy'] + stats['focus']) / 3
    if avg_stat >= 75:
        status = "⚡ ASCENDED"
    elif avg_stat >= 60:
        status = "💪 EMPOWERED"
    elif avg_stat >= 45:
        status = "⚔️ VIGILANT"
    elif avg_stat >= 30:
        status = "⚠️ WEAKENED"
    else:
        status = "💀 CURSED"

    return {
        'hp_bar': hp_bar,
        'energy_bar': energy_bar,
        'focus_bar': focus_bar,
        'overall_status': status,
    }

# ====== SVG GENERATION - ELDEN RING STYLE ======

def generate_svg(stats, display):
    """Generate Elden Ring style character SVG"""

    hp_percent = stats['hp']
    avg_stat = (stats['hp'] + stats['energy'] + stats['focus']) / 3

    # Determine aesthetic based on HP
    if hp_percent >= 80:
        # LEGEND - Golden, radiant
        primary_color = "#D4AF37"  # Gold
        secondary_color = "#FFF8DC"  # Cornsilk
        armor_color = "#FFD700"  # Gold armor
        aura_color = "#FFD700"
        aura_glow = "#FFED4E"
        glow_intensity = 0.4
        stance = "legend"
    elif hp_percent >= 60:
        # STRONG - Silver, bright
        primary_color = "#C0C0C0"  # Silver
        secondary_color = "#E8E8E8"  # Light gray
        armor_color = "#B8B8B8"  # Silver armor
        aura_color = "#87CEEB"
        aura_glow = "#00BFFF"
        glow_intensity = 0.3
        stance = "strong"
    elif hp_percent >= 40:
        # BALANCED - Iron, neutral
        primary_color = "#696969"  # Dim gray
        secondary_color = "#A9A9A9"  # Dark gray
        armor_color = "#808080"  # Gray armor
        aura_color = "#9370DB"
        aura_glow = "#BA55D3"
        glow_intensity = 0.2
        stance = "balanced"
    elif hp_percent >= 20:
        # WEAKENED - Rust, red tint
        primary_color = "#8B4513"  # Saddle brown
        secondary_color = "#CD5C5C"  # Indian red
        armor_color = "#A0522D"  # Sienna (rusted)
        aura_color = "#DC143C"
        aura_glow = "#FF6347"
        glow_intensity = 0.25
        stance = "weakened"
    else:
        # CURSED - Dark, purple corruption
        primary_color = "#2F1B3C"  # Dark purple
        secondary_color = "#4B0082"  # Indigo
        armor_color = "#1C0A2E"  # Very dark purple
        aura_color = "#8B008B"
        aura_glow = "#DDA0DD"
        glow_intensity = 0.3
        stance = "cursed"

    # Build SVG
    svg = f"""<svg width="400" height="600" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 600">
  <defs>
    <!-- Gradients -->
    <radialGradient id="auraGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" style="stop-color:{aura_glow};stop-opacity:{glow_intensity}" />
      <stop offset="100%" style="stop-color:{aura_color};stop-opacity:0" />
    </radialGradient>

    <linearGradient id="armorGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{secondary_color};stop-opacity:1" />
      <stop offset="50%" style="stop-color:{armor_color};stop-opacity:1" />
      <stop offset="100%" style="stop-color:{primary_color};stop-opacity:1" />
    </linearGradient>

    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Dark background -->
  <rect width="400" height="600" fill="#0a0e27"/>

  <!-- Mystical aura -->
  <circle cx="200" cy="240" r="140" fill="url(#auraGrad)" filter="url(#glow)"/>

  <!-- Torso/Chest Armor -->
  <path d="M 200 180 L 165 220 L 160 320 L 240 320 L 235 220 Z" fill="url(#armorGrad)" stroke="{primary_color}" stroke-width="2"/>

  <!-- Shoulder pauldrons -->
  <ellipse cx="140" cy="200" rx="35" ry="45" fill="{armor_color}" stroke="{secondary_color}" stroke-width="1.5"/>
  <ellipse cx="260" cy="200" rx="35" ry="45" fill="{armor_color}" stroke="{secondary_color}" stroke-width="1.5"/>

  <!-- Arms -->
  <path d="M 165 220 Q 120 240 110 320" stroke="{armor_color}" stroke-width="20" fill="none" stroke-linecap="round"/>
  <path d="M 235 220 Q 280 240 290 320" stroke="{armor_color}" stroke-width="20" fill="none" stroke-linecap="round"/>

  <!-- Gauntlets -->
  <rect x="100" y="315" width="20" height="40" fill="{primary_color}" stroke="{secondary_color}" stroke-width="1"/>
  <rect x="280" y="315" width="20" height="40" fill="{primary_color}" stroke="{secondary_color}" stroke-width="1"/>

  <!-- Legs/Leg Armor -->
  <path d="M 185 320 L 180 440 L 195 450 L 200 320 Z" fill="{armor_color}" stroke="{secondary_color}" stroke-width="1.5"/>
  <path d="M 215 320 L 220 440 L 205 450 L 200 320 Z" fill="{armor_color}" stroke="{secondary_color}" stroke-width="1.5"/>

  <!-- Sabatons (boots) -->
  <rect x="175" y="445" width="20" height="35" fill="{primary_color}" stroke="{secondary_color}" stroke-width="1"/>
  <rect x="205" y="445" width="20" height="35" fill="{primary_color}" stroke="{secondary_color}" stroke-width="1"/>

  <!-- Helmet -->
  <circle cx="200" cy="140" r="40" fill="{armor_color}" stroke="{secondary_color}" stroke-width="2"/>
  <path d="M 180 130 L 175 110 Q 200 90 225 110 L 220 130" fill="{primary_color}" stroke="{secondary_color}" stroke-width="1.5"/>

  <!-- Visor/Eyes (glowing) -->
  <ellipse cx="190" cy="135" rx="5" ry="8" fill="{aura_glow}" filter="url(#glow)"/>
  <ellipse cx="210" cy="135" rx="5" ry="8" fill="{aura_glow}" filter="url(#glow)"/>

  <!-- Shield -->
  <path d="M 280 240 L 320 250 L 325 340 Q 305 360 305 360 Q 285 340 280 310 Z" fill="{armor_color}" stroke="{secondary_color}" stroke-width="2"/>
  <path d="M 295 270 L 310 280" stroke="{secondary_color}" stroke-width="1.5" opacity="0.6"/>

  <!-- Weapon (sword) -->
  <rect x="105" y="280" width="8" height="110" fill="{primary_color}" stroke="{secondary_color}" stroke-width="1"/>
  <path d="M 109 280 L 100 250 L 118 250 Z" fill="{aura_glow}" stroke="{secondary_color}" stroke-width="1"/>
  <ellipse cx="109" cy="395" rx="10" ry="8" fill="{armor_color}" stroke="{secondary_color}" stroke-width="1"/>

  <!-- Status bar background (HP) -->
  <rect x="30" y="480" width="340" height="35" fill="#1a1a2e" stroke="{primary_color}" stroke-width="2" rx="5"/>

  <!-- HP Bar fill -->
  <rect x="35" y="485" width="{hp_percent * 3.3}" height="12" fill="{aura_glow}" rx="3"/>

  <!-- Energy Bar fill -->
  <rect x="35" y="502" width="{stats['energy'] * 3.3}" height="12" fill="#87CEEB" rx="3"/>

  <!-- Labels -->
  <text x="210" y="50" font-size="24" font-weight="bold" fill="{aura_glow}" text-anchor="middle" font-family="Arial, sans-serif">{display['overall_status']}</text>
  <text x="210" y="75" font-size="14" fill="{secondary_color}" text-anchor="middle" font-family="Arial, sans-serif">Lv {stats['level']} · {stats['xp']}/1000 XP</text>

  <!-- Stat labels -->
  <text x="35" y="520" font-size="11" fill="{secondary_color}" font-family="Arial, sans-serif">HP: {hp_percent}/100</text>
  <text x="35" y="537" font-size="11" fill="{secondary_color}" font-family="Arial, sans-serif">VIGOR: {stats['energy']}/100</text>

  <!-- Stance indicator -->
  <text x="210" y="570" font-size="12" fill="{primary_color}" text-anchor="middle" font-style="italic" font-family="Arial, sans-serif">{stance.upper()}</text>
</svg>"""

    return svg

# ====== MAIN ======

def main():
    """Main execution"""
    print("[RPG Character Generator]")
    print(f"Vault: {VAULT_PATH}")
    print()

    # Read key files
    print("📖 Reading vault data...")
    today_content = read_file("Today.md")
    work_content = read_file("Work — Tarefas Ativas.md")

    # Read journals dynamically — always today and yesterday, regardless of date
    journal_today = read_file(get_journal_path(0))
    journal_yesterday = read_file(get_journal_path(1))
    recent_journal = journal_today or journal_yesterday or ''

    print(f"   Today's journal:     {get_journal_path(0)} {'✅' if journal_today else '❌ (not found)'}")
    print(f"   Yesterday's journal: {get_journal_path(1)} {'✅' if journal_yesterday else '❌ (not found)'}")

    # Extract data
    print("🔍 Extracting metrics...")

    vault_data = {
        'work_tasks': extract_tasks_status(work_content) if work_content else {},
        'habits': extract_habits(today_content, recent_journal),
        'energy_drains': extract_energy_drains(recent_journal),
        'journal_quality': extract_journal_quality(recent_journal),
    }

    # Calculate stats
    print("⚙️  Calculating stats...")
    stats = calculate_stats(vault_data)
    display = generate_character_status(stats)

    # Generate SVG
    print("🎨 Generating character SVG...")
    svg = generate_svg(stats, display)

    # Save SVG
    svg_path = VAULT_PATH / "🎮-character.svg"
    with open(svg_path, 'w') as f:
        f.write(svg)
    print(f"✅ SVG saved: {svg_path}")

    # Print summary
    print()
    print("=" * 50)
    print("CHARACTER STATS")
    print("=" * 50)
    print(f"HP:     {stats['hp']:3d}/100  {display['hp_bar']}")
    print(f"Energy: {stats['energy']:3d}/100  {display['energy_bar']}")
    print(f"Focus:  {stats['focus']:3d}/100  {display['focus_bar']}")
    print(f"Status: {display['overall_status']}")
    print(f"Level:  {stats['level']} ({stats['xp']}/1000 XP)")
    print("=" * 50)
    print()
    print("💡 Vault data extracted:")
    print(json.dumps(vault_data, indent=2, ensure_ascii=False))
    print()
    print("✅ Done!")

if __name__ == '__main__':
    main()
