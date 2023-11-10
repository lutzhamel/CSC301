woman(ann).
woman(pam).
woman(liz).
woman(pat).

man(tom).
man(bob).
man(jim).  

parent(pat,jim).
parent(pam,bob).
parent(tom,bob).
parent(tom,liz).
parent(bob,ann).
parent(bob,pat).

mother(X,Y) :-
    woman(X),
    parent(X,Y).
    
