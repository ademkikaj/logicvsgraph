max_vars(10).
max_body(8).
head_pred(mutag,1).
body_pred(atom,4).
body_pred(bond,2).
body_pred(nitro,2).
body_pred(benzene,2).
body_pred(edge,3).
type(mutag,(id,)).
type(atom,(id,node_id,atom_type,charge)).
type(bond,(id,node_id)).
type(nitro,(id,node_id)).
type(benzene,(id,node_id)).
type(edge,(id,node_id,node_id)).