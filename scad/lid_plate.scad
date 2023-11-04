include <base_plate.scad>


module bearing_hole(){
    translate([0,0,l_eccebearing_h-l_eccebearing_fr])
    cylinder(h=l_eccebearing_fr,r=d_eccebearing_fr/2);
}

module window(){
    wr = 6.6;
    
    for(deg = [0:120:360]){
        hull(){
            rotate([0,0,deg])
            translate([17,0,0])
            cylinder(h=20,r=wr-3);

            rotate([0,0,deg + 35])
            translate([16,0,0])
            cylinder(h=20,r=wr-1);

            rotate([0,0,deg + 70])
            translate([17,0,0])
            cylinder(h=20,r=wr-3);
        }
    }
}

difference(){
    base_plate(d_eccebearing+tr_bearing_hole);
    bearing_hole();
    
    window();
}

