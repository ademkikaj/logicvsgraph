king(k).
rook(r).
white(w).
black(b).
distance((X1,Y1),(X2,Y2),D) :- D1 is abs(X1-X2), D2 is abs(Y1-Y2), D is max(D1,D2).
one(1).

square(p478,(7,7),w,k).
square(p478,(4,1),w,r).
square(p478,(5,0),b,k).
square(p883,(4,7),w,k).
square(p883,(5,7),w,r).
square(p883,(1,1),b,k).
square(p760,(3,2),w,k).
square(p760,(7,3),w,r).
square(p760,(6,7),b,k).
square(p847,(3,2),w,k).
square(p847,(4,4),w,r).
square(p847,(2,6),b,k).
square(p943,(2,1),w,k).
square(p943,(2,6),w,r).
square(p943,(6,3),b,k).
square(p508,(6,0),w,k).
square(p508,(2,2),w,r).
square(p508,(5,7),b,k).
square(p686,(2,7),w,k).
square(p686,(7,0),w,r).
square(p686,(3,2),b,k).
square(p785,(5,7),w,k).
square(p785,(7,2),w,r).
square(p785,(4,3),b,k).
square(p441,(4,0),w,k).
square(p441,(0,4),w,r).
square(p441,(5,7),b,k).
square(p676,(5,2),w,k).
square(p676,(5,5),w,r).
square(p676,(7,3),b,k).
square(p16,(5,3),w,k).
square(p16,(5,2),w,r).
square(p16,(0,2),b,k).
square(p99,(4,0),w,k).
square(p99,(1,5),w,r).
square(p99,(5,1),b,k).
square(p270,(4,1),w,k).
square(p270,(5,3),w,r).
square(p270,(5,6),b,k).
square(p113,(3,4),w,k).
square(p113,(4,4),w,r).
square(p113,(3,4),b,k).
square(p103,(0,6),w,k).
square(p103,(7,6),w,r).
square(p103,(7,2),b,k).
square(p27,(3,7),w,k).
square(p27,(0,4),w,r).
square(p27,(3,4),b,k).
square(p178,(5,6),w,k).
square(p178,(3,6),w,r).
square(p178,(5,7),b,k).
square(p170,(0,4),w,k).
square(p170,(5,2),w,r).
square(p170,(5,2),b,k).
square(p62,(0,5),w,k).
square(p62,(6,3),w,r).
square(p62,(6,0),b,k).
square(p50,(2,2),w,k).
square(p50,(4,0),w,r).
square(p50,(1,0),b,k).