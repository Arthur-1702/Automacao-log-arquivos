De forma a minimizar o nível de intervenção humana em diretórios para criação de logs e backup, foi escrito um script Python, para automatizar as seguintes ações: 

- Listar todos arquivos (nome, tamanho, data de criação, data da última modificação) localizados no caminho (Ex.: /home/valcann/backupsFrom); 

- Salvar o resultado no arquivo (Ex.: backupsFrom.log) em (Ex.: /home/valcann/); 

- Remover todos os arquivos com data de criação superior a 3 (três) dias; 

- Copiar todos os arquivos os arquivos com data de criação menor ou igual a 3 (três) dias em (Ex.: /home/valcann/backupsTo); 

- Salvar o resultado no arquivo backupsTo.log em (Ex.: /home/valcann/). 


Pra isso, foi criada uma classe FileSystem, que contém os métodos log(),removeOldFiles() e copyFile, e respectivamente faz a lista de arquivos em log, remove os arquivos com data de criação superior a 3 dias e copia os arquivos para o backup.
