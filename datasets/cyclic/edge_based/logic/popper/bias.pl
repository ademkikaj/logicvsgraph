max_vars(8).
max_body(6).
head_pred(cyclic,1).
body_pred(edge,2).
body_pred(node,2).
body_pred(green,1).
body_pred(red,1).
body_pred(instance,1).
type(cyclic,(id,)).
type(node,(id,color)).
type(edge,(id,id)).
type(instance,(id,)).
direction(cyclic,(in,)).
direction(node,(in,out)).
direction(edge,(in,out)).
direction(green,(out,)).
direction(red,(out,)).
direction(instance,(out,)).