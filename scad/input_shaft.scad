include <param.scad>

module shaft_hole(){
    hull(){
        translate([0,0,l_motshaft+6])
        cylinder(h=0.1,r=0.1);
        cylinder(h=l_motshaft,r=d_motshaft/2);
    }
}

module shaft_holder(){
    union(){
        //shaft holder
        cylinder(h=l_motshaft+7,r=d_shaftholder/2,center=false);
        //eccentric shaft
        translate([ecce,0,0])
        cylinder(h=l_motshaft+15,r=d_motshaft/2);
    }
}

difference(){
    %shaft_holder();
    shaft_hole();
}
