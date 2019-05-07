threshold_limit is 8. % [mm]

rusting(body, X) :- X = 1.
rusting(pipes, X) :- X = 1.
rusting(joints, X) :- X = 1.

less_thickness(body, X) :- X < threshold_limit.
less_thickness(pipes, X) :- X < threshold_limit.
less_thickness(joints, X) :- X < threshold_limit.


parts(body).
parts(pipes).
parts(joints).
