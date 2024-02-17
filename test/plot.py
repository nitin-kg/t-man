import matplotlib.pyplot as plt

# write a script to take csv file name as input and plot a bar plot between it's two columns
# and save the plot as png file
# Example: python3 plot.py ring_N100_k5.csv

import sys
import pandas as pd

def plot_cs_txt(file_name):
    df = pd.read_csv(file_name, delimiter='\t')
    plt.bar(df['cycle'], df['sum_of_distances'])
    plt.xlabel('Cycle')
    plt.ylabel('Sum of Distances')
    plt.title('Sum of Distances vs Cycle')
    # remove .csv from the file_name
    file_name = file_name.split('.')[0]
    plt.savefig(f'{file_name}.png')
    plt.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 plot.py <FILE_NAME>")
        print("Example: python3 plot.py R_N100_k5.txt")
        exit(1)
    FILE_NAME = sys.argv[1]
    plot_cs_txt(FILE_NAME)