#!/usr/bin/env python3
"""
Extrai URLs restantes de Bunker 2, 3 e 5
Instructions for manual notion-fetch execution
"""
import json

BUNKER_2_REMAINING = [
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

BUNKER_3_REMAINING = [
    "83e169a11eaa832aa1c581c2c557d9f5",
    "137169a11eaa83a398bd81e0d8c142ff",
    "ba0169a11eaa82e68fd00115e2bf41a0",
    "c1c169a11eaa8326b84d01f2d485be37",
    "c45169a11eaa83138b7c013c9132e11b",
    "cc2169a11eaa8244850581e19e6f388f",
    "d3f169a11eaa828f88ee8151124a3a08",
    "e66169a11eaa8244821f8116fe680175",
    "f2f169a11eaa83eeaba101cb278e434d",
    "6bd169a11eaa837b936901111ce1722b",
    "783169a11eaa8397a09f81c5e06f784d",
    "8c9169a11eaa822fa996011657119b86",
    "9dc169a11eaa8335bd4c013b16cd139f",
    "5ff169a11eaa8328872e8169ce9e0dd3",
    "60b169a11eaa826fb8018123425dac93",
    "036169a11eaa8381ad09816c48a57e10",
    "166169a11eaa8292bf6d819fae70a771",
    "178169a11eaa837ba0000136644df6cc",
    "402169a11eaa83cc982501d774642910",
    "406169a11eaa83a4bc760191ad57cc26",
    "288169a11eaa8285b25f810e82594359",
    "40d169a11eaa836a9c99017b824844b1",
    "2af169a11eaa83e088aa013517634384",
    "cfc169a11eaa831ba77d814f3c5247d8"
]

BUNKER_5_REMAINING = [
    "86c169a11eaa8233937f01652fa680db",
    "f56169a11eaa825ca873819c33784ccc",
    "3e9169a11eaa824f8c8481285a3610b1",
    "6c1169a11eaa83a8880c81f8a1e0ce0f",
    "692169a11eaa832c828b01d9c8dc8b1e",
    "e49169a11eaa8222a4f5015999a4cf4f",
    "f8b169a11eaa83b587f8016c1ce363f9",
    "136169a11eaa82bcaff181ffaaaf2935",
    "13f169a11eaa82a2baa10135bc33924d",
    "217169a11eaa82869bbd81ef0252411c",
    "25f169a11eaa83248c4a013c659c5ea1",
    "290169a11eaa8394ac0c8101c0d480ed",
    "a4b169a11eaa833887ed81d89c3c6901",
    "4ee169a11eaa82b5a89f01cdc1f7ed86",
    "59f169a11eaa822988a281da936091c5",
    "091169a11eaa83ee92a2015b98a3abe0",
    "b34169a11eaa83c29fc28153c7aa8646",
    "aed169a11eaa821183c4812b35809993",
    "b17169a11eaa839980b2816b24051f26",
    "e5f169a11eaa8285b5a381dce8d307de",
    "e71169a11eaa82dd812001792ffbfa5b",
    "f3f169a11eaa8294ba8a016439513914",
    "fc4169a11eaa824ca72a81818771ba30",
    "8ce169a11eaa8325a78a01b1320935de"
]

print("\n" + "="*80)
print("EXTRACTION INSTRUCTIONS - 72 Remaining URLs")
print("="*80)

print(f"\nBunker 2: {len(BUNKER_2_REMAINING)} URLs remaining")
print(f"Bunker 3: {len(BUNKER_3_REMAINING)} URLs remaining")
print(f"Bunker 5: {len(BUNKER_5_REMAINING)} URLs remaining")
print(f"Total: {len(BUNKER_2_REMAINING) + len(BUNKER_3_REMAINING) + len(BUNKER_5_REMAINING)} URLs")

print("\n" + "="*80)
print("Page IDs to extract via notion-fetch:")
print("="*80)

all_ids = [("Bunker 2", id) for id in BUNKER_2_REMAINING] + \
          [("Bunker 3", id) for id in BUNKER_3_REMAINING] + \
          [("Bunker 5", id) for id in BUNKER_5_REMAINING]

# Save to JSON for reference
extraction_plan = {
    "total_to_extract": len(all_ids),
    "bunkers": {
        "Bunker 2": {"count": len(BUNKER_2_REMAINING), "ids": BUNKER_2_REMAINING},
        "Bunker 3": {"count": len(BUNKER_3_REMAINING), "ids": BUNKER_3_REMAINING},
        "Bunker 5": {"count": len(BUNKER_5_REMAINING), "ids": BUNKER_5_REMAINING}
    }
}

with open("/home/user/opensquad/extraction_plan_72_urls.json", 'w') as f:
    json.dump(extraction_plan, f, indent=2)

print("\nExtraction plan saved to: extraction_plan_72_urls.json")
print("\nTo complete the extraction:")
print("1. For each page_id in the lists above:")
print("2. Call: notion-fetch(id=page_id)")
print("3. Extract URL from 'Nome' field using regex pattern")
print("4. Aggregate into urls_todas_174_roteiros_COMPLETO.json")

