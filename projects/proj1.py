# coding: utf-8

import sys
import io
import urllib.request as request

BUFF_SIZE = 1024 
address = "http://livropython.com.br/dados.zip"

'''
    times = length / BUFF_SIZE 

    --> BUFF_SIZE: Quantidade máxima de bytes que são lidos de uma vez, na reposta recebida do servidor.
        length: comprimento do arquivo.
        times: Quantidade de iterações para ler completamente o arquivo.
    
    if length % BUFF_SIZE > 0:
        times += 1
    
    --> Se length % BUFF_SIZE é diferente de zero, significa que length não é
        um múltiplo de BUFF_SIZE. Assim, é adicionada mais uma chamada extra para
        garantir que o arquivo será lido completamente.

    for time in range(times):
        output.write(response.read(BUFF_SIZE))
        print("Downloaded %d" % (((time * BUFF_SIZE)/length)*100))

    --> O laço se repetirá 'times' vezes, isto é, fará a quantidade necessária de chamadas
        para que o arquivo seja lido completamente.
        response: Objeto HTTP da conexão estabelecida. Já retorna também a resposta do servidor(arquivo).
        response.read(BUFF_SIZE): Realiza a leitura em pedaços de 1024 bytes (1KB) por vez da resposta do servidor.
        output.write(response.read(BUFF_SIZE)): Grava 1KB de dados por vez da resposta recebida do servidor.
        print("Downloaded %d" % (((time * BUFF_SIZE)/length)*100)): A cada interação, mosta a porcentagem lida do arquivo baixado.
'''
def download_length(response, output, length):
    times = length // BUFF_SIZE  
    if length % BUFF_SIZE > 0:
        times += 1
    for time in range(times):
        output.write(response.read(BUFF_SIZE))
        print("Downloaded {}%".format(((time * BUFF_SIZE)/length)*100))


'''
    Semelhante a função anterior, porém, só para de ler a resposta do servidor quando não
    houver mais dados.
'''
def download(response, output):
    total_downloaded = 0
    while True:
        data = response.read(BUFF_SIZE)
        total_downloaded += len(data)
        if not data:
            break
    output.write(data)
    print('Downloaded {bytes}'.format(bytes=total_downloaded))

# Realiza uma requisição HTTP, na URL passada como argumento.
# Cria um arquivo para escrita.
# Verifica se no cabeçalho HTTP está informado o tamanho do arquivo.
#   - Se não estiver vazio, chama download_length().
#   - Se estiver vazio, chama download().
# Quando tudo terminar, fecha a conexão HTTP e o arquivo.

def main():
    response = request.urlopen(address)                 
    out_file = io.FileIO("dados.zip", mode="w")             
    content_length = response.getheader('Content-Length')   
    if content_length:
        length = int(content_length)
        download_length(response, out_file, length)
    else:
        download(response, out_file)
    response.close()
    out_file.close()
    print("Finished")


# Função main
if __name__ == "__main__":
    main()