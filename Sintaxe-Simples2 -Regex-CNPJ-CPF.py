import re

def extrair_cnpj_cpf(texto):
    padrao_cnpj =  r'\b\d{2}.\d{3}\.\d{3}\/\d{4}-\d{2}\b'
    padrao_cpf =  r'\b\d{3}.\d{3}\.\d{3}-\d{2}\b'
    cnpjs = re.findall(padrao_cnpj, texto)
    cpfs = re.findall(padrao_cpf, texto)
    return cnpjs, cpfs

texto = "Texto com um cnpj 12.123.687/0001-90 "
texto +=" e um cpf 384.116.728-40 dentro dele"

cnpjs, cpfs = extrair_cnpj_cpf(texto)

print("CNPJs encontrados:", cnpjs)
print("CPFs encontrados:", cpfs)
