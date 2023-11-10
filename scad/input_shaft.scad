include <param.scad>

module shaft_hole(){
    hull(){
        translate([0,0,l_motshaft+4.5])
        cylinder(h=0.1,r=0.1);
        cylinder(h=l_motshaft,r=d_motshaft/2);
    }
}

module eccentric_shaft(){
    
    GAP = 0.025;
    
    translate([ecce,0,0]){
        translate([0,0,l_motshafthld])
        cylinder(h=l_eccesleeve_h,r=d_ecceshaft/2+l_motecce_fr);
        cylinder(h=l_motecceshaft,r=d_ecceshaft/2-GAP);
    }
}

module shaft_holder(){
    union(){
        //shaft holder
        cylinder(h=l_motshafthld,r=d_shaftholder/2+1.2);
        
        eccentric_shaft();
    }
}

difference(){
    shaft_holder();
    shaft_hole();
}
