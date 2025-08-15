#Lista de onibus conhecidas
buss_list = []
with open('out.csv', 'r') as arquivo:
    for linha in arquivo:
        #separa os elementos pelas ','
        str_arr = linha.strip().split(",")
        
        #Pega os elementos a partir da segunda posição
        valores = [int(item.split(':')[0]) for item in str_arr[1:]]
        soma = sum(valores)
        
        
        found = False
        for linha in buss_list:
            if linha["line"] == str_arr[0]:
                found = True
                linha["pass"] += soma
        if not found:
            buss_list.append({"line": str_arr[0], "pass": soma})
            
# Ordena a lista de dicionários pelo campo "pass".
# - sorted(buss_list, ...): cria e retorna uma NOVA lista ordenada (não altera a original).
# - key=lambda x: x["pass"]: para cada item (x) da lista, usa x["pass"] como chave de comparação.
# - reverse=True: ordena em ordem decrescente (do maior para o menor) ou false para ordem crescente.
buss_list = sorted(buss_list, key=lambda x: x["pass"], reverse=True) 

print(buss_list)
