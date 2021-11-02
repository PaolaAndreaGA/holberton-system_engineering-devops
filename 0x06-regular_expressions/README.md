# Expresiones Regulares. Conócelas y Piérdeles el miedo

PublishedHace 13 años

Última actualizaciónHace 9 años

Una expresión regular es una cadena de caracteres que es utilizada para describir o encontrar patrones dentro de otros strings, en base al uso de delimitadores y ciertas reglas de sintaxis. La mayoría de los programadores no se dan el tiempo de aprender a aplicar las expresiones regulares, lo cual es una lástima ya que son de gran utilidad. Cuando aprendas a aplicar las expresiones regulares, te darás cuenta de lo poderosas que son, la gran cantidad de problemas que pueden resolver, y lo mucho que aumentará tu productividad al programar.

Si es la primera vez que te acercas al concepto de expresiones regulares –también conocidas como “regex” en el argot de la programación– te animará saber que muy probablemente ya las has usado aún sin saberlo, al menos en su vertiente más básica. Por ejemplo, el comando dir *.txt para obtener un listado de todos los archivos con extensión txt es una forma muy sencilla de expresión regular, donde el patrón * coincide con cualquier cadena de caracteres.

Veamos el ejemplo sencillo de un patrón y las cadenas con las que podría coincidir:

am // este es nuestro patrón. Si lo comparamos con:
am // coincide
ambicion // coincide
campamento // coincide
mano // no coincide

Se trata sencillamente de ir cotejando un patrón (pattern) -que en este ejemplo es la secuencia de letras ‘am’- con una cadena (subject) y ver si dentro de ella existe la misma secuencia. Si existe, decimos que hemos encontrado una coincidencia (match).

Estos ejemplos son muy sencillos ya que utilizan patrones literales, es decir que solo encontramos coincidencias cuando hay una ocurrencia exacta. De hecho, normalmente no es necesario usar expresiones regulares si vamos a textos exactos. Todos los lenguajes tienen funciones de string para este propósito. El poder de las expresiones regulares radica precisamente en la flexibilidad de los patrones, que pueden ser confrontados con cualquier palabra o cadena de texto que tenga una estructura conocida.

Caracteres y metacaracteres
Nuestro patrón puede estar formado por un conjunto de caracteres (letras, números o signos) acompañado de metacaracteres que representan a otros caracteres o permiten una búsqueda contextual.
Los metacaracteres reciben este nombre porque no se representan a ellos mismos, sino que son interpretados de una manera especial. Por ejemplo, a través de metacaracteres podemos definir diferentes condiciones tales como agrupaciones, alternativas, comodines, multiplicadores, etcétera.

Los metacaracteres más usados son: . * ? + [ ] ( ) { } ^ $ | \.

A continuación los explicamos de forma detallada.

Metacaracteres de posicionamiento, o anclas
Los signos ‘^’ y ‘$’ sirven para indicar donde debe estar situado nuestro patrón dentro de la cadena para considerar que existe una coincidencia.Cuando usamos el signo ‘^’ queremos decir que el patrón debe aparecer al principio de la cadena de caracteres comparada. Cuando usamos el signo ‘$’ estamos indicando que el patrón debe aparecer al final del conjunto de caracteres. O más precisamente, antes de un caracter de nueva línea.

Ejemplo:

