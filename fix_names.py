import re

with open('/home/kal/Projects/keyboards/Adv360-Pro-ZMK/config/freecad.dtsi', 'r') as f:
    dtsi_content = f.read()

# 1. Rename macro varset_ref -> varset_ins
dtsi_content = dtsi_content.replace("varset_ref: varset_ref", "varset_ins: varset_ins")
dtsi_content = dtsi_content.replace("<&varset_ref>", "<&varset_ins>")

# 2. Rename tap-dances
dtsi_content = dtsi_content.replace("varset_td_pdes: varset_td_pdes", "varset_l1_ins_create: varset_l1_ins_create")
dtsi_content = dtsi_content.replace("varset_td_skch: varset_td_skch", "varset_l4_ins_create: varset_l4_ins_create")

# 3. Remove eq_varset_ins tap dance completely
td_pattern = r"eq_varset_ins: eq_varset_ins \{\n    compatible = \"zmk,behavior-tap-dance\";\n    #binding-cells = <0>;\n    tapping-term-ms = <250>;\n    bindings = <&kp EQUAL>, <&varset_ins>;\n\};\n\n"
dtsi_content = re.sub(td_pattern, "", dtsi_content)

with open('/home/kal/Projects/keyboards/Adv360-Pro-ZMK/config/freecad.dtsi', 'w') as f:
    f.write(dtsi_content)


with open('/home/kal/Projects/keyboards/Adv360-Pro-ZMK/config/adv360.keymap', 'r') as f:
    keymap_content = f.read()

# 1. Revert Base Layer eq_varset_ins to kp EQUAL
keymap_content = keymap_content.replace("&eq_varset_ins", "&kp EQUAL")
# Also fix the ASCII block just in case
keymap_content = keymap_content.replace("║  &eq_varset_ins   ║", "║  &kp EQUAL   ║")

# 2. Rename in PartDesign
keymap_content = keymap_content.replace("&varset_td_pdes", "&varset_l1_ins_create")

# 3. Rename in Sketcher
keymap_content = keymap_content.replace("&varset_td_skch", "&varset_l4_ins_create")

with open('/home/kal/Projects/keyboards/Adv360-Pro-ZMK/config/adv360.keymap', 'w') as f:
    f.write(keymap_content)
