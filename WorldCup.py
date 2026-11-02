#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
"""Entertainment-only simulator using the 2018 World Cup group roster."""
from __future__ import annotations
import argparse
import random
import tkinter as tk
from tkinter import ttk

GROUPS = {
    "A": ("Russia", "Saudi Arabia", "Egypt", "Uruguay"),
    "B": ("Portugal", "Spain", "Morocco", "Iran"),
    "C": ("France", "Australia", "Peru", "Denmark"),
    "D": ("Argentina", "Iceland", "Croatia", "Nigeria"),
    "E": ("Brazil", "Switzerland", "Costa Rica", "Serbia"),
    "F": ("Germany", "Mexico", "Sweden", "South Korea"),
    "G": ("Belgium", "Panama", "Tunisia", "England"),
    "H": ("Poland", "Colombia", "Senegal", "Japan"),
}

def simulate(seed: int | None = None) -> tuple[str, list[str]]:
    rng = random.Random(seed)
    if len({team for group in GROUPS.values() for team in group}) != 32:
        raise ValueError("Expected 32 distinct teams")
    lines = ["2018 World Cup fictional simulation", ""]
    qualifiers = {}
    for name, teams in GROUPS.items():
        order = rng.sample(teams, len(teams))
        qualifiers[name] = order[:2]
        lines.append(f"Group {name}: {order[0]} / {order[1]} qualify")
    keys = list(GROUPS)
    bracket = []
    for i in range(0, 8, 2):
        left, right = keys[i], keys[i + 1]
        bracket.extend([(qualifiers[left][0], qualifiers[right][1]),
                        (qualifiers[right][0], qualifiers[left][1])])
    for round_name in ("Round of 16", "Quarterfinals", "Semifinals", "Final"):
        lines.extend(("", round_name))
        winners = []
        for a, b in bracket:
            winner = rng.choice((a, b))
            winners.append(winner)
            lines.append(f"{a} vs {b} -> {winner}")
        bracket = list(zip(winners[::2], winners[1::2]))
    return winners[0], lines

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--text", action="store_true")
    parser.add_argument("--seed", type=int, help="Optional reproducible simulation seed")
    args = parser.parse_args()
    def run() -> str:
        winner, lines = simulate(args.seed)
        return "\n".join(lines + ["", f"Champion: {winner}"])
    if args.text:
        print(run())
        return
    root = tk.Tk()
    root.title("2018 World Cup Simulator")
    root.geometry("720x620")
    frame = ttk.Frame(root, padding=12)
    frame.pack(fill="both", expand=True)
    output = tk.Text(frame, wrap="word", font=("monospace", 10))
    output.pack(fill="both", expand=True)
    def refresh():
        output.delete("1.0", "end")
        output.insert("1.0", run())
    ttk.Button(frame, text="Simulate again", command=refresh).pack(pady=8)
    refresh()
    root.mainloop()

if __name__ == "__main__":
    main()
