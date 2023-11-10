include <param.scad>



module roter_assy(){
    translate([ecce,0,0]){
        color("yellow")
        rotate([180,0,0])
        //translate([0,0,-l_eccebearing_h-l_eccesleeve_h])
        translate([0,0,-l_eccebearing_h])
        import("bearing.stl");
        
        translate([0,0,l_eccebearing_fr])
        color("cyan")
        import("inner_roter.stl");
    }
}

module base_assy(){
    
    import("bottom_plate.stl");
    
}

module lid_assy(){
    color("gray")
    import("lid_plate.stl");
    
    color("yellow")
    import("bearing.stl");
    
    color("orange")
    translate([0,0,-l_output_h-l_output_shaft_fr])
    rotate([0,0,th_outp_angle])
    import("outplate.stl");
}



translate([0,0,-l_bottomplate_h]){
    base_assy();
}

translate([0,0,-l_motshafthld-l_motecce_fr]){
    color("green")
    import("input_shaft.stl");
}


//translate([0,0,30])
roter_assy();


translate([0,0,l_pole+l_lidspacer_h])
lid_assy();

translate([0,0,-15])
import("motor_plate.stl");



