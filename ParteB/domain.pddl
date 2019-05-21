;Header and description

(define (domain acciones_de_mecanizado)

;remove requirements that are not needed
(:requirements :strips :fluents :typing :conditional-effects :negative-preconditions :equality)

(:types Tool Piece Angulo Distancia
;todo: enumerate types and their hierarchy here, e.g. car truck bus - vehicle
)

; un-comment following line if constants are needed
;(:constants )

(:predicates (Tool ?t) (Piece ?p) (Distancia ?d) (Angulo ?a)
            (change_tool ?t1 ?t2) (rotate_piece ?p ?a1 ?a2) (move_piece ?p ?d1 ?d2) (using ?t)
            (drill_piece ?p ?t1 ?d1 ?a1) (grind_piece ?p ?t1 ?d1 ?a1) (lathe_piece ?p ?t1 ?d1)
            (in ?p ?d1) (at ?p ?a1) (hole_in ?p ?t1 ?d1 ?a1) (groove_in ?p ?t1 ?d1 ?a1) (lathe_in ?p ?t1 ?d1)
;todo: define predicates here
)

;(:functions ;todo: define numeric functions here
;)

;define actions here
(:action change_tool
    :parameters (?t1 - Tool ?t2 - Tool)
    :precondition (and (Tool ?t1) (Tool ?t2) (using ?t1))
    :effect (and (not (using ?t1)) (using ?t2))
)
(:action rotate_piece
    :parameters (?p - Piece ?a1 - Angulo ?a2 - Angulo)
    :precondition (and (Piece ?p) (Angulo ?a1) (Angulo ?a2) (at ?p ?a1))
    :effect (and (not(at ?p ?a1)) (at ?p ?a2))
)
(:action move_piece
    :parameters (?p - Piece ?d1 - Distancia ?d2 - Distancia)
    :precondition (and (Piece ?p) (Distancia ?d1) (Distancia ?d2) (in ?p ?d1))
    :effect (and (not(in ?p ?d1)) (in ?p ?d2))
)
(:action drill_piece ;perforado
    :parameters (?p - Piece ?t1 - Tool ?d1 - Distancia ?a1 - Angulo)
    :precondition (and (Piece ?p) (Tool ?t1) (Distancia ?d1) (Angulo ?a1) (in ?p ?d1) (at ?p ?a1) (using ?t1))
    :effect (and (hole_in ?p ?t1 ?d1 ?a1))
)
(:action grind_piece ;cepillado
    :parameters (?p - Piece ?t1 - Tool ?d1 - Distancia ?a1 - Angulo)
    :precondition (and (Piece ?p) (Tool ?t1) (Distancia ?d1) (Angulo ?a1) (in ?p ?d1) (at ?p ?a1) (using ?t1))
    :effect (and (groove_in ?p ?t1 ?d1 ?a1))
)
(:action lathe_piece ;torneado
    :parameters (?p - Piece ?t1 - Tool ?d1 - Distancia)
    :precondition (and (Piece ?p) (Tool ?t1) (Distancia ?d1) (in ?p ?d1) (using ?t1))
    :effect (and (lathe_in ?p ?t1 ?d1))
)


)