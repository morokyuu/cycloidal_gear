include <param.scad>

translate([ecce,0,0])
import("inner_roter.stl");

translate([0,0,-l_motshafthld])
import("input_shaft.stl");
