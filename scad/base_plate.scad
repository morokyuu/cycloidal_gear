include <param.scad>



module outerpin_holes(){
    for(deg = [0 : 360/9 : 360]){
        rotate([0,0,deg])
        translate([d_pole_position/2+ROTER2OUTERPIN_GAP,0,0])
        cylinder(h=l_bottomplate_h,r=d_pole_hole/2);
    }
}

module base_plate(aperture){
    difference(){
        difference(){
            cylinder(h=l_bottomplate_h, r=30);
            outerpin_holes();
        }
        
        cylinder(h=l_bottomplate_h, r=aperture/2);
    }
}