# Algoritmidiricercastudenti

Il progetto contiene l'implementazione degli algoritmi di ricerca presentati durante il corso di Intelligenza Aritificiale I nell'ambito del corso di laurea in [Filosofia-e-Intelligenza-Artificiale] (https://corsidilaurea.uniroma1.it/it/corso/2023/31774/home). Tale implementazione va completata
in corrispondenza dei metodi la cui definizione è preceduta da "TODO". In particolare i metodi
sui quali verrà svolto il lavoro si trovano nella cartella "algorithms". Ulteriori commenti 
contrassegnati dal flag "TODO" sono stati spesso inseriti anche all'interno dei metodi da
completare per fornire dei suggerimenti.


## Dipendenze (Ambiente di lavoro)

- [ ] [Python] (https://www.python.org/downloads/), versione 3.8 o superiore 
- [ ] Package Installer per Python - [pip] (https://pip.pypa.io/en/stable/installation/#get-pip-py) 

Occorre avere installato sulla propria macchina un editor di codice; Si raccomanda l'uso 
di [vs-code] (https://code.visualstudio.com/) ma non è necessario.


## Dipendenze (librerie)

Creiamo un python virtual environment ed installiamo al suo interno le librerie necessarie.
Le istruzioni relative alla creazione di un virtual environment e all'installazione delle librerie al
suo interno si trovano nella [documentazione] (https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) riportata. Tutti le librerie richieste si possono installare
semplicemente attraverso "pip install X" da lanciare in un terminale aperto all'interno 
del virtual environment che si intende utilizzare. Sostituire X rispettivamente con:

- [ ] [matplotlib] (https://pypi.org/project/matplotlib/): per la visualizzazione grafica
- [ ] [networkx] (https://pypi.org/project/networkx/): per la creazione e gestione di grafi
- [ ] [xlrd] (https://xlrd.readthedocs.io/en/latest/): per la lettura di file in formato .xls 

Un passaggio ulteriore è richiesto per il setup della seguente libreria:

- [ ] [graphviz] (https://pypi.org/project/graphviz/), per la visualizzazione interattiva degli algoritmi: 
    la libreria deve essere installata come le altre in primo luogo mediante pip nel virtual environment 
    ed in seguito anche sul sistema seguendo le seguenti [istruzioni] (https://forum.graphviz.org/t/new-simplified-installation-procedure-on-windows/224)

## Esecuzione 

Il codice va eseguito dal proprio virtual environment. Se si utilizza l'editor vs-code 
la sezione "Working with Python interpreters" della seguente [documentazione] (https://code.visualstudio.com/docs/python/environments).
Altrimenti è sufficiente eseguire il codice da terminale, come indicato nel seguito, dopo
aver attivato il virtual environment (c.f. "Activate a virtual environment" in questo [documento] https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).

Si lanci il codice in una delle due configurazioni riportate:

- [ ] con 1 parametro che può essere "expand" o "walkback". Nel primo caso vengono eseguiti 
dei test sulla funzione di espansione chiamata a partire da un nodo del problema di ricerca,
mentre nel secondo vengono lanciati i test associati alla funzione che opera backtracking (i.e. 
visita di tutti i nodi genitore) a partire da un nodo del problema di ricerca. Esempi di esecuzione 
sono quindi "python main.py expand" e "python main.py walkback".

- [ ] con 5 parametri dove il primo indica il file .xls contenente il problema di ricerca in input, 
il secondo l'algoritmo di ricerca da eseguire (bfs, dfs, ucs, astar), 
il terzo l'ordine con cui le azioni vengono considerate dalla funzione di espansione a partire 
da un nodo (y se lessicografico e n se lessicografico inverso), ed infine gli ultimi due che 
indicano se stampare o meno (y o n) a schermo un report rispettivamente sul problema di ricerca 
letto da file e sul relativo grafo ad esso associato.

Nel secondo caso le configurazioni di esecuzione possibili sono:

- [ ] "X bfs y/n y/n y/n"
- [ ] "X dfs y/n y/n y/n"
- [ ] "X ucs y/n y/n y/n"
- [ ] "X astar y/n y/n y/n"

dove X è il file in input da posizionare nella cartella "resources",
bfs indica breadth-first-search (o ricerca in ampiezza), dfs indica 
depth-first-search (o ricerca in profondità), ucs indica uniform-cost-search,
e astar denota A* Search.

Si noti che, senza aver prima implementato quanto richiesto, l'esecuzione del codice 
solleverà un'eccezione di tipo "Not Implemented".