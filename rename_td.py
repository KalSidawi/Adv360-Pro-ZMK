import re

# 1. Update freecad.dtsi
with open('/home/kal/Projects/keyboards/Adv360-Pro-ZMK/config/freecad.dtsi', 'r') as f:
    dtsi_content = f.read()

dtsi_content = dtsi_content.replace("equal_td: equal_td", "eq_varset_ins: eq_varset_ins")

with open('/home/kal/Projects/keyboards/Adv360-Pro-ZMK/config/freecad.dtsi', 'w') as f:
    f.write(dtsi_content)

# 2. Update adv360.keymap
with open('/home/kal/Projects/keyboards/Adv360-Pro-ZMK/config/adv360.keymap', 'r') as f:
    keymap_content = f.read()

keymap_content = keymap_content.replace("&equal_td", "&eq_varset_ins")

with open('/home/kal/Projects/keyboards/Adv360-Pro-ZMK/config/adv360.keymap', 'w') as f:
    f.write(keymap_content)
