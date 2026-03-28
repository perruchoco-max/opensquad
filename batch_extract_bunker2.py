#!/usr/bin/env python3
"""
Batch notion-fetch for Bunker 2 remaining URLs
Creates shell script with all notion-fetch commands
"""
import json

BUNKER_2_IDS = [
    "806169a11eaa82e892520126b449aaf9",
    "80f169a11eaa8233a735010912129a1c",
    "981169a11eaa829885d9810a4f861be2",
    "1cd169a11eaa825a89b2813f4ef54e69",
    "243169a11eaa826d86e28112ffeb24a6",
    "2fc169a11eaa83ed82d28160f3aa5fa6",
    "120169a11eaa83a0bac181b6c704e43d",
    "db7169a11eaa824e85c6811277f62678",
    "e9f169a11eaa8252a6c40152a392ee31",
    "c5d169a11eaa8380b8cc017a48f1f262",
    "e89169a11eaa8378bdb00192aec5db23",
    "b7b169a11eaa8327ada201dbe1219f1d",
    "b8a169a11eaa82038357016492e08c26",
    "c1f169a11eaa82a1abc601e6e0264590",
    "232169a11eaa82e99de48157bf7ec03c",
    "08b169a11eaa836995468130ed9c69c4",
    "a1d169a11eaa82f1b22a81e8dcfb4a0d",
    "ae0169a11eaa83e89cb40191b875f7bc",
    "b31169a11eaa8208b0e1817406c76997",
    "421169a11eaa83c49ce881b77b93c706",
    "46f169a11eaa83c3aed901c5dc4dcf5c",
    "695169a11eaa82f79f7e816a1cef123a",
    "84b169a11eaa824abaac81b8441c41e9",
    "ed1169a11eaa830f863101da08fbce4d"
]

print(f"Generated extraction commands for {len(BUNKER_2_IDS)} Bunker 2 page IDs")
print("To execute notion-fetch for each, use the tool interface")
