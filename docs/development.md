# Kernel Porting Framework (KPF) — ambiente e testes

## Configuração local .env

Atualização de 2026-10-29, por escolha do usuário: a fonte ativa é `.env` na raiz
descoberta do checkout. Copie `.env.example` e configure valores próprios. O
arquivo real é ignorado; nunca contém a chave privada em si, apenas seu path.
Não existe fallback para lab.json nem leitura implícita do ambiente do processo.
Os trechos históricos abaixo que citam lab.json descrevem a fase anterior.

Os consumidores continuam usando `load_lab`/`development_root`. Precedência:
argumento CLI explícito > arquivo `.env` > default portátil já permitido pelo
consumidor. Runtime é KPF_K40S_RUNTIME_ROOT; endpoints e identidade são
KPF_K40S_NORMAL_SSH_HOST, NORMAL_SSH_USER, NORMAL_SSH_PORT, USB_SSH_HOST,
USB_SSH_USER, USB_SSH_PORT, SSH_IDENTITY_FILE e STRICT_HOST_KEY_CHECKING,
todos com prefixo KPF_K40S_. KNOWN_HOSTS_FILE, NOTE e AUTHORITY são opcionais.

Sintaxe literal: KEY=VALUE, comentários em linhas iniciadas por #, valores simples
ou entre aspas simples; aspas duplas usam escapes JSON. Não há `export`, execução
shell, interpolação, busca em HOME ou comentários no final do valor. Aspas simples
preservam barras Windows; elas são convertidas somente na fronteira apropriada.
Ports exigem inteiros e booleanos usam true/false. Duplicatas, sintaxe inválida,
campos desconhecidos da placa e symlink no arquivo são recusados sem fallback.
Não rode `source .env`: o loader lê dados, não comandos. O formato não torna paths
Windows utilizáveis por ferramentas Linux ou substitui requisitos do filesystem.

O `.env` fornece os endpoints reais, mas não redefine os limites da recuperação.
O perfil público contém `ssh_contract`, com usuários/portas e endpoint USB
esperados pelo workflow da placa. Para K40S os valores permanecem root/22 e
root/10.15.0.1/2222. O loader recusa divergências ou contrato ausente/inválido,
mantém host-key estrito para todas as placas e não abre sessões. Não mudar esse
contrato para contornar uma recusa de segurança.

Migração local: os valores foram copiados do JSON privado para `.env` e comparados
campo a campo sem exibi-los. JSON antigo foi preservado como backup privado,
inativo; o template público antigo foi removido (recuperável pelo Git). Provas
históricas e hashes não foram repinados. O modelo público novo usa placeholders.

## Migração de portabilidade — 2026-10-29

