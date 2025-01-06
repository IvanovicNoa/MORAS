Require Import Bool.

Goal forall (X Y : bool), ((X && negb Y) || (negb X && negb Y) || (negb X && Y)) = (negb X || negb Y).
Proof.
  intros x y. destruct x, y; reflexivity.
Qed.

Goal forall (X Y Z : bool), negb (negb X && Y && Z) && negb (X && Y && negb Z) && (X && negb Y && Z) = (X && negb Y && Z).
Proof.
  intros x y z. destruct x, y, z; reflexivity.
Qed.
