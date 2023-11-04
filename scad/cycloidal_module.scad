include <param.scad>



module roter_assy(){
    translate([ecce,0,0]){
        color("yellow")
        rotate([180,0,0])
        translate([0,0,-l_eccebearing_h+l_eccesleeve_h])
        import("bearing.stl");
        
        //translate([0,0,l_eccesleeve_h])
        //color("cyan")
        %import("inner_roter.stl");
    }
}

module base_assy(){
    
    import("bottom_plate.stl");
    
}

module lid_assy(){
    import("lid_plate.stl");
    
    //translate([0,0,l_eccebearing_h])l_eccebearing_h
    //translate([0,0,l_output_h+5+l_output_shaft_fr])
    translate([0,0,5-0.5])
    rotate([180,0,0])
    
    color("yellow")
    import("bearing.stl");
    
    translate([0,0,-l_output_h])
    rotate([0,0,th_outp_angle])
    import("outplate.stl");
}


//translate([0,0,30])
roter_assy();

translate([0,0,-l_bottmoplate_h]){
    base_assy();
}

translate([0,0,30])
lid_assy();

translate([0,0,-15])
import("motor_plate.stl");

translate([0,0,-l_motshafthld-l_eccesleeve_h])
color("green")
import("input_shaft.stl");

