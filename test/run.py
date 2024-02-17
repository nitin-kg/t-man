import json
import subprocess
import sys

def run_experiment(configuration):
    command = ['python', 'main.py', str(configuration['N']), str(configuration['K']), configuration['topology']]
    subprocess.run(command)
    plot_command = ['python', 'plot.py', f'{configuration["topology"]}_N{configuration["N"]}_k{configuration["K"]}.txt']
    subprocess.run(plot_command)

def main():
    test_topology = sys.argv[1]
    # Load configurations from experiments.json
    with open(f'{test_topology}.experiments.json', 'r') as file:
        configurations = json.load(file)

    # Loop through configurations and run experiments
    for config in configurations:
        run_experiment(config)

    # Exit the script when the work is done
    sys.exit(0)

if __name__ == "__main__":
    main()
