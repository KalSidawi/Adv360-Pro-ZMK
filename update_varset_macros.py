import re

with open('/home/kal/Projects/keyboards/Adv360-Pro-ZMK/config/freecad.dtsi', 'r') as f:
    content = f.read()

# Replace the entire VARSET macros section
old_macros = """// --- MACROS: VARSET ---
varset_stay: varset_stay {
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
};

eq_varset: eq_varset {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp EQUAL>, <&kp LS(V)>, <&kp A>, <&kp R>, <&kp LS(S)>, <&kp E>, <&kp T>, <&kp DOT>;
};"""

new_macros = """// --- MACROS: VARSET ---
varset_ref: varset_ref {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp EQUAL>, <&kp LS(V)>, <&kp A>, <&kp R>, <&kp LS(S)>, <&kp E>, <&kp T>, <&kp DOT>;
};

varset_create_pdes: varset_create_pdes {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&tog PDES>, <&kp V>, <&kp S>;
};

varset_create_skch: varset_create_skch {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&tog SKCH>, <&kp V>, <&kp S>;
};"""

content = content.replace(old_macros, new_macros)


# Replace the entire VARSET tap-dance section
old_tds = """// --- TAP-DANCES: VARSET ---
varset_td_pdes: varset_td_pdes {
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
};

eq_varset_ins: eq_varset_ins {
    compatible = "zmk,behavior-tap-dance";
    #binding-cells = <0>;
    tapping-term-ms = <250>;
    bindings = <&kp EQUAL>, <&eq_varset>;
};"""

new_tds = """// --- TAP-DANCES: VARSET ---
varset_td_pdes: varset_td_pdes {
    compatible = "zmk,behavior-tap-dance";
    #binding-cells = <0>;
    tapping-term-ms = <250>;
    bindings = <&varset_ref>, <&varset_create_pdes>;
};

varset_td_skch: varset_td_skch {
    compatible = "zmk,behavior-tap-dance";
    #binding-cells = <0>;
    tapping-term-ms = <250>;
    bindings = <&varset_ref>, <&varset_create_skch>;
};

eq_varset_ins: eq_varset_ins {
    compatible = "zmk,behavior-tap-dance";
    #binding-cells = <0>;
    tapping-term-ms = <250>;
    bindings = <&kp EQUAL>, <&varset_ref>;
};"""

content = content.replace(old_tds, new_tds)

with open('/home/kal/Projects/keyboards/Adv360-Pro-ZMK/config/freecad.dtsi', 'w') as f:
    f.write(content)
