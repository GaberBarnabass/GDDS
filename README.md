# GDDS - Gastroenterological Disease Detection System

Questo progetto è uno strumentio diagnostico che ha come obiettivo quello di identificare le malattie e i disturbi dell'apparato digerente.
Attualmente è capace di individuare:  

- IBS sindrome dell'intestino irritabile;  
- UC Rettocolite Ulcerosa;  
- CM Morbo di Chron.

Ad eccezione dell'IBS, per UC e CM può anche essere identificata la gravità della malattia:

- Lieve;
- Grave;
- Fulminante.

A tale scopo viene utilizzato un sistema basato su conoscenza, il quale utilizza un insieme di regole e una rete bayesiana, grazie alla quale non solo è possibile predire una malattia da da sintomi, ma anche la probabilità del verificarsi un sintomo data la malattia e la presenza di altre sintomatologie.

A causa della mancanza di dati reali, si è prima effettuato uno studio per ognuna delle tre malattie:

ibs: https://www.niddk.nih.gov/health-information/digestive-diseases/irritable-bowel-syndrome/definition-facts  
uc https://www.niddk.nih.gov/health-information/digestive-diseases/ulcerative-colitis/definition-facts  
crohn https://www.niddk.nih.gov/health-information/digestive-diseases/crohns-disease/definition-facts

Successivamente, basandosi su quanto appreso si è creato un dataset artificiale composto da 10.000 esempi per malattia.