include <param.scad>

module shaft_hole(){
    cylinder(h=l_motshaft,r=d_motshaft/2);
}

module eccentric_shaft(){
    
    GAP = 0.025;
    
    translate([ecce,0,0]){
        
        translate([0,0,l_motshafthld])
        cylinder(h=l_eccesleeve_h,r=d_ecceshaft/2+0.3);
        cylinder(h=l_motecceshaft,r=d_ecceshaft/2-GAP);
    }
}

module shaft_holder(){
    union(){
        //shaft holder
        cylinder(h=l_motshafthld,r=d_shaftholder/2,center=false);
        
        width = 7
        translate([10,-5,0])
        cube([10,10,l_motshafthld]);
        eccentric_shaft();
    }
}

difference(){
    %shaft_holder();
    shaft_hole();
}
