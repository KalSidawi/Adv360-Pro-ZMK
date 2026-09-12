import re

with open('/home/kal/Projects/keyboards/Adv360-Pro-ZMK/config/adv360.keymap', 'r') as f:
    keymap = f.read()

def extract_block(layer_name):
    pattern = rf"display-name = \"{layer_name}\";\n(.*?)bindings ="
    match = re.search(pattern, keymap, re.DOTALL)
    if not match:
        return ""
    
    lines = match.group(1).splitlines()
    ascii_lines = []
    for line in lines:
        if line.strip().startswith("// "):
            clean_line = line.replace("// ", "", 1)
            # Slice at 146 characters to perfectly crop out the right keyboard half
            ascii_lines.append(clean_line[:146])
    return "\n".join(ascii_lines)

layers = ["PartDesign", "Sketcher", "Constraints"]

md_content = """---
title: FreeCAD ZMK Visual Layouts (Left Half)
categories: [hardware-config, ai-reference]
tags: [freecad, zmk, adv360]
status: stable
---

# FreeCAD ZMK Visual Layouts (Left Half)

This document contains the raw ASCII grid extractions for the left hand of the FreeCAD-specific layers on the Advantage360.

"""

for layer in layers:
    block = extract_block(layer)
    if block:
        md_content += f"## {layer} Layer\n\n```text\n{block}\n```\n\n"

with open('/home/kal/Dropbox/wiki/Systems_and_SOPs/freecad_zmk_visual_blocks.md', 'w') as f:
    f.write(md_content)
