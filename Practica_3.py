void DFS ( grafo & g,int s){
    nodoVisitado[s]=true;
    procesarNodo(s);
    list<int>::iterator it;

    for(it=g.lados[s].begin(); it!=g.lados[s].end(); ++it){
        if(!nodoVisitado[*it]){
            nodoPadre[*it]=s;
            DFS(g,*it);
        }else if(!nodoProcesado[*it]){
            procesarLado(s,*it);
        }
    }
    nodoProcesado[s]=true;
}
