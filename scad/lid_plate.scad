include <base_plate.scad>


module bearing_hole(){
    cylinder(h=l_eccebearing_fr,r=d_eccebearing_fr/2+tr_bearing_shaft);
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

module spacer(){
    difference(){
        cylinder(h=l_lidspacer_h, r=d_pole/2-0.2);
        cylinder(h=l_lidspacer_h, r=d_pole_hole/2);
    }
}

difference(){
    base_plate(d_eccebearing+tr_bearing_hole);
    
    bearing_hole();
    
    window();
}

rotate([180,0,0])
//spacers
for(deg = [0 : 360/9 : 360]){
    rotate([0,0,deg])
    translate([d_pole_position/2+ROTER2OUTERPIN_GAP,0,0])
    spacer();
}