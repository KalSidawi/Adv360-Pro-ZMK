#!/usr/bin/env python3
import re
import argparse
import sys
import os

# Map application aliases to their respective ZMK layer names
APP_LAYERS = {
    "freecad": ["PartDesign", "Sketcher", "Constraints"],
    "vscode": ["VisualStudioCode"],
    "kicad": ["KiCAD"],
    "base": ["default_layer", "Keypad", "symbols", "Function", "mod"],
    "wiki": ["Wiki"]
}

def extract_block(keymap_content, layer_name):
    pattern = rf"display-name = \"{layer_name}\";\n(.*?)bindings ="
    match = re.search(pattern, keymap_content, re.DOTALL)
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

def generate_markdown(app_name, layers, keymap_path, out_dir):
    with open(keymap_path, 'r') as f:
        keymap = f.read()

    md_content = f"""---
title: {app_name.capitalize()} ZMK Visual Layouts (Left Half)
categories: [hardware-config, ai-reference]
tags: [{app_name.lower()}, zmk, adv360]
status: stable
---

# {app_name.capitalize()} ZMK Visual Layouts (Left Half)

This document contains the raw ASCII grid extractions for the left hand of the {app_name.capitalize()}-specific layers on the Advantage360.

"""
    found_any = False
    for layer in layers:
        block = extract_block(keymap, layer)
        if block:
            md_content += f"## {layer} Layer\n\n```text\n{block}\n```\n\n"
            found_any = True

    if not found_any:
        print(f"Error: Could not find any visual blocks for {app_name}.")
        return False

    out_file = os.path.join(out_dir, f"{app_name.lower()}_zmk_visual_blocks.md")
    with open(out_file, 'w') as f:
        f.write(md_content)
    
    print(f"Successfully generated: {out_file}")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract left-half ZMK ASCII blocks for specific applications.")
    parser.add_argument("app", choices=list(APP_LAYERS.keys()) + ["all"], 
                        help="The application to extract layers for (e.g., freecad, vscode).")
    parser.add_argument("--keymap", default="/home/kal/Projects/keyboards/Adv360-Pro-ZMK/config/adv360.keymap",
                        help="Path to adv360.keymap")
    parser.add_argument("--outdir", default="/home/kal/Dropbox/wiki/Systems_and_SOPs",
                        help="Output directory for the generated markdown files")
    
    args = parser.parse_args()

    apps_to_process = APP_LAYERS.keys() if args.app == "all" else [args.app]

    for app in apps_to_process:
        generate_markdown(app, APP_LAYERS[app], args.keymap, args.outdir)
