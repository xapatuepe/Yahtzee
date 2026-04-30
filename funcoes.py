def guardar_dado(rolados,estoque,índice):
    estoque.append(rolados[índice])
    del estoque[índice]
    return [rolados,estoque]