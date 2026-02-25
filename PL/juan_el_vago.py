import pulp
from pulp import LpAffineExpression as Sumatoria
def juan_el_vago(trabajos):
    laburo = []
    for i in range(len(trabajos)):
        laburo.append(pulp.LpVariable("t" + str(i), cat="Binary"))

    problem = pulp.LpProblem("Juan el vago", pulp.LpMaximize)
    for i in range(1, len(laburo)):
        problem += laburo[i] + laburo[i-1] <= 1
    problem += sum([laburo[i] * trabajos[i] for i in range(len(laburo))])
    problem.solve()
    return list(map(lambda ti: pulp.value(ti), laburo))

if __name__ == "__main__":
    print(juan_el_vago([100, 5, 50, 1, 1, 200]))
