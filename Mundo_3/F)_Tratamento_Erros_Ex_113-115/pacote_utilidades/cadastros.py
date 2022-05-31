def cadastro(arq,nome,idade):
    with open(arq,'+a') as arquivo:
        arquivo.write(f' Nome: {nome} - Idade {idade}\n')

def lerArquivo(arq):
    with open(arq,'r') as arquivo:
        ler = arquivo.readlines()
        c=0
        for p in ler:
            print(ler[c])
            c+=1


