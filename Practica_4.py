a = a
                                   // coste del camino hasta .

caso  =  perteneciente a ()
   si g(.) < g(.) entonces // (-----)
      // nos quedamos con el camino de menor coste
      .:= MEJORNODO
      actualizar g(.) y f'(.)
      propagar g a . de .
   eliminar .
   a�adir . a ._MEJORNODO
caso . = . perteneciente a )-----(
   si g(.) < g(.) entonces
      // nos quedamos con el camino de menor coste
      .:= MEJORNODO
      actualizar g(.) y f'(.)
   eliminar .
   a�adir . a ._MEJORNODO
caso . no estaba en ).( ni (.)
   a�adir . a ).(
   a�adir . a ._MEJORNODO
   f'(.) := g(.) + h'(.)

