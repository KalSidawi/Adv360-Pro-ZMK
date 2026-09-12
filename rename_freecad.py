macros_and_tds = """// ══════════════════════════════════════════════════════════════════════════════
// FREECAD MACROS & TAP-DANCES
// ══════════════════════════════════════════════════════════════════════════════

// --- MACROS: SKETCHER DOMAIN ---
line: line {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp G>, <&kp L>;
};

polyline: polyline {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp G>, <&kp M>;
};

rectangle: rectangle {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp G>, <&kp R>;
};

slot: slot {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp G>, <&kp S>;
};

circle: circle {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp G>, <&kp C>;
};

arc: arc {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp G>, <&kp A>;
};

trim_edge: trim_edge {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp T>;
};

point: point {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp G>, <&kp P>;
};

ext_geo: ext_geo {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp G>, <&kp E>;
};

construct: construct {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp G>, <&kp T>;
};


// --- MACROS: PART DESIGN DOMAIN ---
pad: pad {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp P>, <&kp A>;
};

pocket: pocket {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp P>, <&kp O>;
};

revolve: revolve {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp R>, <&kp E>;
};

groove: groove {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp G>, <&kp R>;
};

fillet: fillet {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp F>, <&kp I>;
};

chamfer: chamfer {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp C>, <&kp H>;
};

lin_pattern: lin_pattern {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp L>, <&kp P>;
};

pol_pattern: pol_pattern {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp P>, <&kp P>;
};

mirror: mirror {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp M>, <&kp I>;
};

multi_trans: multi_trans {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp M>, <&kp T>;
};

new_sketch: new_sketch {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp C>, <&kp S>;
};

leave_sketch: leave_sketch {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp ESC>;
};


// --- MACROS: CONSTRAINTS DOMAIN ---
coincident: coincident {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp C>;
};

pt_on_obj: pt_on_obj {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp O>;
};

horizontal: horizontal {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp H>;
};

vertical: vertical {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp V>;
};

distance: distance {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp K>, <&kp D>;
};

radius: radius {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp K>, <&kp R>;
};

equal_const: equal_const {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp E>;
};

symmetric: symmetric {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp S>;
};

parallel: parallel {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp P>;
};

perpendic: perpendic {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    wait-ms = <30>;
    tap-ms = <30>;
    bindings = <&kp N>;
};


// ══════════════════════════════════════════════════════════════════════════════
// TAP-DANCE DEFINITIONS
// ══════════════════════════════════════════════════════════════════════════════

// --- TAP-DANCES: SKETCHER DOMAIN ---
td_line_poly: td_line_poly {
    compatible = "zmk,behavior-tap-dance";
    #binding-cells = <0>;
    tapping-term-ms = <250>;
    bindings = <&line>, <&polyline>;
};

td_rect_slot: td_rect_slot {
    compatible = "zmk,behavior-tap-dance";
    #binding-cells = <0>;
    tapping-term-ms = <250>;
    bindings = <&rectangle>, <&slot>;
};

td_circ_arc: td_circ_arc {
    compatible = "zmk,behavior-tap-dance";
    #binding-cells = <0>;
    tapping-term-ms = <250>;
    bindings = <&circle>, <&arc>;
};

td_trim_pt: td_trim_pt {
    compatible = "zmk,behavior-tap-dance";
    #binding-cells = <0>;
    tapping-term-ms = <250>;
    bindings = <&trim_edge>, <&point>;
};

td_geo_const: td_geo_const {
    compatible = "zmk,behavior-tap-dance";
    #binding-cells = <0>;
    tapping-term-ms = <250>;
    bindings = <&ext_geo>, <&construct>;
};

// --- TAP-DANCES: PART DESIGN DOMAIN ---
td_pad_pock: td_pad_pock {
    compatible = "zmk,behavior-tap-dance";
    #binding-cells = <0>;
    tapping-term-ms = <250>;
    bindings = <&pad>, <&pocket>;
};

td_rev_groov: td_rev_groov {
    compatible = "zmk,behavior-tap-dance";
    #binding-cells = <0>;
    tapping-term-ms = <250>;
    bindings = <&revolve>, <&groove>;
};

td_fill_cham: td_fill_cham {
    compatible = "zmk,behavior-tap-dance";
    #binding-cells = <0>;
    tapping-term-ms = <250>;
    bindings = <&fillet>, <&chamfer>;
};

td_lin_polar: td_lin_polar {
    compatible = "zmk,behavior-tap-dance";
    #binding-cells = <0>;
    tapping-term-ms = <250>;
    bindings = <&lin_pattern>, <&pol_pattern>;
};

td_mir_trans: td_mir_trans {
    compatible = "zmk,behavior-tap-dance";
    #binding-cells = <0>;
    tapping-term-ms = <250>;
    bindings = <&mirror>, <&multi_trans>;
};

td_sketch: td_sketch {
    compatible = "zmk,behavior-tap-dance";
    #binding-cells = <0>;
    tapping-term-ms = <250>;
    bindings = <&new_sketch>, <&leave_sketch>;
};

// --- TAP-DANCES: CONSTRAINTS DOMAIN ---
td_coincident: td_coincident {
    compatible = "zmk,behavior-tap-dance";
    #binding-cells = <0>;
    tapping-term-ms = <250>;
    bindings = <&coincident>, <&pt_on_obj>;
};

td_distance: td_distance {
    compatible = "zmk,behavior-tap-dance";
    #binding-cells = <0>;
    tapping-term-ms = <250>;
    bindings = <&distance>, <&radius>;
};

td_horizontal: td_horizontal {
    compatible = "zmk,behavior-tap-dance";
    #binding-cells = <0>;
    tapping-term-ms = <250>;
    bindings = <&horizontal>, <&vertical>;
};

td_equal_sym: td_equal_sym {
    compatible = "zmk,behavior-tap-dance";
    #binding-cells = <0>;
    tapping-term-ms = <250>;
    bindings = <&equal_const>, <&symmetric>;
};

td_parallel: td_parallel {
    compatible = "zmk,behavior-tap-dance";
    #binding-cells = <0>;
    tapping-term-ms = <250>;
    bindings = <&parallel>, <&perpendic>;
};
"""

with open("config/freecad.dtsi", "w") as f:
    f.write(macros_and_tds)
