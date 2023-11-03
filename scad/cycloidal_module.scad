include <param.scad>


translate([ecce,0,0]){
    
    
    color("blue")
    import("inner_roter.stl");
    color("yellow")
    import("bearing.stl");

}
color("green")
translate([0,0,-l_motshafthld-l_eccesleeve_h])
import("input_shaft.stl");

