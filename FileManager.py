import os
import time
import shutil

class FileSystem:
    def log(self, pathFile, pathLog):
        # Abrir o arquivo log para escrita
        f = open(pathLog, "w")
        # Escrever o cabeçalho no arquivo log
        f.write("Nome, Tamanho (bytes), Data de criação, Data da última modificação\n")    
        # Passa na lista de arquivos do diretório
        for filename in os.listdir(pathFile):
            file_path = os.path.join(pathFile, filename)
            if os.path.isfile(file_path):
                file_info = os.stat(file_path)
                # Obter informações do arquivo
                file_size = file_info.st_size
                creation_time = time.ctime(file_info.st_ctime)
                modification_time = time.ctime(file_info.st_mtime)
                # Escrever informações do arquivo no log
                f.write("{}, {}, {}, {}\n".format(filename, file_size, creation_time, modification_time))
        f.close()
    
    def removeOldFiles(self,path):
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path):
                # Tempo atual em segundos
                current_time = time.time()
                # Calcular a diferença entre a data de criação do arquivo e o tempo atual em segundos
                file_info = os.stat(file_path)
                time_diff = current_time - file_info.st_ctime
                if time_diff > 259200: # 3 dias em segundos
                    # Remover o arquivo se ele tiver mais que 3 dias
                    os.remove(file_path)

    def copyFile(self, pathFrom, pathTo):
        # Lista de arquivos no diretório de origem
        arquivos = os.listdir(pathFrom)

        # Passa sobre a lista de arquivos e copia para o diretório de destino
        for arquivo in arquivos:
            caminho_origem = os.path.join(pathFrom, arquivo)
            caminho_destino = os.path.join(pathTo, arquivo)
            shutil.copy2(caminho_origem, caminho_destino)


script = FileSystem()
origem = "/home/valcann/backupsFrom"
log = "/home/valcann/backupsFrom.log"
destino = "/home/valcann/backupsTo"
novoLog = "/home/valcann/backupsTo.log"
script.log(origem,log)
script.removeOldFiles(origem)
script.copyFile(origem,destino)
script.log(destino,novoLog)