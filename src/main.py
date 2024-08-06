import sys
from read_input_file import read_file
from gurobi import gurobi

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python main.py <caminho_para_o_arquivo_de_entrada>")
        sys.exit(1)

    file_path = sys.argv[1]
    n, m, b, w, p = read_file(file_path)
    gurobi(n, m, b, w, p)