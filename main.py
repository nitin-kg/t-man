from algo import TMAN
import sys
import pandas as pd
import matplotlib.pyplot as plt

def main():

    # input and file name handling
    topology_dict = {
        'R': 'ring',
        'S': 'spectacles'
    }

    if len(sys.argv) != 4: 
        print("Usage: python3 main_class.py <total_nodes> <total_neighbors> <topology>")
        print("Example: python3 main_class.py 100 5 ring")
        exit(1)

    N = int(sys.argv[1])
    k = int(sys.argv[2])
    topology = topology_dict[sys.argv[3]]

    FILE_NAME = f'{sys.argv[3]}_N{N}_k{k}'

    # create FILE_NAME txt file to store sum of distances
    with open(f'{FILE_NAME}.txt', 'w') as f:
        f.write('cycle,sum_of_distances\n')

    if topology not in ['ring', 'spectacles']:
        print("Topology must be either 'ring' or 'spectacles'")
        exit(1)

    tman = TMAN(N, k, topology)
    nodes = tman.get_nodes()

    # The sum of distances of neighboring nodes during the initialization phase
    initial_sum_of_distances = tman.calculate_total_node_distance(nodes)
    # save the initial sum of distances in the csv file
    with open(f"{FILE_NAME}.txt", "a") as f:
        f.write(f"0,{initial_sum_of_distances}\n")

    # Perform network evolution
    tman.evolve_topology(nodes)

    def plot_cs_txt():
        df = pd.read_csv(f'{FILE_NAME}.txt', delimiter=',')
        df.columns = ['cycle', 'sum_of_distances'] 
        plt.bar(df['cycle'], df['sum_of_distances'])
        plt.xlabel('Cycle')
        plt.ylabel('Sum of Distances')
        plt.title('Sum of Distances vs Cycle')
        plt.savefig(f'{FILE_NAME}.png')
        plt.close()

    plot_cs_txt()

if __name__ == "__main__":
    
    main()