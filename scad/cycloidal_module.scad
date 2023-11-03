include <param.scad>



module roter_assy(){
    translate([ecce,0,0]){
        color("yellow")
        import("bearing.stl");
        
        translate([0,0,l_eccesleeve_h])
        color("blue")
        import("inner_roter.stl");
    }
}

module base_assy(){
    
    import("bottom_plate.stl");
    
    translate([0,0,l_bottmoplate_h]){
    //translate([0,0,4]){
        //spacers
        for(deg = [0 : 360/9 : 360]){
            rotate([0,0,deg])
            translate([d_pole_position/2,0,0])
            color("pink")
            import("spacer_pole.stl");    
        }
    }
}

module lid_assy(){
    %import("lid_plate.stl");
    
    translate([0,0,-l_eccebearing_fr])
    color("yellow")
    import("bearing.stl");
}



roter_assy();

translate([0,0,-l_bottmoplate_h]){
    base_assy();
}

translate([0,0,10])
lid_assy();

translate([0,0,-l_motshafthld-l_eccesleeve_h])
color("green")
import("input_shaft.stl");

