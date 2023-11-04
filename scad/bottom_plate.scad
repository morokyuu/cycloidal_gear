include <base_plate.scad>


module spacer(){
    difference(){
        cylinder(h=l_pole, r=d_pole/2-0.2);
        cylinder(h=l_pole, r=d_pole_hole/2);
    }
}

module spacer_array(){
    for(deg = [0 : 360/9 : 360]){
        rotate([0,0,deg])
        translate([d_pole_position/2+ROTER2OUTERPIN_GAP,0,0])
        spacer();
    }
}


base_plate(30);

translate([0,0,l_roter_thick])
spacer_array();


//translate([d_pole_position/2,0,0])


