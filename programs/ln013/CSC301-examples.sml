(* factorial using if expression *)
fun fact n = if n=1 then 1 else n*fact(n-1);

fact(3) = 6;

(* sum integer values on a list *)
fun listsum l = if l=[] then 0 else hd(l)+listsum(tl(l));

listsum([1,2,3]) = 6;


(* factorial with multi-dispatch *)
fun fact 1 = 1
  | fact n = n*fact(n-1);

fact(3)=6;

(* listsum head-tail pattern matching *)
fun listsum [] = 0
  | listsum (h::t) = h+listsum(t);

listsum([1,2,3])=6;

(* wild card pattern *)
fun f 0 = "zero"
  | f _ = "something else";

f(0) = "zero";
f(1) = "something else";
