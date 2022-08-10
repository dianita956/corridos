#data frames#
import numpy as np
import pandas as pd


corridos = dict({'Title': ['la toma de Matamors',
                    'el general Cortinas'],
                    
            'Lyrics':['''Voy a cantar estos versos,
                    pongan mucha atención todos,
                    voy a cantar la tragediade
                    de la Heroica Matamoros.
                    
                    Dia martes tres de junio
                    de mil novecientos trece,
                    a las diez de la mañana
                    Lucio Blanco se aparece.
                    
                    Pues traía miles de hombres,
                    bien armados y valientes
                    para tomar esa plaza y
                    hacer correr a las gentes.

                    La gente de Matamoros
                    ya resuelta toda estaba
                    a defender a su pueblo
                    aunque la vida costara.

                    Por hojas sueltas pidieron
                    la plaza al Mayor Ramos,
                    diciendo: -Si no la entregan
                    de todos modos entramos. -

                    Cuando estas hojas llegaron
                    a manos del Mayor Ramos,
                    sonriendo dijo al enviado:
                    -La plaza no la entregamos.

                    Pues decía el Mayor Ramos,
                    lo mismo que Barragán:
                    -Lo que es Carranza no gana
                    y si no ya lo verán.

                    Ya la hora se llegó,
                    pues ya se le cumple el plazo,
                    por dondequiera se oía
                    la bala y el cañonazo.

                    La gente de Matamoros
                    muy contenta se quedaba
                    cuando vino la noticia
                    que Blanco se retiraba.
                    Pero un repique oportuno,
                    que no saben quién lo dio,
                    alentó a los carrancistas
                    y Blanco se devolvió.

                    Para las tres de la tarde
                    había muertos y heridos,
                    y los soldados de línea
                    se iban a Estados Unidos.

                    El empuje fue terrible,
                    la defensa por demás;
                    eran pocos los de adentro,
                    los de afuera muchos más.

                    Los valientes voluntarios
                    de López y Chazarreta
                    se salían de las trincheras
                    a tirar a la banqueta.

                    A las diez de la mañana
                    algunas casas quemaron,
                    pero éstas fueron venganzas
                    que llegando consumaron.

                    Agarraron prisioneros
                    a unos niños que pelearon,
                    y otro día en el Parián
                    a las seis los fusilaron.

                    Pues lo niños que pelearon
                    con bastante decisión
                    al enemigo causaron
                    bastante admiración.

                    Pero un antiguo artillero
                    que era también gobiernista,
                    a ese no le hicieron nada,
                    lo defendió un carrancista.

                    Pero a Antonio Chazarreta
                    le tocó muy mala suerte,
                    lo cogieron prisionero
                    y fue sentenciado a muerte.

                    Las gentes de Matamoros
                    perdieron toda esperanza
                    al oír que por las calles
                    gritan que viva Carranza.

                    Las gentes de Matamoros
                    en Texas aventurando,
                    dicen que no han de volver
                    mientras Lucio tenga el mando.

                    Ya con ésta me despido,
                    me compadezco de todos,
                    y con tristeza les digo
                    que perdimos Matamoros. ,
                    
                    Ese general Cortina
                    el libre y muy soberano,
                    han subido sus honores
                    porque salvó a un mexicano.
                    
                    Viva el general Cortinas
                    que de su prisión salió,
                    vino a ver a sus amigos
                    que en Tamaulipas dejó.
                    
                    Los americanos hacían huelga,
                    borracheras en las cantinas,
                    de gusto que había muerto
                    ese general Cortinas.'''],
                    'Sentiment Score':[' 10, 10 ']})
                    
df=pd.DataFrame.from_dict(corridos, orient ='index')
df

compression_opts = dict(method='zip', archive_name='out.csv')
df.to_csv('out.zip', index=False, compression=compression_opts)

import os
os.makedirs('/c/users/dmlpz/Corridos', exist_ok=True)
df.to_csv('/c/users/dmlpz/Corridos/out.csv')
