a = a
                                   // coste del camino hasta .

caso  =  perteneciente a ()
   si g(.) < g(.) entonces // (-----)
      // nos quedamos con el camino de menor coste
      .:= MEJORNODO
      actualizar g(.) y f'(.)
      propagar g a . de .
   eliminar .
   añadir . a ._MEJORNODO
caso . = . perteneciente a )-----(
   si g(.) < g(.) entonces
      // nos quedamos con el camino de menor coste
      .:= MEJORNODO
      actualizar g(.) y f'(.)
   eliminar .
   añadir . a ._MEJORNODO
caso . no estaba en ).( ni (.)
   añadir . a ).(
   añadir . a ._MEJORNODO
   f'(.) := g(.) + h'(.)

