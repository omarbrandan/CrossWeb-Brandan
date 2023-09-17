Es una página web creada con Django por Omar Brandán donde fans de CrossFit, en un estilo de blog pero acotado, pueden sugerir atletas de la élite del mundo competitivo de este deporte que no están registrados en la página oficial de CrossFit, los cuales se merecen estar ahí.
También funciona para sugerencias de competencias que están emergiendo y actualmente no se las conoce, así un atleta que quiera competir esté en conocimiento de todos los torneos.
Y por último, para sugerencias de productos que no están publicados en ninguna página oficial y que son necesarios para el entrenamiento diario. Usualmente serían productos nuevos que buscan reemplazar a los tradicionales con ofertas disruptivas.

Hay cuatro secciones:

Inicio;
Competitions, son las competencias de la temporada;
Athletes, son los múltiples atletas del año;
Store, es la tieda.

Con los formularios de Competitions, Athletes y Store, se puede agregar ítems a dichas secciones.
Sólo los usuarios logueados pueden crear, editar y eliminar. En caso de no estarlo, sólo pueden visualizar los listados y detalles.

También se puede buscar a un atleta por su apellido.

El orden para probar sería:

Inicio ---> /app-coder/
Athletes ---> /app-coder/athletes/
Competitions ---> /app-coder/competitions/
Store ---> /app-coder/store/

AthletesFormulario ---> /app-coder/athletes-formulario/
CompetitionsFormulario ---> /app-coder/competitions-formulario/
StoreFormulario ---> /app-coder/store-formulario/

BusquedaApellido ---> /app-coder/busqueda-apellido/

Admin ---> /admin/ ---> Username (Admin): omar 
                        Password: Omar123

                        Username: dave
                        Password: dave_2023

                        Username: carlos 
                        Password: Homero1234