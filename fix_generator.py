import re

with open('/home/kal/Projects/keyboards/Adv360-Pro-ZMK/generate_freecad.py', 'r') as f:
    gen_content = f.read()

# Insert the macros before // --- MACROS: LAYER NAVIGATION ---
varset_macros = """// --- MACROS: VARSET ---
varset_ins: varset_ins {
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
};

// --- MACROS: LAYER NAVIGATION ---"""
gen_content = gen_content.replace("// --- MACROS: LAYER NAVIGATION ---", varset_macros)


# Insert tap dances before // --- TAP-DANCES: SKETCHER DOMAIN ---
varset_tds = """// --- TAP-DANCES: VARSET ---
vs_l1_ins_cr: vs_l1_ins_cr {
    compatible = "zmk,behavior-tap-dance";
    #binding-cells = <0>;
    tapping-term-ms = <250>;
    bindings = <&varset_ins>, <&varset_create_pdes>;
};

vs_l4_ins_cr: vs_l4_ins_cr {
    compatible = "zmk,behavior-tap-dance";
    #binding-cells = <0>;
    tapping-term-ms = <250>;
    bindings = <&varset_ins>, <&varset_create_skch>;
};

// --- TAP-DANCES: SKETCHER DOMAIN ---"""
gen_content = gen_content.replace("// --- TAP-DANCES: SKETCHER DOMAIN ---", varset_tds)


with open('/home/kal/Projects/keyboards/Adv360-Pro-ZMK/generate_freecad.py', 'w') as f:
    f.write(gen_content)
