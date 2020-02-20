#!/usr/bin/python3


with open('lista-cpf.txt') as f:
	linhas = [line.rstrip() for line in f]
	cpf_unicos = {}
	print(linhas[0])
	for linha in linhas:
		cpf_unicos[linha] = cpf_unicos.get(linha, 0) + 1

	# print(len(cpf_unicos))
	# print(cpf_unicos.get('﻿595.680.187-71'))
	with open('lista-cpf-unicos.txt', 'w') as f_saida:
		for cpf in cpf_unicos:
			f_saida.write(cpf)
