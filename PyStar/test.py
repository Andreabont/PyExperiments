import Path
import Grid

griglia = Grid.GridWithWeights(30,30)

griglia.set_wall((3,3),(3,20))
griglia.set_wall((10,3),(10,20))
griglia.set_wall((3,3),(10,3))
griglia.set_wall((4,20),(8,20))
griglia.set_wall((5,15),(10,15))
griglia.set_wall((4,10),(8,10))

print("Ricerca breadth first")
ricerca_percorso_bfs = Path.breadth_first_search(griglia, (2,3), (4,4))
Grid.drawGrid(griglia, mark = [(2,3),(4,4)],  draw_function =  lambda current : Path.arrow_draw(ricerca_percorso_bfs, current))

print("Ricerca dijkstra")
ricerca_percorso_dijkstra = Path.dijkstra_search(griglia, (2,3), (4,4))
Grid.drawGrid(griglia, mark = [(2,3),(4,4)],  draw_function =  lambda current : Path.arrow_draw(ricerca_percorso_dijkstra, current))

print("Ricerca A*")
ricerca_percorso_astar = Path.a_star_search(griglia, (2,3), (4,4))
Grid.drawGrid(griglia, mark = [(2,3),(4,4)],  draw_function =  lambda current : Path.arrow_draw(ricerca_percorso_astar, current))

print("Percorso finale: ")
percorso = Path.reconstruct_path(ricerca_percorso_bfs, (2,3), (4,4))
Grid.drawGrid(griglia, mark = percorso)