![](http://www.sg.com.mx/images/stories/200705/programacion1.gif)

De la misma forma, la expresión ^$ se puede utilizar para encontrar líneas vacías, donde el inicio de una línea es inmediatamente seguido por el final de ésta.

Los metacaracteres ‘^’ y ‘$’ también conocidos como anclas (anchors) ya que no representan otros caracteres, sino posiciones en una cadena.

Escapando caracteres
Puede suceder que necesitemos incluir en nuestro patrón algún metacaracter como signo literal, es decir, por si mismo y no por lo que representa. Para indicar esta finalidad usaremos como caracter de escape a la barra invertida ‘\’. Como regla general, la barra invertida \ convierte en normales a los caracteres especiales.

Ejemplo:

![](http://www.sg.com.mx/images/stories/200705/programacion2.gif)

El comodín ‘.’
El metacaracter ‘.’ (punto) es el comodín por excelencia. Un punto en el patrón representa cualquier caracter excepto nueva línea.

Ejemplo:

![](http://www.sg.com.mx/images/stories/200705/programacion2a.gif)

Observa en el ejemplo anterior como el patrón coincide con cualquier caracter (incluido el de espacio en blanco) seguido de una l.

Clases de caracteres
Los corchetes ‘[ ]’ definen una clase de caracteres y permiten encontrar cualquiera de los caracteres dentro de un grupo. Imaginemos que queremos encontrar la palabra “niño”, pero también queremos encontrar en caso de que la hayan escrito con n el lugar de ñ. Podríamos lograr esto con una clase de caracter, de forma que la expresión regular ni[ñn]o se interpretaría como “n, seguida de i, seguida ya sea de ñ o n, seguida de o”.

La mayoría de los metacaracteres pierden su significado al ser utilizados dentro de clases de caracteres. Es así que la expresión [a.] se refiere literalmente a la letra a y al caracter punto. Un caso especial es el caracter ‘^’, que al ser utilizado al comienzo de una clase de caracteres significa negación. Es decir que la expresión [^a] se refiere a cualquier cadena que NO contenga la letra a. Este significado se pierde si el ‘^’ no está al inicio de la clase de caracteres, así que la expresión [a^] se refiere a la letra a y al caracter ^ literalmente.

Así como la mayoría de los metacaracteres pierden su significado especial al ser utilizados dentro de corchetes, existe un caracter que solamente al ser utilizado dentro de corchetes adquiere un significado especial. Este es el caracter ‘-‘ (guión), el cual se utiliza dentro de una clase de caracteres para indicar un rango. Por ejemplo, si queremos referirnos a un caracter hexadecimal, en lugar de definir la clase [01234567890abcdefABCDEF] utilizaríamos [0-9a-fA-F], que es mucho más conveniente.

Veamos ejemplos con algunas clases de caracteres:

![](http://www.sg.com.mx/images/stories/200705/programacion_x.gif)

Algunos lenguajes de programación definen atajos para clases de caracteres que son comúnmente utilizadas. La siguiente tabla muestra algunos de los atajos más comunes:

![](http://www.sg.com.mx/images/stories/200705/programacion4.gif)

Delimitación
Los paréntesis se pueden utilizar para definir un subconjunto dentro de una expresión. Por ejemplo, para capturar la parte correspondiente al hostname de un url, utilizaría una expresión como http://([^/]) lo que estoy diciendo con esta expresión es que primero tengo la secuencia de caracteres “http://” y seguido de esto tengo una subexpresión, la cual estoy delimitando con los paréntesis, y aplico una expresión a este segmento en específico, en este caso estoy buscando una cadena que coincide con cualquier caracter excepto el ‘/’.

Alternativas
El metacaracter ‘|’ (barra vertical) significa “o” (or). Permite buscar diferentes alternativas de expresiones (más bien subexpresiones), dentro de una sola expresión.

Esa definición sonó muy enredada, así que mejor expliquémoslo con un ejemplo. Imaginemos que tenemos la expresión Doña y la expresión Don. Cada una es una expresión separada, pero si definimos la expresión Don|Doña entonces tenemos una sola expresión que coincide con cualquiera de las dos subexpresiones.

También podemos utilizar los paréntesis para delimitar el alcance de una alternativa. En este caso, la expresión Do(n|ña) nos daría el mismo resultado que la expresión Don|Doña. Sin embargo, hay que tener cuidado con abusar del uso de paréntesis, porque podemos terminar con expresiones difíciles de entender, y por lo tanto de mantener.

Cuantificadores o Multiplicadores
Los metacaracteres que hemos visto nos informan si nuestro patrón coincide con la cadena a comparar. Pero ¿y si queremos comparar con nuestra cadena un patrón que puede estar cero, una o mas veces? Para esto usamos un tipo especial de metacaracteres: los multiplicadores.

Estos metacaracteres se aplican al caracter (o agrupación) que les precede, e indican el número de veces que se puede encontrar dicho elemento para que haya una ocurrencia. Los tres metacaracteres cuantificadores son ‘?’ ‘*’ ‘+’. El ‘?’ indica una multiplicidad de 0 o 1, el ‘*’ indica una multiplicidad de 0 a n, y el ‘+’ indica una multiplicidad de 1 a n. Los siguientes ejemplos dejan esto más claro:

![](http://www.sg.com.mx/images/stories/200705/programacion5.gif)
También es posible indicar la multiplicidad exacta que es aceptable para un cuantificador. Para esto se utilizan las llaves ‘{ }’, y la sintaxis es primero indicar el valor mínimo de la multiplicidad, seguido de una coma, y luego el valor máximo de la multiplicidad.

![](http://www.sg.com.mx/images/stories/200705/programacion6.gif)
Conclusión
En este artículo hemos estudiado la sintaxis y metacaracteres utilizados para definir expresiones regulares. Ahora lo que queda es que escojas el lenguaje de programación de tu preferencia y comiences a experimentar con el uso de expresiones regulares. Te garantizo que es una habilidad que te será de gran utilidad.

**Referencias**
• Autor anónimo. “Expresiones regulares”.
**www.ignside.net/man/php/regex.php**
• Mike Malone. “The bare minimum that every programmer should know about regular expressions.
**http://immike.net/blog**