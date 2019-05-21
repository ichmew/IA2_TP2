(define (problem mecanizado_de_pieza1) (:domain acciones_de_mecanizado)
(:objects Pieza - Piece
        Fresa Cepillo Torno - Tool
        d0 d1 d2 d3 d4 d5 - Distancia
        a0 a1 a2 a3 - Angulo
)

(:init 
    (Piece Pieza)
    (Tool Fresa) (Tool Cepillo) (Tool Torno)
    (Distancia d0) (Distancia d1) (Distancia d2) (Distancia d3) (Distancia d4) (Distancia d5)
    (Angulo a0) (Angulo a1) (Angulo a2) (Angulo a3)
    (in Pieza d0) (at Pieza a0) (using Torno)
    ;todo: put the initial state's facts and numeric values here
)

(:goal (and
    (hole_in Pieza Fresa d1 a1)
    (groove_in Pieza Cepillo d3 a3)
    (groove_in Pieza Cepillo d2 a2) 
    (lathe_in Pieza Torno d0)
    (lathe_in Pieza Torno d4) 
    )
    ;todo: put the goal condition here
)

;un-comment the following line if metric is needed
;(:metric minimize (???))
)
