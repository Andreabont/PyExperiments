import Path
import Grid

griglia = Grid.GridWithWeights(30,30)

griglia.set_wall((3,3),(3,20))
griglia.set_wall((10,3),(10,20))
griglia.set_wall((3,3),(10,3))
griglia.set_wall((4,20),(8,20))
griglia.set_wall((5,15),(10,15))
griglia.set_wall((4,10),(8,10))

def disegna(nome, algoritmo):
    ricerca = algoritmo(griglia, (2,3), (4,4))
    generatore_calcolo =  Grid.drawGrid(griglia, mark = [(2,3),(4,4)],  draw_function =  lambda current : Path.arrow_draw(ricerca, current))
    percorso = Path.reconstruct_path(ricerca, (2,3), (4,4))
    generatore_percorso = Grid.drawGrid(griglia, mark = percorso)
    print("Eseguo algoritmo '%s':" % nome)
    for (a,b) in zip(generatore_calcolo, generatore_percorso):
        print( a,b )

disegna("Breadth first", Path.breadth_first_search)
disegna("Dijkstra", Path.dijkstra_search)
disegna("A*",Path.a_star_search)
