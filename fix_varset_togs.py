import re

with open('/home/kal/Projects/keyboards/Adv360-Pro-ZMK/config/freecad.dtsi', 'r') as f:
    dtsi_content = f.read()

# 1. Replace the universal macro/TD with layer-specific ones
old_varset_macros = """varset_stay: varset_stay {
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
};"""

new_varset_macros = """varset_stay: varset_stay {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp V>, <&kp S>;
};

varset_exit_pdes: varset_exit_pdes {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp V>, <&kp S>, <&tog PDES>;
};

varset_exit_skch: varset_exit_skch {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp V>, <&kp S>, <&tog SKCH>;
};"""

dtsi_content = dtsi_content.replace(old_varset_macros, new_varset_macros)


old_varset_tds = """varset_td: varset_td {
    compatible = "zmk,behavior-tap-dance";
    #binding-cells = <0>;
    tapping-term-ms = <250>;
    bindings = <&varset_stay>, <&varset_exit>;
};"""

new_varset_tds = """varset_td_pdes: varset_td_pdes {
    compatible = "zmk,behavior-tap-dance";
    #binding-cells = <0>;
    tapping-term-ms = <250>;
    bindings = <&varset_stay>, <&varset_exit_pdes>;
};

varset_td_skch: varset_td_skch {
    compatible = "zmk,behavior-tap-dance";
    #binding-cells = <0>;
    tapping-term-ms = <250>;
    bindings = <&varset_stay>, <&varset_exit_skch>;
};"""

dtsi_content = dtsi_content.replace(old_varset_tds, new_varset_tds)

with open('/home/kal/Projects/keyboards/Adv360-Pro-ZMK/config/freecad.dtsi', 'w') as f:
    f.write(dtsi_content)


# 2. Update adv360.keymap bindings
with open('/home/kal/Projects/keyboards/Adv360-Pro-ZMK/config/adv360.keymap', 'r') as f:
    keymap_content = f.read()

# PartDesign Layer
parts = keymap_content.split("display-name = \"PartDesign\";")
pd_block = parts[1].split("};")[0]
new_pd_block = pd_block.replace("&varset_td", "&varset_td_pdes")
keymap_content = parts[0] + "display-name = \"PartDesign\";" + new_pd_block + "};" + "};".join(parts[1].split("};")[1:])

# Sketcher Layer
parts2 = keymap_content.split("display-name = \"Sketcher\";")
sk_block = parts2[1].split("};")[0]
new_sk_block = sk_block.replace("&varset_td", "&varset_td_skch")
keymap_content = parts2[0] + "display-name = \"Sketcher\";" + new_sk_block + "};" + "};".join(parts2[1].split("};")[1:])

with open('/home/kal/Projects/keyboards/Adv360-Pro-ZMK/config/adv360.keymap', 'w') as f:
    f.write(keymap_content)
