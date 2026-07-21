unprinted_designs=['phonecase','robot pendant','dodecahedron']
completed_models=[]
def printModels(unprinted, completed):
    while unprinted:
        current_design=unprinted.pop()
        print(f"Printing model: {current_design}")
        completed.append(current_design)

def showCompletedModels(completed):
    print("\nThe following models have been printed:")
    for model in completed:
        print(model)


printModels(unprinted_designs, completed_models)
showCompletedModels(completed_models)