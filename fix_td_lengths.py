import re

with open('/home/kal/Projects/keyboards/Adv360-Pro-ZMK/config/freecad.dtsi', 'r') as f:
    dtsi_content = f.read()

# Rename the tap-dances
dtsi_content = dtsi_content.replace("varset_l1_ins_create: varset_l1_ins_create", "vs_l1_ins_cr: vs_l1_ins_cr")
dtsi_content = dtsi_content.replace("varset_l4_ins_create: varset_l4_ins_create", "vs_l4_ins_cr: vs_l4_ins_cr")

with open('/home/kal/Projects/keyboards/Adv360-Pro-ZMK/config/freecad.dtsi', 'w') as f:
    f.write(dtsi_content)

with open('/home/kal/Projects/keyboards/Adv360-Pro-ZMK/config/adv360.keymap', 'r') as f:
    keymap_content = f.read()

# Replace bindings
keymap_content = keymap_content.replace("&varset_l1_ins_create", "&vs_l1_ins_cr")
keymap_content = keymap_content.replace("&varset_l4_ins_create", "&vs_l4_ins_cr")

# Fix ASCII Grid Alignment
# We know the cell is 14 characters wide.
# Previously it was ║  &varset_td  ║ which is 14 chars. (10 + 4 spaces)
# But earlier I replaced &varset_td with &varset_l1_ins_create, which blew out the grid!
# Let's fix the specific blocks. We just need to replace the blown-out string with the perfectly padded string.
# Blown out: "║  &varset_l1_ins_create  ║" or similar.
# Actually, I used replace() without padding logic, so it just expanded the line.
# Let's find the exact lines and fix them.

# PartDesign Layer Row 4 visual block:
# It used to be ║    &trans    ║
# I replaced it with ║  &varset_td  ║
# Then with ║  &varset_l1_ins_create  ║
# Let's replace "║  &varset_l1_ins_create  ║" with "║&vs_l1_ins_cr ║"
keymap_content = keymap_content.replace("║  &varset_l1_ins_create  ║", "║&vs_l1_ins_cr ║")
# In case spacing was different:
keymap_content = re.sub(r"║\s*&varset_l1_ins_create\s*║", "║&vs_l1_ins_cr ║", keymap_content)

# Sketcher Layer Row 4 visual block:
keymap_content = re.sub(r"║\s*&varset_l4_ins_create\s*║", "║&vs_l4_ins_cr ║", keymap_content)

with open('/home/kal/Projects/keyboards/Adv360-Pro-ZMK/config/adv360.keymap', 'w') as f:
    f.write(keymap_content)