Seguir também as regras de paths/configuração local e privacidade do AGENTS.md.
Não transportar defaults de um laboratório para outra máquina. O primeiro
incremento migrou as raízes de testes para a configuração local descrita em
[referências WMT](#referências-wmt-separadas-do-desenvolvimento--2026-10-29).
Os caminhos anteriormente usados foram preservados somente em arquivo ignorado;
nenhuma fonte, pin ou evidência histórica foi reescrita.

Primeira validação direcionada: 20 testes de resolver, runner C e seletores passaram
sob guarda offline. Incluem precedência, configuração inválida sem fallback,
checkout sintético sem laboratório e cwd diferente. Isto não significa que todos
os scripts e perfis já estejam portáveis; exemplos históricos restantes abaixo
devem ser migrados junto com seus consumidores, sem alteração de recuperação.

### Runtime do workspace fora do perfil de hardware

`tools/kernel-workspace.py` não lê mais a raiz do runtime do perfil público da
placa. Configurar `development.runtime_root` no `boards/<placa>/local/lab.json`
ignorado, usando o exemplo público `boards/k40s/lab.example.json`, ou passar
`--runtime-root` com caminho absoluto válido no host em execução. O argumento
tem prioridade e não exige ler lab.json. O loader privado existente é reutilizado;
não há busca automática nem fallback para outro laboratório ou pasta antiga.

Exemplo sintético do campo de build, sem configuração SSH:

```json
{"development": {"runtime_root": "/srv/kpf-runtime"}}
```

Build/configure exigem esse campo ou argumento antes da preparação/execução.
Plan, components, prepare, check e patch-existing não precisam dessa raiz quando
não a utilizam. Isso não remove suas outras validações. Raiz relativa, traversal,
UNC ou caracteres de controle são recusados; paths de outro sistema devem ser
convertidos na fronteira apropriada antes de executar o build Linux.

As configurações SSH seguem verificadas separadamente por `load_lab`; um arquivo
com apenas `development` permite selecionar runtime, não conectar ao aparelho.
Na migração local, o runtime anterior e os demais campos privados foram conferidos
iguais. Cinquenta e dois testes de perfis, fontes, workspace e composição passaram
offline, incluindo roteamento configure/build, argumento prioritário, raiz
alternativa e recusa antes de preparar o build. Fontes/pins e montagem dos comandos
make não foram alterados. Não houve build real, conexão ou operação física.

### Runtime do compositor CONNSYS

`tools/build-k40s-connsys-staging.py` reutiliza a mesma seleção de runtime:
`--runtime-root` absoluto ou `development.runtime_root` no lab.json local. Somente
kernel e referência de memória são resolvidos sob `kernel-workspaces/` dessa
raiz; os demais inputs continuam relativos à localização do projeto. Import e
`--help` não carregam lab.json. `--output` relativo é ancorado na raiz do projeto,
não no cwd; continua exigindo diretório novo confinado a `artifacts/`.

Exemplo com localização de runtime explicitamente configurada:

```sh
python tools/build-k40s-connsys-staging.py --runtime-root /srv/kpf-runtime --output artifacts/connsys-portability-candidate
```

Esse comando compõe uma imagem experimental local, não faz flash nem autoriza
ensaio. Não foi executado na migração: só verificações de seleção/recusa foram
rodadas. Vinte e cinco testes direcionados passaram; a leitura dos seis inputs
reais confirmou os hashes originais. Nenhum pin, limite de sessão, autostart,
packer, formato de imagem ou caminho no telefone foi alterado. Os testes
históricos de imagens existentes usam agora `input_files()` para os dois inputs
externos; não houve regeneração de evidências ou das imagens preservadas.

### Builders de módulos HWRNG/TRNG

`build-k40s-hwrng.py` e `build-k40s-trng-probe.py` recebem `--runtime-root`
ou usam o mesmo `development.runtime_root` local. Resolução lazy: help/import
não carregam lab.json. Workspace kernel fica em `kernel-workspaces/<variante>`
e o trabalho de módulo em `module-workspaces/<artefato>` sob essa raiz; saídas
continuam em `artifacts/` do projeto descoberto pela localização do script.

Nomes, hashes, releases e política do registro fechado `k40s_kernel_variants.py`
continuam os mesmos. Naquele incremento, os dois builders deixaram de chamar seu
resolver legado; a retirada posterior desse helper está documentada em
[registro sem resolver de host](#registro-sem-resolver-de-host).

Verificação: 23 testes direcionados passaram sob guarda offline. Raiz alternativa,
cwd diferente, configuração inválida sem fallback, help sem laboratório e recusa
de kernel incorreto antes de diretórios/subprocessos foram exercitados. As sete
chamadas subprocess dos dois builders ficaram textualmente iguais às anteriores;
os três kernels reais selecionados mantêm seus hashes pinados. Nenhuma compilação,
alteração de fontes C, atualização de toolchain ou operação no aparelho ocorreu.

### Builder de experimentos de bateria

`tools/build-k40s-battery-snapshot.py` também usa `--runtime-root` ou o mesmo
`development.runtime_root` local para workspace kernel e trabalho do módulo.
Seleção de fontes e artefatos permanece relativa ao projeto. Help e recusas
de modos inválidos precedem a configuração local; `--native` continua aceito
somente com `--continuous`. Não foram adicionados modos, permissões físicas,
escritas no PMIC ou políticas de carga.

Dez testes direcionados passaram offline: seleção atomic/native, raiz alternativa,
configuração ausente/inválida, precedência explícita, outro cwd e kernel errado
recusado antes de diretórios/subprocessos. A reversão em memória apenas dos
trechos de migração reproduziu o script anterior byte a byte; comandos e lógica
dos experimentos não mudaram. Não houve compilação, alteração de fonte C,
regeneração de evidência ou acesso ao aparelho.

### Shell de build do kernel vendor

`tools/build-kernel.sh` descobre o projeto a partir de `BASH_SOURCE`, sem caminho
Windows antigo ou junction. Consulta `kernel-workspace.py runtime-root`, que
reutiliza o loader local existente; aceita `--runtime-root` absoluto como override.
`--help` não lê configuração nem inicia patch/build. A ação `runtime-root` só
resolve configuração: não verifica inputs de build, abre transporte ou cria saída.

O bloco posterior de patching, make, cópia e hash permaneceu byte a byte igual.
O runtime Linux configurado foi conferido igual ao anterior. O alias antigo do
projeto não existia na verificação, portanto não foi possível provar identidade
de filesystem daquele alias; a saída agora pertence ao checkout que contém o
script, como exige a diretriz. Não foi recriado alias nem renomeado workspace.

Verificação offline: 34 testes de perfis/workspace passaram; `bash -n`, help a
partir de outro diretório e recusa de runtime relativo também passaram. Nenhum
make, aplicação real de patch, cópia de zImage ou acesso ao aparelho ocorreu.
Os demais shells ainda precisam de migração; não assumir portabilidade deles
porque o shell principal passou a resolver sua própria localização.

### Shells de módulos Wi-Fi, Bluetooth e USB network

`build-wifi-modules.sh`, `build-bluetooth-modules.sh` e
`build-usbnet-modules.sh` passam a usar a mesma resolução do shell principal:
projeto por `BASH_SOURCE`, runtime por `kernel-workspace.py runtime-root` e
override opcional `--runtime-root` absoluto. Não dependem mais do nome antigo
do checkout ou de junction. Help não consulta lab; argumento inválido interrompe
antes de criação de diretório, cópia, compilação ou assinatura.

No Wi-Fi, `TASK_OUTPUT` continua disponível: se absoluto, é respeitado; se
relativo, é ancorado no projeto, não no terminal. Valor vazio conserva o default
`artifacts/wifi-modules`. Isso não acrescenta seleção automática de placa, fonte
ou chave. Layout de toolchain e chave de assinatura continua relativo ao runtime
explicitamente escolhido; não houve migração da identidade de assinatura.

As três verificações de sintaxe e os caminhos de help/recusa passaram fora do
cwd do projeto. Os blocos restantes de build, cópia, strip, assinatura e hash
foram comparados byte a byte com os anteriores, descontando somente a ancoragem
do output Wi-Fi. Não foram compilados/assinados módulos, criados artefatos ou
executados fluxos físicos. Outros shells exigem migração própria; a retirada do
resolver legado é registrada abaixo.

### Stock, bring-up e preparação do Python legado

`build-stock-kernel.sh`, `build-bringup-kernel.sh` e `build-legacy-python.sh`
usam agora o resolvedor de runtime local/argumento já descrito. O projeto é
descoberto pela localização do script; não há default de pasta pessoal nem
comando de exemplo com distribuição/usuário Windows fixos. O Python legado
continua sob `toolchains/legacy-python/` do runtime selecionado.

As verificações de sintaxe, help em outro cwd e recusa de runtime relativo ou
argumento desconhecido passaram nos três shells. A partir das definições derivadas
do runtime, os blocos de execução foram comparados byte a byte com os anteriores:
configuração, make, logs e hashes de kernel preservados; download, verificação
e instalação do Python legado também não foram alterados nem executados.
Essa migração não atesta segurança atual do Python legado ou de sua política
histórica de aquisição; somente remove a dependência de host desses paths.
Não houve download, instalação, build, geração de imagem ou operação física.

### Property shim do launcher Wi-Fi

`build-propshim.sh` usa a mesma resolução local de runtime e aceita
`--runtime-root` absoluto. Descobre o projeto pela localização do script.
`TASK_OUTPUT` absoluto continua respeitado; relativo fica ancorado no projeto,
e vazio mantém `artifacts/wifi-modules`, como no builder Wi-Fi.

Sintaxe, help fora do projeto e recusas de runtime relativo/argumento desconhecido
passaram. A seleção de runtime com espaços e três modalidades de output foi
conferida executando somente o prefixo de resolução, com localização do script
fornecida pelo harness. O corpo de compilação, símbolos e hash ficou idêntico.
Não houve compilação, instalação ou operação no aparelho. Initramfs/boot e os
resolvers Windows/WSL continuam exigindo migração e equivalência próprias.

### Prova de compilação das políticas I²C

`build-k40s-i2c5-policy-proof.py` usa `--runtime-root` ou
`development.runtime_root` local para workspace kernel e trabalho do módulo.
Mantém a variante atomic fechada, revisão vN, pins e verificação de prova existente.
Help e revisão inválida precedem a leitura de configuração. Não há fallback para
o resolver legado de variantes. Output continua relativo ao projeto.

Onze testes do grupo de portabilidade de módulos passaram sob guarda offline,
incluindo três casos novos de configuração/precedência, help/revisão inválida e
kernel incorreto recusado fora do cwd antes de saídas/processos. O kernel local
continua com o hash pinado. O corpo desde a criação do workspace até o relatório
foi comparado idêntico ao anterior; não houve build nem carregamento de módulo.

Pendência de boot identificada e tratada nos incrementos abaixo: fontes pessoais
dos manifests e seleção automática de backup por glob/ordem lexicográfica.
O `gen_init_cpio` vendor já suporta expansão `${VAR}` nas fontes; reutilizar esse
recurso evita criar um formatador paralelo. Evidências históricas não foram
reescritas.

### Initramfs básico: fontes relativas à configuração

`build-initramfs.sh` descobre o checkout e consulta o mesmo runtime local ou
`--runtime-root`. TASK_OUTPUT absoluto é respeitado; relativo é ancorado no
projeto. Help e argumentos inválidos são tratados antes da criação de diretórios.
Raízes com token literal `${` são recusadas para evitar expansão recursiva.

`initramfs/contents.list` usa `${KPF_BUSYBOX}` e `${KPF_PROJECT_ROOT}` apenas nos
campos de origem. O shell fornece essas duas variáveis exclusivamente ao comando
`gen_init_cpio`; não são entradas de configuração alternativas. Invocações diretas
do gerador precisam fornecer ambas. Paths do telefone, ordem, modos e uid/gid
continuam iguais; pin do pacote BusyBox, verificações QEMU, gzip e hashes também.

Validação manual offline: sintaxe/help fora do projeto, recusas de runtime relativo,
argumento desconhecido e token de expansão. Fixture temporária com conteúdo e
mtimes controlados produziu CPIO byte a byte igual entre manifest com fontes
absolutas e manifest com variáveis, usando o gerador vendor existente e raiz com
espaços. O corpo de execução foi comparado idêntico exceto pelas variáveis locais
da chamada do gerador. A equivalência é da fixture, não de uma imagem real antiga:
o alias antigo de projeto não deve ser presumido igual ao checkout atual.
Nenhuma imagem de produção/boot foi gerada, nem houve build, flash ou transporte.
O builder LTS foi migrado no incremento seguinte.

### Builder de boot LTS: backup explícito

`build-lts-test-boot.sh` exige `--backup ABSOLUTE_DIRECTORY` antes dos argumentos
posicionais existentes; não seleciona mais backups por busca ou ordenação. O
diretório deve conter `boot_a.bin` e `dtbo_a.bin`, sem traversal. Também aceita
`--runtime-root` nessa posição, ou consulta o runtime local existente. Ausência ou
erro de seleção não aciona fallback. A primeira ocorrência de argumento posicional
encerra o bloco dessas opções. Os cinco posicionais conservam sua ordem e modos.

```sh
bash tools/build-lts-test-boot.sh --backup /srv/private-backup --runtime-root /srv/kpf-runtime
```

O exemplo apenas documenta a CLI; não autoriza geração, flash ou ensaio.
Checkout é descoberto pelo script; workspace, saída, cmdline e manifest relativos
são ancorados no projeto. Fontes relativas dentro de manifest também pertencem
ao projeto: o gerador executa nesse diretório. O manifest padrão usa as mesmas
duas variáveis de origem do initramfs básico; o `/init` correspondente é resolvido
antes de QEMU. Inputs essenciais são conferidos antes de criar a saída. Recusa de
saída explícita existente e allowlist dos modos de overlay foram preservadas.

`advance-k40s-lts.py` exige `--backup` absoluto válido antes de criar logs ou rodar
etapas e o encaminha ao packager. A conversão Windows/WSL, antes limitada ao drive
C: e distro fixa, foi migrada no incremento seguinte. Não houve
seleção automática, alteração ou publicação de um backup real nesta migração.

Verificação: 28 testes direcionados passaram sob guarda offline. O teste de modos
incompatíveis recebeu backup sintético explícito para não passar apenas pela
ausência do novo argumento; novo teste cobre recusas de backup antes de writes e
etapas. Verificação manual do prefixo de seleção resolveu sete paths em raiz com
espaços fora do cwd; seis recusas do shell completo precederam saída. Fixture CPIO
sintética manteve igualdade byte a byte, ordem e metadados. Comandos de boot pack,
round-trip, overlay, remoção temporária e hashes ficaram textualmente idênticos.
Nenhum build, imagem de boot de produção, transporte ou ensaio físico ocorreu.
Essas fixtures não comprovam equivalência com uma imagem histórica real; isso
requer conferir os inputs do backup explicitamente escolhido antes de empacotar.

### Fronteira Windows/WSL do workflow advance

`advance-k40s-lts.py` exige `--wsl-distro` explícito, além de `--backup`.
Converte checkout e backup por `wslpath -a -u` na distro selecionada, em vez de
montar `/mnt/c` manualmente. Caminhos internos são relativos ao checkout já
convertido, com recusa de escape. Consulta `kernel-workspace.py runtime-root`
dentro dessa distro para selecionar o workspace fechado da variante; deixa de
usar o resolver legado com default pessoal. Configuração é a mesma do builder
Linux, sem sistema ou campo de runtime paralelo no host Windows.

As consultas precedem logs e etapas. Path inválido, conversão falha ou runtime
ausente/inválido interrompem sem fallback. WSL usa `--exec`, inclusive nas etapas
existentes: a checagem nativa encontrou que `--` passava pelo shell e consumia
barras invertidas. Execução direta preserva espaços e metacaracteres como dados.
O usuário root dos harnesses de namespace/chroot é requisito desses harnesses,
não um login pessoal de desenvolvimento.

Dez testes direcionados passaram sob guarda offline, com roots sintéticos em
drives distintos, distro com espaços, plano capturado sem execução e falha de
runtime antes de escrita/etapas. Testes de recusa de modos recebem a distro e o
backup sintéticos para continuarem cobrindo a restrição original. Consultas reais
somente de leitura no Windows confirmaram conversão do checkout, preservação de
espaços/metacaracteres e o mesmo workspace atomic configurado anteriormente.
Drives alternativos foram simulados, não validados em volume real. O corpo de
execução do workflow foi comparado igual, exceto `--exec` e backup pré-convertido;
não foram executados suíte do workflow, builds, geração de imagem ou transporte.
Ferramentas chamadas por ele ainda podem conter defaults legados e exigem
migração própria; isto não declara o workflow completo portável ou validado.

### Identidade pública do payload SSH

`prepare-k40s-ssh-payload.py --authorized-key ABSOLUTE_PUBLIC_KEY` exige seleção
explícita de chave pública Ed25519 ao criar payload novo. Não lê mais uma chave
em pasta pessoal fixa. Somente tipo e material público são copiados, com o mesmo
prefixo `restrict`; comentário não é incluído. Não passar chave privada. Paths
relativos, traversal, UNC e controles são recusados. Help não exige root.

Payload existente pode ser verificado sem selecionar outra chave, preservando
pins e identidade. Se `--authorized-key` for fornecido, deve ser válido e igual à
autorização existente; erro ou divergência interrompe, sem fallback ou regeneração.
Geração de chave host, configuração efetiva de SSH, bind USB, permissões e chroot
permanecem iguais. A validação de tipo/material mantém o comportamento anterior;
não é uma nova validação criptográfica do arquivo público.

No workflow Windows, usar `--ssh-public-key ABSOLUTE_PUBLIC_KEY` com `--stage ssh`.
Arquivo é validado pelo mesmo helper antes de logs/etapas, convertido por wslpath
na distro selecionada e encaminhado como `--authorized-key`. Sem payload existente,
ausência da chave interrompe antes das consultas WSL e etapas. Verificação de um
payload já existente não exige selecionar novamente a identidade.

Onze testes direcionados passaram sob guarda offline, incluindo cinco novos
casos de chave/recusa/payload existente e encaminhamento de argumentos capturado
sem execução. O corpo de geração/configuração foi comparado igual, exceto o valor
selecionado para authorized_keys. A verificação real do payload privado existente
também passou somente por leitura; não foram exibidas chaves, criadas identidades,
executados chroot, iniciados listeners ou acessado o aparelho. O gerador de rootfs
continua pendente: ainda acrescenta paths pessoais e herda manifest histórico.

### Gerador de perfis rootfs sem raízes pessoais

`prepare-k40s-rootfs-test.py` emite `${KPF_PROJECT_ROOT}` para fontes internas e
`${KPF_BUSYBOX}` para o BusyBox. São as mesmas variáveis fornecidas pelo packager
LTS; não há descoberta de host ou sistema novo de configuração. Output relativo
é ancorado no projeto, preservando a exigência de diretório novo sob `artifacts/`.

O manifest base histórico é somente lido, não editado. Na nova saída, o helper
`portable_base_manifest` remapeia exatamente as três entradas de arquivo
conhecidas: BusyBox, `/init` e emmc-readonly. Confere destinos e sufixos de origem
do layout revisado; rejeita entrada inesperada, duplicada, ausente ou traversal.
Não usa o prefixo pessoal antigo para localizar arquivos e não varre diretórios.
Demais entradas, ordem, modos e proprietários ficam intactos. Política, hashes de
módulos, one-shot, modos nativo/residente/carga e flags de metadados não mudaram.

Dezenove testes direcionados passaram sob guarda offline, incluindo geração em
raiz sintética com espaços/cwd diferente, recusa de output externo e preservação
da base, OpenRC gerado sem SSH e restrições de bateria. O teste de pacote passou
a chamar o mesmo main em processo, sem subprocesso Python desnecessário. Os três
manifests base reais foram aceitos e permaneceram byte a byte intactos. Fixture
CPIO da base produziu bytes iguais entre paths absolutos e variáveis em outra
raiz. Reversão em memória somente dos trechos migrados reproduziu integralmente
o script anterior: nenhuma guarda ou pin foi relaxado.

Não houve geração de boot de produção, build de kernel ou ensaio. Equivalência
de fixture não comprova igualdade com uma imagem histórica real, cujo alias de
checkout já não existe; conferir os inputs escolhidos antes de empacotar continua
obrigatório. Evidências antigas permanecem privadas e sem substituição global.

### Consumidores restantes do workspace de variantes

`audit-k40s-ccf-probe.py`, `audit-k40s-i2c5-irq.py`, `audit-k40s-i2c5.py` e
`stage-k40s-i2c5-irq-dt.py` deixam de chamar `workspace_for`. Consultam o loader
local existente, com `--runtime-root` explícito prioritário; a variante atomic
continua fechada. Output relativo é ancorado no projeto, sem dependência do cwd.
Help não consulta runtime. Recusas de output existente/confinamento, pins de
kernel/DTB, controller disabled e verificação de overlays não foram relaxados.

Treze testes direcionados passaram sob guarda offline: seleção local/argumento,
ausência/erro sem fallback, outro cwd/raiz com espaços, auditorias existentes e
invariantes de staging. Corpos após seleção de paths foram comparados byte a byte
iguais. Leitura do workspace local confirmou identidade com a seleção anterior
e os mesmos hashes pinados de kernel e DTB. Não foram gerados novos relatórios de
auditoria reais, staging DT, builds de kernel/módulo ou operações no aparelho;
os testes existentes de código C host continuam separados de aceite físico.

Após esse incremento, restavam a definição de `workspace_for` e um teste legado.
Sua retirada está descrita no incremento seguinte; nenhum pin/baseline foi
atualizado para esconder diferenças.

### Registro sem resolver de host

`k40s_kernel_variants.py` agora contém apenas o catálogo fechado e get_variant;
o helper sem consumidores operacionais e seu import Path foram retirados. Não
aceita hashes novos, não resolve laboratório nem lê configuração ao importar.
Builders/auditorias usam o loader local; Windows consulta esse loader dentro da
distro configurada, conforme os incrementos anteriores.

A prova histórica de arquivo inteiro continua usando o SHA original, sem repin.
Para não copiar o path pessoal removido para um teste público, a versão anterior
à retirada foi preservada como evidência privada ignorada. O teste acessa essa
evidência pelo resolver existente `support.source_path`, chave
`historical_variants`, arquivo `k40s_kernel_variants.py`. Primeiro compara cada
byte do registro atual com o prefixo preservado, descontando apenas o import
retirado; depois aplica as reversões revisadas anteriores à testemunha e confere
o mesmo hash histórico completo. Alterar catálogo ou testemunha faz a prova falhar.

Em outro ambiente, configurar a raiz da evidência autêntica no mapa local existente,
sem copiar paths/identificadores para arquivos públicos. Exemplo sintético de entrada
em `roots` de `local/test-sources.json`:

```json
"historical_variants": "/srv/private-evidence/variants-pre-portability"
```

Não gerar a testemunha a partir do arquivo já migrado nem alterar baseline para
compensar ausência de evidência. Sem a fonte privada, a prova histórica falha
explicitamente; testes puros do catálogo não dependem dela. O snapshot desta
migração fica em `local/baselines/variants-pre-portability/`, ignorado pelo Git;
os demais campos do mapa local foram preservados.

Vinte testes direcionados passaram sob guarda offline, incluindo a prova histórica,
catálogo, consumidores de runtime e geração de manifest. Ensaios em memória de
adulteração do registro público e da testemunha privada foram ambos rejeitados.
A fixture de importação das auditorias foi corrigida para não depender da ordem
da suíte. Nenhum kernel, imagem ou mecanismo de recuperação foi alterado ou
executado; evidência privada não foi publicada.

### Coletor da baseline I²C sem identidade ou host públicos

`probe-k40s-i2c5-baseline.py` obtém identidade e host normal pelo load_lab existente,
somente no caminho de coleta. Não embute chave privada ou IP de laboratório.
Mantém BatchMode, StrictHostKeyChecking e limites de tempo do comando original.
SSH vem do PATH (`ssh.exe` no Windows, `ssh` no Linux) ou de `--ssh-executable`;
override com diretório precisa ser absoluto e sem traversal/controles.

Output e evidência salva relativos são ancorados no projeto. O comando remoto
fixo, seu SHA, parser de stdout e tratamento de falha/sem retry ficaram iguais.
`--validate-saved` e help não carregam lab.json nem abrem transporte; validação
offline continua possível sem laboratório. Output novo continua confinado a work/.

Sete testes direcionados passaram sob guarda offline, incluindo argumentos com
identidade sintética/host reservado, erro de configuração sem fallback, validação
salva em outro cwd e recusas de executável. Montagem real de argumentos no Windows
confirmou igualdade com chave, host e comando anteriores deste ambiente, sem
imprimir seus valores nem executar SSH. Não houve coleta, nova telemetria ou acesso
ao aparelho. Configuração de coleta não é autorização para executá-la.

### Composição USB/eMMC e template USB

`initramfs-lts-usb/contents.list` usa `${KPF_BUSYBOX}` e `${KPF_PROJECT_ROOT}` nas
duas origens de arquivo. O compositor `compose-k40s-usb-emmc.py` usa a mesma raiz
para o hook emmc-readonly acrescentado; output relativo é ancorado no checkout.
O packager LTS já fornece ambas as variáveis. Invocações diretas de gen_init_cpio
precisam fornecê-las explicitamente. Não há seleção nova de kernel ou dispositivo.

Dezenove testes direcionados passaram sob guarda offline, incluindo validação real
do perfil gerado fora do cwd e recusa de output existente/externo. Comparação em
memória da versão anterior com a atual confirmou os mesmos perfis, cmdlines e
contrato do archive nos seis modos existentes (clocks/PWRAP/atomic permitidos).
Foi normalizada somente a quebra de linha da captura usada nessa comparação.
Fixture CPIO sintética com origens relocadas para raiz com espaços manteve bytes
iguais. Ordem, destinos, modos, proprietários, hooks opcionais e política forbidden
continuam iguais. Não houve build ou imagem real de boot; os perfis temporários
dos testes foram removidos ao terminar. Artefatos históricos não foram reescritos.

### Shells de compilação dos diagnósticos BROM

`build-brom-arm-once-module.sh` e `build-brom-readonly-module.sh` descobrem o
checkout por BASH_SOURCE e consultam o runtime local existente ou `--runtime-root`
absoluto. O segundo mantém revisão posicional vN e default v2; aceita o override
de runtime antes ou depois da revisão. Recusa revisão inválida, argumentos extras
e runtime duplicado. O primeiro continua restrito à revisão v1 fixa. Nenhum deles
ganhou instalação, reset ou operação de transporte.

Verificação manual offline: sintaxe/help em outro cwd, dez casos de recusa
(incluindo runtime inválido/duplicado e workspace existente) e seis execuções
somente do prefixo de seleção, com localização do script fornecida pelo harness,
runtime com espaços e ordens de argumentos equivalentes. Diretórios existentes
foram preservados. Os corpos de compilação/cópia/strip/assinatura/modinfo/hash
foram comparados idênticos aos anteriores após a seleção de paths/revisão.
Não houve make, assinatura, instalação, mudança de limites ou acesso ao aparelho.
Os caminhos de chave/certificado continuam relativos ao runtime explicitamente
escolhido; não houve descoberta nem troca de identidade de assinatura.

### Shells de ferramentas GPU/PVR

`build-gpu-egl-probe.sh`, `build-pvr-lifecycle-probe.sh` e
`build-pvr-version-query.sh` descobrem o projeto por BASH_SOURCE e usam o runtime
local existente ou `--runtime-root` absoluto. Toolchain e headers vendor mantêm
seus layouts relativos ao runtime; saídas continuam sob artifacts/ do checkout.
Não foram adicionados modos, drivers, instalação ou novas permissões físicas.

Validação manual offline: três sintaxes/help fora do cwd, nove recusas anteriores
ao build e três execuções somente dos prefixos de seleção em runtime sintético
com espaços, com localização de script fornecida pelo harness. Corpos posteriores
de compilação/file/hash/tar permaneceram byte a byte iguais. Não houve compilação,
geração de pacotes, execução de probe ou acesso ao aparelho. Essa migração de
paths não reativa a frente GPU/PVR, adiada na primeira entrega funcional.

### Scanner offline de referências LK

`inspect-lk-boot-paths.py` descobre o checkout pelo módulo e só lê imagem/executa
objdump dentro de main. Import e help não iniciam análise nem criam saída. O
executável vem de `--objdump` (PATH ou path absoluto local) ou do runtime local
existente/`--runtime-root`; seleções explícitas são mutuamente exclusivas, sem
fallback. Paths relativos com diretório, traversal, UNC, controles e opções no
lugar de executável são recusados. A imagem continua no path relativo revisado
e a saída sob artifacts/bootloader-analysis do checkout.

Quatro testes passaram sob guarda offline, com imagem/disassembly sintéticos,
outro checkout/cwd, espaços, seleção local/argumento e recusas antes de leitura,
processo ou saída. O corpo de scanner, limites e argumentos objdump, parser e
escrita de resultado foram comparados iguais após descontar a indentação em main
e a seleção do executável. Help também passou no Windows. Não foi executado
objdump real, analisado firmware real ou gerada evidência de engenharia reversa.
O ciclo de flash/recuperação continua pendente de migração específica, preservando
sua prova histórica e ordem operacional; não foi alterado neste incremento.

### Configuração SSH do caminho BROM/recuperação

`flash-boot-auto-brom.py` não contém mais identidade/host pessoais. Import e help
mantêm SSH_ARGS com identidade ausente e HOST ausente, sem ler lab.json.
`ensure_transport_configuration` resolve ambos pelo loader existente antes de
remote, prepare ou run_flash, inclusive antes de abrir o writer. Configuração
parcial é recusada sem fallback. O ciclo existente continua fornecendo ambos
pelos campos previamente validados, conservando argv e sua ordem. Imagem relativa
na CLI pertence ao checkout, não ao cwd. Ferramentas Windows, timeouts, pins,
geometria, comandos remotos, listener-before-arm, readback, reset único, cancelamento
e limpeza do processo escritor não mudaram.

Vinte e sete testes direcionados passaram sob guarda offline. Escrita/reset e
cancelamento são simulados; mensagens de confirmação nesses testes não são
evidência de flash real. Cobrem configuração ausente/parcial antes de subprocessos,
configuração lazy e integração existente do ciclo. Montagem de configuração no
Windows confirmou mesmos argv/host/pins históricos sem abrir transporte.

A versão anterior foi preservada em
`local/baselines/auto-brom-pre-portability/flash-boot-auto-brom.py`, ignorada pelo
Git, e configurada como raiz `historical_auto_brom` no mapa de fontes existente.
A prova de integridade reverte em memória somente os trechos exatos de seleção,
compara integralmente com essa testemunha e mantém o mesmo SHA histórico. Não
copiar dados pessoais da testemunha para testes públicos. Exemplo sintético de
raiz em `local/test-sources.json`: `"historical_auto_brom": "/srv/private-evidence/auto-brom-pre-portability"`.
Sem evidência autêntica a prova falha; não repinar nem reconstruir a partir do
arquivo migrado. Corrupções sintéticas de código público e testemunha privada
foram rejeitadas. Nenhum SSH, SCP, writer USB, flash, reboot ou operação física
foi executado; configurar o caminho não autoriza utilizá-lo.

### Seleção portátil de ADB no diagnóstico manual PVR

`diagnostico-pvr.ps1` aceita `-AdbExecutable` (nome no PATH ou path absoluto local
existente). Seleção explícita inválida é recusada antes de logs, consultas ou
transporte, sem fallback. Recusa vazio, controles, UNC, path relativo com diretório
e traversal. Sem argumento, procura PATH, cópia em tools/platform-tools e SDK no
LocalApplicationData obtido do sistema, nessa ordem. Foi retirado o fallback para
um perfil pessoal fixo; nenhum drive ou usuário específico é presumido.

Validação manual: parser PowerShell, duas seleções explícitas, sete recusas e
precedência padrão com ferramenta sintética/checkout alternativo com espaços.
Somente o prefixo de seleção foi executado, com raiz do script fornecida pelo
harness; os executáveis selecionados não foram invocados. O corpo desde a seleção
do probe até firmware/hash, confirmação, transporte, log e limpeza foi comparado
byte a byte igual. `-CheckOnly` ainda consulta o aparelho pelo contrato antigo;
não foi executado nesta migração e não é um modo de validação offline.
Nenhum ADB real, probe ou operação física ocorreu. Frente PVR permanece adiada.

### Destinos explícitos dos coletores de boot

`backup-linux-boot-readonly.py` e `collect-k40s-boot-evidence.py` exigem `--host`
e `--key` explícitos, sem IP de laboratório ou chave pessoal default. Não há busca
de identidades. Destino vazio, opções/whitespace/controles e chave relativa, UNC,
com traversal, ausente ou dentro do projeto são recusados antes do transporte.
Output relativo pertence ao checkout descoberto pelo módulo. Backup existente é
recusado antes da primeira consulta SSH, preservando FileExistsError e os dados.

Treze testes direcionados passaram sob guarda offline, cobrindo primeiras argv
capturadas, recusas anteriores à conexão, outro cwd, cópia curta/longa, identidade
de boot, parser e filtragem de snapshot. O teste anterior de backup existente
recebe host/chave sintéticos explícitos para manter cobertura da condição original.
Os corpos desde argv SSH até cópia, verificação, falha e relatório permaneceram
idênticos. Nenhum SSH, readback de partição ou coleta real foi executado. As CLIs
não leem lab.json: esses seletores são argumentos obrigatórios, sem fallback ou
novo sistema de configuração. Selecionar destino não autoriza operação física.

### Status de rede explícito e catálogo sem usuário fixo

`minecraft-status.py` exige host posicional explícito; mantém porta padrão 25565
e porta alternativa posicional. Import e help não abrem socket. Host vazio/com
controles ou whitespace e porta fora de 1..65535 são recusados. Timeout, handshake,
VarInt, limite de resposta e parser JSON foram preservados após a seleção.
Essa ferramenta auxiliar não é parte do aceite do kernel nem autorização de rede.

`catalog-tests.py` reconhece possíveis fixtures em `/home/` sem nome de usuário
específico; mantém classificação por AST, sem import ou transporte. Destino relativo
explícito é ancorado no checkout. Três testes offline passaram com rede simulada,
resposta sintética e fixture AST que falharia se fosse importada. Nenhuma consulta
real a servidor, aparelho ou criação de nova infraestrutura ocorreu. A auditoria
de portabilidade ainda inclui conversões dinâmicas Windows/WSL e consumidores
que resolvem paths explícitos pelo cwd; ausência de literal pessoal não prova
portabilidade completa.

### Workspaces externos independentes do cwd

`kernel-workspace.py` exige `--workspace` absoluto local sem traversal/controles
nas ações que utilizam workspace, e `--source` absoluto equivalente em
patch-existing. Não resolve mais esses argumentos externos a partir do terminal.
A recusa existente de workspace em /mnt/ continua ativa; não foram alteradas
políticas de perfil, patches pinados, argumentos make ou ordem de aplicação.
Plan/components/runtime-root mantêm seus caminhos lazy e contratos anteriores.

`audit-dtb-schema.py` exige fonte kernel externa absoluta, sem traversal/UNC;
DTB e output relativos são ancorados no checkout. Preserva a exigência de saída
nova fora da árvore kernel, ferramentas pelo PATH/argumentos, limites de execução
e a regra de que warning/erro não pode resultar em clean ou autorização de boot.

Quarenta e dois testes direcionados passaram sob guarda offline: matriz de ações
recusa paths externos inválidos antes de preparar/patch/verificar; auditoria DT
funciona fora do cwd com raiz contendo espaços e recusa output existente antes
de ferramenta. As ferramentas de schema foram simuladas; não houve validação real
de DT ou build. Testes anteriores aplicaram somente patch em fixture temporária,
não no kernel de desenvolvimento. Nenhum transporte ou operação física ocorreu.

### Validação de chave externa sem presumir mount Windows/WSL

`load_lab` não concatena mais `/mnt/<drive>` para verificar se uma identidade SSH
Windows vista do Linux fica dentro do checkout. Quando o path é estrangeiro ao
host, consulta `wslpath -a -u` sem shell, com limite de dez segundos. Resultado
deve ser uma única raiz absoluta local válida, sem traversal/controles/UNC e sem
stderr. Falha, ausência ou timeout interrompem com erro, sem mount presumido ou
fallback. O path resolvido, incluindo symlinks, mantém a recusa de chave no projeto.

A conversão aqui é para containment: o campo original da configuração continua
preservado, pois consumidores Windows usam ferramentas Windows; não converter
globalmente o argv de transporte. Consumidores nativos Linux devem receber paths
nativos no ponto apropriado de uso. Paths nativos não exigem esse subprocesso.
Runtime, perfis, endpoints e política de host key não foram alterados.

Trinta e um testes direcionados passaram sob guarda offline, incluindo mount
sintético alternativo, rejeição de conversão interna/symlink, respostas inválidas,
warning, erro e timeout, além dos consumidores existentes com transportes simulados.
Uma consulta real somente de leitura no WSL confirmou a checagem da configuração
local pelo mapeamento do sistema, sem exibir identidade/host ou abrir conexão.
Nenhum SSH, SCP, writer USB, flash ou reboot real foi executado.

### Paths relativos no runner verificado e coleta/restauração

`run-k40s-verified-test.py --image` relativo é ancorado no checkout e continua
confinado a artifacts/. `collect-and-restore-lts-test.py --output` relativo também
pertence ao checkout, mantendo diretório novo privado em work/. Não mudam pins,
endereços, geometria, allowlists de transporte ou sequência de captura/restauração.
Argumentos absolutos conservam seus destinos. O main de recuperação aceita argv
para a mesma CLI ser verificada em processo, sem novos modos de transporte.

Doze testes direcionados passaram sob guarda offline: outro cwd/raiz com espaços,
recusas de escape/existência antes de payload/transporte e harnesses existentes de
captura, restauração, falha e seleção atomic/native. Mensagens de restauração nos
testes provêm de mocks, não são evidência física. Reversão em memória apenas de
paths/assinatura CLI reproduziu os dois scripts anteriores integralmente.
O `--validate-only` real também passou partindo de `/`, conferindo somente payload
pinado e limites e sem criar a saída relativa solicitada. Nenhum DA, capture real,
flash, reboot ou transporte foi iniciado. Uso operacional exige autorização própria.

### Templates nativos CCF/I²C

Os manifests de `initramfs-lts-native-ccf`, `initramfs-lts-native-i2c`,
`initramfs-lts-native-i2c-identity`, `initramfs-lts-native-i2c-observe-v2` e
`initramfs-lts-native-i2c-pins-v3` usam as variáveis existentes KPF_BUSYBOX e
KPF_PROJECT_ROOT somente nas origens. No perfil identity, i2ctransfer continua
vindo de sources/i2c-tools-4.4/tools, sob o checkout selecionado. O packager LTS
fornece essas variáveis; uso direto do gen_init_cpio exige fornecê-las. Inits,
fontes de driver, hooks, permissões físicas e artefatos históricos não mudaram.

Quarenta e quatro testes direcionados passaram sob guarda offline, incluindo
invariantes USB/nativo e recuperação simulada. Comparação com os cinco manifests
anteriores confirmou ordem, destinos, modos, proprietários e demais entradas
idênticos. Cinco fixtures CPIO sintéticas produziram bytes iguais entre origens
absolutas e variáveis em outra raiz com espaços. Não foi gerado boot real nem
comprovada equivalência de imagem histórica; nenhum I²C, flash, reset ou transporte
real ocorreu. Templates adicionais ainda identificados na auditoria (early,
stability, PWRAP, eMMC e PMIC) exigem revisão própria, não substituição global.

### Templates early, stability, PWRAP, eMMC e PMIC

`initramfs-lts-native-early`, `initramfs-lts-stability`, `initramfs-lts-pwrap-diag`,
`initramfs-lts-emmc`, `initramfs-lts-pmic-id` e `initramfs-lts-pmic-reg` usam as
mesmas variáveis KPF_BUSYBOX/KPF_PROJECT_ROOT do packager nas fontes revisadas.
O executável stability continua em artifacts/lts-stability/build-v1; não houve
novo build ou seleção de variante. Fornecer variáveis ao invocar gen_init_cpio
diretamente. Destinos, ordem, modos e uid/gid foram comparados iguais aos anteriores.

Quarenta e três testes direcionados passaram sob guarda offline, incluindo
restrições de stability, eMMC e PMIC. Seis fixtures CPIO com payloads sintéticos
e mtimes controlados produziram bytes iguais após relocação para raiz com espaços.
Nenhum init, limite de watchdog, driver ou artefato histórico foi alterado. Não
houve geração de boot real, eMMC/PMIC físico ou transporte. A busca nos templates
fora de artifacts/work/sources/local não encontrou os padrões de pastas pessoais
consultados; isso não prova ausência de todos os problemas de portabilidade ou
equivalência com imagens históricas reais. Outras CLIs seguem em auditoria.

### Prefixos da CLI de retorno watchdog

`test-k40s-wdt-return.py` resolve prefixos relativos dos três modos capture-brom,
capture-da-state e receive-checkpoint sob o checkout. Paths absolutos permanecem
iguais. A CLI aceita argv em processo, mas não ganhou novos modos ou permissões.
O parser DA existente continua verificando backup pinado, outputs/parent e
combinações antes do transporte; opções de captura não se misturam com reset.

Vinte e quatro testes direcionados passaram sob guarda offline. Seleção dos
três modos com paths relativos/absolutos foi capturada em raiz com espaços e cwd
diferente; validate-only não carregou transporte. Recusas de combinações precedem
carregar backends, e a suíte DA simulada preservou falhas/readback/sem retry.
Reversão em memória somente de paths/assinatura CLI reproduziu integralmente o
script anterior. Mensagens de escrita/reset nos testes são dos mocks. Nenhuma
DLL sintética foi carregada, nem ocorreu captura/DA/flash/reset real.

### Entrada direta da sessão DA

`k40s-da-session.py` resolve --restore, --image e --out-prefix relativos pelo
checkout antes das verificações existentes. Paths absolutos são preservados;
prefixo explicitamente vazio é recusado, sem selecionar o checkout como default.
Mantém validação de backup/imagem por tamanho/magic/hash, outputs existentes,
parent de captura, comandos/modos, geometria GPT e limites de DRAM.

Vinte e seis testes direcionados passaram sob guarda offline: resolução em outro
cwd com raiz contendo espaços, imagem/backup capturados antes das verificações,
prefixo vazio/existente recusado antes de leitura e sessão DA simulada com falhas.
Reversão exata somente do bloco de paths reproduziu integralmente o arquivo
anterior. Mensagens de escrita/reset são de mocks; nenhum DA, USB, flash, reboot
ou captura real ocorreu. Pins e fallback de recuperação continuam inalterados.

### Runtime Linux: recusa conservadora de mounts de host

`development_root` aplica também aos consumidores shell/build a recusa de runtime
sob `/mnt` em host POSIX. Resolve symlinks para essa checagem, sem mudar o path
retornado nem criar diretórios. Configuração local inválida e override explícito
em /mnt falham sem fallback; override Linux válido continua prioritário. Isso
estende a restrição conservadora já usada para workspace pelo kernel-workspace.
Não é detecção universal de filesystem: um mount diferente exige configuração
correta do operador; não houve varredura de mounts ou migração automática de dados.

Cinquenta e dois testes direcionados passaram sob guarda offline, incluindo
runtime local/argumento, symlink para /mnt e consumidores de módulos/workspace.
O runtime local real permaneceu aceito; um shell real recusou runtime sintético
em /mnt antes de build. Nenhum build, assinatura, deslocamento de workspace ou
operação física ocorreu. Testes existentes aplicaram patch só em fixture temporária.

A execução conjunta encontrou ainda uma prova histórica DA que precisava
incorporar a seleção de paths do incremento anterior. O teste agora reverte apenas
o bloco exato daquela migração antes de conferir o mesmo SHA original. Não houve
repin, supressão de falha ou alteração de políticas de recuperação. Após a redução
equivalente da checagem de /mnt, os dois testes diretamente afetados passaram.

### Packer de boot lazy e independente do cwd

`build-boot-image.py` mantém a CLI existente dentro de main(argv): import/help não
leem imagens nem geram saída. Entradas stock/kernel/ramdisk/cmdline/DTB e output
relativos pertencem ao checkout. Recusa output existente ou symlink, inclusive
quebrado, antes de ler inputs; não usar arquivo histórico como destino.
Header v2, layout, alinhamento, DT table, legacy digest, cmdline e padding permanecem
iguais. O packer não faz flash nem autoriza boot.

Três testes dirigidos passaram sob guarda offline, cobrindo import/help lazy,
output existente/link quebrado, cwd alternativo, DTB substituído e teste anterior
de DTB/cmdline. O caso de cmdline inválida usa saída nova para não ser mascarado
pela nova recusa de sobrescrita. O teste anterior chama o mesmo main em processo,
sem subprocesso Python desnecessário. Comparação em memória executou a versão
anterior e a atual com as mesmas fixtures sintéticas: saídas com DTB original e
substituído ficaram byte a byte iguais. Arquivos temporários foram removidos ao
encerrar; nenhuma imagem de produção/histórica foi regenerada ou sobrescrita,
e não houve transporte ou operação física.

### Paths dos analisadores SMP/stability/PWRAP

`analyze-smp-log.py`, `analyze-stability-log.py`, `analyze-k40s-smp-logs.py` e
`analyze-k40s-pwrap-diag.py` ancoram entradas e outputs relativos no checkout.
Os dois legados aceitam argv em processo mantendo as mesmas opções. Outputs
conservam o symlink visível ao escritor/recusa: não resolver o destino final antes
de verificar existência/link, inclusive quebrado. Nos dois legados a recusa de
link precede inputs; nos genéricos o write_evidence existente mantém a proteção.

Trinta e quatro testes dirigidos passaram sob guarda offline. Logs incompletos
sintéticos mantêm boot_authorized falso e os retornos 0/2 anteriores dos genéricos;
fixtures em outro cwd confirmam paths e recusas de report existente/link quebrado.
Parsers SMP/PWRAP/captures anteriores também passaram. Reversão em memória somente
dos paths, assinatura CLI e recusa de link reproduziu os quatro arquivos anteriores
integralmente. Nenhum critério de diagnóstico/aceite foi relaxado, log privado
exportado, coleta nova ou transporte executado. Saídas temporárias dos testes
foram descartadas com as fixtures.

### Coletores estáticos watchdog/clocks/USB/segurança

`collect-k40s-watchdog-evidence.py`, `collect-k40s-clock-evidence.py`,
`collect-k40s-usb-evidence.py`, `collect-k40s-usb-power-evidence.py` e
`collect-k40s-security-evidence.py` resolvem backup relativo sob o checkout e
ancoram output nessa mesma raiz, sem esconder symlinks do destino. Report
existente ou link quebrado é recusado antes da coleta. Main aceita argv da mesma
CLI; nenhuma nova seleção de backup, descoberta ou fonte foi acrescentada.

Vinte e cinco testes direcionados passaram sob guarda offline: paths em raiz com
espaços/outro cwd, report existente/link preservados e contratos/parsers anteriores
de clocks, USB e DT. Coleta dos novos testes foi simulada e mantém phone_access e
boot_authorized falsos; não foi lido backup privado nem gerado relatório real.
Reversão exata somente das definições de raiz, paths/assinatura CLI e recusa de
link reproduziu integralmente os cinco scripts. Hashes pinados de backup, filtros,
contratos e formatos de report não mudaram. Nenhum transporte/aparelho ocorreu.

### Coletores estáticos PMIC/pinctrl

`collect-k40s-pmic-evidence.py` e `collect-k40s-pinctrl-evidence.py` ancoram
backup/output relativos no checkout, mantendo symlink do destino visível para a
recusa antes de coleta. O pinctrl exige `--kernel` absoluto local sem traversal,
UNC ou controles; não escolhe fonte externa a partir do cwd. As mesmas CLIs
aceitam argv em processo, sem novas fontes, operações ou modos de hardware.

Dezenove testes direcionados passaram sob guarda offline: seleção de backup e
fonte pinctrl capturada em outra raiz/cwd, recusas prévias à coleta, preservação de
report e contratos PMIC/pinctrl anteriores. Corpos posteriores à seleção de paths,
incluindo comparação de tabelas/hashes e relatórios, foram comparados iguais.
Nenhum backup privado foi coletado, relatório real emitido ou aparelho acessado.
Isso fecha este grupo de coletores estáticos, não a auditoria de todas as CLIs.

### Comparação DT e Kconfig independentes do terminal

`compare-dtb.py`, `compare-reference-dt.py` e `check-kconfig.py` ancoram inputs e
outputs explícitos relativos no checkout. Comparação em lote mantém os defaults
históricos do perfil e sua validação de confinamento; a seleção explícita não
busca outro diretório. Destino final conserva symlinks visíveis para a recusa,
inclusive quebrados. Comparadores DT recusam output existente antes de ler inputs;
Kconfig mantém write_evidence create-only e omissão de valores privados.

Dezoito testes direcionados passaram sob guarda offline. Comparações DT reais com
DTC/libfdt em fixtures sintéticas e Kconfig em outro cwd/raiz com espaços mantêm
canonical_equal, ordem dos fragments, mismatch e ausência de boot_authorized.
Recusas de output/link impedem criação do destino; comparação canônica continua
sem provar binding/hardware. Corpos de comparação, evidência e critérios foram
comparados iguais após a seleção/recusa. Nenhum DT real, valor privado, build ou
aparelho foi usado; apenas arquivos sintéticos temporários dos testes.

### Backup LAF com import lazy e destino explícito do checkout

`backup-laf-readonly.py` mantém a CLI dentro de main(argv); import/help não
carregam lglaf, não criam saída nem abrem serial. Output relativo pertence ao
checkout e diretório existente/link (inclusive quebrado) é recusado antes de
importar transporte. Porta continua argumento explícito, sem descoberta ou
fallback. Autenticação LAF permanece distinta do backend MediaTek/DA.

Dois testes dirigidos passaram sob guarda offline com módulo LAF simulado.
GPT sintética com CRC válido, em raiz com espaços/outro cwd, confirmou sequência
HELO/autenticação/OPEN/duas READs/fechamento e modo GPT-only sem payload de partição.
Import/help e outputs existentes/link foram verificados sem transporte disponível.
O corpo inteiro desde criação da saída até finally-close foi comparado igual após
descontar a indentação em main: CRCs, limites, allowlist, hashes e fechamento não
mudaram. Nenhuma serial, USB, autenticação ou leitura de firmware real ocorreu;
arquivos sintéticos temporários dos testes foram descartados.

### Gerador offline de GPT lazy e create-only

`make-linux-gpt.py` mantém os dois posicionais em main(argv), sem ler/escrever ao
importar. Entrada/output relativos pertencem ao checkout. Output precisa ser novo
e não pode ser symlink, inclusive quebrado; recusa precede leitura. Não grava discos,
somente os dois arquivos GPT no destino explicitamente escolhido. Layout, contiguidade,
entradas preservadas, UUID de tipo Linux e geração UUID4 operacional continuam iguais.

Três testes dirigidos passaram sob guarda offline com GPT inteiramente sintética:
import/help, outra raiz/cwd com espaços, recusas de output/link, CRC da tabela e dos
dois headers, entradas não mescladas intactas e falhas de CRC/contiguidade sem saída.
Executar versão anterior e atual na mesma fixture com UUID fixo somente no harness
produziu GPT primária e backup idênticos byte a byte. O gerador real não fixa UUID.
Nenhuma GPT histórica/real foi regenerada, sobrescrita ou gravada no aparelho.
O gerador de logo continua pendente: além da CLI no import, usa uma fonte externa
de localização Linux fixa; sua migração exige seleção explícita/portável da fonte
e equivalência das imagens, sem reativar acabamento visual como prioridade funcional.

### Gerador de logo e fonte externa explícita

`make-boot-logo.py` mantém os posicionais stock/output em main(argv) e exige
`--font` com arquivo absoluto local existente, sem traversal/UNC/controles. Não
usa mais localização Linux fixa para fonte. Seleção inválida não procura outra
fonte. Manter a mesma DejaVu Sans Mono é necessário para equivalência visual;
escolher outro arquivo pode mudar pixels e requer revisão própria.

Import/help não carregam Pillow, fonte ou firmware. Pillow é importado somente
quando necessário aos helpers/renderização. Output relativo pertence ao checkout
e deve ser novo, sem symlink; recusa antecede inputs. Font loading é verificado
antes de criar saída. Draw/recolor, mensagens, posições de composição, header,
tail preservado e reparse das 36 imagens não foram modificados.

Dois testes de CLI passaram sob guarda offline no ambiente oficial (sem Pillow),
cobrindo help/import lazy, argumentos/fontes inválidos, outro cwd e output/link.
O Python de sistema WSL já tinha Pillow e a fonte anterior; foi usado somente
para comparação manual da versão anterior e atual em partição sintética de 36
imagens. Logo binário, todos os previews e folha de contato ficaram byte a byte
iguais com a mesma fonte explícita. Nenhuma dependência instalada, logo real
regenerado ou imagem visual fornecida ao aparelho. Arte/avisos permanecem iguais;
acabamento visual não foi promovido a prioridade da entrega funcional.

### Registros, ramoops e modelo zImage

`analyze-register-snapshot.py` e `decode-ramoops-console.py` ancoram inputs/outputs
no checkout. Preservam os escritores create-only sem esconder symlinks; decoder
recusa destino existente/link antes de inputs. Contratos de registros, assinatura,
layout/ecc ramoops e omissão de autorização física continuam iguais.

`audit-k40s-zimage-layout.py` exige workspace absoluto local sem traversal/UNC/
controles; summary e log LK relativos são ancorados no checkout. `nm` usa PATH ou
override explícito (nome PATH ou path absoluto válido), não localização /usr/bin
fixa. Output novo/link recusado antes da auditoria. Modelo permanece NOT-BOOT-READY
e retorna 2 mesmo em cenário aritmético válido; não escolhe novos endereços.

Grupos de 19 e 23 testes dirigidos passaram sob guarda offline: paths sintéticos
em outro cwd, registros/console incompletos, parsers e modelo de layout anteriores.
Após validar também overrides nm inválidos, o teste diretamente afetado passou.
Consulta somente de resolução confirmou que nm pelo PATH neste runtime aponta
para o mesmo executável anterior, sem executá-lo. Corpos de parsing/decodificação/
modelo/report foram comparados iguais após seleção e recusas. Nenhum dump privado,
DT/kernel real, MMIO ou aparelho foi lido; outputs dos testes são temporários.

### Paths locais de checkpoint e auditoria DA

`build-k40s-da-checkpoint.py` ancora payload/output relativos no checkout;
`audit-k40s-da-patches.py` ancora output. Ambos aceitam argv da mesma CLI e recusam
output existente/link, inclusive quebrado, antes de ler inputs privados. Não
descobrem outro payload/container nem alteram pins, registration, limites ou
políticas NOT-FOR-FLASH/target_execution falso.

Cinco testes direcionados passaram sob guarda offline: outro cwd/raiz com espaços,
seleção de inputs capturada, outputs/link e help sem leitura privada, mais auditoria
AST existente. Nos novos casos, leitura e build foram simulados: manifest sintético
não é prova de build/replay real. Corpos posteriores à seleção foram comparados
iguais: patch offsets, hashes, verificação e relatórios não mudaram. Nenhum firmware
privado, replay Unicorn, upload ou aparelho foi usado. CLIs de emulação DA/BROM
continuam pendentes de paths/saída; não foram executadas nesta migração.

### CLIs de emulação DA/BROM sem dependência do cwd

`emulate-k40s-brom-policy.py`, `emulate-k40s-da-checkpoint.py`,
`emulate-k40s-da-framing.py`, `emulate-k40s-da-reset.py` e
`emulate-k40s-da-shutdown.py` ancoram output relativo no checkout e recusam report
existente/link antes de leitura/replay. Reset/shutdown também ancoram estágios
explícitos relativos; fontes pinadas default permanecem iguais. Main aceita argv
da mesma CLI. Imports Unicorn foram movidos para replay, sem mudar instruções:
import/help/recusas não exigem emulador instalado, mas replay continua exigindo-o.

Cinco testes dirigidos de paths/builders locais passaram sob guarda offline,
incluindo CLIs sem Unicorn, reports existentes/links e estágio capturado em outra
raiz/cwd. Leituras/build/replay são simulados ou interrompidos antes dos inputs;
não representam emulação real. Comparação exata após reverter seleção CLI/paths e
reposicionar imports confirmou os demais bytes dos cinco arquivos iguais: pins,
limites, hooks, matrizes e verificações de resultado preservados. Help nativo Windows
também passou sem Unicorn. Nenhuma dependência instalada, firmware real lido,
replay/upload/USB ou aparelho executado. Evidências antigas de replay não mudaram.

### Validadores DT inicial e política de userspace

`validate-k40s-early-dtb.py` ancora DTB/evidência/output relativos no checkout e
recusa report existente/link antes de ler inputs. Mantém a exigência de evidência
Android verificada, concordância das variantes de memória, checks estruturais e
boot forbidden. `k40s_userspace_policy.py` ancora policy/snapshot/output relativos,
mantém DEFAULT/PID1_POLICY por localização do módulo e recusa output/link antes
dos inputs. Não aprova serviços nem modifica allowlists; mesmas CLIs aceitam argv.

Na execução dirigida, 27 testes passaram e um caso privilegiado namespace/QEMU
ficou pulado pelos pré-requisitos existentes (root e qemu-arm-static). Novas
fixtures exercitam outro cwd/raiz com espaços, seleção de evidência/snapshot e
outputs preservados; regras reais anteriores de DT/policy/PID1 também foram
verificadas nos testes aplicáveis. Corpos de validação e report foram comparados
iguais após seleção/recusa. Nenhuma evidência privada exportada, imagem de boot
gerada, serviço autorizado ou processo iniciado no aparelho. Skip não é evidência
de teste privilegiado aprovado.

### Arquivos locais da sessão residente

Em `tools/k40s-resident.py`, LOCAL relativo de push/pull parte da raiz do projeto,
não do cwd. Pull recusa destinos existentes e links, inclusive pendentes, e valida
a configuração SSH antes de criar o arquivo. Reutiliza o loader/pin existente;
não acrescenta transporte nem abstração. A restrição de upload a `/tmp` e `/run`
e os comandos remotos continuam iguais. Cinco testes do helper verificaram argv,
cwd externo e recusas com transporte simulado; não comprovam sessão no aparelho.

### Paths dos inspetores offline de DT

`inspect-dt-table.py`, `inspect-boot-snapshot.py` e `inspect-android-backup-dt.py`
resolvem entradas/saídas relativas pela raiz descoberta do projeto. Não fazem
descoberta de backups, seleção automática de PCB ou coleta no aparelho. Saídas
existentes e links pendentes são recusados antes da leitura; a publicação JSON
dos dois primeiros continua pelo writer atômico create-only existente.

Validação dirigida: 12 testes de tabela/snapshot com FDTs sintéticos e sete de
backup; incluem execução em cwd externo, equivalência byte a byte dos relatórios
relativos/absolutos e recusa anterior à leitura. Hashes, filtros de privacidade,
limites dos parsers e corpo da extração de backup foram preservados. Não houve
extração de backup real, geração de imagem ou transporte.

### Paths dos contratos DT e decodificadores de sessão

`check-dt-contract.py`, `decode-session-logs.py`, `decode-k40s-session-logs.py`
e `k40s-pstore-layout.py` usam a raiz do projeto para argumentos relativos de
captura/saída. Saídas existentes e links pendentes são recusados antes de consumir
capturas. Não há mudança de assinatura ramoops, ECC, limites, janelas permitidas,
contratos de hardware ou autorização de boot. Os cores/loaders existentes são
reutilizados; nenhum coletor ou sistema de configuração foi acrescentado.

Passaram 18 testes dirigidos de contratos/sessões e seis do decoder de console.
Fixtures em raiz alternativa/cwd externo produziram os mesmos bytes de relatório
e texto que argumentos absolutos. O caso legado mantém sua opção de logbuf e seu
schema, também verificado pelo teste existente. Não foram usadas capturas reais,
transportes ou builds de kernel. Paths internos Linux como `/chosen` não são paths
do host e permanecem no contrato.

### Paths do gerador de stubs LK

Os três argumentos de `gen-k40s-lk-overlay-targets.py` são resolvidos pela raiz do
projeto quando relativos. Use um destino dtsi novo: arquivo existente ou symlink
é recusado antes da leitura e a escrita usa modo exclusivo. A antiga sobrescrita
não é mais permitida. Parsers, hashes de origem, argumentos/ordem de extração e
lógica de geração foram preservados, sem busca automática de backup.

Nove testes dirigidos de gerador/parser passaram. A execução em cwd externo foi
verificada em raiz temporária; saída antes/depois é byte-idêntica com extração
simulada. Comparação exata do restante do código confirmou corpo inalterado.
Esses testes não executam fdtget nem validam DT de um aparelho: nenhuma imagem,
backup real, DT de produção ou autorização física foi alterada.

### Ferramentas externas da auditoria DT-schema

`audit-dtb-schema.py` aceita `--mk-schema`/`--validate` como nome de comando no
PATH ou arquivo absoluto local. Paths relativos com diretório, traversal, UNC,
controles e arquivo absoluto ausente são recusados antes de criar saída. Um nome
PATH mantém a resolução normal do subprocesso; não há busca em laboratórios nem
fallback de uma seleção inválida. O arquivo deve ser executável no ambiente de uso.

O destino relativo continua ancorado no checkout, preservando o symlink final
para recusar inclusive links pendentes antes de ler o DTB. A checagem de destino
fora dos fontes ainda resolve ancestrais, recusando links para dentro do kernel.
Dez testes dirigidos passaram com ferramentas simuladas; argumentos e ordem da
pipeline permanecem, e warning não vira aprovação. Não foi executada uma nova
auditoria de schemas reais nem alterado qualquer resultado histórico.

### Entradas locais de OCV e OpenRC

`prepare-k40s-ocv-profile.py` resolve base, identidade e saída relativas pela raiz
do projeto; o backup histórico pinado não foi movido ou descoberto por busca.
Saída existente ou link pendente é recusado antes de consultar inputs privados.
`probe-k40s-openrc-ram.py` faz o mesmo para `--source`, preservando o default
interno, os hashes e os comandos do chroot. Nenhuma nova configuração foi criada.

Cinco testes dirigidos passaram: caminhos relativos/absolutos em cwd externo,
default OpenRC, saída pendente e recusas/unidades existentes da conversão OCV.
Prepare/stage foram simulados; não houve chroot, geração de perfil de bateria ou
leitura de calibração real. A alteração não habilita SOC nem controle de carga.

### Imagem dos runners de estabilidade e ciclo

`run-k40s-lts-stability.py` e `lts-auto-cycle.py` resolvem `--image` pela raiz do
projeto antes de encaminhar a seleção à validação. Argumentos absolutos continuam
selecionando o mesmo arquivo. Não mudam hashes exigidos, allowlists, permissões,
ordem de transporte, limites de tentativas ou mecanismos de recuperação.

Passaram 34 testes dirigidos dos caminhos de recuperação, core congelado e ciclo.
As novas fixtures verificam cwd externo, equivalência da seleção relativa/absoluta
e falha de validação antes de executar. A prova do baseline mantém seu hash e
reverte somente a nova linha de resolução, além das mudanças antes revisadas.
Subprocessos/transportes dos runners foram simulados: não houve ensaio, flash,
lock real ou nova validação de imagem do aparelho.

### Seleção local do teste USB Windows

`test-mtk-usbdk-reboot.ps1` exige `-Port COM<N>` explícito, sem porta fixa ou busca
automática. `-PythonExecutable` e `-LibusbDll` aceitam arquivos absolutos locais;
quando omitidos, preservam o runtime dedicado e a DLL sob `work/` do checkout.
Seleção explícita vazia/inválida não usa fallback. A validação acontece antes de
alterar ambiente/iniciar processos. Raiz e porta são passadas como argumentos
Python, não interpoladas no código, permitindo apóstrofos no checkout.

Não executar esse script apenas para verificar configuração: seu corpo solicita
reset físico e exige autorização própria. A validação deste incremento usou
somente AST/prefixo PowerShell antes do corpo: arquivos sintéticos aceitos e cinco
seleções inválidas recusadas. Um teste persistente executa o comando Python com
LAF simulado, conferindo três roots sintéticos, porta, timeouts e CTRL/RSET. O
monitor/limpeza e lançamento do probe foram comparados ao estado anterior e
continuam iguais. Não houve acesso serial, USB ou reset real. Fixtures temporárias
vazias foram removidas; nenhum dado do usuário foi removido.

### Backup explícito do extrator Android

`extract-android-rt.sh ABSOLUTE_BACKUP_DIR [NEW_OUTPUT.tar.gz]` não busca mais o
último backup em `work/`. Backup relativo, traversal, UNC, delimitador `:` e
controles são recusados; as três imagens exigidas devem existir e não estar vazias.
Isso valida seleção/presença, não integridade nem compatibilidade do backup.
Saída relativa parte da raiz do projeto; arquivo/link existente é preservado e a
publicação tar usa criação exclusiva. O default de saída continua interno ao
projeto. Use `--help` para consultar o contrato sem iniciar extração.

Staging agora usa diretório único com permissão privada em `/var/tmp`; o script
não apaga o staging anterior e mantém a nova extração para inspeção. O restante
da seleção de conteúdo e dos comandos debugfs foi preservado. Não executar para
testar portabilidade: a verificação deste incremento foi Bash syntax/help, prefixo
isolado em fixtures (oito recusas/cwd externo), comparação exata do corpo e tar
sintético byte-idêntico, incluindo recusa de sobrescrita. Nenhuma imagem de backup
real foi extraída, nenhum staging antigo removido ou arquivo no telefone alterado.

### Paths de ambiente do builder Alpine

Em `build-alpine-rootfs.sh`, OUT_DIR, ANDROID_RT, AUTHORIZED_KEYS e WPA_CONF
relativos partem do checkout antes da mudança de diretório para build. Entradas
de arquivo explicitamente selecionadas precisam existir e não estar vazias;
OUT_DIR deve ser diretório ou destino novo. Valores vazios, traversal, UNC,
controles ou paths Windows não convertidos são erros, sem fallback. Entradas
opcionais omitidas e defaults permanecem. Não há nova fonte de configuração.

`--help` consulta o contrato sem build. Validação offline: Bash syntax/help,
prefixo isolado com raiz temporária/cwd externo, seleção relativa/absoluta/default
e 20 recusas. Corpo do build desde VER, incluindo pacotes, hash, montagem/chroot
e integração, permaneceu byte-idêntico. Não foram executados download, build,
montagem ou chroot; essa migração não valida uma imagem nem autoriza instalação.

### Arquivos locais do envio serial

`push-files-serial.py PORT DEST FILE [FILE...]` resolve FILE relativo pelo checkout
e verifica todos os arquivos antes de importar/abrir serial. Lista vazia, fonte
ausente ou diretório são recusados antes de comunicação. Agora import/help são
inertes; porta e destino remoto continuam explícitos. Helpers e corpo de envio
permanecem iguais após remover a indentação de `main`; o protocolo e a política
legada de destino shell não foram ampliados ou tornados genéricos.

Três testes offline passaram com serial simulado, incluindo cwd externo, seleção
relativa/absoluta, payload gzip/base64 exato e resultados para checksum correto e
incorreto. Nenhuma porta foi aberta, thread de leitura real iniciada ou arquivo
remoto escrito. Uso físico continua dependendo de autorização; testes simulados
não comprovam transferência no aparelho.

### Paths do verificador LK e scanner pstore

`check-k40s-lk-overlay.py` resolve DTB, tabela de overlays e referência relativa
pelo checkout. O campo `dtb` continua com o argumento fornecido pelo usuário,
sem inserir o path absoluto do host. `scan-k40s-pstore.py` usa a mesma base para
o dump. ABI, zonas, flags, regras de overlays e contratos permanecem iguais;
nenhuma descoberta automática de dump, backup ou PCB foi acrescentada.

Quatro testes dirigidos passaram: seleção relativa/absoluta em cwd externo nos
três modos LK, rótulo de relatório, contrato CCF existente e scanner sintético
com saída idêntica. A comparação exata do código descontou somente as mudanças
de paths. Ferramentas LK foram simuladas e o teste de rótulo usou tabela vazia;
isso não comprova aplicação de overlay ou boot. Nenhum dump privado foi lido.

### Configuração SSH dos wrappers PWRAP e estabilidade

`installer/lts-pwrap-diag-session.ps1` e `installer/lts-stability-session.ps1`
consultam `portkit.profiles.load_lab` pelo Python dedicado, capturando somente os
campos SSH necessários. A consulta ocorre antes de abrir transcript/transporte;
`-ValidateOnly` continua retornando antes dela. Configuração ausente/inválida não
usa fallback nem inicia SSH. Nenhuma nova configuração ou busca de chave/host
foi criada. A configuração privada não é impressa no relatório desta revisão.

Um teste persistente com loader real e config sintética verificou seleção,
campos emitidos e recusas por configuração ausente/insegura. AST e snippets
PowerShell isolados passaram em seis casos com Python/SSH simulados; argv da
telemetria foi conferido. Comparação exata descontou só consulta e seleção SSH:
hashes, limites de bateria, ordem de flash/coleta e recuperação continuam iguais.
Não foi iniciado transcript, sessão, subprocesso externo ou acesso ao aparelho.

### Fronteira Windows/WSL do builder legado do instalador

`installer/build.ps1` exige StockBoot, WslDistro e WslUser explícitos, valida
arquivos selecionados, converte via wslpath e consulta runtime-root existente
antes da saída. Usa `--exec` com arrays de argumentos/env, sem bash -c ou montagem
manual de drives. SshPublicKey não usa HOME; WpaConfig explícito inválido não cai
no arquivo local opcional. Destinos anteriores são preservados. O gerador GPT
recebe `out/gpt` novo, não `flash` já existente, e move somente seus dois outputs.
Não foram alterados pacotes, fontes, pins, política de flash ou alvo do kernel.

AST e plano completo PowerShell com WSL/Python/escritas simulados passaram em
seis casos: sucesso, saída existente, conversão inválida, runtime ausente, boot
relativo e chave explicitamente vazia. Conferidos 13 comandos WSL, dois Python,
arrays env com espaços, staging GPT e ordem textual das etapas antes/depois.
Nenhum build, download, montagem, cópia real ou transporte foi iniciado; isso
não comprova geração de imagens. O fluxo permanece legado 4.9, separado da
primeira entrega Linux 6.18, e não autoriza executar a instalação permanente.

### Seleção de imagem nos flashes boot/logo

`installer/flash-boot.ps1` e `flash-logo.ps1` resolvem imagem relativa pelo
checkout e usam Get-Item literal. O hash do logo também usa path literal, sem
interpretar colchetes como glob. Restore do logo exige `-BackupImage` absoluto
junto a `-Restore`, sem busca de backups; combinações ambíguas são recusadas.
A limpeza `.state` do boot foi movida para depois da validação local de imagem.

Treze verificações nativas com imagens sintéticas passaram: caminhos relativos/
absolutos, colchetes, restore explícito e recusas antes do Python/limpeza de
estado simulados. Setores, tamanhos e argumentos foram conferidos e o corpo a
partir do transporte permaneceu idêntico. Não houve execução real de mtkclient,
flash, leitura de backup ou remoção do `.state` do projeto. Arquivos temporários
sintéticos foram removidos. Esses scripts não devem ser executados como teste
de portabilidade e continuam exigindo autorização física própria.

### Backup explícito do restaurador Android legado

`installer/restore-android.ps1 -LegacyLayout` exige StockBoot absoluto local,
sem traversal ou controles; não escolhe backup por diretório/data. O hash usa
path literal. O guard que recusa layout atual continua igual, assim como o hash
esperado, o warning legado por divergência e a chamada para escrever boot_a.
Essa migração não aprova o restaurador para uso nem altera sua política de hash.

Oito casos PowerShell com raiz/hash/Python simulados passaram: seleção literal
com espaços/colchetes, comportamento de hash igual/diferente e recusas antes da
chamada. AST e comparação exata confirmaram guard e corpo de escrita inalterados.
Não houve leitura de backup, execução Python ou transporte. O parser vendor
multi usado em outros scripts continua pendente para paths contendo espaços;
esse problema foi identificado, não resolvido ou contornado por junction.

### Batches internos do instalador em checkout com espaços

O parser vendor multi usa split por espaço, sem interpretar aspas. Em
`installer/flash.ps1` e `dump-pstore.ps1`, os nomes internos conhecidos entram
como `installer/out/flash/NAME` e `work/dram-STAMP-ZONE.bin`. A chamada multi usa
Push-Location na raiz descoberta e Pop-Location em finally, sem junction, nomes
curtos, alteração do fornecedor ou protocolo paralelo. Paths absolutos externos
não são enviados dentro desses batches; leitura/preflight continuam na raiz.

AST e snippets reais isolados com processo simulado passaram em seis casos,
usando raiz com espaços/colchetes. Foram conferidos os quatro comandos de cada
batch, tokens segundo o split vendor, ordem, offsets/tamanhos e restauração do
cwd em sucesso, retorno não zero e exceção. Nenhum processo real, `.state`,
backup, captura ou aparelho foi usado; fixtures vazias foram removidas. Isso
cobre somente esses dois consumidores, não todo batch existente. As validações
de imagem/partições e autorização física não foram relaxadas.

### Workspace e manifestos do runner KUnit

`run-kunit-offline.py --workspace` exige path Linux absoluto, sem traversal,
UNC, controles ou separadores Windows, antes de resolver symlinks. Mantém as
recusas de `/mnt`, checkout e nome fora de `kunit-*`. O loader existente de
test sets resolve manifestos relativos pela raiz do projeto fornecida, não cwd,
preservando confinamento inclusive de symlinks. Não há configuração paralela.

Onze verificações dirigidas passaram em duas execuções: seleção em cwd externo,
recusas antes de preparação, árvore existente, pins e suíte de test sets com
isolamento. Fluxos prepare/run emitidos pelos testes foram simulados, não builds
ou execução UML real. Não houve acesso ao aparelho ou alteração de pins/fontes.

### Override da entrada kselftest

`tools/testing/selftests/portkit/portkit.sh` descobre a raiz pelo script quando
PORTKIT_ROOT é omitido. Quando definido, esse override tem precedência e deve
ser diretório absoluto nativo, sem traversal, UNC, controles CR/LF ou separador
Windows, contendo `tools/test-offline.py`. Vazio ou inválido produz erro antes
de criar saída temporária/iniciar a suíte; não há fallback pelo cwd.

Onze verificações shell isoladas passaram: raiz descoberta/override com espaços,
falha da suíte simulada e oito recusas. A fixture de test-offline não foi executada;
python3 era uma função simulada que verificava o argumento exato. Formato TAP,
tratamento do resultado e limpeza temporária permanecem. Não houve suíte ampla,
build ou transporte; diretórios temporários sintéticos foram removidos.

### Paths dos inspetores A/B e comparação IRQ PMIC

`inspect-k40s-ab.py` resolve argumentos relativos record/partition-image/
compare-record pela raiz do projeto. O comparador `compare-k40s-pmic-irq-init.py`
exige as duas árvores externas como paths nativos absolutos, recusando relativos,
traversal, UNC e controles antes de ler qualquer fonte. Não há seleção automática
de fontes. Pedido remoto A/B, CRC, limites e interpretação dos parsers não mudam.

Doze testes dirigidos passaram em cwd externo: relatórios A/B byte-idênticos
para paths relativos/absolutos em fixtures; seleção de fontes PMIC e retorno
igual/diferente simulados, além de recusas. Comparação exata do código confirmou
somente mudanças de CLI/paths. Nenhum snapshot privado, fonte externa real,
transporte ou operação no aparelho foi usado; não há novo aceite de boot.

### Backup do extrator GPU legado

`extract-gpu-runtime.sh ABSOLUTE_BACKUP_DIR` exige diretório de backup explícito,
sem default datado, descoberta ou fallback. Recusa path relativo/traversal/UNC/
Windows não convertido/controles e exige system_a.bin/vendor_a.bin não vazios
antes de criar saída. Output permanece artifacts/gpu-bringup; seleção de conteúdo,
comandos e política incremental do extrator legado não mudam. Presença não é
prova de integridade do backup; não houve nova autorização de extração/uso.

Bash syntax/help e prefixo isolado verificaram seleção com espaços/cwd externo
e oito recusas. Comparação exata confirmou todo o corpo desde apex inalterado.
Não houve debugfs, extração, backup real, artefato ou aparelho. A frente GPU
permanece adiada; não foi feita generalização funcional ou arquitetura nova.

### TASK_OUTPUT explícito nos builders

`build-initramfs.sh`, `build-wifi-modules.sh` e `build-propshim.sh` distinguem
TASK_OUTPUT omitido de explicitamente vazio. Omitido mantém o destino documentado;
seleção relativa válida parte do checkout. Vazio, traversal, UNC, separador/path
Windows não convertido e CR/LF são recusados antes de consultar runtime, sem
fallback. Não são alterados os comandos de build, assinatura ou empacotamento.

Vinte e sete verificações de prefixo isolado passaram em cwd externo: três
seleções válidas e seis recusas por builder. Consulta Python/runtime foi simulada
e o prefixo terminou antes do primeiro mkdir. Syntax Bash e comparação exata
confirmaram somente o bloco de validação adicionado, sem executar build, ler
chaves ou gerar artefatos. Essa verificação não comprova módulos no aparelho.

### Seleção de chave pública no builder legado

`installer/build.ps1` recusa SshPublicKey vazio ou com cabeçalho privado
PEM/OpenSSH/PuTTY antes das conversões WSL e criação de saídas. Conteúdo não é
impresso. O helper public_key do payload SSH foi inspecionado, mas seu contrato
restrito Ed25519 não foi imposto ao instalador legado: formatos públicos e
múltiplas linhas antes aceitos permanecem. Não há nova infraestrutura de chaves.

Dez casos PowerShell isolados passaram com conteúdo sintético/simulado, incluindo
algoritmos públicos diferentes, várias linhas e sete recusas. Isso detecta enganos
de seleção comuns; não é validação criptográfica geral de authorized_keys. Nenhum
arquivo de chave real foi consultado, copiado ou exibido; sem WSL, build ou imagem.

### Diretório do processo do wrapper MediaTek somente leitura

`mtk-readonly.py` inicia o cliente com cwd na raiz descoberta pelo módulo. Paths
relativos do cliente (inclusive saída/estado) deixam de depender do terminal;
argumentos absolutos permanecem. Allowlist, argumentos, escolha do interpretador
dedicado/atual e propagação do código de saída não mudam. O parser multi vendor
continua sem suporte a paths com espaço dentro de um token; os consumidores
internos migrados usam paths relativos fixos, sem alterar esse parser.

Dois testes dirigidos passaram com subprocesso simulado, raiz temporária com
espaços e cwd externo. Conferidos argv/cwd/retorno nas duas seleções de runtime
e oito recusas antes de executar. Nenhum cliente real, USB, `.state`, captura ou
arquivo do aparelho foi acessado. Isso não amplia autorização de leitura física.

### Base dos paths do helper SHA-256 Windows

`installer/file-sha256.ps1` resolve argumentos relativos de Get-K40sFileSha256
pela raiz descoberta a partir do script de definição. Paths absolutos continuam
literais; formas drive-relative como `C:arquivo` são recusadas por dependerem de
estado do terminal. Cálculo streaming, saída hexadecimal e descarte dos recursos
permanecem. Nenhum hash/pin histórico foi recalculado para aceitar uma diferença.

Cinco verificações PowerShell nativas passaram: README público por path relativo/
absoluto em cwd temporário externo, arquivo ausente e duas formas drive-relative
recusadas antes de abrir arquivo. O cwd foi preservado. Não houve leitura de
imagem privada, transporte ou alteração de estado; diretório temporário vazio
foi removido. Isso verifica resolução/digest, não aprovação de boot ou flash.

### Staging Alpine e retirada de paths pessoais dos exemplos ativos

O builder Alpine consulta o mesmo `kernel-workspace.py runtime-root` dos demais
builders, após validar inputs. Exige o diretório configurado existente e cria
`alpine-rootfs.XXXXXX` privado/único dentro dele; não reutiliza nem remove staging
global antigo. Tarball/cache e imagem ficam nesse staging, que é preservado para
inspeção. Isso muda a localização de build, não autoriza limpar diretórios antigos
ou alterar limites/controles de montagem. Configure development.runtime_root no
lab.json ignorado para o filesystem Linux apropriado.

Prefixo isolado com consulta runtime simulada verificou duas execuções distintas,
modo 0700, preservação da anterior e recusa de runtime ausente, sem saída/build,
download ou chroot. Oito testes dirigidos SSH, KUnit, libfdt e equivalência congelada
passaram após trocar dados de fixtures por sintéticos. O teste congelado recupera
a identidade histórica exclusivamente do testemunho privado já configurado, sem
repinar baseline. Exemplos ativos de arquitetura/kernel/desenvolvimento foram
sanitizados; paths ilustrativos devem ser substituídos por seleção explícita.
Manifestos históricos e documentos de resultados originais não foram reescritos.
Persistem tarefas de seleção Python/libusb em wrappers; a migração não terminou.

## Prioridade de entrega — 2026-10-27

Seguir a diretriz de trabalho do [AGENTS.md](../AGENTS.md): cada etapa deve
desbloquear um resultado observável no aparelho. Reutilizar código disponível,
integrar em incrementos pequenos e executar validação proporcional aos caminhos
afetados. Depois da primeira integração funcional, consolidar regressões e ampliar
telemetria e testes prolongados conforme os problemas encontrados.

Compilação, verificações críticas de falha, limites elétricos e recuperação
continuam anteriores à ativação correspondente. Os comandos de teste abaixo são
ferramentas disponíveis, não uma exigência de executar todas as suítes a cada
alteração. Usar a suíte direcionada; ampliar quando houver impacto transversal,
falha ou requisito explícito. Preservar os controles existentes.

No relatório de cada etapa, informar: entrega funcional, evidência no aparelho ou
somente offline e próximo bloqueio. Generalização e infraestrutura adicional ficam
para depois, salvo quando necessárias para essa entrega.

## Ambiente

O pacote continua `portkit`; a raiz do projeto é descoberta pelos scripts.
Configure o runtime Linux externo em `development.runtime_root` no lab.json
local. Não há dependência operacional autorizada de junction ou nome antigo.
Diretórios e aliases presentes nas evidências históricas não devem ser apagados
como parte desta migração; exemplos abaixo omitem caminhos pessoais.

O ciclo exige `boards/k40s/local/lab.json` (ignorado). Use `lab.example.json`
como referência, configure IPv4 normal e caminho absoluto externo da identidade;
não copie chaves para o projeto. O contrato atual mantém root/22 normal e
root/10.15.0.1/2222 USB e host-key estrito. O pin do host USB permanece no manifesto
validado do payload. Sem config válida, parar antes do transporte é esperado.

Usar Ubuntu 24.04 LTS no WSL2, Python 3.12. Workspaces de kernel e saídas C ficam
no filesystem Linux, não em `/mnt/c`. O código host pode ser lido do projeto
Windows durante a transição. Versões: `manifests/environment.json` e
`manifests/host-requirements.txt`. Não atualizar checkouts para instalar dependências.

O ciclo físico legado continua híbrido Windows/WSL: **não** foi certificado como
CLI Linux nativa. A preferência por Linux para build/teste não muda esse contrato.

## Comando único seguro

Para inspecionar componentes sem build/transporte, use no venv oficial:
`python tools/kernel-workspace.py components --board k40s`. A ação requer
jsonschema 4.26.0 já fixado no venv e funciona sem lab.json. Testes novos no Python
Windows sem essa dependência informam explicitamente o ambiente exigido.

Dentro do WSL, na raiz do projeto:

```sh
python tools/test-offline.py  # Python do venv preparado no PATH
```

Do PowerShell, sem mudar de pasta:

```powershell
wsl -d 'DISTRO_CONFIGURADA' --cd '/CAMINHO/LINUX/DO/CHECKOUT' --exec /CAMINHO/DO/VENV/bin/python tools/test-offline.py
```

A allowlist fixa testa core/perfis, kernel-workspace offline, política IRQ em C e
DTC/libfdt. Não faz discovery geral; bloqueia import dos transportes USB/serial,
rede, arquivos de dispositivo e subprocessos não aprovados. Não aceita nomes de
testes/comandos/hardware por argumento. É defesa contra acidentes em testes
revisados, não sandbox contra código hostil. A execução final não pode deixar um
transporte carregado. Não é permitido contornar o bloqueio para “só ler” o aparelho.

Num checkout somente de fontes, dois casos históricos de perfil inicial que
dependem de evidência privada são explicitamente ignorados com essa justificativa;
não são fornecidas evidências falsas nem relaxadas validações de produção.
A comparação libfdt com os seis DTBs reais também é explicitamente ignorada
quando o backup está ausente; os testes sintéticos e negativos continuam ativos.

No Windows nativo, a entrada segura termina com “somente WSL/Linux”. As três
falhas antigas estão identificadas e puladas com motivo explícito; isso não
transforma o ambiente Windows em ambiente oficial de build.

Para reconstruir o venv em um **novo diretório Linux**, usar Python venv e
`pip install -r manifests/host-requirements.txt`. A instalação precisa de rede e
fica separada da execução offline. Dependências estão versionadas; o lock não
contém hashes de todos os wheels, portanto não é atestado de supply chain.

## Suíte legada e testes no aparelho

### Referências WMT separadas do desenvolvimento — 2026-10-29

Os testes que leem `staging-wmt-lts-20261027-v1` usam agora a raiz nomeada
`wmt_baselines`, independente de `development`, no resolver já existente.
O mapa público `manifests/test-sources.json` não contém raízes de host.
Configurar o mesmo formato em `local/test-sources.json` (ignorado pelo Git),
ou selecionar explicitamente um arquivo privado. Nenhuma fonte é descoberta,
copiada ou declarada imutável por essa configuração.

Precedência do resolver existente: argumento `configuration`, variável
`KPF_TEST_SOURCE_ROOTS`, `local/test-sources.json`, mapa público vazio. Um arquivo
selecionado substitui o mapa inteiro; inválido/ausente não aciona fallback.
Paths relativos do arquivo de configuração são relativos à raiz do projeto
descoberta pelo módulo, não ao diretório do terminal. Valores de `roots` continuam
absolutos, locais e explícitos, sem traversal ou compartilhamentos UNC.

Para selecionar uma referência preservada, `KPF_TEST_SOURCE_ROOTS` pode apontar
para um JSON privado com o mapa completo, por exemplo:

```json
{
  "schema": 1,
  "roots": {
    "development": "/srv/kpf-sources",
    "wmt_baselines": "/srv/kpf-references"
  }
}
```

O subdiretório esperado é `staging-wmt-lts-20261027-v1`. O exemplo não cria nem
recupera esse conteúdo. Configuração explícita substitui o mapa inteiro; omitir
`wmt_baselines` gera erro, sem fallback para desenvolvimento. As suítes legadas
mantêm seus skips por ausência de fontes/toolchain; um skip não comprova baseline.
Hashes, modelos, patches e verificações permanecem específicos de cada regressão.
Nem todos os casos históricos necessariamente aceitam a mesma revisão: antes de
adotar uma cópia, verificar os pins de cada suíte relevante e sua sequência de patches.
Fontes vendor originais continuam em `development`; recortes locais em `artifacts`
não foram migrados. Isso não muda fontes de build nem ensaios físicos.

A referência de staging usada nas verificações históricas divergira dos pins
de `wmt_lib.c` e `stp_dbg.c`; relocalizar não resolve essa divergência.
O próximo bloqueio é recuperar/reconstruir as revisões esperadas com origem e
patches verificáveis, não atualizar pins ou copiar a árvore divergente e chamá-la
de referência validada.

`python3 -m unittest discover -s tools/tests -p 'test_*.py'` é a regressão histórica
do laboratório, não a entrada segura transport-free. Depende de sources, fixtures
e evidências privadas excluídas do Git; um clone limpo não deve prometer cobertura
idêntica. Muitos casos usam mocks de BROM/DA/flash: mensagens de escrita desses
mocks não representam operações no telefone. Testes físicos são workflows
separados, nunca descobertos pela entrada offline.

`manifests/test-catalog.json` classifica cada método, incluindo os dois herdados.
`tools/catalog-tests.py --refresh` regenera esse catálogo por AST, sem importar
testes ou drivers. Classificações podem se acumular: offline, compilação C,
WSL/QEMU, telefone somente leitura, escrita temporária e recuperação obrigatória.
WSL/QEMU no catálogo significa dependência POSIX/toolchain, não execução QEMU já
comprovada. Classificação não concede autorização de hardware.

## KUnit e kselftest

O runner atual também exige a suíte `mt6357-car-raw-offline`: três casos de CAR
bruto, incluindo 2^21 payloads, bits ignorados/sentinelas e falhas preservando out.
Agora são 18 casos em cinco suítes: IRQ3, CAR3, timing MT6765 com3,
quatro testes upstream `iio-multiply` e cinco testes do helper de bateria com
power_supply/workqueues reais e medições sintéticas. JSON com qualquer suíte
ausente/falha, contagem incorreta ou caso inesperado é recusado. Provas antigas
de seis casos continuam históricas e não são sobrescritas.
As provas antigas abaixo continuam históricas; use sempre uma árvore nova depois
de alterar os inputs e preserve os diretórios preparados anteriores.

`kernel/tests/kunit` porta os testes puros da política IRQ para KUnit: 65.536
status, erro tardio/notificação única, quota spurious e cancelamento. O objeto
compilou para ARM32 contra a árvore 6.18.58. Em 2026-10-25, os mesmos três casos
executaram e passaram em um kernel UML 6.18.58 isolado, em duas invocações
explícitas, com kernel/config/JSON dos resultados idênticos. Não houve execução
no telefone, nem validação de IRQ físico ou ARM32 em runtime. Os oráculos
Python/C e a prova ARM32 continuam preservados, não substituídos.

Preparar e executar pelo runner oficial, em um workspace Linux **novo**:

```sh
python3 tools/run-kunit-offline.py prepare --workspace /srv/kpf-runtime/kernel-workspaces/kunit-host-NEW
python3 tools/run-kunit-offline.py run --workspace /srv/kpf-runtime/kernel-workspaces/kunit-host-NEW --attempt first --jobs 4
```

O adaptador verifica o tarball, reutiliza a extração segura e patch --fuzz=0,
integra testes puros de IRQ/CAR/timing, a suíte IIO upstream e testes do helper;
aplica os três patches staging auditados ao helper apenas nessa árvore e chama
`kunit.py build`/`exec`. Verifica também hashes de inkern.c/iio-test-multiply.c.
Confere `.config` **antes** da execução: sem NET/UML_NET, HOSTFS, MCONSOLE ou
MODULES, KUNIT_ALL_TESTS, driver AUXADC ou objeto normal ADC_BATTERY_HELPER.
POWER_SUPPLY e KPF_ADC_HELPER_KUNIT_TEST são exigidos; o fonte do helper entra
uma única vez no TU de teste. Root device e supply fictícios são liberados por
grupo devres, sem barramento/driver físico. IIO core/testes não habilitam acesso
ao PMIC. Usa TMPDIR Linux, pois /dev/shm do WSL pode ser noexec.
Limites: 900s para build+exec, 60s para o kernel; erro/timeout/interrupção sinaliza
e recolhe o grupo POSIX, sem retry. Cada tentativa tem diretório exclusivo com
started/verified ou failed JSON e log; não sobrescrever resultados anteriores.
Uma nova invocação explícita com --attempt diferente pode reutilizar a build,
somente após conferir os hashes dos inputs/preparação.

Essa execução não faz parte do comando rápido `test-offline.py`: ali entram os
testes do adaptador com mocks, inclusive timeout/cleanup e bloqueio de configuração
insegura, sem iniciar UML ou uma build completa.

Prova de compilação externa, com diretório de saída novo:

```sh
make -C /srv/kpf-runtime/kernel-workspaces/lts-6.18.58-pwrap-atomic-v1/linux-6.18.58 \
  O=/srv/kpf-runtime/kernel-workspaces/lts-6.18.58-pwrap-atomic-v1/build \
  M="$PWD/kernel/tests/kunit" MO=/srv/kpf-runtime/kunit-compile-NEW \
  ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- PORTKIT_ROOT="$PWD" k40s_irq_policy_test.o
```

`make -C tools/testing/selftests/portkit run_tests` executa o contrato kselftest
TEST_PROGS/TAP e chama a entrada offline. Use o Python do venv no PATH para incluir
o teste libfdt. Funciona standalone; integração no runner de uma árvore Linux
maior ainda não é alegada como validada.

## Sessões residentes do kernel nativo

Para iterar drivers compilados como módulos, agrupar testes na mesma sessão
SSH USB do 6.18; não encerrar o ciclo após cada leitura ou troca de módulo.
Usar `tools/k40s-resident.py run`, `push` e, apenas ao terminar a sessão, `end`.
Conferir hash/vermagic antes de insmod, dependências e ordem de remoção, manter
eMMC/rootfs somente leitura e não carregar aquisições concorrentes do PMIC.

O mecanismo existente aceita imagem residente preparada com
`--resident --session-seconds N` (120–3600 segundos) e ciclo com
`--resident-minutes M` (2–60 minutos, exige `--require-ssh-ram`). Os dois
limites devem corresponder; mudar o argumento no host não estende uma imagem
que já foi iniciada. Manter o coletor de recuperação do ciclo vivo enquanto
se usa o SSH. Não executar outro ciclo simultaneamente nem desativar o watchdog.

Mudanças de kernel/DT ainda exigem nova imagem e boot; uma falha pode exigir
recuperação. `end` ou o prazo da imagem levam à coleta/restauração já validada.
Isto é uma sessão temporária de laboratório, não instalação permanente nem
garantia de recuperação de toda classe de falha. Preservar o 4.9 e seus hashes.

## Git, licenças e preservação

Repositório apenas local, sem remote/push. `.gitignore` começa negando raízes e
libera somente fontes revisados; exclusões finais protegem diretórios privados,
imagens, binários, arquivos grandes e chaves. Antes de cada commit:

```sh
git add -- <arquivos-revisados>
python3 tools/check-repository.py
git diff --cached --check
```

O verificador lê **bytes do índice** e recusa arquivos binários/>1 MiB, roots
privados, chaves, gitlinks e symlinks não revisados. `.gitignore` não é scanner
universal de segredos; revisar manualmente fontes/patches antes de compartilhar.

Baseline anterior à refatoração: commit `b2c9ac8`, inventário SHA-256 em
`docs/baselines/pre-refactor-20261025.json`. Não sobrescrever essa evidência.
Ferramentas próprias MIT, código kernel próprio GPL-2.0-only, terceiros preservam
licenças originais. Os sete C/H sem identificação receberam SPDX MIT. Arquivos
críticos preservados usam anotações SPDX em `REUSE.toml` em vez de comentários
cosméticos que mudariam seus hashes. Isso não é alegação de certificação REUSE
completa de todos os arquivos históricos/derivados.

Terceiros: `manifests/third-party.json`, `source-archives.json` e
`python-environment.json`. Patches locais em `third-party/patches`; forward apply
somente sobre a revisão exata em uma cópia separada. Reverse-check sem escrita
confirmou correspondência aos checkouts atuais. Nada foi atualizado nesses repos.

Histórico permanece em paths canônicos, catalogado em `historical/`, sem apagar
experimentos nem colocar evidências privadas/binários no Git.
