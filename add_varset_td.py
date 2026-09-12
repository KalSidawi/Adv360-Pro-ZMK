import re

with open('/home/kal/Projects/keyboards/Adv360-Pro-ZMK/config/freecad.dtsi', 'r') as f:
    dtsi_content = f.read()

# 1. Add macros
varset_macros = """// --- MACROS: VARSET ---
varset_stay: varset_stay {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp V>, <&kp S>;
};

varset_exit: varset_exit {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp V>, <&kp S>, <&to 0>;
};

eq_varset: eq_varset {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp EQUAL>, <&kp LS(V)>, <&kp A>, <&kp R>, <&kp LS(S)>, <&kp E>, <&kp T>, <&kp DOT>;
};

// --- MACROS: LAYER NAVIGATION ---"""

dtsi_content = dtsi_content.replace("// --- MACROS: LAYER NAVIGATION ---", varset_macros)

# 2. Add tap-dances
varset_tds = """// --- TAP-DANCES: VARSET ---
varset_td: varset_td {
    compatible = "zmk,behavior-tap-dance";
    #binding-cells = <0>;
    tapping-term-ms = <250>;
    bindings = <&varset_stay>, <&varset_exit>;
};

equal_td: equal_td {
    compatible = "zmk,behavior-tap-dance";
    #binding-cells = <0>;
    tapping-term-ms = <250>;
    bindings = <&kp EQUAL>, <&eq_varset>;
};

// --- TAP-DANCES: SKETCHER DOMAIN ---"""

dtsi_content = dtsi_content.replace("// --- TAP-DANCES: SKETCHER DOMAIN ---", varset_tds)

with open('/home/kal/Projects/keyboards/Adv360-Pro-ZMK/config/freecad.dtsi', 'w') as f:
    f.write(dtsi_content)

# Now update adv360.keymap
with open('/home/kal/Projects/keyboards/Adv360-Pro-ZMK/config/adv360.keymap', 'r') as f:
    keymap_content = f.read()

# Base Layer Row 2
keymap_content = keymap_content.replace("&kp EQUAL &kp Q", "&equal_td &kp Q", 1)
# Also update the visual block in Base layer
keymap_content = keymap_content.replace("║  &kp EQUAL   ║    &kp Q", "║  &equal_td   ║    &kp Q", 1)

# PartDesign Layer Row 4
parts = keymap_content.split("display-name = \"PartDesign\";")
pd_block = parts[1].split("};")[0]
new_pd_block = pd_block.replace("&trans &trans &trans &trans &trans &trans                      &trans &trans",
                                "&trans &trans &trans &trans &trans &varset_td                 &trans &trans", 1)
# Visual block
new_pd_block = new_pd_block.replace("║    &trans    ║    &trans    ║    &trans    ║    &trans    ║    &trans    ║    &trans    ║",
                                    "║    &trans    ║    &trans    ║    &trans    ║    &trans    ║    &trans    ║  &varset_td  ║", 1)
keymap_content = parts[0] + "display-name = \"PartDesign\";" + new_pd_block + "};" + "};".join(parts[1].split("};")[1:])


# Sketcher Layer Row 4
parts2 = keymap_content.split("display-name = \"Sketcher\";")
sk_block = parts2[1].split("};")[0]
new_sk_block = sk_block.replace("&trans &kp R  &kp A  &kp L  &kp M &trans                       &trans &trans",
                                "&trans &kp R  &kp A  &kp L  &kp M &varset_td                 &trans &trans", 1)
# Visual block
new_sk_block = new_sk_block.replace("║    &trans    ║    &kp R     ║    &kp A     ║    &kp L     ║    &kp M     ║    &trans    ║",
                                    "║    &trans    ║    &kp R     ║    &kp A     ║    &kp L     ║    &kp M     ║  &varset_td  ║", 1)
keymap_content = parts2[0] + "display-name = \"Sketcher\";" + new_sk_block + "};" + "};".join(parts2[1].split("};")[1:])

with open('/home/kal/Projects/keyboards/Adv360-Pro-ZMK/config/adv360.keymap', 'w') as f:
    f.write(keymap_content)
