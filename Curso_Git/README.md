# COMANDOS IMPORTANTES:
### OBS.: Nem todas essas informações fazem parte do Video assistido, e sim de ANOTAÇÕES *_PESSOAIS_* que fiz ao decorrer dos meus estudos.
**Qualquer informação incorreta, se possivel, avisar** :smile: <br> <br>
![Curso em Video](https://github.com/GabrielRioo/Curso_em_Video/blob/master/Curso_Git/curso-em-video-cor.png)
* Visual Code
   * `Ctrl` + `click` em uma pastar com arquivo inexistente = Cria a pasta + o arquivo
   * No paramentro `src` - `Ctrl` + `Espaço` = Procura as pastas. 
   <br>
* Terminal

Comando | O QUE FAZ
---:|:---
mkdir | Cria um folder
touch | Cria um Arquivo
rm | Remove um arquivo
ls/dir | Lista os Arquivos dentro do Folder
cd <folder>| Acessa a Pasta digitada
cd .. | Volta um diretorio

* Git (_tentei por na ordem, para q eu possa localizar e realiza-las na ordem._)

Comando | O QUE FAZ
:---|:---
git config --global user.name "_seuNome_" | Configura o git com seu nome
git config --global user.email "_seuEmail_" | Configura o git com seu email
git config --global core.editor "_caminhoDoExecutavel_" | Configura o git com um Editor padrão
code . | Abre o seu editor padrão
**git clone _https://..._** | Clona os arquivos do repositório para sua Maquina Local
git init | Cria um novo repositório na pasta aberta(arquivo .git)
git remote | Verifica se existe um repositório remoto
git remote add origin _https://..._ | Linka seu repositório local com o GitHub
git push -u origin master | Envia o repositório para o GitHub
git diff _nomeArquivo_ | Mostra as alterações feita no Arquivo (**antes de adicionar**) 
**git add _nomeAquivo_** | Adiciona as modificações a serem "Comitadas"
git reset HEAD | Remove um arquivo que ja foi adicionado(_caso não queira commita-lo ou caso queira altera-lo_)
**git commit -m "_seuComentario_"** | Adiciona um comentário para a modificação
git reset --hard _seuComentário_ | Volta para o Commit digitado e apaga os mais recentes
git commit -am "_seuComentário_" | Adiciona e comenta ao mesmo tempo
**git log** | Mostra todos os commits ja feitos, e seus codigos
git log --oneline | Mostra os commits mais resumidos
git log -- graph | Mostra o gráfico dos commits
git log --oneline --graph | Mostra o gráfico e os commits resumidos
**git push** | Envia os arquivos "commitados" para o GitHub
**git status** | Informações modificadas, adicionadas, "commitadas", branch atual, conflitos...
**git fetch** | Busca por atualizações feitas no repositório do gitHub
**git pull** | Atualiza seu repositório local com o que foi adicionado no gitHub
git branch | Mostra todos os branch
**git branch _newBranch_** | Cria uma nova Branch(ramificação)
**git branch -d _nomeBranch_** | Deleta uma branch
git branch -D _nomeBranch_ | Deleta FORÇADO uma branch
git push origin _newBranch_ | Envia para o gitHub a nova Branch
git push -u origin _newBranch_ | Envia para o gitHub a nova Branch
git switch _nomeBranch_ | Troca de Branch
**git checkout _nomeBranch_** | Troca de Branch
git checkout -b _newBranch_ | Cria uma nova Branch(ramificação) e ja entra nela
git checkout _numeroCommit_ | Volta o repositório para como estava no Commit digitado
git checkout master | Retorna ao estado atual do Projeto
**git merge _nomeBranch_** | Na Branch master, junta as Branch, na atual que estiver usando(master)
git tag _nomeTag_ | Definir versões estáveis do Projeto(Release no GitHub)
git tag | Mostra em qual versão está
git tag -a _nomeTag_ -m _seuCommit_ | Cria a tag e ja "Commita"
git tag -d _tagUsada_ | Deleta uma tag (**antes do push**)
git push origin _nomeTag_ | Envia ao gitHub a nova Tag
git rebase _branch_ | **não me lembro**
git rebase --continue | **não me lembro**
git cat _noneArquivo_ | Mostra o que está escrito no Arquivo
gitk | Abre a interface gráfica do Git


