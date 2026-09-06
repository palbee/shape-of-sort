import PIL.Image
import numpy as np
import tabulate

from shape_of_sort.algs import algorithms
from shape_of_sort.algs import prepare_data


def main():
    n_cells = 256
    report = []
    start_data = prepare_data(n_cells, shuffled=False, reverse=True)
    for alg_name in algorithms.keys():
        trace, compares = algorithms[alg_name](start_data[:])
        # with open(f"{alg_name}.dot", 'w') as dest:
        #     render(trace, dest)
        memory = np.zeros((len(trace), n_cells, 3), dtype="uint8")

        for row, cols in enumerate(trace):
            cols = np.array(cols)
            memory[row, :, 0] = cols / n_cells * 256
            memory[row, :, 1] = cols / n_cells * 256
            memory[row, :, 2] = cols / n_cells * 256
        img = PIL.Image.fromarray(memory, mode="RGB")
        img = img.convert("RGB")
        img.save(f"{alg_name}_{n_cells}_memory.png")
        del img
        checks = np.zeros((len(compares), n_cells), dtype=bool)
        for row, cols in enumerate(compares):
            checks[row, cols] = 1
        img = PIL.Image.fromarray(checks)
        img.save(f"{alg_name}_{n_cells}_compares.png")

        report.append(
            {'Algorit hm': alg_name, 'Compares': len(checks),
             'Assignments': len(trace)},
        )

    print(tabulate.tabulate(report, headers='keys'))
