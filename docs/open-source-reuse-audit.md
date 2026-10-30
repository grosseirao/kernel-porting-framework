# Auditoria de reutilização open source

Nota de privacidade (2026-10-29): os exemplos de comando abaixo omitem o path
pessoal do runtime. KPF_RUNTIME_ROOT é entrada explícita apenas desses exemplos,
não um novo loader de configuração. Use o runtime local selecionado; comandos
históricos sanitizados não substituem os registros originais ou autorizam build.

## Fixtures C do porte sem cópia de componentes — 2026-10-29

As fixtures existentes podem usar o mapa de fontes `support.source_path`, já
validado, com uma raiz nomeada `kpf` explícita. Reutilizar `component_source`
para verificar os headers selecionados e derivar somente seus diretórios de
include. Não criar mais configuração, descobrir o pai ou mudar fontes C/flags.
Manter os oráculos LG/Linux e hashes existentes. Esse mapa configura fontes
dos testes, não substitui o `.env` de runtime/SSH. A ausência de `kpf` é erro,
sem retorno às cópias locais. Fontes e notices permanecem no framework original.
Drivers/frameworks Linux e ferramentas de RE não substituem essa seleção host;
não introduzir novos drivers, compiladores nem protocolos.

## Perfis kernel e KUnit com fontes externas explícitas — 2026-10-29

Estender os workflows MIT existentes, reutilizando `component_source` do KPF:
somente nomes lógicos sob `kernel/components` usam a raiz compartilhada. Perfis,
patches, evidências, fontes da placa, arquivos de configuração e arquivo-fonte
do kernel permanecem no workspace consumidor. Não reinterpretar os manifestos
históricos nem mudar seus hashes para acomodar o layout.

Nenhuma ferramenta/driver paralelo é necessário. KUnit oficial, tarfile,
hashing e instalador de fontes existentes continuam responsáveis pelo preparo.
APIs de driver Linux/postmarketOS/MediaTek/Qualcomm não substituem resolução
de inputs host. Preservar licenças por arquivo, fingerprints, staging e recusas;
raiz inválida deve falhar antes de novos diretórios/extracão quando selecionada.
Verificar com fixtures temporárias; não executar build kernel/UML nesta migração.

## Fontes compartilhadas para builders — 2026-10-29

O builder de CAR MT6357 ainda encontra dois headers no porte. Reutilizar
validadores de raiz/path de `portkit.composition` e hashing existente para
resolver arquivos somente em `kernel/components`, por raiz explícita.
Inventário e builder devem compartilhar essa recusa, sem buscas no pai,
fallback silencioso, parser novo ou mudança no C. Fonte MIT do resolver;
headers mantêm avisos por arquivo. Compiladores/driver frameworks não substituem
a resolução host; nenhum driver Linux/postmarketOS/MediaTek/Qualcomm é alterado.

Preservar nomes lógicos, ordem e bytes do staging, flags de make e hashes de
kernel/módulo. Testar raiz externa e falhas antes de criar saída ou chamar make.
Não construir nem operar o aparelho para testar essa resolução de paths.

## Raiz explícita de componentes compartilhados — 2026-10-29

O consumidor Git independente precisa usar catálogo, schemas e fontes de chip
do KPF sem duplicá-los ou descobrir o checkout pai. Estender o loader MIT
existente `portkit.composition.load_composition` com `components_root` opcional,
absoluto e explícito. Reutilizar `_workspace_root`, jsonschema e as verificações
atuais de namespace/symlink, sem novo resolver, transporte ou sistema de plugins.
APIs de drivers Linux, postmarketOS e protocolos MediaTek/Qualcomm não resolvem
essa fronteira host; não alterar drivers para resolver layout de repositórios.

Catálogo, schemas e definições vêm dessa raiz; `reusable_sources` somente de
`kernel/components` nela. Perfil, composição, evidências, fontes legadas e fontes
da placa continuam na raiz do porte. Sem argumento, manter o comportamento
anterior e os mesmos hashes/fingerprint. Raiz explícita inválida não pode cair
para uma cópia local. Preservar licença MIT do loader e licenças das fontes;
nenhum protocolo físico nem novo código de driver é introduzido.

Aceite: composição integral idêntica com raízes separadas, inclusive sem cópias
compartilhadas no porte; recusar raiz relativa, componente ausente e symlink.
Não remover dependências dos builders antes de migrar e verificar seu consumo.

## Seleção canônica de candidatos DT reaproveitada do porte — 2026-10-29

Necessidade existente: compare-reference-dt.py procura uma correspondência
canônica única e usa um candidato de fallback explícito quando não há match.
Extrair esse mecanismo para core.devicetree, mantendo a seleção de tabelas,
nomes boot-dtb/dtbo, IDs, diretórios e política de placa no workflow consumidor.
Fonte local MIT; preservar canonical_dts/compare_dtb, libfdt e DTC existentes.

Linux/DTC/libfdt já fornecem parsing e canonicalização; não implementar parser
nem reescrita de propriedades. Drivers/postmarketOS/MediaTek/Qualcomm não são
substitutos para essa seleção host. API recebe bytes de referência, candidatos
nomeados e callback explícito de leitura, sem glob, perfil ou transporte interno.
Não introduzir um sistema de plugins/loader. Compatibilidade DT não é inferida.

Aceite: seleção única, fallback, ambiguidade e candidato inválido; preservar a
ordem de leitura/canonicalização e releitura do selecionado no workflow atual.
Comparar relatórios/arquivos e falhas do consumidor original; output continua
create-only e só após validar todas as entradas. Testes sintéticos com libfdt/DTC,
sem instalação, imagem nova, alteração de pins ou execução no aparelho.

## Snapshot, contrato e comparação DT no toolkit — 2026-10-29

Reutilizar os corpos MIT existentes de inspect-boot-snapshot.py,
check-dt-contract.py e compare-dtb.py. O core segue usando libfdt para parsing,
DTC para canonicalização/diff e contratos estáticos já existentes; não implementar
parser, normalização de phandle ou inferência de compatibilidade. Comparar DTBs
não é validação de binding/driver/hardware. Drivers Linux/postmarketOS/MediaTek/
Qualcomm não são substitutos necessários para essa separação host.

Mover somente execução para o pacote, preservar adaptadores e obter workspace
absoluto pelo helper existente. Política/seletor de nó continua em perfil externo;
nenhum default K40S ou SSH no pacote. Libfdt FdtSw existente cria fixtures, sem
novo gerador/parser binário. Mesmas licenças MIT dos scripts/testes; dependências
libfdt/DTC já declaradas e disponíveis, sem download/instalação. Aceite: saídas e
códigos antes/depois, recusas de input/contrato/output e pacote fora do workspace.

## Decodificadores binários por perfil no toolkit — 2026-10-29

Reutilizar os corpos MIT existentes de decode-ramoops-console.py e
decode-session-logs.py, core.ramoops/session_logs/captures e seus controles de
publicação. Mover execução para o pacote, manter adaptadores e resolver workspace
explícito pelo helper existente. Não criar codec, varredura de memória, inferência
de layout ou reconstrução de rings. Linux ramoops/libfdt e pilhas de drivers
Linux/postmarketOS/MediaTek/Qualcomm não precisam ser substituídos nessa extração.

Políticas permanecem no perfil externo; tamanhos/assinatura/ECC/variantes exigem
declaração e continuam limitados. Output é privado e só em diretório novo após
validação. Capturas com layout inválido ou override não permitido são recusadas;
preservar saída existente e não abrir transporte. Origem local MIT, sem fonte ou
dependência nova. Aceite: bytes de todos os arquivos e códigos antes/depois,
recusas existentes, suíte de integração e pacote isolado sem dados da placa.

O harness legado de tamanhos logbuf chama o mesmo main em processo, via loader
de testes existente, em vez de subprocesso Python recusado pelo offline_guard.
Sucesso mantém bytes hello/tamanho original/raw_inputs_modified=false; tamanho
divergente exige ValueError e nenhum diretório. Não mudar CLI legada, parser,
tamanhos, fronteira de layout, guard ou allowlist de execução para obter PASS.

## Analisadores de capturas textuais no toolkit — 2026-10-29

Reutilizar os corpos MIT de analyze-stability-log.py, analyze-smp-log.py e
analyze-register-snapshot.py, que já chamam os parsers core existentes. Nenhum
protocolo/parser novo ou executor de diagnóstico; mover a execução para o pacote,
conservar adaptadores nos caminhos atuais e adicionar raiz explícita pelo helper
existente. Políticas continuam nos perfis; capturas existentes são únicas entradas.

Linux/postmarketOS/MediaTek/Qualcomm não substituem essa fronteira host; seus
drivers, testes físicos e transportes ficam fora do incremento. Não adicionar
framework de plugins, configuração paralela ou inferência de dispositivo.
Aceite: mesmos códigos/relatórios, omissão de linhas privadas, validação de
contratos e publicação create-only; interpretação de log não é prova física.
Executar fixtures sintéticas em wheel isolado e regressões dos adaptadores.
Licença MIT preservada; nenhuma dependência nova ou operação no aparelho.

## Contrato de dependência e CLI DT table — 2026-10-29

Próximo recorte: declarar o consumidor K40S por requirements padrão, fixando a
versão de `kpf-portkit`, sem resolver customizado ou caminho ao checkout vizinho.
O pacote está em desenvolvimento; esse pin não afirma publicação de release ou
imutabilidade criptográfica do wheel. Consumo externo deve usar artefato local
revisado, sem índice de rede; hashes de release só após estabilizar o artefato.

Reutilizar o corpo MIT de `tools/inspect-dt-table.py`, core.android_dt/captures/
evidence e argparse, movendo apenas execução para o pacote e mantendo adaptador.
Não criar parser DT, lógica de seleção de PCB, extração de firmware ou novo
diagnóstico. A validação de FDT continua libfdt existente; Linux/postmarketOS/
MediaTek/Qualcomm não fornecem substituto necessário para essa fronteira host.
Usar a validação de raiz já existente, sem novo loader. Aceite: metadados e
recusas preservados, output create-only antes de ler inputs, workspace explícito
e wheel sem dados da placa. Sem mudança de driver/transporte/MediaTek ou rádio.

## Política SSH pertence ao workspace — 2026-10-29

Reutilizar `load_lab` e o parser `.env` existentes (MIT). Não criar transporte,
segundo loader ou resolvedor de hosts. O pin de usuário/portas/USB antes embutido
em `portkit.profiles` foi transferido, com os mesmos valores, para `ssh_contract`
do perfil K40S. O toolkit só valida o contrato explícito e sua correspondência
com a configuração local. A pequena validação de campos/tipos/IPv4/usuários
impede que contrato ausente/inválido vire aceitação irrestrita.

Host-key estrito, host normal IPv4 e chave absoluta externa permanecem invariantes
no toolkit; conversão wslpath, argv/timeouts e consumidores não mudam. Para o
K40S o aceite exige exatamente o contrato anterior e as mesmas recusas, não
maior permissividade. O `.env` não fornece nem sobrepõe a política pública.
Não se aplica substituir essa fronteira host por drivers Linux/postmarketOS/
MediaTek/Qualcomm; APIs e protocolos dessas pilhas permanecem inalterados.

Origem/licença: fontes locais profiles.py e perfil público; validação/testes
MIT. Nenhuma dependência, fonte vendor ou firmware novo. Alterar o JSON público
é mudança explícita de configuração versionada; não repinar evidências antigas
que registram o hash anterior do perfil. Não generalizar DA ou extrair MediaTek.

## Workspace explícito na fronteira toolkit/porte — 2026-10-29

Reutilizar os loaders de perfil/composição/.env existentes, em vez de criar
descoberta de projetos, outro formato ou resolver de dependências. Fonte local
MIT: `portkit/profiles.py` e `composition.py`; mesma licença dos novos checks.
Não se altera driver, transporte ou protocolo MediaTek; alternativas de kernel
Linux/postmarketOS/MediaTek/Qualcomm não substituem validação de paths host.

Problema: `development_root` sem project buscava `.env` junto do pacote Python;
as outras APIs aceitavam raiz relativa ao terminal. Isso mistura localização da
biblioteca com identidade do workspace. A validação pequena `_workspace_root`
é compartilhada pelos loaders existentes, recusa ausência/raiz relativa/controle
antes de ler inputs e não descobre nada. Override de runtime explícito continua
sem exigir project/configuração, preservando a precedência. Todos os chamadores
ativos do porte já fornecem raiz absoluta; não foi necessário mudar suas CLIs.

Aceite offline: recusas sem leitura implícita, mesmo runtime/precedência .env,
mesmos controles SSH/DA e plano K40S idêntico com toolkit de wheel em workspace
externo sem biblioteca local. Não remover a política /mnt, relaxar strict SSH,
mudar allowlists nem generalizar o transporte neste incremento.

## Extração da CLI Kconfig existente — 2026-10-29

Reutilização: mover o corpo de `tools/check-kconfig.py` (fonte local MIT) para
`portkit/cli/kconfig.py`, mantendo core.captures/kconfig/evidence, argparse e
unittest existentes. Não criar novo verificador, resolvedor de dependências ou
ferramenta de build. Linux Kconfig continua responsável por símbolos/dependências;
essa comparação literal não substitui olddefconfig. Transporte/hardware dos
projetos Linux/postmarketOS/MediaTek/Qualcomm não participa desse caminho host.

Única entrada nova: raiz absoluta explícita `--workspace`, necessária no comando
distribuído sem checkout. O adaptador antigo fornece sua raiz por localização do
script e permite override explícito. Não adicionar loader/configuração paralela,
busca de perfis ou defaults de host. Código novo é apenas a fronteira de execução
e validação dessa entrada; licença MIT, mesmo escopo do código extraído.

Aceite: mesmo parser, ordem dos fragmentos, códigos 0/2 e relatório byte a byte
para inputs iguais; recusas de entrada inválida e evidência create-only. Dois
testes CLI genéricos mudam de suíte, sem duplicação; integração do adaptador
permanece no workspace. Não há efeito em probe/erro/remove de drivers nem em
sequência física. Instalação do pacote não autoriza operações no aparelho.

## Separação inicial toolkit/workspace — 2026-10-29

Decisão: reutilizar `portkit`, seus parsers/validadores existentes, unittest e
empacotamento Python padrão setuptools/PEP517. Não há ferramenta de build,
loader de ambiente, transporte, driver ou diagnóstico novo. Não se aplica
substituir esse recorte host por drivers Linux/postmarketOS/MediaTek/Qualcomm;
as integrações desses projetos e o contrato MediaTek permanecem inalterados.

Origem: fontes locais `portkit/**/*.py` com SPDX MIT e copyright preservado;
`pyproject.toml` e testes do recorte também MIT. O backend de empacotamento já
disponível localmente é setuptools 68.1.2 (MIT), wheel 0.42.0 (MIT); não houve
download, instalação ou cópia dessas dependências para o projeto. As dependências
opcionais libfdt/jsonschema usam as versões já fixadas no ambiente host existente.

Alteração executável limitada a retirar uma constante sem consumidores que
nomeava CLIs K40S dentro do backend e a permitir os novos testes explicitamente
listados no runner/catalogador existentes. A referência às CLIs fica no mapa do
workspace, sem mover código validado. Sete testes puros são realocados, não
reimplementados; a fixture de argv usa paths temporários nativos em vez de
paths POSIX fixos, com as mesmas assertions. Core/SoC/placa e política elétrica
mantêm suas fronteiras.

Limite: o wheel distribui biblioteca, não um workspace autossuficiente nem CLIs
instaláveis. APIs de perfil/composição exigem raiz externa explícita e seu layout
existente. Não há promessa de compatibilidade com outro aparelho. A verificação
do wheel isolado não constitui boot, validação de rádio ou equivalência física.

## WMT: recusa de dispatch após falha terminal — decisão prévia 2026-10-29

Entrega: operação aceita antes da falha de whole-reset não atravessa os
consumidores só porque é HW/SW reset permitido pelo bit RST_ON legado. Reusar
wmt_lib_reset_allows_op e o caminho existente de conclusão/refcount nas duas
threads. Retorno ESHUTDOWN antes do dispatch quando a falha já é observável;
não executar timers de worker nem publicar current-op para operação recusada.
Não implementar drain do scheduler ou esperar uma operação em voo sob mutex.

Runtime PM/genpd Linux 6.18.58 não cancela filas LG. Manter threads, filas,
atomics e sinais existentes é menor adaptação; alternativas MediaTek/postmarketOS/
Qualcomm triadas não oferecem substituto compatível demonstrado, sem necessidade
de RE/novo driver/framework. Fonte LG GPLv2, regressão host MIT. Somente perfil
nativo, nenhuma API/export novo. GPIO_STATE conserva política existente: main
aceita diagnóstico, worker ainda recusa durante RST_ON. Não ampliar allowlist.

Aceite host: consumidores reais processam operação pré-enfileirada sob falha,
sem core/timer/current-op, completam waiter ou devolvem última referência à fila
livre; sem regressão do dispatch normal e reset em curso não falho. Check não é
atômico com execução: falha iniciada depois dele ainda requer quiesce de operação
em voo, e parada das threads ainda não comprova drain das filas remanescentes.

## WMT: posse e falha terminal de whole-reset — decisão prévia 2026-10-29

Entrega: concorrente não limpa WMT_STAT_RST_ON do dono; reset nativo não repete
hardware após erro incerto nem limpa marcadores de falha como se recuperado.
Reusar bit atômico de admissão e fluxo LG, com latch privado de falha nativa e
READ_ONCE/WRITE_ONCE Linux. Nenhum framework/export/driver novo ou RE. Runtime
PM/genpd 6.18.58 não gerencia notificações/filas/reset STP LG; alternativas
MediaTek/postmarketOS/Qualcomm triadas não oferecem equivalente comprovado.
Fontes LG GPLv2 preservadas, teste host MIT.

No perfil nativo, somente owner confirmado finaliza admissão. Sucesso requer
HW, SW e notificação END confirmados. Falha mantém reset bloqueado, não executa
limpeza final dos flags de assert/coredump, desativa STP e recusa novas submissões
act/worker salvo GPIO_STATE diagnóstico. Não promete drenar operações já em voo.
RETRY antes de reset por disputa PSM continua sem latch terminal. Não transformar
abertura/reinicialização parcial em OFF após sw reset falho nem zerar bits STP
antes de confirmar o reset. Legado conserva sua política anterior.

Aceite offline: concorrência/reentrada sem roubar posse, HW/SW/START/END falhos
sem retry/sucesso falso, sucesso único e cleanup, submissões recusadas em falha,
ownership STP preservado antes da operação e estado não-OFF no SW reset falho;
compilação ARM32/MODPOST. Falha terminal não ganha recuperação física automática;
unload, full quiesce, filas em voo e reset direto ainda exigem integração.

Implementado em `wmt-whole-reset-failure-v1.patch`. Snapshot local
`work/wmt-whole-reset-base-20261029-v1/`:
`common_main/core/wmt_lib.c` entrada SHA256
`30c90360dce9e77ebde32ba72386ad50db44474484d9dc3d09f228fd0a35e9ec`,
integrado `d8b10c8b414b860e14d8f6a9ba3342dbdedd717fb72947afc73f96b6610cd445`;
`common_main/core/wmt_core.c` entrada
`c8c667819803137ab5766a0942db2122dc95263ad1e207598fc628c491eb2465`,
integrado `5a7d5ef9cccd5a5456798fc8e68cd88fefd60d22ccb4f8b2b55e6603ecf1571b`.
Tipos dos rótulos de fonte do reset corrigidos para const char, sem mudar texto;
fonte inválida recusa antes de indexar. Nenhum novo export/ABI ou limite elétrico.

Três testes dirigidos sob guarda offline passaram: `test_wmt_whole_reset`,
`test_wmt_stp_power_admission`, `test_wmt_reset_callbacks`. Novo harness executa
whole-reset, HW/SW wrappers, submissões act/worker e opfunc_sw_rst reais com
ASan/UBSan. Fronteiras de fila, operação de hardware, STP/PSM e notificação são
doubles. Cobre reentrada em START/END, owner já presente, falhas START/HW/SW/END/
alocação, ausência de retry, latch já visível no END_FAIL, manutenção de flags
STP antes da operação HW e bloqueio das duas filas com liberação da ref act.
GPIO_STATE continua aceito, RETRY PSM pré-reset não cria latch e sucesso limpa
admissão/final flags. Não testa filas/IRQs/SRCU reais ou operações já em voo.

Build WMT ARM32/MODPOST com KCFLAGS=-Werror, configuração nativa e símbolos
BTIF reais passou. `nativewifi1-20261028-v1/wmt/wmt_drv.ko` SHA256
`92b270cf0494fc9b96710eb753e5c6a8ece42bbb702ae4f345ef0355f4bfd74e`.
Somente lib/core sincronizados após conferir baseline dos destinos. Sem alteração
de imagem/cápsula/firmware ou ensaio físico. Não existe API para limpar o latch
e repetir destrutivamente um reset falho; recuperação explícita ainda é gate.

Limites: não prometer preservação de todos os flags internos STP através da
reinicialização, que mantém efeitos anteriores; este patch impede a limpeza
final indevida e desativa STP ao falhar. Latch recusa novas submissões, mas não
drena fila já aceita nem operação em andamento, e controles diretos podem
contornar as filas. O bloqueio RST_ON não é recuperação física demonstrada.
Coordenação de quiesce/HIF/PALDO/remove e lifetime EMI/coredump seguem pendentes.

## WMT: admissão energia/STP no controle nativo — decisão prévia 2026-10-29

Entrega: power-off não atravessa sessão STP ativa/parcial/incerta, e open/close/
conf não atravessam a chamada nativa de plataforma power/reset. Reusar mutex STP
e mutex de controle de energia existentes; ambos com trylock e sem espera por
callback em reentrada. Ordem: controle de energia, admissão STP, plataforma.
Não adicionar bloqueio global ao longo de operações STP/firmware, nem alterar
sequência elétrica ou limites. On/reset podem operar sessão publicada segundo
o fluxo LG existente; off exige sessão vazia, incluindo flags OPEN/EN/RDY.

Linux 6.18.58 genpd/runtime PM permanece backend de energia; não conhece a
publicação STP. APIs MediaTek/postmarketOS/Qualcomm triadas não fornecem substituto
compatível demonstrado. A adaptação local reaproveita os dois mutexes, sem RE,
novo framework/export ou driver. C LG GPLv2, teste host MIT. Busy/fault antes
da plataforma não altera bits ou ownership; falha de plataforma mantém controles
anteriores. Erro incerto de open impede off, mas reset não ganha nova capacidade
de recuperação ou bypass dos gates inferiores.

Aceite offline: sessão ativa e cada estágio parcial recusam off sem efeitos;
limpeza confirmada permite off; chamadas STP durante plataforma retornam busy;
disputa STP anterior recusa power/reset sem acessar plataforma; erro libera
admissão sem confirmar estado falso. Isso não cobre chamadas diretas à plataforma,
transação inteira de whole-reset, hif-conf, unload/pdev ou todos os leitores TX.

Implementado em `wmt-stp-power-admission-v1.patch`. Snapshot local
`work/wmt-stp-power-admission-base-20261029-v1/common_main/core/wmt_ctrl.c`,
SHA256 de entrada
`9b42079649a79117eb80f93800657cab29f540212be21b541bfb70621df55887`;
integrado
`da21e81bc8c8d7289279aab7e20e2dabef8f0dab41cbfb41a6872e66049f477a`.
Sem novo estado global de recuperação: os dois helpers privados adquirem/liberam
o mutex STP existente e consultam ownership/fault já registrado pelo controle.
Branches legados e corpos elétricos não foram alterados.

Três testes dirigidos sob guarda offline passaram: `test_wmt_stp_power_admission`,
`test_wmt_stp_session`, `test_wmt_power_results`. O novo harness executa controles
power/reset/open/close/conf reais com mutex pthread e ASan/UBSan. Plataforma em
double tenta reentrar nas seis entradas, todas busy sem efeito; disputa prévia
do mutex STP não acessa plataforma e libera mutex power. Testa cada flag/ownership
parcial, fault de open, close falho, cleanup confirmado, erro de plataforma e
EALREADY sem publicação falsa. Não testa escalonador/IRQs/lockdep nem interleavings
arbitrários; o modelo de plataforma não é prova de sequência elétrica.

Build WMT ARM32/MODPOST com KCFLAGS=-Werror, configuração nativa e símbolos
BTIF reais passou. Saída `nativewifi1-20261028-v1/wmt/wmt_drv.ko` SHA256
`6ac15804c58ce3e8cf2dd7a1bd5a25ac6a21789af7b487d73c2834797ea25346`.
Somente wmt_ctrl.c sincronizado após confirmar baseline do destino. Sem novas
imagens/cápsulas, mudanças de firmware ou operações no aparelho.

Limite importante: a admissão dura a chamada de plataforma, não o processo
inteiro de whole-reset que desliga funções antes dela e reinicializa depois.
Chamadas diretas de plataforma, remove/unload, configuração HIF, energia PALDO
e produtores TX ainda requerem coordenação. On/reset com sessão já publicada
mantém a semântica LG existente, não acrescenta comprovação de quiesce/reset.
Não declarar integração funcional dos rádios ou recuperação a partir deste gate.

## BTIF: resultado explícito de rollback de open — decisão prévia 2026-10-29

Entrega: falha de getter de task seguida de close confirmado não prende o
controle STP em fault permanente. A própria ponte confirma esse caso por saída
booleana; preservar errno original e distinguir de close falho/erro de aquisição
inferior. Reusar sequência LG/task refs, API local checked e parâmetro de saída;
sem RE, transporte/framework novo ou export novo. Mainline fornece errno/task
refs, não a aquisição BTIF LG. Alternativas MediaTek/postmarketOS/Qualcomm da
triagem não demonstram substituto compatível. C LG GPLv2, testes MIT.

Manter API antiga como wrapper, saída false por padrão, true apenas no rollback
confirmado do getter. Não usar ID zero como prova de recuperação elétrica: uma
falha anterior de btif_open pode reter dma_fault sem ID. No stub weak nativo,
recusar ENODEV e não inventar implementação presente. Controle usa confirmação
somente em falha BTIF; UART e falha de aquisição inferior permanecem incertas.
Não autoriza retry físico nem limpa faults do backend. Aceite host: getter
NULL/ERR_PTR, close sucesso/falha, busy, ausência, erro original e comportamento
da sessão após resultado limpo/incerto; compilação ARM32/MODPOST com Werror.

Implementado em `wmt-btif-open-result-v1.patch`. Snapshot de entrada
`work/wmt-btif-open-result-base-20261029-v1/`, pins por arquivo:

| Arquivo | SHA256 de entrada | SHA256 integrado |
| --- | --- | --- |
| common_main/linux/stp_btif.c | bb33f1a1bbe805289092559b7ea9b4f4bb33cbcf10ecf755624676e85ab4f683 | dca836e1fdb6aab33a0750d3cd9693c1429fa40e926cbb6ab0538fd81827662e |
| common_main/linux/include/stp_btif.h | 38e9947fd30a9b7fa20b700115248f276acc85e383c1d46cb6b0477f81257a3b | 8e5f949ac9c4d016ed66f044b5a21ba25030869b132469c5832d092a73d53395 |
| common_main/core/stp_core.c | b2f3fe44c097282a452b7ff110e8d23d761d544a396d8ca5b5d9e05c77296892 | 11259efc1d5e7760e3b17746fdf2a8f736cbc73d0757a3d13724e57a09b2b47e |
| common_main/core/include/stp_core.h | cdd009e262c2a2a4fa24e97eee6608f6a44deac51ac3cd5f937ba2041956bbf5 | f8d97e6a31bf3ce66edc33f30d7fee9b8364320ae80f1172cb197682915fc106 |
| common_main/core/wmt_ctrl.c | 58a1e7b0400ee7ee2a0feb4a7c4d380e6165b5c92ecdfc8567ba6a68b6fe117e | 9b42079649a79117eb80f93800657cab29f540212be21b541bfb70621df55887 |

Três testes direcionados sob guarda offline passaram: `test_wmt_btif_open_result`,
`test_wmt_stp_session`, `test_wmt_btif_lifecycle`. Novo harness encadeia ponte,
wrapper core e controle reais, com ASan/UBSan e fronteiras BTIF em doubles.
Verifica getter NULL/ERR_PTR, errno e close positivo/não zero, rollback confirmado
permitindo nova chamada, rollback falho mantendo ID/fault, busy sem sinalização
de limpeza, sucesso pela API legada e UART ainda incerta. Stub weak nativo
compilado/testado separadamente: ENODEV e rolled_back=false, nunca sucesso falso.
Não é teste de falha elétrica, IRQ/RCU real ou de todos os consumidores do ID.

Build WMT ARM32/MODPOST com KCFLAGS=-Werror, AUTOCONF_H nativewifi1 e símbolos
BTIF reais passou. `nativewifi1-20261028-v1/wmt/wmt_drv.ko` SHA256
`474871834f6f50b73f20cf5d44d4f4082a4b8b8bbf294b17230894b27ae4ba4a`.
Cinco fontes/headers sincronizados após conferir baseline dos destinos. Nenhum
novo export, mudança da API antiga ou de firmware/imagem/cápsula. Próxima entrada
após falha limpa volta a consultar backend, não limpa seu dma_fault; a indicação
não é autorização para retry físico. Erros de aquisição inferior e UART ainda
não têm contrato suficiente de rollback, e energia/reset/unload não estão
inteiramente coordenados com a sessão STP. Objetivo funcional continua aberto.

## WMT: ownership por etapa de abertura STP — decisão prévia 2026-10-29

Entrega: rollback remove somente callback/parser/transporte adquiridos pelo
controle nativo, em ordem inversa e parando antes de destruir dependência se
drain falha. Reusar APIs LG STP/BTIF atuais, mutex_trylock e flags privadas no
wmt_ctrl; sem framework, novo transporte, RE ou novos exports. Mainline runtime
PM/genpd e devres não conhecem esta publicação STP em runtime. Alternativas
MediaTek/postmarketOS/Qualcomm triadas não demonstram substituto compatível;
adaptar a sequência LG é menor caminho. C LG GPLv2, regressão host MIT.

Guardar transporte escolhido no início, não reler configuração mutável ao
desfazer. Só registrar ownership após sucesso de cada API. Retorno de open
BTIF/UART falho não garante ausência de efeitos (BTIF pode reter ID quando seu
rollback falha; UART pode expirar após executar): manter erro incerto, sem
retirada de recurso que não sabemos possuir ou reabertura automática. Depois
de transporte adquirido, falha de registro dispara rollback das etapas aceitas;
cleanup falho mantém ownership e recusa open, close explícito pode tentar retirar
o restante pelos contratos existentes. Conservar erro primário e registrar
cleanup distinto. Reentrada/disputa retorna busy sem efeitos.

Configuração STP nativa compartilha admissão com open/close. RDY/EN=0 com sessão
confirmadamente vazia é no-op, para deinit após rollback completo não inventar
erro e reter energia. Estado parcial/incerto não é vazio. Não relaxar enable ou
configuração inválida. Preservar caminho legado e transportes UART/SDIO/BTIF,
sem habilitar nenhum no aparelho. Flush STP VOID e lifecycle global de WMT
continuam fora do alcance dessa prova de ownership.

Implementado em `wmt-stp-session-rollback-v1.patch`, sobre controle nativo com
propagação power/reset e ponte BTIF com admissão do parser. Snapshot local
`work/wmt-stp-session-base-20261029-v1/common_main/core/wmt_ctrl.c` SHA256
`b8b1d4356fac0900c0a4bf8cd43c7a22f100d8f766072e5718cb76456bc6ff6d`;
fonte integrada SHA256
`58a1e7b0400ee7ee2a0feb4a7c4d380e6165b5c92ecdfc8567ba6a68b6fe117e`.
Flags privadas ficam no módulo, sem mudar structs/API externas; branches legados
permanecem. Corpo de configuração anterior virou helper, sem mudar seus checks;
o wrapper nativo adiciona a admissão e o no-op de desativação vazia descrito acima.

Quatro testes direcionados passaram sob guarda offline: `test_wmt_stp_session`,
`test_wmt_btif_lifecycle`, `test_wmt_stp_deinit`, `test_stp_rx_callbacks`.
O novo harness executa helpers/open/close/conf reais com ASan/UBSan, APIs de
fronteira em doubles. Cobre UART/SDIO/BTIF, errno e retornos positivos não zero,
falhas de registro/drain/close, erro primário preservado, callback de outro owner
não retirado, reentrada busy, configuração posterior não troca transporte de
cleanup, reopen após rollback completo, estado parcial e open incerto bloqueados.
Isso não testa IRQ/SRCU reais, interleavings arbitrários, lifetime de unload ou
timeout UART físico. Não é prova de rádio nem de recuperação.

Build WMT ARM32/MODPOST com KCFLAGS=-Werror, AUTOCONF_H nativewifi1 e símbolos
BTIF reais passou. `nativewifi1-20261028-v1/wmt/wmt_drv.ko` SHA256
`4d60caee0b1e5fcecb587fad43c32f58f23c5c65e8c1c80da68855fc0fe48c67`.
Somente wmt_ctrl.c sincronizado após conferir baseline da cópia de build.
Firmware/cápsulas/imagens e fontes LG originais intactos. Não foi iniciado ensaio.

Limites: open do transporte com retorno falho permanece incerto, inclusive erros
que poderiam ter ocorrido antes de efeitos, pois a API atual não distingue isso.
Não afirmar que todos esses erros necessitam recuperação física; falta contrato
explícito para separar falha limpa de rollback incompleto sem adivinhar por errno.
No close parcial, etapas confirmadas não são repetidas; retomada explícita tenta
só ownership restante, sem autorizar retry físico automático. Chamadas a partir
do próprio callback a ser drenado continuam proibidas. Power/reset global e
unload ainda precisam coordenar essa sessão: o mutex STP não serializa sozinho
energia, hif-conf e todos os consumidores WMT. Esse é o próximo gate de integração.

## STP/BTIF: admissão do parser no lifecycle — decisão prévia 2026-10-29

Entrega: parser não usa ID concorrente com open/close, retorna o errno real e
recusa reentrada sem esperar pelo próprio drain. Reusar stp_btif_lifecycle_lock
existente e mutex_trylock Linux; sem transporte/RE/framework novo. O registro
BTIF já usa referências de sessão e callback SRCU na integração atual. Esse
contrato não cobre o acesso cru de g_stp_btif no wrapper WMT. As alternativas
upstream/MediaTek/postmarketOS/Qualcomm já triadas não substituem a ponte LG;
primitivas Linux 6.18.58 são a adaptação menor. Fonte LG/MediaTek GPLv2 preservada,
teste host MIT. Sem novos símbolos exportados ou alterações elétricas.

Open/close/register usarão trylock do mesmo mutex, evitando espera recursiva
quando o callback STP em drain chama caminho de controle. Sem ID, registro não
nulo deve retornar ENODEV; retirada nula permanece idempotente. Registro falho
não muda ID/task e não é reduzido a -2. Busy não tem efeitos. Open mantém seu
rollback/task reference, close mantém recursos em falha. Isso é pré-requisito
do rollback por etapas de wmt_ctrl_stp_open, não sua implementação completa.
Aceite host: sucesso/erro/idempotência, lock durante uso do ID, reentrada e
disputa com registro bloqueado, sem I/O físico; build ARM32/MODPOST com Werror.

Implementado em `wmt-btif-parser-lifecycle-v1.patch`. Snapshot de entrada
`work/wmt-btif-lifecycle-base-20261029-v1/common_main/linux/stp_btif.c` SHA256
`3cd897fbe3890ec7b5943cd37877a7a5744b10880590a4433772cc893b661337`;
fonte integrada SHA256
`bb33f1a1bbe805289092559b7ea9b4f4bb33cbcf10ecf755624676e85ab4f683`.
Mudança na ponte já adaptada a lifecycle/task refs, não no LG 4.9 original.

Três testes dirigidos sob guarda offline passaram: `test_wmt_btif_lifecycle`,
`test_wmt_stp_deinit`, `test_wmt_power_results`. Novo harness usa os três corpos
reais open/close/register, pthread e ASan/UBSan; bloqueia registro no double BTIF
e verifica recusa concorrente, reentrada dos três métodos, errno exato,
idempotência sem ID, rollback do getter e retenção após close falho. Não testa
implementação real SRCU/RCU, IRQs ou concorrência arbitrária. O mutex protege
somente estas três entradas, não todos os leitores crus do ID (TX/PM/debug).
Registro/retirada continuam proibidos dentro do próprio callback RX cujo SRCU
será drenado; trylock não torna auto-synchronize_srcu permitido. Retorno EBUSY
de operação recusada não autoriza retry automático ou liberação por chamador.

Build WMT ARM32/MODPOST com KCFLAGS=-Werror, AUTOCONF_H nativewifi1 e símbolos
BTIF reais passou. `nativewifi1-20261028-v1/wmt/wmt_drv.ko` SHA256
`76a9b5f675e25c2083dbe55e90458cb60cb4710d2d44205ca1081ad32682e227`.
Somente stp_btif.c sincronizado após conferir o baseline da cópia de build.
Nenhuma imagem, cápsula, firmware ou fonte LG original alterada. Rollback por
etapas no wmt_ctrl e lifetime dos outros consumidores do ID continuam pendentes.

## WMT: deinit STP sequencial com confirmação — decisão prévia 2026-10-29

Entrega: falha interna de sw_deinit/PSM/RDY/EN/close/SDIO não pode virar sucesso
e permitir power-off pelo chamador. Reusar os callbacks e APIs LG já presentes,
com retorno imediato na primeira falha nativa. Sem somar errno nem executar
desligamento de recurso dependente após erro de etapa anterior. Manter p_ic_ops
até sw_deinit confirmar; callback ausente em ops não nulo é EOPNOTSUPP, não
sucesso. O deinit SoC deve preservar gp_soc_info quando ps_disable falha.

Alternativas: o teardown de runtime PM/genpd Linux 6.18.58 existente não conhece
o protocolo STP/PSM e não substitui essa sequência. As alternativas MediaTek,
postmarketOS/Qualcomm triadas não provam equivalência desse transporte LG.
Usar callbacks existentes é a adaptação menor; sem RE ou framework novo.
Origem C LG/MediaTek GPLv2, avisos preservados; regressão host MIT. Escopo nativo,
sem novos exports, backend ou mudanças elétricas. Ordem bem-sucedida mantida.

Aceite offline: injetar erro em cada etapa e conferir retorno/nenhum efeito
dependente, retenção de ops/chip-info na falha correspondente, liberação após
sucesso, variantes PSM e transporte, e caller power-off sem desligamento em
falha. Não usar ausência de ponteiro como prova de drain físico. Open parcial,
reentrada, demais callbacks e full-reset continuam exigindo integração própria.

Implementado em `wmt-stp-deinit-errors-v1.patch`, sobre o delta anterior de
propagação power/reset. Snapshot `work/wmt-stp-deinit-base-20261029-v1/`:
entrada `common_main/core/wmt_core.c` SHA256
`f47070a1af4dec6f92d6b6c464cf6dabc474b3bccfe0df7b1882025fcebaf3c8`,
entrada `common_main/core/wmt_ic_soc.c` SHA256
`64264e09f016bfef6dc7a8d7963705d869839c2f38ea484ef81e91a7ff1f20cb`.
Saídas respectivas:
`c8c667819803137ab5766a0942db2122dc95263ad1e207598fc628c491eb2465`,
`4319259f094199a4dc91bd0291fc20a3fe83a966f83afb7bc6868dbaf042850b`.

Três testes direcionados sob guarda offline passaram: `test_wmt_stp_deinit`,
`test_wmt_power_results`, `test_wmt_power_calibration`. O novo harness extrai
deinit SoC/STP e caller power-off reais, com ASan/UBSan; injeta errno e retorno
positivo não zero em cada etapa para UART/BTIF/SDIO. Verifica primeiro erro,
ausência de efeitos dependentes, retenção de ops/chip-info, PSM ligado/desligado,
callback ausente e sucesso. Também conecta o callback SoC real ao deinit STP
e power-off, recusando desligamento quando PSM falha. Testes não abrem transportes
e não representam sincronização real, hardware ou prova completa de drain.

Build WMT ARM32/MODPOST com KCFLAGS=-Werror, AUTOCONF_H nativewifi1 e símbolos
BTIF reais passou. `nativewifi1-20261028-v1/wmt/wmt_drv.ko` SHA256
`1cca1c78dc125bca740aebe1ec365563e46a57d5a10d3418d0da0660425bf825`.
Somente os dois arquivos foram sincronizados com src/wmt após comparar baseline;
nenhuma imagem/cápsula/firmware foi modificada. Caminho legado fica no #else.
Retorno de sw_deinit confirmado libera p_ic_ops antes de RDY/EN/close; falha
posterior não reconstitui esse callback já concluído. Não há promessa de retry
automático nem recuperação a partir de estado parcialmente retirado.

Próximo bloqueio concreto: wmt_ctrl_stp_open pode abrir BTIF/publicar parser e
falhar no callback WMT sem rollback; close não possui ownership por etapa nem
confirma todas as dependências de open parcial. Além disso, full-reset ainda
tem caminhos que desligam funções e repetem operações após erro. Não declarar
o transporte funcional ou seguro para carga a partir apenas deste incremento.

## WMT: confirmação de energia e propagação de reset — decisão prévia 2026-10-29

Entrega: estado lógico não confirma transição falha; reset não perde seu erro
quando STP close sucede. Adaptar os controles LG existentes com mutex_trylock
Linux e retornos já disponíveis, sem novo driver/framework/RE. Genpd/runtime PM
6.18.58 já é usado no backend; não substitui os bits/estados de controle LG.
Alternativas MediaTek/postmarketOS/Qualcomm triadas não demonstram equivalência
para essa máquina de estados. Fontes LG/MediaTek GPLv2, regressão host MIT.

Perfil nativo: serializar on/off/reset no controle sem espera recursiva. On/off
consulta a plataforma inclusive se o bit sugere estado repetido, para não
contornar fault/stopping. Somente 0 ou EALREADY do preflight nativo sem fault
confirma o estado solicitado; erros mantêm o bit anterior. Isso depende do
backend MT6765 já integrado, não é contrato genérico para SoCs/combo legados.
Não criar nova quarentena para busy anterior a efeitos; falhas incertas continuam
retidas pelo backend. Reset propaga errno e não altera esse bit.

No core, power-off só publica OFF após confirmar, sem desligar após drain STP
falho. Power-on nativo propaga falha e não repete ativação após cleanup falho.
Reset preserva erro principal apesar do close e não publica o marcador lógico
OFF para reinicialização antes de confirmar reset. Esse marcador legado não
representa prova de domínio fisicamente desligado após reset off/on.
Aceite offline: sucesso, busy/fault/timeout, repetição sem mascarar fault,
limpeza e prioridade de erros; build ARM32/MODPOST. Não habilita operação física.

Implementado em `wmt-power-result-propagation-v1.patch`. Snapshot local
`work/wmt-power-result-base-20261029-v1/`, entradas SHA256:
`common_main/core/wmt_ctrl.c` =
`56f2101d0ebe289e6648b46c3dd8e0a999551b67a985533f38ebe03087199212`,
`common_main/core/wmt_core.c` =
`c17422bf28c3e1fd74192918450a9e9c53b9e4901a806d2bbcce6ccc9979b74e`.
Saídas respectivas:
`b8b1d4356fac0900c0a4bf8cd43c7a22f100d8f766072e5718cb76456bc6ff6d`,
`f47070a1af4dec6f92d6b6c464cf6dabc474b3bccfe0df7b1882025fcebaf3c8`.

Três testes dirigidos passaram sob guarda offline: `test_wmt_power_results`,
`test_wmt_power_calibration`, `test_wmt_reset_admission`. O novo harness executa
os controles e opfunc_pwr_on/off/hw_rst reais com ASan/UBSan, plataforma/STP em
doubles. Cobre erros, busy/reentrada, estado duplicado com fault, cleanup falho
sem retry, reset+close com erros simultâneos e sucesso. Isso não prova falhas
elétricas, escalonador real ou todos os caminhos de reset. Inspeção do backend
integrado confirma consys_power_preflight verifica stopping/fault antes de
consys_hw_power_check, que verifica domain_dev/fault antes de EALREADY.

Build WMT ARM32/MODPOST com KCFLAGS=-Werror, AUTOCONF_H nativewifi1 e símbolos
BTIF reais passou. `nativewifi1-20261028-v1/wmt/wmt_drv.ko` SHA256
`31a95cb3ff09dce22b9c1fccef095f4c8f933a41dcd90f9320ae20fe4d94dfdb`.
Só ctrl/core foram sincronizados para a cópia de build após conferir baseline.
Firmware, imagens, cápsulas e fontes LG originais preservados. Código novo é
condicionado ao perfil nativo; branches legados existentes não foram substituídos.

Limites encontrados: wmt_core_stp_deinit ainda sobrescreve/soma erros de etapas
anteriores e retira p_ic_ops antes de confirmar sw_deinit; seus chamadores novos
podem impedir power-off somente quando recebem o erro. Não declarar drain
completo com esse retorno. wmt_lib mantém tentativas de whole-reset e rollback
dos estados de cada função ainda exige revisão; nenhuma destas alterações
autoriza recuperação automática ou prova integração do ciclo completo.

## WMT: power-on/off excluídos da calibração — decisão prévia 2026-10-29

Entrega: impedir liga/desliga global enquanto a transação de calibração nativa
STP/EMI está em curso. Reusar o mutex de calibração já existente, trylock e
callbacks síncronos locais, como no reset. A entrada detém consys_power_lock e
não pode esperar pelo dono da calibração: o caminho STP pode pedir reset.
Busy deve retornar antes de STEP/reg/GPIO/JTAG e sem criar fault/quarentena nova.
O corpo elétrico e sua retenção de fault em erro permanecem byte-idênticos.

Alternativas: runtime PM/genpd Linux 6.18.58 já controla o domínio MT6765,
mas não conhece a transação de calibração LG. Usar somente runtime PM ou um
mutex bloqueante não estabelece essa exclusão. Pilhas MediaTek/postmarketOS e
Qualcomm triadas nesta matriz não fornecem substituto compatível demonstrado
para o protocolo de calibração LG/CONNAC. Nenhuma RE ou infraestrutura nova é
necessária. C LG/MediaTek GPLv2 e avisos preservados, regressão host MIT.

Escopo: somente pwr_on/pwr_off nativos, sem novo símbolo exportado ou mudança
de limites elétricos. Helper com lock condicionado a CFG_CALIBRATION_BACKUP_RESTORE,
mesmo gate da calibração/reset atual. Não cobre PALDO em volta da calibração,
coredump, mmap, retirada do pdev ou todas as APIs WMT. Não habilita rádio/carga.
Aceite offline: busy sem efeitos, retorno exato, liberação após falha/sucesso,
exclusão nos dois sentidos e ausência de regressão nas sequências existentes;
build ARM32/MODPOST com símbolos reais, sem acesso ao aparelho.

Resultado offline: `wmt-power-calibration-admission-v1.patch` acrescenta helper
síncrono privado ao módulo e o usa nas duas entradas nativas; sem EXPORT_SYMBOL.
Snapshot `work/wmt-power-calibration-base-20261029-v1/`, SHA256 de entrada:
`common_main/core/wmt_ic_soc.c` =
`5941a1f99db283d005c46de72c6e781faac1bcf83d6995585d99eb08feac9c02`,
`common_main/core/include/wmt_ic.h` =
`805f2e0860d52755dad27e845a93e3c72b93897a1b5b940fd833e64517dc39b4`,
`common_main/platform/mtk_wcn_consys_hw.c` =
`8657e410e576d21f07cd135424298460eadc0b504e6b60b569651ebf5a4a3926`.
Saídas respectivas:
`64264e09f016bfef6dc7a8d7963705d869839c2f38ea484ef81e91a7ff1f20cb`,
`d899146c84112981d1cd7b4406acc3d672a895bc8b59966522c7e725f5ce7761`,
`6fbc7b88414e17e399042894b43c31d5e61fc34f965d42654af2bc96a82733dc`.

Quatro testes direcionados passaram sob guarda offline:
`test_wmt_power_calibration`, `test_wmt_reset_admission`,
`test_wmt_calibration_reset`, `test_wmt_calibration_stp`. O novo teste exercita
os corpos reais de power/preflight/calibration-admission, com pthread mutex e
ASan/UBSan; native com backup ligado/desligado e branch legado dos wrappers.
Não é teste do escalonador/lockdep ou de concorrência arbitrária. Verifica busy
sem STEP/reg/GPIO/JTAG, exclusão da calibração enquanto power detém o lock,
retornos/fault/rejeição posterior e liberação em erro; sequências elétricas
e corpos de reset/calibração existentes permanecem iguais por comparação.

Build WMT ARM32/MODPOST com KCFLAGS=-Werror, AUTOCONF_H nativewifi1 e símbolos
BTIF reais passou. `nativewifi1-20261028-v1/wmt/wmt_drv.ko` SHA256
`e071a2302a669027f438df4fc3330095e0e419e33d5c4126247f31acdea99294`.
Só os três arquivos de `nativewifi1/src/wmt` foram sincronizados, após conferir
igualdade dos destinos com o snapshot. Imagens/cápsulas/firmware preservados.

Auditoria de chamadores identificou pendência concreta anterior a este delta:
`wmt_ctrl_hw_pwr_on/off` altera WMT_STAT_PWR antes de confirmar a plataforma;
`wmt_ctrl_hw_rst` descarta o retorno, e `opfunc_pwr_off` publica POWER_OFF mesmo
com erro. Esta etapa protege somente a transação de baixo nível, não corrige
esse estado lógico nem libera carga física. Próximo incremento deve preservar
erro e evitar sucesso lógico falso sem converter estado incerto em retry seguro.

## BT: parser e commit de reset concorrente — decisão prévia 2026-10-29

Entrega: rejeitar payload reset inválido antes de memcpy; impedir que read
antigo avance cursor ou marque entregue um novo reset que chegou durante
copy_to_user. Reusar spin_lock_irqsave, snapshots e geração privados da sessão
LG; não segurar spinlock em copy_to_user/STP/wakeup/log, nem substituir STP por
framework paralelo. Mainline oferece primitivas e contrato read/EIO, não o
protocolo de reset LG; MediaTek/postmarketOS/Qualcomm não justificam RE/driver
novo para esse estado. C/delta GPL-2.0, regressão Python MIT.

Estado/cursor/geração serão alterados juntos sob spinlock; reader usa cursor
local e só faz commit depois da cópia e se geração/estado ainda iguais. Cópia
invalidada retorna EIO sem bytecount falso; não promete continuar framing após
esse erro fatal de transporte. Mensagem END duplicada não reinicia cursor de
Hardware Error parcial. Novo START invalida operações antigas. TX usa checagem
central sem lock durante STP; bloqueio físico durante reset continua pertencendo
ao STP/WMT (WMT bloqueia STP antes da notificação START), não ao spinlock BT.
Poll conserva máscara/ABI e usa snapshot de estado, sem anunciar novo modelo de
reconexão. Open/cleanup limpam estado antes de publicar/depois de drenar.

Aceite offline: NULL/short/long/origem/tipo/enum inválidos sem efeito, eventos
normais e duplicados, reset inserido durante cópia sem sobrescrever estado novo,
EFAULT sem avanço de cursor, retry/fragmentação/sinal, lock fora de chamadas
dormíveis. Build ARM32 com Werror. Não validar IRQ/lockdep/RF a partir de doubles.

Implementado em `patches/kernel/staging/bt-reset-state-v1.patch`, depois do delta
de sessão. Baseline local `work/bt-reset-state-base-20261029-v1/stp_chrdev_bt.c`
SHA256 `10c9251cf7e5855c3fc1ebfbdff3dd36a87e535ef868053dd343c222b5e04e98`.
Fonte LG/MediaTek com aviso GPLv2 preservado; MODULE_LICENSE Dual BSD/GPL legado
não foi reinterpretado como licença dos arquivos. Reuso: primitivas spinlock,
waitqueue, VFS e compilação do Linux local 6.18.58, sem novo driver/transporte.
Fonte integrada SHA256
`6664f1a9516d051515d384f53b19cf06b196482aa297a7a172061093a6eea2be`.

Verificação: cinco testes dirigidos sob guarda offline passaram:
`test_bt_reset_state`, `test_bt_callback_session`, `test_bt_read_interruptible`,
`test_stp_rx_callbacks`, `test_wmt_reset_callbacks`. O novo harness executa os
helpers/callback/read/write/poll reais com ASan/UBSan e injeta reset nas fronteiras
de cópia/STP. Verifica ausência de spinlock durante cópia, STP, wake e espera;
não modela IRQs nem interleavings arbitrários. Não altera testes/pins históricos.
Init/exit, ownership, rollback/power/quarentena de open/close preservados, salvo
substituir a limpeza do estado pelo helper protegido e com geração.

Build ARM32/MODPOST com `KCFLAGS=-Werror` passou no perfil nativewifi1 e símbolos
reais WMT, usando a mesma linha da etapa de sessão abaixo. `bt_drv.ko` SHA256
`9c730fe4eaa6bcebf6d54c1f017667d70c755b2ea6c4a6a479e8f768e0980c12`,
vermagic `6.18.58-k40s-nativewifi1-NOT-FOR-FLASH`, depends `wmt_drv`.
Só a cópia `nativewifi1/src/bt/stp_chrdev_bt.c` foi sincronizada após conferir
igualdade com o baseline. Cápsula antiga, firmware e imagens não foram alterados.
Próximos gates compartilhados: EMI/coredump, energia/reset e lifetime, falha de
flush STP VOID; nenhum resultado autoriza ativação física ou atesta rádio.

## BT: registro transacional e sessão em quarentena — decisão prévia 2026-10-29

Entrega: cliente BT usa 0/errno do STP RX e booleano1/0 do reset WMT sem
confundi-los; inicializa estado/semaphores antes de publicar, desfaz somente
callbacks aceitas e não libera sessão/power-off se retirada não confirmou drain.
Reusar APIs já portadas STP/WMT, atomic_cmpxchg e module_get/put Linux; sem
framework/session manager, novo transporte ou RE. Mainline fornece lifetime
de módulo, não handshake STP/BTIF; triagem MediaTek/postmarketOS/Qualcomm existente
não demonstra substituto para essa pilha. C LG GPL-2.0, regressão Python MIT.

Lease de módulo adquirida antes do primeiro efeito e mantida com busy em erro
incerto. Adicionar BT_fops.owner explicitamente (antes ausente): VFS mantém
essa referência durante open/release, então liberar lease nesses métodos após
cleanup não deixa método executando sem referência. Se open falhar
com callback ainda publicada, lease impede unload mesmo sem FD entregue.
Quarentena não é recuperação aprovada: requer reset/reboot autorizado, sem retry
automático ou tentativa de contornar o bloqueio. Depende do par STP RX SRCU e
reset WMT SRCU nativewifi1, não apenas de mesmo vermagic em módulo antigo.

Baseline stp_chrdev_bt.c após leitura interrompível SHA256
38349926f575a55f07f2afbbd9816e974def35f1298899d0ac1ea39c2bec13b2,
snapshot work/bt-callback-session-base-20261029-v1/stp_chrdev_bt.c, fonte/build
iguais. Aceite offline: falhas em registro/drain/off, ordem de rollback, callbacks
imediatas com estado inicializado, exclusividade, busy/ref retidos sob falha,
nenhum unreg de registro rejeitado e nenhum reopen após cleanup incerto.
Não altera função-on/off física nem presume ownership global de outros clientes
legados; coordenação WMT/energia/coredump continua gate de ativação.

Resultado: bt-callback-session-v1.patch integrado à fonte e cópia src/bt do
nativewifi1. Registros são marcados owned só após aceitação; cleanup tenta
retirar ambos os owned, preserva primeiro erro e não remove callback rejeitada.
Não faz function-off nem libera busy/lease com drain incompleto. Function-on
falho ou function-off incerto mantém quarentena; nenhum retry automático.
State/semaphores são preparados antes de registros, e nenhuma inicialização
posterior apaga reset/wakeup entregue sincronicamente pela API. Release limpa
estado somente após drains/off confirmados e libera a lease antes de busy.

Seis testes passaram sob offline_guard, sem skips: sessão nova, SRCU RX STP,
SRCU reset WMT, leitura BT e init/exclusive históricos. Novo teste aplica delta
ao input pinado, compila helpers/open/close reais com ASan/UBSan e injeta falhas
de module_get, function-on/ready, registros0/errno versus booleano, unregister
individual/duplo e off. Callbacks imediatas encontram semaphores/estado prontos;
cleanup bem-sucedido permite reopen; falha mantém busy e referência, inclusive
callback ainda chamável após open/close falho. Modelo resetado entre casos
representa boot novo, não recuperação implementada ou retry de quarentena.
Leitura/init/exit byte-idênticos ao baseline após esse delta, owner de fops
conferido. Não prova sinais/RCU físicos ou todos os clientes legacy.

Build BT ARM32/MODPOST aprovado com KCFLAGS=-Werror, WMT_STAGE/symvers atuais
e o comando nativewifi1/bt já documentado abaixo. bt_drv.ko SHA256
628c26109eca39fcb89710a26ceb9002b23d4735ac73a311c65f243bb4edad70,
vermagic `6.18.58-k40s-nativewifi1-NOT-FOR-FLASH SMP mod_unload ARMv7 p2v8`,
depends wmt_drv. Requer par com os patches WMT reset SRCU e STP RX SRCU; mesmo
release em módulo antigo sozinho não comprova esses contratos. Fonte/cópia
conferidas iguais; cápsula BTv14/driver antigo não substituídos. Estado de reset
e seu parser no BT, falhas de flush VOID STP e coordenação WMT/energia/coredump
continuam pendentes. Orientação atual do usuário: continuar offline, sem ensaio
no aparelho por enquanto. Nenhuma carga de módulo, firmware, RF ou telefone.

## STP nativo: drain RX de callback — decisão prévia 2026-10-29

Entrega: retirar callback RX antes de fechar BT sem leitor ainda executando
código do módulo. Reusar SRCU/mutex/RCU já usados no WMT, sem novo framework.
srcu.h 6.18.58 local exige lock/unlock no mesmo contexto e proíbe esperar grace
period direta/indiretamente no reader. Callback RX pode vir do contexto STP
atômico: não adicionar mutex ou sleep ao dispatcher; preservar contexto da
callback. API de registro/retirada é processo, não reentrante pelo callback.
BT_event_cb e wmt_dev_rx_event_cb inspecionados não registram/retiram a si mesmos.
Mainline já oferece as primitivas; MediaTek/postmarketOS/Qualcomm não substituem
esse protocolo STP. Sem driver novo ou RE. C GPL-2.0, regressão Python MIT.

Contrato 0/errno do STP, não booleano WMT. Native valida type>=0 e <MAX; dono
duplicado idêntico é idempotente, outro callback/reg durante drain retorna
EBUSY. Reg NULL retira publicação, solta API mutex, espera SRCU, faz flush legado
e só então encerra drain. Registro vazio faz flush antes de publicar e rechecagem
de fila após publicação acorda o callback atual caso dados tenham chegado nessa
janela; não invocar ponteiro cru. Fluxo TX callback/interface não é abrangido.
Flush legado é VOID e pode registrar falha de lock internamente; este incremento
não inventa sucesso verificável da limpeza nem resolve esse contrato de erro.

Baseline stp_exp.c SHA256
8d934a9b0687a64553b42a235f7ca5f7867cc8336a45813f517f80d0586cb88f,
snapshot work/stp-rx-callback-base-20261029-v1/common_main/core/stp_exp.c,
fontes/build conferidas iguais. Aceite: índices extremos, payload/control status,
drain concorrente, reg durante drain, flush depois do último reader e wakeup de
dados já pendentes; build ARM sem relaxar checagens. Retornos/rollback BT ainda
precisam ser integrados antes de declarar fechamento de sessão seguro no aparelho.

Resultado: stp-rx-event-srcu-v1.patch aplicado à fonte e cópia nativewifi1.
Dispatcher RX nativo lê uma única callback sob SRCU; consulta de atividade usa
rcu_access_pointer, sem invocar ponteiro desprotegido. TX/event/interface não
foi migrado e não herda automaticamente essa garantia. Reg/unreg só processo,
nunca do próprio reader ou segurando lock de ring/STP que o reader possa usar.
Flush de registro vazio ocorre sob API mutex com callback não publicado;
drain/flush de retirada ocorrem sem API mutex, e nova publicação fica bloqueada.

Cinco testes passaram com offline_guard, sem skips: RX STP novo, reset WMT,
leitura BT e os dois testes históricos init/exclusive BT. Novo teste aplica
delta ao input pinado e usa funções reais do dispatcher/status/API com o modelo
SRCU de dois epochs já existente e pthreads/ASan/UBSan. Callback em andamento
fica parado, unreg publica NULL e não faz flush antes de terminar; novas
chamadas não usam callback antigo. Reg concorrente/segundo unreg recusa EBUSY,
callback novo não sobrescreve owner, idempotência não descarta dados, bounds
negativo/MAX/255 são seguros, dados injetados na janela flush/publicação
recebem wake inicial, referências/epochs ficam drenados. Não é execução IRQ,
SRCU kernel real ou prova de flush sob falha (API VOID permanece limitada).

Build WMT ARM32/MODPOST aprovado com o mesmo comando nativewifi1/AUTOCONF_H
explícito anterior, sem novo export/protótipo ou supressões. wmt_drv.ko SHA256
136c396734350a29fe9dff90d34e93ee10745c9ad152281cae6f5891aa2dc188,
vermagic `6.18.58-k40s-nativewifi1-NOT-FOR-FLASH SMP mod_unload ARMv7 p2v8`.
stp_exp.c integrado SHA256
55888df83a928df24c4c7b8fd745ac604883ab5ce154114d1be88affe0b05f9d;
fonte/build conferidos iguais. Pins históricos que exigem 8d934a9b... não foram
alterados para aceitar essa revisão. Próxima etapa: tratar registro/rollback
e close no cliente BT com os contratos booleano WMT e errno STP distintos.
Sem empacotar/carregar módulos, mudar cápsula BTv14/kernel, RF ou telefone.

## WMT nativo: drain de callbacks de reset — decisão prévia 2026-10-29

Entrega: unreg BT/Wi-Fi de reset retira publicação e espera leitores anteriores,
sem segurar mutex da API durante callback ou synchronize_srcu. Reusar Linux
SRCU/mutex/rcu_assign_pointer já usados no WMT WLAN/logging, não criar registry
framework, protocolo ou cópia de driver. Mainline fornece lifetime sleepable;
postmarketOS/Qualcomm não substituem essa API LG. Sem RE ou código externo.
Delta C mantém GPL-2.0 do wmt_lib.c; regressão Python MIT reaproveita o modelo
SRCU de dois epochs existente (não alegar execução do SRCU kernel no host).

Escopo WMT_K40S_NATIVE_PROFILE: tabela privada não é apagada pelo sync_init da
biblioteca. Reg/unreg mantêm booleano1/0, reg NULL equivale a unreg; duplicata
idêntica é idempotente, callback diferente não sobrescreve owner, reg durante
drain recusa. Todos os leitores nativos passam por SRCU em wmt_cdev_rstmsg_snd;
init/raw rFdrvCb legado não é usado nesse perfil. Caminho não nativo preservado.
Unreg não pode ser chamado pelo próprio callback/dentro do domínio SRCU: BT
bt_cdev_rst_cb e Wi-Fi glResetCallback inspecionados não fazem isso (Wi-Fi apenas
enfileira trabalho). Isso é contrato, não detecção runtime de qualquer cliente
legado. Não afirmar suporte a callbacks arbitrários/FM/GPS não auditados.

Aceite: concorrência com callback dormindo, publicação NULL antes do drain,
nenhuma chamada nova ao callback removido, reg durante drain recusado, unreg
retorna só após callback e permite novo owner depois; invalid/NULL/idempotência
e payload/ordem de reset preservados. Build ARM32 real sem mudar ABI externa.
Registro ignorado pelo BT e drain RX STP continuam gates separados.

Entrada wmt_lib.c SHA256 b435b48b3a47be665ff9850f9828d400b8dcf764d1b73c6c4cd3d47c0aa898de,
snapshot work/wmt-reset-callback-base-20261029-v1/common_main/core/wmt_lib.c,
fontes/build iguais antes da edição. Resultado wmt-reset-callback-srcu-v1.patch
aplicado à fonte e cópia nativewifi1. Lista de nomes de log foi tipada const char
para não converter literais em UINT8*: primeiro build do host recusou pointer-
sign; corrigido o tipo, sem suprimir warning ou alterar mensagens/ordem.

Cinco testes passaram sob offline_guard, sem skips: registry reset novo, WLAN
SRCU histórico, leitura BT, init/exit e exclusividade BT históricos. Regressão
nova usa funções reais/região de estado e o modelo SRCU existente com pthreads/
ASan/UBSan: callback fica parado, unreg publica NULL, API mutex fica livre,
novos dispatches não entram no callback antigo, segunda retirada/reg durante
drain recusam, callback termina antes de unreg retornar e novo owner entra só
depois. Cobre payload/START/END/FAIL, bounds, idempotência e reg NULL. Modelo
não prova SRCU/lockdep reais, todos os clientes ou auto-unreg proibido.

Build WMT ARM32/MODPOST passou com o comando nativewifi1/AUTOCONF_H explícito
já registrado; sem novo export/header público ou mudança de ABI. wmt_drv.ko
SHA256 637c9a33a7bfa83f25667fe82430f31dbfb885e2b5abbc968d43c704eff91d39,
vermagic `6.18.58-k40s-nativewifi1-NOT-FOR-FLASH SMP mod_unload ARMv7 p2v8`.
Fonte integrada wmt_lib.c SHA256
30c90360dce9e77ebde32ba72386ad50db44474484d9dc3d09f228fd0a35e9ec.
Pins de regressões históricas anteriores continuam intactos; seleção nova não
alega que a árvore modificada passa nos pins 8c7c26b5... dessas regressões.
Próximo incremento é drain STP RX e registro/rollback no BT antes de encerrar
o gate de callbacks. Sem alteração da cápsula BTv14, carga/boot/RF ou telefone.

## Bluetooth: leitura interrompível para recuperação — decisão prévia 2026-10-29

Entrega: processo dono do transporte BT pode sair de leitura bloqueada ao receber
sinal, inclusive aguardando reset, sem perder o semaphore nem inventar EOF.
Reusar down_interruptible/wait_event_interruptible, READ_ONCE/WRITE_ONCE e
contrato read Linux; manter STP, limites de buffer e Hardware Error HCI existentes.
Mainline fornece as primitivas; Bluetooth serdev/HCI não substitui por analogia
o transporte LG STP/BTIF já portado. Triagem MediaTek/postmarketOS/Qualcomm
anterior não demonstra driver substituto para esse protocolo integrado. Sem RE,
driver paralelo ou ferramenta nova. Fonte LG/MediaTek GPL-2.0 stp_chrdev_bt.c,
snapshot original pinado 3b564b34462a227add99a67ea4c9d5b9638a939686798238c1b6f2cbca8de4ec
em work/bt-read-interrupt-base-20261029-v1; Makefile glue MIT, teste Python MIT.

Aceite offline: zero-length sem bloquear, sinal na aquisição ou duas esperas
retorna ERESTARTSYS liberando somente lock adquirido; nonblocking/data/erro STP
e entrega parcial do Hardware Error preservados. Wake sem dados não vira EIO
espúrio; reset ocorrido durante espera normal entra no caminho de reset.
Init/exit/open/close devem permanecer byte-idênticos e seus testes passam sobre
o snapshot original com pins intactos. Novo teste aplica delta e compara esses
quatro corpos. Callback WMT/STP lifetime e reset global continuam gates, não
declarados resolvidos pela leitura interrompível.

Compilar BT em cópia limpa e MO separado nativewifi1, WMT_STAGE/symvers da mesma
release; não substituir bt_drv.ko antigo nem reempacotar a cápsula BTv14. Nenhum
acesso ao telefone, carga de módulo, firmware, rádio ou autorização física.

Resultado: bt-read-interruptible-v1.patch altera somente BT_read e metadado
MODULE_DESCRIPTION. Esperas/semaphore retornam ERESTARTSYS sob sinal; count0
não adquire lock. Wake sem dados repete receive, não inventa EOF/EIO; reset
durante espera passa ao ramo de reset. Evento HCI só avança definitivamente
após copy_to_user: falha restaura rd_offset, inclusive entrega parcial, evitando
perda de bytes do Hardware Error. Init/exit/open/close comparados byte a byte
entre snapshot e fonte com delta, inalterados. Seus dois testes usam agora o
snapshot pinado original (mesmos pins/casos), não ignoram drift silenciosamente.

Três testes passaram sob offline_guard, sem skips: test_bt_read_interruptible,
test_bt_legacy_api e test_bt_legacy_exclusive. Funções reais BT_read e helper HCI
compiladas com ASan/UBSan: zero-length, sinal na aquisição, espera normal/reset,
nonblocking sem dados/reset, data/clamp, erro STP, wake espúrio, reset chegando
durante read, evento fragmentado e EFAULT no primeiro/últimos bytes com retry.
Modelos não provam entrega de sinal/kernel STP real nem callbacks concorrentes.

Nova cópia limpa src/bt contém somente Makefile/bt.h/stp_chrdev_bt.c; saída
nativewifi1/bt separada da staging e da cápsula antiga. Build ARM32/MODPOST
aprovado contra WMT atual, depende de wmt_drv, vermagic
`6.18.58-k40s-nativewifi1-NOT-FOR-FLASH SMP mod_unload ARMv7 p2v8`.
bt/bt_drv.ko SHA256 a6c3ec5fd4944c67dcf8434367dfa81f0412ad5aea29b5436574dfbaaac51863.
Primeiro build avisou MODULE_DESCRIPTION ausente; adicionado metadado, rebuild
final sem esse warning, sem relaxar checagem. Comando:

```sh
runtime="${KPF_RUNTIME_ROOT:?Selecione explicitamente o runtime local}"
make -C "$runtime/kernel-workspaces/lts-6.18.58-native-connsys-v1/linux-6.18.58" \
  O="$runtime/kernel-workspaces/lts-6.18.58-native-connsys-v1/build-wifi-20261028-v1" \
  M="$runtime/module-workspaces/nativewifi1-20261028-v1/src/bt" \
  MO="$runtime/module-workspaces/nativewifi1-20261028-v1/bt" \
  ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- \
  WMT_STAGE="$runtime/module-workspaces/nativewifi1-20261028-v1/src/wmt" \
  KBUILD_EXTRA_SYMBOLS="$runtime/module-workspaces/nativewifi1-20261028-v1/wmt/Module.symvers" \
  KCFLAGS=-Werror -j4 modules
```

Fonte/cópia conferidas iguais. bt_drv.ko da staging antiga e cápsula BTv14
não foram substituídos, imagem/firmware/policy preservados. Próximo bloqueio BT:
open ignora retornos de registro STP/WMT, e unreg ainda precisa demonstrar drain
de callbacks antes de close/unload. Coredump/energia/lifetime compartilhados WMT
continuam gates; não abrir stpbt ou promover este build como Bluetooth funcional.

## CAC/radar: snapshot e estado cfg80211 — decisão prévia 2026-10-29

Entrega: estender o wiphy_work já integrado a CAC/radar, sem nova fila/timer ou
API elétrica. Linux6.18.58 mlme.c copia chandef para cac_done/radar_chandef e
retém chan; usar o canal canônico no worker evita ponteiro LG liberado. Estado
cac_started deve ser encerrado via cfg80211_cac_event ABORTED/FINISHED, não
escrever diretamente no wdev de outro contexto. FINISHED requer CAC ativo e
prazo do kernel alcançado; não reduzir duração nem marcar DFS disponível cedo.
Reusar Linux wiphy_work/cfg80211/tempo, netif_carrier_off/stop_all_queues e cópia
delimitada existente. Mainline já fornece as APIs; pmaports/Qualcomm não mudam
esse contrato nem justificam driver/RE novo. Delta mantém LG dual GPLv2/BSD;
regressão Python MIT. Sem alterar firmware, regras regulatórias ou RF.

Radar deve parar filas/carrier antes de alocar/enfileirar. Erro de fila mantém
o chandef LG para diagnóstico/recuperação, não retoma TX nem relata sucesso.
Sucesso de fila permite liberar clone LG pois o evento não o retém. CAC
prematuro/obsoleto é descartado com warning e cleanup, não promovido a sucesso.
Recuperação do FSM em perdas de fila/novas sessões continua gate separado.

Entrada gl_p2p_kal.c integrada após wiphy_work SHA256
9d94a97b66fc4201f48c8fc86c8b34727fae8241f3d8ea6c055b21ed0a575970,
snapshot work/gen4m-dfs-cac-base-20261029-v1/os/linux/gl_p2p_kal.c, fonte/build
conferidas iguais. Resultado: gen4m-dfs-cac-radar-work-v1.patch reutiliza o mesmo
evento/fila com tipo switch/CAC/radar. No worker, CAC exige started salvo/atual,
mesmos start_time/duração e deadline alcançado. Radar em CAC ativo emite ABORTED
antes de radar_event; não escreve cac_started fora do cfg80211. Canal canônico
também vale para cópias retidas em cac_done_chandef/radar_chandef do core.

Regressão de fila existente ampliada, sem novo modelo paralelo: aplica patches
wiphy_work e CAC em ordem, verificando hash intermediário. Três testes passaram
com offline_guard, sem skips (fila/snapshot ampliado, alocação chandef e radar/CAC
histórico). ASan/UBSan com funções reais cobre FINISHED no deadline, prematuro,
start/duração alterados, started falso, radar abortando CAC e deixando link1
intacto, stop de filas anterior à alocação, clone liberado antes do worker,
ENOMEM preservando clone e TX parado, radar seguido de FINISHED sem promover
disponibilidade, argumentos/índices inválidos. Doubles não executam regulação,
timer/wiphy real nem RF; igualdade de tempos não é identidade completa de sessão.

Build gen4m ARM32/MODPOST passou com o mesmo comando CONNAC/6765 já documentado
abaixo, sem alteração de flags/símbolos/proteções. wlan_drv_gen4m.ko SHA256
736e41684bb40bd0a3e0098d4a3e308106f208fb7dc51539a28af2bc918420d7,
vermagic `6.18.58-k40s-nativewifi1-NOT-FOR-FLASH SMP mod_unload ARMv7 p2v8`.
Pendências: identidade/serialização de sessão CAC no FSM, recuperação de perdas
de fila/notificação e auditoria dos demais produtores/teardown. Nada disso foi
declarado resolvido por queue success; nenhum firmware/RF/boot/telefone acessado,
kernel/WMT/cápsula BTv14 preservados. Catálogo só atualiza hashes da regressão.

## DFS: notificação em wiphy_work — decisão prévia 2026-10-29

Entrega: retirar cfg80211_reg_can_beacon_relax/ch_switch_notify do thread WLAN
sem mutex wiphy, evitando bloqueá-lo em wiphy_lock enquanto cfg80211 aguarda
kalIoctl. Reusar wiphy_work_init/queue do Linux 6.18.58 local (cfg80211.h/core.c,
GPL-2.0), não criar workqueue privada ou notifier paralelo. Worker executa sob
wiphy.mtx; wiphy_unregister drena a lista antes de liberar a estrutura. AP/GO
ch_switch_notify copia chandef mas retém seu ponteiro chan (nl80211.c); usar o
canal canônico obtido de ieee80211_get_channel dentro do worker, não clone LG.
Mainline já fornece a API; pmaports/Qualcomm não substituem esse contrato nem
justificam backend próprio. Sem RE ou driver novo. LG dual GPLv2/BSD, delta
conserva licença; regressão Python MIT.

Evento possui cópia de chandef sem ponteiro emprestado, frequência e iftype;
dev_hold/put preserva netdev enquanto pendente. Worker descarta evento se wiphy
ou netdev não registrado, wdev ausente/estrangeiro ou iftype mudou, antes de
notificar. Sem guardar glue/role/chandef LG para depois. Fontes locais mostram
wlanRemove parando threads antes de p2pNetUnregister e wiphy_unregister; produtores
FSM da troca de canal são esses threads. Não alegar que isso audita todos os
outros caminhos de teardown/reset/role nem CAC/radar. Fila rejeita halted.

Snapshot work/gen4m-dfs-notify-base-20261029-v1, fontes/build iguais:
mgmt/p2p_func.c c12b3dc0e8e12d1589f95a92fe3402616a61ada2c264ad68c8e13b00d6f5b58b;
gl_p2p_kal.c e0dc971d49338b68830b31828f043d96ae4f4639dc8e61ff9edc69d7da44ca05;
gl_p2p_kal.h b1015431582afa23a39d4e3b9babaa310087641a5eb10b9d924d6e2e5b183333.
Aceite offline: fila não chama cfg80211 inline, snapshot sobrevive à liberação
do chandef original, worker exige contexto wiphy e canal canônico, erros e
discard liberam evento/ref, build ARM/MODPOST sem supressões. Sem RF/telefone.

Resultado: `gen4m-dfs-wiphy-work-v1.patch` aplicado às três fontes de trabalho e
cópias de build. Callback verifica registro antes de ler wdev, usa iftype salvo,
canal canônico e cfg80211_chandef_valid; warning regulatório original preservado
sem alterar a regra de permissões. Return0 da API nova significa enfileirado,
não notificação já completada. Caller registra falha de fila; recuperação dessa
falha e notificações CAC/radar ainda são gates explícitos, sem nova autorização.

Três testes passaram com offline_guard, sem skips: test_gen4m_dfs_notify,
test_gen4m_dfs_chandef e test_gen4m_p2p_cac. Novo teste aplica delta aos inputs
pinados e executa os helpers reais sob ASan/UBSan: nada é notificado inline;
libera clone de canal antes de executar worker; callback sob contexto wiphy
simulado retém no core somente ponteiro canônico. AP/GO, dois eventos pendentes,
ENOMEM/halted/argumentos inválidos, netdev/wiphy retirados (wdev deliberadamente
inválido), wdev ausente/estrangeiro, iftype alterado, canal ausente e chandef
inválido conferem cleanup/ref balanceado. Não roda scheduler/locks cfg80211 reais.

Build completo gen4m ARM32 e MODPOST aprovado com o comando CONNAC/6765,
MTK_ANDROID_WMT=y, MET no e ambos Module.symvers WMT/adaptor documentados abaixo,
sem mudanças de flags/Werror. API/símbolos wiphy_work reais linkaram. Módulo
wlan_drv_gen4m.ko SHA256
9c63afb895607eb54eb0dfb1cb9926df3a0e6ec9310400a793c23e27cbce6fdf,
vermagic `6.18.58-k40s-nativewifi1-NOT-FOR-FLASH SMP mod_unload ARMv7 p2v8`.
Gate de shutdown assumido é o normal observado: parar produtores FSM/threads
antes de unregister que drena wiphy_work; auditar demais falhas/teardown/role
antes da ativação. Não há referência diferida a glue/role do driver, mas isso
não demonstra automaticamente lifetime correto em todo o driver legado.
Sem mudança de kernel/WMT/cápsula BTv14, RF, boot ou acesso ao aparelho.

## DFS gen4m: construção de chandef sob falha — decisão prévia 2026-10-29

Subpasso do gate P2P/DFS: corrigir NULL dereference/leak/publicação parcial em
p2pFuncDfsSwitchCh, preservando o gate de wiphy.mtx/lifetime de channel. Não
adicionar wiphy_lock bloqueante no thread WLAN que atende kalIoctl síncrono.
Reusar cnmMemAlloc/Free, kalMemZero, ieee80211_get_channel e construção LG
existentes; mainline cfg80211/wiphy_work já inspecionado é candidato à fase de
notificação, não substituto direto do lifetime dos objetos LG. Não importar
driver postmarketOS/Qualcomm nem parser/RE para corrigir alocação desta fonte.

Origem integrada LG dual GPLv2/BSD mgmt/p2p_func.c SHA256
41518bb5f528476072a852ef55a4fd06ff67a78db884d93ec78d8bf817dd5f48,
snapshot work/gen4m-dfs-chandef-base-20261029-v1/mgmt/p2p_func.c, sem commit
upstream inventado. Cópia de build conferida igual. Delta conserva licença;
regressão própria Python MIT. Aceite offline: ambas alocações/lookup falhos não
publicam objeto parcial nem vazam, canais válidos preservam width/centros e
cleanup, ponteiros/índices de roles inválidos não são dereferenciados. Compile
ARM32 mantendo Werror. Não afirma resolver notificação/DFS/regulação/RF reais.

Tentativas de build iniciais omitiram MTK_COMBO_CHIP=CONNAC, selecionando MT6632
por padrão apesar de WLAN_CHIP_ID=6765. Isso expôs MET/ABI RSSI/tabela AXI de
outro perfil. A tentativa de adaptar RSSI foi retirada integralmente de ambas
as cópias, junto do delta local criado para ela; não portar outro chip para
fechar esse rebuild. gl_wext_priv.c preservado com SHA256
9c13701018ddcff2a6d8d03d48c01b38c84a854188d6d9898f86389d0a3d756e.
Não alterar Werror nem omitir unidades. Restaurar CONNAC, MTK_ANDROID_WMT=y e
MET no como nos .cmd do build anterior. Snapshot RSSI local preservado em work/.

Resultado: somente gen4m-dfs-chandef-allocation-v1.patch integrado à fonte de
trabalho e cópia de build. Alocações de chandef/channel em temporários zerados;
ambas são verificadas e liberadas em erro de channel/lookup. Publicação ocorre
depois de preencher width/frequências, sem mudar o flag de switch sob falha.
Role BSS/glue e wdev/wiphy inválidos não são dereferenciados. Não altera comandos
RF anteriores à construção, nem migra a notificação ou torna channel canônico:
esses pontos continuam gates, não foram cobertos por um mock de wiphy_lock.

Dois testes passaram sob offline_guard, sem skips: nova regressão compila a
função inteira real com ASan/UBSan, falhas das três alocações (comando incluído),
lookup ausente, larguras 20/80/160/80+80, reuso da definição existente e roles
inválidos; radar/CAC histórico mantém limpeza original. Sem RF ou lockdep real.

Build completo ARM32/MODPOST aprovado, inclusive p2p_func.o/gl_wext_priv.o e
AXI reais, mantendo Werror. A primeira tentativa MODPOST do perfil correto
omitiu símbolos do adaptor; adicionar seu Module.symvers real resolveu seis
imports, sem stub/supressão. Comando reproduzível usado:

```sh
runtime="${KPF_RUNTIME_ROOT:?Selecione explicitamente o runtime local}"
make -C "$runtime/kernel-workspaces/lts-6.18.58-native-connsys-v1/linux-6.18.58" \
  O="$runtime/kernel-workspaces/lts-6.18.58-native-connsys-v1/build-wifi-20261028-v1" \
  M="$runtime/module-workspaces/nativewifi1-20261028-v1/src/wlan/core/gen4m" \
  MO="$runtime/module-workspaces/nativewifi1-20261028-v1/gen4m" \
  ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- \
  KERNEL_OUT="$runtime/kernel-workspaces/lts-6.18.58-native-connsys-v1/build-wifi-20261028-v1" \
  WMT_API_ROOT="$runtime/module-workspaces/nativewifi1-20261028-v1/src/wmt" \
  WLAN_CHIP_ID=6765 MTK_COMBO_CHIP=CONNAC MTK_ANDROID_WMT=y \
  CONFIG_MTK_COMBO_WIFI_HIF=axi CONFIG_MTK_COMBO_WIFI=m MODULE_NAME=wlan_drv_gen4m \
  MTK_MET_PROFILING_SUPPORT=no MTK_MET_TAG_SUPPORT=no DRIVER_BUILD_DATE=20261028213712 \
  KBUILD_EXTRA_SYMBOLS="$runtime/module-workspaces/nativewifi1-20261028-v1/wmt/Module.symvers $runtime/module-workspaces/nativewifi1-20261028-v1/adaptor/Module.symvers" \
  -j4 modules
```

DRIVER_BUILD_DATE conservado do .cmd anterior, não data alegada do ensaio.
wlan_drv_gen4m.ko SHA256
6f0cdc9839faca90e2aa37840ddf841205ec72527228dd0ee44b548fcd255f69,
vermagic `6.18.58-k40s-nativewifi1-NOT-FOR-FLASH SMP mod_unload ARMv7 p2v8`.
Fonte/cópia conferidas iguais. Patch RSSI temporário criado nesta etapa foi
removido; fonte RSSI restaurada exatamente do hash original, snapshot recuperável
preservado em work/. Nenhuma mudança no kernel/cápsula BTv14 ou aparelho.

## Consumidor DT Wi-Fi MT6765 — decisão prévia 2026-10-29

Entrega de integração offline: ligar o consumidor gen4m OF existente aos recursos
reais no overlay WMT/BTIF, sem novo driver/imagem e sem habilitar o rádio. Base LG
kernel-4.9/arch/arm/boot/dts/mt6765.dts GPL-2.0: wifi@18000000, MMIO 1 MiB e SPI268
level-low. Reservas dinâmicas CONNSYS4MiB/Wi-Fi3MiB existentes no template K40S;
preservar geometry/no-map/alloc-ranges, sem inventar endereços fixos. SYSIRQ
upstream já integrado preserva a polaridade LG antes de GIC, como WMT/BTIF.

Alternativas auditadas localmente: framework OF/reserved-memory/IRQ Linux e
consumidor gen4m AXI já integrado são reaproveitados. Providers ICC mainline
MediaTek locais oferecem mt8183/mt8195, não match MT6765 comprovado; não copiar
seus IDs para fingir provider. Tela atual é LK/simplefb, não drm_panel nativo.
Mainline/postmarketOS/Qualcomm não fornecem phandles compatíveis por analogia.
Sem RE, novo parser, provider ou protocolo; DT GPL-2.0-only, teste Python MIT.

Decisão: nó native-compatible desativado, com MMIO/IRQ/reservas exatos; não
adicionar panel/interconnects fictícios. Driver mantém exigências e rejeita
habilitação incompleta. Só após providers e demais gates integrar status okay.
Aceite: DTC/fdtoverlay sobre baseline real, comparar recursos ao backup, nomes
e phandles de reserva corretos, status disabled preservado pelos seis overlays
LG, recursos WMT/BTIF e geometria das reservas sem alteração. Artefatos BTv14,
boot policy e imagens existentes não são regenerados ou substituídos.

Origem LG confirmada pelo cabeçalho GPLv2/MediaTek 2015, arquivo mt6765.dts
SHA256 cf608e7d9c2de0a48d2bb6cc8a3d3031a30e46ed16f5d98601064c0a00c57efb;
árvore local 4.9, sem commit Git confirmado (não inventar revisão upstream).
O compatible específico é o já consumido pelo gen4m integrado, não um binding
upstream reivindicado. Código do driver e validação de providers não mudaram.

Resultado: overlay existente ganhou wifi@18000000 disabled e somente um phandle
na reserva Wi-Fi já existente, com memory-region-names consys/wifi. Sem DTB/image
persistente novo. Sete testes passaram sob offline_guard, sem skips: três casos
DT CONNSYS (incluindo aplicação dos seis DTBOs reais LG), reservas gen4m,
lifecycle OF, follower DRM e bandwidth ICC. DTC/fdtoverlay reais executados em
temporários; regressões C preservam seus modelos/flags/falhas existentes.
Comparação inicial recusou o novo phandle da reserva: expectativa foi ajustada
somente para esse campo intencional, com igualdade estrita de todas as demais
propriedades e do phandle referenciado pelo consumidor; geometria não relaxada.
Isso valida ligação desativada, não bind, alocação efetiva ou WLAN/RF no aparelho.
Sem rebuild de kernel/módulos, alteração da cápsula BTv14 ou operação física.

## Admissão de reset antes do hardware — decisão prévia 2026-10-29

Inspeção do gate coredump: stp_dbg_start_emi_dump abre proteção e notifica
userspace; WMT_mmap em wmt_dev.c usa remap_pfn_range para EMI/MCIF, sem drenar
VMAs ao stop/timeout. Logo um begin/end de MPU sozinho não prova ownership dos
leitores assíncronos. Sem alterar essa ABI ou desabilitar diagnóstico/proteções
para declarar o gate resolvido. Continua pendente portação do leitor/ownership.

Próxima entrega concreta: impedir que reset entre em efeitos de power-off/PDMA
quando a calibração está ocupada. Reusar mutex_trylock já integrado e um callback
escopado ao reset LG (mesmo padrão de lifetime da transação MPU), não exportar
lock/unlock independentes nem autorizar entrada owned fora do callback.
Linux já fornece mutex; postmarketOS/Qualcomm não substituem a sequência de
reset MT6765. Sem driver paralelo ou RE. C/delta GPL-2.0, regressão Python MIT.

Ordem: consys_power_lock -> trylock calibração -> preflight/efeitos/reset/restore
-> MPU. Não esperar calibração enquanto mantém power_lock; EBUSY antes de entrar
no callback não muda PDMA/status/fault ou energia. Callback recebe restore owned
sem reaquisição do mesmo mutex. Em erro depois da admissão, preservar guards e
fault do reset existente; liberar calibração em todo retorno. Não resolve todos
os outros controles de energia, lifetime do pdev ou coredump.

Snapshot work/wmt-reset-admission-base-20261029-v1, fontes/build iguais:
wmt_ic_soc.c b0ed6d110f40477324caed8b6334abe0ea832b401b6db8b2389b211704f6fba5;
wmt_ic.h 62b91dfc2307969eee0371cb170a6cf2ea8c9778320f7c3fbfa36f9d95f540b3;
mtk_wcn_consys_hw.c 38990ee1a38823117f739832d707325ed760d16a7f41bec72431e206eb2b1a09.
Sem mudança de kernel, originais LG, cápsula BTv14 ou autorização física.

Resultado: `wmt-reset-calibration-admission-v1.patch` integrado às fontes de
trabalho e cópia nativewifi1. Callback síncrono interno ao mesmo módulo, sem
EXPORT_SYMBOL novo. Entradas de reset nativas passam pelo escopo; reset legado
não nativo continua recebendo a função original de restore. O helper rejeita
callback NULL e libera calibração em todo retorno do callback. Nenhuma mudança
em verificador, limite elétrico, backup, supervisão ou caminho de recuperação.

Regressão nova `test_wmt_reset_admission` aplica o delta sobre os três inputs
pinados e compila funções reais do escopo, reset interno e wrapper público sob
ASan/UBSan, calibração ligada/desligada e hooks opcionais presentes/ausentes.
Busy com mutex real já adquirido preserva todos os efeitos e fault anterior;
preflight falho não toca hardware; falhas off/restore/on mantêm guards/fault e
sempre soltam ownership. Sucesso preserva a sequência de eventos LG esperada.
Os seis testes direcionados passaram sob offline_guard, sem skips (admissão,
STP/lifetime, restore de reset, MPU24, reset e SRCU históricos). O teste novo
não é execução do reset físico nem validação concorrente de todas as transições.

Build ARM32 e MODPOST passaram com o comando nativewifi1/AUTOCONF_H explícito
já documentado no incremento inicial de reset. wmt_drv.ko SHA256
082dd2903d3e8f26f9fbec71de31187d7ebeb9f61eb734fd694faca0a63d33ae,
vermagic `6.18.58-k40s-nativewifi1-NOT-FOR-FLASH SMP mod_unload ARMv7 p2v8`.
Coredump/mmap, outros controles de energia e pdev continuam gates. Sem alteração
de gen4m/kernel/cápsula BTv14, SMC, carga, boot, RF ou acesso ao aparelho.

## Lifetime de calibração nativa — decisão prévia 2026-10-29

Entrega: exclusão de leitores/substituição/limpeza dos buffers BT/Wi-Fi entre
do_calibration e restore exportado do reset. Reutilizar mutex_trylock/unlock do
Linux e os caminhos LG GPL-2.0 existentes; não introduzir RCU/refcount/duplicação
de protocolo. Mainline já fornece a primitiva, postmarketOS/Qualcomm não mudam
o ownership desse estado LG local; sem driver novo, RE ou biblioteca externa.
Delta C GPL-2.0, regressão host MIT.

Inspeção local: todos os acessos a gBTCalResult/gWiFiCalResult e seus tamanhos
estão em wmt_ic_soc.c, nos caminhos de calibração e restore/reset. wmt_core_rx
entra em wmt_ctrl e sinaliza falhas/assert; TX pode esperar/repetir. Logo não
esperar bloqueando outro controlador com um mutex de calibração. No perfil
nativo, as duas entradas disputarão o mesmo mutex por trylock e devolverão
-EBUSY se ocupado, sem tocar buffers ou esperar STP/MPU. Entrada dona cobre
restore STP, backup/publicação e limpeza até seu retorno. Restore do reset já
propaga erro e mantém guards quando falha. A ordem dentro da cópia é
calibração -> MPU; nenhum novo caminho espera calibração segurando MPU.

Isso resolve lifetime de buffers, não a coordenação integral de energia: reset
legado já pode ter desligado hardware antes de chamar restore; sua falha EBUSY
quarentena o reset, não autoriza retry/power-on. Serialização de transições,
ownership do dispositivo e coredump continuam gates antes de ativação.

Baseline após STP: wmt_ic_soc.c SHA256
bc53c329ce77502028af75f8a6427af9e8863052240ec537989cb8d7e8507249,
snapshot work/wmt-cal-lifetime-base-20261029-v1/common_main/core/wmt_ic_soc.c,
cópia de build conferida igual. Preservar caminho fora do perfil nativo, fontes
LG originais, cápsula BTv14 e mecanismos de recuperação; sem ação física.

Resultado: `wmt-calibration-lifetime-v1.patch` integrado à fonte canônica de
trabalho e cópia de build. Calibração existente passa a corpo owned privado;
wrapper original e restore exportado nativo adquirem por trylock, liberando em
todo retorno de sucesso/falha. Nenhum novo export ou ABI; caminho não nativo
continua chamando o corpo existente sem essa política de laboratório.

Regressão `test_wmt_calibration_stp` ampliada sem duplicar modelo: aplica STP e
lifetime em ordem, conferindo o hash intermediário bc53c329... antes do delta.
Pthreads/condvars suspendem o dono nas duas cópias EMI, RX STP e script que falha
antes da limpeza. Ambas entradas reais concorrentes devolvem EBUSY sem alocar,
copiar, liberar/substituir buffers nem emitir TX. Depois da liberação, dono
termina e os dados/limpeza são conferidos; mutex novamente disponível inclusive
após falha. Sem sleeps ou retry de transporte. MODELO usa pthread mutex_trylock,
não um bool que inventa exclusão; ASan/UBSan não equivale a prova lockdep/TSAN
nem a ensaio concorrente no aparelho. Transições de energia continuam pendentes.

Cinco testes passaram sob offline_guard, sem skips: calibração STP ampliada,
calibração reset, MPU24, reset e SRCU históricos. Build ARM32/MODPOST passou com
o comando nativewifi1/AUTOCONF_H explícito já registrado abaixo. wmt_drv.ko
SHA256 fe77768d269edf5feca008088361d63421d84610e3e80c6625886ea9a030037c,
vermagic `6.18.58-k40s-nativewifi1-NOT-FOR-FLASH SMP mod_unload ARMv7 p2v8`.
Fontes de trabalho/build conferidas iguais; sem rebuild gen4m, alteração do
kernel/cápsula BTv14, SMC, carga, RF, boot ou acesso ao aparelho.

## Calibração STP nativa: backup delimitado — decisão prévia 2026-10-29

Bloqueio: backup lê comprimentos STP sem conferir todo o frame, altera buffers
publicados antes de concluir EMI e ignora erro de MPU. O chamador ainda transforma
falha de backup em sucesso. Entrega: validar frame/reserva antes de alocar/copiar,
copiar sob a transação MPU24 existente, publicar somente após reproteção e
propagar erro no perfil nativo. Restore STP não deve abrir janela apenas para
scripts STEP arbitrários, nem recalibrar após erro real de transporte/proteção.

Reutilizar código LG/MediaTek GPL-2.0 já integrado em wmt_ic_soc.c, transação
mtk_wcn_consys_wifi_emi_access e APIs Linux get_unaligned_le16/32, ioremap,
OSAL memcpy_fromio/toio e alocação existente. Mainline/SMCCC já compõe o backend;
postmarketOS/Qualcomm não fornecem substituto comprovado para o frame LG nem a
política MPU MT6765. Não implementar protocolo novo, driver paralelo ou RE.
Python de regressão MIT; C/delta mantém GPL-2.0 e avisos originais.

Entrada integrada após o incremento de reset, SHA256 wmt_ic_soc.c
4c3849fda1ba1177e151b5acc8b7ae97d0516dcf53bebfb163cf8a80d4e0e02d,
preservada em work/wmt-cal-stp-base-20261029-v1/common_main/core/wmt_ic_soc.c;
cópia de build conferida idêntica antes da edição. Escopo nativo: caminho legado
não selecionado permanece disponível. Serialização/lifetime global de calibração
e ownership de coredump continuam gates separados, não serão declarados resolvidos.
Sem autorização para carga/SMC/RF/ensaio ou mudança do candidato físico validado.

Resultado: `wmt-calibration-stp-transaction-v1.patch` integrado à fonte de trabalho
e cópia nativewifi1. Regra de frame baseada no formato LG existente: payload
declarado X+14 e recebido X+18, BT não vazio e descritor Wi-Fi de 8 bytes. Não
aceita extensões/truncamentos implícitos nem usa comprimentos antes dos limites.
Backups temporários só substituem o conjunto salvo após cópia/reproteção; em erro
o conjunto anterior permanece. Isto não oferece exclusão mútua entre threads.
Restore STP não faz cópia EMI: restauração Wi-Fi já pertence ao reset, preservando
essa ordem LG; seu antigo toggle atendia somente STEP arbitrário, não selecionado
no caminho nativo. Inicialização sem backup usa -ENODATA como único fallback
nativo para calibração nova; erros de transporte/estado não são disfarçados.

Cinco testes passaram sob offline_guard, sem skips: test_wmt_calibration_stp,
test_wmt_calibration_reset, test_wmt_emi_transaction, test_wmt_reset_errors e
test_wmt_wlan_srcu. Nova regressão aplica o delta à entrada pinada e executa
funções reais de backup, restore, cópia/validação e chamador sob ASan/UBSan.
Cobre sucesso e volta EMI->backup->EMI, frames curtos/longos/inconsistentes,
limites de BT/descritor/offset/tamanho, três falhas de alocação, mapping,
admissão/reproteção, TX/RX/short write e ausência/estado inválido de backup.
Confere preservação dos buffers antigos/liberação dos temporários e que erro
não é convertido em nova calibração ou sucesso. Snapshots dos outros quatro
testes continuam históricos: não são testes físicos nem toda a integração.

Primeira compilação do double expôs seleção de protótipos em vez das definições
(corrigida para rindex explícito) e comparação signed/unsigned no double;
comparação de tamanho do novo C também usa constante unsigned. Nada foi aprovado
por troca de pin ou relaxamento de proteção. Build ARM32 e MODPOST passaram com
o mesmo comando documentado no incremento de reset, AUTOCONF_H nativewifi1
explícito. wmt_drv.ko SHA256
57f495948d7a8904a508b62cc3c6e7d3626c1d766d09b8ae0cc3f6a417de7682,
vermagic `6.18.58-k40s-nativewifi1-NOT-FOR-FLASH SMP mod_unload ARMv7 p2v8`.
Sem mudança de ABI exportada, recompilação gen4m, kernel, cápsula BTv14 ou aparelho.
Próximos gates: lifetime concorrente de calibração, ownership de coredump,
DT/providers e autorização específica antes de qualquer ativação.

## Reset nativo: restauração de calibração Wi-Fi — decisão prévia 2026-10-29

Entrega pretendida: impedir power-on após erro de restauração de calibração no
reset WMT do candidato 6.18.58 nativewifi1. Aceite offline: cópia delimitada pela
transação MPU24 existente, validação dos limites sem overflow, erro de mapping/
abertura/reproteção propagado ao reset, guards de reset/PDMA retidos sob falha.
Não equivale a rádio funcionando e não autoriza carga/SMC/RF/flash.

Reuso antes de implementar: fonte LG/MediaTek GPL-2.0 em wmt_ic_soc.c, wmt_ic.h
e mtk_wcn_consys_hw.c, já adaptada para 6.18; API local auditada
mtk_wcn_consys_wifi_emi_access em mt6765.c e mtk_emi_native.h. Usar ioremap,
memcpy_toio e iounmap existentes, não criar driver, parser ou backend de MPU.
Mainline I/O/SMCCC já usados pelo backend; regmap não substitui transferência
de RAM EMI nem o protocolo de calibração LG. Alternativas postmarketOS/Qualcomm
não demonstram compatibilidade com a janela/firmware MT6765 e não são importadas.
Sem RE ou dependência externa nova. Delta de C GPL-2.0; regressão Python MIT.

Snapshot anterior preservado em work/wmt-cal-reset-base-20261029-v1, cópias
canônica/de build conferidas iguais antes da edição. SHA256 de entrada:
wmt_ic_soc.c 98f95819c7be4335960b0789666e6f174b0ad99eda91d0580f6edb509118546a;
wmt_ic.h 6677995be21cfad11b6a95d4aee6a7a43b4a7e8d941c75388f2f5b6b0482b02d;
mtk_wcn_consys_hw.c 68456e4cafe600e5194f3da3134c77252c948b8105ec7db3931090cada80b1f1.

Incremento restrito ao restore de reset nativo; backup/restauração por comando
STP e ownership de coredump continuam gates. Não reaproveitar scripts STEP de
debug arbitrários dentro da transação MPU: o callback nativo faz somente a cópia
delimitada, sem reentrada em controle WMT. Caminho legado fora do perfil nativo
preserva sua sequência; não há substituição de candidato físico validado.

Resultado offline: delta `patches/kernel/staging/wmt-calibration-reset-transaction-v1.patch`
integrado à fonte de trabalho e à cópia de build, sem alterar originais LG,
kernel, gen4m ou cápsula BTv14. Callback usa a assinatura real OSAL (PVOID const
é ponteiro const, não ponteiro para dados const); build inicial detectou o erro
de qualifier na adaptação e foi corrigido sem suprimir warning.

Quatro testes passaram sob offline_guard, sem skips: test_wmt_calibration_reset,
test_wmt_emi_transaction, test_wmt_reset_errors e test_wmt_wlan_srcu. A nova
regressão aplica o patch sobre os três inputs pinados e executa C real de
restore/reset com ASan/UBSan, calibração ligada/desligada, admissão/reproteção
falhas, ioremap falho, ausência/estado parcial de buffer, reserva pequena, offsets
fora da janela, overflow e limite superior exato. Os outros testes preservam
seus próprios baselines históricos; não alegam cobertura do backup/STP atual.
O primeiro ensaio host expôs macro de logging ausente no double CFG=0, corrigida
somente no double; execução final aprovada. Nada disso valida SIP ou RF físico.

Build ARM32/MODPOST aprovado com o comando (raiz Linux abaixo abreviada somente
na documentação, não variável de sistema):

```sh
runtime="${KPF_RUNTIME_ROOT:?Selecione explicitamente o runtime local}"
make -C "$runtime/kernel-workspaces/lts-6.18.58-native-connsys-v1/linux-6.18.58" \
  O="$runtime/kernel-workspaces/lts-6.18.58-native-connsys-v1/build-wifi-20261028-v1" \
  M="$runtime/module-workspaces/nativewifi1-20261028-v1/src/wmt" \
  MO="$runtime/module-workspaces/nativewifi1-20261028-v1/wmt" \
  ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- \
  AUTOCONF_H="$runtime/kernel-workspaces/lts-6.18.58-native-connsys-v1/build-wifi-20261028-v1/include/generated/autoconf.h" \
  KBUILD_EXTRA_SYMBOLS="$runtime/module-workspaces/nativewifi1-20261028-v1/btif/Module.symvers" \
  -j4 modules
```

AUTOCONF_H explícito é obrigatório: omiti-lo misturou autoconf nativeusbemmc1
com nativewifi1 e o compilador recusou CONFIG_LOCALVERSION duplicado; nenhuma
verificação foi relaxada. Módulo resultante wmt/wmt_drv.ko SHA256
3ba72c9ed03ef192d51836f90a52385f7e032273310ef86f7c42d7ad97cc8c20,
vermagic `6.18.58-k40s-nativewifi1-NOT-FOR-FLASH SMP mod_unload ARMv7 p2v8`.
Nenhuma ABI exportada foi alterada por este delta interno. Backup/STP, lifetime
dos buffers, coredump e DT/providers continuam bloqueios explícitos de ativação.

## Seleção independente de referências WMT — 2026-10-29

Reutilização: resolver MIT `tools/tests/support.py:source_path` e mapa schema 1
em `manifests/test-sources.json`, worktree atual. Não criar downloader, cópia de
fontes, snapshotter, driver ou protocolo. Mainline/postmarketOS/MediaTek/Qualcomm
não substituem a identidade das revisões C exercitadas por estes testes; não há
nova implementação de hardware nem RE. Python/metadados próprios MIT; fontes e
modelos C existentes mantêm suas licenças, hashes e avisos sem alteração.

Decisão: selecionar os inputs staged WMT por raiz `wmt_baselines`, conservando
os caminhos finais padrão e todos os pins. Um mapa explícito pode separar as
referências das edições ativas sem redirecionar fontes vendor/kernel. A ausência
da raiz no mapa explícito falha sem fallback. O padrão continua legado/mutável;
não afirmar imutabilidade nem sanar divergências por troca de hash. Esforço
limitado a metadados de localização e regressões de seleção/falha; nenhum efeito
de probe/remove, carga, build ou recuperação no aparelho.

Validação direcionada com offline_guard: 26 testes de resolver/fixtures passaram;
BTM init, PSM init e STP core init compilaram/executaram suas fixtures C e passaram.
Caller e STP debug init continuam falhando antes de compilar, pelos mesmos pins:
`wmt_lib.c` observado `b435b48b...`, esperado `8c7c26b5...`; `stp_dbg.c`
observado `e9b55e4a...`, esperado `729c6415...`. Total da seleção: 29 passaram,
2 falharam, sem skips. Catálogo AST atualizado (938 casos classificados, não
938 testes executados). Nenhum transporte carregado; nenhum acesso ao aparelho.

## Checks PWRAP v2/v3 e fixture caller/quiesce WMT — 2026-10-29

Entrega host: eliminar herança entre módulos de teste PWRAP e import caller WMT
para obter modelos/pins/casos compartilhados. Aceite: mesmos IDs de casos PWRAP,
mesmo C v2/v3, metadados/modelos WMT idênticos, consumidores sem outros testes.
Não alterar polling, limites, drivers, recuperação ou pins divergentes.

Origem MIT: FILES/atributos/checks de `test_k40s_pwrap_handoff_v2.py` e
PINS/MODEL/CASES de `test_wmt_caller_init.py`, worktree atual. Reusar harnesses
sem unittest e dados já compartilhados; não criar parser, modelo de PMIC/SMC,
driver ou backend paralelo. Linux/LG/MediaTek continuam fonte do comportamento;
postmarketOS/Qualcomm não tornam PWRAP/WMT equivalentes ou universais. Sem RE ou
código externo novo. Python MIT, C gerado preserva avisos/licenças anteriores.
V3 ganha wrappers explícitos para os dois casos antes herdados; não é cobertura
nova nem motivo para somar crescimento do catálogo estático como testes novos.

Resultado: quatro consumidores desacoplados. IDs dos sete casos PWRAP coletados
antes/depois idênticos; C gerado v2/v3 preservado, SHA256
`b9d385f5b1d3f57708d4f3fad44b91d096a48f1f63472d408eac6f4608f440f2`,
`789a12f8c0ec491e6436b346929b87d73ea3909980cd59aca7920c35f5b2260f`.
MODEL/CASES WMT idênticos, SHA256
`4fd698dbf45ad8898ef0247a915e3e1280724c046afc272f1050190b0fbea1e8`,
`38e0abe578e601c9709830e2fdf30fdece047516ed322da856405f1c1ce86f1f`.
Gate de import carrega os quatro sem outros testes; novo gate AST cobre todos
os test_*.py, inclusive aliases/aninhados, e confirma zero imports estáticos.
Não afirmar ausência de dependências dinâmicas nem encerramento de toda a meta.

Vinte e oito testes sob guarda offline: vinte e seis passaram, caller/quiesce
recusaram wmt_lib observado
`b435b48b3a47be665ff9850f9828d400b8dcf764d1b73c6c4cd3d47c0aa898de`, esperado
`8c7c26b59774c23c8017f8bbeefabdb18a3982695eafe344e50da5a0922aa822`.
Recusa caller já reproduzida com path anterior; quiesce reproduzido com paths e
dados de pins anteriores, antes de acessar modelo/casos. Nenhum pin, limite,
fonte canônico, mecanismo de recuperação ou componente físico foi modificado.

## Harnesses I2C/DMA MT6765 sem imports entre testes — 2026-10-29

Entrega host: separar preparo/modelos/compilação I2C e lifetime DMA, incluindo
três vetores já reutilizados pelo probe, de suas classes unittest. Aceite: C
gerado igual em configuração, transferências e vetores probe; mesmas fontes,
patches, flags, timeouts, casos/quarentenas e skips. Sem transferência, DMA,
reset, IRQ ou PM reais, sem alteração no driver/perfil.

Origem MIT: metadados/PRELUDE/function/block/sources/base/run_c de
`test_mt6765_i2c_native.py`; metadados/EXTRA/STUBS/SETUP/sources/fixture/run_c e
três casos compartilhados de `test_mt6765_dma_lifetime.py`, worktree atual.
Reusar mixins/helpers e fontes pinadas Linux/MediaTek; não criar parser, protocolo
ou driver paralelo. Mainline/postmarketOS/Qualcomm não comprovam comportamento
dos doubles de DMA/IRQ nem tornam a sequência MT6765 universal. Sem RE/código
externo novo; Python MIT, avisos GPL-2.0-only no C preservados.

Resultado: três consumidores desacoplados; casos não delegados dos provedores
preservados por AST. Três vetores compartilhados mantêm wrappers unittest e o
mesmo C no harness, sem herança de TestCase ou métodos test_* nas fixtures.
Modelos idênticos, SHA256 PRELUDE
`0c65df693b626888322becb82797fabe92e21b6f26ad9c9b31a19714ab4a93d4`, EXTRA
`11890a1a96a0c9480efaec0c6e414c2668238b91f93919e2609a9677df0529ef`, STUBS
`25960783062db884cac83b11db7b508c448f48213b2da13969a1b7914643165b`, SETUP
`e61591d1ef77abf3a21939b8dfe5c484f29d5dc72ef42dd05ba22e7bb47baeab`.
Cinco programas C comparados antes/depois: nativo
`fe02796b66508b2000bcacbbf812527b77e1249c4572142101a0240d263a8dd3`, DMA
`95d5b7dc04d798d84443925d53e35cc92cb0a4a57d59da1a66e0284ac0b0692f`, probe
`c6f808902e428147bbfab23c1d8a0a2e3e714614d71d4b5914b40ad5e6fa50bf`,
`270912807718e9a67c52952061a2eeec8d72307f15f8e3b6432b6faf2fa064af`,
`918dc4f1086fc37ddbfbb38d1fb437bd55e2580277b9c6401e6df02a0f84e4b6`.
Trinta e cinco testes sob guarda offline passaram sem skips, incluindo DT/schema,
falhas/requisição seguinte, quarentena, remoção/PM e probe. Gate carrega os três
módulos recusando imports de outros testes. Flags/timeouts/recusas mantidos,
compilação/patches em temporários, nenhum driver/fonte canônico/aparelho alterado.

## Harnesses CCF callbacks/unwind MT6765 — 2026-10-29

Entrega host: compartilhar fontes/modelos/compilação CCF e preparo/run do patch
de unwind sem importar TestCase de clocks em PLL, consumers ou I2C probe.
Aceite: modelos/pins e C gerado idênticos, métodos/skips/casos/flags intactos;
classes de suporte sem unittest. Sem CCF, PLL, SMP, MMIO ou kernel real.

Origem MIT: metadados/PRELUDE e sources/run_c/compile_c de
`test_mt6765_ccf_callbacks.py`; ROOT/PATH/PATCH/STUBS e sources/run_c de
`test_mt6765_ccf_unwind.py`, worktree atual. Reusar mixins e helpers existentes,
funções Linux pinadas, patch e compilador; não criar clock provider, parser C
ou modelo paralelo. Linux CCF/MediaTek permanecem autoridade sobre os contratos;
postmarketOS/Qualcomm não tornam os registradores/providers intercambiáveis.
Sem RE/código externo novo. Python MIT; avisos de GPL-2.0-only em C preservados.

Resultado: cinco módulos ajustados; casos dos dois provedores preservados por
comparação AST. PRELUDE e STUBS idênticos, SHA256
`73625b78ae2d5e2bbb9fab8d448b087cf8673312150863ff397d03388ce46ce9` e
`c22f38e8260edf1b6fadff68f803cdab7deef1a8da1e48ead71aeaab529d331c`.
C gerado nos dois vetores de equivalência permaneceu igual: callbacks
`5de1746b9740e39d8b5ec6d0458dbd815553886ed923e92224cc03bce65924f0`, unwind
`360164d324d5a37cd76f6f1d73ed5a56b714a917071b514ff71c44af10dcc76e`.
Quarenta e três testes sob guarda offline passaram sem skips, incluindo DT/schema,
PLL, native-consumers e I2C probe afetado. Gate novo carrega quatro consumidores
CCF/PLL sem outros testes; I2C probe ainda tem suas dependências de fixtures I2C,
não afirmar desacoplamento total dele. Mixins sem TestCase/casos test_* verificados.
Compilação/patches somente em fixtures temporárias, fontes canônicas e aparelho
intactos. Parâmetros, flags, timeouts, hashes e recusas anteriores preservados.

## Fixture FIFO para identificação/status sem introspecção de testes — 2026-10-29

Entrega host: compartilhar prelude/casos FIFO e compilação do fault suite sem
importar/instanciar FifoIdTests ou extrair strings de seu método por AST. Aceite:
C gerado idêntico para identificação, fault suite adaptado e seleção de status;
mesmos IDs, seletores, limites, recuperação e gates de carga preservados.
Nenhuma operação I2C/FIFO, carga, SMC ou gravação no aparelho.

Origem MIT do projeto: prelude/main e compilação em `test_k40s_fifo_id.py`,
worktree atual. Reusar o mesmo modelo/casos, headers reais e runner C existente;
helper recebe explicitamente o texto de sequência já selecionado, em vez de
monkeypatch global de Path.read_text. Sem novo driver/parser/protocolo. Linux,
postmarketOS/MediaTek/Qualcomm não tornam a janela FIFO MT6370 intercambiável;
não generalizar seletores/efeitos elétricos. RE desnecessária. Fixture Python
MIT; licenças de headers/C gerado preservadas. Testes de produção continuam
wrappers com mesmos skips/casos, sem remover verificações por erro/restauração.

Resultado: dois consumidores desacoplados, removida introspecção AST e execução
de TestCase alheio. Modelos literais idênticos, SHA256 PRELUDE
`9cb9e554f0a7b55a654891463c046e5a2433f7a8bfb9e3c7abd24b92cc3286aa`, CASES
`ef975bb61f4ac9db3144b411f4e33057f170aaa4ca4186404ad6a427a1efdc0a`.
Capturado C gerado antes/depois, hashes iguais: identificação
`28c04481b9db9d246f772868bc125570b95dfbbde6c7b9d6948c55aa59626d18`, fault suite
adaptado `793ec8897b8d3634faa381743ef1961fd55f9e9ad4dbf086e09ca325de66849d`, seletores
`1af619db9be8b3a966e46a0a5ef19dd09230a2bfad3e01180efa495e4f78e534`.
Vinte e quatro testes sob guarda offline passaram sem skips, incluindo import
dos dois consumidores bloqueando outros testes. Flags e assertions anteriores
preservados, nenhuma fonte/limite/recuperação alterada. Headers e códigos C apenas
compilados como fixtures host; nenhum acesso ao carregador/FIFO físico.

## Harnesses ADC/NTC e telemetria de bateria — 2026-10-29

Entrega host: reaproveitar verificações C parametrizadas ADC/NTC e telemetria/soak
sem importar ou instanciar outro TestCase. Aceite: C gerado idêntico para quatro
variantes, mesmos casos/flags/limites, wrappers e skips preservados. Nenhuma carga,
leitura física, conversão ADC real, térmica ou política elétrica alterada.

Origem MIT: método parametrizado de `test_k40s_battery_adc.py` e cycle/método
parametrizado de `test_k40s_battery_telemetry.py`, worktree atual. Extrair mixins
sem unittest, com assertions fornecidas pelo consumidor. Reusar drivers/headers,
models, seletores e compilador existentes; não criar driver/parsers concorrentes.
Linux power_supply/IIO e fontes LG continuam autoridade sobre ABI/unidades;
postmarketOS/MediaTek/Qualcomm não tornam calibração/limites comuns a qualquer
placa. Sem RE/código externo novo. Fixture Python MIT; licenças C preservadas.

Resultado: quatro módulos desacoplados; os casos não delegados dos provedores
permaneceram iguais por AST. Comparação de C gerado detectou reindentação
introduzida na extração, corrigida antes do aceite. As quatro variantes voltaram
a produzir exatamente os hashes anteriores: ADC
`fbf75e191730bd8cf02477e8378ab76e9ea3a9023ad9c42ec556def725590aa7`, NTC
`a86570bc2a90fb04769b4215432c5f242d56278dd5f6133ebbf596ab37f18e61`, telemetria
`507b191ffe52b41a9aeead00ca44fa079f37581f5c9b784426a133e1c98a4f9a`, soak
`940a441b7de8b1f609ab255ee30a624c6b569aba7d8437a53e045ddfa2f37500`.
Vinte e nove testes sob guarda offline passaram sem skips, incluindo gate de
imports e classes de suporte sem herança TestCase/casos test_*. Gates existentes
de falhas, limites, expiração e recuperação foram exercitados. Arquivos C só em
temporários; fontes canônicas, drivers, limites elétricos e aparelho intactos.

## Harness FT5446 fora das classes unittest — 2026-10-28

Entrega host: separar fontes/modelos e helpers de compilação frame/power dos
testes, para optional-iovcc não instanciar/importar outro TestCase. Aceite:
mesmos pares de fontes antes/depois dos patches, modelos C idênticos, casos,
flags, limites e erros preservados. Não executar touchscreen, regulador ou PM
no aparelho. Nenhuma ativação de patch/perfil ou alteração de fonte canônica.

Origem MIT: metadados/PRELUDE e métodos sources/run_c em
`test_ft5446_upstream.py`; PATCH/STUBS e sources/run_c em
`test_ft5446_power_prefix.py`, worktree atual. Reusar mixins de suporte sem
TestCase, assertivas do consumidor, source_path, parser/driver Linux e os mesmos
patches; não implementar driver, parser de frame ou modelo elétrico paralelo.
Linux/MediaTek/Qualcomm/postmarketOS não substituem os gates de componente e não
tornam FT5446 universal. RE desnecessária. Fixtures Python MIT; stubs/fontes C
GPL-2.0-only mantêm os avisos anteriores. Aliases/métodos públicos legados mantidos.

Resultado verificado em 2026-10-29: três módulos desacoplados. Modelos C
idênticos, SHA256 frame
`0bb593479c1131877674fd1153e0179f7d811e31dc99cc09e4b67deadec3d44a`, power
`c378dac48dd49eed661c64fd9a9a20265990a26c5e6747445fb399645fe3a3f4`.
Seis hashes dos pares sources() comparados antes/depois: upstream
`81817c94769417d6510981374a19411e28e4018a31d6d7bfa3e1c424fdab8ce9`, frame-v2
`46f197a1e80385d9d74d0942883bbba9aa383a5822576ba18b79157dd904d73c`, power
`f525d0be513ae66d6dc50e06d2dea4c1bf776cfd3041a3f9536322a8d93ce7b2`, optional
`f8a5510935f0e84f9d48e5ed037f0ddc55ad8abb82fbe3226e8fd55e0ab24fbc`.
Corpos dos casos dos provedores confirmados por AST; a composição de sources()
mantém cada etapa de patch e run_c continua despachando sources() do consumidor.
Vinte e sete testes sob guarda offline passaram sem skips, incluindo gate de
import sem outros testes e classes de suporte sem herança TestCase/casos test_*.
Flags, tempos e assertions C preservados. Nenhum componente físico alterado.

## Modelo da biblioteca WMT fora de unittest — 2026-10-28

Entrega host: compartilhar MODEL/ROOT/SOURCE de init WMT com late-init,
ownership e async-stop sem importar o teste early-init. Aceite: bytes C iguais,
corpos/pins/flags/casos intactos, quatro consumidores sem imports de outros testes.
Sem tocar no staging/driver, fonte canônica, firmware ou aparelho.

Origem MIT: metadados e MODEL em `test_wmt_lib_early_init.py`, worktree atual;
extrair `fixtures/wmt_library.py`, reutilizando source_path e doubles existentes.
Não criar framework de lifecycle, parser ou worker WMT alternativo. Os fontes
LG/Linux e seus pins continuam autoridade para esses testes; mainline,
postmarketOS/MediaTek/Qualcomm não tornam os doubles prova de ownership real.
RE desnecessária, sem código externo novo. Fixture Python MIT, C gerado com
funções vendor permanece com as licenças anteriores. Divergência de pin recusa.

Levantamento AST encontrou imports `import test_*` por alias que a busca anterior
por `from test_*` não cobria; a remoção desses três from-imports não significa
fim do desacoplamento de todos os testes. Não usar essa busca como prova global.

Resultado: quatro módulos migrados; comparação AST excluindo imports/constantes
movidas confirmou demais corpos/casos intactos. String C MODEL byte a byte
idêntica, SHA256 `d8647798be3099fdf5b1fcf5788a962a22f4a7e0077ed96d2865782510993fe3`.
Gate novo carrega os quatro consumidores recusando imports de outros testes.
Dezesseis testes sob guarda offline: doze testes de suporte passaram, quatro
regressões WMT recusaram o pin da fonte antes de usar modelo/seletor. Observado
`b435b48b3a47be665ff9850f9828d400b8dcf764d1b73c6c4cd3d47c0aa898de`, esperado
`8c7c26b59774c23c8017f8bbeefabdb18a3982695eafe344e50da5a0922aa822`.
As quatro recusas reproduzidas com path anterior e sentinelas de modelo/seletor;
não alterar hash/fonte nem afirmar regressões de ownership WMT aprovadas.

O teste de compatibilidade de aliases gen4m agora carrega explicitamente o módulo
legado, em vez de criar um import estático entre testes. Dois checks direcionados
após esse ajuste passaram. Auditoria AST de todos os test_*.py registra ainda
16 arestas estáticas em 12 módulos (inclui aliases), não zero dependências.
Nenhum transporte, staging, fonte canônico, backup ou componente foi modificado.

## Fixtures EMI, staging e seleção debug WMT — 2026-10-28

Entrega host: remover imports entre testes para obter o modelo EMI, paths
staging/debug e o seletor da última definição C. Aceite: constantes/modelo e
seleção/erros equivalentes; corpos/pins/flags intactos; sete consumidores
carregáveis sem outros unittest. Sem SMC, MPU, DMA ou execução no aparelho.

Origem MIT: ROOT/LG/PRELUDE de `test_wmt_emi_mpu.py`, ROOT/STAGING de
`test_wmt_caller_init.py`, ROOT/SOURCE/actual de `test_wmt_stp_debug_init.py`,
worktree atual. Reusar source_path e c_function, extraindo somente dados/helper
já compartilhados; não criar driver, parser C, protocolo ou modelo novo. Mainline,
MediaTek/Qualcomm/postmarketOS não tornam EMI/MPU intercambiáveis nem o modelo
host prova elétrica. Sem RE/código externo novo. Fixtures Python MIT; licenças
do C gerado preservadas. Pins divergentes de staging continuam recusados.

Resultado: sete módulos migrados; comparação AST excluindo imports e dados/helper
movidos confirmou o restante inalterado. Modelo EMI byte a byte idêntico, SHA256
`93763973f76aee4818dd8f9b7400ca9f7428ff16c300fc90ec9d783bd9c8e7ce`.
Seletor debug preservou texto/erros em cinco comparações contra o anterior.
Gate novo carrega os sete consumidores recusando imports de outros testes.

Dezoito testes sob guarda offline: quinze passaram, três recusaram fontes
divergentes antes da seleção C. Caller: wmt_lib observado
`b435b48b3a47be665ff9850f9828d400b8dcf764d1b73c6c4cd3d47c0aa898de`, esperado
`8c7c26b59774c23c8017f8bbeefabdb18a3982695eafe344e50da5a0922aa822`.
Debug init/teardown: stp_dbg observado
`e9b55e4ada6f6757889caac17a9da6187a3cb3c03cd6eb335e597de23f0ca274`, esperado
`729c64157b45b2ee419dad3f557cebcce7d7d9e355c9ac65883b10028c6cdbb6`.
As três recusas foram reproduzidas com paths anteriores explícitos. Pins não
alterados; não afirmar regressões caller/debug aprovadas. EMI/MPU/transação/SDIO
e testes de suporte passaram offline; fontes canônicas e aparelho intocados.

## Fixtures AXI/DMA e inputs gen4m — 2026-10-28

Entrega host: remover imports entre testes para obter modelos AXI/DMA, casos
de pool já compartilhados e sequência de patches/pins de ownership. Aceite:
constantes/string C byte a byte e ordem de patches iguais; corpos/flags/assertions
intactos; sete consumidores carregam sem importar outros unittest. Sem DMA,
cache, interconnect, EMI ou Wi-Fi no aparelho.

Origem MIT: PRELUDE de `test_gen4m_axi_dma.py`, PRELUDE/CASES de
`test_gen4m_axi_pool.py` e FILES/PATCHES de `test_gen4m_arm_stack_cache.py`,
worktree atual. Extrair fixtures por componente, não criar novos modelos nem
framework de DMA. Reusar as funções vendor/Linux e doubles existentes; mainline,
MediaTek/Qualcomm/postmarketOS não tornam esses modelos prova de DMA/cache real.
Sem código externo novo ou RE. Fixtures Python novas MIT; gerado C com fontes
GPL mantém licenças anteriores. Aliases antigos são preservados.

Resultado: sete módulos migrados, comparação AST excluindo imports/constantes
movidas confirmou demais corpos intactos. Strings C idênticas, SHA256 PRELUDE AXI
`0f2bd5e7663faebcbaecbb733754150ac2fd5fb2a9499b230770f3301d945787`, PRELUDE pool
`8cc4911a353c812e1470415edd9ad57ca4002f9f85ca80d560225a77eaa24b80`, CASES pool
`d2cf30b60b93b8288666695ad686b3aeb271da0825a02a92b051bbccd5a5fa4a`.
Representações dos pins e tuple de patches comparadas antes/depois, inclusive
ordem/tipos. Dezessete testes direcionados sob guarda offline passaram sem skips,
incluindo gate novo que carrega os sete módulos recusando imports de outros
testes. Flags/sanitizers originais preservados; patches e compilações somente em
fixtures temporárias, sem alterar fontes canônicas, kernel ou aparelho.

## Logging/SRCU e fonte DRM sem dependências entre testes — 2026-10-28

Entrega host: separar metadados de logging, modelo SRCU de dois epochs e a
localização DRM compartilhada por WMT/gen4m. Aceite: dados e string C idênticos,
mesmos pins/flags/casos, consumidores sem importar outro unittest. Sem rádio,
display, callback kernel, diagnóstico ou recuperação física.

Origem MIT: VENDOR/FILES de `test_wmt_log_lifecycle.py`, PRELUDE de
`test_wmt_log_callbacks.py`, LINUX/DRM de `test_wmt_panel_follower.py`, worktree
atual. Reusar source_path e modelos existentes em fixtures, não implementar
SRCU/DRM alternativos. Linux SRCU/DRM são as implementações reais, ainda extraídas
e testadas pelos mesmos consumidores; modelos host não as substituem.
MediaTek/Qualcomm/postmarketOS não tornam o modelo de logging WMT genérico nem
demonstram sincronização/atividade física. Nenhum código externo copiado, RE
desnecessária. Fixtures novas MIT; licenças de C gerado permanecem anteriores.

Resultado: seis módulos migrados; comparação AST excluindo imports e constantes
movidas confirmou o restante inalterado. String SRCU idêntica antes/depois,
SHA256 `b0ec043c6e2cffcaf325697f9bc1cb987f4093ba4bd62b81ffdf9605ae8ae612`.
Quinze testes direcionados sob guarda offline passaram sem skips, incluindo
gate novo que carrega os seis módulos recusando imports de outros testes.
As regressões existentes compilam as mesmas funções/modelos com flags anteriores
e aplicam patches somente em temporários; nenhuma fonte canônica ou componente
de kernel/aparelho foi alterado. Não afirmar validação física SRCU/DRM/WLAN.

## Fixtures de ciclo de vida WMT — 2026-10-28

Entrega host: compartilhar os modelos BTM, PSM e STP-core usados por testes de
init/teardown sem importar classes unittest entre si. Aceite: strings C iguais,
mesmos pins/flags/casos e consumidores importáveis sem outros testes. Sem WMT
real, workers de kernel, rádio, MMIO ou recuperação física.

Origem MIT: MODEL/ROOT/SOURCE existentes em `test_wmt_btm_init.py`,
`test_wmt_psm_init.py` e `test_wmt_stp_core_init.py` no worktree atual; mover para
fixtures por componente, preservando aliases dos módulos anteriores. Reusar
source_path e seletores C de suporte; não criar modelo de transporte nem
generalizar BTM/PSM/STP como protocolos Qualcomm ou drivers universais.
Fontes LG/MediaTek/Linux continuam pinadas; postmarketOS e mainline não substituem
estes testes locais de callbacks. Nenhum código externo copiado, RE desnecessária.
Fixtures Python novas MIT; C gerado com fonte GPL mantém licença anterior.

Resultado: seis módulos migrados; comparação AST excluindo somente imports e
constantes movidas confirmou corpos/casos inalterados. Strings MODEL preservadas
byte a byte, SHA256 BTM
`9c9e2b2c4cfdd8b1f0b63be1ac298e93948da124dfae820cf7064c54a1a743d4`, PSM
`6b80c933588ac1ef9178bb6b62941f214e25293167568e3dfe3af9564f05df64`, STP
`a9a5144afdad67e22e9f1be54286dbb88570f80d6e0441c20c485c71e6090d79`.
Gate novo carrega os seis módulos recusando imports de outros testes.

Quatorze testes sob guarda offline: treze passaram, um recusou hash de baseline
de debug após reverse-patch no temporário. Canonical staging `common_main/linux/stp_dbg.c`
tem SHA256 `e9b55e4ada6f6757889caac17a9da6187a3cb3c03cd6eb335e597de23f0ca274`;
depois de desfazer `wmt-stp-owner-teardown-v1.patch`, observado
`e2e52471cfeaed89f76de72137bd1d76b4590adca86dadbb2689a2d973fdfbce`, esperado
`254fef9209171078b1801ca68596d7fc777cb53773708c5920198f136eb36c8c`.
Reprodução com path anterior explícito e modelo sentinela confirmou a mesma
falha antes de acessar MODEL. Não atualizar pin/patch/fonte para fazer passar;
não afirmar regressão STP teardown aprovada. Os demais testes compilam fixtures
locais com flags anteriores; nenhum componente ou fonte canônico foi modificado.

## Referência libfdt e imports dos testes legados — 2026-10-28

Entrega host: remover dependência do módulo memory-handoff para obter ROOT/KERNEL
e do teste de recovery para obter o helper pstore. Aceite: caminhos/overrides e
corpos de teste preservados, consumidor carrega sem importar outro unittest.
Nenhuma alteração no código de handoff, recuperação ou composição de boot.

Reusar ROOT, source_path e load_tool de suporte; selecionar os mesmos fontes
libfdt existentes, sem novo parser/modelo/build. Linux/DTC já implementam libfdt;
postmarketOS/MediaTek/Qualcomm não justificam copiá-lo ou substituir o check C
existente. Sem RE. Factory de localização em `fixtures/libfdt_sources.py` MIT,
com raiz padrão já registrada no mapa. Código C/Linux mantém licença anterior.

`K40S_TEST_KERNEL` continua prioridade exata, inclusive valor vazio como antes;
na ausência dela, `KPF_TEST_SOURCE_ROOTS` permite relocar a mesma árvore early-v2.
Não inferir compatibilidade com outra revisão só por existir libfdt no diretório.
Não executar nenhum fluxo de coleta/restauração para testar a organização.

Resultado: dez módulos desacoplados de memory-handoff/recovery, sem alterar seus
corpos de teste. Nos sete consumidores de ROOT apenas, comparação AST excluindo
imports confirmou invariância do restante. Os dez módulos carregam com imports
de outros testes proibidos. Teste da factory confirma caminho padrão, override
de raiz e prioridade da variável legada (inclusive vazia) sem consultar mapa
inválido. Cento e trinta e cinco testes direcionados passaram sob guarda offline,
sem skips; checks C compilados localmente e regressões de recuperação em mocks.
Mensagens DA_SESSION/flash/restore são produzidas pelos doubles: nenhum transporte
real foi importado/aberto nem houve gravação no aparelho. Pins, fontes externas,
backups e mecanismos de recuperação permaneceram intocados.

## Modelos BTIF compartilhados fora de unittest — 2026-10-28

Entrega host: separar modelos de MMIO/clock/locks e sessão/usuários das classes
de teste DMA reset e membership. Aceite: strings C byte a byte idênticas,
consumidores sem importar outro unittest, caminhos/pins/flags/assertions mantidos.
Não executar Bluetooth, DMA, MMIO ou ensaio no telefone.

Origem MIT: stubs locais MODEL de `test_btif_dma_reset.py` e MODEL/DRAIN_MODEL de
`test_btif_user_membership.py`, no worktree atual. Reusar estes modelos em
`tools/tests/fixtures/btif_dma.py` e `btif_users.py`; não implementar modelo novo,
parser, driver, protocolo ou abstração universal. Fontes LG/Linux continuam
pinadas pelos consumidores e C gerado com funções GPL conserva sua licença.
Mainline/postmarketOS/MediaTek/Qualcomm não tornam estes stubs validação de DMA
ou locking real; RE não é necessária com as fixtures/fontes existentes.

Fixtures novas MIT, aliases legados mantidos nos módulos originais. Modelos
permanecem específicos do componente e do teste host, nunca backend de transporte
nem substitutos para SRCU, IRQ ou sincronização de kernel reais.

Resultado: dez módulos migrados; comparação AST excluindo somente imports e
constantes movidas confirmou demais declarações/corpos intactos. SHA256 das
strings C antes/depois idêntico: MODEL DMA
`cedc9a1cfaef9f02e389981d5e3cbc4544e8ca23dc90f8ff68f8cb660d21e482`,
MODEL usuários `cccb50435449697df721942ea9294f1d4792e4488f71423bf0c619693cdd7360`,
DRAIN_MODEL `c1a54500bd396f50e8514ddb2a7a5648cc63224bf942f1ec36c5f6d75f700172`.
Quinze testes direcionados sob guarda offline passaram sem skips, incluindo os
dez testes BTIF afetados e um novo gate que carrega os dez módulos recusando
imports de qualquer outro teste. Fixtures reais compiladas com flags anteriores,
incluindo sanitizers/pthread nos consumidores que já os exigiam. Patches somente
em temporários, fontes externas canônicas e pins intactos; nenhum ensaio físico.

## Fixtures gen4m sem importar testes de chaves — 2026-10-28

Entrega host: retirar a dependência do teste cfg80211 keys para obter a localização
das fontes gen4m. Aceite: constantes padrão idênticas, consumidores não importam
testes de outro recurso, corpos/hash/flags/skips preservados. Sem ensaio de rádio.

Reusar `source_path`/ROOT existentes e extrair somente os dois aliases de
`test_gen4m_cfg80211_keys.py` (MIT) para fixture de componente. Não criar catálogo
de drivers, novos modelos ou loader de fonte vendor. Linux/postmarketOS e fontes
MediaTek/Qualcomm não fornecem a configuração local das fixtures; o conteúdo e
licença vendor continuam intocados e os hashes permanecem nos testes consumidores.
RE não se aplica. `fixtures/__init__.py`, `fixtures/gen4m_sources.py` e testes novos
são MIT do projeto. Arquivos C já existentes em fixtures permanecem inalterados.

O path de componente gen4m não vira regra para qualquer SoC. Configuração de
raízes é selecionada antes dos imports, como antes; imports que precisam apenas
ROOT usam suporte sem carregar configuração de fonte desnecessária.

Continuação no mesmo incremento: metadados da fixture generic-adc-battery
(origem/revisão, hashes e patches) separados do módulo unittest. `linux_source()`
resolve a localização quando o consumidor é carregado, preservando seleção por
ambiente e reloads anteriores. RTC/watchdog passam a usar diretamente o resolver
de fontes, sem depender da fixture de bateria para localizar sua árvore Linux.
Não mudar ordem ou conteúdo de patches nem retirar checks/limites elétricos.

Resultado: 32 módulos gen4m/WMT ajustados; importação de todos sob guarda offline
e 11 testes direcionados passaram sem skips. Quatro módulos de bateria/RTC/WDT
ajustados; seleção adicional de 27 testes passou sem skips, incluindo seleção de
raiz/override, status/pareamento sintéticos, RTC e watchdog. Há sobreposição dos
testes de suporte entre as seleções; não somar como casos distintos. Comparação
AST confirmou corpos de testes inalterados. Quatro testes novos de suporte
confirmam aliases, resolver e carregamento de netdev/bateria pareada com imports
de outros testes proibidos. `fixtures/generic_adc_battery.py` também é MIT.
Nenhum source canônico, firmware, hardware, patch ou pin foi modificado; as
compilações/aplicações de patch ocorreram apenas nas fixtures temporárias.

## Enquadramento de snapshots de registradores — 2026-10-28

Entrega host: reutilizar a validação de begin/read-only, campos ordenados,
amostras, máscaras de exportação e conclusão consistente do analisador PWRAP.
Aceite: JSON válido do wrapper preservado, mesmas capturas inválidas recusadas;
outro contrato com quantidade/offsets/máscaras diferentes funciona offline.
Nenhum MMIO, leitura PMIC, execução diagnóstica ou operação física.

Origem MIT: primeira parte de `tools/analyze-k40s-pwrap-diag.py` no worktree atual.
Reusar regex/algoritmo existentes, perfis, captura limitada e evidência create-only;
não escrever decoder binário, regmap paralelo ou interpretador de expressão.
Linux/regmap e fontes MediaTek já definem o significado dos registradores; os
valores/mainPLL/WACS não são genéricos nem transferíveis de MediaTek para
Qualcomm/postmarketOS. RE não se aplica ao formato com fonte disponível.

Decisão: core só valida formato de log e máscaras explícitas por campo. Política
do protocolo fica no perfil; cálculos/limites/estado de PWRAP e seleção das cópias
pstore permanecem no consumidor específico. Mascaramento no log não autoriza
acesso ao hardware nem prova ausência de efeitos elétricos. Helper, CLI e testes
novos MIT, sem fonte externo copiado ou alteração dos diagnósticos no kernel.

Resultado: 28 testes direcionados sob guarda offline passaram sem skips,
incluindo seis testes novos. Perfil sintético com três amostras, dois bancos,
offsets e máscaras diferentes prova separação do formato. Negativos cobrem
campos duplicados/fora de ordem, amostras, bits privados, marcadores, contagem,
read-only declarado, estabilidade inconsistente, contrato inválido, UTF-8/NUL,
contrato ausente e saída existente. Captura intacta e flags de limitação testadas.
Quinze comparações com o `analyze` anterior preservaram JSON completo ou recusa
por ValueError; mensagens de contagem/máscara agora são genéricas. O wrapper
mantém tratamento de bytes inválidos e aceite de snapshots completos cujo
handoff é falso; CLI nova exige UTF-8 válido. Fonte do diagnóstico, decoder de
estados e funções de captura/main não foram alterados. Nenhum ensaio físico.

## Análise SMP offline sem diagnósticos da placa — 2026-10-28

Entrega host: analisar eventos SMP capturados com prefixos/limite de CPU explícitos,
sem carregar PLL/CCF/ATF K40S. Aceite: wrapper conserva relatórios e recusas;
perfil sintético usa outro prefixo/IDs; inferência ARM exige opção booleana
explícita e continua marcada como inferência, não medição. Sem ensaio físico.

Origem MIT: corpo de `kernel_findings` em `tools/analyze-k40s-smp-logs.py` no
worktree atual; extração para `portkit/core/smp.py`. Reusar regexes existentes,
`parse_cpu_list`, leitura limitada de captura, perfis e evidência create-only.
Não implementar tracing de kernel, transporte, protocolo PSCI ou parser ATF novo.
Logs mainline dependem de arquitetura/versão; postmarketOS e árvores MediaTek/
Qualcomm não justificam inferir a mesma semântica em toda placa. Flags do DT ou
timeout de uma captura não comprovam power-on, entrada C ou boot correlacionado.
Reaproveitar o diagnóstico existente em vez de copiar código vendor ou usar RE.

Decisão: prefixos e limite passam ao perfil; somente a hipótese ARM anteriormente
usada é selecionável, sem inferir arquitetura do nome da placa. PLL/CCF/ATF,
endereços e registros permanecem específicos. Helpers/CLI/testes novos MIT;
nenhum fonte/driver/kernel é modificado por esta extração.

Resultado: 37 testes direcionados sob guarda offline passaram sem skips,
incluindo sete novos testes de parser/CLI e regressões SMP, clock, ARMPLL/CCF e
estabilidade. Comparação com a função anterior preservou JSON completo (inclusive
ordem das chaves) ou mensagem de recusa em 24 casos: capturas vazias/privadas,
releases, CPUs 0/4/63/64, timeout, retorno, entry, GIC, limites e requests repetidos.
Perfil sintético usa CPU100 e prefixos não K40S, com inferência ARM desabilitada.
CLI recusa binário/UTF-8 inválido/placa ausente e saída existente sem sobrescrever;
entrada intacta e flags de limitações verificadas. Sem boot/probe/ensaio físico.

## Seletores C compartilhados nas fixtures — 2026-10-28

Entrega host: remover a dependência de testes de bateria/netdev para selecionar
trechos C pinados nas fixtures de outros componentes. Aceite: texto selecionado
e erros equivalentes; nenhum teste/hardware importado para obter o helper;
modelos, flags e checks de hashes preservados. Sem ensaio no aparelho.

Origem MIT: helpers locais em `test_generic_adc_battery_status.py`,
`test_gen4m_netdev.py` e duplicatas upstream; extração para `tools/tests/support.py`.
Reusar seletores exatos existentes, sem introduzir parser C, libclang ou RE.
Linux/mainline, postmarketOS, MediaTek e Qualcomm são fontes dos trechos pinados,
não motivo para copiar uma implementação ou alterar o código selecionado.
Generated C derivado de fontes GPL permanece sob sua licença; helper Python MIT.

Manter separados o seletor por terminador e o contador de chaves: o segundo só
serve aos fontes revisados sem chaves em comentários/literais. Não alegar parser
genérico C nem reescrever ambos em um algoritmo supostamente equivalente.
Wrappers das APIs antigas continuam disponíveis; imports novos só usam suporte.

Resultado: 107 módulos ajustados, sete wrappers preservados. Comparação AST,
excluindo apenas imports e wrappers substituídos, confirmou corpos/fixtures
inalterados. Os sete helpers originais foram comparados aos novos em oito
entradas cada: 56 resultados/erros equivalentes, incluindo ausência de declaração,
terminador e fechamento. Importação dos 107 módulos sob guarda offline passou.
Quatro testes novos cobrem seleção exata, terminador curto, chaves/trailing comment,
erros e import do suporte sem testes de hardware ou leitura de configuração.

Suíte direcionada: 51 executados sem skips, 50 passaram e um recusou drift de
fonte externa antes de chamar o seletor. Fonte:
`module-workspaces/staging-wmt-lts-20261027-v1/common_main/core/wmt_lib.c` na raiz
de desenvolvimento; SHA256 observado
`b435b48b3a47be665ff9850f9828d400b8dcf764d1b73c6c4cd3d47c0aa898de`, esperado
`8c7c26b59774c23c8017f8bbeefabdb18a3982695eafe344e50da5a0922aa822`.
Reprodução com o helper original confirmou a mesma recusa, zero chamadas ao
seletor. Não atualizar pin nem modificar o workspace para fazer passar. Os outros
testes exercitam bateria, netdev, touchscreen, ADC, charger, CCF, I2C e BTIF em
fixtures host; não há ensaio físico nem qualificação do WMT com fonte divergente.

## Localização das fontes externas nos testes — 2026-10-28

Entrega host: substituir caminhos absolutos repetidos nos testes por raiz
nomeada configurável, sem alterar seleção de revisão, hash ou corpo das fixtures.
Aceite: caminho padrão idêntico, override explícito sem fallback quando inválido,
recusa de escapes relativos e preservação dos checks de conteúdo existentes.
Nenhuma busca automática de fontes, download, alteração externa ou ensaio físico.

Reusar pathlib/JSON da biblioteca padrão e `tools/tests/support.py` (MIT), sem
criar gerenciador de fontes ou ferramenta concorrente de build. A configuração
de laboratório/placa existente trata transporte e não deve ser carregada para
localizar fixtures host. Linux/postmarketOS/árvores MediaTek/Qualcomm continuam
fornecedores dos fontes pinados; não há código externo copiado nem necessidade
de RE. O resolver e o manifesto `manifests/test-sources.json` são MIT do projeto;
fontes/fixtures derivadas mantêm suas licenças anteriores.

Decisão: mapa explícito de raízes, padrão versionado e substituição via arquivo
`KPF_TEST_SOURCE_ROOTS`. Só a localização muda; nomes dos workspaces/componentes,
hashes e skips por ausência continuam nos testes específicos. Configuração não
é sandbox nem prova compatibilidade com outro SoC. Não misturar esta opção com
raízes de execução no aparelho, transporte ou recuperação.

Resultado: 78 expressões `Path` migradas em 66 módulos. Comparação AST antes/depois
com transformação inversa confirmou mudança somente nessas expressões e no import
do helper; preservados corpos, hashes, flags e skips. Importação dos 66 módulos
sob guarda offline e 38 testes direcionados passaram sem skips. Seleção inclui
BTIF DMA/reset, gen4m keys, FT5446, MT6357 ADC, bateria e cinco testes novos do
resolver; fontes reais pinadas e fixtures compiladas localmente, não no aparelho.
Override sintético muda o caminho de um consumidor real sem mudar seu hash;
configuração ausente/duplicada/inválida, raiz desconhecida e traversal recusados.
Patches exibidos pela suíte foram aplicados em diretórios temporários das fixtures;
nenhum fonte externo canônico ou componente do aparelho foi alterado.

## Executor KUnit e conjuntos declarativos — 2026-10-28

Entrega host: separar fontes, pins, patches, configuração e suites do mecanismo
de preparar/verificar/executar UML. Aceite: conjunto padrão preservado, outro
conjunto explícito sem editar o executor, rejeição de caminhos fora da raiz,
suite/caso/contagem incompletos e configuração com integração host proibida.
Não há boot ARM, acesso ao telefone ou nova entrega funcional no aparelho.

Reusar `tools/run-kunit-offline.py` (MIT), seu preparo isolado e helpers existentes
de extração/patch/hash, `run_group` e o `tools/testing/kunit/kunit.py` oficial do
Linux. Não criar runner de kernel ou parser KTAP paralelo. O JSON oficial continua
exigindo PASS exato e contagens sem skips/erros. Linux/postmarketOS e projetos
MediaTek/Qualcomm não oferecem a composição local de componentes, mas nenhum
driver/algoritmo dessas árvores precisa ser copiado para parametrizá-la.
RE não se aplica com fontes disponíveis. Arquivos novos do projeto são MIT;
fonte Linux permanece no archive/revisão/hash já fixados, sem relicenciamento.

Decisão: descritor JSON de dados, nunca código importado do usuário; mecanismos
de isolamento host são fixos e conjuntos só acrescentam restrições. O conjunto
padrão preserva nomes, hashes e ordem dos patches atuais. Workspaces novos
registram identidade do descritor; os anteriores só são aceitos pelo conjunto
padrão, com todas as verificações legadas mantidas. Não executar build amplo
para validar somente a extração de metadados e contratos.

Origem: definições literais do runner no worktree atual, incluindo alterações
anteriores do usuário. Migração mecânica por AST/literal_eval preservou mapas,
ordem dos patches, hashes e conjuntos de casos; a serialização ordena somente
nomes de casos antes sem ordem em sets Python. Nenhum fonte vendor foi alterado.
`portkit/core/kunit_sets.py`, `manifests/kunit/host-policy.json` e
`tools/tests/test_portkit_kunit_sets.py` têm licença MIT do projeto.

Resultado: 14 testes direcionados sob guarda offline, sem skips, incluindo as
oito regressões existentes. Segundo conjunto sintético de dois casos valida
seleção de versão/fontes/configuração, preparo/check e orquestração build/exec
com helpers/toolchain mockados, não execução real de UML. Negativos cobrem pins,
paths/symlinks, casos/contagens/arch/skips, isolamento fixo, drift de fonte e
descritor, além de recusa de adoção de workspace legado por outro conjunto.
`--help` funciona de fora da raiz. Nenhum archive Linux foi extraído nem kernel
compilado/executado nesta etapa; mensagens RUN/PASS sintéticas vêm dos mocks.

## Aplicação offline de overlays — 2026-10-28

Entrega host: compartilhar o mecanismo base + overlays independentes dos coletores
clock/watchdog, mantendo checksums, quantidade/identidade dos PCBs e comparação
dos snapshots nos consumidores. Não há entrega nem ensaio no aparelho nesta etapa.
Aceite: resultados equivalentes, falha de DTC/timeout propagada sem relatório,
arquivos temporários removidos, cada overlay aplicado à base original.

Reutilização: DTC/fdtoverlay já utilizado pelos dois coletores, executado pelo
`portkit.core.processes.run_bounded` existente; não implementar merge FDT próprio.
Origem local: loops de `collect-k40s-clock-evidence.py` e
`collect-k40s-watchdog-evidence.py`, base Git
`fa77817f5f3a49ce21ccfd2f734d154cfee57d6b`; extração MIT para
`portkit/core/dt_overlays.py`. Sem código externo copiado. Linux/libfdt oferecem
a operação estrutural, não a seleção de backup/PCB da placa. postmarketOS,
MediaTek e Qualcomm não tornam overlays ou hashes intercambiáveis; não importar
drivers/protocolos nem usar RE para uma operação já resolvida por DTC.
Escopo limitado a snapshots de arquivos; timeout continua 15 segundos por merge,
sem retry/fallback. Labels repetidos passam a ser recusados para evitar que uma
variante desapareça do relatório. Recursos e recuperação permanecem específicos.

Resultado: 32 testes direcionados sob guarda offline, sem skips. Seis testes
novos cobrem DTC real, aplicação independente, overlay inválido/alvo ausente,
labels ambíguos, timeout/falha do processo/callback, limpeza e saída faltante
sem reutilização de resultado anterior. Integração dos dois coletores usa
backup sintético e extração Android mockada, mantendo aplicação DTC e snapshot
reais: sete snapshots concordantes aceitos; variante divergente recusada;
inputs intactos e flags de limitação preservadas. Isso não revalida o backup
privado rev8 nem prova funcionamento no aparelho. Checksums e contagem legados
não foram flexibilizados; o teste existente de backup corrompido continua verde.

## Contratos DT: helpers comuns e contrato SECURITY_AO no perfil — 2026-10-28

Entrega host: extrair checks duplicados de células, compatible único, propriedades
exatas e status para uso independente de placa; mover o contrato SECURITY_AO
K40S para configuração e expor verificação offline por perfil. Aceite: mesmos
relatórios válidos e recusas dos consumidores; outra janela/células em fixture;
nenhuma inferência de address translation, IRQ trigger ou probe funcional.
Sem MMIO, alteração DT ou qualquer ensaio no aparelho.

Origem MIT: fontes existentes `collect-k40s-security-evidence.py`,
`collect-k40s-watchdog-evidence.py` e `collect-k40s-usb-evidence.py`, base Git
`fa77817f5f3a49ce21ccfd2f734d154cfee57d6b`. Helper novo
`portkit/core/dt_contracts.py` e CLI `tools/check-dt-contract.py` MIT, sem código
externo copiado. Reusar parse_fdt/libfdt, captura limitada, perfil e evidência
create-only existentes. Nenhum parser binário, driver ou schema alternativo.

Linux bindings/dt-schema continuam sendo a autoridade para o binding; o helper
apenas compara invariantes explícitas em um snapshot. Mainline/postmarketOS e
árvores MediaTek/Qualcomm não tornam endereços, células, IRQs ou IDs de clock
intercambiáveis. Não importar drivers de outro SoC nem usar RE para dados já
descritos no fonte. Política do watchdog (inclusive status apenas reportado) e
regras USB de clock/IRQ/FIFO permanecem nos consumidores, sem relaxamento.

Decisão: contador de células recebe valores explícitos; busca exige uma única
ocorrência por token de compatible, nunca substring. Status só é exigido quando
o consumidor já o exigia ou o contrato declara isso. Perfil novo declara bytes
exatos de propriedades, não transforma reg em endereço físico traduzido. CLI
com --board/--contract exige FDT de arquivo e publica só metadados/checks, sem
valores arbitrários. Contrato verifica também que o nó está no pai declarado;
esse check adicional recusa ambiguidade de encoding em outro barramento.

Proveniência SHA256 das fontes anteriores: security
`3a39b2d7dcf6cde43a29508db4ad983e59a82cac031a71297670ab56e82bd6e9`,
watchdog `7c7576452af2b34a23b10255a3e2ec05a02254dd29d31d09b3c5fbc9cf2245ac`,
USB `098389a6e6df9ad2411d97c7d71231d310f06e199159578ee2690fa00ebce4ae`.
Validação: 53 testes direcionados sob guarda offline; comparação diferencial de
21 casos contra os snapshots da base Git preservou JSON válido e recusas.
O vínculo adicional ao pai declarado é uma restrição nova, testada separadamente.
Após acrescentar essa asserção, os oito testes do módulo foram repetidos com
sucesso sob a mesma guarda. Preservados coleta, checksums, seleção de overlays
e caminhos físicos legados; nenhum deles foi executado no aparelho.

## Evidência de boot: filtro comum e seleção de nós no perfil — 2026-10-28

Entrega host: inspecionar FDT/iomem já capturados de outra placa sem SSH e sem
salvar identificadores/bootargs. Aceite: relatório K40S válido equivalente,
prefixos/nós do perfil separados do mecanismo, allowlist de propriedades fixa,
chosen excluído mesmo com seletor amplo, CLI create-only, ausência de transporte.
Não há coleta física nem autorização para executar o coletor SSH legado.

Origem MIT: `tools/collect-k40s-boot-evidence.py`, base Git
`fa77817f5f3a49ce21ccfd2f734d154cfee57d6b`, SHA256 anterior
`97c364ef2c5958602a80128de95c43cf7d0db19c58b744163b31f6a921c40427`.
Extrair somente `safe_snapshot` para `portkit/core/boot_snapshot.py` (MIT),
reusando libfdt por `portkit.core.devicetree.parse_fdt`, leitura limitada e
publicação create-only existentes. Não alterar parser legado exportado, comandos,
host/key defaults ou política SSH nessa etapa. CLI nova
`tools/inspect-boot-snapshot.py` é estritamente offline e não importa transporte.

Linux/libfdt/DTC já fazem parsing de DT e não devem ser substituídos por parser
próprio. O filtro reutilizado seleciona metadados em vez de reproduzir um dump
geral; postmarketOS e árvores MediaTek/Qualcomm não oferecem uma seleção de nós
universal e não justificam copiar probes/protocolos. RE é desnecessária com
fonte disponível. Nenhuma identificação de hardware é inferida só de compatible.

Decisão: `diagnostics.boot_snapshot` contém caminhos/prefixos K40S originais.
Propriedades exportáveis permanecem fixas no core; perfil não pode incluir
serial-number, bootargs ou calibração arbitrária. Excluir /chosen e descendentes
independentemente dos seletores. CLI exige arquivos FDT/iomem explícitos e
release de sintaxe limitada, reporta origem offline e não prova boot atual.
Wrapper conserva os rótulos de origem/limitação anteriores para seus consumidores,
inclusive snapshots estáticos de backup; strings de release desses callers não
serão reinterpretadas como kernel corrente. RAM sem ordem válida é recusada.

Resultado: filtro e CLI offline integrados, seletores K40S movidos ao perfil.
O corpo AST de `main` SSH e do parser legado foi comparado ao commit acima e
permanece igual. O relatório JSON legado foi comparado diretamente à função
original em 14 casos: um FDT sintético e seis overlays locais, cada um com
release normal e rótulo estático; bytes JSON iguais. Nada foi coletado por SSH.

Trinta e nove testes de snapshot/early-port/backup/libfdt/perfis passaram no
WSL sob `offline_guard` e `assert_no_transports`. Cinco casos novos cobrem outro
caminho de UART e RAM acima de 4 GiB, chosen/bootargs/serial/calibração excluídos,
recusa de seletores e intervalo inválidos, labels estáticos preservados,
create-only e impossibilidade de ampliar propriedades pelo perfil. CLI --help
passou fora da raiz. Nenhuma imagem, fonte de driver ou rotina de recuperação
foi alterada; arquivos de captura usados na equivalência permaneceram intactos.

## Android DT table v0: parser comum entre consumidores — 2026-10-28

Entrega host: retirar parsers de container Android duplicados de ferramentas
de backup/referência/LK, preservando suas APIs e mantendo seleção de PCB no
consumidor. Aceite: metadados e payloads válidos equivalentes; bounds/cabeçalhos
inválidos, versão não suportada e FDT inválido recusados; CLI de metadados sem
exportar DT bruto, sem overwrite e sem acesso ao aparelho. Não há entrega física.

Origem MIT: parser de `tools/inspect-android-backup-dt.py`, base Git
`fa77817f5f3a49ce21ccfd2f734d154cfee57d6b`, snapshot SHA256
`284df701c3525260fc2e5ae589f7e5fcd0f73771d1335d4a145f9d824aad0db6`.
Consumidor comparação antes deste incremento:
`049172e030ca94cf12148a1501650a94cbf5c72149de7e743f1594ea8586e8b3`.
Novo `portkit/core/android_dt.py`, CLI `tools/inspect-dt-table.py` e testes MIT,
adaptando o parser próprio existente, sem copiar código de terceiros.

Alternativa primária: AOSP libufdt/mkdtimg, header Apache-2.0
[`dt_table.h` no commit cb30f6426d4486d55e14ec952c374d7f06002df1](https://android.googlesource.com/platform/system/libufdt/+/cb30f6426d4486d55e14ec952c374d7f06002df1/utils/src/dt_table.h),
blob `831b80f782f59db32d35f176285cb238fe241d2f`, inspecionado. Não importar
licença/código C nem adicionar binário mkdtimg só para substituir o parser local
já utilizado. Não criar packer ou camada bootloader. libfdt continua validando
FDT, DTC continua compilando; parser de container não substitui esses frameworks.

Linux/postmarketOS e árvores MediaTek/Qualcomm podem consumir DTs, mas não
definem política universal de IDs/revisões/custom ou seleção PCB. Seus
protocolos físicos ficam fora desse parser de arquivo; ferramentas de RE não
são necessárias com fonte e formato disponíveis. Manter o subconjunto v0,
stride32 e payload FDT v17+ revisados; não alegar v1, compressão ou assinaturas.

Decisão: extrair o parser mais rigoroso, com limites e offsets originais,
substituindo apenas a validação FDT legada pelo adapter libfdt existente.
Wrappers preservam seus formatos list/tuple/generator para entradas válidas.
Leitores antes permissivos passam a recusar tabelas não revisadas, sem fallback
ou relaxamento de gates. CLI nova só relata header/entradas/hashes; não extrai
conteúdo privado nem escolhe entrada ativa, boot ou aplicação de overlay.

Snapshot do gerador LK antes da extração:
`000ce18e6485b6769071d02676c348378ec3b1d72bec966401bc786a3fd22a3e`.
Resultado: três consumidores migrados e CLI de metadados integrada. Os adapters
preservam list/tuples/generator e o parser compartilhado não contém configuração
K40S. O gerador exige agora o pylibfdt já usado pelo ambiente oficial; documentado,
sem fallback. A política LK e o corpo de geração de dtsi não foram alterados.

Trinta e dois testes direcionados de Android DT/backup/comparação/libfdt/core
passaram no WSL com `offline_guard` e `assert_no_transports`. Cinco casos novos
cobrem entradas múltiplas/aliases, metadados opacos, versões/limites/payloads,
adapters, recusa antes do primeiro yield, privacidade, entrada intacta e
create-only. Comparação direta com as três funções da revisão Git original na
tabela privada local disponível: seis entradas tiveram metadados/bytes iguais
em todos os adapters. Não foram encontrados localmente os dois containers da
referência rev7 nessa checagem; não declarar que foram revalidados.
CLI --help passou fora da raiz. Nenhum blob derivado ou DT de boot foi gerado,
nenhuma coleta/flash ocorreu e as imagens validadas permanecem preservadas.

## Comparação DT: mecanismo comum e seleção no perfil — 2026-10-28

Entrega host: comparar DTBs explícitos sem paths/placa fixos e mover a seleção
de candidatos da ferramenta histórica para o perfil. Aceite: canonicalização
DTC e diff anteriores preservados, parâmetros fora da placa aceitos sem fallback
K40S, import sem escrita, output existente recusado, falhas antes da publicação.
Nenhum DT é aplicado ao aparelho ou declarado compatível por ser igual ao backup.

Origem MIT: `tools/compare-reference-dt.py`, base Git
`fa77817f5f3a49ce21ccfd2f734d154cfee57d6b`. Reusar seus flags DTC, difflib e
comparações; novos helpers em `portkit/core/devicetree.py` e CLI
`tools/compare-dtb.py` são MIT. Sem parser DT novo: DTC/libfdt já disponíveis
continuam responsáveis pelo formato. O seletor de tabelas Android da ferramenta
histórica fica separado do comparador de blobs, sem ser chamado de formato de
placa Qualcomm/MediaTek genérico. Não adicionar bootloader ou backend físico.

Linux bindings/dt-schema validam contratos de hardware, enquanto DTC só fornece
a representação normalizada aqui: igualdade não é certificação de binding ou
comportamento elétrico. Fluxos postmarketOS e MediaTek/Qualcomm podem usar o mesmo
DTC, mas seus IDs/revisões/mapeamentos não são intercambiáveis. RE não é necessária
com árvores e toolchain existentes. Não implementar canonicalizador alternativo.

Decisão: flags `dtc -q -s -I dtb -O dts` preservados, subprocesso limitado via
helper existente e sem shell. Valores do seletor histórico vêm de
`diagnostics.reference_dt_comparison`; a CLI do par exige duas entradas explícitas
e saída privada nova. DTS/diff podem incluir identidade/calibração: não imprimir
ou publicar o conteúdo automaticamente. Endereços/partições/recuperação intactos.

Snapshot de origem confirmado SHA256
`12ded99637d6e627961ee0efa683f58feb6b86a8cb6f63d4f069f375a7ecf805`.
Resultado: comparador comum e CLI do par integrados; lote histórico importa sem
IO e lê defaults/mapeamento do perfil. Seleção sintética de ID7 com paths e
candidatos diferentes passou, sem editar o core nem depender do mapa K40S.
Canonicalização comparada diretamente à função da revisão original: três
fixtures distintas deram DTS idêntico. A validação libfdt v17+ e deadlines
agora precedem DTC; formatos não revisados são recusados em vez de fallback.

Quarenta e dois testes de comparação/DT/libfdt/backup/perfis/core passaram no
WSL sob `offline_guard` e `assert_no_transports`. Seis casos novos cobrem import
sem escrita, defaults antigos, ordem vs bytes, diferenças reais, privacidade/
create-only, entradas inválidas, timeout, lote com outro perfil e ambiguidade/
escape de paths. As duas CLIs --help passaram fora da raiz do projeto. Nada foi
aplicado a DT, imagem de boot ou dispositivo; recuperação permaneceu intacta.

## Fixtures C host: executor comum sem política de placa — 2026-10-28

Entrega host: extrair o ciclo repetido de fonte temporária/compilar/executar dos
testes de charge-state, battery-i2c-refresh e gen4m netdev para suporte comum.
Aceite: mesmas fontes, flags, asserts, sanitizers e pthread quando usados;
falhas/timeout propagados sem retry ou fallback; limpeza das fontes/binários
temporários e guarda offline preservada. Nenhuma entrega no aparelho.

Origens locais MIT conforme REUSE.toml, snapshots anteriores:
`tools/tests/test_k40s_charge_state.py` SHA256
`eb2906ded827fe9b816a46dc7a40efcbb128d6513d3fbad2aabed72df79697fd`;
`tools/tests/test_k40s_battery_i2c_refresh.py`
`57e17a320712ecac8c01ad3c1cf90ff5fdf27cc3746e8bec74afd218c165c18c`;
`tools/tests/test_gen4m_netdev.py`
`a8cb675f691f03959ef95649452690191f3024fa012b8206ef8de4618af8d2f4`.
Base Git do projeto `fa77817f5f3a49ce21ccfd2f734d154cfee57d6b`; fontes C/patches
vendor e seus hashes continuam pertencendo a cada teste, não ao helper MIT.

Reuso: `tempfile`, compilador host e `portkit.core.processes.run_bounded` já
existentes, sem nova dependência/executor externo. Linux KUnit/kselftest continuam
preferidos para testes kernel: este helper só reduz duplicação nas fixtures host
existentes e não é substituto dos frameworks. PostmarketOS/MediaTek/Qualcomm/RE
não precisam fornecer protocolo ou BSP para compilar uma fixture host; não
transformar os doubles específicos em implementação genérica de hardware.

Decisão: `tools/tests/support.py:run_c`, flags obrigatórias e explícitas, sem
shell/seleção automática de compiler, sem skips/retries internos. Reusar o limite
de 60 s por subprocesso já definido por `run_bounded`; defaults 30 s compilação,
10 s execução, como no caso gen4m. Os dois wrappers anteriores sem timeout passam
a ter essas cotas, sem alterar caminho de sucesso nem relaxar verificações.
O helper não é sandbox para código C hostil e não promete controle de netos;
estas fixtures revisadas não geram processos reais em seus casos de hardware.

Resultado: três consumidores migrados, preservando código C, preparações de
patch, hashes das fontes, flags `-Werror`, pthread e UBSan. Dezoito testes
direcionados passaram no WSL sob `offline_guard`, seguidos de
`assert_no_transports`. Os seis casos novos incluem execução C real e validação
de argv, falha de compilador, exit não zero, timeout real e simulado, limpeza
temporária e recusa de deadlines/argv inválidos. Não houve skip nesses casos.
Nenhum backend de transporte, driver, controle de carga ou recuperador mudou.

## Kconfig: leitura/comparação compartilhadas e verificação offline — 2026-10-28

Entrega host: parser literal `.config` comum aos consumidores existentes e
verificação de fragmentos independente de placa/arquitetura. Aceite: equivalência
dos dois parsers, ordem dos fragmentos, nenhuma aceitação de y/m/string ausente
ou alterada, omissão de n invisível tratada como antes, saídas create-only sem
expor valores de configuração privados. Não há build, configure ou acesso físico.

Reuso: parser e comparação existentes de `tools/kernel-workspace.py` e parser
de `tools/audit-k40s-zimage-layout.py`, MIT conforme REUSE.toml; base Git
`fa77817f5f3a49ce21ccfd2f734d154cfee57d6b`. Adaptar para
`portkit/core/kconfig.py` (MIT), sem resolver dependências nem modificar arquivos
de configuração. CLI nova `tools/check-kconfig.py` compõe captura UTF-8 limitada
e evidência create-only já existentes. Sem dependência Python adicional.

Linux `scripts/kconfig` continua sendo a autoridade para símbolos/dependências;
merge_config.sh/olddefconfig permanecem no build. Kconfiglib seria um resolver
adicional desnecessário para comparar valores já emitidos: não importá-lo nem
reescrever o Kconfig. PostmarketOS e árvores MediaTek/Qualcomm também usam esse
formato, mas seus símbolos/defconfigs não se tornam equivalentes: comparar
somente os requisitos explicitamente fornecidos. Ferramentas RE não participam
dessa leitura de texto. Não confundir configuração correta com driver funcional.

Decisão: preservar valores raw (inclusive aspas/escapes), n desabilitado e
última ocorrência; o wrapper zImage conserva sua view antiga sem aspas. Extrair
também a comparação já usada no workspace, com a mesma falha do primeiro
requisito divergente. A CLI genérica não precisa de --board: suas entradas são
um .config e fragmentos explícitos, sem qualquer default de placa. Relatório
exporta nomes dos símbolos divergentes e identidades dos arquivos, não valores.

Identidades confirmadas antes da extração: workspace
`fd0caf5377636c11c5753da9df89ed1da35dd57b66ec6fd980319b338c36d345`;
auditoria zImage
`d9a2684406702f640de86af32497879d6e7c8b5be1fce599f2bc8d9920c49109`.
Referência Linux 6.18.58 `scripts/kconfig/merge_config.sh`, GPL-2.0,
SHA256 `fecdeb0747c88f818f0d5d39333b948cdf83d9aca11c422253da17f5cc36e6f1`,
inspecionada; nada copiado/invocado. Seu fluxo de merge/configuração não é
substituído por essa comparação read-only de arquivos já emitidos.

Resultado: ambos os consumidores usam o core. Comparação direta das funções do
commit original confirmou igualdade em sete entradas por view, inclusive
duplicatas, desabilitados, strings, linhas ignoradas e CRLF. Cinquenta testes
direcionados (Kconfig/workspace/core/layout) passaram no WSL com `offline_guard`
e `assert_no_transports`; os testes de patch usam apenas fixtures temporárias.
Cinco casos novos cobrem raw/escape, faltas relevantes, erro inicial preservado,
wrappers, fragmentos em ordem, configurações ARM64/RISCV sintéticas, privacidade
e recusa de sobrescrita/entrada inválida. CLI --help também passou fora da raiz.
Nenhum build, configuração, driver ou fluxo de recuperação foi executado.

## Sessões offline: layout no perfil, decoder compartilhado — 2026-10-28

Entrega host: decoder de conjunto de capturas com nomes, tamanhos e offset do
console declarados pela placa, sem presumir LG, ATF ou quatro arquivos. Aceite:
CLI K40S anterior equivalente em arquivos/relatório e recusas; perfil sintético
com outra composição; variantes de tamanho somente quando declaradas; falhas
antes da criação de saída e diretório existente preservado. Sem entrega física.

Origem MIT: `tools/decode-k40s-session-logs.py`, base Git
`fa77817f5f3a49ce21ccfd2f734d154cfee57d6b`, SHA256 anterior
`acc71d361a1a092db7067c0165a404a0c0ded226ba9c74fc3cd74e3d6778af5d`.
Novo `portkit/core/session_logs.py` e `tools/decode-session-logs.py`: MIT,
adaptação/composição da lógica existente, sem código externo copiado e sem
dependência nova. Codec, leitura binária exata, loader de placas e helpers de
teste KPF existentes serão reaproveitados, não duplicados.

Linux ramoops/pstore e a fonte/assinatura/rotação foram auditados na seção
console abaixo. Coleta nativa e postmarketOS não decodificam estes conjuntos
locais por prefixo; não criar coletor para resolver organização offline.
MediaTek/Qualcomm e ferramentas RE anteriormente triados não participam deste
formato de arquivos: não transportar endereços/protocolos da placa para o core.
Recortes ASCII de anéis ATF/printk continuarão explicitamente desordenados,
sem alegação de reconstrução de ring, correlação de boot ou retenção.

Decisão: `diagnostics.session_logs` declara capturas, tamanhos, variantes
permitidas, zona console e fontes de texto desordenado. Formato/assinatura do
console usam `diagnostics.ramoops_console`, sem segunda cópia desses parâmetros.
Validar nomes, limites, referências e faixa inteira da zona antes de ler; reusar
leitura exata limitada. CLI genérica exige `--board`; wrapper K40S conserva
posicionais e `--logbuf-size` com as duas escolhas antigas. Nenhum offset é
descoberto por heurística. Limites host por captura/conjunto não são elétricos.

Resultado integrado: core e CLI genérica sem nomes/offsets K40S; perfil contém
os dados originais e wrapper mantém posicionais, duas escolhas de logbuf,
mensagem final, nomes de saída e formato legado. O teste de compatibilidade
confere bytes completos do JSON e de todos os arquivos decodificados, além de
entradas intactas. Fixture independente usa duas capturas (`memory`/`trace`),
outro tamanho/assinatura/offset e não exige ATF.

Validação WSL: 49 testes de sessão/core/perfis/capturas/ramoops passaram sob
`offline_guard`, com `assert_no_transports`; os dois testes subprocesso da CLI
legada também passaram. Os oito casos novos cobrem composição alternativa,
variantes, referências inválidas, limites da zona (inclusive fim exato), teto
host, entrada final ausente, saída existente e relatório legado byte-idêntico.
CLI `--help` executada fora da raiz. Não executar a suíte legada via a guarda
sem revisão: seus testes subprocesso não fazem parte da allowlist segura.
Nenhum transporte foi aberto nem houve alteração em coletor/boot/recuperação.

## Console ramoops: separar formato de layout LG — 2026-10-28

Entrega offline: reutilizar a decodificação do console com tamanho/assinatura
explícitos e CLI selecionada por placa, sem inferir layout de RAM. Aceite:
rotação e recusas antigas preservadas, outro tamanho/assinatura em fixture,
ECC não suportado recusado, entrada intacta e nenhuma sobrescrita. Não há nova
entrega no aparelho, coleta física, escrita em RAM ou autorização de boot.

Origem MIT: `tools/k40s-pstore-layout.py`, base Git
`fa77817f5f3a49ce21ccfd2f734d154cfee57d6b`, SHA256 local anterior
`aa988e72e069d8036c8b7cfa58eb7f3456e932c5db8bf19235940c75e344bf9e`.
Referência disponível Linux 6.18.58 `fs/pstore/ram_core.c`, GPL-2.0-only,
SHA256 `f2aa18da063598873bae44361162717b7d468e61c5861eed50e7bbf8ca6fbbb7`:
cabeçalho sig/start/size, assinatura PERSISTENT_RAM_SIG xor tipo da região e
ordem de cópia de `persistent_ram_save_old`. Não copiar C nem supor que a
assinatura base vale para todo tipo/firmware/endian. Novos helpers e CLI são
adaptação do decoder MIT existente; dependem apenas da biblioteca padrão.

Reuso: pstore/ramoops nativo continua responsável pela coleta no Linux;
deviceinfo/fluxos postmarketOS e protocolos MediaTek/Qualcomm não substituem a
identificação da zona no dump. As alternativas e ferramentas de RE auditadas
anteriormente não são necessárias com esse fonte disponível. Não implementar
ECC, scanner heurístico, reconstrução de anéis ATF/printk ou leitura física.
O layout LG de duas regiões NÃO é layout upstream genérico: conservar offsets,
opt-ins e recuperadores específicos, extraindo apenas o codec de uma zona.

Decisão: `portkit/core/ramoops.py` com assinatura/tamanho obrigatórios e ECC0;
wrapper LG mantém relatório/recusas anteriores. `diagnostics.ramoops_console`
declara somente o formato de uma zona já extraída, sem endereço físico. Reusar
capturas/evidências KPF para a CLI `decode-ramoops-console.py --board ...`.
Adicionar leitura binária exata limitada ao helper de capturas existente;
limite host de 16 MiB, não limite de hardware. Não reclassificar uma captura
antiga como boot atual nem comprovar retenção/reset pela decodificação.

Resultado: codec e CLI integrados, perfil K40S com a assinatura/tamanho atuais;
wrapper LG e consumidores PWRAP/sessão preservados. Comparação direta com a
função original do commit acima (SHA confirmado): oito casos de buffer vazio,
parcial, cheio, rotação e erro produziram bytes/metadados ou erros idênticos.
Regressão direcionada de recovery/pstore/PWRAP/sessões mais testes novos:
34 casos passaram no WSL. Core/perfis/capturas/ramoops sob a guarda offline:
41 casos passaram e `assert_no_transports` não encontrou transportes.
Os seis novos casos cobrem outro tamanho/assinatura sintéticos, cabeçalhos,
ECC, leitura exata com crescimento/encolhimento, política e saída create-only.
Nenhum driver, coletor físico, endereço de RAM ou recuperador foi modificado.

## Generalização continuada: capturas, CPU lists e suporte de teste — 2026-10-28

Pedido do usuário: continuar procurando e extraindo lógica reutilizável. Entrega
somente host: análise offline de estabilidade selecionada por `--board`, leitor
de captura e parser de CPU lists sem nome de aparelho, e loader de ferramentas
para testes sem importar outro módulo de testes K40S. Aceite: resultados legados
preservados, texto inválido/grande e perfil incompleto recusados, publicação
create-only e ausência de transportes. Nenhuma entrega ou ensaio no aparelho.

Origem local MIT: `tools/analyze-k40s-smp-logs.py` após a primeira extração,
SHA256 `7e1c1276eeb7a5535493933fe1e13c6690a8e7ad586354cb46f930a7945ce936`;
base Git `fa77817f5f3a49ce21ccfd2f734d154cfee57d6b`. Loader já existente em
`tools/tests/test_k40s_early_port.py` e duplicado nos testes de boot/USB. Novos
arquivos `portkit/core/captures.py`, `portkit/core/cpulist.py`,
`tools/analyze-stability-log.py` e `tools/tests/support.py` são MIT, sem código
externo importado; origem/licença dos arquivos de teste conforme REUSE.toml.
Mudança pequena, sem dependências além da biblioteca padrão Python existente.

Reuso preferido: `pathlib`, `hashlib`, `importlib.util`, loader JSON de placas,
parser de estabilidade e publicação atômica `write_evidence` já existentes.
Não criar novo formato de teste/executor. Linux kselftest/KTAP e deviceinfo
postmarketOS foram comparados na seção anterior: não decodificam os relatórios
legados nem substituem o perfil já usado aqui. O parser de CPUs mantém o
subconjunto decimal `N,N-M`; não reivindica toda sintaxe bitmap/cpulist Linux.
Protocolos MediaTek/Qualcomm e ferramentas abertas de RE não participam de leitura
de arquivos host/importação Python; manter suas implementações já auditadas e
não inferir compatibilidade de hardware a partir deste código genérico.

Justificativa do código novo: extrair as implementações existentes e compor uma
CLI com `--board` explícito, sem exigir ATF ou aceitar parâmetros que alterem o
perfil durante o comando. Os wrappers legados mantêm nomes e limites. Leitura
do arquivo será limitada também no `read`, não apenas no tamanho prévio. CCF,
PLL, semântica ATF/ARM e formato LG A/B ficam fora do core; não generalizar por
mera troca de nome. Helpers de teste não carregam transporte por conta própria,
mas não são sandbox para scripts hostis: manter a guarda offline existente.

Segundo incremento de suporte: mover também a fixture FDT v17 existente do
teste early-port para `tools/tests/support.py`, sem alterar seus bytes. Ela
apenas fabrica árvores mínimas em memória para testes; não é parser nem gerador
de DT de boot. DTC/libfdt continuam obrigatórios nos testes e ferramentas que já
os usam. Reescrever a fixture com outro encoder introduziria dependência e
mudança de representação sem necessidade; conferir a saída contra libfdt e
conservar os casos negativos existentes. Remover imports entre testes de placa
apenas onde eram usados ROOT/module/fdt, sem mover fixtures de hardware.

Resultado integrado: CLI genérica com placa obrigatória, evidência create-only,
leitor limitado no read e CPU list com limite explícito. ROOT/loader/fixture
compartilhados substituem os imports do teste early-port; seus aliases antigos
foram mantidos. Comparação direta com as funções do commit acima: dez entradas
CPU (incluindo erros e suas mensagens) iguais e três fixtures FDT byte-idênticas.
A fixture compartilhada também foi decodificada pelo adapter libfdt existente.

Verificação WSL: regressão dos módulos migrados executou 150 testes, sem falhas,
com dois skips existentes; não houve execução física. Regressão direcionada de
core/perfis/capturas/estabilidade sob `offline_guard` executou 39 testes sem
falhas, seguida de `assert_no_transports`. Casos novos cobrem UTF-8 inválido,
NUL, limite exato, crescimento depois do stat, perfil alternativo sintético,
política ausente, relatório incompleto e recusa de sobrescrita. Catálogo AST
atualizado sem importar os testes. CLI `--help` também executada fora da raiz
do projeto; defaults de execução física, drivers e recuperação não mudaram.

## Generalização inicial: parser offline de estabilidade — 2026-10-28

Pedido explícito do usuário: iniciar reutilização de testes/ferramentas entre
aparelhos. Escopo deste incremento: extrair o parser existente, não o executor
C, watchdog, transporte, carga ou recuperação. Nenhuma nova entrega física.
Aceite: mesmos eventos/resultados K40S e mesmas recusas, perfil alternativo
sintético sem dependência K40S, configurações inválidas recusadas.

Origem: `tools/analyze-k40s-smp-logs.py`, revisão base Git
`fa77817f5f3a49ce21ccfd2f734d154cfee57d6b`; conteúdo local antes da extração
SHA256 `d6003147c7d6ed56bc8468cd3a9933b3264680331b0367351d285e59ed14389d`.
MIT conforme REUSE.toml; novo `portkit/core/stability.py` também MIT, sem código
externo copiado. Dependências: biblioteca padrão Python e loader de perfil já
existente. Esforço limitado a parser, perfil e regressões; sem probe/remove.

Reutilização comparada: [kselftest Linux](https://www.kernel.org/doc/html/v6.9/dev-tools/kselftest.html)
e [KTAP v1](https://www.kernel.org/doc/html/v5.17/dev-tools/ktap.html) já são
os formatos preferíveis para novos testes kernel, mas não interpretam as
capturas legadas `*-STABILITY: ... value=...`. Não substituir esses frameworks
por executor novo nem converter evidência antiga em um pass KTAP fictício.
[deviceinfo postmarketOS](https://docs.postmarketos.org/pmaports/main/deviceinfo-reference.html)
organiza dados de aparelho, mas não define este protocolo de estabilidade;
reusar o perfil JSON KPF existente evita dependência de pmbootstrap. Versões de
documentação são referências, não código importado/licença incorporada.

MediaTek/Qualcomm e ferramentas abertas de RE já triados nesta matriz não
oferecem substituto para esse protocolo local: acesso a firmware/hardware não
é necessário para analisar texto. Não copiar política de watchdog MediaTek para
Qualcomm nem declarar compatibilidade elétrica. O prefixo, CPUs, duração e faixa
esperada do relatório pertencem ao perfil da placa; endereços/CCF/ATF continuam
no analisador específico. Justificativa do helper: separar mecanismo já existente
dos quatro parâmetros de aceite, preservando teto de eventos e avisos de limite.

Resultado: extração integrada, parâmetros em `boards/k40s/profile.json`, wrapper
legado preservado. Comparação direta com a função da revisão acima (SHA
confirmado igual ao snapshot local) deu saída integral idêntica em 120 variações
de CPUs, duração, timeout e marcadores de falha/fim. Quatro testes novos e 28
regressões de estabilidade/SMP/perfis passaram no WSL; incluem supervisor C com
tempo virtual e falhas de watchdog, sem dispositivo. Os quatro testes novos
também passaram sob `offline_guard` e `assert_no_transports`. Catálogo AST e
allowlist offline atualizados, sem ampliar a guarda. Não houve ensaio físico,
mudança do executor C, firmware, limites de carga ou mecanismo de recuperação.

Navegação: [código e candidato atuais](current-state.md) e
[raízes dos patches de staging](../patches/kernel/staging/README.md).
As seções abaixo preservam decisões e resultados por incremento; uma decisão
prévia ou compilação isolada não é aceite no aparelho.

## MPU24: resultado offline do incremento — 2026-10-28

Implementados os deltas `wmt-wifi-emi-transaction-v1.patch` e
`gen4m-wifi-emi-transaction-v1.patch`, sobre as fontes integradas preservadas.
Mutex cobre validar25, verificar24 fechado, abrir24, callback delimitado,
barreira `mb()` e reproteção24. Falha de fechamento prevalece, erro após escrita
fica latched; não há rollback permissivo. Calibração e coredump legados não
foram migrados, portanto o conjunto continua bloqueado para ativação.

Compilações ARM/MODPOST passaram nos logs
`work/wmt-wifi-emi-transaction-build-20261028-c.log` e
`work/gen4m-wifi-emi-transaction-build-20261028-a.log`. Oito testes direcionados
passaram em `work/wifi-emi-transaction-regression-20261028-a.log`, incluindo
equivalência do encoding LG real, concorrência, falhas de abertura/fechamento,
readback, latch e regressões25/29/probe/genpd/XO. Modelo não comprova SIP/MPU
físico. Identidades dos módulos e próximos gates estão no mapa atual; cápsula
BTv14, kernel LG4.9 e mecanismos de recuperação permanecem preservados.

## MPU24: transacao delimitada de firmware — decisao previa2026-10-28

Entrega visada: download Wi-Fi com janela AP controlada do inicio ao fim.
Reusar mutex/transporte/checks SIP25/29 no backend mt6765 existente. Helper
locked privado permite apenas perfis24/25/29. Perfil24 reusa politica LG
plat_priv.c: offset0x177000/tamanho0xF9000, encoding64KiB efetivo cobre
0x170000..0x26ffff (a ampliacao0x7000 e herdada LG). Fechado APC0=0x00b6da2d,
aberto APC0=0x00b6da28, APC1=0x00b6db6d; dom2 CONNSYS permanece permitido,
dom0 AP somente aberto. Aceitar apenas slot zero para inicializar fechado,
estado esperado ou a politica oposta conhecida no mesmo intervalo. Nao
sobrescrever outro intervalo/politica nem oferecer toggle aberto publico.

API minima WMT wifi_emi_access(base,operation,context): conferir reserva comum,
inicializar/verificar24 fechado, abrir, executar operacao sincrona delimitada,
reproteger sempre, inclusive se operacao retorna erro. Mutex mantido em todas
as fases; falha de reprotecao prevalece sobre erro da operacao e latch impede
novas chamadas apos falha SIP. Callback nao pode chamar API MPU/WMT nem dormir
aguardando outra transacao; no download executa apenas memcpy_toio validado.
Nao manter locks pendurados entre tasks, usuarios ou start/stop assincronos.

Justificativa dos pequenos helpers/contexto novos: adaptar copia LG existente
a lifetime delimitado que o bool off/on nao oferece; sem framework universal,
novo driver ou diagnostico. Core gen4m conserva validacao/claim/map/unmap,
backend WMT conserva transporte/politica SoC; header publico GPL minimo ja
existente. API GPL compativel com fontes LG GPLv2/dualGPLv2-BSD identificadas;
Linux6.18.58/SIP32/alternativas mainline/TF-A/pmaports/MediaTek/Qualcomm e
hashes de origem constam nas auditorias MPU25/29. Reusa caminho mais completo,
sem RE nem importar arquitetura de outro SoC. Snapshot integrado em
work/wifi-fw-transaction-backup-20261028-v1.

Aceite offline: encoding24 comparado a politica LG real, concorrencia sem
janelas simultaneas, nenhum callback em erro de abertura, fechamento em erro
do callback e latch sob erro de reprotecao; regressao25/29 e build ARM. Nao
e autorizacao/validacao SIP fisica. Calibracao e coredump WMT ainda precisam
migrar ao contrato antes de carga: nao ativar o conjunto intermediario, pois
esses consumidores legados ignoram erro bool e podem acessar24 fechado.

Correcao fundamentada pelo teste contra LG: SET_ACCESS_PERMISSION usa
((unsigned int) lock <<31) sem parenteses no parametro. Com argumento
enable ? LOCK : UNLOCK, o ternario resulta em1 quando enable, nao BIT31;
OR com d0=FORBIDDEN5 deixa APC0 fechado0x00b6da2d, aberto0x00b6da28.
Primeira versao do porte assumia LOCK permanente0x80b6da2d e falhou no teste
de equivalencia (log-b). Corrigido o PORTE, nao o esperadoLG/teste: preservar
bits realmente emitidos e AP proibido fora da transacao. Nao habilitar LOCK
permanente24 sem demonstrar reabertura/recuperacao no firmware instalado.
25/29 usam LOCK constante, continuam com BIT31 e nao foram afrouxados.

## Gen4m firmware MPU: contrato de erro antes de abrir24 — decisao previa2026-10-28

Bloqueio concreto encontrado ao integrar24: kalSetEmiMpuProtection e void,
fallback weak apenas avisa, download sempre copia/retorna sucesso; mesmo
toggle e usado em calibracao e start/stop assincrono de coredump WMT. Nao
ativar unlock nativo sem ownership da janela completa e propagacao dos erros
nesses consumidores. Primeiro incremento: adaptar API LG existente a int
__must_check, fallback EOPNOTSUPP, retornar errno do provider legado onde
selecionado, hif callback retornar erro e download copiar somente se abertura
suceder, retornar falha se reprotecao falhar e limpar claims/mappings em ambos.
Nao adicionar backend paralelo, novo diagnostico ou callback framework.

Reuso: mesmo encoder/transporte Linux6.18/LG e alternativas mainline/TF-A/
pmaports/MediaTek/Qualcomm auditados nas secoes MPU25/29; este incremento
altera apenas contrato de retorno e fluxo de erro, sem novo provider ou SIP.
Origem LG gen4m dualGPLv2/BSD, hashes originais fw_dl/gl_kal/gl_kal.h/axi e
plat_priv ja registrados. Snapshot integrado imutavel em
work/gen4m-fw-mpu-errors-backup-20261028-v1, sem modificar4.9. API de firmware
nao e compartilhada com MPU DMA29 ja checked; nao regredir29 para resolver24.
Aceite: falha ao abrir sem copia, falha ao fechar nunca sucesso, limpeza CPU
preservada e compilacao ARM. Estado MPU parcial ainda requer latch/reboot do
backend futuro; cleanup de mapping nao comprova restaurar politica fisica.

Continuacao obrigatoria da entrega: transacao nativa24 serializada abrangendo
abertura/copia/reprotecao, integrar calibracao e tratar coredump assincrono sem
janela solta. Esta preparacao de erro nao resolve24 nem autoriza carga/RF.

Resultado: gen4m-fw-mpu-errors-v1.patch muda API para int __must_check,
weak EOPNOTSUPP e hif callback deixa de mascarar errno. Download real nao
copia quando abrir falha e retorna WLAN_STATUS_FAILURE se fechar falha;
claims/mappings CPU sao liberados em ambos. Teste existente foi ampliado com
EOPNOTSUPP/EACCES/EIO/EBUSY nas duas etapas, sem alterar seus criterios de
sucesso/bounds/dados/versionamento. No erro de reprotecao, permite somente
cleanup CPU com falha explicitamente injetada e exige retorno falho; nao
considera a MPU restaurada. Fixture seguinte simula estado novo, nao recovery
fisico. Passou ASan/UBSan/-Werror em
work/gen4m-fw-mpu-errors-host-20261028-a.log, patch reproduzido com fuzz0
apos fw-loader originalLG. Nao e teste de firmware/MPU instalado no aparelho.

Build ARM/MODPOST passou work/gen4m-fw-mpu-errors-build-20261028-a.log;
wlan_drv_gen4m.ko SHA256
0ae13b211a62537f55c48feaab22071af516f9ca6075fd749ed33ed484766769,
release6.18.58-k40s-nativewifi1-NOT-FOR-FLASH. Fonte canonico/copia conferido
por SHA256; baseline privado sincronizado. nm confirma firmware MPU ainda
weak W (agora falha), DMA MPU forte T preservado. WMT/provider25/29/API publica
WMT inalterados, portanto nao repetir esses builds. Branch initWlan sob
CONFIG_MTK_EMI ainda ignora retorno; nao selecionada no candidato. Nao ativar
esse config para contornar24; __must_check deve impedir ignorar erro em build.

Proximo bloqueio tecnico: booleanos off/on independentes nao garantem exclusao
entre download, calibracao e coredump; cal WMT ainda ignora errno e restore
retorna void. Integracao nativa deve oferecer operacao delimitada sob a mesma
exclusao MPU (abertura/copiar/reproteger, sem lock deixado solto entre tasks),
propagar falha antes de IO/power-on e nao permitir que coredump assincrono
deixe a janela aberta. Nao implementar apenas unlock por SIP num callback
bool e considerar24 resolvida. DT/ICC/panel/reset continuam gates. Nenhuma
operacao fisica nem alteracao da capsulaBTv14/firmware stock.

## Wi-Fi DMA MPU29 checked — decisao previa2026-10-28

Entrega visada: buffers/rings PDMA na reserva Wi-Fi3MiB protegida, sem publicar
mappings se MPU falhar. LG region29 usa exatamente permissoes da CONNSYS25
(AP/domain0 e CONNSYS/domain2 permitidos, demais FORBIDDEN5, LOCK grupo0).
Reusar transporte/readback/latch SIP32 ja portado, com helper privado restrito
a25/29 e tamanhos4/3MiB. Nao duplicar transporte no gen4m nem criar provider
MPU generico. Novo export GPL WMT especifico DMA recebe device/base/size,
confere phandle nomeado wifi do proprio consumidor, compatible/no-map/nao
reusable/enabled, reserva exata, alinh16MiB/fim32 e nao sobreposicao CONNSYS.
Confere regiao25 antes de29; nao altera a politica25 para satisfazer o Wi-Fi.

Header publico minimo vendor-api/mtk_emi_native.h GPL-2.0-only separa a API
do backend; parametro WMT_API_ROOT no Makefile gen4m aponta este header sem
importar headers privados/plataforma WMT. Caller kalSetDrvEmiMpuProtection
passa device, retorna int; fallback weak retorna EOPNOTSUPP, nao sucesso com
aviso. AXI libera apenas claim CPU se protecao falhar, sem mapear/alocar/
publicar pool. Politica MPU permanece; nenhum CLEAR/unlock na limpeza.

Auditoria SIP25 acima fixa origem/revisao/licenca Linux6.18.58/LG e compara
mainline/TF-A/pmaports/MediaTek/Qualcomm; mesmas alternativas para29, cuja
compatibilidade vem do mesmo mpu_v1 e politica LG plat_priv.c dualGPLv2/BSD.
Sem nova necessidade de RE. Snapshot integrado dos arquivos afetados em
work/wifi-dma-mpu-backup-20261028-v1, fontes4.9 preservadas. Justificativa:
extensao pequena do fornecedor existente e erro checked no consumidor.
Aceite offline: encoding29 identico LG, DT invalido/MPU falho sem mappings,
claims liberados sob erro, comportamento25 preservado e MODPOST com export
real. Nao prova firmware instalado/LOCK/DMA e nao autoriza carga/RF/flash.
Lifetime do device WMT/concorrencia de reset, firmware24 e coredump assincrono
continuam gates; dependencia de modulo nao e prova de lifetime de dispositivo.

Resultado2026-10-28: wmt-wifi-dma-mpu-sip32-v1.patch e
gen4m-wifi-dma-mpu-checked-v1.patch integrados, fontes canonicas/copias
conferidas byte a byte por SHA256. Teste executa backend/provider/bridge reais
e politica DMA original LG (plat_priv.c original dual GPLv2/BSD SHA256
8580f2615efb33fd3ed3042ab8309ccac4b3c24c9c75110e2d7eafaae5c74509),
com encoder mpu_v1 original ja identificado e doubles OF/SMCCC. Verifica
identidade das duas escritas29, politica25 inalterada quando ja configurada,
estado29 ja protegido sem writes, DT/campos invalidos recusados antes de SIP,
overlap/claim diferente recusados, erros nas duas escritas e divergencias nos
quatro readbacks com latch. Fallback weak retorna EOPNOTSUPP. Passou
work/wmt-wifi-dma-mpu-host-20261028-b.log; log-a foi falha do typedef ausente
no double, corrigida sem suprimir warnings.

Alocador AXI real passou errosMPU EIO/EOPNOTSUPP/EBUSY/EACCES com exatamente
um claim/liberacao CPU e zero mappings/publicacao; sucesso e falhas parciais
de mapping preservam cleanup, sem tentar apagar politica MPU. Reusa doubles
do teste de pool existente, geometria reduzida (nao prova capacidade real).
work/gen4m-dma-mpu-gate-host-20261028-a.log. Backend25 foi reexercitado apos
extrair helper comum, incluindo tres bases/erros/readbacks anteriores; probe,
genpd/XO afetados pela identidade do fonte tambem passaram, com pins exatos
atualizados sem relaxar checks. work/wifi-dma-mpu-regression-20261028-a.log.

Builds ARM/MODPOST exit0: work/wmt-wifi-dma-mpu-build-20261028-a.log e
work/gen4m-wifi-dma-mpu-build-20261028-a.log. Export GPL real
mtk_wcn_consys_wifi_dma_mpu_protect na tabela WMT e import no gen4m, cujo
kalSetDrvEmiMpuProtection agora e simbolo forte T, nao fallback W. Makefile
gen4m requer WMT_API_ROOT apontando src/wmt para header vendor-api nativo;
manter esse parametro em builds futuros, sem importar headers4.9.
wmt_drv.ko SHA256bb6fcd5808f9c1730452012cb56f1376e0fa79945db91527295e6360573bd204;
wlan_drv_gen4m.ko SHA25669aeedae944620d48e2f44fbb2a9bd11faf711183ab3ec02760eca4139fd9012,
ambos release6.18.58-k40s-nativewifi1-NOT-FOR-FLASH. Nenhuma chamada fisica
SIP/DMA; nao comprova compatibilidade do firmware instalado ou LOCK efetivo.
Proximo bloqueio: firmware24 ainda usa retorno void e fallback weak, inclusive
download/calibracao; portar erro/reprotecao e inicializacao antes de ativar RF.
DT/ICC/panel/reset/coredump continuam gates. CapsulaBTv14 inalterada e sem
novos boot/flash/carga/aceite no aparelho.

## MT6765 CONNSYS MPU SIP32 — decisao previa2026-10-28

Bloqueio funcional: hook region25 WMT retorna sucesso com CONFIG_MTK_EMI
ausente; backend LG mpu_v1.c tambem ignora retorno SIP. Portar primeiro a
protecao comum4MiB da reserva WMT no arquivo mt6765.c existente, nao um driver
MPU universal. Reusar API arm_smccc_smc Linux6.18.58 e algoritmo LG comprovado
em fonte: SIP32 READ0x82000261/SET0x82000262, start=(PA>>16)|(25<<24),
end=(endPA>>16)|(group<<24), grupo1 antes de0; dom0/dom2 sem restricao, demais
FORBIDDEN5, LOCK bit31 no grupo0. Perfil16dom/32reg/64KiB MT6765. Readback
SA=0x100+reg*4, EA=0x200+reg*4, APC=0x300+reg*4+grupo*0x100;
SA/EA guardam endereco relativo a DRAM_OFFSET0x40000000. Nao importar violacao,
DEVAPC, modem, debug sysfs ou MMIO direto. Fonte permanece GPLv2.

Mainline6.18.58 local drivers/soc/mediatek e mtk_sip_svc.h nao fornecem este
contrato EMI MPU; TF-A mt8183 consultado em
https://github.com/ARM-software/arm-trusted-firmware/blob/master/plat/mediatek/mt8183/drivers/emi_mpu/emi_mpu.c
(BSD-3-Clause, master sem commit fixado, somente candidato) usa8 regioes e
MMIO/firmware proprio: nao equivalente a16dom/32reg/SMC32 stock6765. Nenhum
codigo desse candidato e importado. pmaports/MediaTek/Qualcomm da matriz nao
oferecem fornecedor compativel confirmado; Qualcomm SCM/IOMMU nao substitui
MPU Mediatek. Priorizar fonte LG disponivel; sem necessidade de RE nesta etapa.

Origens LG sem commit, SHA256: emi/submodule/mpu_v1.c
b4d688e7ff3770e977c76e30439356efb0e108e799936aecd09bf317215d886a;
mpu_v1.h 26146cd78603a4f10da09b8c04f079c645d81720d9250ae75b6f13d9562f6a6c;
emi/mt6765/mt_emi_api.h
71e45ef6b63748415e0249f0ba2c965586b4460d44135a5f6024032ea12ea2d6;
mt_emi.h 7aac690c5c23a2bcd4614253d81f42fc4b49de90be9ed306e69fdba401838fc5;
include/mt-plat/mtk_secure_api.h
1be80cfb1d6d2f1694029500439fea90a49160517001ab502820ce774e4a41d4.
Todos GPLv2 conforme cabecalho, sem licenca adicional inferida. Base integrada
preservada work/wmt-emi-mpu-backup-20261028-v1. Extensao pequena no backend
SoC existente, sem exports genericos novos; Wi-Fi24/29 sao etapas seguintes.

Antes de escrever: exigir ARM32, perfil exato LG, reserva4MiB/alinh16MiB/fim32,
e estado atual igual ao esperado (retornar sem writes) ou slot completamente
zerado (nao sobrescrever slot de outro owner). Rejeitar READ unsupported.
Mapear erros SIP conforme headerLG, conferir quatro registradores depois,
latchear falha apos write para impedir retry cego. Sem CLEAR, sem rollback
que afrouxe politica ou remova LOCK. Estado parcial requer recuperacao por
reboot antes de novo uso; nenhuma afirmacao de recuperacao fisica ainda.
Probe deve proteger ANTES de zerar/mapear EMI e recusar hook ausente.
Aceite offline: equivalencia com encodingLG, erros de transporte/readback/
slot ocupado e probe sem efeitos de memoria apos falha; ARM/MODPOST. Isto
nao confirma ABI do firmware instalado, prioridades/LOCK efetivos ou protecao
eletrica no aparelho. Nenhuma chamada SIP fisica, boot, carga ou flash autorizada.

Resultado2026-10-28: wmt-mt6765-emi-mpu-sip32-v1.patch integrado somente no
staging WMT/copia nativewifi1; fontes4.9 preservadas. Backend e core iguais
entre canonico/copia, SHA256 respectivamente
85628222a44c3344b637e6fe89809e3a83c4da749d7877d8e889912cdf2bf275 e
68456e4cafe600e5194f3da3134c77252c948b8105ec7db3931090cada80b1f1.
Testa helpers nativos reais versus emi_mpu_set_protection/SET_ACCESS_PERMISSION
LG reais (hashes fixados), com SMCCC/register doubles. Encoding de ambas as
chamadas identico nas bases0x40000000/0x90000000/0xff000000; perfil invalido
nao chama SIP; estado ja protegido nao escreve; quatro slots ocupados recusam;
READ unsupported recusa; erros em primeira/segunda escrita preservam errno e
latcheiam fault; quatro divergencias de readback impedem novos acessos SIP.
Passou ASan/UBSan/-Werror em work/wmt-emi-mpu-host-20261028-a.log. O modelo de
registradores nao confirma a implementacao do firmware instalado ou efeito
fisico de LOCK/prioridade; identidade de encoding nao equivale a radio ativo.

Regressoes existentes resolver/probe/genpd/XO passaram em
work/wmt-emi-mpu-probe-regression-20261028-a.log. Pins dos arquivos integrados
atualizados para o fonte realmente exercitado, sem retirar checks ou protecoes;
probe ganhou verificacao de que MPU ausente/falha nao tenta mapear/zerar EMI.
Build ARM/MODPOST passou work/wmt-emi-mpu-build-20261028-a.log; importa
__arm_smccc_smc real do kernel. wmt_drv.ko SHA256
d6f2de142d26a675c8b460ed8408b85a380181e823ed18c7731c32813f7885c6,
vermagic6.18.58-k40s-nativewifi1-NOT-FOR-FLASH. Nenhum export/header publico
mudou nesta etapa, portanto nao repetir builds de consumidores inalterados.
Hook hibernation legado ignora retornos, mas CONFIG_MTK_HIBERNATION nao esta
selecionado no candidato: nao o considerar validado/ativavel por este porte.

Proximo bloqueio MPU concreto: regioes Wi-Fi24 (firmware) e29 (PDMA) ainda usam
API void/fallbacks weak no gen4m; integrar transporte checked, propagacao de
falhas e reprotecao antes de qualquer copia/PDMA. Nao carregar o conjunto por
esta preparacao da regiao25. DT/ICC/panel, serializacao reset e coredump EMI
assincrono continuam gates. CapsulaBTv14 SHA2562938ca25648cb732c7b31b800df64ee04f9200e3563a6a315dbc2d0c58bd7fa0
inalterada; nenhuma chamada SIP fisica ou outro novo funcionamento no aparelho.

## WMT: lifetime da tabela Wi-Fi — decisao previa2026-10-28

Entrega visada: radio interno com retirada/reset recuperaveis. Bloqueio: seis
ponteiros globais Wi-Fi permitem chamada depois de unreg e troca entre teste e
call. Reusar SRCU/guard(srcu) Linux6.18.58 include/linux/srcu.h (GPL-2.0,
arvore local sem HEAD Git), como nos bridges/logs WMT ja auditados. Publicar
uma copia privada da struct LG existente com rcu_assign_pointer; leitores
capturam tabela uma vez sob guard SRCU ate retorno (inclusive todos os gotos).
Isso conserva a tabela durante janelas MPU-off/copia/MPU-on em calibrações e
na consulta get/clear de trafego. Unreg publica NULL e espera synchronize_srcu
antes de permitir liberar codigo/dados do gen4m. Nao adicionar mutex aos
leitores nem esperar grace period dentro de callback. Registro/unreg podem
dormir e nao podem ser chamados de um leitor do mesmo dominio.

Manter interface externa reg/unreg existente, sem novos exports. Getter/domain
sao internos ao WMT; remover externs dos ponteiros crus para encontrar qualquer
leitor esquecido na compilacao. Registro duplicado recusa EBUSY em vez de
substituir modulo ativo; probe/remove obrigatorios, campos opcionais preservam
fallback legado. Falha de probe imediato retira tabela e drena leitores antes
de retornar. Esperar leitores anteriores a publicacao antes de consumir o
pending gWifiProbed, usando READ/WRITE_ONCE. Serializacao funcional de chamadas
probe/reset e backend MPU continuam gates proprios, nao provados pelo SRCU.

Fontes LG WMT GPLv2 conforme cabecalhos, snapshot sem commit: wmt_exp.c,
wmt_func.c, wmt_lib.c, wmt_ic_soc.c, wmt_dev.c, stp_dbg.c e wmt_exp.h.
Base integrada preservada em work/wmt-wlan-srcu-backup-20261028-v1 com hashes
na evidencia desta etapa. Esforco: adaptar os nove leitores existentes, sem
driver/framework paralelo ou mudar comandos/limites EMI. Mainline/pmaports/
MediaTek/Qualcomm da matriz nao implementam este registro LG; framework SRCU
nativo e implementacao LG existente resolvem a lacuna, sem engenharia reversa.
Aceite offline: build WMT/gen4m com exports reais e teste de leitores bloqueados
contra unreg/falha, incluindo retornos antecipados. Sem carga/RF/flash autorizados.

Integracao necessaria no caller gen4m: erro de reg nao chama unreg global,
pois novo reg desfaz sua propria publicacao falha; EBUSY preserva outro owner.
Desfazer somente recursos locais do probe. Coredump assincrono start/stop EMI
continua gate: guard por chamada nao mantem ownership entre APIs distintas,
nem fornece MPU. Nao declarar janelas assincronas/serializacao reset resolvidas.

Resultado2026-10-28: wmt-wlan-callback-srcu-v1.patch implementa tabela privada
e nove leitores guardados. Nenhum dos seis ponteiros antigos permanece como
simbolo no agregado WMT; nomes sobrevivem somente em mensagens legadas.
Getter e dominio SRCU nao foram exportados. Reg/unreg publicos preservam ABI;
struct callback nao mudou. gen4m-wmt-register-transaction-v1.patch adapta o
caller para nao desregistrar outro owner quando recebe EBUSY.
Proveniencia/hash de cada uma das sete entradas da base integrada esta em
tools/tests/test_wmt_wlan_srcu.py INPUTS; backup imutavel em work indicado acima.

Teste usa os helpers reais de registro/on/off e o corpo real de
mtk_wcn_soc_restore_wifi_cal_result, com o modelo SRCU de dois epochs ja usado
nos logsWMT. Passou ASan/UBSan/-Werror/pthreads em
work/wmt-wlan-srcu-host-20261028-c.log: callback probe/remove bloqueado mantem
unreg esperando; novos leitores veem NULL, tabela e copia independente,
registro duplicado nao substitui, pending-on e servido, probe imediato falho
retira tabela e retornos antecipados/combo/erro soltam read guard. Durante
copia de calibracao bloqueada, unreg nao retorna antes da reprotecao usando
o mesmo snapshot. Sao doubles de MPU/OF/threads, nao prova de MPU fisica ou
Linux SRCU real. Log-a falhou pelo extrator pegar prototypes e indentacao do
double; corrigido sem suprimir warnings. Teste gen4m atualizado para contrato
transacional e EBUSY preservando outro owner passou em
work/wmt-wlan-srcu-gen4m-host-20261028-a.log.

Builds ARM/MODPOST finais exit0: work/wmt-wlan-srcu-build-20261028-b.log,
work/gen4m-wmt-srcu-build-20261028-a.log e
work/gen4m-adaptor-wmt-srcu-build-20261028-a.log (adaptor KCFLAGS=-Werror).
Set nativewifi1 coerente; canonico/copia dos sete arquivos iguais por SHA256.
wmt_drv.ko SHA256d875280cd7849f22c28a7897a997442f9adb8a632093c5bfca92a85ba96c0012;
wlan_drv_gen4m.ko SHA256232939152c51266da8334d40e012ad5a71383ee13325b512a6285aae343d6570;
wmt_chrdev_wifi.ko SHA25613decf06ef141cb51b4af629e064af7c8045ed94b9aae4296cecaa27a9430ea2.
CFG_CALIBRATION_BACKUP_RESTORE=1 no C selecionado. Sem warnings ou exports
ficticios. Gates restantes: backend MPU com erros/reprotecao real, consumer
DT/ICC/panel, serializacao das transicoes/estado de reset e ownership do
coredump EMI assincrono entre start/stop. Nao ativar firmware/RF por este build.
Fontes4.9/capsulaBTv14 preservadas, nenhuma operacao fisica ou novo aceite.

## Gen4m: vinculo OF e ciclo sequencial AXI — decisao previa2026-10-28

Bloqueio: CONNAC sintetico nao possui DT; id_entry e NULL no matching OF
nativo. Reusar platform_driver/of_match_table/device_get_match_data e
platform_get_irq do Linux6.18.58 (drivers/base/platform.c/include/linux/property.h,
GPL-2.0, copia local sem HEAD Git) com fonteLG AXI dual GPLv2/BSD ja identificada.
Compatible especifico mediatek,mt6765-wifi somente CONNAC; nao assumir que todo
mediatek,wifi tem mesmo chip. No ARM registrar somente o driver, sem criar ou
deletar dispositivo pertencente ao OF. Sem dispositivo, registro pode suceder
sem bind (sem afirmar wlan0); deferred probe permanece com o core nativo.
Publicar pdev antes de registrar callbacksWMT, pois reg pode chamar probe
sincronamente. Propagar erro de reg e desfazer callbacks/recursos adquiridos.
Desmontagem sequencial: retirar callbacks, parar WLAN ainda com IRQ/MMIO/pool/
panel/ICC vivos, depois soltar recursos; nao remover WLAN duas vezes.

wlanProbe em gl_init.c ja faz unwind por eFailReason; nao chamar wlanRemove
novamente quando probe falhou. Preservar erro PALDO antes de WLAN e desfazer
PALDO em falha; native WMT registra fault de rail. Guardar start duplicado e
limpar estado ativo no stop, mantendo a interface existente. Esforco pequeno
no AXI, sem backend novo; outras arquiteturas mantem registro sintetico legado.
Matriz mainline/pmaports/MediaTek/Qualcomm existente continua aplicavel: API
platform resolve a lacuna, nao importar outra pilha. Sem RE por haver fonte.
Aceite offline: matching/IRQ e lifecycle real com falhas sob doubles + build
ARM. WMT unreg atual apenas zera ponteiros sem drenar leitores; esta mudanca
NAO resolve concorrencia/unload/reset e nao autoriza carga. MPU/ICC/panel/DT
consumidor e recuperacao continuam gates. Nao criar overlay ativando hardware
antes dessas dependencias. Entrega final continua IP/trafego com USB/SSH vivo.

Resultado: gen4m-axi-of-lifecycle-v1.patch reproduzido sobre LG+prerequisitos
com fuzz0. Teste dos helpers reais passou ASan/UBSan/-Werror em
work/gen4m-of-lifecycle-host-20261028-c.log: match ausente, falhas panel/ICC/
DMA/CSR/pool, WMTreg falha, callback imediato/deferido, PALDO-on falha,
wlanProbe falho sem segunda chamada remove, start/stop repetidos, owner
estrangeiro, registro sem dispositivo/probe falho e IRQ com defer/erro.
Reset simplificado preserva GLUE; dispositivo removido forca fluxo completo,
inclusive depois de stop simplificado sem restart. Nenhuma task real, DMA ou
callback concorrente e exercitado por doubles. Remocao continua bloqueada por
WMT unreg sem drain: leitores em wmt_func.c, wmt_lib.c, wmt_dev.c, stp_dbg.c
e wmt_ic_soc.c precisam ownership/sincronizacao antes de unload fisico.

Build ARM final MODPOST exit0 em
work/gen4m-wifi-of-lifecycle-build-20261028-d.log. Fonte canonica/copia iguais
SHA25621d5e3bd1306c396d6af7985a73026fd564b32b5010137b08c3687ee95bd1350.
wlan_drv_gen4m.ko SHA256
6f54e0af7b1b882850a5df579d14490c0ac5d63fc90a31213b0769c3d0077daa,
vermagic nativewifi1, depends cfg80211/WMT/adaptor e aliases OF mt6765-wifi
conferidos por modinfo. nm confirma platform_get_irq/device_get_match_data,
sem imports platform_device_alloc/add/del no alvo ARM. Registro apenas de
driver nao equivale a bind nem RF: consumer DT/panel/ICC/MPU ainda faltam.
Logs build-a/b/c sao versoes intermediarias anteriores aos ultimos ajustes de
reset, nao evidencia do fonte final. FonteLG4.9/capsulaBTv14 inalterados;
nenhuma carga, instalacao, operacao fisica ou novo aceite no aparelho.

## Gen4m: reservas por consumidor ARM — decisao previa2026-10-28

Entrega visada: Wi-Fi interno com firmware/PDMA usando as reservas LG corretas,
sem invadir RAM normal ou perder recuperacao. Bloqueio offline: quatro globais
do built-in4.9 ainda sem fornecedor. WMT ja valida seu proprio memory-region,
mas seus globais sao privados e nao devem virar exports mutaveis compartilhados.
Reusar of_parse_phandle/of_property_match_string/of_reserved_mem_lookup do
Linux6.18.58 e o mesmo perfil LG: CONNSYS4MiB, Wi-Fi3MiB, alinhamento16MiB,
no-map, nao reusable, enabled, base nao zero, fim32bits e regioes nao sobrepostas.
Ambos devem ser phandles nomeados consys/wifi do proprio consumidor AXI; o
phandle consys deve apontar a mesma reserva usada pelo WMT no futuro DT.
Sem busca global, kmalloc ou endereco fixo. Publicar somente apos validar ambas;
um owner por modulo, limpar em probe falho/remove, nao exportar novos globais.
Antes de panel/ICC/DMA/MMIO, exigir aquisicao valida. Dispositivo sintetico sem
OF falha fechado; DT real/probe lifecycle/MPU/ICC seguem etapas necessarias.

Fonte LG axi.c dual GPLv2/BSD e DTS mt6765.dts possuem identidades registradas
acima/na secao WMT; original intacto. Extensao pequena ao AXI existente, nao
driver novo. API GPL do kernel compativel com licenca GPL escolhida pelo modulo.
Mainline/pmaports/MediaTek/Qualcomm da matriz nao substituem esse transporte;
o resolver WMT local ja demonstra o padrao compativel de OF e validacao.
Nao copiar adaptador builtin4.9 inteiro nem exportar seus dados brutos.
Revisao kernel6.18.58 local sem HEAD confirmado; versao LG sem commit conhecido.
Aceite offline: resolver real com falhas OF/limites/ownership e build/link ARM
usando tabelas reais. Nao comprova protecao MPU, cache, callback lifetime ou RF.

Resultado2026-10-28: gen4m-axi-reserved-memory-v1.patch integrado no AXI
canonico/copia de build (SHA256 igual
62d87822bbd3cb70a99ca0205e51215d370f2537cf1f8eeb05313374e79e77d9).
Teste reproduz todos os prerequisitos sobre originalLG com fuzz0 e executa
resolver/probe reais com doublesOF: referencias nomeadas em ordem invertida,
phandle/reserva ausentes, disabled/compatible/no-map/reusable invalidos,
base0/desalinhada/>32bits, tamanhos errados, sobreposicao e probe falho em
panel/ICC/DMA/CSR/pool nao deixam publicacao; owner estrangeiro nao limpa,
segundo bind recusa EBUSY e rebind apos release funciona. ASan/UBSan/-Werror
passaram work/gen4m-reserved-memory-host-20261028-b.log. Primeiro teste falhou
por indentacao do double (log-a); corrigido sem relaxar Werror. Perfil do probe
no teste nao registra callbacksWMT; nao prova remove concorrente/allocatorOF.

Build ARM/MODPOST terminou exit0, agora existe
module-workspaces/nativewifi1-20261028-v1/gen4m/wlan_drv_gen4m.ko no WSL,
SHA2562588a269409b1ba1913322ab317e4c46202178f7e2a6d3878c8472b9d58bc5aa,
vermagic6.18.58-k40s-nativewifi1-NOT-FOR-FLASH, depende cfg80211,wmt_drv,
wmt_chrdev_wifi. Log work/gen4m-wifi-reserved-memory-build-20261028-a.log.
Quatro globais agora pertencem ao AXI e recebem somente reservas validadas;
nenhum export publico novo. Nenhum simbolo fabricado/tabela symvers manual.
Nao aprovado para carga: glRegisterBus ainda cria CONNAC sintetico sem OF e
probe agora recusa ENODEV; falta consumer DT real/OF matching/lifecycle.
MPU ainda e bloqueio: CONFIG_MTK_EMI nao fornece backend nativo no candidato;
gl_kal.c contem kalSetEmiMpuProtection/kalSetDrvEmiMpuProtection weak que
apenas avisam. Nao considera-los protecao funcional nem ativar RF/download
sem substituir por backend compativel com retorno de erro e recuperacao.
ICC MT6765/panel/IRQ/WMT lifetime/teardown continuam gates registrados.
Nenhuma carga, boot, RF, flash ou mudanca na capsula BT foi realizada.

## Gen4m ARM: wrappers stack/cache — decisao previa 2026-10-28

Bloqueio: dois exports do built-in LG4.9 impedem o link Wi-Fi6.18. Reusar
as APIs reais do Linux6.18.58 local, sem novo fornecedor/export ou diagnostico.
CONNAC conserva a assinatura do callback; ponte privada chama sched_show_task
(GPL export), escolhendo current quando task=NULL. ARM4.9 show_stack ignora sp;
ARM6.18 tambem. A API nativa acrescenta contexto da task e protege as paginas
de stack, mas nao resolve lifetime do ponteiro task nos callers kalHaltLock.
AXI usa __cpuc_flush_dcache_area de asm/cacheflush.h: dispatch cpu_cache para
flush_kern_dcache_area, cujo backend v7 e a mesma operacao clean/invalidate
com barreira do wrapper antigo. Preservar endereco/comprimento e chamada mesmo
com len=0. Nao usar flush_kernel_vmap_range (pode no-op), API DMA privada ou
remover callback. Alocacao/mapping/ownership DMA nao mudam; coerencia fisica
continua nao provada. Outros alvos nao ARM conservam wrappers antigos.

Origens locais sem HEAD Git confirmado: LG connac.c dual GPLv2/BSD SHA256
51b574f54db5c9847ef51305898073e60ba969b5314f9fc2df15fc81b8d97fd4;
axi.c mesma licenca, SHA256
8d8b59ef79084e5d5c537707dcf65f738f9900d84757db93a67fe70b671fb404.
Wrapper kernel4.9 connectivity_build_in_adapter.c SHA256
d3e1668093d4d88ce59daa4556b3da1291e021bac08bd6d354f75a9087ef4507;
Linux6.18.58 cacheflush.h SHA256
5cef8491149608de514de1e7d88be3c55df92be2f9f2f1b7cfae8671ce5d30cd,
cache-v7.S SHA256
36e3fe2430db605c7d78285469b175224799b88e20e0fbc03badc0f63d71d863,
fontes kernel GPL-2.0. Matriz mainline/mt76/pmaports/MediaTek/Qualcomm abaixo
continua aplicavel: trocar o driver nao resolve esta pequena lacuna de API
ARM e nao ha equivalencia AXI6765 demonstrada nessas alternativas. Esforco:
duas adaptacoes locais, sem importar transporte de outro SoC. Aceite offline:
checagem dos argumentos/dispatch e build ARM com exports reais; entrega final
permanece wlan0 associado/IP/trafego com USB/SSH preservado. Sem ensaio fisico.

Resultado: patch gen4m-arm-stack-cache-v1.patch reproduzido sobre fontes LG
originais com prerequisitos, fuzz=0. Teste dos helpers reais versus wrappers
originais passou ASan/UBSan/-Werror: task explicita/NULL=current, sp ignorado,
cache len0/1/31/32/64/127, offsets0..64 e dispatch alternativo de CPU. Doubles
nao comprovam stack lifetime nem efeito cache/DMA fisico. Log
work/gen4m-arm-stack-cache-host-20261028-a.log. Build ARM completo compilou,
mas MODPOST ainda falhou somente nos4 globais de memoria: gConEmiPhyBase,
gConEmiSize, gWifiRsvMemPhyBase, gWifiRsvMemSize. Log
work/gen4m-wifi-arm-stack-cache-build-20261028-a.log. nm do agregado agora
refere cpu_cache/sched_show_task, ambos presentes no Module.symvers real do
kernel nativewifi1; nenhum dos dois wrappers antigos permanece indefinido.
Fontes canonicas e copia de build conferidas por SHA256. Nao ha .ko Wi-Fi.
Proximo bloqueio: obter reservas reais DT e ownership/MPU, nao definir globais
zero nem alocar memoria arbitraria para satisfazer link. Imagem BTv14 inalterada
(SHA2562938ca25648cb732c7b31b800df64ee04f9200e3563a6a315dbc2d0c58bd7fa0).

## Conectividade: triagem de compilacao 2026-10-27 (sem carga)

### Bluetooth LG: primeiro bloqueio de build 6.18 — 2026-10-28

#### Wi-Fi LG/gen4m: primeiro build isolado6.18 — 2026-10-28

Entrega no aparelho visada: wlan0 interno, associacao com IP e trafego,
preservando USB/SSH; independente do aceite Bluetooth. Sem autorizacao fisica,
esta etapa apenas localiza incompatibilidades reais de compilacao. Reusa fontes
LG ja usadas no4.9, selecao CONNAC/6765/HIF AXI e simbolos do WMT6.18 existente.
Nao modifica fonte4.9, imagem candidata BT, firmware, runner ou limites eletricos.

Copia isolada em module-workspaces/staging-wifi-lts-20261028-v1 no workspace WSL,
sem objetos/modulos gerados4.9. Origem conn-src LG sem commit identificado:
adaptor/wmt_cdev_wifi.c GPL-2.0, SHA256
7b6d5e2d211d355109941552eabbfbb7baf077b115aeaeceb7d004c1c30944a6;
core/gen4m/os/linux/gl_init.c dual GPLv2/BSD conforme cabecalho, SHA256
9443b36eb9606d16cd0789d9dd85fe05b595f8dd657665c5b0f7307dd8ba48a9.
Alternativas mainline/mt76, pmaports e Motorola/MediaTek permanecem avaliadas
na matriz WMT/CONNSYS abaixo; nenhuma equivalencia de AXI/firmware6765 foi
demonstrada para substituir a implementacao LG. Nao criar driver paralelo.

Primeiro build contra6.18.58 falhou, sem desabilitar Werror: dependencia vendor
cpu_ctrl.h/topo_ctrl.h em plat_priv.c (boost CPU), timeval removido em tokens
PDMA, declaracao iommu_ops ausente e macro OWE duplicada com ieee80211.h nativo.
Log work/gen4m-lts-baseline-build-20261028-a.log. Nenhum modulo Wi-Fi6.18 pronto.
Proxima adaptacao deve usar APIs existentes de tempo/cfg80211/IOMMU e comparar
o boost com cpufreq/freq_qos, incluindo liberacao sob erro/remove; nao copiar
headers Linux4.9 nem substituir boost por sucesso no-op. MPU EMI/AXI e DMA
precisam ser preservados antes de qualquer carga, mesmo se o build passar.

Decisao previa PDMA: usar timespec64/ktime_get_real_ts64, timespec64_sub e
timespec64_compare do proprio6.18.58 local (include/linux/time64.h e timekeeping.h,
GPL-2.0, arvore extraida sem metadados Git;2926d88 e referencia da matriz,
nao um HEAD confirmado desta copia). Manter relogio real,
descarte de amostra se agora<token, limiares em segundos e comparacao >=;
resolucao passa de microssegundos a nanossegundos, sem diminuir limiares.
Nao alterar alocacao, retorno de tokens, DMA ou travas. Sem fonte mainline,
pmaports ou Qualcomm equivalente ao protocolo AXI6765, API Linux de tempo
resolve esta lacuna sem importar codigo de outro driver. Macros OWE devem
reusar ieee80211.h quando presentes; forward declaration iommu_ops apenas
corrige escopo de tipo, nao implementa nem aprova o transporte IOMMU.

Resultado parcial: common/dump.o, dbg_pdma.o e hal_pdma.o compilam ARM contra
6.18 com Werror, log work/gen4m-lts-pdma-build-20261028-b.log. Patch reproduzivel
patches/kernel/staging/gen4m-pdma-linux618-time-v1.patch passou dry-run sobre
fontes originais, sem aplica-lo ao4.9. Tres helpers de RX/alocacao de rings
usados somente em hal_pdma.c ficaram static; corpos de DMA intactos. Include
publico sched/clock.h declara sched_clock existente. timer_delete_sync substitui
o antigo del_timer_sync, preservando espera pelo callback no mesmo ponto SER.
Macro de intervalo conserva unidade microssegundos e largura unsigned long;
nao controla o timeout de ownership. Comparador usado somente por sinal (<0,
>=0, >0) nos dois consumidores, compativel com timespec64_compare.
Isso nao comprova equivalencia sob falha/recuperacao no hardware, nem build do
modulo completo; boost CPU e demais dependencias continuam por adaptar.

Arquivos LG afetados, todos com cabecalho dual GPLv2/BSD preservado; caminhos
relativos a wlan/core/gen4m, SHA256 da origem local sem commit identificado:

| Arquivo | SHA256 original |
| --- | --- |
| os/linux/hif/common/include/hif_pdma.h | 6711890f9fb79230e2c8605e3a4946a90afdad5d5915b8d663f3eefc41f0c9fd |
| os/linux/hif/common/dbg_pdma.c | c7ba88416179f5600c847a0550554bbfb3b96d088de22c1dca405432bb4da348 |
| os/linux/hif/common/hal_pdma.c | de0fc30b646bd396d3c95e553114dd6616515460b7c557c5c1fe4461f20e54fd |
| os/linux/include/gl_os.h | c40ca512d45e3b23947a234c38c7fdf16241f0275650dceea0552e5d6a34b697 |
| os/linux/include/gl_kal.h | 4cd7e3cc47e8c2a2114e9edbb75e57556199bae437e83ddbe9d8cb6359747381 |
| include/mgmt/rsn.h | 85ea75d1eb8be45180a61dfa78c61117d963637add679e558c8702b99e429b20 |

#### Gen4m: rebuild coerente nativewifi1 — decisao previa2026-10-28

Entrega offline: BTIF/WMT/adaptor/gen4m com mesmo release do kernel Wi-Fi,
dependencias/exports reais, preservando fontes/outputs anteriores. Kbuild
MO= recusou BTIF porque M original contem modules.order, log
work/gen4m-wifi-btif-build-20261028-a.log. Nao executar clean para contornar
ou remover artefatos preservados. Reusar rsync local para copias byte-identicas
das fontes e Makefiles em nativewifi1-20261028-v1/src/{btif,wmt,wlan}, excluindo
somente produtos de build (*.o/ko/mod/mod.c, .cmd/.d, Module.symvers,
modules.order e .tmp_versions). MO= distinto para cada modulo. Sem modificar
codigo, protocolo, kernel flags ou relaxar guarda de source tree limpa.
Parametros KERNEL_OUT/AUTOCONF_H devem apontar autoconf real do novo kernel;
WMT_API_ROOT e KBUILD_EXTRA_SYMBOLS apontam fontes/tabelas do mesmo conjunto.
Aceite: compilacao/MODPOST, vermagic novo e lista residual derivada das tabelas
geradas; nao prova ABI/runtime, callbacks ou radio no aparelho. Triagens de
reuso/licencas das mesmas fontes permanecem aplicaveis; nao sao novos drivers.

Resultado rebuild2026-10-28: copias limpas criadas por rsync sem clean/delete
dos originais; verificacao checksum/dry-run vazia antes e depois dos builds
confirma as mesmas fontes/Makefiles (produtos excluidos). BTIF/WMT/adaptor
geraram .ko e MODPOST passou nos outputs nativewifi1-20261028-v1/{btif,wmt,
adaptor}, todos vermagic6.18.58-k40s-nativewifi1-NOT-FOR-FLASH. Dependencias
reais conferidas: wmt_drv->lg_btif e wmt_chrdev_wifi->wmt_drv. Logs
work/gen4m-wifi-btif-build-20261028-b.log,
work/gen4m-wifi-wmt-build-20261028-a.log e
work/gen4m-wifi-adaptor-build-20261028-e.log, sem warnings/erros. Comando
real WMT .wmt_ctrl.o.cmd usa -imacros do kernel Wi-Fi novo, nao autoconf antigo.
Makefile fonte WMT ainda tem default antigo, portanto manter override explicito
AUTOCONF_H do candidato. Adaptor usa WMT_API_ROOT da copia limpa correspondente.

Gen4m compilou todas as unidades contra WEXT on e export checked real, gerou
objeto agregado e chegou ao MODPOST: work/gen4m-wifi-full-build-20261028-e.log.
KBUILD_EXTRA_SYMBOLS recebeu tabelas WMT e adaptor por argumentos GNU make
var=path1 var+=path2, sem tabela agregada manual ou bypass. Pendencias caíram
de14 para6, todas do antigo built-in adapter: connectivity_export_show_stack,
connectivity_flush_dcache_area, gConEmiPhyBase, gConEmiSize,
gWifiRsvMemPhyBase e gWifiRsvMemSize. Lista independente de nm versus tabelas
reais em work/gen4m-wifi-residual-symbols-20261028-b.log. Nao existe .ko gen4m.
Nao definir globais0 ou retirar flush; resolver fornecedor/DT/coerencia reais.
Leitura nativa mostra sched_show_task e cpu_cache exportados como candidatos
para substituir wrappers, mas requer comparar callers/semantica antes de usar.
Modulos antigos/fontes originais, config base e imagem BTv14 hash preservados.
Nenhum modulo carregado ou boot/flash/RF feito; todos os gates runtime mantidos.

#### Gen4m: adaptor LG — triagem previa2026-10-28

Entrega visada: fornecedor real dos6 exports de controle/reset/buffers usados
por gen4m, mantendo USB/SSH e futuro Wi-Fi/IP/trafego. Reusar adaptor LG
wmt_cdev_wifi.c (GPL-2.0 no cabecalho; MODULE_LICENSE legado Dual BSD/GPL
nao amplia permissao do arquivo), SHA256original ja registrado7b6d5e2d...
na triagem inicial. Sem substituir por stubs. Kbuild LG existente e headers
WMT6.18 ja portados sao o menor caminho; APIs cdev/class/device nativas6.18
substituem somente interfaces removidas. Triagem mainline/pmaports/MediaTek/
Qualcomm vinculada nao comprova outro fornecedor para este contrato LG.
Primeiro compilar objeto com Werror no kernel base ja pronto, enquanto build
kernel Wi-Fi separado segue vivo; nao compilar contra output em construcao.
Depois corrigir falhas concretas, incluindo init de semaphore antes de
exposicao, owner de fops e rollback de registro/class/device. Callbacks globais
e reset/write ainda exigem ownership/drain/recuperacao antes de qualquer uso
fisico; compilacao nao os valida. Nenhuma mudanca de firmware ou radio agora.

Triagem adaptor: baseline parou em mtk_wcn_cmb_stub.h ausente pelo layout
Android antigo, work/gen4m-adaptor-baseline-build-20261028-a.log. Header real
ja existe no vendor-api WMT portado. Adicionar selecao WMT_API_ROOT no
Makefile LG para usar esses headers coerentes, preservando caminho original
quando parametro ausente e todos os flags/objetos/caminhos opcionais LG.
Nao copiar headers kernel4.9 nem usar fake config. Makefile LG sem cabecalho
de licenca proprio: nenhuma concessao adicional inferida; fonte C GPL-2.0
continua condicao do codigo compilado. Mudanca somente de include roots,
nao contrato do radio, e precisa ser conferida no comando real do compilador.

Com WMT_API_ROOT real, compilador alcançou C e apontou somente declaracoes
e class_create antigo, work/gen4m-adaptor-native-headers-build-20261028-b.log.
Makefile original SHA256 674683c9bb32d114e72e4578e1e5464a5c98cd3a617af91b9863f623f5a76ed6.
Decisao previa de API/lifecycle: class_create(name) nativo Linux6.18
include/linux/device/class.h/drivers/base/class.c GPL-2.0. Fops .owner usa
pin de modulo do proprio fs.h/fops_get; nao implementar refcount paralelo.
Inicializar wr_mtx antes de cdev_add/device_create. Preservar APIs exportadas,
declarando seus tipos ja existentes; helpers set_low_latency_mode/WIFI_write
e tabela usados somente neste C ficam static. Preservar corpos dos comandos.
Propagar errno real de register/cdev/class/device/fwlog e desenrolar somente
recursos obtidos; falha fwlog nao deve deixar cdev/class/device publicados.
Testar init/exit reais com falha em cada API e owner/semaphore no momento de
exposicao, com doubles; nao confundir com lifetime de callbacks/write/reset.
Config FWLOG on so pode ser declarada valida apos portar/testar seu proprio
backend; doubles aqui apenas verificam erro do sub-init e rollback do adaptor.

Resultado adaptor2026-10-28: wmt_chrdev_wifi.ko gerado ARM com KCFLAGS=-Werror
e MODPOST real WMT, sem warnings apos adicionar MODULE_DESCRIPTION; log
work/gen4m-adaptor-native-build-20261028-d.log. Seis exports reais presentes
em adaptor/Module.symvers. Esse build e para release base
6.18.58-k40s-nativeusbemmc1-NOT-FOR-FLASH, nao carregar com kernel Wi-Fi novo.
Preservados corpos dos11 helpers/comandos/reset/open/write conferidos em
work/gen4m-adaptor-equivalence-20261028-a.log. Init usa class_create(name),
semaphore antes de exposicao e owner de fops; errno real e rollback de
recursos obtidos, inclusive se sub-init fwlog falhar. Logs/teste host
ASan/UBSan work/gen4m-adaptor-init-host-20261028-b.log: falhas de registro,
cdev/class/device/fwlog, ordem de liberacao, ausencia de recursos publicados
apos falha e fops owner no cdev_init, com FWLOG off/on em doubles. Isso nao
valida backend FWLOG on, open-fd/unload real ou callbacks globais/reset/RF.
Patch gen4m-adaptor-linux618-v1.patch reconstruido fuzz0 nas fontes originais;
dois arquivos finais copiados ao baseline/adaptor e conferidos por hash.

Kernel Wi-Fi terminou com sucesso, work/gen4m-wifi-kernel-build-20261028-a.log:
vmlinux contem release6.18.58-k40s-nativewifi1-NOT-FOR-FLASH, e vmlinux.symvers
contem sched_setattr GPL e wireless_send_event reais. zImage SHA256
24b285afbd1a22d6a8b7229985c2db8e9e4bc306a8d35adb6b3a929141174383;
zImage base preservado SHA256
8045c62e6ebaf3af4fb6950f4ac8ef6f16ba421b15911d10432ed3fe9c617acd.
Cfg80211/BT/crypto nativos reconstruidos e MODPOST concluido para release
novo, work/gen4m-wifi-native-deps-build-20261028-c.log; vermagic dos4 .ko
conferido e Module.symvers novo inclui os2 exports necessarios. Nenhum warning
nos logs finais desses builds. Config base e imagem BTv14 hash preservados.
Nenhum boot image novo foi empacotado, nenhum ensaio fisico feito ou autorizado.
Proxima etapa: reconstruir BTIF/WMT/adaptor/gen4m para release novo, em MO=
separado, e resolver memoria/cache/stack residuais com fornecedores reais.
Callbacks e reset do adaptor permanecem gates de ownership/drain antes de
uso; nao declarar modulo inteiro seguro por causa de teste de init/exit.

#### Gen4m: kernel candidato Wi-Fi separado — decisao previa2026-10-28

Entrega offline: kernel/modules reais que fornecam sched_setattr checked e
wireless_send_event, mantendo a entrega BT anterior. WEXT_CORE nao e modulo
isolado: net/wireless/Makefile o compila em vmlinux quando selecionado pela
opcao visivel CONFIG_CFG80211_WEXT em net/wireless/Kconfig. Reusar esse
caminho nativo, nao copiar wext-core para modulo paralelo, criar stub de
evento ou forcar define ausente. Fonte Linux6.18.58 GPL-2.0 local; extensao
checked sched_setattr ja auditada, corpo/protecoes intactos. Triagem mainline/
pmaports/MediaTek/Qualcomm vinculada favorece exatamente essas APIs nativas,
sem transporte, driver ou tabela regulatoria nova.
Clone nao compartilhado do build947MiB existente em O=build-wifi-20261028-v1,
espaco754GiB verificado. Config herda alvo validado, muda somente release e
CFG80211_WEXT, deixando Kconfig selecionar dependencias. Fragmento
kernel/devices/lg-k40s/lts-6.18/wifi-link.config registra a diferenca real.
Release -k40s-nativewifi1-NOT-FOR-FLASH distingue modulos do perfil BT antigo.
Nao alterar O=build anterior, imagem BTv14/runner/registry/firmware; fonte
6.18 compartilhada so possui export checked adicional ja auditado.
Aceite: diff config limitado, protecao regdb mantida, build kernel/modulos e
exports reais WEXT/scheduler, sem ignorar modpost. Modulos WMT/gen4m precisam
ser reconstruidos para novo release antes de carga futura. Nenhum ensaio
fisico, flash, RF ou carga autorizados por esta preparacao.

Preparacao kernel Wi-Fi2026-10-28: clone O=build-wifi-20261028-v1 concluido
sem hardlinks mutaveis com O antigo; olddefconfig passou, log
work/gen4m-wifi-kernel-olddefconfig-20261028-a.log. Comparacao de todos os
simbolos da config confirmou apenas LOCALVERSION, CFG80211_WEXT e selecoes
nativas WEXT_CORE/WEXT_PROC. Signed regdb preservado; config base identica
ao backup. Objeto syscalls.o do candidato recompilado explicitamente com
KCFLAGS=-Werror, work/gen4m-wifi-scheduler-werror-20261028-b.log, passou.
Build zImage iniciado em O separado, work/gen4m-wifi-kernel-build-20261028-a.log;
ainda em execucao no ultimo acompanhamento, sem aceite de imagem gerada.
Arquivos herdados pelo clone nao provam novo kernel/modulos: exigir termino
com sucesso, novo release e exports nas tabelas reais antes de considera-los
prontos. Nao reconstruir/rerodar por mera espera enquanto processo estiver
vivo. WMT/gen4m tambem precisam rebuild para o release novo, preferindo MO=
separado suportado no Kbuild6.18 para preservar outputs antigos.
Adaptor LG segue proximo fornecedor ausente: sua init publica cdev/device
antes de sema_init e possui erros de rollback/owner alem de class_create
antigo; tratar antes de ativa-lo. Nenhuma dessas preparacoes muda autorizacao
fisica, imagem BT ou recuperacao ja validada.

#### Gen4m: scheduler verificado e threads transacionais — decisao previa2026-10-28

Entrega visada: remover dependencia sched_setscheduler nao exportada e fechar
falha concreta de startup (ERR_PTR usado em scheduler, callers ignoram retorno
de wlanOnPreNetRegister). Reusar kthread_create/stop/wake, completions e refs
Linux6.18, criando tasks paradas, configurando todas antes de executar e
revertendo tarefas ainda paradas em erro. So sucesso publica execucao; refs
das tasks mantidas ate a barreira de completion existente, rearmada em reset.
Caller probe deve propagar erro para cleanup NET_REGISTER_FAIL existente;
reset nao deve marcar sucesso apos falha de startup. Sem novo thread framework.

Linux6.18 kernel/sched/syscalls.c GPL-2.0 SHA256original
60a87e6183fd3cdb5661245da92438a6f25732577036f857891e1625f2399a95:
sched_setattr usa mesmo __sched_setscheduler com user=true que o wrapper
legado. sched_setattr_nocheck/FIFO helpers exportados pulam checks; nao sao
substitutos equivalentes para politica/prioridade configuraveis LG. Preferir
extensao minima EXPORT_SYMBOL_GPL(sched_setattr), sem mudar corpo/validacoes,
a wrapper paralelo ou bypass. Preservar nice e custom_slice como conversao
legada nativa; politica byte nao representa RESET_ON_FORK/SETPARAM negativos.
Gen4m declara Dual BSD/GPL. API exportada so estara disponivel apos rebuild
real do kernel candidato; nao fabricar entrada symvers ou declarar kernel
validado antigo compativel. Backup do C nativo em
work/gen4m-scheduler-kernel-backup-20261028-v1 antes da mudanca.

LG gl_init.c dual GPLv2/BSD, snapshot/hash original ja registrado. Auditoria
mainline/pmaports/MediaTek/Qualcomm vinculada favorece as mesmas APIs nativas
de task/scheduler e pequeno adapter privado, nao importar OSAL de outro SoC.
Nova logica local se justifica por ownership/rollback que faltam na fonte LG;
nao altera callbacks das threads, DMA, RF, firmware ou limites eletricos.
Aceite dirigido: ARM/Werror nos objetos afetados e funcao real com doubles
para falha em cada create/scheduler, nenhuma execucao parcial, ref/completion
sob sucesso/stop e perfis1/3threads. Protecoes scheduler/LSM nao serao removidas.

Resultado threads2026-10-28: objetos kernel/sched/syscalls.o e gl_init.o
compilam ARM/Werror, logs work/gen4m-kernel-scheduler-object-20261028-a.log e
work/gen4m-lts-thread-start-build-20261028-a.log. Comparacao integral do C
nativo com backup confirmou apenas EXPORT_SYMBOL_GPL(sched_setattr); corpo
e checks de permissao/LSM/limites inalterados. nm confirma export no objeto,
nao no kernel/imagem antiga. Patch sched-setattr-checked-export-v1.patch exige
rebuild/relink real de vmlinux antes de gerar symvers/candidato compativel;
nao foi inserida entrada manual nem usado nocheck para satisfazer MODPOST.

GLUE cria1/3tasks paradas, configura politica/prioridade/nice/custom_slice
com API checked, obtem refs antes de acordar todas, e reverte tasks paradas
em cada erro antes de qualquer callback executar. Stop usa completions
existentes e so entao solta refs; reinit evita completion antiga em reset.
Os dois callers agora propagam falha de pre-net-register: probe usa cleanup
NET_REGISTER_FAIL existente, reset nao anuncia sucesso. Falha de scheduler
antes ignorada agora falha startup e faz rollback, sem reduzir prioridade
silenciosamente. Callbacks/wakelocks das threads e ordem de join permanecem.

Teste de funcoes reais com doubles passou ASan/UBSan em1/3threads:
falha de cada create (-ENOMEM), cada scheduler (-EPERM), zero wake parcial,
rollback, politica desativada/ativa, busy sem sobrescrever task, refs apos
completion, stop repetido e restart/reinit. Log
work/gen4m-thread-start-host-20261028-a.log. Reconstrucao fuzz0 desde gl_init
LG original com prerequisitos; patch gen4m-thread-start-scheduling-v1.patch
e baseline final byte-identico. Doubles nao validam scheduler/LSM ou threads
reais, locking global WMT, callbacks em remove ou reset completo no aparelho.
Nenhum callback foi executado no hardware. Config e imagem BTv14 mantem
hashes anteriores; somente fontes/objetos offline preparados, nao boot image.
Modulo Wi-Fi/link continuam pendentes de kernel export/WEXT real, adaptor,
memoria/cache e demais gates DT/ICC/MPU/WMT/P2P-DFS/recuperacao.

#### Gen4m: dependencias nativas de link — decisao previa2026-10-28

Entrega offline: resolver MODPOST com implementacoes reais, antes de qualquer
ensaio de Wi-Fi/IP/trafego. Reusar cfg80211 Linux6.18.58 configurado=m e
Kbuild single .ko (Makefile2016..2034), sem alterar config ou usar WARN para
aprovar simbolo ausente. Compilar net/wireless/cfg80211.ko no mesmo O=/ARCH/
toolchain da arvore alvo; o MODPOST nativo gera tabela real com vmlinux.o.
Backup verificado de Module.symvers, .cmd, vmlinux.symvers/.cmd e .config em
work/gen4m-kernel-link-backup-20261028-v1 antes da operacao. Nao alterar
imagens, capsula/registry BT ou firmware. Fonte upstream GPL-2.0 na arvore
local6.18.58 sem Git HEAD; nao e implementacao nova a auditar por outro SoC.
Exports WMT devem vir de Module.symvers real do stage WMT ja construido,
nao tabela escrita manualmente. Adaptor Wi-Fi LG e backend cache ainda
precisam ter fonte/API/ownership confirmados se restarem apos dependencias.
Triagem mainline/pmaports/MediaTek/Qualcomm vinculada favorece estes mesmos
frameworks/fornecedores existentes; nenhum stub ou nova abstracao justificado.
Aceite dirigido: build da dependencia, MODPOST sem ignorar erros, fornecedor
para cada simbolo residual e configuracao/imagens preservadas. Nao e prova
de carga/compatibilidade runtime ou autorizacao fisica.

Resultado deps2026-10-28: cfg80211.ko gerado pelo Kbuild real, log
work/gen4m-native-cfg80211-build-20261028-a.log, vermagic
6.18.58-k40s-nativeusbemmc1-NOT-FOR-FLASH SMP mod_unload ARMv7 p2v8.
CONFIG_CFG80211=m preservado; dependencia declara regulatory.db e sua
assinatura, nao valida banco regulatorio existente no futuro initramfs.
Single .ko regenera Module.symvers apenas para modulos selecionados. Para
preservar exports nativos anteriores, compilaram juntos cfg80211 e os tres
fornecedores ja presentes na tabela antiga: crypto/ecc, crypto/ecdh_generic,
net/bluetooth/bluetooth. Log work/gen4m-native-link-deps-build-20261028-b.log.
Copias anteriores dos tres .ko tambem preservadas no backup. Comparacao de
todas as linhas da tabela antiga confirmou subset exato da nova tabela real,
sem merge manual, symbols inventados ou perda de exports BT/crypto.

Com cfg80211 e KBUILD_EXTRA_SYMBOLS do WMT real, gen4m recompilou e MODPOST
passou de61 para14 simbolos externos faltantes; ainda falhou, log
work/gen4m-lts-module-wmt-symbols-20261028-a.log. Lista completa derivada de
nm contra as duas tabelas em work/gen4m-link-residual-symbols-20261028-a.log;
__this_module e objeto gerado pelo Kbuild, nao dependencia externa. Grupos:
6 exports existentes em adaptor/wmt_cdev_wifi.c (loaded status, modo P2P,
file buf handler, low latency e reset start/end);6 do antigo built-in adapter
(2 wrappers stack/cache e4 variaveis de memoria); sched_setscheduler nao
exportado; wireless_send_event exige WEXT_CORE, desativado na config atual.
Nao copiar o built-in4.9 inteiro, usar sucesso no-op ou definir memoria0 para
aprovar. Proximos incrementos devem portar adaptor LG com rollback/lifetime,
resolver APIs nativas scheduler/cache/DT-memory e configuracao WEXT real em
candidato apropriado, preservando kernel/imagem ja validados.

Config byte-identica ao backup; imagem BTv14 hash verificado
2938ca25648cb732c7b31b800df64ee04f9200e3563a6a315dbc2d0c58bd7fa0.
Nenhuma imagem/registry/runner/firmware alterados, nenhuma carga/flash/RF ou
configuracao ficticia. Nao existe .ko Wi-Fi completo. Gates DT/ICC/MPU/
threads/WMT/P2P-DFS/recuperacao e autorizacao fisica permanecem.

#### Gen4m: regulatory domain sem array temporario — decisao previa2026-10-28

Entrega visada: compilar ultimo objeto conhecido rlm_domain.o preservando
canais DFS/regulatorios/potencia para futuro Wi-Fi/IP/trafego. Frame1288>1280
vem de RF_CHANNEL_INFO[64] usado apenas pela consulta rlmDomainIsDfsChnls.
Reusar enumeracao LG de rlmDomainGetDfsChnls em helper privado compartilhado,
com lista opcional e retorno de match. Wrapper publico continua preenchendo
lista; predicate usa listaNULL e mesmo limite64. Preservar ordem, bandas,
fgEnable5GBand, flagDFS, rlmIsValidChnl, span/wrap uint8 e cap de validos.
Nao duplicar algoritmo, reduzir64 para63, criar buffer global/mutex ou alocar
memoria cujo erro poderia classificar DFS como naoDFS. Pequeno helper local
justificado para reutilizar caminho completo sem array; nao e framework novo.
Triagem mainline/pmaports/MediaTek/Qualcomm vinculada nao comprova substituto
AXI/firmware6765; nao importar tabela de outro SoC ou mudar dominio/power.
Sem RE, probe/remove novo, firmware ou novos efeitos eletricos.

Fonte LG dual GPLv2/BSD, snapshot sem commit: mgmt/rlm_domain.c SHA256
49401691d5407af4123221011681d05c1b103db2abf224488fdb55c8d2981296;
include/mgmt/rlm_domain.h SHA256
50bf1bb1fa123a1a8e2da945bfa6ffd423956d2924572a45ea9958a8a0c574cf.
19 nomes com referencias apenas no mesmo C: static quando usados, globais
sem uso ativo preservados com declaracao no header proprio. Nao adicionar
callers ou mudar corpos de power limits. Aceite dirigido: ARM/Werror sem
relaxar frame limit; comparar enumerador/predicate LG original e adaptado
para todos os canais, caps64/65, bandas/validade/DFS e campos de saida.
Depois tentar build/link completo para identificar proximo bloqueio real.

Resultado domain2026-10-28: rlm_domain.o inteiro compila ARM/Werror sem
relaxar frame limit, work/gen4m-lts-domain-build-20261028-a.log.19 helpers
privados static; header rlm_domain.h nao alterado. Enumerador/predicate reais
LG antes/depois passaram ASan/UBSan, work/gen4m-domain-host-20261028-a.log:
todos os valores uint8 de canal em casos dirigidos de bandas/DFS/validade,
5G desativado, span0/duplicatas, wrap8, caps0/1/3/63/64/65/255. Comparou ordem
de consultas de validade, contagem, todos os campos/padding e bytes fora da
saida. Confirmou64 presente/65 ausente no predicate legado com65 candidatos.
Reusa RF_CHANNEL_INFO original20bytes de include/nic/wlan_def.h LG dual
GPLv2/BSD SHA256original
d0d074535e321e87b761cadd4679fdf428a0d905ac6a27cef0874273bcb03c58,
sem reduzir struct ou alocar memoria. Comparacao integral confirmou demais
corpos de potencia/regulacao identicos, work/gen4m-domain-equivalence-20261028-a.log.
Patch gen4m-domain-stack-linkage-v1.patch reconstruido fuzz0 pelo teste;
baseline recebeu copia final byte-identica. Teste usa doubles de dominio/
validade; nao comprova tabela/regulacao ou DFS real no aparelho.

Build completo work/gen4m-lts-module-build-20261028-d.log compilou todas as
unidades C e gerou wlan_drv_gen4m.o, mas falhou no MODPOST com61 simbolos nao
resolvidos. CONFIG_CFG80211=m no kernel, mas cfg80211.ko nao existe nesse
build e Module.symvers nao contem cfg80211. WMT externo nao foi passado em
KBUILD_EXTRA_SYMBOLS; sua tabela existente inclui msgcb_unreg e power_off_flag.
Nao criar exports ficticios, ignorar modpost ou inferir que todos os61 sao
somente tabelas ausentes: update_driver_loaded_status e cache flush precisam
ter fornecedor/ABI confirmados. Proxima etapa: compilar dependencias nativas
reais, integrar symvers corretos e resolver somente lacunas que persistirem.
Sem alterar imagem/registry/capsula BT ou autorizacao fisica. Ainda nao existe
.ko Wi-Fi completo; gates DT/ICC/MPU/threads/WMT/P2P-DFS/recuperacao mantidos.

#### Gen4m: P2P func ABI — decisao previa2026-10-28

Entrega visada: fechar unidade p2p_func.o para modulo Wi-Fi6.18. Reusar API
cfg80211_ch_switch_notify(dev,chandef,0), link0 obrigatorio para naoMLD em
Linux6.18.58 include/net/cfg80211.h/net/wireless/nl80211.c GPL-2.0. Preservar
chandef, fluxo LG e comandos;14 helpers sem referencias externas podem ser
static quando usados localmente, mantendo globais legados sem uso declarados
em p2p_func.h. Quedas intencionais recebem fallthrough. Sem novo driver,
framework ou RE; triagem mainline/pmaports/MediaTek/Qualcomm vinculada nao
comprova substituto AXI6765, e nao resolve detalhe de linkage/ABI desta fonte.
LG dual GPLv2/BSD snapshot sem commit, mgmt/p2p_func.c SHA256original
563fe0d277f35553e62d31d4ab99140656494bb5b05005a852533f3632f81477.

Gate encontrado na leitura da API: ch_switch_notify e check_beaconing(relax)
exigem wiphy.mtx; RTNL LG nao satisfaz esse contrato6.18. Chamadores sao FSM
P2P e cfg80211 LG contem kalIoctl sincrono para thread compartilhado. Nao
adicionar wiphy_lock bloqueante nesse thread sem resolver inversao/lifetime.
Esta etapa preserva corpo/locking LG e fecha somente tipos/linkage, nao
autoriza ou valida DFS/P2P no aparelho. Integracao de contexto/notificacao
assincrona e recuperacao, inclusive falhas de chandef/channel alloc e ponteiro
de channel persistente, precisam ser fechadas antes de ativar esse caminho.
Aceite dirigido: objeto ARM/Werror e equivalencia de corpos normalizando
somente static, fallthrough e link_id0. Sem teste espelho ou alegacao de
correcao de locking a partir de mocks; firmware/RF/DT nao sao alterados.

Resultado P2Pfunc2026-10-28: mgmt/p2p_func.o e consumidor p2p_role_fsm.o
inteiros compilam ARM/Werror, work/gen4m-lts-p2p-func-build-20261028-b.log.
12 helpers locais static; p2pFunMgmtFrameTxDone e
p2pFuncComposeBeaconProbeRspTemplate globais sem uso ativo preservados com
declaracoes em include/mgmt/p2p_func.h LG dual GPLv2/BSD, snapshot sem commit,
SHA256original 09efa1dd79293a5d3d3351fd8f19a252615e5509dbd16512c64fadf3970b0500.
Comparacao integral confirmou apenas linkage,4 fallthrough, link_id0 e2
declaracoes, preservando demais corpos/locking/comandos/falhas existentes:
work/gen4m-p2p-func-equivalence-20261028-a.log. Sem novo caller, stubs ou
suppressao. Patch gen4m-p2p-func-abi-v1.patch passa dry-run fuzz0 nas duas
fontes LG originais; baseline recebeu copias finais byte-identicas.
Nao ha claim de callback seguro no runtime: contexto/wiphy mutex, alocacao
chandef/channel, canal canonico/lifetime e recuperacao do DFS continuam gates
concretos antes de ativa-lo. Nenhum teste RF/DFS ou mock foi usado para
declarar esse locking resolvido. Resta rlm_domain conhecido na compilacao;
link/modpost e demais gates gerais ainda nao foram concluídos.

#### Gen4m: stats realtime64 — decisao previa2026-10-28

Entrega visada: fechar stats.o para futuro Wi-Fi associado/IP/trafego. Reusar
ktime_get_real_ts64, rtc_time64_to_tm e tv_nsec/NSEC_PER_USEC Linux6.18.58
(include/linux/timekeeping.h, rtc.h; GPL-2.0), como demais adaptacoes de tempo.
Preservar relogio real UTC, formato microsegundos, contador/delay sched_clock,
filtros IP/portas/limiares e fallthrough TCP/UDP->ICMP. Nao trocar logs por
no-op, clock ficticio ou misturar boottime WMM. Tres parsers exclusivamente
locais recebem static; duas quedas recebem fallthrough. Indentacao DNS sera
alinhada ao controle real existente: somente flag independent e condicional,
log permanece incondicional nesse ramo (nao acrescentar braces silenciosamente).
Triagem mainline/pmaports/MediaTek/Qualcomm desta matriz nao demonstra outro
driver AXI6765; APIs nativas resolvem esta lacuna sem copiar transporte,
reescrever parser ou adicionar diagnostico/framework. Sem RE.
Fonte LG dual GPLv2/BSD snapshot sem commit: mgmt/stats.c SHA256
7bfb196aacb34434e8f1513d545d4ae69ccdc66a4887da147a483896c857ffef.
Aceite dirigido: objeto ARM/Werror, funcao real de timestamp com API doubles
em limites us/ns e filtros/limiares, comparacao dos outros corpos. Parsers
LG de tamanho/IP options/headroom nao sao declarados validados por este port.
Sem novos efeitos de probe/remove, DMA, firmware, PMIC ou limites eletricos.

Resultado stats2026-10-28: mgmt/stats.o inteiro compila ARM/Werror, log
work/gen4m-lts-stats-build-20261028-a.log. Teste host ASan/UBSan da funcao
RX real passou filtros flag/len/EtherType/IP version/protocolo/porta,
TCP/UDP->contagem, ICMP, limiar antes/igual/depois e formato completo do log
com ns0/999/1000/123456789/999999999 -> us0/0/1/123456/999999. Amostra real64
acima2038 entregue intacta ao double RTC: work/gen4m-stats-host-20261028-a.log.
Nao comprova RTC/clock/skb reais ou todos os parsers LG; teste usa buffers
lineares validos. Comparacao do arquivo inteiro, normalizando somente APIs
de tempo, static, fallthrough e indentacao inicial, conservou tokens,
controle e strings: work/gen4m-stats-equivalence-20261028-a.log. Log DNS
incondicional legado preservado; nao foi transformado em evento somente RX.
Patch gen4m-stats-realtime-v1.patch reconstruido fuzz0 pelo teste; baseline
recebeu copia final byte-identica. Sem novos diagnosticos, firmware ou
alteracao de capsula BT. Restam rlm_domain e p2p_func conhecidos no build;
link/modpost, modulo completo e gates do aparelho continuam pendentes.

#### Gen4m: scan sem VLA — decisao previa2026-10-28

Entrega visada: fechar scan.o para futuro Wi-Fi associado/IP/trafego. Reusar
limite LG SCAN_LOG_MSG_MAX_LEN500 de include/mgmt/scan.h: todos os callers
ativos de flush passam esse limite. Trocar VLA controlado por argumento16bit
por array local constante500, com tamanho efetivo min_t(uint16_t,arg,sizeof).
Preserva agrupamento para pedidos<=500, formatos MAC completo/mascarado,
prefixos, esvaziamento da lista e aviso/drain para buffer pequeno. Pedidos
maiores sao divididos em linhas<=500, sem perder BSS ou alocar memoria.
Linux6.18 min_t em include/linux/minmax.h GPL-2.0 e limite vendor bastam;
nao criar buffer global compartilhado, allocator/framework ou diagnostico novo.
Triagem mainline/pmaports/MediaTek/Qualcomm vinculada nao demonstra substituto
AXI6765 e nao exige reescrita do scan LG para esse erro. Sem RE.
Quatro helpers com referencias apenas locais recebem static; duas quedas
intencionais recebem fallthrough. Sem mudar algoritmos de canais/bitmap/BSS.
Fonte LG dual GPLv2/BSD snapshot sem commit: mgmt/scan.c SHA256
127975ebd50c0b29ca081edb9b5e5492fc4bfeab5ac885a4fe05812f57e3f8b2.
Aceite dirigido: objeto ARM/Werror, comparacao dos demais corpos e teste da
funcao real original/adaptada para tamanhos validos e buffers0/curtos/grandes,
lista vazia/invalida,200 BSS, MAC completo/mascarado e prefixo suprimido.
Sem efeito novo de probe/erro/remove, SoC/PMIC, limites eletricos ou firmware.

Resultado scan2026-10-28: mgmt/scan.o inteiro compila ARM/Werror sem VLA ou
relaxamento de frame limit, work/gen4m-lts-scan-build-20261028-a.log. Limite
reusado de include/mgmt/scan.h LG dual GPLv2/BSD, snapshot sem commit,
SHA256original 0d5783044fc7f61c7fd47f307831e04612473f1fc7c22703659af241ccd6e8ce;
header nao alterado. Array500 local nao acrescenta alocacao que possa dormir
ou falhar; nao usa buffer compartilhado entre scans. Tamanho efetivo limitado
ao menor entre pedido e500, com tratamento antigo de buffer curto mantido.
Teste host ASan/UBSan comparou funcao LG original/adaptada, formatos MAC
completo/mascarado, prefixos FW/CFG/D2D, listas0/100/200, tamanhos1..500 nos
limites relevantes, pedidos501/65535 divididos como500, tamanho0 e lista
invalida. Confirmou mesma saida para tamanhos suportados e drain sem perda;
work/gen4m-scan-buffer-host-20261028-a.log. Doubles exercitam list/log APIs,
nao list locking/scan real. Comparacao integral confirmou demais corpos
intactos, work/gen4m-scan-equivalence-20261028-a.log. Patch
gen4m-scan-fixed-buffer-v1.patch reconstruido fuzz0 pelo teste; baseline
incremental recebeu copia final byte-identica. Nao houve mudanca de selecao
de rede/canais/regulacao, nem validacao de todos os payloads/bitmaps LG.
Restam rlm_domain, stats e p2p_func conhecidos no build, sem .ko completo ou
novo resultado fisico. Gates DT/provider/MPU/threads/WMT/recuperacao mantidos.

#### Gen4m: WMM boottime — decisao previa2026-10-28

Entrega visada: compilar admissao WMM sem retirar limites de airtime ou timer,
para futuro Wi-Fi com IP/trafego. Reusar ktime_get_boottime_ts64 do Linux6.18.58
local include/linux/timekeeping.h GPL-2.0: converte o mesmo ktime_get_boottime
usado por get_monotonic_boottime ARM4.9. Conserva tempo incluindo suspend,
resolucao, campos/ciclos32bit LG, segundos de intervalo e ms de timer+20.
Nao substituir por realtime/monotonic sem suspend. Triagem mainline/mt76,
pmaports/MediaTek/Qualcomm vinculada nao demonstra substituto AXI6765; API
nativa de tempo resolve a lacuna, sem novo algoritmo, framework ou RE.
WmmComposeTspecIE local pode ser static; DumpData global sem chamadores
ativos sera preservado com declaracao no header WMM, sem ativar #if0 antigo.
Fontes LG dual GPLv2/BSD, snapshot sem commit: mgmt/wmm.c SHA256
6d0cba8e3144cdd90b600c902f94f0d73b348bc41f1936b7f4cc3c4cb023adf5.
Aceite dirigido: objeto ARM/Werror, comparacao dos demais corpos e teste da
funcao real em limites de admissao, tempo/intervalo e timer ja pendente.
Nao altera indice AC/BSS, recuperacao, DMA, firmware ou limites eletricos;
valida apenas o contrato de tempo afetado, nao WMM/TSPEC real no aparelho.

Falha concreta WMM: teste da funcao real com primeira amostra10.999s e
segunda11.100s, intervalo terminando11s, reproduziu falha de aceite em
work/gen4m-wmm-host-20261028-b.log. Subtracao u32 antiga converte atraso
vencido em espera proxima49 dias. Corrigir usando TIME_BEFORE modular LG
ja existente: se prazo futuro, conservar delta+20ms; se vencido/igual,20ms.
Nao alterar refill, budget, deq, clock, recuperacao ou liberacao de timer.
Isso e ajuste localizado de falha temporal demonstrada, nao relaxamento de
limite. Clock64 tambem evita multiplicacao assinada32 de segundos por1000;
campos/timers LG continuam mod32, sem mudar suas unidades ou limiares.

Resultado WMM2026-10-28: mgmt/wmm.o inteiro compila ARM/Werror, log
work/gen4m-lts-wmm-build-20261028-b.log. Header include/mgmt/wmm.h LG dual
GPLv2/BSD SHA256original
08403b07b47c841437e976a933c430492c78b3ac9af4131db373a6703187bab9:
apenas declaracao de DumpData global ja existente. Teste host ASan/UBSan
da funcao real e struct SOFT_ACM_CTRL passou ausencia WMM/admissao, fast
check, budget parcial/exato, timer pendente, refill no limite e salto de
boottime, fracoes ns/ms e wrap dos contadores32. Regressoes incluem prazo
vencido entre leituras, antes falhando e agora20ms; log
work/gen4m-wmm-host-20261028-c.log. Mantido comportamento LG de consumir
budget exato/incrementar deq mas retornar FALSE quando resto chega a zero.
Comparacao integral work/gen4m-wmm-equivalence-20261028-a.log confirmou
demais corpos identicos. Patch gen4m-wmm-boottime-v1.patch reconstruido
fuzz0 pelo teste; baseline recebeu dois arquivos finais byte-identicos.
Sem novo clock/timer framework, alteracao de airtime, firmware ou hardware.
Nao comprova timer/NAPI/suspend reais, TSPEC negociado ou concorrencia de
AC/BSS. Restam rlm_domain, scan, stats e p2p_func no build; modulo completo
e gates anteriores do aparelho continuam pendentes. Nenhum ensaio fisico.

#### Gen4m: linkage management — decisao previa2026-10-28

Entrega visada: fechar grupo de declaracoes management que impede modulo
Wi-Fi6.18, preservando associacao/roaming/TKIP/RLM/filas e USB/SSH como alvo
do aceite no aparelho. Busca de referencias em todos os C/headers gen4m para
31 nomes diagnosticados mostra referencias apenas no arquivo definidor.
Aplicar linkage static aos helpers usados localmente; se funcao global LG
nao tiver chamadores, preservar corpo/simbolo com declaracao no header proprio,
sem inventar uso, retirar protecao ou usar __maybe_unused para aprovar build.
Reusar source LG existente e seus headers; triagem mainline/pmaports/MediaTek/
Qualcomm desta matriz nao demonstra substituto AXI6765 e nao e necessaria
reescrita de algoritmo para um erro de linkage. Sem framework ou RE.

Fontes LG snapshot sem commit, todas dual GPLv2/BSD conforme cabecalhos;
caminhos gen4m e SHA256 da origem antes de patches:

| Arquivo | SHA256 original |
| --- | --- |
| mgmt/aaa_fsm.c | 2b08f5d0a39601d774a4815f5ba9c7905e1e0a0af3623994a2d83c103b11299b |
| mgmt/ais_fsm.c | 8c3639a2f9f51343c49235f2f2490c4b1fd3185587b9bea54976d6121e0b1915 |
| mgmt/assoc.c | 7648d7dd50d29e73401713984c489c6a0cb0398781c2706797a4dd2d7e57c684 |
| mgmt/bss.c | e774b306f7e83cdec3b8edc4b83f6f1fcdbddbd18bb9967dd623bbba63e089c3 |
| mgmt/cnm.c | 7107696ab7f0d5d057341d9fa144cbbe0451c4c63a730b58581d508ee6c37e4f |
| mgmt/cnm_mem.c | bb5b0c8cc6105be37718931e7185be74fb9b990fdabc075600be881cec320966 |
| mgmt/hem_mbox.c | ba070ebe5800b52471b8f62c5fc85445878a6b97ad23bc519b67b0ef0fc7d0f4 |
| mgmt/rlm.c | dade1376a4fb3e3e806a86e067ce9a6c64c60a17a7cc9a4278070c719fa91bea |
| mgmt/rlm_obss.c | ad606d38ce7c25fd4768b39f48a3a89bf0a6094ce197231d375548c3605be2d9 |
| mgmt/swcr.c | 3823f86ff8d47fd53e901ce02be83234485cb56a10c0b0f23eda92722c9a6b53 |
| mgmt/tkip_mic.c | a66d0dafd1749d06917870be87d0a027ab4d10a515e4e09d29903efd71fc249d |
| mgmt/ap_selection.c | 9e497199dc09474dd5f35c75e63ab48b2a5212686c0109137a672973fffc8d7a |
| mgmt/p2p_role_fsm.c | 3c763aea1ba65536c8083a9a62b9c4f8ab8e44296e5513da798d0f2f1755dbb5 |
| mgmt/p2p_ie.c | b7d1503b024b5276504505553c4f02a5719d58290ed6b5a18679bfb002c3c468 |

Esforco restrito a linkage/prototipos, sem parte nova de SoC/PMIC/placa,
probe/erro/remove ou algoritmo alterado. Cnm preserva adaptacao wakeup_source
anterior. Aceite dirigido: comparar arquivos inteiros com baseline anterior
normalizando somente linkage e compilar unidades ARM/Werror. Sem testes
espelho de declaracoes nem repetir suites de comportamento sem corpo mudado.

Resultado management2026-10-28: as14 unidades visadas compilam ARM/Werror,
work/gen4m-lts-management-linkage-build-20261028-b.log. Sao26 helpers privados
static e5 globais sem chamadores preservados com declaracao em header:
bssCreateStaRecFromAuth, bssUpdateStaRecFromAssocReq, rlmObssUpdateChnlLists,
tkipMicEncapsulate e wfdFuncAppendAttriDevInfo. Nao foi adicionado chamador,
stub, no-op ou suppressao; os corpos vazios/retorno TRUE ja existentes dos
primeiros helpers LG permanecem limitacoes originais, nao funcoes entregues.
Headers LG dual GPLv2/BSD, snapshot sem commit, SHA256 original:

| Header gen4m | SHA256 original |
| --- | --- |
| include/mgmt/bss.h | d55354705063f0cbf085d4836d83946c7b7f859baf25cdd35f1f2c683ec4e06d |
| include/mgmt/rlm_obss.h | 405648500a6e3143cca69a9449532e2d0c7ea33572caf94faff9348b6bdc41fa |
| include/mgmt/privacy.h | 241e4ccd064c876e9949c1645e208fb3934345d0f854353669c2ca7c40e4c7a9 |
| include/mgmt/p2p_ie.h | 2756bf8f800ad805eb2e2fff158a8aaa563c756564674077c5ac88b88c5205d5 |

Comparacao integral work/gen4m-management-linkage-equivalence-20261028-a.log
confirma corpos C identicos ao baseline anterior apos normalizar apenas static,
e headers com apenas5 declaracoes. Sem teste espelho novo ou mudanca de TKIP,
RLM, roaming, limites ou clocks. Patch gen4m-management-linkage-v1.patch passou
dry-run fuzz0 sobre baseline incremental (cnm com prerequisito wakeup_source);
18 arquivos finais de baseline conferidos byte a byte com stage,16 alterados.
Quatro headers compartilhados justificaram rebuild dos consumidores/modulo,
work/gen4m-lts-module-keep-going-20261028-c.log: terminou com falha apenas nas
unidades mgmt/rlm_domain.c, scan.c, wmm.c, stats.c e p2p_func.c (linkage,
stack/VLA, tempo/RTC/fallthrough e channel switch). Demais unidades alteradas
passaram tambem nesse rebuild. Nao houve link/modpost ou modulo completo.
Nenhum novo resultado no aparelho, RF/flash ou alteracao de capsula BT;
gates DT/provider/MPU/threads/WMT/recuperacao anteriores permanecem.

#### Gen4m: headers LG ja existentes — decisao previa2026-10-28

Entrega visada: compilar hooks QA e estados P2P que bloqueiam modulo Wi-Fi,
sem ativar QA/ATE ou alterar estados. Aceite final: associacao/IP/trafego no
aparelho e USB/SSH preservado. As declaracoes ja existem em gl_hook_api.h,
p2p_dev_state.h e p2p_role_state.h; os respectivos arquivos C nao as incluem.
Reusar esses headers LG apos precomp.h, mantendo guard QA existente. Os FSMs
consumidores P2P ja usam esses mesmos headers. Nao criar prototipos paralelos,
substituir implementacoes por mainline/mt76/pmaports/MediaTek/Qualcomm da
triagem vinculada, ou importar framework para resolver include ausente.
Nao ha mudanca de hardware/transportes, probe/erro/remove ou licenca;
esforco limitado a tres includes. Sem codigo novo ou engenharia reversa.

Origem LG snapshot sem commit, todos dual GPLv2/BSD conforme cabecalho:

| Arquivo gen4m | SHA256 original |
| --- | --- |
| os/linux/gl_hook_api.c | 058bf0f666cf5ac3c1ba1ea1bfaa0dc6d2df9d8b3569ee2c7e879b71c6f6fef0 |
| os/linux/include/gl_hook_api.h | ef2fa3e7e3da678008e8a1d31b2b0de60c9476a9493ca3d20d5d2ba58d228a91 |
| mgmt/p2p_dev_state.c | 1336efdf3f61946687bd2d835f58bb63251f813d5dbc9ab4fb304485dc275a94 |
| include/mgmt/p2p_dev_state.h | 6a8753623736f423b917a6d8fe6d7beff922416a5176504a8b72ea5cabf47eb3 |
| mgmt/p2p_role_state.c | 49e3678946b06fced85de45b3e15a866e8b29306d01fb19a247c6e72948ecc1f |
| include/mgmt/p2p_role_state.h | 0e72230f7e95c443c378edc9e9e6b7e57bc4353247e84b6b47ca90671c8ab05c |

Aceite dirigido: tres objetos ARM/Werror, tipos conferidos pelo compilador e
corpos C/headers existentes preservados. Nao criar teste que apenas procure
includes. Nenhuma execucao QA/ATE, escrita efuse, RF ou ensaio fisico permitida.

Resultado headers2026-10-28: gl_hook_api.o, consumidor gl_ate_agent.o e
p2p_dev_state.o/p2p_role_state.o compilam inteiros ARM/Werror, log
work/gen4m-lts-existing-headers-build-20261028-b.log. Tres includes resolveram
as declaracoes ja presentes. Faltava somente TxBfBssInfoUpdate no header de
hooks: adicionada declaracao de mesmo tipo/argumentos, preservando funcao
global existente sem chamadores na arvore; nao criado caller ou alterado corpo.
Comparacao integral confirmou tres corpos C intactos, apenas aquela declaracao
nova e os dois headers de estados byte-identicos aos originais, log
work/gen4m-existing-headers-equivalence-20261028-a.log. Sem teste espelho novo
ou suite ampla: compilador verifica os tipos e consumidor afetado foi recompilado.
Patch gen4m-existing-headers-v1.patch passa dry-run fuzz0 nas quatro fontes;
baseline incremental recebeu copias finais conferidas por SHA256. Nenhuma
mudanca de QA/ATE, comando, limites, imagem ou autorizacao. Modulo completo
ainda depende de linkage management, tempo/RTC, stack/VLA e API channel switch.
Nao houve novo funcionamento no aparelho; gates fisicos anteriores permanecem.

#### Gen4m: P2P NAPI/MAC/CAC — decisao previa2026-10-28

Entrega visada: fechar tres unidades P2P que impedem modulo Wi-Fi6.18;
aceite no aparelho permanece associacao/IP/trafego com USB/SSH. Reusar
netif_napi_add_weight preservando peso64, eth_hw_addr_set para atualizar
endereco e bookkeeping nativo, e cfg80211_cac_event com link0 naoMLD.
Linux6.18.58 local include/linux/netdevice.h, etherdevice.h (GPL-2.0),
net/core/dev_addr_lists.c e net/wireless/mlme.c (GPL-2.0) sao as APIs alvo;
nao copiar campos const nem converter casts para contornar prototipos.
As alternativas mainline/mt76/pmaports/MediaTek/Qualcomm da matriz nao
demonstram substituto AXI/firmware6765; adaptar os callbacks LG existentes
e menor caminho para esta ABI, sem driver paralelo ou engenharia reversa.

Origem LG snapshot sem commit, todos dual GPLv2/BSD conforme cabecalho:
os/linux/gl_p2p.c SHA256 62122072abb812d1544e66c7c3057e0dd491295d86318c20c825fbaa523e4de8;
os/linux/gl_p2p_cfg80211.c SHA256 51dcaa0f55494c9da394e28ba26e6b9117ec9acbcea469363a066fc617ce2b7b;
os/linux/gl_p2p_kal.c SHA256 3cd775a0d4f818ec324e2491541c24fec764223d77c6a67cf47f43f7eb8188f5.
Manter derivacao dos MACs, perm_addr, callback NAPI e ordem de teardown.
Driver nao anuncia MLO: cac_started migra para links[0], evento FINISHED
usa link_id0; sem remover validacoes/tempo CAC do cfg80211 ou alterar
sequencia radar/carrier/queues/free LG. Helper mgmt_tx usado apenas no
mesmo arquivo recebe static; duas quedas intencionais usam fallthrough.
Verificar build ARM/Werror e callbacks CAC/radar com API doubles focados;
nao prova DFS real, autorizacao RF ou uso seguro de todos os roles P2P.

Resultado P2P2026-10-28: gl_p2p.o/gl_p2p_cfg80211.o/gl_p2p_kal.o inteiros
compilam ARM/Werror, work/gen4m-lts-p2p-build-20261028-a.log. Comparacao
integral confirmou corpos originais apos normalizar apenas as APIs citadas,
linkage e fallthrough: work/gen4m-p2p-equivalence-20261028-a.log. Peso NAPI64,
formacao de MAC/perm_addr, mgmt TX e sequencia radar/filas/free preservados.
Patch gen4m-p2p-linux618-api-v1.patch reconstruido sobre tres fontes originais
com fuzz0; baseline incremental recebeu copias finais byte-identicas.
Teste host ASan/UBSan executou callbacks CAC/radar originais e adaptados,
dois roles, GLUE/chandef ausentes, canal ausente, evento CAC sem liberar
chandef e radar com carrier off/queues stop antes de free. Verificou link0
e slot1 intacto; work/gen4m-p2p-cac-host-20261028-a.log. Usa doubles de APIs,
nao exercita NAPI real, netdev locking, validacao/temporizacao DFS cfg80211
ou regulacao/transmissao real. Indices/ponteiros de roles e concorrencia do
codigo LG continuam contratos a validar antes de ativar esses caminhos.
Nenhum novo aceite no aparelho; management/gl_hook_api e gates anteriores
ainda impedem modulo completo/ensaio. Nao houve ativacao RF ou flash.

#### Gen4m: WEXT no perfil nativo — decisao previa2026-10-28

Entrega visada: remover bloqueio WEXT do build Wi-Fi sem eliminar comandos
LG; aceite no aparelho continua associacao/IP/trafego e USB/SSH preservado.
Linux6.18.58 local include/net/iw_handler.h condiciona os quatro campos de
private ioctls a CONFIG_WEXT_PRIV. Perfil atual nao habilita WEXT_PRIV nem
CFG80211_WEXT. Usar esse mesmo guard apenas na tabela rIwPrivHandler e nos
quatro campos, preservando tabela de argumentos, handlers e dispatch LG por
ndo ioctl. Nao criar Kconfig ficticio nem remover o caminho de comandos.
Reuso mainline/pmaports/MediaTek/Qualcomm ja triado nesta matriz: API WEXT
nativa resolve o detalhe de ABI; nao justifica trocar AXI/firmware6765 por
mt76 ou transporte Qualcomm nao equivalente. Sem engenharia reversa.

Fonte LG snapshot sem commit, ambos dual GPLv2/BSD conforme cabecalho:
os/linux/gl_wext.c SHA256 db7784408bbf97fcfdf63c5a9bd4f217624499f68a4516ab84f01e3727e3512c;
os/linux/gl_wext_priv.c SHA256 2e6da0ae6b267fda3a05ad43b275ebd0d658373e5554ce755c4570043445dfc2.
Helpers sem referencia externa podem receber static, preservando corpos.
access_ok(addr,size) nativo substitui variante VERIFY_READ/WRITE removida;
manter os mesmos ponteiro/comprimento, retorno EFAULT e copy_from_user real.
Linux include/asm-generic/access_ok.h GPL-2.0 e arch/arm/include/asm/uaccess.h
sao a API alvo. Isto nao valida tamanhos de buffers ou concorrencia dos
private ioctls LG: esses contratos continuam obrigatorios antes de uso real.
Verificar equivalencia dos corpos/argumentos e compilar os dois objetos com
Werror. Nao ampliar auditoria ou criar driver/helper paralelo para esse ajuste.

Resultado WEXT2026-10-28: gl_wext.o e gl_wext_priv.o inteiros compilam
ARM/Werror no perfil nativo, work/gen4m-lts-wext-build-20261028-c.log.
Comparacao integral work/gen4m-wext-equivalence-20261028-a.log confirma
45 helpers privados static; corpos inteiros identicos apos normalizar
somente linkage e remocao do argumento type nas tres chamadas access_ok
(uma em #if0 preservado). gl_wext.c mantem tabelas/dispatch identicos apos
normalizar guards WEXT_PRIV e linkage de wext_get_priv. ARM4.9 uaccess.h:312
ja ignorava type; ARM6.18 inclui asm-generic/access_ok.h, preservando checagem
de endereco/faixa e copy_from_user, nao validacao de capacidade do destino.
Helper LG global sem chamadores priv_driver_get_dbg_level foi mantido global
com declaracao em os/linux/include/gl_wext_priv.h, dual GPLv2/BSD, origem
SHA256 8a900d264841102482cdc2e738fe64bc388c1ec5838351e510075f6368a271bc.
Nao foi criado caller ou suprimido warning. Nenhum comando foi ativado.
Patch gen4m-wext-linux618-v1.patch passa dry-run sem fuzz nas tres fontes LG
originais; baseline incremental recebeu copias finais conferidas por SHA256.
Perfil WEXT_PRIV on nao foi compilado/ensaiado, codigo foi preservado.
Contratos de tamanho/terminacao de priv_set_driver e __priv_set_ap e buffers
compartilhados ainda precisam ser validados antes de expor private ioctls.
Nao houve modulo completo nem novo resultado no aparelho; P2P e management
permanecem bloqueios reais do build, alem dos gates DT/provider/recuperacao.

#### Gen4m: proc_ops e status limitado — decisao previa2026-10-28

Entrega visada: compilar interfaces proc LG preservando nomes, permissoes,
handlers e seq read/seek/release para bring-up Wi-Fi. Reusar struct proc_ops
Linux6.18.58 include/linux/proc_fs.h e fs/proc/inode.c GPL-2.0: proc_create nao
aceita file_operations; .owner nao existe e proc_entry_rundown bloqueia novas
chamadas, espera em uso e fecha openers. Nao criar wrapper/cast de tabela ou
API paralela. Triagem mainline/pmaports/MediaTek/Qualcomm vinculada nao exige
substituir driver AXI6765 para essa API de filesystem; sem RE.
LG os/linux/gl_proc.c dual GPLv2/BSD SHA256original
8b40217a2800bca8ff90f523a4c099fea981bc7a2226e0e417b0d72b23efca4a,
snapshot sem commit. Trocar tabelas e slots de callbacks mantendo cada alvo.

Leitura drv_status espera fgDrvStatus/evento. Antes de remover entradas no
uninit, desligar flag sob mutex e acordar waitqueue; do contrario rundown de
proc_ops poderia esperar para sempre. Inicializar mutex/waitqueue no comeco
de procInitFs para esse caminho existir mesmo em falha parcial. Nao altera
comandos, permissoes, firmware ou fonte4.9. InitWlan/erros de criacao e demais
lifetimes externos ainda precisam ser fechados antes de unload/ensaio.

Escrita status deve serializar enable/disable com a mesma mutex e recusar
ESHUTDOWN apos flag de teardown, para enable nao recolocar leitor em espera.
Mensagem de status desabilitado usa simple_read_from_buffer Linux6.18
fs/libfs.c GPL-2.0: ramo antigo ignorava count e offsets parciais. Nao mudar
os demais comandos ou permissoes. Testar leitura curta/EOF/falha de copia e
rejeicao de reativacao depois do stop no caminho real.

Rundown precisa preceder destruicao de GLUE/wiphy: mover procUninitProcFs
para inicio de exitWlan, mantendo WMT/bus vivos durante callbacks existentes.
Limpar raizes apos remove_subtree e ignorar raizes ausentes nas remocoes por
radio/cfg, evitando parent pendurado e remocao em raiz global sob init parcial.
Recusar create sem raiz ou apos stop. gl_init.c LG dual GPLv2/BSD/hash ja
registrado; nao ampliar claim de teardown WMT concorrente, ainda gate separado.

glWriteStatus e helper exclusivamente interno: static, timespec64/realtime,
rtc_time64_to_tm e tv_nsec/NSEC_PER_MSEC, conservando ajuste sys_tz e formato.
Reusar vscnprintf Linux lib/vsprintf.c GPL-2.0 para comprimento realmente
armazenado: vsnprintf devolve comprimento desejado e pode causar over-read
do temporario280. Manter ring2048 e mensagens que cabem; excesso trunca ao
temporario, sem suprimir erro ou ler bytes fora dele. Aceite dirigido: objeto
ARM/Werror, slots/tipos, formatter real com wrap/truncamento e ordem de wake
antes de remove. Nao e evidencia de procFS/reset/rede reais no aparelho.

Resultado proc2026-10-28: gl_proc.o e gl_init.o inteiros compilam ARM/Werror,
log work/gen4m-lts-proc-build-20261028-c.log. As doze tabelas preservam os
mesmos alvos read/write/open/seek/release, com slots proc_ops nativos.
Patch gen4m-proc-linux618-v1.patch reconstruido sem fuzz pelo teste, usando
o trecho gl_init do patch DRM como prerequisito; baseline incremental e stage
conferidos byte a byte nos dois arquivos. Fonte LG4.9 preservada.
Teste host ASan/UBSan passou formatter longo/wrap/erros, relogio64/timezone,
leitura curta/EOF/offset/copy fault, comandos, stop/wake/remove e rejeicao de
enable apos stop: work/gen4m-proc-host-20261028-d.log. Usa funcoes LG reais
com doubles de APIs; nao exercita procfs real nem prova concorrencia WMT.
Mutex/waitqueue precedem criacao; rundown precede destruicao de GLUE/wiphy.
Init parcial completo, produtores de status concorrentes e lifetime WMT
continuam gates separados antes de ensaio/unload. Nenhum novo aceite fisico.

#### Gen4m: firmware loader/EMI — decisao previa2026-10-28

Entrega visada: compilar carregador LG sem alterar firmware/endereco ou retirar
protecao sob falha. Reusar ioremap/iounmap, request/release_mem_region,
memcpy_toio e snprintf do Linux6.18.58 local GPL-2.0. Equivalencia ARM4.9
ioremap_nocache->ioremap ja auditada no AXI; nao usar ioremap_cache nem escrever
RAM de outro SoC. Mainline/mt76 tem firmware/protocolo diferentes; triagem
pmaports/MediaTek/Qualcomm vinculada nao comprova substituto AXI6765, portanto
adaptar fonte LG, sem framework/reimplementacao/RE. LG dual GPLv2/BSD, snapshot
sem commit: chips/common/fw_dl.c SHA256original
c8f870f04575908086d8b9d0b2b79c966cae2d1467e64142c1daa84a05a63b76;
chips/connac/connac.c SHA256original
51b574f54db5c9847ef51305898073e60ba969b5314f9fc2df15fc81b8d97fd4.
Busca de consumidores permite oito helpers privados static, sem mudar corpos.

wlanDownloadEMISection deve rejeitar intervalo fora de gConEmiSize/overflow ou
fonte ausente antes de IO; reserva precisa ser obtida, mapping precisa passar
antes de desproteger. Map falho libera apenas reserva propria e nunca deixa
MPU desativada; caminho valido conserva off/copia/on/unmap/release e dados,
usando memcpy_toio para destino __iomem. API de MPU retorna void e backend
nativo ainda e gate: teste de ordem nao comprova protecao no hardware.
Copias de ram_version para buffer32 ja zerado passam a snprintf com precisao
do campo fonte e tamanho do destino; manter bytes/texto/padding equivalentes,
nao aumentar leitura para32 bytes. Datas de campos fixos usam log limitado.
Aceite proporcional: build ARM/Werror, helpers reais com falhas de reserva/map,
limites e equivalencia de formatacao. Parser completo de firmware/release info
e suas faixas continuam exigindo validacao dirigida antes da ativacao; nao
afirmar loader fisicamente seguro so por compilar. Fonte4.9/capsula BT intocadas.

Resultado: gen4m-fw-loader-linux618-v1.patch aplicado com fuzz=0 sobre baseline
dos23 anteriores; dois arquivos reconstruidos identicos a staging. Oito helpers
ficaram static; CONNAC inteiro normalizado e identico a origem. fw_dl.o e
connac.o compilam ARM6.18.58 com Werror: work/gen4m-lts-fw-loader-build-20261028-b.log.
Buffers de exibicao usam char[32], mantendo tamanho/bytes e evitando casts.

work/gen4m-fw-loader-host-20261028-b.log passou ASan+UBSan com funcao EMI real,
resource/map/MPU/I/O doubles e sequencias reais de versao originais/adaptadas.
Testou base/size invalidos, overflow fisico e size_t ARM32, offset/tamanho fora
da regiao, fonte NULL, vazio, reserva negada, map falho, ultima posicao e regiao
inteira; sucesso conserva byte por byte e ordem reserva/map/off/copy/on/unmap/
release, falhas nao desprotegem ou liberam ownership alheio. As duas copias
de versao produziram os mesmos32 bytes para terminador em cada posicao0..9
ou ausente nos10 bytes. Estruturas reais de include/chips/fw_dl.h LG dual
GPLv2/BSD SHA256original6b0b429ce218babfe54371f97381ed25e55b222c8f317c846f2bcb2650dc41cb.

Nao e download de firmware fisico ou prova de MPU ativa. Reserva EMI concorrente
com outros owners, backend MPU nativo, tamanho minimo de tailers e comprimento
dos records/release manifest continuam a verificar na integracao funcional;
nao afirmar parsing de firmware truncado seguro com base nesses testes.
Nao repetir modulo completo agora: outros erros conhecidos do keep-going-b
permanecem em WEXT/P2P/proc e management. Imagem BT/firmware4.9 preservados.

#### Gen4m: limite de evento RX/assert — decisao previa2026-10-28

Entrega visada: caminho de eventos/recovery Wi-Fi compila e recusa comprimento
truncado antes de ler/capturar assert. Reusar wire WIFI_EVENT LG (header12)
e ring PDMA/AXI completos, C flexible-array Linux6.18 e helpers existentes de
log/arquivo/timer. Mainline mt76 usa seus proprios descritores/firmware e nao
e substituto wire AXI6765; triagem mainline/pmaports/MediaTek/Qualcomm vinculada
continua valida. Sem RE, parser universal ou novo protocolo.

Origem LG dual GPLv2/BSD, snapshot sem commit; hashes nic_rx.c/kal_pdma.c/
nic_cmd_event.c ja registrados acima. A lacuna observada: axiCopyRxData limita
maximo de copia, mas kalDevReadData nao preserva SDLen0 depois do recycle;
dispatcher acessa evento sem comparar com bytes efetivamente recebidos. Manter
u4RxReceivedLen em SW_RFB (metadata host, nao wire), zerar antes de receber,
validar SDLen0 contra rxd_size/ring buffer antes de flush/copy, publicar somente
apos copia. Dispatcher verifica espaco para RXD+WIFI_EVENT antes de ler EID,
header da placa igual offsetof(aucBuffer), comprimento wire entre header e
bytes recebidos; erro devolve RFB uma vez, sem handler/NoAck reset.

Trocar somente aucBuffer[0] de WIFI_EVENT por [] (sizeof/offset12 preservados),
nao outras estruturas. Assert handler valida header antes de subtrair, usa
payload length para escrita e %.*s, so compara prefix5 quando ha5 bytes.
Preservar N9/CR4, arquivo/erro, timer e pre-reset para eventos validos, inclusive
payload vazio. Helpers NIC exclusivamente internos ficam static; prototipo
existente nicEventQueryMemDump sai do #if0, sem alterar corpo.
Aceite: funcao real de dispatch e assert com transporte/arquivo doubles, headers
reais, limites/retorno RFB/erros e ARM/Werror. Escopo AXI6765: outros transportes
terao de fornecer comprimento antes de serem aceitos; sem fallback que confie
no proprio frame. Nao alegar validacao de payload minima de todos os EIDs,
DMA/firmware fisico ou unload. Fonte4.9 e capsula BT intocadas.

Headers LG dual GPLv2/BSD da mesma origem sem commit: include/nic_cmd_event.h
SHA256originalcac99f0fb99035b754b7870beba28043061d76951b7a2679540c3a456f065e4a;
include/nic/nic_rx.h SHA256original
01ba998b55a8d9afb57eb104feae824271193aa650a17dc01ed6f37a03ea5d03.
Resultado: gen4m-rx-event-bounds-v1.patch aplicado com fuzz=0 sobre baseline
dos22 anteriores; cinco arquivos reconstruidos identicos a staging.
nic_cmd_event.o/nic_rx.o/kal_pdma.o/AXI.o compilam ARM6.18.58 com Werror:
work/gen4m-lts-event-bounds-build-20261028-a.log, sem stringop-overread ocultado.

work/gen4m-event-bounds-host-20261028-b.log passou com ASan+UBSan usando
recepcao PDMA, dispatcher e assert handler reais; doubles de registradores,
copia, arquivo e log. Cobriu SDLen0 abaixo RXD/acima ring, fragmento, ausencia
de DMA done, timeout/copy falha/ausente (sem publicar tamanho), header truncado,
wirelen curto/maior que recebido, perfil inconsistente, header12/offset12,
prefixes4/5, N9/CR4, payload exato sem NUL/com NUL/vazio, falha open/write e
preservacao de timer/flags nos eventos validos. Invalidos nao chegam a handler,
nao limpam NoAck/timeout e devolvem RFB uma vez. Compilacao nao equivale a
trafego/reset real; nao comprova validacao minima por outros EIDs ou recuperacao
de DMA remap. Esses caminhos exigem verificacao dirigida quando integrados ao
incremento funcional, sem generalizar uma validacao universal antes do prototipo.

Por mudanca de estruturas compartilhadas, rebuild completo keep-going foi
justificado e terminou com falha: work/gen4m-lts-module-keep-going-20261028-b.log.
As quatro unidades afetadas compilam sem erros tambem nesse rebuild. Outros
bloqueios permanecem em WEXT/access_ok, P2P/cfg80211, proc/tempo/RTC, management
e firmware loader; nenhum .ko completo ou aceite fisico. Nao atribuir sucesso
do modulo aos objetos isolados e nao repetir o rebuild antes de nova mudanca
ou resolucao desses bloqueios concretos.

#### Gen4m: RX/filas/UMAC declaracoes — decisao previa2026-10-28

Entrega visada: compilar recepcao e gerenciamento de filas preservando replay
detection, WMM/EDCA e descritores. Busca em C/headers confirmou helpers radiotap,
UMAC e sete helpers de fila usados somente na propria unidade; usar static,
sem mudar corpos. qmDetermineStaToBeDequeued/qmDequeueStaTxPackets nao tem
consumidores atuais: manter globals/implementacao e declarar assinatura, nao
remover funcionalidade ou adicionar stub. API C/mainline local basta para
esses erros; triagem mainline/pmaports/MediaTek/Qualcomm vinculada nao demonstra
driver substituto AXI6765 e nao requer reescrita da pilha. Sem RE ou novo driver.
LG dual GPLv2/BSD, snapshot sem commit: nic/nic_rx.c SHA256original
af234bab4f7731a168dfee5fa6fe65740685925a899256678db27e9854b8f93f;
nic/que_mgt.c SHA256original
ee8e5b14236c9a470a29819138a64cb7a9a71d762beb0023998ec6501fc24d88;
nic/nic_umac.c SHA256original
30a82f3c9f1bb419046e59dd84c06d0bb6d3d509ef19491fdf9d7c91efb613e4.
Aceite proporcional: comparar arquivos completos normalizando apenas os
prefixos/declaracoes, compilar ARM6.18.58 com Werror. Nenhum teste espelho de
keywords, mudanca de algoritmo/caminho de falha ou operacao fisica.

Outro bloqueio ja coletado: nicEventUpdateLowLatencyInfoStatus em
nic/nic_cmd_event.c usa timeval/do_gettimeofday/rtc_time_to_tm removidos.
Reusar timespec64/ktime_get_real_ts64/rtc_time64_to_tm6.18 GPL-2.0, mantendo
wall clock e microssegundos com tv_nsec/NSEC_PER_USEC. Fonte LG dual GPLv2/BSD,
SHA256original127a818dc621b75d13e26a926d77bab391596bd1b2c6812b5ac82bf8fd4887c7,
snapshot sem commit; arquivo ja tem adaptacao separada de leitura QA. Nao
alterar data-stall, codigos dos eventos, flags ou coletar novo diagnostico.
Verificar campos/eventos com funcao real e clock/RTC doubles; compilar objeto
inteiro mantendo protecoes. Nao e evidencia de latencia/rede no aparelho.
Buffer event guarda string ASCII de11 digitos+NUL para sprintf: usar char[12]
em vez de uint8_t[12], preservando bytes/tamanho e eliminando incompatibilidade
de sinal sem cast ou supressao no teste dirigido.

Resultado: gen4m-rx-queue-event-linux618-v1.patch aplicado com fuzz=0 sobre
baseline dos21 anteriores, quatro arquivos reconstruidos identicos a staging.
RX/queue/UMAC normalizados confirmaram15 prefixos static e duas declaracoes,
resto dos arquivos inteiro identico. Replay detection, WMM/EDCA, limites,
alocacao e erros nao mudaram. nic_rx.o, que_mgt.o e nic_umac.o compilam ARM
6.18.58 com Werror: work/gen4m-lts-rx-queue-build-20261028-a.log.

Evento normalizado contra baseline anterior confirma apenas mapping de clock/
RTC/microssegundos e char[12]. work/gen4m-low-latency-event-host-20261028-b.log
passou com UBSan usando funcao/enum/digit decoder LG reais e doubles de clock,
RTC/report: certificado on/off, deteccao on/off, dois eventos na mesma chamada,
sem report quando nao aplicavel, nsec0/123456789/999999999 e segundos64.
Conserva prefixo legado de8 digitos extraido da string11, nao promete precisao
adicional no report. Nenhum novo diagnostico/telemetria/RF foi ativado.

nic_cmd_event.o ainda falha: work/gen4m-lts-nic-event-build-20261028-a.log
nao aponta mais APIs antigas de tempo, mas revela missing-prototypes e
stringop-overread na leitura de aucBuffer[0] do WIFI_EVENT. Nao mascarar por
cast/supressao: proximo incremento deve verificar contrato de payload flexivel
e limites reais antes de ler prefixes do assert dump. Este objeto/modulo e
recuperacao no aparelho ainda nao estao prontos. Imagem BT/fonte4.9 intactas.

#### Gen4m: callbacks reset/SA Query/list_sort — decisao previa2026-10-28

Entrega visada: preservar recuperacao WMT e timeout de SA Query/PMF, sem casts
de ponteiro de funcao incompatível. Reusar PF_WMT_CB void do gl_rst.h/WMT LG,
PFN_MGMT_TIMEOUT_FUNC(adapter,unsigned long) do CNM existente e list_cmp_func_t
const do Linux6.18.58 GPL-2.0 include/linux/list_sort.h. Nao criar protocolo
alternativo, importar frameworks de outro SoC ou substituir PMF. Triagem
mainline/pmaports/MediaTek/Qualcomm vinculada continua sem substituto do radio
AXI6765; adaptacoes pequenas bastam para esses callbacks, sem RE.
LG snapshot sem commit, dual GPLv2/BSD: os/linux/gl_rst.c SHA256original
dc332fcbf7b9a0ae3758f9a4684dd8b9f4bb0321b8d1b8e46a3be4d2a7e2ac60;
mgmt/rsn.c SHA256original
6ba80a234e0fb5508d0dad13372ea206d85b5b3aa0a8dbfd64f7eb52022d83df;
os/linux/hif/common/kal_pdma.c SHA256original
2e1c58694f6ec78db5148d5117bf4834d102362145f7e79e79679f2ad53eaa2f.

Callback WMT retorna void; remover cast/return NULL e inicializar os dois works
antes de publicar callback (registro pode entregar evento imediatamente).
Recusar body NULL antes de dereference do enum; manter reset start/end/fail.
SA Query conserva funcao LG de tres argumentos e cria bridge privado de dois
que passa STA_RECORD do cookie e terceiro argumento0 (mesmo da chamada direta).
Preservar PMF, retry201TU, alocacao/erro e vida da STA; nao generalizar timers.
Comparator so ganha const nos dois list_head, sem mudar ordenacao/descritores.
Aceite: dispatch real callback/bridge e work order com doubles, corpos legacy
normalizados, ARM/Werror. Unreg/drain WMT, fila pendente e erro de registro
continuam gates separados: esta etapa nao torna unload/reset fisico seguro.

Resultado: gen4m-callback-types-linux618-v1.patch aplicado com fuzz=0; tres
arquivos reconstruidos identicos a staging. Busca de consumidores tambem
permitiu seis helpers RSN ficarem static. Comparacao normalizada de rsn.c
inteiro confirmou apenas linkage, bridge e binding: todos os corpos legacy,
incluindo PMF/retry/protecao de frame, ficaram identicos. kal_pdma.c inteiro
e identico salvo const nos dois argumentos do comparator. gl_rst.o, rsn.o e
kal_pdma.o compilam ARM6.18.58 com Werror, sem cast incompatível:
work/gen4m-lts-callbacks-build-20261028-a.log; gl_rst final recompilado em -b.log.

work/gen4m-callback-types-host-20261028-b.log passou com UBSan: callback e
worker reset reais, tipo/enums RESET_STRUCT de gl_rst.h LG dual GPLv2/BSD
SHA25698cf100d4cbde87bcbd1f7e8fd60630c76776d78a94668c574045f8b2dd9a91e,
WMT/work/SA-engine doubles. Registro entrega END sincrono somente depois de
ambos INIT_WORK; NULL/tamanho errado/tipo alheio/reset invalido nao despacham;
START/END/FAIL mantem flags/veredito do worker. Timer registra callback tipado
e preserva STA cookie e argumento0 da rotina LG, inclusive chamada inicial
e repetida. O teste nao executa firmware, frames PMF, reset fisico nem drain
concorrente de WMT; erro de registro e teardown continuam pendentes.
Nao repetir build completo keep-going sem resolver os outros erros ja coletados.
Proximo bloqueio: RX/filas/UMAC e APIs tempo/RTC/proc/P2P/WEXT restantes.
Imagem candidata BT e fontes4.9 preservadas; nenhum radio novo validado.

#### Gen4m: cfg80211 testmode guard/linkage — decisao previa2026-10-28

Entrega visada: compilar caminho cfg80211 STA sem dependencias testmode ausentes,
preservando implementacao factory/calibration no perfil que habilitar a API real.
Linux6.18.58 net/wireless/Kconfig/include/net/cfg80211.h GPL-2.0 condicionam
API e campo cfg80211_ops a CONFIG_NL80211_TESTMODE. Perfil atual tem opcao
desativada; LG gl_os.h tambem condiciona NL80211_DRIVER_STRING_CMD_PARAMS.
Helpers testmode de string ficaram fora desse guard em gl_cfg80211.c: alinhar
definicoes e declaracoes ao mesmo guard, nao definir CONFIG ficticio nem criar
stub/sucesso. NFC scan-done so e chamado por handlers testmode STA/P2P: condicionar
tambem a definicao a API real. Fonte LG dual GPLv2/BSD e hashes gl_cfg80211.c/h
ja registrados; snapshots locais sem commit confirmado. Mainline fornece
Kconfig/API, triagem pmaports/MediaTek/Qualcomm vinculada nao exige novo driver
ou reescrita do protocolo. Nao importar toda pilha factory Android.

Busca de consumidores confirmou cinco helpers mgmt_tx/role exclusivos dessa
unidade e dois scan-dwell exclusivos do bloco string: limitar a static,
sem mudar corpos. Registrar equivalencia do bloco com TESTMODE habilitado e
ausencia de referencias quando desativado; compilar perfil real off com Werror.
Compilacao/runtime do perfil on continua requisito antes de habilitacao fisica;
nao ampliar claims ou retirar teste/protecao existente. Config da imagem BT,
fonte4.9, rails e firmware permanecem intocados.

Resultado: gen4m-cfg80211-testmode-guards-v1.patch aplicado com fuzz=0 sobre
baseline dos dezenove anteriores, dois arquivos reconstruidos identicos a
staging. gl_cfg80211.o inteiro compila ARM6.18.58 com Werror no perfil real
TESTMODE off: work/gen4m-lts-cfg-testmode-build-20261028-a.log. nm confirmou
connect/change_station/mgmt_tx presentes e quatro helpers de testmode ausentes.
Normalizacao de sete prefixos static e guards novos confirmou gl_cfg80211.c
inteiro identico a baseline: nenhum corpo ou caminho de erro foi alterado;
quando CONFIG_NL80211_TESTMODE esta on, conteudo funcional dos blocos permanece.
Nao criar teste espelho de palavras-chave nem repetir suites STA sem mudanca.

Isto nao e compilacao/runtime de TESTMODE on. Antes de habilitar factory API,
compilar esse perfil real e validar seus comandos/limites; nao fabricar flags
para simular kernel habilitado, nem afirmar interface factory pronta. Preserva
opcao atual off, como em Kconfig6.18, e todos os fontes do perfil on. Proximo
bloqueio funcional de build segue nos demais arquivos do log keep-going: RX,
filas/UMAC, P2P/WEXT, tempo/RTC/proc e callbacks. Nao ha modulo completo nem
ensaio novo no aparelho; provider ICC/DT real e recuperacao WMT seguem gates.

#### Gen4m: cfg80211 estado STA e TDLS link params — decisao previa2026-10-28

Entrega visada: preservar rejeicao EALREADY na reconexao durante disconnect e
parametros legacy de peer TDLS para associacao/trafego. Reusar ABI6.18.58 local
include/net/cfg80211.h/net/wireless/nl80211.c GPL-2.0: current_bss do STA
naoMLD passou para links[0].client.current_bss; rates/HT/VHT estao em
station_parameters.link_sta_params, cujo link_id naoMLD e -1. Nao acessar
estrutura interna de BSS nem inventar bool connected. Fonte LG gl_cfg80211.c
dual GPLv2/BSD, SHA256original ecba08fef1418d49062c417a7f839c439c7fd5dcdccbe2ee21ccfd32edcc06a7,
snapshot sem commit; revisao6.18 extraida sem HEAD confirmado. Triagem de
mainline/pmaports/MediaTek/Qualcomm ja vinculada nao prova substituto do
protocolo AXI6765; ABI existente basta, sem driver paralelo ou RE.

Adaptar apenas campos movidos, conservar clamps de rates/extcap, copia HT,
UAPSD legacy, capability/sta_flags/BSS e propagacao do erro do peer update.
VHT era bloco vazio LG e continua sem funcionalidade adicionada. Recusar
MLD/link especifico, HE/EHT/UHR/S1G/6GHz, per-peer TX power/opmode e EML/EPP
antes de backend, pois nao representados no comando LG. Falta de params/rates
mantem retorno legacy sem update. Aceite: testar comando real TDLS com doubles,
limites/erros/sem efeitos sob rejeicao e compilar caminho cfg80211 contra6.18;
outros erros do arquivo nao devem ser ocultados. Nao alterar radio/potencia,
fonte4.9, imagem BT ou afirmar associacao no aparelho.

Resultado offline: gen4m-cfg80211-station-link-v1.patch aplicado com fuzz=0
sobre baseline dos dezoito anteriores, arquivo reconstruido identico a staging.
Ambos ramos de CFG_SUPPORT_TDLS portados; assinatura MAC const corrigida tambem
no ramo desativado. Teste work/gen4m-station-link-host-20261028-a.log compila
funcao LG original e cada ramo adaptado com UBSan e mesmas verificacoes de
comando, usando structs CMD_PEER_UPDATE reais de include/mgmt/cnm_mem.h LG
dual GPLv2/BSD SHA256105614cb5cf51222a0fe64098428ef1119df4e2a3030e2e50a8a6a12dad7f579.
Dados de rates50/extcap5 limitados, HT/MCS/capability/UAPSD/BSS/MAC, zeramento
dos campos restantes, parametros ausentes e invalidos, erro peer update e
guard de reconexao foram preservados. Novos recursos sem representacao nao
atingem kalIoctl. Doubles nao executam firmware nem provam associacao.

Comportamento preexistente preservado: erro da segunda chamada de controle de
channel-switch TDLS continua sem propagacao (a primeira chamada peer update
propaga EINVAL). Nao declarar equivalencia sob falha mais ampla ou novo suporte
VHT/MLD. Native build work/gen4m-lts-cfg-station-build-20261028-a.log nao aponta
mais current_bss/rates/HT/VHT movidos, mas gl_cfg80211.o ainda falha em
testmode/configuracao e missing-prototypes. Ainda nao e objeto/modulo pronto.
Proximo incremento deve resolver interfaces reais restantes; nenhum stub,
define ficticio, mudanca de config BT ou operacao fisica foi realizado.

#### Gen4m: NIC/TX linkage — decisao previa2026-10-28

Entrega visada: compilar nucleo NIC/TX sem alterar alocacao, descritores,
potencia RF ou caminhos de erro. Busca em todos os C/headers LG confirmou
nicHifInit, tres getters chip (dois ramos de preprocessor) e cinco helpers TX
usados somente em seu arquivo: reusar linkage static C. Tres globals sem
consumidor atual (nicProcessFwOwnBackInterrupt, nicSetAutoTxPowerControl,
nicTxCopyDesc) mantem linkage e corpos com declaracao da assinatura existente.
Nao criar stubs, remover funcoes nem desabilitar Werror. API C/mainline local
e suficiente; triagem mainline/pmaports/MediaTek/Qualcomm ja vinculada nao
oferece substituto comprovado do AXI6765 para essa lacuna de declaracoes.
Sem engenharia reversa ou driver paralelo. Fontes LG sem commit identificado,
dual GPLv2/BSD: nic/nic.c SHA256original
7c3fa3fd374ba47be0abe784c399070c9c6998c6e80ad4fd59f5ce2dd730623e;
nic/nic_tx.c SHA256original
0469ed77f88b8d97bf576e09aa284c2ec7c2a892e99ee8b41a01d3e23871e29b.
Aceite proporcional: normalizar apenas declaracoes/linkage e demonstrar corpos
inteiros identicos, compilar ARM/Werror, continuar build para proximo erro real.
Nao criar testes que apenas contem keywords. Fonte4.9 e imagem BT preservados.

Resultado: gen4m-nic-tx-linkage-v1.patch aplicado com fuzz=0 sobre fontes
originais adicionadas a baseline isolada; nove nomes internos (getters nos
dois ramos) ficam static e tres globals mantem assinatura/linkage. Comparacao
dos dois arquivos completos apos normalizar somente esses prefixos e tres
declaracoes confirmou identidade byte a byte dos corpos. nic.o e nic_tx.o
compilam ARM6.18.58 com Werror: work/gen4m-lts-nic-build-20261028-a.log.
Nenhum ajuste de algoritmo, potencia, filas, limites ou recuperacao.

Uma compilacao completa keep-going, mantendo Werror, terminou com falha e
localizou dependencias restantes sem repetir build inteiro a cada primeiro
erro: work/gen4m-lts-module-keep-going-20261028-a.log. Restam declaracoes em
RX/filas/UMAC/mgmt, APIs nativas de tempo/RTC/proc, access_ok, cfg80211 STA/P2P,
NAPI/MAC, assinaturas reset/timer/list_sort e limites stack/VLA em scan/regdomain.
WEXT privado/testmode tambem exige tratar a configuracao e a API reais; nao
fabricar defines/structs ou ocultar essas interfaces para obter build verde.
CONFIG_CFG80211_WEXT nao esta ativo nesse kernel. Nao alterar silenciosamente
config/imagem candidata BT; dependencias de perfil devem ser integradas em
candidato proprio antes de ensaio autorizado. Nao ha .ko completo ou radio
validado; provider ICC/DT real e gates de WMT/threads continuam pendentes.

#### Gen4m: common/wlan_lib e wlan_oid — decisao previa2026-10-28

Entrega visada: progredir ate modulo Wi-Fi6.18 completo, preservando parser de
configuracao, inicializacao e rollback do radio. Busca em todos os C/headers
LG confirmou18 helpers com consumidores exclusivamente em wlan_lib.c:
limitar linkage a static sem alterar corpos. Reusar linux/stddef.h6.18 para
offsetof/NULL/tipos de kernel em wlan_oid.c, nao adicionar headers libc ao
Kbuild. Linux fornece estas APIs/C; alternativas mainline/pmaports/MediaTek/
Qualcomm ja triadas nao exigem trocar a pilha LG para esses erros locais.
Nao importar parser paralelo ou novo framework. Fontes LG snapshot sem commit,
dual GPLv2/BSD: common/wlan_lib.c SHA256original
90d42e61a2528e7faa14ae918bf2c3f7ccea49951b5f70665a728ed4a48471c9;
common/wlan_oid.c SHA256original
ba7f85a9b84b2ab90888630e48ce1acceac5c11f85cb697eafd06620bcfdb2d9.

Corrigir tres limpezas do array local de ponteiros apcArgv para sizeof(apcArgv),
nao simplesmente cast/supressao do warning: WLAN_CFG_ARGV_MAX era contagem,
nao bytes. Array arcArgv_size tem elementos int8 e tamanho antigo correto;
nao mudar gramatica, FW commands, limites ou fallthrough de rollback efetivo.
Anotar fallthrough existente em wlanAdapterStart. Aceite proporcional:
comparar diff/corpos normalizados e compilar objetos com Werror; nao criar
teste que apenas reimplemente sizeof/memset. Original4.9 e imagem BT intocados.

Build apos essa adaptacao compilou wlan_lib/oid e revelou mais dois erros
common: timestamp de pacote de teste VoE usa timeval/do_gettimeofday removido;
P2P possui global sem prototipo e sem consumidor atual. Reusar timespec64 e
ktime_get_real_ts64 Linux6.18 (mesmo wall clock e microssegundos no formato
wire32 via tv_nsec/NSEC_PER_USEC), como na adaptacao PDMA ja auditada, sem
desligar teste VoE nem modificar fases/offsets/guardas. P2P mantem linkage e
corpo, recebe declaracao de sua assinatura existente. LG common/debug.c dual
GPLv2/BSD SHA256original
e1553b668a152610ac38417f8b5a6b1e111c49c8eb28e8ca67cf19ad561c6876;
common/wlan_p2p.c dual GPLv2/BSD SHA256original
986addfd97f67666b02f28bd26c88ab614062775bee169e7b63d503efee0e397.
Validar bytes/offsets e rejeicoes do timestamp com funcao real offline;
isso nao e aceite de trafego no aparelho. Sem necessidade de RE ou novo driver.

Resultado: gen4m-common-linux618-v1.patch aplicado com fuzz=0; quatro arquivos
reconstruidos identicos a staging. wlan_lib.c normalizado confirmou exatamente
18 mudancas de linkage, tres sizeof(apcArgv) e anotacao de fallthrough, resto
dos corpos e ordem identico a origem. wlan_oid.c manteve corpo inteiro salvo
include de kernel e anotacoes equivalentes dos dois "no break here" D1/D2.
Nao inserir break que alteraria o caminho de energia D1/D2 para D3.
Objetos ARM6.18.58 com Werror passaram: work/gen4m-lts-common-build-20261028-b.log
(wlan_lib/oid) e -c.log (debug/P2P). No timestamp, clock real64 substitui
gettimeofday e nanossegundos sao truncados para microssegundos; protocolo
mantem32bits de segundos, nao altera offsets ou flag de teste VoE existente.
work/gen4m-debug-timestamp-host-20261028-a.log: funcao real com doubles de
clock/skb e UBSan preservou bytes de todos os outros campos, tres fases e
guardas para NULL/flag desligada/curto/naoIPv4/naoUDP/marker errado. Nenhum RF.

Novo build completo work/gen4m-lts-module-build-20261028-c.log passou common
e encontrou missing-prototypes em nic/nic.c e nic/nic_tx.c. Proximo incremento
deve verificar consumidores/linkage nesses arquivos, sem suprimir Werror;
modulo completo e provider/DT/ensaio fisico continuam pendentes. Fontes4.9 e
imagem candidata BT nao foram modificadas.

#### Gen4m: consumidor de bandwidth interconnect — decisao previa2026-10-28

Entrega visada: manter voto de bandwidth de memoria do Wi-Fi sob trafego,
sem ignorar falhas nem alterar limites termicos/voltagens diretamente. Fonte
LG4.9 kernel/power/qos.c agrega PM_QOS_GPU_MEMORY_BANDWIDTH por SUM;
drivers/devfreq/helio-dvfsrc.c recebe notifier e escreve DVFSRC_SW_BW_2 com
data/100. Nao e contador inocuo. Native6.18.58 drivers/interconnect/core.c
e include/linux/interconnect.h GPL-2.0 oferecem consumidor e ownership;
mediatek/icc-emi.c agrega media por SUM, mas mtk-dvfsrc.c so anuncia
mt6893/mt8183/mt8195, nao MT6765. Config atual INTERCONNECT=y,
INTERCONNECT_MTK e MTK_DVFSRC desativados. Nao inventar compatibilidade de
outro SoC, usar provider Qualcomm ou importar toda a pilha SSPM/SPM LG.
Triagem mainline/pmaports/MediaTek/Qualcomm anterior continua sem backend
AXI/DVFSRC6765 comprovado. A lacuna especifica de provider permanece aberta.

Extensao pequena no plat_priv.c LG dual GPLv2/BSD, hash original acima:
consumidor of_icc_get(dev,"wifi-memory") obrigatorio antes de DMA/MMIO/WMT,
sem aceitar NULL opcional/stub. Um owner device e mutex; erro/defer propagado,
icc_set_bw inicial zero precisa passar antes de publicar owner. Monitor usa
bytes/periodo em kB/s SI, teto U32_MAX, com arredondamento para cima; nao
transportar o erro antigo de MB por amostra como se fosse taxa. Media somavel,
peak0 (nao inventar pico); voto e hint de performance, nao muda OPP/thermalmax.
Stop zera voto e bloqueia amostra atrasada pelo STOP_BIT existente; remove
solta a referencia e despublica owner. Testar limites/falhas/ownership e compilar
objetos alterados. Isto porta apenas o consumidor: sem DT/provider MT6765 real
o probe deve falhar, nao declarar radio/bandwidth funcionando. Imagem BT e4.9
intactos; nenhum acesso fisico autorizado por esta decisao.

Resultado: gen4m-bandwidth-interconnect-v1.patch porta consumidor, nao provider.
gl_init.o, gl_kal.o, plat_priv.o e AXI.o compilam ARM6.18.58 com Werror,
work/gen4m-lts-icc-build-20261028-a.log. Teste host com UBSan usa helpers reais
e probe AXI, doubles de ICC/DMA/MMIO: ausencia/NULL/defer, erro de voto inicial,
rollback apos DMA/CSR/pool, unico owner, device incorreto, periodo zero,
arredondamento kB/s e saturacao U64/U32, erro de update, STOP e destroy repetido;
work/gen4m-bandwidth-host-20261028-b.log. Stop define STOP_BIT antes de zerar
voto, impedindo amostra positiva atrasada; log explicito se update/zero falhar.
icc_put nativo tenta zerar antes de remover requests/referencias e reporta erro
do provider; isso nao prova zero aplicado no hardware se o provider falhar.
Timer Linux so acorda thread WLAN; cnmTimerDoTimeOutCheck chama monitor nessa
thread, nao hardirq, preservando contexto sleepable para ICC.

Origem consultada, nao copiada: kernel4.9 kernel/power/qos.c GPL-2.0 SHA256
dab0b7082a740a6f80c8fe9a327f118dfed7be7a34b46b7556d0d3184af937ce;
drivers/devfreq/helio-dvfsrc.c GPL-2.0 SHA256
07ffebb3da148d7e1f870f0e6a658b0d4c464991d0c2e3c17ddba59169062abc.
Native6.18.58 drivers/interconnect/core.c GPL-2.0 SHA256
26a8177b98d688cd521c684175a6040a7f83cc9adc04753fe2eebaa0192eb729;
arvores locais sem commit confirmado. Backend conserva licenca LG dual acima.
Baseline privada dos quinze patches preservada em
artifacts/staging-gen4m-icc-20261028-v1, seis hashes fixados no teste.

Build completo tentado apos objetos criticos passarem, sem suprimir Werror:
work/gen4m-lts-module-build-20261028-a.log. Ainda falha em common/wlan_lib.c
(linkage/prototipos, fallthrough e limpeza parcial de array de ponteiros) e
common/wlan_oid.c (stddef.h userspace). Nao gerar/afirmar .ko funcional.
DT Wi-Fi/panel/interconnect e provider nativo MT6765 comprovado permanecem
gates: ICC generico disponivel nao demonstra compatibilidade do controlador.

#### Gen4m: painel DRM — decisao previa2026-10-28

Entrega visada: eventos reais da tela preservam wlan_fb_power_down e
enable/disable do monitor de desempenho, incluindo force-enable existente.
Reusar drm_panel_add/remove_follower Linux6.18.58 local, drivers/gpu/drm/
drm_panel.c MIT, SHA256384d6629b2bca1c1e7667c51f3f153820d627d69029df61f794cdbf73d4381d9,
arvore extraida sem HEAD Git, e integracao WMT ja auditada abaixo. Nao transportar
notifier Android/mainline antigo nem importar driver pmaports/Qualcomm: a
triagem AXI6765 existente nao demonstra substituto compativel, e a lacuna e
a API de painel removida, nao o protocolo do radio. LG gl_kal.c/gl_init.c,
gl_kal.h e AXI axi.c dual GPLv2/BSD, hashes de origem registrados nesta matriz.
Esforco limitado a callback/ownership e pontos existentes de probe/monitor.

Registrar no device AXI antes de DMA/MMIO/WMT; ausencia de panel retorna
ENODEV e erro configurado (incluindo EPROBE_DEFER) propaga sem tocar hardware.
Add DRM pode chamar enabled sincronicamente: callback guarda estado mas nao
acessa GLUE antes do sucesso do monitor. Mutex serializa callback, force-enable
e retirada do ponteiro antes de kalPerMonDestroy; remove DRM fora desse mutex
evita inversao com follower_lock e drena callback. Falhas de probe liberam
follower; remove idempotente antes de recursos AXI. DT Wi-Fi/panel ainda e gate
antes de ensaio. Nao alterar WMT candidato, firmware, rails ou imagem BT.
Aceite offline dirigido: callbacks ON/OFF/force, add sincrono, erros/defer,
retirada antes de destruir monitor, compilacao ARM com API real. Nao equivale
a tela/Wi-Fi/suspend funcionando juntos no aparelho.

Resultado offline: gen4m-drm-panel-follower-v1.patch aplicado com fuzz=0
sobre os quatorze anteriores; copia de baseline privada preservada em
artifacts/staging-gen4m-panel-20261028-v1 com quatro hashes fixados no teste.
Monitor so recebe ponteiro depois de wlanOnWhenProbeSuccess, em boot/reset;
kalPerMonDestroy retira esse ponteiro antes de disable e destroy CPU boost.
Registro/remoção deixam de ocorrer em init/exit global e pertencem ao AXI.
Mutex proprio substitui a tentativa de halt lock para ownership do ponteiro;
estado de tela ainda e lembrado quando halted, sem acessar o monitor nessa fase.
Start aplica estado inicial somente ao monitor ja inicializado.

work/gen4m-lts-panel-build-20261028-a.log: AXI.o ARM/Werror compila; gl_kal.o
nao aponta mais FB_EVENT_BLANK, mas ainda falha em pm_qos_update_request.
work/gen4m-panel-host-20261028-b.log: callbacks reais LG e add/remove reais
DRM com doubles de hardware/monitor e pthread/UBSan passaram ON/OFF,
force-enable, add sincrono antes de monitor, ENODEV/defer/erro configurado,
rollback DMA/CSR/pool, detach repetido e callback concorrente com destroy.
Nao substitui validacao fisica, nem declara seguro unload/WMT concorrente.
Consumer AXI sintetico atual nao tem panel: agora e rejeitado antes do hardware;
ligar o consumer DT real ao painel permanece trabalho obrigatorio, nao fallback.
gl_init e gl_kal continuam bloqueados pelo bandwidth QoS vendor; modulo
completo e funcionamento dos radios no aparelho ainda nao entregues.

#### Gen4m: declaracoes gl_init — 2026-10-28

Proximo bloqueio dirigido em gl_init: module.h LG4.9 define
MODULE_SUPPORTED_DEVICE(name) vazio; remover a chamada obsoleta sem criar
alias/probe ou metadado que nao existia. Reusar linkage C privado
somente para os oito helpers com consumidores exclusivamente nesse arquivo,
e prototipos para tres globals mantidos sem consumidor atual. gl_init.c e
gl_os.h LG dual GPLv2/BSD, revisao e hashes acima; nao substituir driver nem
importar codigo pmaports/Qualcomm para declaracoes C. O hook existente
update_driver_loaded_status pertence ao adaptor LG GPL-2.0 (hash acima),
independente do log dedicado: expor a declaracao fora desse guard, nao criar
stub nem omitir notificacao. Fallthrough deve ser anotado nos caminhos de
rollback existentes sem alterar ordem ou protecoes. Aceite: diff limitado a
esses pontos e recompilacao dirigida mantendo Werror; nao prova runtime.

Resultado: gen4m-init-declarations-v1.patch aplicado com fuzz=0 sobre os treze
patches anteriores; os dois arquivos reconstruidos sao identicos a staging.
Normalizacao das oito mudancas de linkage, tres prototipos, chamada vazia e
anotacoes de fallthrough confirmou gl_init.c inteiro identico: corpos e ordem
preservados. Nao criar teste espelho de keywords. Build ARM/Werror dirigido
work/gen4m-lts-init-declarations-build-20261028-a.log nao aponta mais os erros
tratados; gl_init.o ainda falha exclusivamente em pm_qos_add/remove_request e
PM_QOS_GPU_MEMORY_BANDWIDTH. Nao confundir essa reducao de erros com objeto
ou modulo pronto. Proximo bloqueio concreto: caminho real de bandwidth QoS
compativel com MT6765/6.18 e notificador de painel em gl_kal; nao omitir suas
funcoes para obter build aprovado.

#### Gen4m: wakeup_source nativo — 2026-10-28

Reusar wakeup_source_register/unregister, __pm_stay_awake/relax/wakeup_event
Linux6.18.58 GPL-2.0, como no OSAL WMT ja portado; nao definir CONFIG_ANDROID
nem mascarar macros vazias. Mainline e o framework compativel; triagem
pmaports/MediaTek/Qualcomm nao fornece substituto da pilha AXI6765. Fontes LG
gl_kal.h/gl_os.h/gl_kal.c/gl_init.c dual GPLv2/BSD, hashes registrados acima;
mgmt/cnm_timer.c dual GPLv2/BSD SHA256original
0a78f9b46de9746a3d15a79607e31d2b0e64faeeb11858c35c64f0872811a03b,
snapshot sem commit. Nao importar OSAL inteiro ou novo gerenciador de energia.

Seis fontes pertencem a vida do GLUE/ADAPTER: interrupt, timeout, main/HIF/RX
thread e CNM timer. Registrar antes de HIF/threads, propagar ENOMEM com rollback
das criadas, sem alocacao falhavel dentro de thread. Threads usam slots GLUE,
relaxam antes da completion; waiter nao pode ignorar interrupcao e liberar
enquanto thread ainda usa fonte. CNM mantem uso/tempo, mas registro e liberacao
passam ao owner GLUE: relax no init/destroy de servico, unregister somente apos
timers/HIF e threads encerrados, antes de destruir ADAPTER. Falha de netcreate
deve retornar NULL e limpar ponteiro do adapter destruido. Acquire/release e
conversao de timeout jiffies->ms preservados; active deve ler sob lock do WS.
PM_SLEEP e CFG_ENABLE_WAKE_LOCK devem estar ativos nesse candidato, nunca usar
fallback no-op. Aceite offline inclui registro falho, ownership/ordem, APIs
reais compiladas e sem novas chamadas RF/charge. Suspend/resume real e WMT
concorrente continuam sem aceite fisico; nao declarar unload seguro por isso.

Resultado offline: gen4m-native-wakeup-sources-v1.patch aplicado com fuzz=0
sobre a baseline dos doze patches anteriores. CNM e AXI compilam ARM6.18.58
com Werror: work/gen4m-lts-wakeup-cnm-axi-build-20261028-b.log. O objeto
wakeup_abi_check.o tambem compila contra headers reais; nm confirma referencias
a __pm_stay_awake/relax e wakeup_source_register/unregister. Host com UBSan
exercitou falha de registro nas posicoes1/3/6, rollback, rejeicao de segundo
owner, acquire/release/timeout e destroy repetido; log
work/gen4m-wakeup-host-20261028-b.log. Sao doubles de PM, nao ensaio de suspend.
Criacao precede HIF/threads; completion sucede ultimo uso de fonte na thread;
erro NET_REGISTER_FAIL agora espera as threads validas antes da liberacao.
Nao cobre falha de kthread_run antes de sched_setscheduler, callbacks WMT
concorrentes ou recuperacao fisica: continuam gates antes de probe no aparelho.
gl_kal/gl_init ainda recusam outras APIs antigas; nenhum modulo completo pronto.

#### Gen4m: perfil sem MET e linkage KAL — decisao previa2026-10-28

Reusar opcao LG existente MTK_MET_PROFILING_SUPPORT=no por linha de comando
do build6.18; MTK_MET_TAG_SUPPORT ja e no. MET e profiler Android opcional,
nao log de falha, teste ou protecao. Seu lookup kallsyms nao e exportado no
6.18 e emissao event_trace_printk deste snapshot ja esta em #if0. Nao portar
novo profiler antes de Wi-Fi funcional; preservar todo fonte e default4.9.
Call de cleanup MET no switch de falha precisa do mesmo guard da inicializacao
para a opcao no nao criar simbolo ausente. Nenhum stub novo para enganar link.

Busca de todos os C/headers LG confirmou helpers KAL referenciados somente em
gl_kal.c: limitar linkage a static, sem mudar corpos, assinaturas ou algoritmo.
Funcao global sem consumidor atual kalQueryRegistryMacAddr e hooks weak de
wakeup-debug conservam linkage e recebem prototipo, sem inventar implementacao.
gl_kal/gl_kal.h/gl_init LG dual GPLv2/BSD e hashes ja registrados. Mainline
fornece semantica C/Kbuild; alternativas pmaports/MediaTek/Qualcomm nao exigem
MET para transporte AXI. Extensao minima no caminho existente, nao framework.

Novo bloqueio revelado: CONFIG_ANDROID ausente torna KAL_WAKE_LOCK vazio,
apesar de PM_SLEEP=y. Nao apenas colocar braces/suprimir empty-body para
aprovar: precisa de wakeup_source nativo com lifetime/falhas antes de ensaio.
Esse item nao desliga wakelocks, QoS, testes, recovery ou protecao termica.

Resultado: gen4m-kal-linkage-met-guard-v1.patch tornou17 helpers internos
static e preservou globals diagnosticos sem consumidor ativo (incluindo
kalGetLocalTime) e hooks weak com prototipos. Comparacao normalizando somente
esses17 prefixos confirmou gl_kal.c inteiro identico a baseline; nenhum corpo
mudou. Cleanup MET recebeu guard equivalente ao init e fallthrough explicito.
Sem novos testes espelho para troca exclusiva de linkage; verificacao dirigida
mantem Werror. V=1 confirmou -DCFG_MET_PACKET_TRACE_SUPPORT=0 na opcao LG no:
work/gen4m-lts-no-met-build-20261028-a.log. Log-c nao aponta mais MET/proc,
kallsyms ou missing-prototypes tratados: work/gen4m-lts-no-met-build-20261028-c.log.

gl_kal.o ainda falha por wakelocks vazios (nao mascarados), QoS bandwidth e
FB_EVENT_BLANK antigo. Nao e objeto/modulo pronto. Nao definir CONFIG_ANDROID
artificialmente para esconder a lacuna; proximo incremento deve reutilizar
wakeup_source nativo ja disponivel, propagando falha/lifetime. Fonte4.9/default
MET continuam intactos. Patch reconstruido sobre baseline dos onze anteriores
com fuzz=0 produziu os tres arquivos identicos a staging. Opcao de build no
documentada no handoff, nao e autorizacao de operacao no aparelho.

#### Gen4m: arquivos/boottime6.18 — decisao previa2026-10-28

Usar filp_open/kernel_read/kernel_write e ktime_get_boottime_ts64 do proprio
Linux6.18.58 GPL-2.0. Buffer dos helpers e de kernel; remover set_fs/get_fs
obsoletos, nao usar copy_to_user com endereco de kernel. Mainline fornece API;
triagem pmaports/MediaTek/Qualcomm nao substitui o backend AXI6765. Extensao
pequena ao glue LG dual GPLv2/BSD, sem nova ferramenta, daemon ou protocolo.
gl_kal.c/header tem hashes acima. Dependencia direta nic/nic_cmd_event.c
SHA256original127a818dc621b75d13e26a926d77bab391596bd1b2c6812b5ac82bf8fd4887c7,
dual GPLv2/BSD, snapshot sem commit; nao expandir recurso QA/IQ.

Falha concreta: read negativo era convertido a uint32 e kalReadToFile reportava
sucesso/tamanho enorme ao parser wifi.cfg. Preservar byte count/errno em ssize_t,
validar offset antes de converter a loff_t, devolver erro de leitura com tamanho
zero; write parcial/erro nao pode virar sucesso. Preservar flags, modo, posicao
passada por valor, append e fechamento. Unico caller direto QA deve parar em
leitura incompleta/erro em vez de analisar buffer nao inicializado. Prototipos
dos helpers sempre compilados nao devem depender de CFG_SUPPORT_QA_TOOL.
Boottime segue incluindo suspend e retorna microssegundos truncados como antes,
com segundos64. Aceite offline: API nativa, offsets/erros/short I/O/close e tempo,
sem gravacao no aparelho ou novas operacoes RF/eletricas.

Resultado: gen4m-kernel-file-time-api-v1.patch remove set_fs/get_fs, preserva
offset por valor e informa errno/short write aos callers; leitura falha deixa
tamanho zero, sem enviar numero unsigned gigante ao parser. IQ consome oito
bytes (IQ_FILE_IQ_STR_LEN=8) e agora recusa leitura menor/erro antes do parse;
nao alterou outras funcoes desse recurso. Sete helpers reais compilaram ARM6.18
com Werror em objeto offline fora do modulo:
work/gen4m-file-time-abi-20261028-a.log. Teste C/UBSan passou com FS/clock
dobrados: erro de open, errno de I/O, leitura curta/EOF, escrita curta/erro,
append/flags/modo, fechamento, offset invalido e boottime64 em microssegundos:
work/gen4m-file-time-host-20261028-a.log. Nao escreveu arquivos no aparelho.
Open ainda usa sentinela NULL/-1 legado; nao prometer errno de open completo.

Glue/teste MIT; fonte LG/licencas preservadas. Serie reaplicada com fuzz=0
sobre baseline dos dez patches anteriores produziu os tres fontes identicos
a staging. Build gl_kal.o ainda falha, mas nao aponta as APIs de arquivo ou
boottime tratadas: work/gen4m-lts-files-build-20261028-a.log. Proximos bloqueios
sao declaracoes/linkage, proc/MET legado, QoS bandwidth e notificador FB;
nao desativar verificadores ou protecoes para obter um modulo aprovado.

#### Gen4m: ownership CSR/MMIO — decisao previa2026-10-28

Reusar of_address_to_resource/of_iomap, request/release_mem_region e referencias
of_node_get/put Linux6.18.58 GPL-2.0. devm_platform_ioremap_resource e alternativa
upstream, mas a plataforma CONNAC sintetica LG ainda nao fornece resources;
manter caminho existente com checagens pequenas, nao criar outro transporte.
Preferir of_node do proprio device quando existir, com fallback LG atual.
Recusar no desabilitado, recurso nao-MMIO, intervalo vazio/overflow/truncado,
conflito de reserva e mapeamento falho. Equilibrar referencias em cada saida;
publicar CSR/base/tamanho/owner somente no sucesso. Remove de outro device ou
repetido nao deve liberar mapa alheio. Nao alterar reg/IRQ/energia da placa.

Mainline fornece APIs; triagem pmaports/MediaTek/Qualcomm nao demonstra backend
AXI6765 substituto. AXI.c LG dual GPLv2/BSD, SHA256original ja registrado, sem
commit local. Aceite offline e ownership sob falhas reais de API dobradas,
compilacao ARM e preservacao do mapa ativo em tentativa duplicada. Isso nao
aprova acesso a MMIO no aparelho nem corrige concorrencia dos callbacks WMT.

Resultado: gen4m-axi-csr-ownership-v1.patch publica metadata somente apos
request/map bem-sucedidos e libera somente o mapa do pdev proprietario. AXI.o
inteiro passou ARM6.18/Werror: work/gen4m-lts-axi-csr-build-20261028-a.log.
Teste C/UBSan dos corpos reais passou com OF/resource/MMIO dobrados: ausencia
ou status disabled, recurso invalido, conflito, map falho, node proprio versus
busca legada, referencias equilibradas, duplicacao e unmap de owner diferente
ou repetido. Log work/gen4m-axi-csr-host-20261028-b.log. Glue/teste MIT reutiliza
harness existente; nao testou registradores reais. Reaplicacao com fuzz=0
sobre a baseline dos nove patches anteriores produziu AXI.c identico a staging.

Ainda nao e modulo/transportador funcional: referencia DT da placa e mapa real
nao ensaiados, e WMT reg/unreg legado publica/limpa ponteiros sem drenar chamadas
concorrentes. Nao afirmar unload seguro nem modificar a capsula BT validada
offline so para encobrir essa lacuna. Prosseguir com dependencias restantes
do build completo e fechar gates do primeiro probe antes de qualquer ensaio.

#### Gen4m: limites/rollback do pool AXI — decisao previa2026-10-28

Manter allocator linear e arrays LG prealloc, transportes/atributos cacheados
e Device existentes; nao trocar pelo ramo runtime apenas por compilar. Mainline
gen_pool e DMA pool sao alternativas, mas substitui-los aqui mudaria o layout
fisico ja usado pelo firmware. Reusar check_add_overflow, request/release_mem_region
e ioremap/iounmap Linux6.18.58 (GPL-2.0), com pequena extensao ao allocator.
Triagem pmaports/MediaTek/Qualcomm nao fornece equivalencia desse layout AXI6765.
AXI.c LG dual GPLv2/BSD, hash de origem ja registrado, snapshot sem commit.

Validar base/alinhamento/tamanho/overflow antes de reservar; manter offset32
sem aceitar pool maior que ele representa. Cada bloco verifica alinhamento8,
limite restante e overflow fisico; falha nao publica pa/va nem avanca offset.
Reserva deve falhar em conflito, sem liberar regiao de outro owner. Em erro,
desmapear somente blocos proprios e liberar a reserva propria pelo snapshot
base/tamanho, incluindo TxCmdBuf que o free legado omitia. Free repetido deve
ser inofensivo. Probe deve desfazer CSR e devolver erro sem registrar WMT se
prealloc falhar. Nao desabilitar MPU: chamada/protecao existente permanece;
rollback aqui cobre recursos CPU, nao afirma desfazer configuracao MPU.
Esse glue nao aprova cache/DMA real, WMT concorrente ou remove sob carga.

Resultado: gen4m-axi-pool-bounds-v1.patch preserva layout/loops LG, limita
alinhamento/offset/pool/intervalo fisico e mascara DMA, nao avanca bloco em
falha e libera todos os mapeamentos proprios (incluindo TxCmdBuf). Pool vazio,
ocupado ou insuficiente impede registro WMT; probe libera seu CSR nesse erro.
AXI.o inteiro continua compilando ARM6.18 com Werror, log
work/gen4m-lts-axi-pool-build-20261028-b.log. Patch reconstruido sobre a baseline
dos oito anteriores com fuzz=0 produziu fonte identica a staging.

Teste C/UBSan dos corpos reais de alloc/free/probe passou, com tamanhos de
arrays reduzidos e mapeadores/reservas/MPU/WMT dobrados: capacidade exata e
um byte insuficiente, alinhamento/overflow, reserva alheia preservada, free
repetido e falhas no inicio/meio/fim sem mapeamentos vivos nem callbacks WMT.
Log work/gen4m-axi-pool-host-20261028-b.log. Nao foi criada nova implementacao
de allocator no teste. Nao comprova MPU, cache, IOMMU, capacidade real da placa
ou remove concorrente; MPU permanece conforme contrato legado e pode exigir
reset para recuperacao. Glue/teste MIT. Proximo bloqueio de transporte e
reserva/ownership CSR e registro/desregistro de callbacks WMT, sem ampliar
para framework universal. Modulo inteiro e Wi-Fi fisico ainda nao comprovados.

#### Gen4m: setup DMA AXI6.18 — decisao previa2026-10-28

Entrega visada e probe Wi-Fi que recusa DMA invalido antes de MMIO/alocacao,
sem liberar firmware/IRQ com setup falho. Reusar dma_set_mask_and_coherent
do Linux6.18.58 (include/linux/dma-mapping.h e kernel/dma/mapping.c GPL-2.0),
mantendo u4DmaMask=36 do CONNAC. Nao reduzir a32 bits para compilar nem
sobrescrever ops/IOMMU escolhidos pelo core. Platform_device_alloc6.18 ja
inicializa o ponteiro dma_mask; a API valida suporte e ajusta os dois limites.
No ARM desta config, asm/dma-mapping.h gerado usa asm-generic (ops NULL por
padrao) e DMA core usa caminho direto nao-coerente com syncs arch quando nao
ha IOMMU. Portanto nao transportar o adaptador vendor arch_setup_dma_ops de
cinco argumentos, nem criar stub. Se houver ops/IOMMU no dispositivo, conserva-los.

Validar largura1..64 antes de DMA_BIT_MASK; propagar errno de setup no probe.
Recusar falha de CSR mapping antes de prealloc/WMT. get_dma_ops/dma_supported
eram apenas diagnostico local: remover consulta privada, nao a validacao feita
por dma_set_mask_and_coherent. Reuso mainline suficiente; triagem pmaports,
MediaTek/Qualcomm nao demonstra substituto para transporte AXI6765 inteiro.
AXI LG dual GPLv2/BSD, SHA256original registrado no item timers. Glue pequeno
no driver existente; nao criar backend/diagnostico paralelo.

Para demais erros de compilacao AXI: ioremap_nocache antigo ARM e documentado
como alias de ioremap em arch/arm/include/asm/io.h4.9; preservar atributo Device,
nao converter para memoria cacheada silenciosamente. remove callback agora
void, manter corpo/ordem existente; resume usado somente no arquivo pode ser
static. Esses ajustes nao aprovam lifetime, limites de pool, MMIO ou remove
sob carga: o caminho prealloc/WMT ainda requer verificacao antes de probe real.

Resultado: gen4m-axi-dma-linux618-v1.patch faz axiDmaSetup retornar errno e probe
parar antes de CSR/prealloc/WMT em erro. AXI.o inteiro compilou ARM6.18 com
Werror: work/gen4m-lts-axi-build-20261028-b.log. Simbolos do objeto usam
dma_set_mask/dma_set_coherent_mask, sem connectivity_arch_setup_dma_ops.
Header AXI recebeu prototipo da funcao global existente glIsReadClearReg, nao
nova implementacao. Dual GPLv2/BSD, os/linux/hif/axi/include/hif.h SHA256original
39335283dbb37f3c9f430d8b6228bca9547fb34c0ddf9ee5865f4d31e0f300dd.

Teste C/UBSan executou setup/probe reais com doubles DMA/CSR/prealloc/WMT:
larguras invalidas, largura64 sem shift indefinido, erro/defer DMA preservado,
mask pointer ausente, falha CSR antes de callbacks, sucesso e preservacao de
ops/coerencia do dispositivo. Log work/gen4m-axi-dma-host-20261028-a.log. Nao e
teste DMA/IOMMU real. Glue/teste MIT reutiliza harness existente. Fonte4.9,
imagem candidata, runner e aparelho nao alterados. Nao afirmar transporte pronto:
pool reservado, reserva MMIO e ciclo de callbacks WMT/probe/remove ainda tem
lacunas concretas de falha/limites; fechar antes de autorizar uso fisico.

#### Gen4m: timers nativos6.18 — decisao previa2026-10-28

Reusar timer_setup/timer_container_of/timer_delete_sync do Linux6.18.58 local
GPL-2.0; este header nao tem mais from_timer. Mesmos intervalos, mod_timer/add,
locks e ponto de espera sincrona. Nao trocar delete por cancelamento assincrono
nem alegar que impede todo rearm. Timer tickfn tem um unico inicializador e
callback no source LG: tipar kalOsTimerInitialize com callback timer_list e
obter GLUE_INFO de tickfn no kalTimeoutHandler. TX-direct conserva handlers
legados e usa pontes pequenas recuperando ADAPTER pelo timer e seu prGlueInfo
ja estabelecido em wlanAdapterCreate. SER AXI conserva halHwRecoveryTimeout e
reset existente; ponte recupera GL_HIF_INFO e GLUE_INFO proprietarios. Nao
transportar APIs Linux4.9, usar contexto global ou desativar recuperacao SER.

Fontes LG dual GPLv2/BSD, gl_init/gl_kal/gl_kal.h com identidades acima;
os/linux/hif/axi/axi.c SHA256original
8d8b59ef79084e5d5c537707dcf65f738f9900d84757db93a67fe70b671fb404.
Sem commit no snapshot local. Mainline fornece API de timer; triagem
pmaports/MediaTek/Qualcomm nao oferece substituto do protocolo AXI6765.
PCIe nao e transporte deste aparelho e nao sera generalizado neste incremento.
Aceite offline: callbacks com proprietarios distintos nao misturam contexto,
mesmo timeout/flags/wakeup e espera sincrona preservados; compilacao dirigida.
Teardown sob carga real e recuperacao no aparelho continuam nao comprovados.

Resultado: gen4m-linux618-timers-v1.patch preserva handlers legados TX/SER e
seus intervalos; tickfn agora usa callback tipado, sem void* de funcao/data.
Funcoes reais e APIs de timer compilaram ARM com Werror em objeto offline fora
do modulo, log work/gen4m-timer-abi-20261028-a.log. Teste C/UBSan dos corpos
reais passou com dois proprietarios distintos, flags/wakeup, contexto legado
TX/SER, branches mod/add, expiry e chamada timer_delete_sync em cancelamento
repetido: work/gen4m-timers-host-20261028-a.log. Timers e handlers legados sao
doubles nesse teste; nao prova espera/teardown/reset real do kernel. Glue MIT.
Patch final reaplicado com fuzz=0 sobre a baseline dos seis patches anteriores;
os quatro arquivos reconstruidos ficaram identicos a staging.

Builds dirigidos nao apontam mais os erros de timer adaptados, mas gl_init/gl_kal
ainda falham por outras APIs (work/gen4m-lts-timers-build-20261028-a.log).
AXI.o tambem ainda falha por DMA/get_dma_ops/dma_supported, ioremap_nocache,
remove callback e prototipos, log work/gen4m-lts-axi-build-20261028-a.log.
Esse e um bloqueio concreto de transporte/seguranca antes de qualquer probe,
nao justificativa para no-op, ignorar erro DMA ou copiar headers4.9.

#### Gen4m: netdev/NAPI6.18 — decisao previa2026-10-28

Entregavel visado e trafego no wlan0 sem corromper endereco/fila/RX; nesta
etapa somente compilar e verificar glue offline. Reusar netif_napi_add_weight
com mesmo peso64 e mesmo poll, eth_hw_addr_set para atualizar dev_addr via API
(inclui shadow/hash do netdev), netif_rx que no6.18 aceita thread/IRQ e desliga
BH quando necessario, e include publico net/gro.h para napi_gro_flush existente.
Manter registro/unregister/NAPI teardown, perm_addr, endereco BSS/firmware e
locks de GRO. ndo_select_queue novo recebe sb_dev nao usado; algoritmo LG de
prioridade permanece integral, assim como skb/queue mapping. Nao copiar
headers4.9, converter const por cast ou alterar offload para compilar.

APIs do Linux6.18.58 local GPL-2.0, sem HEAD extraido; fontes LG gl_init,
gl_kal e gl_os.h dual GPLv2/BSD tem hashes registrados acima. Mainline fornece
essas APIs; pmaports/MediaTek/Qualcomm da triagem nao substituem o HIF AXI6765.
Extensao pequena ao driver existente, sem nova fila, RX ou controlador.
Aceite: peso/poll e callbacks nativos compilam, MAC temporario altera endereco
BSS e netdev sem alterar perm_addr, atualizacao identica nao escreve novamente.
Nao significa pacotes/RF funcionando no aparelho; nenhum teste fisico autorizado.

Resultado: gen4m-netdev-linux618-api-v1.patch preserva peso64/poll, corpo da
selecao de filas e wlanUninit; troca copias diretas a dev_addr pela API publica,
mantendo perm_addr e BSS conforme caminho original. Cast char sockaddr para
const u8 preserva constness, nao escreve por ponteiro const. Teste C/UBSan dos
dois callbacks MAC reais passou: temporario em BSS/netdev, perm_addr intacto,
guard de entrada e endereco identico sem nova escrita, log
work/gen4m-netdev-host-20261028-b.log. Setter netdev e dobrado nesse teste;
shadow/hash do kernel nao foi ensaiado em runtime.

Corpos reais MAC/selecao de filas, tabela net_device_ops e chamadas NAPI/GRO/RX
compilaram ARM com Werror em objeto offline fora do modulo, log
work/gen4m-netdev-abi-20261028-b.log. Build dirigido gl_init/gl_kal nao aponta
mais incompatibilidades netdev/NAPI tratadas, mas continua falhando por timers,
QoS, proc/fs, metadados/prototipos e notificador FB antigo, log
work/gen4m-lts-netdev-build-20261028-a.log. Nao chamar isso de modulo pronto.
Napi poll LG ja retorna0 porque seu RX alimenta/flush GRO diretamente; esse
codigo foi preservado, nao e novo stub. Glue/teste MIT reutiliza harness C,
com extracao por chaves para nao capturar outra funcao apos comentario em '}'.

#### Gen4m: demais callbacks de tabela6.18 — decisao previa2026-10-28

Aceite offline: completar ABI da tabela ativa, sem casts/remover operacoes,
mantendo backend LG e seus erros. Reusar cfg80211.h/nl80211.c6.18.58 local:
TDLS nao-MLO link_id=-1; radar/stop_ap/bitrate/get_txpower link_id=0; radio_idx=-1
para wiphy nao indexado. Recusar outros IDs antes do backend. change_beacon
recebe cfg80211_ap_update e encaminha somente seu beacon; rejeitar updates
FILS/unsolicited/S1G nao implementados em vez de ignorar pedidos. Nao anunciar
MLO/multirradio/6GHz. LG gl_cfg80211.c/header dual GPLv2/BSD com hashes acima.
AP/TDLS nao sao ampliados como funcionalidade desta entrega: adaptar apenas
contrato exigido pela tabela ja existente para compilar a mesma pilha STA.

Set/get TX power LG sao recusados em STA e backend P2P tambem retorna EINVAL;
preservar isso, nao inventar sucesso nem implementar novos comandos RF.
API permite wdev=NULL para wiphy global: devolver EOPNOTSUPP sem dereference.
Nao mudar valores mBm/dBm, limites/regulatory ou firmware. Framework upstream
cfg80211 e suficiente; pmaports/MediaTek/Qualcomm da triagem nao oferecem
substituicao comprovada de AXI6765. Justificativa do glue e diferenca de ABI,
nao implementar controlador paralelo. Ensaio fisico continua nao autorizado.

Resultado: gen4m-cfg80211-radio-link-abi-v1.patch preserva parametros/erros dos
backends, rejeita indices nao suportados e evita dereference de wdev global
NULL. Corpos reais dos oito callbacks e tabela nativa compilaram em objeto ARM
com Werror, log work/gen4m-cfg80211-radio-abi-20261028-a.log. Teste C/UBSan
aplicando patch a fontes LG fixadas passou para IDs, novos updates AP recusados,
readiness, NULL, limites de modo STA/P2P e erros backend, sem mudar saida dBm
em falha: work/gen4m-radio-abi-host-20261028-b.log. Fonte/teste de glue MIT.
Nenhum comando RF novo; set/get_txpower continuam sem suporte no backend LG.

Serie de cinco patches reaplicada com fuzz=0 a outra copia das fontes LG;
os onze arquivos reconstruidos ficaram identicos a staging. Build dirigido
gl_init.o confirma ausencia dos erros de inicializacao da tabela cfg80211,
mas ainda falha por netdev/NAPI, timers, QoS bandwidth, prototipos/fallthrough
e metadados antigos: work/gen4m-lts-gl-init-build-20261028-b.log. Nao afirmar
modulo completo, radio ou associacao funcionais. Proximo bloqueio e compor
essas dependencias Linux sem copiar headers4.9 ou apagar verificacoes.

#### Gen4m: inscricoes de gerenciamento cfg80211 — decisao previa2026-10-28

Reusar mgmt_frame_regs/interface_stypes da API Linux6.18.58 (GPL-2.0,
cfg80211.h SHA256 ja registrado abaixo), mantendo os filtros LG por interface
STA/P2P e os dois subtipos implementados: PROBE_REQ e ACTION. Adaptar snapshot
aos setters legados existentes, incluindo false para cancelamento; nao usar
global_stypes para ativar filtros de outra interface. Nao reimplementar filtro
firmware, scan ou mailbox; callback pode dormir sob mutex wiphy conforme API.
LG gl_cfg80211/gl_init/headers dual GPLv2/BSD, identidades ja registradas nesta
auditoria. Mainline/mac80211/mt76 fornecem a ABI; alternativas pmaports,
MediaTek/Motorola e Qualcomm da triagem nao substituem o backend AXI6765.
Glue novo pequeno justificado pela troca de callback incremental por snapshot.
Perfil atual CFG_ENABLE_UNIFY_WIPHY=0, dual STA6765 desabilitado no Makefile.
AUTH era anunciado mas nao implementado nesse setter LG; esta mudanca nao
declara conserto de SAE/recepcao AUTH nem amplia subtipos silenciosamente.
Aceite offline: assinatura nativa e codigo real preservando rota/filtros/flags,
inscricao/cancelamento e separacao de interfaces; sem acesso ao aparelho.

Resultado offline: gen4m-cfg80211-mgmt-regs-v1.patch preserva byte a byte o
roteador legado e setter STA; acrescenta somente adapter snapshot, prototipo
e troca do callback na tabela ativa. Corpos reais de roteador/adapter e campo
cfg80211_ops nativo compilaram ARM com Werror (objeto offline fora do modulo),
log work/gen4m-cfg80211-mgmt-abi-20261028-a.log. Teste C/UBSan usa estes corpos
reais e setters STA/P2P dobrados, cobrindo mascara por interface, enable/disable,
subtipo nao implementado, mascara multicast, guard NULL e readiness, log
work/gen4m-mgmt-regs-host-20261028-b.log. Nao comprova filtro aplicado pelo
firmware. Sem carga, nova imagem ou mudanca eletrica. Outros callbacks e
QoS bandwidth continuam impedindo o modulo completo; proximo incremento deve
adaptar suas assinaturas/semantica, nao remover operacoes para compilar.

#### Gen4m: ABI cfg80211 de chaves6.18 — decisao previa2026-10-28

Entrega visada e associacao STA protegida com trafego. Reusar os cinco callbacks
LG de chaves e seus backends STA/P2P, acrescentando link_id exigido pelo header
cfg80211.h6.18.58 local (GPL-2.0, arvore extraida sem HEAD). Contrato documenta
-1 para nao-MLO; driver6765 nao anuncia suporte MLO. Recusar qualquer link_id
diferente de-1 antes de acessar o contexto ou chamar firmware. Nao ignorar
link_id, fazer cast de callback, mudar cifragem ou remover operacoes da tabela.
Mainline/mac80211/mt76 e cfg80211 fornecem ABI, nao firmware/transporte AXI6765;
pmaports/MediaTek/Qualcomm da triagem nao demonstram substituto desse backend.
Patch pequeno no roteamento Linux LG dual GPLv2/BSD, sem driver paralelo.

Origem local LG sem commit: os/linux/gl_cfg80211.c SHA256
ecba08fef1418d49062c417a7f839c439c7fd5dcdccbe2ee21ccfd32edcc06a7;
os/linux/include/gl_cfg80211.h SHA256
5e5590841d371773f9815afe1ff727c6c6a28698bc8b0a42a6368173cc3fc231.
Preservar readiness, parametros/callback get_key e retorno dos backends sob erro.
Verificar assinaturas com a struct cfg80211_ops real do6.18 e exercitar funcoes
reais com backend dobrado. Compilacao nao comprova instalacao de chaves ou WPA
no aparelho. Outro bloqueio observado, roam_info.bss migrou a links[0].bss,
deve preservar referencia BSS e IEs, sem anunciar MLO.

Resultado offline: gen4m-cfg80211-keys-roam-v1.patch altera somente os cinco
roteadores e seus prototipos, mais o campo links[0].bss no roam_info zerado
(valid_links=0/ap_mld_addr=NULL do caminho nao-MLO). Nenhuma transferencia ou
liberacao de referencia BSS, IE ou chamada cfg80211_roamed mudou. Header6.18
include/net/cfg80211.h SHA256:
bccd698032f5a7b9b88ec1026e8b9ce4d78697c8b185f8427b8c42d59c741442.

Os cinco corpos reais de callback e tabela cfg80211_ops compilaram em objeto
ARM isolado com includes nativos e Werror, log
work/gen4m-cfg80211-key-abi-20261028-c.log. key_abi_check.c na copia staging e
somente esse ensaio offline, fora dos objetos do modulo; nao e driver novo.
Teste C/UBSan executou os corpos reais do patch com backends dobrados: grupo
(MAC NULL)/pairwise, STA/P2P, get_key cookie/callback, erro de readiness e
retornos de backend preservados; link invalido recusado antes de acessar
contexto, inclusive com contexto NULL. Log
work/gen4m-cfg80211-keys-host-20261028-c.log. Glue/teste MIT reutiliza harness C
existente. Gerenciamento de chaves de gestao STA continua retornando o erro
legado; nao simular suporte. Criptografia, roaming e associacao nao ensaiados
no aparelho; outros callbacks cfg80211 e QoS bandwidth ainda impedem o build.

#### Gen4m: decisao previa de boost CPU nativo — 2026-10-28

Reusar cpufreq_cpu_get/put e freq_qos_add/remove_request do Linux6.18.58 local,
GPL-2.0, sem HEAD Git na arvore extraida. Identidade SHA256 de cpufreq.c:
12399b42bc7e528153fd0a687526f30f736b28fd4acfd0bf69a936dd2890e7e4;
kernel/power/qos.c:
63d5d5a98477a6f28fe879beee2203e133003768a876983a810a9c19ecd8b25d.
Vendor cpu_ctrl/topo_ctrl ausentes;
copiar seus headers nao implementa PPM. Consulta da referencia Motorola
gen4m1e0e348/os/linux/plat/mt6765/plat_priv.c retornou404; nao e doador
confirmado. Mainline/pmaports/Qualcomm nao fornecem o PPM MT6765 especifico;
freq_qos e o framework existente suficiente, sem controlador paralelo.

Adapter pequeno no plat_priv.c LG dual GPLv2/BSD, preservando limiar de boost.
Requisitar somente FREQ_QOS_MIN ate cpuinfo.max_freq, nao copiar voto vendor
min=max de3GHz nem sobrescrever FREQ_QOS_MAX/limite termico. Cpufreq6.18
limita min ao max agregado em cpufreq_set_policy; nenhuma voltagem/OPP nova.
Uma referencia/pedido por politica, ate os tres clusters ja previstos no LG;
falha parcial desfaz todos os pedidos/referencias adquiridos. Sem politica:
retornar ENODEV, nao sucesso no-op. Perfil atual nao habilita ARM_MEDIATEK_CPUFREQ;
disponibilidade real e beneficio de desempenho continuam nao comprovados.

Escopo e a unica radio integrada6765: owner e mutex de modulo, inicializados
por kalPerMonInit e fechados por kalPerMonDestroy (remove/reset), com stop
liberando votos mesmo em chamadas repetidas. Callback de monitor vem da thread
wlan via wlanTimerTimeoutCheck/cnmTimerDoTimeOutCheck, fora do spinlock CNM;
nao executar cpufreq/freq_qos em timer IRQ. Novo owner diferente e recusado,
chamadas tardias apos destroy nao readquirem votos. Verificar erros de QoS,
politica ausente, clusters compartilhados, stop/destroy/reinit em teste offline
do codigo real. Nao habilitar boost fisico sem validar termica/cpufreq.

Resultado offline: plat_priv.o ARM compila com Werror (build completo log
work/gen4m-lts-build-20261028-b.log recompilou o objeto apos os guards finais).
Teste do patch aplicado a fontes LG fixadas passou com UBSan e mutex pthread:
work/gen4m-cpu-qos-host-20261028-b.log. Executa funcoes reais de boost, stop,
disable e destroy, com doubles somente para CPUFreq/QoS/CNM; inclui corrida
vote/destroy/reinit, rollback parcial, erros QoS, ENODEV, limite de clusters,
owner distinto e stop repetido. Nao e teste de termica/hotplug no aparelho.
Cleanup adicional antes de wlanAdapterDestroy cobre probe falho; reset reabre
owner explicitamente em wlanOnWhenProbeSuccess. DRM/energia e EMI nao alterados.

Patch gen4m-cpu-freq-qos-v1.patch e incremental apos o patch PDMA. Arquivos LG
afetados mantem dual GPLv2/BSD: plat_priv.c SHA256original
8580f2615efb33fd3ed3042ab8309ccac4b3c24c9c75110e2d7eafaae5c74509;
os/linux/gl_kal.c SHA256original
029bb66f2ab748c9a780df5399d00a6a368f13ad8034f2d7367aabc2186eada8;
gl_init.c e include/gl_kal.h tem identidades registradas acima. Snapshot LG
local sem commit; glue/teste novo MIT reutiliza framework de testes C existente.

Modulo inteiro continua sem compilar: log-b aponta headers stddef/prototipos,
zeragem parcial de array de ponteiros e fallthrough no common. Build dirigido
gl_kal/gl_init (work/gen4m-lts-glue-build-20261028-a.log) tambem mostra ABI
cfg80211 antiga, QoS vendor de largura de banda GPU, netdev/timers/proc e
notificador FB removidos. Nenhum erro foi suprimido. Proximo passo funcional e
adaptar interfaces Linux existentes sem transportar a pilha vendor de energia;
nao produzir nova imagem ou carregar gen4m antes de fechar esses bloqueios.

#### Sessao candidata curta — preparacao offline2026-10-28

Sem resposta humana a solicitacao de operacao fisica: continuar somente offline.
Entrega visada e limitar a primeira sessao residente a120s pelo dado existente
etc/k40s-session-seconds, em vez da baseline3600s. Nao tocar codigo watchdog,
init/SSH/PID1 nem registro/runner. Reusar GNU cpio para gerar o unico registro
substituto; o leitor newc existente fornece os limites para encaixa-lo sem criar
encoder paralelo. Todos os outros registros da base devem ficar byte-identicos.
Mudanca intencional e somente o valor canonico120 newline, com mesmo modo/uid/gid
e sem membro duplicado ou token novo. Origem glue MIT/GNU cpio2.15 GPL-3.0-or-later,
mesmas interfaces Linux/LG ja auditadas. Mainline/pmaports e MediaTek/Qualcomm
nao mudam esse limite especifico de sessao do laboratorio. Protecoes reforcadas,
nao relaxadas para obter aprovacao; imagem continua boot_policy=forbidden.

Resultado: v13/v14 concluidos e com SHA256 identico
2938ca25648cb732c7b31b800df64ee04f9200e3563a6a315dbc2d0c58bd7fa0.
Seis testes dirigidos passaram, incluindo leitura da imagem real, preservacao
byte a byte dos demais registros, recusa de valor inesperado/hardlink antes
de gerar substituto e copia/bootstrap ARM do payload. Logs
work/connsys-short-session-host-20261028-b.log e
work/connsys-runtime-boot-build-20261028-m.log / -n.log. Limite configurado120s,
nao evidencia de expiracao/watchdog real; nenhum ensaio fisico realizado.

#### Startup comum manual e acesso pelo resident — decisao previa2026-10-28

Entrega: WMT/BTIF vinculados e launcher LG com fd stpwmt, sem ligar BT/Wi-Fi.
Aceite offline: guarda de perfil/hash/fresh-boot precede mutacoes; uma tentativa
por boot; falha nao dispara unload/retry nem mata launcher de outra sessao.
FD aberto nao comprova configuracao/firmware: resultado deve dizer attached,
firmware_validated=false. Ensaio fisico continua nao autorizado nesta etapa.

Reuso: ssh-ram-prepare ja copia /etc/ssh-payload/. para o root resident em RAM.
Mover a capsula para esse payload resolve visibilidade sem modificar scripts
de init/SSH/PID1 validados. Bibliotecas novas ficam em opt/k40s-connsys; loader
musl privado e PYTHONHOME explicito executaram Python ARM/framing em QEMU,
log connsys-private-python-bootstrap-20261028-a.log. Firmware fica no root initns.
Nao substituir musl/SSH do resident, nem iniciar OpenRC/BlueZ automaticamente.

Reusar wmt-detect.py (projeto MIT) com initialize/main import-safe, mesmo ABI
de tres ioctls; no caminho nativo exigir6765 e retorno0. Launcher, propshim e
runtime LG permanecem binarios originais. Codigo novo MIT apenas glue manual:
bind de dev/proc/sys para o runtime Android, insmod lg_btif/wmt, helper existente,
launcher com chroot no filho, ambiente limpo e sem herdar watchdog fd. Nao criar
protocolo/driver/daemon novo. APIs Python subprocess/os e BusyBox mount/insmod
ja sao os frameworks da composicao; mainline/pmaports/MediaTek/Qualcomm nao
fornecem esse orchestrador especifico do laboratorio LG. Arquivos e efeitos
separados da pilha vendor, nao portar wifi-up.sh ou depender de gen4m.

Nao usar killall, limpar dmesg, mudar timeout global de firmware, desligar rails,
abrir stpbt, carregar bt_drv ou iniciar RF neste incremento. Falha conserva
modulos/mounts ate recuperacao por reset validado; timeout userspace nao garante
interromper ioctl em estado D. Preservar supervisor/watchdog, sem afirmar
cleanup seguro do WMT sob falha. Marker em run e estado da tentativa, nao
autorizacao fisica. Usar este caminho somente apos aprovacao humana separada.

Resultado offline: wmt-detect import-safe preserva tres ioctls e fecha FD em
erro, com opcao6765/retorno0 no caminho nativo. Nove testes dirigidos cobrem
guard/claim, erro sem launcher, erro de attach sem unload/retry, sinal somente
ao filho proprio, preservacao da falha original e chip/init/ioctl invalidos.
Log work/connsys-manual-start-host-20261028-b.log. Kernel/launcher sao doubles
nesses casos, nao prova de probe ou de firmware no aparelho.

Integracao real do pacote em QEMU: cpio extraido, cp -R original com BusyBox ARM,
loader musl/Python privado, helpers --help e framing executados da copia RAM.
Hashes dos modulos/launcher/propshim empacotados conferem com o starter. Firmware
real no payload SSH e links no root inicial atendem init_task.fs antes/depois
do handoff, sem duplicar blobs; leituras nos dois roots deram bytes iguais.
Todos os membros cpio originais e scripts init/resident/SSH/PID1 preservados.
Log work/connsys-resident-copy-arm-20261028-d.log. Nenhum hardware acessado.

Imagem v11/v12 byte-identica por cmp, SHA256
731bfd54eb76e9ee46e753e0e1dded30490d3a18d124db9a12a25714afe36d9e;
ramdisk29855757 comprimido/66199040 bruto, margem45056. Symlinks novos tiveram
timestamps normalizados apos v9/v10 revelarem variacao. Logs build-20261028-k/l
em work. Limite3600s da baseline preservado; antes do primeiro ensaio preparar
limite curto120s e obter autorizacao especifica, sem relaxar politica/registro
ou runner. Continua boot_policy=forbidden. O glue nao pede function-on
diretamente; efeitos internos do launcher continuam nao comprovados.

#### Composicao de boot CONNSYS — decisao previa 2026-10-28

Entrega visada: imagem temporaria com runtime disponivel em RAM, firmware no
root do loader e DT consumidor, sem startup automatico de radio. Reusar
tools/build-boot-image.py e GNU cpio2.15 para append newc; nao escrever outro
encoder boot/cpio nem alterar registro fechado de kernels ou runner fisico.
LG/kernel6.18/Alpine/launcher seguem origens e licencas acima. Codigo novo MIT
somente glue de composicao, checagem de hashes e extracao reversa, necessario
para reunir as entradas ja preparadas sem refatorar o builder legado.
Mainline/pmaports fornecem formatos/frameworks usados, mas nao essa composicao
LG; MediaTek/Qualcomm nao mudam header/enderecos confirmados desse aparelho.

Base preservada: imagem provider-only b7cd790ac10c056c7114a40a56ca3444363653ebe2382b393766257f0395d510.
Kernel recompilado zImage -Werror, log work/connsys-kernel-zimage-20261028-a.log,
SHA8045c62e6ebaf3af4fb6950f4ac8ef6f16ba421b15911d10432ed3fe9c617acd;
nao registrar como aprovado no aparelho. Limites mantidos: particao41943040,
initramfs descomprimido64MiB, load addresses e cmdline originais. Membros da
base cpio devem permanecer byte-identicos; novos arquivos so em opt/k40s-connsys
e lib/firmware. Nenhum hook/runlevel/modprobe novo e nenhuma execucao de capsule.

Checker LK original recusou candidato por phandle adicional em reserva EMI,
log work/connsys-consumer-lk-overlay-20261028-a.json. Nao mudar checker nem
referencia original. Criar referencia candidata independente da original,
acrescentando somente phandle unico ao mesmo no; validar que todos os outros
nos/propriedades/reservas permanecem iguais. Isto atualiza metadado esperado do
DT consumidor, nao limites de memoria ou politica do verificador. Checker antigo
sera executado sem mudanca, com referencia candidata e todos os DTBOs LG.

Revisao IRQ durante composicao encontrou erro funcional do primeiro overlay:
ligava IRQs LEVEL_LOW diretamente ao GICv3, cujo gic_set_type6.18 rejeita LOW
para SPI. LG4.9 ext_gic/mtk-gic-v3-extend.c configura inversor via
_mt_irq_set_polarity, nao basta trocar o flag para HIGH. Reusar SYSIRQ upstream
drivers/irqchip/irq-mtk-sysirq.c GPL-2.0-only (ja compilado por ARCH_MEDIATEK):
o dominio em /interrupt-controller@10200a80 ja existe e permanece inalterado,
binding mediatek,mt6577-sysirq admite MT6765 e inversao por SPI. set_type nativo
preserva LOW no consumidor, programa intpol e passa HIGH ao GIC pai. Alteracao
minima: interrupt-parent de WMT/BTIF para &sysirq, mesmos IDs/flags do backup;
sem C novo, sem escrever registrador em teste host. Imagens v2/v3 ficam
supersedidas pelo candidato com SYSIRQ; nenhuma foi usada no aparelho.

Resultado de composicao: imagens staging v4/v5 byte-identicas por cmp,
SHA8ebcdc820afc39f60920850490b4394c8e7962e721ce78908d2099214528b0b9.
41943040 bytes, ocupacao41889792 e margem53248; ramdisk29849290 comprimido,
66155008 bruto (abaixo de64MiB). Round-trip kernel/ramdisk/DTB/cmdline e
enderecos aprovados. Prefixo/membros cpio originais byte-identicos, somente
adicoes opt/k40s-connsys e lib/firmware, nenhum autostart de radio acrescentado.
Imagens anteriores e entradas validadas preservadas. Config/registro fechado
e runner fisico nao foram alterados; imagem segue proibida para boot fisico.

Testes direcionados passaram: hashes errados e saida existente/fora de artifacts
recusados antes de subprocessos; cpio/header invalidos recusados; imagem real
reextraida preserva base e firmware em initns. Checker LK original aprovado
nos seis overlays com referencia candidata independente; tests DT tambem provam
que MMIO/IRQs/parents/SYSIRQ nao sao sobrescritos pelos overlays LG.
Logs work/connsys-runtime-boot-build-20261028-d.log/e.log,
work/connsys-runtime-boot-host-20261028-b.log e
work/connsys-sysirq-dt-host-20261028-a.log. Primeira tentativa de cpio-a falhou
por falta de --create junto a --append; corrigido sem alterar verificadores.
Timestamps dos dois diretorios novos fixados para permitir reproducao exata.
Nao comprova boot ou recuperacao fisica deste novo kernel, probe, energia,
handshake launcher nem Bluetooth. Proximo incremento e startup comum e revisao
dos parametros de recuperacao, antes de qualquer nova autorizacao fisica.
System.map recompilado conserva __log_buf=c1e8a284 e _end=c1ee8a10 da baseline
provider-only, mantendo a mesma janela de coleta41e8a000/21000 para o buffer
20000. Isto verifica o posicionamento estatico, nao uma nova recuperacao fisica.

#### Capsula userspace de CONNSYS — preparacao offline 2026-10-28

Bloqueio: resident RAM nao contem Python; nao substituir seu loader/musl/SSH
validados para executar wmt-detect.py e stp-bluetooth.py existentes. Reusar
Alpine minirootfs3.24.2 armv7 e apk oficial com Python em root separado,
sem novo interpretador, daemon, driver ou emulacao. Archive local SHA256
5552f1ef2398cee46ef2cf733f8f1258f39a77ad065dfd47282fc0df9fe1976c
confere com SHA256 publicado em dl-cdn.alpinelinux.org/alpine/v3.24/releases/armv7/.
Pacotes devem ser verificados pelo apk com suas chaves oficiais; nao usar
--allow-untrusted ou scripts de instalacao. CPython PSF-2.0, musl MIT;
versoes/licencas efetivamente instaladas serao registradas pelo banco apk.

Manter runtime Android privado existente em /opt/android-rt dentro da capsula,
sem redistribuir firmware/binarios. Kernel mainline/MediaTek/pmaports/Qualcomm
nao fornecem substituicao comprovada desse launcher LG; reutilizar o fecho
bionic ja extraido, propshim MIT e scripts existentes. Integracao e arquivos
de placa, nao novo framework. QEMU binfmt ARM existente sera usado somente
para import/framing offline, sem dispositivos reais, bind mounts ou rede do
telefone. Capsula nao altera rootfs/particoes/imagens e nao tem auto-start.
O firmware do kernel precisa ficar no root initramfs, nao apenas no chroot
userspace; separar esta necessidade da busca de firmware feita pelo launcher.

Resultado: capsula privada armv7 pronta em
`work/connsys-userspace-20261028-v1.tar.gz`, SHA256
19fe19c12239e57757f1fb1ed53b1afac3894c6941af27aa096af351224aa10d,
25337938 bytes. CPython3.14.10-r1, musl1.2.6-r2, BlueZ5.86-r2 e D-Bus1.16.2-r2;
45 pacotes, banco apk com versao/licenca/arquivos incluido, sem bypass de assinatura.
BlueZ/D-Bus reutilizados, nao novo daemon. Conta messagebus e machine-id
descartavel criados explicitamente como previsto nos scripts do pacote D-Bus;
nao executar scripts de instalacao completos, nao copiar identidade do host.
Rootfs e bibliotecas resident/SSH continuam intocados. DNS do host removido
da copia de staging; nenhum dispositivo WMT/BTIF existente no chroot offline.

Validacao do archive descompactado em diretorio novo: Python ARM real via
binfmt/QEMU executou testes existentes de framing e nova verificacao da sequencia
initialize_address existente (HCI reset, vendor0xfc1a e Read_BD_ADDR, com doubles
de CID/command, inclusive readback divergente). Nao substitui teste de radio.
BlueZ --version e D-Bus --version executaram; D-Bus ARM abriu socket em
namespaces novos mount/PID/network e encerrou no limite. Logs e composicao em
[userspace CONNSYS de staging](lts-connsys-userspace.md).

Compatibilidade do launcher: primeiro ensaio QEMU recebeu SIGSEGV, rastreio
mostrou ENOENT /dev/null imediatamente antes; com null veio SIGABRT por falta
de /proc/self/exe. Proc isolado removeu essa falha; propshim existente carregou
e o launcher chegou a open /dev/stpwmt -> ENOENT, sendo interrompido no limite.
Nao classificar como handshake aprovado, nem atribuir os aborts a bug QEMU.
REA binary_session confirmou perfil Windows GhidraP0 sem suporte ELF ARM e
inspect_binary_layout sem provider Linux/pwntools. Nao repetir open rejeitado,
instalar engines ou reparar configuracao. Conforme skill, fallback focado
QEMU_STRACE foi registrado como evidencia de shell, nao REA Evidence/decompilacao.
Nenhum binario LG alterado e nenhuma operacao de telefone executada.

#### DT consumidor WMT/BTIF nativo — decisao previa 2026-10-28

Bloqueio concreto anterior ao launcher: a baseline SOC atual tem somente um stub
/consys@18002000 disabled e nenhum BTIF. O overlay anterior fornece apenas genpd.
Entrega visada: WMT/BTIF recebem recursos reais, reservam EMI e adquirem rails
nativos; nenhum script novo de startup resolve a ausencia desse contrato DT.
Aceite desta etapa e offline: overlay compila/aplica na baseline fixada, recursos
MMIO/IRQ preservam os bytes do backup BMW e os phandles resolvem providers atuais.

Reusar LG MT6765/backup real overlay-0-id0-rev6.merged.dtb (demais identidades
nao sao prova de selecao em runtime). Reg de WMT conserva13 slots, inclusive
dois buracos, e tres IRQs; BTIF conserva3 janelas e3 IRQs. Fontes LG GPLv2;
novo DT GPL-2.0-only. Linux6.18.58 commit2926d88: binding mt6357-regulator e
driver nativo fornecem ldo-vcn18/28/33-bt/33-wifi, supplies consumidos pelo WMT
ja adaptado; mt6765-clk.h usa BTIF18 e AP_DMA27 (nao IDs vendor antigos).
VCN18/28 fixos1800000/2800000 e VCN33 limitado3300000, conforme backend LG.
Nao usar fixed-regulator falso nem copiar clocks antigos scpsys.

Framework escolhido: genpd nativo e propriedade privada ja auditada
mediatek,conn-power-domain, nao power-domains (evitar auto power-on antes do
probe). Reusar reserva CONNSYS dinamica4MiB/alinhamento16MiB/no-map da baseline,
sem inventar base fisica nem outra reserva. Overlay consumidor inclui a mesma
estrutura do provider anterior com label local; arquivo provider-only validado
fica intocado. Pinctrl default original e vazio; GPS/LNA nao sao requisitos BT.
Triagem mainline/pmaports/MediaTek/Qualcomm anterior continua sem substituto
comprovado da sequencia LG6765; somente extensao DT local, sem driver novo ou RE.
Nao aplicar no aparelho: probe pode escrever remapeamento EMI e infraestrutura,
e registrar reguladores pode alterar rails; autorizacao/protecoes seguem exigidas.

Resultado offline: novo arquivo mt6765-k40s-wmt-btif-overlay.dts compilado e
aplicado a baseline SOC sem warnings ou supressoes. Primeiro DTC apontou
reg_format porque reg estava no __overlay__ de um fragmento sem contexto do pai;
mover o consumidor para o overlay raiz com #address/size-cells2 resolveu sem
alterar os bytes reg. Provider-only e todas as imagens existentes intocados.
DTBO candidato SHA256eea27afb35785e2bba5021459df2e74da35b1c88f2d85468e1dd6d1ba719eaf8;
DTB composto75ca8aad8cd646701dafb3560c089a3ceafed31ef348129ceea83dac6aa077cd,
ambos em work/wmt-btif-consumer-20261028.* (nao boot/flash).

Verificacao em tools/tests/test_mt6765_connsys_dt.py compara reg/IRQs/compatible
de WMT e BTIF com o DTB real do backup, incluindo os13 slots WMT; confirma
phandles de EMI/genpd/GIC/CCF/rails, nomes de clock e limites de tensao.
Reserva dinamica existente nao muda (so recebe phandle), demais nos existentes
fora do stub consumidor e symbols permanecem iguais. Provider-only continua
passando. Log work/wmt-btif-consumer-dt-host-20261028-a.log aprovado.
Nao validado: alocacao EMI no boot, probe/bind real, handoff OFF, clocks/rails,
firmware/launcher ou trafego. O contexto RAM resident atual nao inclui Python;
o caminho Python legado necessita userspace Alpine ou empacotamento explicito,
nao sera iniciado automaticamente so porque os modulos compilaram.
Proximo incremento: compor este DT com o runtime comum, sem ativar gen4m para
Bluetooth; manter os gates de autorizacao, energia e recuperacao antes do ensaio.

#### Reuso do runtime existente e dono unico STP — 2026-10-28

Entrega visada: uma sessao Bluetooth utilizavel sem segunda abertura rearmar
semaforos ou ligar/desligar o radio da primeira. Aceite offline: segunda abertura
retorna EBUSY antes de qualquer efeito; fechamento confirmado permite nova sessao;
falha de energia nao libera admissao para outra tentativa sobre estado incerto.

Reuso confirmado: tools/phone/wifi-up.sh, wmt-detect.py, propshim.c e
stp-bluetooth.py ja integram o launcher original e inicializam BD_ADDR.
O runtime privado /var/tmp/k40s-android-rt/root e o archive
installer/out/android-rt.tar.gz existem; contem launcher, bionic, WMT_SOC.cfg e
soc1_0_ram_bt_1_1_hdr.bin. Nao extrair outra copia, publicar binarios ou executar
esses scripts. A ponte Python existente e preservada; a candidata BlueZ nao
demonstrou equivalencia de inicializacao de endereco e nao a substitui.
wifi-up.sh e legado4.9: insmod, killall, dmesg -c, firmware timeout global e
dependencia de gen4m nao serao transportados automaticamente ao ensaio6.18.

Origem da alteracao: stp_chrdev_bt.c LG GPLv2 (hash de base da etapa anterior
de0abe3d9db6e412f4c74fd9963aa986d0fc60e100c8120d167403e66c638d14).
Linux6.18.58 fornece atomic_cmpxchg/atomic_set via linux/atomic.h; reusar esta
API, sem novo gerenciador de sessoes. VHCI upstream cria hci_dev por fd e nao
resolve exclusividade desse char LG global. MediaTek/LG e o backend compativel;
drivers pmaports/Qualcomm ou btmtk de outro transporte nao resolvem essa corrida.
Esforco pequeno: flag privada adquirida antes de func_on, liberada somente em
func_off confirmado (inclusive STP-not-ready). Falha de func_on ou de func_off
mantem admissao fechada; nao acrescentar reset automatico nem unload como
recuperacao. Esse gate nao prova drenagem de callbacks ou lifecycle completo WMT.

Resultado: `bt-legacy-exclusive-open-v1.patch` aplicado apos
bt-legacy-linux618-api-v1.patch. Build ARM -Werror/modpost aprovado em
`work/bt-legacy-exclusive-build-20261028-b.log`, sem stubs. O primeiro build-a
recusou exports vmlinux duplicados: o Module.symvers criado na etapa VHCI ja
incluia vmlinux; remover apenas a entrada redundante de KBUILD_EXTRA_SYMBOLS
(mantendo WMT e o Module.symvers real padrao) resolveu. Nenhum verificador
relaxado. Aviso legado MODULE_DESCRIPTION ausente permanece.

Init/exit anteriores e open/release reais passaram com ASan/UBSan em
`work/bt-legacy-exclusive-regression-20261028-a.log`: abertura reentrante durante
func_on e segunda abertura ativa nao chegam ao backend; close confirmado
permite reabrir; func_on falho, STP-not-ready com off falho e close com off falho
mantem admissao fechada. STP-not-ready com off confirmado permite retry.
A retencao apos falha de func_on e deliberada: sem prova de rollback eletrico,
nao repetir energizacao automaticamente. Reset/recuperacao autorizados ficam
pendentes; descarregar/recarregar o modulo nao e mecanismo aprovado de recuperacao.
Registros e drenagem de callbacks continuam como no LG nesta alteracao.
Nao demonstrado seguro para carga fisica ou substituicao do caminho4.9 validado.

SHA256 stp_chrdev_bt.c
3b564b34462a227add99a67ea4c9d5b9638a939686798238c1b6f2cbca8de4ec;
bt_drv.ko ffda53eb6e1b2aea084e4b1f858a5d4ad1062bbf0a712dd6d03c5b90cc116360.
Dry-run reverso do patch sem fuzz aprovado. Runtime somente inspecionado:
launcher SHA256690fbefab3b35c8c96974f58984fe628da9221fc48ad9112227c42748b26af0c;
BT firmware235c723b30850daf0be7853094d37a723756498920e86b0a02c5d03969277320;
WMT_SOC.cfg fc633926687a925801f749a20ca3fc3181a440b3996406d454cdd17a8b3c9d4b.
Os tres nomes estao tambem no archive existente. Macros WMT_IOCTL/WMT_IOC_MAGIC
do wmt_dev.c staged continuam iguais ao original; isso nao prova os layouts,
o handshake do launcher nem o funcionamento de firmware no6.18.
Proxima integracao deve partir desse runtime e da inicializacao Python existente,
sem depender de gen4m apenas para subir BT e sem adotar wifi-up.sh legado inteiro.

#### Ponte STP/HCI: decisao previa — 2026-10-28

Reuso escolhido: BlueZ5.83, tag anotada bd70451b69d736008596ccbf22a97a69fea2cbfa,
commit d97d1951b447f8575e972458d3007afcfed6cf28, copia isolada
`bluez-btproxy-5.83-20261028-v1`. tools/btproxy.c GPL-2.0-or-later;
src/shared/{mainloop,mainloop-notify,io-mainloop,timeout-mainloop,queue,util}.c
LGPL-2.1-or-later; ecc.c BSD-2-Clause. Cabecalhos preservam SPDX upstream.
Reutilizar framing H4, VHCI, epoll e limpeza existentes; wrapper Makefile MIT
somente para compilar essa ferramenta sem daemon/servicos Android.

Linux6.18 hci_vhci GPL-2.0-or-later suporta registro HCI, mas nao energiza/inicializa
CONNSYS; LG WMT/STP/BT permanece responsavel. btattach exige TTY, btmtk de
USB/UART nao substitui BTIF integrado. Triagem postmarketOS/MediaTek/Qualcomm
continua sem backend6765 equivalente confirmado, conforme tabela acima.
Nao usar RE nem outro protocolo para uma lacuna ja explicada pelo fonte.

Extensao pequena escolhida: modo explicito --stpbt, sem ativacao automatica,
abre VHCI antes do char LG e fecha ambos em erro/termino. O driver char
pode ligar o radio no open: compilar/testar apenas com endpoints simulados,
nunca executar esse modo com syscalls reais nesta etapa. Preservar modos
upstream. Tratar EOF, tamanho H4 invalido e write zero/EAGAIN no novo modo
como falha com saida, sem loop ocupado, descarte silencioso ou retry de pacote
parcial. Nao adicionar fila/framework novo; contrapressao sob carga e init
firmware/endereco permanecem requisitos anteriores ao aceite fisico.

Resultado: `bluez-btproxy-stpbt-v1.patch` aplicado somente ao checkout isolado;
checagem reversa git apply --check aprovada. SHA256 tools/btproxy.c
99618520acbef5eac3f62c5a51c4679e1f9b78acc06c7f0ac22b3778c51bd069.
Build ARM estatico aprovado, sem interpretador dinamico ELF, SHA256
a0350bbd8a53f2b9ffb16d6381499a153da3892be972001074791ba669919ef6;
log `work/bluez-btproxy-stp-static-arm-20261028-a.log`. Comando reproduzivel
no checkout BlueZ: `make -B -f <repo>/patches/kernel/staging/bluez-btproxy-5.83.Makefile CC=arm-linux-gnueabihf-gcc LDFLAGS=-static`.
Avisos upstream de parametros nao usados preservados, sem flags para suprimi-los.

Host com ASan/UBSan aprovado em `work/bluez-btproxy-stp-host-20261028-b.log`:
fonte real inteiro incluido, open de /dev/vhci e /dev/stpbt obrigatoriamente
substituido por pares de sockets. Verificados framing de comandos/eventos/ACL,
fragmentacao/coalescencia, caminho normal upstream e STP, recusa de argumentos
incompativeis antes de open, falta de VHCI antes de abrir STP, create VHCI curto,
falha de cada registro epoll e fechamento dos descritores. EAGAIN, write0,
escrita parcial seguida de EAGAIN, tamanho65535 sem wrap, tipo invalido, EOF e
HUP/ERR no novo modo terminam em erro, sem busy retry ou uso de proxy liberado.
Modo STP nao aceita emulacao ECC, AMP ou outros transportes. Isto nao verifica
um controlador HCI real, fluxo sustentado, BD_ADDR ou firmware.

Dependencia kernel tambem compilada, sem modificar .config/zImage/DTB ou carregar:
alvos crypto/ecc.ko, crypto/ecdh_generic.ko, net/bluetooth/bluetooth.ko e
drivers/bluetooth/hci_vhci.ko, -Werror e modpost com exports vmlinux reais;
CONFIG_BT_HCIVHCI=m apenas na chamada make. Primeira tentativa de bluetooth.ko
isolado recusou crypto_ecdh_key_len/encode_key; build conjunto das quatro
dependencias passou, log `work/bluetooth-vhci-dependencies-build-20261028-a.log`.
HCI/VHCI e ECDH sao Linux6.18.58 inalterado (ecdh.c/ecdh_helper.c
GPL-2.0-or-later; ecc.c BSD-2-Clause, MODULE_LICENSE Dual BSD/GPL), sem adaptar
hardware Qualcomm. Ordem declarada nos depends: ecc -> ecdh_generic -> bluetooth
-> hci_vhci. Reconferencia posterior: Module.symvers contem os exports vmlinux
mais os desses quatro modulos (14158 linhas, contra14041 do vmlinux.symvers),
nao os de todos os modulos possiveis do kernel. Nao importar vmlinux.symvers
novamente em KBUILD_EXTRA_SYMBOLS quando esse Module.symvers ja e lido pelo Kbuild.
Fragmento staging `bluetooth-stp-vhci.config` registra a selecao para futura
composicao isolada; a .config atual continua com VHCI desativado.

SHA256 dos modulos gerados:
ecc e5df2d43144b1083bddfe10ef7048ae87d0e11177e9a91e185be199be5146a64;
ecdh_generic fc849f504123ac1b0f57a24ce6982504aa65bce7ff208f5514531b1392c97f45;
bluetooth 3b74ecb5a8ccde737c0715716c8388048ebdfff77bb1c912908ca61b7c846a04;
hci_vhci ff9cd3ffc2e00f5dca35afe82f8ed10f43ccb9c021d40e9d6ce51780d8f79333.
Todos com vermagic6.18.58-k40s-nativeusbemmc1-NOT-FOR-FLASH ARMv7.

Proximo bloqueio funcional: composicao do launcher/firmware/configuracao e
endereco Bluetooth vendor com o WMT adaptado; seus ioctls SET_PATCH_INFO,
WMT_CFG_NAME e STP_MODE existem, mas nao foram exercidos nessa composicao.
Open LG pode acionar hardware antes de haver controle exclusivo; acesso
exclusivo e recuperacao de erro precisam estar definidos antes do ensaio.
Nao instalar servico automatico nem executar --stpbt no aparelho por causa
desses resultados. Permanecem a autorizacao fisica e as protecoes vigentes.

Entrega no aparelho pretendida: controlador HCI reconhecido pelo BlueZ, depois
descoberta, pareamento e comunicacao basica, com USB/SSH preservado. Esta etapa
somente localiza incompatibilidades de compilacao do transporte LG; nao comprova
HCI nem autoriza carregar o modulo. Nao ampliar teardown generico do WMT aqui.

| Alternativa | Origem/revisao/licenca | Compatibilidade e decisao |
| --- | --- | --- |
| Transporte LG STP BT | Snapshot LG local sem commit: stp_chrdev_bt.c SHA256 66f527af66a9dc9d5256ed99a3ca99adb5753fad3aaaeb75eeaa2dc398bc0d10; bt.h abd6734613dbc9a7b5eb92678c2a957ca7a1e58116fc940131fd300e6cf47665. Ambos cabecalhos GPLv2; MODULE_LICENSE declara Dual BSD/GPL, nao presumir licenca BSD para o arquivo | Reusar em copia isolada, headers WMT ja adaptados, kernel 6.18.58 commit 2926d88bb7fc4608fd942453d929c39e4e5ec006. Expõe /dev/stpbt com H4 e liga/desliga WMT no open/release; nao registra hci_dev. Compilar primeiro sem modificar sequencias de radio, sem headers Linux4.9 ou stubs. |
| Linux btmtk / hci_uart / hci_vhci | Mesmo commit Linux, GPL-2.0; fontes locais drivers/bluetooth | Framework HCI reutilizavel, mas btmtk USB/UART nao demonstra suporte ao STP/BTIF integrado6765. TTY H4 nao aceita automaticamente um char device STP; VHCI exige ponte e framing. Nenhuma ponte nova implementada nesta etapa. |
| postmarketOS / MediaTek / Qualcomm | Triagem de conectividade e referencias fixadas nas tabelas anteriores desta auditoria | Nenhuma equivalencia comprovada de transporte/firmware para substituir o LG6765. Nao importar outro driver somente pelo nome MediaTek, nem usar transporte Qualcomm como backend BTIF. |

Novo codigo limitado ao wrapper Kbuild MIT de compilacao, necessario para
selecionar o fonte LG e os headers WMT adaptados sem transportar a arvore4.9.
Primeiro build identificou wakeup_source_init/trash removidos, class_create
com assinatura antiga e helpers locais sem linkage static. Adaptacao escolhida:
APIs wakeup_source_register(NULL, name)/unregister do mesmo Linux GPL-2.0,
tratando ENOMEM antes da publicacao e liberando em falhas; class_create(name).
Manter evento de wakeup100ms. Declaracao send_hci_frame continua publica para
fw_log_bt, demais callbacks locais static. WMT_IDC_SUPPORT=0 reproduz a selecao
original para o kernel sem CONFIG_MTK_CONN_LTE_IDC_SUPPORT; nao e stub.
Probe/init cria cdev/wakeup; open pode energizar o radio; falhas e release
precisarao de verificacao direcionada antes de ensaio. Resultado de build abaixo
deve informar o primeiro erro real, nao converter compilacao em aceite fisico.

Resultado offline: patch `bt-legacy-linux618-api-v1.patch` e wrapper
`bt-legacy-linux618.Makefile` permitem gerar bt_drv.ko ARMv7 para
6.18.58-k40s-nativeusbemmc1-NOT-FOR-FLASH; depends=wmt_drv. Build com -Werror,
modpost com vmlinux.symvers e WMT/Module.symvers reais, sem
KBUILD_MODPOST_WARN: `work/bt-legacy-lts-api-20261028-a.log`. Permanecem avisos
de BUILD/Module.symvers ausente (exports fornecidos explicitamente) e
MODULE_DESCRIPTION ausente; nenhum simbolo externo foi substituido por stub.
SHA256 ko af2044d696a6f7ba2c18476910784d7415a063053e3d72866a44efec071f5893;
stp_chrdev_bt.c de0abe3d9db6e412f4c74fd9963aa986d0fc60e100c8120d167403e66c638d14;
bt.h 91f9967f49bf6f991a90dc89c693a0b332043756eb2e578a8bd14c44b3fbc6b8.

Verificacao proporcional: init/exit reais extraidos, doubles apenas das APIs
externas, ASan/UBSan; falhas de alocacao wakeup, reserva de major, cdev, class
e device, alem de sucesso/saida/reinit. Todos liberam o novo wakeup adquirido;
sem alterar errno legado dos demais caminhos. Log
`work/bt-legacy-lts-api-host-20261028-b.log` aprovado. Primeira execucao-a
falhou por indentacao do double, corrigida sem mudar driver. Nao valida
concorrencia dos callbacks, open/close do radio nem lifecycle WMT completo.

Proximo bloqueio funcional: ligar o fluxo H4 do char device ao HCI Linux.
O kernel atual tem CONFIG_BT=m, mas CONFIG_BT_HCIVHCI desativado. Fonte
[BlueZ btattach](https://github.com/bluez/bluez/blob/master/tools/btattach.c)
exige TTY/termios/line discipline; nao atende diretamente /dev/stpbt.
[BlueZ btproxy](https://github.com/bluez/bluez/blob/master/tools/btproxy.c)
ja faz framing H4 e VHCI, mas seus endpoints sao sockets/canal HCI, sem
opcao char STP direta. Licenca GPL-2.0-or-later; revisao master consultada
sem commit fixado: candidata, nao codigo incorporado. Comparar uma adaptacao
pequena desse caminho antes de escrever ponte propria. A sequencia LG de
firmware/endereco e o acesso exclusivo ao radio ainda precisam ser conferidos;
nao presumir que transportar H4 basta para parear. Nenhum modulo carregado,
radio ligado, firmware enviado ou telefone acessado nesta etapa.

### WMT lib: ownership persistente para deinit parcial — auditoria previa

Entrega visada: retirada de init parcial nao destroi mutex/evento nao criado,
nao apaga owner quando cleanup falha e permite retry dos restantes. Aceite
offline: flags de core/sync/plataforma/PS persistem no erro; deinit falha
antes de retirar dependencias posteriores, preserva errno e usa join/destroy
OSAL uma vez. Historicos/snapshots, ROM patch e tabela sao liberados antes
de memset. Config/firmware pertencem a lib; STEP pertence ao caller.

Reuso fontes LG wmt_lib.c/wmt_dev.c GPLv2-only, mesmo grafo de init/unwind
ja auditado, native kthread_stop_put/timer/work Linux6.18.58
2926d88bb7fc4608fd942453d929c39e4e5ec006. Reusar cleanup de history BTM/PSM
e release_firmware via wmt_dev_patch_put existente. Triagem mainline/
pmaports/MediaTek/Qualcomm anterior nao fornece outro lifecycle WMT privado;
nao criar backend/ledger generico. Promover flags locais para estado privado
persistente e limpar cada uma somente apos sucesso da respectiva retirada.
PlataformaEBUSY conserva marcador de owner alheio e impede cleanup destrutivo.

STEP_INIT e chamado em WMT_init, nao lib_init: seu DEINIT deve ficar no
caller, apos STP parar, sob flag propria. Lib completa distingue IDC de
init parcial; contrato IDC/exportados genericos ainda nao foi aprovado.
Esta etapa pressupoe produtores externos retirados; FDs/proc/APIs/STP podem
usar lib e ainda exigem sequencia global/admissao. Nao afirmar teardown
ativo total ou unload/FAULT seguro por validar memoria/flags offline.
Sem aparelho/carga/flash nem permissao fisica nova.

### WMT lib: desligar timers e bloquear requeue de work antes de joins

Entrega visada: callback timer/work nao usa contexto/sinais liberados nem
agenda novamente durante stop. Aceite offline: shutdown de dois timers e
disable/drain de tres works adquiridos antes de joins, com dependencias
vivas; repetir fase nao repete disable; init incompleto nao toca objeto
nao inicializado; retry limpo reinitializa apenas work ocioso. Sem aparelho.

Reuso Linux6.18.58 2926d88bb7fc4608fd942453d929c39e4e5ec006:
timer_shutdown_sync e disable_work_sync (kernel/workqueue.c, GPL-2.0-only),
nao criar gate/worker paralelo. disable_work_sync aguarda execucao atual e
incrementa disable count: queue_work falha enquanto desabilitado, evitando
janela cancel/requeue. Mesma familia native ja usada nos owners BTM/PSM,
mas agora com bloqueio de nova fila. Fonte wmt_lib.c LG GPLv2-only; triagem
mainline/pmaports/MediaTek/Qualcomm anterior nao fornece driver substituto
para WMT privado. Tres flags privadas indicam quais pares timer/work e
assert work foram inicializados. Nao e ledger universal ou backend novo.

Fase chamada depois de quiesce stub e antes de parar tarefas, pois work
pode esperar servico WMT. Caller nao pode chama-la de dentro do proprio work.
INIT_WORK no retry somente depois de disable/drain completo e ausencia de
owners; API kernel reinicializa data/disable count. Falhas que retêm owner
continuam bloqueadas para novo init. Demais produtores/FDs, ownership de
core/plataforma/exports e erros de deinit ainda sao gates separados.

Resultado: wmt-lib-async-stop-v1.patch adiciona helper privado que para
worker_timer/utc_sync_timer e disable_work_sync de wmtd_worker_thread_work,
utcSyncWorker e assert work. Flags sao publicadas depois de INIT_WORK e
retiradas somente depois do respectivo drain; fase repetida nao acumula
disable count. Aplicada em worker-create-failure, late-init-failure e
deinit antes de thread_stop, depois de quiesce da plataforma. Assert work
agora e drenado ANTES dos joins, enquanto seu consumidor pode atende-lo.
Nao adiciona accesso hardware nem altera periodo/funcao de sucesso.

Teste helper real + init real + corpos reais de dois timeout handlers
passou -Werror/ASan+UBSan. SRCU/worker scheduling/timer sao doubles:
sem owners nao toca primitivas; init completo seguido de fase conserva
threads rodando, locks/config/core/plataforma/historicos, mas dois timers
ficam dead e tres works disabled. Repeticao nao chama APIs novamente;
tentativas de queue via timeout handlers reais e assert sao recusadas.
Work UTC pausado mantem consumidores vivos enquanto disable aguarda; a
tentativa de auto-requeue tambem e recusada antes da fase terminar.
Fixture success dispose e manual, NAO teardown completo. Primeiro harness
acusou cookies de timer intencionalmente nao usados em -Wextra; anotou-se
somente parametro unused no C gerado, mantendo corpos reais e Werror.
Produto/verificacoes funcionais nao foram alterados para essa advertencia.
Log final work/wmt-async-stop-host-20261028-b.log; roundtrip fuzz=0 e hash
anterior5cb5b5b2727f86856472b493e9cfcd9e735c7c19f8a6ac8a5da63efb0b82e6bf conferido.

Regressoes dos init reais passaram, incluindo retry sem reset de owners
e flags da fixture, hist opcional e erro de quiesce que nao toca async:
work/wmt-async-stop-init-host-20261028-a.log. Contadores de cancel history
e disable principal agora sao distintos, preservando checks de ownership.
Caller init/exit-order e native-profile tambem passaram, com pins/roundtrips
anteriores preservados: work/wmt-async-stop-caller-host-20261028-a.log,
work/wmt-async-stop-quiesce-host-20261028-a.log e
work/wmt-async-stop-native-host-20261028-a.log.
Build ARM32/-Werror/modpost real passou sem relaxamento:
work/wmt-async-stop-build-20261028-a.log, exports kernel/BTIF reais via
KBUILD_EXTRA_SYMBOLS. disable_work_sync GPL export resolvido pelo kernel;
aviso de arquivo build/Module.symvers ausente permanece, sem MODPOST_WARN.
Fonte wmt_lib.c SHA256808a6fd2d9edcf85c6636a9b0aab3f596efe27f9d5ee0086c701ff689030d297;
wmt_drv.ko4c490cdd8e9774920d75afd5366b0dc519f58da236dcf89524651878772a7d8b;
Module.symvers230395d0d7450136aed7ab84d5a63f433feaa7ffbc2aad91c8e7eb28e4f066f3.
Sem aparelho/carga/flash. Helper cobre somente produtores principais
citados: history dump works ainda dependem de cleanup ativo proprio. Gate
seguinte: ownership persistente de core/sync/plataforma/PS/config/exports
para deinit parcial e parada no erro antes de free/memset; FDs/proc/APIs
ainda precisam admissao/drain. Nao e aceite de unload/FAULT nem funcional
no aparelho; restantes do lib_deinit nao foram exercitados por esse teste.

### WMT: quiesce de plataforma antes de parar consumidores — auditoria previa

Entrega visada: callback stub/bridge em andamento consegue terminar usando
workers e locks ainda vivos, sem drain esperando worker ja parado. Aceite
offline: fase quiesce retira apenas stub, conserva hardware/wakelock/locks,
idempotente; erro preserva owners e impede qualquer retirada posterior.
Caller exit fecha novos opens e chama fase antes dos locks WMT; lib deinit
e init-unwind chamam antes dos joins. Nao e aceite de todo teardown ativo.

Reuso LG wmt_plat_alps.c/wmt_dev.c/wmt_lib.c/wmt_plat.h GPLv2-only e
unregister SRCU ja integrado no stub/bridge, Linux6.18.58
2926d88bb7fc4608fd942453d929c39e4e5ec006. Mainline/pmaports/MediaTek/
Qualcomm nao oferecem substituto para esse grafo privado; triagem anterior
mantida. Pequena divisao do deinit existente, sem nova fila/driver/backend
ou mecanismo de sync. Mesmas flags privadas rastreiam stub adquirido.
Init/deinit/quiesce serializados pelo caller; proibido quiesce dentro do
proprio callback. Sem carga/flash/acesso ao aparelho.

Complementa, nao substitui retirada dos produtores fora desse stub: FDs,
proc, APIs exportadas e timers/work WMT ainda precisam admissao/ownership.
WMT_exit void em FAULT continua gate; se quiesce falhar, reter estado e
recursos (nao fingir sucesso). Outros erros de deinit preexistentes ainda
nao sao corrigidos neste delta. Init-unwind preserva errno causal quando
quiesce falha e deixa guard ocupado, sem perder tarefas ou dependencias.

Resultado: wmt-platform-quiesce-before-stop-v1.patch extrai somente retirada
do stub para wmt_plat_quiesce; repete sem efeitos, deixa hardware/wake/mutex
e flags de owner vivos. Deinit delega a fase e para no erro. Init-unwind lib
chama quiesce da plataforma tentada antes de timers/joins e conserva errno
causal se falhar. Lib deinit chama antes de thread_stop. WMT_exit fecha
novos opens com START, drena antes de panel stop/locks/transportes/lib;
falha vira FAULT com recursos preservados. Sucesso final acorda open que
aguardava e retorna a NOT_START, sem tornar outros erros de teardown seguros.

Testes reais plataforma quiesce/init/deinit passaram com mocks de hardware:
quiesce preserva dependencias, repeticao nao repete unreg e callback pausado
conclui antes de free. Logs work/wmt-quiesce-platform-host-20261028-a.log.
Init lib real agora exige quiesce nos doubles antes de qualquer destroy
quando plataforma esta viva; falha de quiesce apos segundo run falho
preserva ambas tarefas, main rodando, timers/work nao retirados, contexto e
errno original. Regressoes init inicial/tardio passaram:
work/wmt-quiesce-lib-host-20261028-a.log.

test_wmt_quiesce_order.py compila WMT_init/exit/open reais com getter/STP
exit reais, usando library-stop/quiesce/recursos doubles. Callback pausado
exige lib e tres locks vivos; exit aguarda em START sem parar panel/lib nem
liberar locks/cdev/region. Novos opens recusados nesse estado no wait double;
lib so pode ser retirada depois de callback concluir. QuiesceEIO/positivo
preserva tudo em FAULT, sem sucesso falso. Library deinit inteiro NAO e
executado; teste comportamental do caller e check de ordem no corpo real
de lib complementam build, nao provam restante do teardown. Primeiro harness
falhou ao extrair helper fixture one-line com extrator multiline; corrigido
para substituicao exata da fixture, sem alterar codigo ou assercoes do
produto. Passou ASan+UBSan/-Werror:
work/wmt-quiesce-caller-exit-host-20261028-b.log.
Roundtrip quatro arquivos fuzz=0 passou, assim como regressoes caller init,
native profile e roundtrip do transporte SDIO:
work/wmt-quiesce-caller-init-host-20261028-a.log,
work/wmt-quiesce-native-host-20261028-a.log e
work/wmt-quiesce-sdio-regression-20261028-a.log.

Build inicial compilou ARM32 mas falhou modpost nos exports BTIF:
work/wmt-quiesce-build-20261028-a.log. Arquivo BTIF atual tem13 exports reais,
sem build concorrente observado; repeticao V=1 confirmou dois -i reais de
kernel e BTIF e passou modpost/link, sem MODPOST_WARN:
work/wmt-quiesce-build-20261028-b.log. Causa da primeira falha NAO confirmada;
nao atribuir a fonte nem a uma correcao ficticia. Aviso build/Module.symvers
ausente permanece. BTIF symvers atual SHA256
516b10f53e2e18d7caeeddbec72e0d43a9259d32cec6bf9f6ac95e8dbb01ac14;
wmt_drv.koecac1d49de6d1665a9c5fc5f39b82e7ab5462c031b65887c5cda1e83c4608606;
WMTsymvers230395d0d7450136aed7ab84d5a63f433feaa7ffbc2aad91c8e7eb28e4f066f3.
Fontes: plat58ca0fa72a8a7ef119f918b944540e045d7a2ffbf144f96de70871c970511047;
header9592a0bf94a89e3a766309e13a2d78bf5f8379742711efbf584e1eae56c43181;
lib5cb5b5b2727f86856472b493e9cfcd9e735c7c19f8a6ac8a5da63efb0b82e6bf;
devba252d2613e932cab043bdc89ad80c055eac8ad04a7c789e23f776703dedaa78.
Sem carga/flash/aparelho. Proximos gates: shutdown de timers/work lib antes
de frees, ownership persistente para deinit partial/FAULT, retorno de
outros erros no caller e admissao/drain de FDs/proc/APIs restantes. Nao usar
esse sucesso offline como aprovacao de module_exit ou funcionamento fisico.

### Stub MediaTek: retirar callbacks diretos com SRCU — auditoria previa

Entrega visada: unregister da plataforma aguarda chamadas diretas do stub
que ja entraram e impede novas, incluindo trigger_assert esquecido no
cleanup anterior. Aceite offline: tabela completa e imutavel publicada no
sucesso, alloc/param/busy sem sobrescrever owner; unregister fecha publicacao,
retira bridge, synchronize_srcu e so entao libera tabela/dependencias.
Sucesso, argumentos e retornos ausentes das sete rotas preservados.

Reuso Linux6.18.58 2926d88bb7fc4608fd942453d929c39e4e5ec006:
DEFINE_STATIC_SRCU/srcu_read_lock/srcu_dereference/synchronize_srcu,
kmemdup/kfree e mutex, mesmo padrao do bridge WMT ja adaptado. Fontes LG
mtk_wcn_stub_alps.c GPLv2-only; triagem mainline/pmaports/MediaTek/Qualcomm
anterior nao substitui estas assinaturas privadas. Sem novo backend,
framework ou thread. Uma copia da struct existente substitui sete pointers
independentes, evitando publicacao parcial e nova API de callbacks.

SRCU preserva callbacks que dormem; mutex e apenas de register/unregister,
nao fica preso durante callbacks. Unregister nao pode ser chamado de dentro
do proprio callback (mesma restricao do bridge ja existente). As rotas
atuais plataforma/audio/func/thermal/assert/deepidle/reset/clock nao chamam
registro/unregister do stub; callbacks que o fizerem serao incompatíveis.
O caller de hardware deve retirar os outros produtores/operacoes por conta
propria; drenagem destas rotas nao prova teardown completo WMT/BTIF. Sem
carga/flash/aparelho. Novo ENOMEM antes da publicacao e EBUSY em registro
duplicado devem ser propagados pela plataforma, como corrigido antes.

Resultado: wmt-stub-callback-srcu-v1.patch publica copia kmemdup da struct
existente sob mutex de lifecycle. Parametro invalido continua-1; novo
ENOMEM nao publica nada; duplicado EBUSY nao troca owner. Sete rotas leem
tabela imutavel dentro de SRCU ate retorno (aif/func/thermal/assert/clock/
BTIF-deepidle/reset). Argumentos/retornos e ausencia preservados, inclusive
UART/MSDC deepidle no-op legado. Aif stat usa READ/WRITE_ONCE. Unregister
fecha ponteiro, retira bridge e sincroniza leitores raw antes de kfree;
assert deixa de ficar pendurado, pois tabela inteira sai. Sem owner e
idempotente. Common_detect/wmt_platform_bridge.c atual foi conferido:
bridge_unregister tambem fecha active_bridge e synchronize_srcu antes de
retornar; ordem aninhada nao libera tabela enquanto bridge/raw a usa.

Teste funcoes reais registry e sete dispatchers passou -Werror/ASan+UBSan:
work/wmt-stub-srcu-host-20261028-a.log. Doubles SRCU com readers/condicao,
memory e bridge; verifica OOM, null/size, copia independente da stack,
busy sem nova alloc, dois registros concorrentes com um owner, callbacks
ausentes/argumentos/retornos e sete leitores pausados (um por rota). Em
cada caso unregister fecha publicacao mas nao libera tabela/dependencias
ate reader sair; chamadas novas retornam defaults sem executar callback.
Registro de tabela vazia valido, unregister repetido e retry verificados.
Dois modos de registro bridge/remove-kernel-module no harness, NAO build
completo builtin/ABI do wrapper publico; corpos dispatch equivalentes sao
extraidos do arquivo atual. SRCU/kernel callbacks reais nao executados.
Roundtrip fuzz=0 confirma hash anterior37fd5c0c4802db51a1dec7945eff4793c87e5acc4d4a4adb280f870db5018be9.
Regressao native-profile com pin atualizado passou sem mudar assercoes:
work/wmt-stub-srcu-native-regression-20261028-a.log.

Build ARM32/-Werror/modpost reais final passou:
work/wmt-stub-srcu-build-20261028-b.log (rebuild apos READ_ONCE no log).
Exports kernel/BTIF reais via KBUILD_EXTRA_SYMBOLS, sem MODPOST_WARN;
aviso build/Module.symvers ausente permanece. Fonte stub SHA256
fc996f79d7fe69a6a382b384ba57de63c1e1a22938a72979c7ee7958afd2ff2b;
wmt_drv.kodb01df29924a58c499127a3c463b060aa8e90ff5bd05b7e7641c4a7bb227650a;
Module.symvers230395d0d7450136aed7ab84d5a63f433feaa7ffbc2aad91c8e7eb28e4f066f3.
Sem aparelho/carga/flash. Isto fecha o contrato dessas rotas, NAO a ordem
global de stop WMT. Gate concreto seguinte: quiesce do stub/bridge deve
ocorrer ENQUANTO workers WMT ainda podem atender callback em andamento,
antes de joins; deinit ativo atual para workers antes da plataforma e pode
travar o drain. FDs/proc/APIs restantes ainda requerem admissao/drenagem,
e FAULT/module_exit/BTIF DMA continuam sem aceite de ensaio ou unload.

### Transporte inicial: perfil BTIF e erros genéricos — auditoria previa

Entrega visada no K40s: WMT BTIF nao depender de registro ldisc UART ou
driver/cliente SDIO externos que o perfil ja recusa. Aceite offline:
native nao chama init/exit HIF-SDIO/UART/STP-SDIO; generic continua chamando
os transportes e so publica DONE se ambos retornarem0. Erro SDIO client_reg
nao e sobrescrito por op_reg. Sem carga/flash ou alegacao de Wi-Fi/BT fisico.

Reuso do perfil WMT_K40S_NATIVE_PROFILE ja auditado (SoC6765/BTIF, root DT
lge,mmh55lm-memory-draft, MSDC0 eMMC/1 SD/2-3 desabilitados). Arquivos LG
wmt_dev.c/stp_sdio.c GPLv2-only e APIs existentes, Linux6.18.58
2926d88bb7fc4608fd942453d929c39e4e5ec006. Mainline/pmaports/MediaTek/
Qualcomm triagem anterior: nao substituir STP por driver novo. Nenhum novo
backend, loop, ferramenta ou caminho hardware; condicionar registros pela
politica de placa existente, preservando corpos genericos.

Generic UART_init tem rollback de FIFO/work/ldisc no erro. SDIO client_reg
pode adquirir parte da tabela e agendar probe antes de falhar: nao e atomic.
Portanto no erro SDIO nao publicar novos callbacks nem liberar host que
um probe ja possa usar; retornar errno e conservar owner existente no
FAULT do caller lib-owned. Isso nao implementa rollback parcial HIF/SDIO
ou unload em FAULT. op_reg atualmente retorna0, mas seu erro tambem deve
interromper publicacao. Registrar transportes antes dos setups proc/debug
evita publicar essas entradas quando a etapa de transporte falha.
Exit chama apenas transportes que esse perfil/modo de ownership inicializa;
MTK_WCN_REMOVE_KO mantem os registros sob caller externo. Nao aprovar
teardown ativo/raw/exportado por essa alteracao de selecao.

Resultado: wmt-transport-profile-errors-v1.patch exclui registros HIF SDIO,
UART ldisc e STP SDIO do init K40s BTIF e respectivas retiradas em exit.
Generic continua usando mesmos drivers; MTK_WCN_REMOVE_KO nao retira
registros do caller externo. No generic, UART/SDIO init antecedem setups
proc/debug; erros retornam antes de DONE, passam a FAULT com lib/STP/HIF
retidos e nao chamam deinit completo parcial. Nao tenta desmontar cliente
SDIO parcialmente registrado por esse caminho.

stp_sdio_init retorna erro client_reg imediatamente, sem sobrescrever por
op_reg nem publicar outros callbacks/debug. Tambem para no erro op_reg.
Host preservado porque HIF client_reg nao e atomic: pode adicionar algumas
entradas/agendar probes antes de falhar. A correcao NAO torna init/exit
diretos/exportados SDIO seguros para retry/teardown apos erro; caller WMT
FAULT e gate, nao mecanismo completo de recuperacao. Nenhum protocolo ou
corpo de transporte substituido, nenhuma protecao/checagem relaxada.

Teste caller real atualizado passou native/generic e variantes anteriores
de ownership/node: native com falhas injetadas nas APIs externas nao as
chama e completa pelo caminho BTIF; generic retorna erro, retém owners e
nao publica proc/READY. Continua verificando todos os erros anteriores,
retry/cdev refs/init concorrente. Log work/wmt-transport-caller-host-20261028-a.log.
test_wmt_sdio_init_errors.py compila init SDIO real anterior/atual, reproduz
erro client EIO sobrescrito antes, e verifica EIO/EPROBE_DEFER/positivo com
client inexistente/parcial, host retido e ausencia de callbacks posteriores;
erro op_reg tambem para publicacao, sucesso conserva callbacks/debug.
ASan+UBSan/-Werror e roundtrip dos dois arquivos fuzz=0 passaram:
work/wmt-transport-sdio-host-20261028-a.log. Registro/probe/work sao doubles,
nao prova de MMC/IRQ/kernel lifetimes reais. Fixture nao executa cleanup
de partial HIF e nao o afirma validado.

Build ARM32/-Werror/modpost reais passou:
work/wmt-transport-profile-build-20261028-a.log. Exports kernel/BTIF reais
via KBUILD_EXTRA_SYMBOLS, sem MODPOST_WARN; aviso de arquivo
build/Module.symvers ausente permanece. nm do wmt_dev.o desse build nao
tem referencias a nenhum dos seis init/exit HIF-SDIO/UART/STP-SDIO:
work/wmt-transport-native-symbols-20261028-a.log. Isso confirma selecao
compilada no caller nativo, nao ausencia dessas APIs exportadas no modulo.
wmt_drv.ko SHA2562aa745a503718ba5a2d92ddd2439eca0100660d25bc532763e733c7fae1d00da;
Module.symvers230395d0d7450136aed7ab84d5a63f433feaa7ffbc2aad91c8e7eb28e4f066f3.
Fonte dev61cb419727508da4a2b1e145f0d929f61aa26aa4849689a23310242f8ea8bbae;
sdio2ef7482c2e140b59444a131d25a4f3f3e15030bac3f6cd0dab044f669b741b95.
Sem aparelho/carga/flash. Proximo gate do K40s: teardown WMT active/partial
e admissao/drenagem de consumidores externos/FD/proc/raw, com unload em
FAULT ainda inseguro. Generic SDIO partial-registration rollback permanece
separado e nao e dependencia funcional do aparelho BTIF atual.

### WMT caller init: erro, ownership e retry — auditoria previa

Entrega visada: WMT_init nao publica sucesso apos erro HIF/STP/lib, nem
chama deinit completo de biblioteca parcial/ja retirada. Aceite offline:
errno exato, cleanup reverso de cdev/device/class/region adquiridos, lib
responsavel pelo proprio rollback; se lib conservar owner, reter STP/HIF
e estado FAULT sem aceitar init novamente. STP exit propaga erro; init STP
falho totalmente limpo (deinitEINVAL sem owners) e distinguido de falha de
retirada. Nao constitui teardown ativo nem autorizacao de carga.

Reuso Linux6.18.58 2926d88bb7fc4608fd942453d929c39e4e5ec006: cdev_alloc,
cdev_add/cdev_del, kobject_put e DECLARE_WAIT_QUEUE_HEAD (fs/char_dev.c,
SPDX GPL-2.0) em vez de lifetime/refcount paralelo. cdev dinamico conserva
referencias de open concorrente apos del sem reinit do objeto anterior;
fila de espera tem vida do modulo, nao e reinicializada sob open aguardando.
fops.owner fixa ref de modulo durante FD. Mutex existente kernel serializa
chamadas lifecycle init/exit, nao callbacks. Fontes WMT LG GPLv2-only;
novo getter lib-owned interno apenas comunica ownership real para caller,
nao consulta hardware. Triagem mainline/pmaports/MediaTek/Qualcomm anterior
mantida: adaptar caller vendor e APIs nativas, sem novo driver/framework.

WMT_open ja espera INIT_DONE antes de tocar lib; init falho nao abre FD
operacional. Isso nao drena FDs de uma execucao bem-sucedida nem callbacks
exportados/raw/proc: esses caminhos continuam gates. API final UART/SDIO e
setups void apos lib ainda precisam auditoria propria; nao prometer aceite
completo de init por este delta. Falha de rollback em FAULT nao autoriza
module_exit void a liberar codigo com workers vivos; unload permanece gate.

Resultado: wmt-caller-init-ownership-v1.patch faz WMT_init observar erros
HIF/STP/region/cdev_alloc/cdev_add/class/device/lib e retornar errno causal.
Lib gerencia seu rollback: caller NUNCA chama lib_deinit no error init.
Getter interno wmt_lib_is_owned informa guard real, nao heuristica sobre
tarefas. Se lib reteve owners, preserva STP/HIF e FAULT; init retornaEBUSY
nessa condicao, nao falso0. STP exit propaga deinit; failed-init sem owners
(EINVAL) pode concluir rollback, mas EINVAL apos STP ter iniciado e erro
de retirada. STPEBUSY nao retira owner alheio. Cleanup so de aquisicoes
reais, reverso device/class/cdev/region, antes de STP/HIF; major preservado.
No perfil atual DELETE_HIF_SDIO_CHRDEV=1: erro HIF e sdio_register_driver,
sem thread auxiliar adquirida. Variante com esse macro0 nao foi aprovada.

DEFINE_MUTEX serializa init/exit; initDONE idempotente, outros estados
ocupados nao refazem setup. DECLARE_WAIT_QUEUE_HEAD tem vida do modulo;
open espera sair de START e aceita apenas DONE, sem tocar lib em erro.
cdev_alloc por tentativa e fops.owner corrigem lifetime/ref do objeto e
modulo; add falho usa kobject_put, publicado usa cdev_del. Referencia antiga
nao e reinicializada no retry. Exit usa ponteiro dinamico e mesmo mutex,
sem transformar o teardown ativo preexistente em caminho validado. DONE
passa a ser publicado depois das tentativas finais UART/SDIO e antes de
panel work, mas retornos desses dois init continuam pendentes de auditoria.

test_wmt_caller_init.py compila init/open/close reais, fops real, getter
real e stp_drv_exit real, com doubles de recursos e pthread mutex. Falhas
EIO/EPROBE_DEFER, cdevENOMEM, cada aquisicao e lib sem/ com owner residual
verificam errno, ausencia de deinit indevido, frees seletivos e retry.
STP parcial limpo/retido, STPEBUSY, EINVAL apos sucesso e FAULT sao distintos.
Modelo de ref cdev atrasada conserva objeto antigo ate put e cria outro no
retry; isso nao executa kobject/cdev kernel reais. Duas chamadas init reais
concorrentes com primeira pausada no HIF nao duplicam setup. Open em estados
naoDONE nao incrementa ref; DONE/close preservam contagem. Waitqueue nativa
nao executada no modelo; fonte compilada/assercoes preservam fila estatica.
Host func variants remove0/dynamic1, remove0/dynamic0 e remove1/dynamic1
passaram; nao sao tres builds de modulo. ASan+UBSan/-Werror e roundtrip dos
cinco arquivos fuzz=0 passaram: work/wmt-caller-init-host-20261028-a.log.
Fixture descarta success/quarantine manualmente, nao valida active exit.

Regressoes dos init lib e native-profile passaram com pins atualizados e
roundtrip de patches anteriores conservado:
work/wmt-caller-lib-regression-20261028-a.log e
work/wmt-caller-native-regression-20261028-a.log.
Build ARM32/-Werror/modpost reais passou:
work/wmt-caller-init-build-20261028-a.log; exports reais kernel/BTIF via
KBUILD_EXTRA_SYMBOLS, sem MODPOST_WARN. Aviso de build/Module.symvers ausente
permanece. wmt_drv.ko SHA256
6b61b5156689b0ded417b3cb606b0a87c2e2bdf1dd419cbc6d5130f0224359a0;
Module.symvers230395d0d7450136aed7ab84d5a63f433feaa7ffbc2aad91c8e7eb28e4f066f3.
Fontes apos delta:
wmt_dev.c08ec032a9a40dd4649dd2f642ae6af8652222f24b04fb3e24ae803e9b8ad4280;
wmt_lib.c1b93bb65d5c8026f49638d2f17d603d348b6f8a89718249b530dbd335ab30917;
stp_exp.c8d934a9b0687a64553b42a235f7ca5f7867cc8336a45813f517f80d0586cb88f;
wmt_lib.h77e8b1c52b7492d979cebc169b5b7a8ccac56db49f497f82e56639639e4629fe;
stp_core.hcdd009e262c2a2a4fa24e97eee6608f6a44deac51ac3cd5f937ba2041956bbf5.
Sem aparelho/carga/flash. Proximos gates concretos: erros finais UART/SDIO,
teardown WMT ativo/partial por ownership, admissao e drenagem de FDs/proc/
callbacks exportados/raw, inclusive module_exit void em FAULT. fops.owner
so protege referencias abertas, NAO substitui pin de owners assinc ou
cleanup; FAULT nao permite unload seguro ao fechar ultimo FD. Nao ensaiar
este modulo ate esses mecanismos de recuperacao estarem fechados.

### WMT lib: unwind core/plataforma/PS/run — auditoria previa

Entrega visada: erro apos criacao das tarefas nao deixa WMT sem caminho de
rollback, nem reporta sucesso ou perde owners. Aceite offline: erros originais
core/plataforma/PS/run retornam sem conversao; timers sao shutdown e works
drenados, tarefas joined com dependencias vivas, depois PS/plataforma/core
e sincronizacao adquirida, depois historicos/config. Falha de cleanup para
a cadeia e conserva os owners restantes/guard ocupado. Esta e recuperacao
de init sem produtores externos admitidos, NAO teardown ativo/publico.

Reuso LG/MediaTek wmt_lib.c GPLv2-only e labels ja integrados na etapa
anterior. core_init/core_deinit reais apenas inicializam/zeram contexto;
PS init/deinit atuais retornam0 sem recursos. Plataforma agora tem rollback
por ownership e deinit idempotente (patch anterior). APIs OSAL/kthread/timer/
work do Linux6.18.58 2926d88bb7fc4608fd942453d929c39e4e5ec006 ja auditadas.
Triagem mainline/pmaports/MediaTek/Qualcomm anterior nao fornece substituto
do fluxo privado WMT; sem novo driver/fila/framework. Novidade minima:
flags locais de aquisicao e label de unwind, nao novo backend SoC/PMIC.

As duas threads consultam should_stop antes de retirar proxima operacao;
filas estao vazias durante init sem produtores. Worker/UTC works so sao
agendados por seus timers; assert work tambem pode vir de caller externo,
que deve estar retirado. Inicializa-lo antes de rodar tarefas, nao depois,
permite drenagem em erro. Nao usar esse rollback como prova para stop de
atividade/hardware ja solicitado por cdev/API. PlataformaEBUSY indica owner
alheio/incerto: nao desmonta tal owner nem suas dependencias, mantem guard.

Resultado: wmt-lib-late-init-unwind-v1.patch preserva errno original em
core/plataforma/PS/run. Flags locais distinguem core/sync/PS adquiridos e
plataforma tentada (incluindo init cujo rollback interno falhou). Excecao
EBUSY conserva tudo e nao retira owner alheio/incerto. Assert work passa a
ser inicializado antes das tarefas rodarem. Erros tardios desligam ambos
timers, cancelam seus works, juntam worker e main mantendo dependencias,
cancelam assert work, retiram PS/plataforma/core adquiridos e depois sinais,
eventos e mutexes. Reusam labels anteriores para historicos/config. Qualquer
erro de cleanup interrompe cadeia, conserva recursos posteriores e guard;
nao substitui errno causal por erro de rollback. Nao e cleanup ativo e nao
habilita unload, retry de quarantine ou acesso fisico.

Teste init real inteiro com doubles passou com PS0/1, ASan+UBSan/-Werror.
Falhas EIO/EPROBE_DEFER numerico517/positivo nos cinco estagios comprovam
cleanup por aquisicao e retry real: so contadores/failpoints da fixture
sao resetados, nenhum owner/lock/timer/work/flag. INIT_WORK global pode ser
reinicializado apenas se cancelado e ocioso nesse retry. Falhas de join em
cada tarefa, PS, plataforma e core conservam dependencias/sincronizacao,
historico/config e EBUSY sem sobrescrita. Plataforma partial cleanup e
plataformaEBUSY diferenciadas; COMBO e historico opcional sem falsos frees.
Checks dos doubles verificam dependencias ainda vivas no join e ausencia de
threads antes do free. Nao exercita kernel threads/callbacks reais nem
operacoes externas/hardware concorrentes. Roundtrip fuzz=0 e hash anterior
04d4bfe96c6789bcc3fb38db4bba0106da32f48745071257741cd2503872e634 conferido.
Logs work/wmt-lib-late-init-host-20261028-a.log e
work/wmt-lib-late-init-regression-20261028-b.log (inclui init inicial).
Regressao native-profile passou com pin atualizado, sem mudar assercoes:
work/wmt-lib-late-init-native-regression-20261028-a.log.

Build ARM32/-Werror/modpost reais passou:
work/wmt-lib-late-init-build-20261028-a.log, exports kernel/BTIF reais via
KBUILD_EXTRA_SYMBOLS; sem MODPOST_WARN. Aviso build/Module.symvers ausente
permanece. Fonte wmt_lib.c SHA256
9cdbf79c4f7f0226e823f5247e0c79f595da0abcf015dca0fb9342cf03b91f3c;
wmt_drv.ko0bd2e65256365be4c4f73608045372ee6f0d72e42ec2d3f643e2e9a365c88663;
Module.symvers230395d0d7450136aed7ab84d5a63f433feaa7ffbc2aad91c8e7eb28e4f066f3.
Sem aparelho/carga/flash. Gate imediato: WMT_init error ainda chama
wmt_lib_deinit incondicionalmente, mesmo apos rollback ou em quarantine;
isso nao e valido. Caller deve distinguir ownership/retirar entradas e
nao chamar deinit completo em estado parcial. Cdev e APIs sem admissao
antes de initDONE tambem impedem assumir a pre-condicao de ausencia de
produtores em ensaio. Nao ensaiar este modulo antes de fechar esses gates.

### Plataforma WMT: erro real e ownership antes do rollback lib — auditoria previa

Entrega visada: inicializacao WMT nao aparentar sucesso quando registro
do driver CONNSYS/bridge falha, nem desmontar owners nao adquiridos.
Aceite offline: errno exato, init ocupado nao altera owner, dependencias
prontas antes de publicar stub, rollback reverso, deinit para no erro e
retry nao repete retirada ja concluida. Sem carga/flash/acesso ao aparelho.

Reuso LG/MediaTek wmt_plat_alps.c GPLv2-only, APIs existentes de hardware,
stub e wakelock OSAL; Linux6.18.58 2926d88bb7fc4608fd942453d929c39e4e5ec006.
hw_init SoC e platform_driver_register; erro nao adquiriu driver. COMBO
hw_init so configura tempos e retorna0; nao e protocolo Qualcomm. hw_deinit
SoC/COMBO e stub_unreg hoje retornam0, mas caller deve preservar erros.
Bridge exportado ja usa SRCU na adaptacao anterior; unregister drena seus
leitores antes de liberar dependencias. Stub raw/direct nao esta drenado
por essa API: permanece gate de admissao externa. Triagem mainline/pmaports/
MediaTek/Qualcomm anterior nao substitui callbacks privados da plataforma;
nao ha novo driver/framework. Nova cola minima: ownership local de tres
estados e labels usando init/deinit existentes. Init/deinit serializados
pelo caller, nao prometem lifecycle concorrente.

Problema observado: init soma erro stub+hardware e retorna0; deinit tambem
retorna0. Stub e publicado antes de locks/wakelock/hardware estarem prontos.
Adaptar ordem para locks -> hw -> stub; deinit reverso stub -> hw -> locks.
Registro de driver nao significa probe/bind bem-sucedido: esse aceite nao
prova hardware pronto nem funcionalidade CONNSYS. Erro de rollback preserva
owner remanescente, sem limpar flag ou sobrescrever em nova inicializacao.

Resultado: wmt-platform-owner-errors-v1.patch remove soma de errno e
retornos0 incondicionais. Init guarda backend uma vez, rejeita owner ocupado,
prepara wakelock/mutex/spinlock, inicializa backend e so entao publica stub.
Falha de wakelock propaga ENOMEM real da OSAL; hardware/register conservam
errno. Rollback usa deinit por flags adquiridas, preservando erro original
e owner caso cleanup falhe. Deinit idempotente sem owner; com owner, retira
stub antes do hardware e locais, para no primeiro erro e limpa cada flag
so no sucesso. Nova chamada continua do recurso remanescente. Chip detector
alterado depois do init nao troca backend do deinit. CFG_WAKELOCK usa #if
consistente com declaracoes, nao #ifdef sobre macro0. Nao altera backend,
limites eletricos, fontes LG originais nem acesso ao aparelho.

test_wmt_platform_owner.py compila funcoes reais init/deinit atual e init
anterior; reproduz sucesso falso anterior apos falha de hardware. Doubles
de wake/hw/stub verificam dependencias ja prontas na propria publicacao;
testa ENOMEM/EIO/EAGAIN/positivo em cada aquisicao/retirada para SoC/COMBO,
rollback incompleto com errno original, retry sem retirar duas vezes e
initEBUSY sem novos efeitos. Callback recebido pausado mantem hardware e
locais vivos enquanto unregister espera; depois join/deinit concluem.
Modelo apenas do contrato de drain do bridge, nao SRCU real nem retirada
de callers raw. Wake0/1 compilados so para essas funcoes, NAO build completo
da variante0. Co-clock detectado/explicitado/fallback e backend fixado
foram preservados. Roundtrip patch e reverse dry-run na workspace passaram
fuzz=0. ASan+UBSan/-Werror passaram:
work/wmt-platform-owner-host-20261028-a.log.

Build ARM32/-Werror/modpost reais passou em
work/wmt-platform-owner-build-20261028-a.log. Exports reais kernel/BTIF via
KBUILD_EXTRA_SYMBOLS, sem MODPOST_WARN; mesmo aviso de arquivo
build/Module.symvers ausente. Fonte wmt_plat_alps.c SHA256
63e28b0eb3dbb28d072733d0f1bcb5ed282058931e2a8b1e9b16ebc159546b93;
wmt_drv.ko01ea09ab1a528a98244d3a4007fa79aebc9b159ec8f7780472ebc3667b3c1963;
Module.symvers230395d0d7450136aed7ab84d5a63f433feaa7ffbc2aad91c8e7eb28e4f066f3.
Registro do driver pode retornar0 com probe falho/deferido: nao e prova de
probe, bind ou funcionalidade fisica. WMT lib agora pode observar erro real
de plataforma, mas ainda precisa unwind dos estagios posteriores antes de
permitir retry. Callers WMT e admissao/retirada raw permanecem gates.
Em particular stub_unreg existente nao limpa trigger_assert_cb e nao drena
os callbacks raw: nao interpretar deinit plataforma como unload seguro.

### WMT lib: falhas antes do core/plataforma — auditoria previa

Entrega visada no aparelho: inicializacao WMT falha sem perder tarefas ou
historicos e pode ser tentada novamente quando o rollback foi completo.
Aceite offline desta etapa: errno de config/create preservado; falhas nas
duas criacoes retiram somente recursos adquiridos; timer/work de worker
desarmados antes do join; fila/history/config preservadas ate worker parar;
sem memset sobre owner existente. Timers/work/locks posteriores e rollback
de core/plataforma ficam em etapa propria, nao cobertos por este aceite.

Reuso LG MediaTek wmt_lib.c/wmt_conf.c GPLv2-only, OSAL ja adaptado a
kthread_stop_put e timer_shutdown_sync/cancel_work_sync Linux6.18.58
2926d88bb7fc4608fd942453d929c39e4e5ec006. Reaproveitar labels de erro e
cleanup de historico usado no BTM/PSM do proprio port, sem novo alocador,
thread ou framework. Mainline/pmaports/Qualcomm nao substituem esse fluxo
privado LG, conforme triagem vinculada anterior. Codigo novo minimo e
especifico do ownership WMT: guard privado e labels locais; historico e
opcional. Init/deinit permanecem serializados pelo caller, sem promessa de
concorrencia entre chamadas de lifecycle. Sem I/O SoC/PMIC/placa novo.
Config cleanup failure ou join failure mantem owner ocupado; nao permite
retry destrutivo. Erros posteriores continuam ocupados, nao fingem rollback.
Esse trabalho nao corrige WMT_init ignorando STP/HIF nem autoriza carga.

Resultado: wmt-lib-early-init-unwind-v1.patch conserva errno de config e
das duas criacoes. Primeira falha limpa historicos opcionais/config; segunda
desliga timer do worker, cancela work inicializado e faz join da primeira
tarefa ANTES de liberar historicos/config. Falha de join/config cleanup ou
firmware residual conserva guard ocupado; nenhum memset em retry. Owner
existente por flag/tarefa/historico retorna EBUSY sem alterar bytes. Guard
limpo apenas em rollback completo ou deinit com resultado0; nao e mutex de
lifecycle. Erros posteriores a criacao permanecem ocupados, sem rollback
fingido. Fonte original LG nao foi alterada.

Timer UTC deixa de ser armado antes de INIT_WORK/core/locks; agora e armado
somente apos ambos workers, callbacks e work assert estarem prontos. Nenhum
novo timer/read/retry hardware; mesmo periodo no sucesso. Falhas posteriores
nao deixam esse timer como produtor adicional. Os outros recursos dessas
falhas ainda requerem unwind proprio. wmt_conf_parse foi inspecionado:
seu retorno de erro ocorre antes de parse/alocacoes de campos; read_file
libera firmware obtido via patch_put. Guard de pWmtCfg residual impede
perder owner se esse contrato nao se cumprir. cfgExist0 nao chama deinit,
pois wmt_conf_get_cfg retornaNULL nesse estado.

test_wmt_lib_early_init.py compila init inteiro atual e anterior com
dependencias doubles e -Werror/ASan+UBSan. Reproduz leak anterior na primeira
falha. ConfigENOENT sem owner permite retry; falhas ENOMEM/EAGAIN/EIO nas
duas criacoes, quatro combinacoes de historico opcional, SoC/COMBO, PS0/1
fazem rollback e sucesso posterior. Confirma que join ocorre com config e
historicos vivos e antes de qualquer free. Falhas de join/config cleanup
preservam owners restantes e EBUSY; firmware residual tambem bloqueia retry.
Owners residuais nos quatro campos e init repetido preservam bytes.
Falhas core/plataforma/PS/run nao armam UTC e bloqueiam sobrescrita, mas
NAO provam limpeza ou recuperacao desses casos. Sucesso conserva callbacks,
duas threads e um arm UTC apos consumidores prontos. Dispose de sucesso do
harness e manual, NAO teste de deinit ativo. Roundtrip patch fuzz=0 passou.
Log work/wmt-lib-early-init-host-20261028-a.log. Nao ha kernel threads reais.
Regressao diretamente afetada test_wmt_native_profile.py inicialmente acusou
o hash antigo de wmt_lib.c; repin da fonte foi necessario, sem alterar
assercoes ou bodies de admissao/PM. A mesma regressao passou depois:
work/wmt-lib-early-init-native-regression-20261028-a.log. HIF BTIF/chip6765,
recusas nativas e bodies COMBO continuam verificados; nao e ensaio hardware.

Build ARM32/-Werror/modpost reais passou em
work/wmt-lib-early-init-build-20261028-a.log, exports reais kernel/BTIF via
KBUILD_EXTRA_SYMBOLS, sem MODPOST_WARN (aviso existente de arquivo
build/Module.symvers ausente permanece). Fonte wmt_lib.c SHA256
04d4bfe96c6789bcc3fb38db4bba0106da32f48745071257741cd2503872e634;
wmt_drv.ko40c1b960600c0867225225f3837829ca98e9374c484d794ea9ac6c94f8fa8a1b;
Module.symvers230395d0d7450136aed7ab84d5a63f433feaa7ffbc2aad91c8e7eb28e4f066f3.
Sem carga/flash/acesso ao aparelho. Proximo bloqueio concreto: unwind apos
core/plataforma/run e quiesce completo WMT antes do STP; WMT_init ainda
ignora STP/HIF e seu error ainda chama deinit em estado parcial. Nao ha
aceite para ensaio fisico enquanto esses caminhos e admissao externa faltam.

### BTM: separar join de liberacao para romper dependencia com debug

Entrega visada: desmontagem STP sem worker usando debug liberado nem timer
do debug usando fila BTM destruida. Antes da integracao dessa ordem, criar
fase pequena de parada que conserva fila, sinais, callback e historico;
deinit final somente apos retirada dos demais produtores. Aceite offline:
stop drena timer proprio e join, nao libera recursos; repeticao nao refaz
join; init bloqueado enquanto owner parado existe; erro preserva owner;
deinit normal conserva comportamento e deinit apos stop libera uma vez.

Reuso: manter BTM LG/MediaTek GPLv2-only e OSAL ja adaptado a
timer_shutdown_sync/kthread_stop_put do Linux6.18.58,
2926d88bb7fc4608fd942453d929c39e4e5ec006. Triagem mainline/pmaports e
Qualcomm anterior nao oferece substituto compativel com fila/ops STP LG;
nao criar thread/fila/framework novo. Dividir trecho existente de deinit
em stop e cleanup, com ownership privado do singleton. Custo pequeno;
nenhuma operacao SoC/PMIC/placa nova. Stop nao bloqueia produtores externos:
o caller deve retira-los antes do cleanup final. Sem admissao concorrente
de init/stop/deinit nesta etapa; contrato de lifecycle serializado mantido.
Essa divisao prepara, mas nao implementa ainda a ordem completa do STP.

### STP: integrar parada BTM e destruir debug apos join — auditoria previa

Aceite offline desta integracao: timer TX desligado antes dos owners;
worker BTM joined com fila viva; PSM retirado mantendo debug/core vivos;
debug drena ambos timers e log work antes dos frees; so entao libera BTM.
Erro em qualquer owner interrompe a cadeia, preserva os seguintes e permite
retry das etapas remanescentes. Limpeza final apaga os sete callbacks e
ponteiros STP/debug. Pre-condicao: caller ja retirou produtores externos;
esta mudanca nao implementa essa admissao nem autoriza carregar o modulo.

Reuso: mesmas fontes LG GPLv2-only, destructor compressor LG existente,
timer_shutdown_sync e cancel_work_sync Linux6.18.58 commit2926d88bb7fc4608fd942453d929c39e4e5ec006.
Mainline fornece drenagem, nao o grafo privado STP/BTM/debug; triagem
mainline/pmaports/MediaTek/Qualcomm anterior mantida. Sem nova abstracao,
somente ordenar ownership existente. Centralizar compressor no destructor
do core dump exige remover free duplicado em flush; reset continua usando
destructor. Snapshot pendente apos cancel pertence ao log; ignorar sentinel
STP_MAGIC_NUM. Mantem netlink errno antes de qualquer free. Reset/flush
concorrentes e emissores externos continuam bloqueios separados.

Resultado integrado: wmt-btm-stop-retain-v1.patch divide stop/cleanup.
Flag privada conserva ownership apos join; stop repetido nao repete join,
init nao sobrescreve owner parado; deinit libera uma vez e so entao limpa
flag. Sem locks novos nem promessa de lifecycle concorrente. Testes reais
BTM init/deinit/stop passaram com ASan+UBSan/-Werror, inclusive owner errado,
falha de join, recursos vivos durante join pausado e stop sem frees,
historico opcional e deinit normal/apos stop. Testes antigos preservam
roundtrip e hashes anteriores, revertendo primeiro o delta novo.
Log work/wmt-btm-stop-host-20261028-a.log. Header novo compilado junto.

wmt-stp-owner-teardown-v1.patch integra timerTX shutdown -> stopBTM ->
deinitPSM -> deinitdebug -> cleanupBTM -> locks/callbacks. Cada ponteiro
e apagado so apos sucesso da respectiva retirada; erro exato interrompe
caminho preservando owners posteriores/locks/sete callbacks para retry.
Guard sem owners impede tocar timer/locks nao inicializados/repetir deinit.
Core dump drena timers ANTES de liberar compressor/cabecalho/lock; compressor
centralizado elimina leak no teardown e free duplicado no flush/reset.
Debug limpa globals, cancela log work e libera snapshot se cancelado antes
de executar, sem liberar sentinel. gcoredump tambem limpa global.

test_wmt_stp_teardown.py compila init/deinit reais com owners doubles;
confirma ordem TSPDB, errno EIO/ETIMEDOUT/positivo em cada um dos quatro
estagios, quarantine, initEBUSY e retry sem double-free. Roundtrip dois
arquivos fuzz=0 e hashes anteriores conferidos. Log
work/wmt-stp-teardown-host-20261028-a.log.
test_wmt_stp_debug_teardown.py compila destructors reais debug/core/compressor
e flush real com reset double delegando ao destructor real. Verifica
ENOMEM nao necessario aqui (nao ha alocacao), netlinkEIO sem free, owner
errado, timer callback pausado com owners vivos ate drain, compressor com
L1/L2/worker/workspace, snapshot ausente/pendente/ja consumido/sentinel,
globalsNULL e flush sem double-free, gcoredump repetido. Log
work/wmt-stp-debug-teardown-host-20261028-a.log. ASan+UBSan/-Werror passaram;
timer/work/thread e netlink sao doubles, NAO execucao de kernel real.
Regressoes init/netlink atuais passaram em
work/wmt-stp-teardown-init-host-20261028-a.log e
work/wmt-stp-teardown-netlink-host-20261028-a.log.

Build ARM32 -Werror/modpost reais passaram em
work/wmt-stp-teardown-build-20261028-a.log. Exports reais kernel/BTIF
via KBUILD_EXTRA_SYMBOLS, sem MODPOST_WARN; mesmo aviso de Module.symvers
do build ausente, nao exports ausentes. wmt_drv.ko SHA256
b09db2bcc73ccc9b5c587492092b2e05ba7a31634c0582b2be0dae513451f238;
Module.symvers230395d0d7450136aed7ab84d5a63f433feaa7ffbc2aad91c8e7eb28e4f066f3.
Fonte BTMf9cb47a60a19e5e1ba759e61074f1539e7574c86ebc2b091dfc0c4bd653146a2,
header2ab9e7ffed5c86577915c3ae93cbbf06f023012146f07b3207c63f58e47f03ee;
coreb2f3fe44c097282a452b7ff110e8d23d761d544a396d8ca5b5d9e05c77296892;
debug729c64157b45b2ee419dad3f557cebcce7d7d9e355c9ac65883b10028c6cdbb6.
Sem aparelho/carga/flash. Ordem interna corrigida sob pre-condicao de
retirada externa, ainda nao satisfeita pelo caller WMT. Proximos gates:
admissao/drenagem de APIs/transportes/cdev externos e propagacao de erro
nos callers WMT, alem do remove DMA BTIF ja registrado. Nao e aceite fisico.

### STP debug: ownership do registro generic-netlink — auditoria previa

Entrega visada no aparelho: habilitar/desabilitar o canal de coredump sem
registro duplicado ou estado publicado apos falha. Aceite desta etapa offline:
registro idempotente, errno preservado, retirada apenas de familia adquirida,
pares preservados quando unregister falha e flag alterada somente no sucesso.
Nao autoriza carga nem resolve a retirada dos produtores internos do debug.

Reuso: manter familia/ops LG MediaTek GPL-2.0 existentes e usar
genl_register_family/genl_unregister_family e mutexes do Linux6.18.58,
commit2926d88bb7fc4608fd942453d929c39e4e5ec006. net/netlink/genetlink.c
declara SPDX GPL-2.0. A familia LG nao habilita parallel_ops; unregister
serializa handlers recebidos via genl_lock_all e remove o ID antes de retornar.
Isso NAO drena chamadas de envio internas ao WMT. Mainline, postmarketOS e
pilhas Qualcomm nao fornecem substituto compativel para este protocolo privado;
mantem-se a decisao da triagem anterior, sem novo driver ou backend paralelo.
Cola pequena especifica desta familia: ownership e propagacao de erro;
binding lock com vida estatica, separado do lock de registro. Nunca manter
binding lock durante unregister, pois um handler recebido pode precisar dele.
Remocao ativa de timers/work e corridas dos emissores continuam fora do aceite.

Resultado netlink: wmt-stp-netlink-lifecycle-v1.patch mantem binding mutex
estatico, separa registro serializado e retorna errno exato. Init repetido
nao registra novamente; deinit ausente nao toca familia. Unregister ocorre
sem binding mutex; so no sucesso limpa pares/ownership. Em falha, preserva
pares e registro. Controle de modo serializado garante registro real a cada
chamada e publica flag somente apos sucesso (inclusive retry e modo1->2).
stp_dbg_deinit valida owner e interrompe antes de qualquer free se unregister
falhar. Isso nao corrige o teardown do STP caller, que ainda ignora esse
erro, nem drena emissores/timers/work: modulo continua sem aceite de carga.

Teste test_wmt_stp_netlink.py passou com funcoes reais de init/deinit/mode e
guard do destructor, doubles de registry e mutexes pthread, ASan+UBSan e
-Werror. Injeta ENOMEM/EEXIST/EIO em register/unregister; confirma estado,
pares e flag preservados, retry, ausencia idempotente, owner invalido sem
efeitos e doze mudancas concorrentes com apenas um register. Callback
recebido pausado espera unregister entrar e depois adquire binding mutex:
join conclui e pares sao limpos, sem inversao nesse modelo. Nao executa
netlink nem kernel locks reais; nao testa emissor concorrente. Roundtrip
reverse/reapply dos tres arquivos passou fuzz=0 e hashes anteriores de
debug/core conferidos. Regressao dos dois init reais passou mantendo
verificacao do patch anterior, nao apenas repin. Logs:
work/wmt-stp-netlink-host-20261028-a.log e
work/wmt-stp-netlink-init-regression-20261028-a.log.

Build ARM32 -Werror/modpost reais passou:
work/wmt-stp-netlink-build-20261028-a.log. Exports reais via vmlinux.symvers
e BTIF/Module.symvers, sem KBUILD_MODPOST_WARN. Aviso existente de ausencia
de build/Module.symvers permanece; exports foram supridos explicitamente.
Fonte debug SHA254fef9209171078b1801ca68596d7fc777cb53773708c5920198f136eb36c8c;
header55580eec34bb44c85af0daa8ee4bc90736247ace0bc446fa9ac5135b6667fb5a;
core4adcf875a69981a5779bcfc24da43af999249e39ea65ad7bde0c2ce0ff641c3d.
wmt_drv.ko6c0916f0c5792ee791abc6f5d91c899d917403f12394560705b44d1e405f2d30;
Module.symvers230395d0d7450136aed7ab84d5a63f433feaa7ffbc2aad91c8e7eb28e4f066f3.
Sem carga, flash, nova leitura do aparelho ou alteracao de fonte LG original.

### STP debug: init com ownership local e publicacao somente ao concluir

Entrega pretendida: falha de alocacao do debug nao deixa globals apontando
para memoria liberada nem desmonta netlink que a tentativa nao registrou.
Aceite offline: falha em cada alocacao retira somente subobjetos locais,
sem publicar globals, cancel de work apenas se inicializado e retry valido;
sucesso conserva mesmos objetos/log/BTM. Sem carga/flash.

Reuso: stp_dbg.c LG GPLv2-only e alocadores/timer/work Linux 6.18.58 revisao
2926d88bb7fc4608fd942453d929c39e4e5ec006. Triagem mainline/pmaports/MediaTek/
Qualcomm anterior nao fornece debug STP proprietario equivalente. Reusar
helpers cpupcr/dmaregs/core_dump existentes e cleanup local em labels, nao
criar novo coletor, formato ou framework. Remover testes IS_ERR de kzalloc/
vmalloc: essas APIs retornam NULL na falha, nao ERR_PTR.

Problema: init publica g_stp_dbg antes de criar subobjetos e usa globals
intermediarios. ERR_EXIT2 chama stp_dbg_deinit que desmonta netlink separado,
nao zera globals e nao drena log work; proxima tentativa pode reutilizar
ponteiros liberados. Netlink e criado por selecao de sink, nao pelo init.
Adaptacao: criar core_dump/cpupcr/dmaregs em variaveis locais, publicar os
quatro globals apenas ao concluir; erro usa labels de subobjetos adquiridos
e drena work do log antes de free. Core_dump local nunca foi publicado nem
teve timers armados; seu destructor existente vale para essa fase.
Guard de globals existentes impede sobrescrever outro owner. Nenhum novo
acesso MMIO ou ativacao de timer/netlink. Teardown ativo debug global e
producao concorrente continuam gates separados, nao autorizacao de carga.

Resultado: wmt-stp-debug-local-init-v1.patch aplicado e reverse dry-run
fuzz=0. Init recusa qualquer global de owner anterior antes de alocar;
core_dump/cpupcr/dmaregs sao locais ate todos existirem. Erro de logsys
somente libera debug, sem work nao inicializado. Erros seguintes desfazem
subobjetos locais em ordem inversa e cancelam log work antes de vfree.
Nao chama stp_dbg_deinit/netlink no rollback. Sucesso publica subobjetos e
g_stp_dbg por ultimo. Nao e publicacao RCU/atomica para leitores concorrentes;
contrato de caller sem produtores durante init ainda e obrigatorio.

Teste test_wmt_stp_debug_init.py passou em
work/wmt-stp-debug-init-host-20261028-a.log com -Werror/ASan+UBSan.
Compila init atual e helpers reais core_dump/cpupcr/dmaregs init/deinit,
com alocadores/timers/locks/work doubles. Injecao nas cinco alocacoes
(debug, logsys e tres subobjetos) verifica globalsNULL em cada aquisicao e
free do rollback, nenhum residual/cancel de work nao inicializado, timers
locais nao armados, e retry bem-sucedido apos cada falha. Sucesso conserva
BTM/log/locks/timeouts, inclusive btmNULL permitido; init duplicado ou cada
global de owner anterior bloqueia novas alocacoes e preserva referencias.
Fixture de sucesso libera globals manualmente para descartar teste, nao
aprova deinit ativo. Nenhum helper de netlink e fornecido no harness: init
nao o usa. Roundtrip reverse/reapply fuzz=0 confirma hash anterior e bytes
atuais. Nao executa kernel timer/work reais nem leitores concorrentes.

Fonte debug antes SHA256
12c4ebafa8b978a85c20735be73b016c7bdbcb9e4c0b41fd8384ea9d2cfcf9aa;
apos 8696b02f6892237a52fed8b30810300969ecb9745cba16cbf488b15ebb5c2298.
Build ARM32 -Werror e modpost reais passaram em
work/wmt-stp-debug-init-build-20261028-a.log. stp_dbg.o SHA256
bdf1e8169072d88e7a5b0d736753e71749111aa274f679c0a99be5ca784ecc27;
wmt_drv.ko 5a27aea9698a4b6bddefa5a5495345827777cd032a4ccdf3dd2801e8df3724c8;
Module.symvers segue 230395d0d7450136aed7ab84d5a63f433feaa7ffbc2aad91c8e7eb28e4f066f3.
Exports reais vmlinux/BTIF via KBUILD_EXTRA_SYMBOLS; aviso Module.symvers
ausente permanece, sem KBUILD_MODPOST_WARN, novos exports ou rebuild amplo.

Limites: este rollback usa core_dump destructor antigo somente sobre objeto
local com timers nunca armados e compressorNULL. Destructor ativo ainda usa
stop nao sincrono e pode vazar compressor; stp_dbg_deinit global deixa
ponteiros pendurados e log dump pendente, netlink init/deinit nao tem tracking.
Nao declarar unload/reinit apos uso corrigidos. Proximo bloqueio e owner
debug ativo com netlink/timers/work, depois admissao/retirada STP/WMT e
WMT_init. Nenhuma carga, flash ou funcionalidade nova comprovada no aparelho.

### STP core: ownership das etapas de init falho

Entrega pretendida: erro de init PSM/BTM/debug nao perde worker valido nem
libera sincronizacao que ele ainda pode usar. Aceite offline: NULL de callback
recusado; owner existente impede init duplicado; timer de retry shutdown,
BTM/PSM validos retirados antes de locks/callbacks; cleanup falho conserva
referencias e impede sobrescrita. Sem carga ou uso no aparelho.

Reuso: stp_core.c/PSM/BTM LG GPLv2-only, respectivos owners/deinit corrigidos
e timer_shutdown_sync Linux 6.18.58 revisao
2926d88bb7fc4608fd942453d929c39e4e5ec006. Triagem mainline/pmaports/MediaTek/
Qualcomm anterior nao oferece protocolo STP equivalente, usar codigo LG
com pequenas extensoes de erro em vez de novo framework. Nao reimplementar
parser/transporte, alterar sucesso ou relaxar checagem/diagnostico.

Bug: ERROR chama apenas psm_deinit, inclusive com NULL, nao retira BTM se
debug falha, nem timer/locks/callbacks. Adaptar ERROR por ownership existente
nos ponteiros core; shutdown de timer antes de joins; limpar ponteiro apenas
apos deinit bem-sucedido; em falha de cleanup retornar erro original e reter
restante em quarentena, sem destruir locks usados pelo owner. ABI de falha
das etapas continua -3. Caller ainda deve serializar lifecycle e nao admitir
produtores externos durante init; nenhum mutex universal novo.

Limite identificado antes de implementar: stp_dbg_init tenta cleanup proprio,
mas stp_dbg_deinit deixa globals de subobjetos pendurados e nao drena todos
os trabalhos/timers. Retirada dos owners core nao prova que debug parcial
esta limpo; retry apos falha de debug e unload continuam gates ate correcoes
no owner debug. Esta etapa valida core, nao essa implementacao subordinada.

Resultado: wmt-stp-core-init-unwind-v1.patch aplicado e reverse dry-run
fuzz=0. NULL de callback retorna EINVAL antes de dereference; PSM/BTM/debug
ja publicados retornam EBUSY antes de alterar contexto. ERROR desliga
timer definitivamente, destroi BTM se existe e depois PSM se existe,
limpa cada referencia apenas apos deinit bem-sucedido. Se deinit falha,
retorna erro original -3 com owners/locks/callbacks retidos e init novo
recusado; nao afirmar recuperacao. Se owners drenam, deinit dos ring locks
e ctx lock e limpeza dos sete callbacks. Nao modificado sucesso STP ou parser.

Teste test_wmt_stp_core_init.py passou em
work/wmt-stp-core-init-host-20261028-b.log, compilando init original e portado
reais com -Werror/ASan+UBSan, owners/debug/timer/locks como doubles.
Original com PSM falho chama deinitNULL e conserva lock/callback;
portado nao deinit owner inexistente e traces sao T, TP ou TBP para falha
de PSM, BTM ou debug. Timer precede joins, owners precedem locks/callbacks;
NULL e init duplicado/owner debug existente nao alteram contexto. Injecao
de EIO/ETIMEDOUT/nonzero positivo em deinit BTM/PSM mantem referencias
necessarias, locks e callbacks; segunda tentativa recebe EBUSY. Retry com
owners doubles limpos funciona, sucesso conserva os sete callbacks e todos
os subowners. Isso nao comprova retry do debug LG real: double de debug
falho nao tem os globals pendurados observados no owner subordinado.
Roundtrip reverse/reapply fuzz=0 devolve bytes exatos. Harness a recusou
macro timer que descartava resultado com warning; double virou funcao,
sem relaxar -Werror ou sanitizers. Nao executa kernel/threads/IRQ reais.

Fonte STP core final SHA256
42d03c074203d9365d1dde8c6f17a5a21aa4235e9732e00bd8ae4e0f0cdab2fa.
ARM32 -Werror e modpost reais passaram em
work/wmt-stp-core-init-build-20261028-a.log. stp_core.o SHA256
9f5e7bea342c07a55007658951d7a5511e1ca8dcb497ebb007957442a90a4f6b;
wmt_drv.ko 314dac1881700557a398ef1c8208b692e9e55f44089aa29d98e78d1ab1b96029;
Module.symvers segue 230395d0d7450136aed7ab84d5a63f433feaa7ffbc2aad91c8e7eb28e4f066f3.
Exports reais vmlinux/BTIF via KBUILD_EXTRA_SYMBOLS; aviso Module.symvers
ausente permanece, sem KBUILD_MODPOST_WARN, novos exports ou rebuild amplo.

Limites: guard de owner nao serializa duas inicializacoes simultaneas nem
drena public APIs. Init ainda publica callbacks antes do final; caller deve
impedir consumidores durante tentativa. Deinit ativo core ainda libera
debug antes de BTM/PSM e nao limpa todos os ponteiros/timer, portanto nao
aprovado para unload/reinit real. Proxima dependencia concreta: cleanup do
owner debug sem globals pendurados e com seus timers/work drenados, seguido
de admissao/retirada core e WMT_init. Nenhuma carga, flash ou funcionalidade
nova comprovada no aparelho nesta etapa.

### BTM owner: timer definitivo e join antes do historico

Entrega pretendida: BTM quiescido pelo chamador encerra timer/thread antes
de liberar historico/signals/event/lock; reinit nao perde alocacoes antigas.
Aceite offline: callback e join pausados conservam recursos, shutdown recusa
rearm, snapshot historico pendente/running liberado uma vez, owner estranho
ou nao inicializado recusado, falha de destroy conserva dados. Sem carga.

Reuso: BTM/OSAL LG GPLv2-only e timer_shutdown_sync/cancel_work_sync Linux
6.18.58 revisao 2926d88bb7fc4608fd942453d929c39e4e5ec006, ja auditados na
etapa PSM. Triagem mainline/pmaports/MediaTek/Qualcomm anterior nao fornece
protocolo BTM WMT; reaproveitar helper de cleanup existente, sem thread/fila
nova. Drenagem definitiva fica no owner de timer/worker, nao novo transporte.

Problema: stp_btm_deinit atual apenas destroi task, nao drena timer nem
libera historico/sincronizacao. Adaptar deinit para validar singleton e task
owner, shutdown timer, join e helper existente; helper tambem deve liberar
snapshot de dump cancelado, alem da queue. Init falho continua usando mesmo
helper e timer stop sync apos thread retirada. Nenhuma API de produtores e
desabilitada; caller precisa retirar/drenar todas antes de chamar deinit.

Resultado: wmt-btm-owner-teardown-v1.patch aplicado/reverse dry-run fuzz=0.
Owner NULL, diferente de stp_btm_i ou sem task e recusado antes de timer/
globals. Shutdown definitivo precede destroy/join. Erro de destroy conserva
dados; sucesso chama helper existente de recursos, agora tambem retira
snapshot de historico cancelado apos cancel_work_sync. Stop sync adicional
do helper sobre timer ja shutdown e seguro e preserva seu uso no init falho.
ABI de retorno BTM_FAIL/SUCCESS, fila e caminho de sucesso de init preservados.

Teste test_wmt_btm_teardown.py passou em
work/wmt-btm-teardown-host-20261028-b.log com -Werror/ASan+UBSan/pthreads.
Compila init/helper/deinit reais da fonte fixada; primitivas kernel sao
doubles. Callback pausado conserva recursos ate shutdown drenar; join pausado
conserva historico/signals/event/lock/callback, duas tentativas de rearm apos
shutdown sao recusadas. Verifica snapshot ausente, cancelado pendente e
running que termina/libera base, memoria opcional de historico ausente,
erro de destroy sem free, NULL/owner estranho/segundo deinit recusados e
init/deinit/reinit completos sem residuos. Snapshot running e simulado pelo
double cancel, nao executa worker historico kernel. Tentativa a do harness
recusou tipo bool do timer OSAL; fixture corrigida para distinguir wrapper
OSAL e timer nativo, mantendo -Werror e sanitizers.
Regressao init falho passou em work/wmt-btm-init-host-20261028-b.log,
com pin novo e roundtrip dos patches teardown/init na ordem inversa e
reaplicacao fuzz=0, confirmando bytes exatos. Sem suites amplas.

Fonte BTM final SHA256
5c378711a8395e68157a202ab43e064682d46e79becbe76c805992e6c6667e14.
Build ARM32 -Werror e modpost reais passaram em
work/wmt-btm-teardown-build-20261028-a.log. btm_core.o SHA256
a155ce70910af6b67c76847e87bd27a3686911d485876cedae907e86608d9b43;
wmt_drv.ko 9ee8ae445faf33c93a95e46524f9076ea30b6010b5bd51cf50b7b5d1eec942d8;
Module.symvers segue 230395d0d7450136aed7ab84d5a63f433feaa7ffbc2aad91c8e7eb28e4f066f3.
Exports reais vmlinux/BTIF fornecidos por KBUILD_EXTRA_SYMBOLS; aviso
build/Module.symvers ausente permanece, sem KBUILD_MODPOST_WARN, novo
export ou recompilacao ampla do kernel.

Limites: caller ainda deve retirar e drenar APIs de enqueue/debug BTM antes
de chamar deinit; guard de task nao implementa admissao. Nao chamar deinit
do proprio callback/worker nem concorrer lifecycle. Snapshot/work/timer
Linux reais nao foram executados pelos testes. STP core deinit precisa
retirar produtores e respeitar ordem entre debug, BTM e PSM; init parcial
core ainda pode perder referencias. Esses sao proximos bloqueios antes de
carga, junto de WMT_init e recuperacao DMA BTIF. Nenhuma carga, flash ou
nova funcionalidade comprovada no aparelho nesta etapa.

### PSM teardown: shutdown do timer e join antes de liberar dados

Entrega pretendida: owner PSM, apos retirar produtores externos, pode parar
timer/worker antes de liberar debug, opid e historico; init seguinte nao
perde ponteiros residuais. Aceite offline: callback pendente drena, rearm
apos shutdown nao reabre timer, worker ainda pode acessar dados durante join,
snapshot de historico pendente ou em execucao nao vaza/double-free; NULL ou
init falho nao libera owner alheio. Nao e aceite de retirada dos produtores.

Reuso: timer_shutdown_sync Linux 6.18.58 revisao
2926d88bb7fc4608fd942453d929c39e4e5ec006, kernel/time/timer.c GPL-2.0-only;
OSAL thread destroy task-ref, cancel_work_sync, FIFO/locks LG GPLv2-only.
Mainline fornece exatamente shutdown contra rearm circular timer/worker;
timer_delete_sync sozinho nao impede rearm pelo callback _stp_psm_stp_is_idle.
Triagem pmaports/MediaTek/Qualcomm anterior nao substitui protocolo PSM,
mas API nativa de timer e compativel. Nao criar scheduler/worker novo.

Adaptar _stp_psm_deinit_monitor local para shutdown definitivo, usado apenas
em deinit e init falho; retry executa timer_setup existente. Em deinit:
validar owner/FIFO, shutdown, join, depois dados e sincronizacao. Historico
usa cancel_work_sync, mas se trabalho foi cancelado antes de executar ainda
ha snapshot em dump_ring_buffer.base; libera-lo apos drenagem, sem tocar
snapshot ja liberado pelo worker (baseNULL). Nao alterar caminho de power,
FIFO ou debug normal para obter resultado. Caller deve garantir sem novos
produtores; isso ainda nao e implementado por esta etapa.

Resultado: wmt-psm-owner-teardown-v1.patch aplicado/reverse dry-run fuzz=0.
_stp_psm_deinit_monitor usa timer_shutdown_sync definitivo (nao pause de
monitor normal); busca nesse arquivo confirma uso somente em init falho e
deinit. Deinit recusa NULL, owner diferente de stp_psm_i e FIFO ausente
antes de tocar globals/timer; shutdown precede join. Erro de destroy nao
libera dados. Apos join, retira ambos debug/locks, snapshot historico e queue,
signals/event/wakelock/FIFO/locks/callbacks. Timer setup do init permite retry.
Snapshot cancelado e liberado somente apos cancel_work_sync; worker que
terminou limpa baseNULL e nao sofre segunda liberacao. osal_free usa kvfree,
aceitaNULL. Nao adicionada dependencia de alocacao ou novo timer/workqueue.

Teste test_wmt_psm_teardown.py passou em
work/wmt-psm-teardown-host-20261028-a.log com -Werror/ASan+UBSan/pthreads.
Compila monitor shutdown, init e deinit reais extraidos da fonte fixada;
primitivas kernel sao doubles. Timer callback pausado mantem dados vivos,
shutdown espera e callback tenta rearm (recusado); join pausado mantem FIFO,
debug/opid e locks ate worker terminar. Worker tambem tenta rearm depois do
shutdown, recusado. Casos de snapshot ausente, cancelado pendente e running
que termina/libera base, historico opcional ausente, erro de join preservando
dados, NULL/owner estranho sem efeitos, segundo deinit vazio recusado e
init/deinit/reinit completos sem residuos passaram. Modelo de running work
termina dentro do double cancel, nao executa worker historico real. Teste nao
prova scheduler/timer Linux ou isolamento de produtores externos.
Regressao init parcial passou em work/wmt-psm-init-host-20261028-c.log com
pin atual. Roundtrip patch fuzz=0 devolve bytes exatos, sem teste amplo.

Fonte PSM final SHA256
0fff4cb8a2d304dbde1a5aeb5094cba57d470e33a0cac2939cfb6c7a19ea3031.
Referencia timer.c nativo SHA256
8b17624a9a27787d29b52f5a4cadbd8bd458d92b3d5c811f145397f8ae283e60,
documenta shutdown seguido de retirada de work para impedir rearm circular.
ARM32 -Werror e modpost reais passaram em
work/wmt-psm-teardown-build-20261028-a.log. psm_core.o SHA256
fd3e911f215da962e141c04163c00f3f5f91897363bf9ecc94e3ec731085029e;
wmt_drv.ko 3abcb9f8de53c5fc68031c487bbc2245e9538b47c2b7ca9e1a06e7a4dd66e343;
Module.symvers segue 230395d0d7450136aed7ab84d5a63f433feaa7ffbc2aad91c8e7eb28e4f066f3.
Exports reais vmlinux/BTIF fornecidos via KBUILD_EXTRA_SYMBOLS, aviso
Module.symvers ausente permanece, sem KBUILD_MODPOST_WARN ou novos exports.

Limites: caller precisa retirar e drenar todas as APIs/diagnosticos PSM e
serializar lifecycle. Nem guard de FIFO nem shutdown do timer garantem isso
sozinhos; nao chamar deinit sincrono de callback/worker proprio. Dados de
worker sao preservados ate join, mas produtores que ignorem contrato ainda
podem acessar memoria liberada. Ordem de STP core e admissao/retirada WMT
continuam proximos bloqueios antes de carga. Deinit BTM ativo tambem precisa
drenar timer/historico antes de STP poder confiar na limpeza. Nenhuma carga,
flash ou nova funcionalidade comprovada no aparelho nesta etapa.

### PSM: memoria de debug antes do primeiro wake e unwind de init parcial

Entrega pretendida: erro de init PSM nao deixa thread rodando ou referencia
perdida; worker so inicia com dados que pode acessar prontos. Aceite offline:
falhas FIFO/create/monitor/alloc/run liberam etapas adquiridas, debug nunca
liberado com task ainda viva, retry funciona apos falha; sucesso conserva
callbacks/filas/timer e semantica de power LG. Nenhum ensaio fisico.

Reuso: psm_core.c/OSAL LG GPLv2-only e primitivas Linux 6.18.58 revisao
2926d88bb7fc4608fd942453d929c39e4e5ec006. Triagem mainline/pmaports/MediaTek/
Qualcomm anterior nao fornece implementacao do protocolo PSM WMT; adaptar
fila/thread/monitor existentes, nao novo framework de energia. Thread
create/destroy/ref OSAL ja corrigidos, timer stop sync, cancel_work_sync e
deinit/free existentes. Codigo novo e apenas bookkeeping local de etapas.

Falha observada: run e chamado antes de alocar g_stp_psm_dbg/opid; falha de
qualquer malloc retornaNULL sem parar worker. Create/monitor/run falhos
tambem nao retiram todas as etapas, historico ou debug. Mover as duas
alocacoes para antes de run e manter NULL como resultado falho (nao relaxar
debug requerido pelo codigo atual); parar/destruir task criada antes de
liberar dados. Guard contra owner/debug ainda presentes evita sobrescrever
recurso de inicializacao anterior. Helper so para init falho, sem alterar
deinit ativo ou afirmar isolamento de novos produtores.

Resultado: wmt-psm-init-unwind-v1.patch aplicado e reverse dry-run fuzz=0.
Guard inicial recusa task/debug ainda presentes antes de sobrescrever estado.
As duas estruturas debug/locks agora existem antes de run; erros de malloc
continuam retornandoNULL, nao desabilitado diagnostico para obter sucesso.
Bookkeeping local wait_ready/monitor_ready impede deinit de objeto ainda
nao inicializado. Erros apos create param/soltam owner task primeiro, depois
monitor/wait/debug, historico/signals/event/wakelock/locks/FIFO. Erro FIFO
nao libera FIFO inexistente; callbacks/flag de tentativa sao retirados.
Monitor atual so inicializa timer e retorna0 para objeto valido; erro
injetado e contrato sem timer parcialmente inicializado, nao timeout fisico.

Teste test_wmt_psm_init.py passou em work/wmt-psm-init-host-20261028-b.log
com -Werror/ASan+UBSan, compilando init anterior e portado reais da fonte
staging fixada. Original com primeiro malloc falho acorda worker cedo,
retornaNULL e deixa task/memoria; fixture descarta residuos so para teste.
Portado injeta ENOMEM/EAGAIN/EINTR/EPROBE_DEFER em FIFO/create/monitor/run,
falha em cada uma das duas alocacoes debug, com historico opcional alocado
ou sem memoria. Verifica owner retirado antes dos frees, monitor/wait/event/
signals/locks e FIFO liberados, nenhuma alocacao residual, callbacks limpos
e retry de sucesso apos cada falha. Historico opcional ausente nao impede
sucesso; init duplicado e debug de owner anterior nao sao sobrescritos.
Workerdados so sao considerados prontos se ambos debug/locks existem antes
do primeiro run. Teste nao executa thread/timer/workqueue do kernel real.
Primeiro teste work/wmt-psm-init-host-20261028-a.log detectou segunda falha
de malloc ainda sem unwind; corrigido goto e repetido sem relaxar criterio.
Patch roundtrip fuzz=0 preserva bytes atuais exatos.

Fonte PSM final SHA256
d85adb7c78fbe68bc4cf8a6d3819480bbc9e4bb62daa563e0b78dc44b396775d.
Build ARM32 -Werror e modpost reais passaram em
work/wmt-psm-init-build-20261028-a.log. Exports reais vmlinux/BTIF fornecidos
por KBUILD_EXTRA_SYMBOLS; aviso build/Module.symvers ausente permanece,
sem KBUILD_MODPOST_WARN ou exports novos. Objeto psm_core.o SHA256
8c20f08ce5d49799df01c7a006e051eb896d3c75cf91cc209494b8f568b8bcc4;
wmt_drv.ko dde47ffb949be73bfdaf6fbc29a49662b36ca821a3096fba409e2120d4c2a30c;
Module.symvers segue 230395d0d7450136aed7ab84d5a63f433feaa7ffbc2aad91c8e7eb28e4f066f3.
Sem rebuild amplo do kernel ou alteracao de fonte LG original.

Limites: callers ainda devem serializar init e nao admitir produtores antes
do retorno. Guard de ponteiro nao substitui mutex; teste e sequencial e
libera fixture de sucesso manualmente, nao aprova deinit ativo. PSM deinit
LG ainda libera debug antes de parar task, nao libera opid e nao drena
historico; guard novo recusa reutilizar esse owner residual em vez de perder
ponteiro. Esse teardown precisa correcao antes de unload/reinit funcional.
Falhas internas de wakelock/OSAL init que caller ignora tambem nao foram
auditadas como resolvidas. STP core e WMT_init continuam com init parcial e
retornos ignorados; remocao DMA/recuperacao BTIF continua gate. Nenhuma
carga, flash ou nova funcionalidade comprovada no aparelho nesta etapa.

### BTM: desfazer init parcial sem perder a thread criada

Entrega pretendida: erro ao criar/iniciar worker BTM nao deixa task, timer,
fila de historico ou locks de init pendentes; retry nao sobrescreve owner.
Aceite offline: create/run falhos devolvem NULL como ABI LG e liberam apenas
recursos adquiridos, sucesso preserva fila/callback/worker, init duplicado
nao reinicializa objetos ativos. Sem carga/flash.

Reuso: LG common_main/core/btm_core.c e OSAL GPLv2-only, Linux 6.18.58
revisao 2926d88bb7fc4608fd942453d929c39e4e5ec006. Reusar thread destroy com
task ref ja corrigido, timer stop sync, cancel_work_sync e osal_free. PSM/BTM
do mainline/pmaports nao implementam protocolo proprietario WMT; Qualcomm
nao e backend BTIF MT6765. Auditoria de alternativas anterior permanece.
Nao novo worker/fila/framework; helper local somente para init falho.

Falha concreta: init BTM cria lock/event/signals, timer e queue de historico,
mas ERR_EXIT1 retorna NULL sem cleanup. Run falho perde referencia de thread
ja criada. Timer init retorna0 no OSAL atual, historico e opcional e seu
work so e inicializado quando queue alocada. Cleanup deve respeitar isso;
nao transformar falha de memoria de log em dependencia obrigatoria do radio.
Repetir init com BTMd.pThread presente deve recusar antes de tocar recursos.
Nao generalizar esse helper para deinit ativo: produtores externos e callbacks
ainda precisam quiescencia, e stop timer nao basta contra novos produtores.

Resultado: wmt-btm-init-unwind-v1.patch aplicado e reverse dry-run fuzz=0.
BTMd.pThread presente recusa init antes de tocar locks/event/queue. Falha de
create vai ao helper local; run falho primeiro destroi task ja criada e so
depois drena timer/historico e deinit signals/event/lock, limpa callback.
OSAL destroy de task valida retorna0 apos esperar e soltar ref, conforme
etapa anterior. Historico NULL nao chama cancel_work em work nao inicializado;
historico alocado e drenado antes de free e ring base limpa. Nao alterado
stp_btm_deinit ativo ou formato de mensagens/ABI do retorno NULL.

Teste test_wmt_btm_init.py passou em work/wmt-btm-init-host-20261028-a.log:
compila init original e portado/helper reais, fixados por SHA, com
-Werror/ASan+UBSan e doubles OSAL/work/timer/thread. Original retornaNULL
apos create falho deixando historico, timer e sincronizacao; fixture
descarta esses residuos somente para comparar, nao e recuperacao real.
Portado testa ENOMEM/EAGAIN/EINTR/EPROBE_DEFER em create/run com historico
alocado e sem memoria opcional; nenhuma task antes de free, nenhum free
invalido/cancel de work sem init, signals/event/lock e callback retirados;
retry de sucesso apos cada falha; sucesso mesmo sem historico; init
duplicado nao muda bytes/recursos ativos. Roundtrip reverse/reapply fuzz=0
confirma hash anterior e bytes finais. Nao executa thread/timer/work kernel
reais ou produtores concorrentes. Cleanup do fixture de sucesso e somente
limpeza de teste, nao prova do deinit ativo LG.

Fonte BTM antes SHA256
e0b4da14b1e44b5d5239fb068b03ea7fa5828727d16e5d8a123ac0fcf66b98af;
apos 6045487f7ff7208b34ff31c098c605c6dd62d9dde71c79d06a302c123d09b50d.
Build ARM32 -Werror e modpost reais passaram em
work/wmt-btm-init-build-20261028-a.log, com exports reais vmlinux/BTIF.
Aviso build/Module.symvers ausente permanece, fornecidos exports via
KBUILD_EXTRA_SYMBOLS, sem KBUILD_MODPOST_WARN. btm_core.o SHA256
b13187cddbd83d66b2328f6046d801f29d45984c8d42f2be67fced56a0f78d68;
wmt_drv.ko 70289cb175e491226be7eb3068656d3b6d35abc06a54ca8ceabac78ad9cdfffd;
Module.symvers segue 230395d0d7450136aed7ab84d5a63f433feaa7ffbc2aad91c8e7eb28e4f066f3.
Sem novo export, rebuild amplo de kernel ou alteracao de codigo LG original.

Limites: helper vale para init que nao admitiu produtores externos. Guard
de ponteiro nao serializa duas chamadas simultaneas; caller WMT/STP precisa
serializacao. Callback/timer externo durante tentativa nao esta validado.
Deinit ativo BTM ainda so destroi thread; nao foi aprovado para unload.
PSM tem falhas parciais proprias e STP core pode perder BTM valido ao falhar
debug. Esses sao proximos bloqueios do unwind, junto de admissao/retirada
dos cdevs e recuperacao DMA. Nenhuma carga, flash ou funcionalidade nova
comprovada no aparelho nesta etapa.

### OSAL: referencia de task entre create, stop e destroy

Entrega pretendida: stop seguido de destroy (WMT_lib_deinit existente) nao
usa task liberada; worker que terminou sozinho permanece valido ate destroy.
Aceite offline: get_task_struct antes de publicar/acordar, stop conserva
referencia do owner, destroy usa kthread_stop_put exatamente uma vez e
limpa ponteiro. Erro de create nao adquire ref, erro/NULL nao chega a stop.
Sem carga, flash ou acesso fisico.

Reuso: kthread/get_task_struct/kthread_stop_put Linux 6.18.58 revisao
2926d88bb7fc4608fd942453d929c39e4e5ec006. kernel/kthread.c GPL-2.0-only,
SHA256 edc2aa0e2788de9f706e6a155d2eee0593c1dac61c6f3f480fc929f32c30c90e;
documentacao de stop exige lifetime task se thread termina sozinha, e
stop_put exige ref adicional. Free da estrutura kthread ocorre com task.
Reuso OSAL LG GPLv2-only existente, sem copiar kthread ou criar worker.
Triagem mainline/pmaports/MediaTek/Qualcomm ja registrada: lifetime nativo
e aplicavel ao wrapper; transporte/hardware nao muda. BTIF ja usa padrao
equivalente auditado, sem substituir seu getter ou referencias STP emprestadas.

Adaptacao pequena: create bem-sucedido pega referencia antes de publicar;
destroy para/espera e solta essa referencia. Stop mantem ponteiro e resultado
historico. Nao adicionar mutex universal; callers devem serializar lifecycle.
Nao chamar destroy sobre OSAL_THREAD que so empresta ponteiro de outro owner.
WMT_lib usa stop/destroy no mesmo owner; STP BTIF tem release proprio e nao
deve passar pelo destroy. Concorrencia de create/stop/destroy e callbacks
externos continuam dependencia explicita antes de carga.

Resultado: wmt-osal-thread-task-reference-v1.patch aplicado e reverse dry-run
fuzz=0. get_task_struct ocorre antes da publicacao do ponteiro e do primeiro
wake; destroy usa kthread_stop_put exportado pelo vmlinux nativo. Stop nao
solta a referencia, preservando uso stop/destroy de WMT_lib_deinit. Erros de
create/run/stop/destroy da etapa anterior permanecem; nenhum export novo.
Busca limitada em common_main encontrou assignments pThread apenas no OSAL;
STP BTIF usa publicacao RCU e release proprio. Chamadas destroy de WMT_lib,
PSM, BTM e STP SDIO correspondem a create pelo wrapper. Nao e auditoria de
todos os consumidores externos do simbolo exportado.

Teste existente test_wmt_osal_thread_errors.py ampliado, sem remover casos
de erro: passou em work/wmt-osal-thread-reference-host-20261028-a.log com
-Werror/ASan+UBSan. Compila wrappers reais atuais e create anterior; modelo
kthread conta ref de execucao/owner e recusa operacao sobre task de ref0.
Stop retira ref de execucao, owner permanece; destroy seguinte para task
ja encerrada sem acesso invalido e solta ref unica; destroy repetido vazio
nao solta novamente. Worker que sai espontaneamente conserva ref do owner
ate destroy. Create falho/NULL e ERR_PTR legado nao adquirem/soltam ref;
EBUSY nao sobrescreve owner. Roundtrip da pilha ref/erro na ordem inversa
e reaplicacao fuzz=0 devolvem bytes exatos. Nao executa kernel kthread real
nem concorrencia de lifecycle; teste e evidencia do wrapper, nao do scheduler.

ARM32 -Werror e modpost reais passaram em
work/wmt-osal-thread-reference-build-20261028-a.log. Fonte OSAL SHA256
6334dc8feecbac4f4cb9aab582fcf62e012e16f33812de3fe8af2b4ea6e4994b;
osal.o 8c0abba07e650a10bffd7dc3e72a650c4d98e5ee7780683d6545416ce4a9fb09;
wmt_drv.ko a9c746d3ac0c150971386ce00330fedad4b4733ea00dad22dda6d88f4c33b102;
Module.symvers segue 230395d0d7450136aed7ab84d5a63f433feaa7ffbc2aad91c8e7eb28e4f066f3.
Aviso build/Module.symvers ausente permanece com exports reais fornecidos
explicitamente; nao usado KBUILD_MODPOST_WARN. Sem recompilar kernel inteiro.

Limites: quem chama destroy deve possuir o owner e serializar outros
create/run/stop/destroy. Leitor diagnostico que faz get sob RCU ainda exige
retirada sincronizada: destroy nao foi tornado escritor RCU por esta mudanca.
Nao afirmar essa corrida resolvida por manter ref enquanto thread roda.
Saida espontanea sequencial agora protegida, mas buffer/callback/timer dos
owners nao recebe lifetime automatico. PSM/BTM init/deinit e WMT init parcial
continuam proximo bloqueio concreto, junto de remocao ativa/fault BTIF.
Nenhuma carga, flash ou funcionalidade nova comprovada no aparelho.

### OSAL thread: errno de kthread_create antes do unwind WMT/STP

Entrega pretendida no aparelho: falha de criar worker nao chega a
wake_up_process/kthread_stop com ERR_PTR. Aceite offline: errno exato
propagado, ponteiro limpo na falha, run/stop/destroy nao desreferenciam erro;
sucesso mantem kthread nativo. Nenhuma carga ou acesso fisico.

Reuso: OSAL LG common_main/linux/osal.c GPLv2-only, API Linux 6.18.58
kthread_create/IS_ERR/PTR_ERR revisao 2926d88bb7fc4608fd942453d929c39e4e5ec006.
Mainline e semantica autoritativa: erro e ERR_PTR, nao NULL. Pmaports usa
mesma API; wrappers Qualcomm/MediaTek distintos nao justificam thread
paralela. Auditoria anterior de reuso permanece; adaptar o wrapper existente
em vez de novo worker/framework. Correcao pequena especifica de compatibilidade
Linux, nao de hardware. Chamadores PSM/BTM/WMT verificam retorno negativo,
mas alguns nao fazem unwind completo: esta etapa nao declara isso corrigido.

Evidencia: osal_thread_create atual testa somente pThread->pThread==NULL,
retorna0 para ERR_PTR; run acorda qualquer non-NULL e destroy chama stop.
WMT_init ainda ignora retornos; mesmo apos corrigir caller isso precisa ser
resolvido para erro real de alocacao chegar ao unwind. Preservar retornos
historicos de parametro NULL; nao substituir referencia de task ativa.

Resultado: wmt-osal-thread-create-errors-v1.patch aplicado/reverse dry-run
fuzz=0. Create usa task temporario e publica somente sucesso, devolvendo
PTR_ERR; NULL defensivo vira ENOMEM e referencia ja existente retorna EBUSY.
Run/stop recusam ERR_PTR; destroy de ERR_PTR limpa campo e devolve errno,
sem chamar kthread_stop. Retornos de NULL do wrapper antigo preservados.
Sucesso continua mesmas primitivas nativas; nao houve nova thread/framework.

Teste test_wmt_osal_thread_errors.py passou em
work/wmt-osal-thread-errors-host-20261028-a.log, compilando wrappers reais
antes/depois com -Werror/ASan+UBSan. Demonstra antes: ERR_PTR de kthread_create
retorna0 e fica publicado. Depois: ENOMEM/EAGAIN/EINTR/EPROBE_DEFER exatos,
campoNULL, nenhuma chamada de wake/stop; retry cria/acorda/destroi uma vez;
destroy repetido vazio nao para outra vez; referencia ativa nao e sobrescrita;
ponteiro legado ERR_PTR e recusado sem dereference; NULL defensivo de create
recusado. Native kthread/wake/stop sao doubles, nao workers reais. Roundtrip
reverse/reapply preserva bytes do staging. Fonte OSAL final SHA256
056c14ee08f418f9476ef61a575ddcb55472601736a4ab95fed53221f4ee29dc.
Semantica fonte kernel/kthread.c nativa SHA256
edc2aa0e2788de9f706e6a155d2eee0593c1dac61c6f3f480fc929f32c30c90e:
create mantem thread parada, stop espera saida e devolve resultado de thread.

Build ARM32 -Werror e modpost reais passaram em
work/wmt-osal-thread-errors-build-20261028-a.log. Objeto osal.o SHA256
603fcd61ad61bf88a8b3cfc703798b1db185f384bae396fb7cb8e2868445dd14;
wmt_drv.ko 4a9bdffd4c21e659e53184e6fbfabdd0d8d32f16454f121b173a19b9b2262313;
Module.symvers segue 230395d0d7450136aed7ab84d5a63f433feaa7ffbc2aad91c8e7eb28e4f066f3.
Exports reais vmlinux/BTIF fornecidos, aviso Module.symvers ausente permanece;
sem KBUILD_MODPOST_WARN ou mudanca de exports, sem rebuild amplo de kernel.

Limites importantes: wrapper nao serializa create/run/stop/destroy nem passa
a possuir referencia task adicional. Stop preserva ponteiro como antes;
sequencia stop/destroy de thread ja terminada exige lifetime proprio antes
de carga. Teste nao finge que isso foi resolvido: usa fixture, nao task real.
PSM/BTM init ainda podem deixar recursos apos falhar; deinit de PSM libera
parte antes de parar worker, e WMT_init ainda ignora retornos HIF/STP.
Proxima entrega precisa usar erro agora correto e fazer unwind dos owners,
sem chamar deinit completo sobre init parcial. Fonte/dump de task com RCU
de etapas anteriores nao mudou. Nenhuma carga, flash ou funcionalidade nova
comprovada no aparelho; objetivo continua em andamento.

### WMT detect: unwind por etapas e errno original na inicializacao

Entrega pretendida: falha ao inicializar wmtdetect nao deixa registro SDIO,
platform driver, major/cdev ou class residuais; proxima tentativa usa mesmo
major configurado. Aceite offline: falha em cada aquisicao devolve errno exato,
nao remove recurso nao adquirido, nao guarda ERR_PTR e desfaz na ordem inversa.
Sem carga/flash. Nao e aceite de init interno WMT ou teardown ativo.

Reuso: caminho LG common_detect/wmt_detect.c GPLv2-only e APIs Linux
6.18.58 revisao 2926d88bb7fc4608fd942453d929c39e4e5ec006: register_chrdev_region,
cdev_add/del, class_create/destroy, device_create/destroy e registro platform.
Triagem mainline/pmaports/MediaTek/Qualcomm anterior nao fornece wmtdetect
compativel com protocolo LG; miscdevice substituiria ABI de major fixo sem
desbloquear hardware. Pequeno unwind goto no codigo existente e preferivel
a novo framework. Header/licencas das APIs permanecem do kernel nativo.

Falhas observadas: sdio_detect_init e platform_driver_register ignorados;
cdevErr nao propagado; class/device ERR_PTR mantidos; falha devolve -1 em
vez de errno e altera gWmtDetectMajor para -1. Modulo ja ligou, mas esses
caminhos impedem ensaio seguro. Manter sequencia de sucesso, identidade do
perfil antes de aquisicoes e ABI, corrigir somente efeitos sob falha.

Resultado: wmt-detect-init-unwind-v1.patch aplicado no staging com fuzz=0;
fonte anterior SHA256
7d982e69aefa96710265385ba69d42b42dff127264b1f1ed763da841e82bb93f,
final 7e109e915873a28dab0d83aab7f69b4cbf800d7e346bfa01a68e7aef6ecec837.
Init propaga erro SDIO sem cleanup indevido; erro platform retira somente
SDIO; erros seguintes retiram platform se adquirido. Class/device falhos
sao convertidos para errno e ponteiros NULL; major nao e alterado no erro.
Sequencia de sucesso/cdev/ABI nao mudou, nenhum export ou acesso MMIO novo.

Teste test_wmt_detect_unwind.py executa init real extraido da fonte fixada
com doubles de registro/cdev/class/device. Passou -Werror/ASan+UBSan em
work/wmt-detect-unwind-host-20261028-a.log: perfil nativo, generico e COMBO;
EIO/ENOMEM/EBUSY/EPROBE_DEFER em cada aquisicao, errno preservado e trace
de cleanup inverso exato, nenhum double-free/unregister nao adquirido,
ponteiros NULL, major154 preservado e retry de sucesso apos cada falha.
Root errado nao executa aquisicoes no perfil nativo. Fixture roundtrip
reverse/reapply fuzz=0 confirma bytes exatos. Nao executa driver core real.
Regressao test_wmt_native_profile.py passou em
work/wmt-native-profile-host-20261028-f.log com hash novo e roundtrip da
pilha unwind/perfil na ordem correta; criterios de admissao preservados.

Build ARM32 -Werror e modpost reais passaram em
work/wmt-detect-unwind-build-20261028-a.log (exit0). Exports nativos e BTIF
fornecidos por KBUILD_EXTRA_SYMBOLS; aviso build/Module.symvers ausente
permanece, sem KBUILD_MODPOST_WARN. Objeto wmt_detect.o SHA256
68194346f1cab5f6cac51922ed87354f4bdcb56e97a96c919e0fbed72af1b7a4;
wmt_drv.ko 7ea236bb4cff3e9e723fb1d5de5eaf485107c5b64c0062e83cb0357211d2884d;
Module.symvers segue 230395d0d7450136aed7ab84d5a63f433feaa7ffbc2aad91c8e7eb28e4f066f3.

Limites: cdev ainda e publicado antes de class/device e nao tem gate de
admissao/drenagem para descritores concorrentes com erro init/exit. O teste
valida ownership das aquisicoes, nao essa concorrencia. sdio_detect_exit
limpa g_func antes de unregister e probe pode ignorar enable_func falho;
teardown/probe SDIO ainda exigem correcoes. WMT_init interno ignora retornos
HIF/STP e publica estado cedo; proxima etapa e seu unwind/serializacao.
WMT_exit nao iniciado retorna sem efeito, mas nao e aceite de cleanup ativo.
Recuperacao/remove WMT/BTIF continua bloqueando carga. Nenhuma carga,
flash ou nova funcionalidade comprovada no aparelho nesta etapa.

### K40s nativo: perfil de hardware explicito, sem PM SDIO de COMBO externo

Entrega pretendida: carregar futuramente WMT do K40s com caminho SoC/BTIF
real, sem tratar eMMC/cartao SD como alimentacao Wi-Fi. Aceite offline:
perfil nativo identificado antes de init; chipset 0x6765/BTIF aceitos;
chipset externo/HIF SDIO ou UART nao integrado recusados antes de publicar
estado; pedido SDIO HW retorna EOPNOTSUPP sem tocar status/host/PM. Caminho
COMBO legado continua no fonte e na compilacao sem o perfil K40s. Sem carga.

Evidencia LG: arch/arm/boot/dts/cust_mt6765_msdc.dtsi define msdc0 como
MSDC_EMMC e msdc1 como MSDC_SD, ambos okay, msdc2/3 status disable. Include
lge/mt6762-mmh55lm/mt6762-mmh55lm-common.dtsi somente troca CD do msdc1
para GPIO80; nao configura SDIO Wi-Fi. Plataforma MT6765 retorna
PLATFORM_SOC_CHIP=0x6765; wmt_ic_soc.c seleciona MTKSTP_BTIF_FULL_MODE.
Wi-Fi SoC usa mtk_wcn_wlan_probe/remove; so WMT_CHIP_TYPE_COMBO chama
WMT_CTRL_SDIO_FUNC. Core liga slot SDIO quando HIF SDIO ou UART legado,
nao no BTIF integrado. Faltava expressar essa selecao de placa no build.

Reuso: perfil de build existente Makefile (MIT) e admissao LG GPLv2-only,
sem novo driver/framework de PM. Mainline Linux 6.18.58 revisao
2926d88bb7fc4608fd942453d929c39e4e5ec006 usa MMC host/pwrseq/regulators,
nao callbacks mt_sdio_ops PM_EVENT_USER_RESUME/SUSPEND do MSDC LG. Criar
esses callbacks para host inexistente no K40s nao atende o aparelho.
Triagem pmaports/MediaTek/Qualcomm anterior nao comprova outro backend de
power desse hardware. DT LG e backend SoC completos sao evidencia para
adiar COMBO externo, conforme diretriz de nao generalizar a outros aparelhos.

Decisao: opt-in WMT_K40S_NATIVE_PROFILE no Makefile de staging, com root
identity K40s de laboratorio obrigatoria. Conservar corpos COMBO antigos sob
selecao de perfil, HIF SDIO nativo inteiro e UART no fonte, sem globals ou
callbacks de fachada, nenhum retorno de sucesso para operacao nao integrada.
Nao afirmar suporte externo SDIO/PM ou UART fisico nesse perfil. Validar
profile on/off em C; caminho legado sem opt-in deve manter efeitos anteriores.
Eliminar dependencias inaplicaveis e consequencia dessa selecao de hardware,
nao aceite funcional do radio. Wi-Fi/BT reais e recuperacao continuam exigidos.

Falhas a corrigir na fronteira: ioctl publica chipid antes de validar tipo;
HIF set muda transporte antes de detectar FM invalido; ctrl SDIO marca bit
on antes de backend, e opfunc retorna0/marca off mesmo apos falha. Perfil
recusa SDIO antes dos bits; opfunc deve propagar erro sem inventar estado.
Somente admissao/preservacao de estado nesta etapa, nao API de power nova.

Resultado: wmt-k40s-native-hardware-profile-v1.patch aplicado ao staging;
fonte generica de PM COMBO preservada sob !WMT_K40S_NATIVE_PROFILE, e
combinacao de perfil com MTK_WCN_COMBO_CHIP_SUPPORT provoca #error. Makefile
MIT seleciona explicitamente opt-in. Detect init confere compatible raiz
lge,mmh55lm-memory-draft antes de sdio_detect_init/cdev. Seletor admite
somente 0x6765, inclusive recusa -1; ioctl agora valida antes de publicar
chipid. HIF valida BTIF e strap FM antes de qualquer mutacao/callback.
ctrl SDIO valida slot e recusa antes de bits; board_sdio_ctrl recusa com
erro explicito. opfunc_sdio_ctrl propaga errno/retorno nonzero e preserva
estado anterior quando backend falha; sucesso mantem comportamento LG.

Testes test_wmt_native_profile.py passaram em
work/wmt-native-profile-host-20261028-e.log, com -Werror/ASan+UBSan.
Compilam funcoes reais de chip selector, HIF, ctrl SDIO, opfunc e corpos PM
legados em dois executaveis, perfil nativo e sem perfil. Percorrem 16 modos
HIF x 16 straps, somente BTIF+FM validos alteram configuracao; recusa deixa
struct/callbacks intactos. Chip externo/-1/invalido nao troca tipo;
SDIO1/2 on/off retorna EOPNOTSUPP sem bits/platform/PM; backend opfunc com
EIO/ETIMEDOUT/EOPNOTSUPP/nonzero positivo preserva estado e propaga retorno.
Sem perfil, COMBO e HIF UART/SDIO/BTIF aceitos, PM conserva trace off-on
SDDRW e off wSD, incluindo sentinela IRQ ausente. Nao e teste fisico.
Assercoes de fonte conferem ordem init antes de SDIO e ioctl antes de
publicacao; nao executam init/char-device real. Constantes HIF/FM/state e
STP IF do modelo sao conferidas contra headers LG. Roundtrip do patch com
fuzz=0 conserva bytes dos seis arquivos. Tentativa inicial do patch pegou
forward declaration de opfunc; dry-run recusou e foi corrigido para corpo.
Harness corrigiu logs para consumir parametros e trace esperado off-on;
nenhum teste/protecao foi desativado para aceitar resultado.

Build ARM32 -Werror e modpost contra exports reais passaram, sem warnings
transformados em sucesso, em work/wmt-k40s-native-profile-build-20261028-b.log
(exit 0). Aviso de build/Module.symvers ausente continua; vmlinux.symvers e
BTIF/Module.symvers foram explicitamente fornecidos em KBUILD_EXTRA_SYMBOLS.
Nao usado KBUILD_MODPOST_WARN, exports artificiais ou callbacks dummy.
Primeiro wmt_drv.ko desse perfil com link completo: SHA256
0c70d3cc36f20c2a59b9238dbcd40a0d370eef01d6f3d32b9f7d2cc8a287bf31;
wmt_drv.o 3fb3a408730e427da14fa0344ffced4e7cd6f2167fe8fa44b1ef1f6987b06810;
Module.symvers 230395d0d7450136aed7ab84d5a63f433feaa7ffbc2aad91c8e7eb28e4f066f3.
modinfo depende de lg_btif, vermagic
6.18.58-k40s-nativeusbemmc1-NOT-FOR-FLASH SMP mod_unload ARMv7 p2v8.
nm nao referencia os quatro simbolos PM COMBO nem adapters XO/GPIO antigos.

Fontes finais SHA256: Makefile
ddd2a948db1dd947bf3865e3bc896d13ad243d82771cd7c1af02da88bf5700df;
mtk_wcn_stub_alps.c 37fd5c0c4802db51a1dec7945eff4793c87e5acc4d4a4adb280f870db5018be9;
wmt_detect.c 7d982e69aefa96710265385ba69d42b42dff127264b1f1ed763da841e82bb93f;
wmt_lib.c a633683e61a8bde9cc96c0c008e30e714777d81327562abb0cfaafed9b79983e;
wmt_ctrl.c 56f2101d0ebe289e6648b46c3dd8e0a999551b67a985533f38ebe03087199212;
wmt_core.c c17422bf28c3e1fd74192918450a9e9c53b9e4901a806d2bbcce6ccc9979b74e.
DT cust_mt6765_msdc.dtsi SHA256
a6545f450ff009f56086c4c70254347ecd0e641af11be5cea6033874e984b9fc;
mmh55lm-common.dtsi 3ac0d3eee3b34d1a44cb8709b40b81551c70adf625322f85555227a7104447a5.

Limites/decisao de carga: link completo nao autoriza insmod. SDIO-detect/HIF
ainda compilados, aliases SDIO permanecem; nao afirmar suporte COMBO externo
ou PM SDIO. Identidade root e politica de perfil nao provam placa fisica.
Init detect ainda ignora falha de sdio_detect_init e tem unwind parcial de
cdev/class; init interno WMT e cleanup precisam verificacao antes de carga.
Remocao WMT/BTIF sob DMA fault, referencias de consumidores, callbacks e
recuperacao ainda sao gates; BTIF remove void nao pode vetar devres. Firmware
radio e consumer WLAN tambem nao foram executados. Proxima entrega: unwind
deterministico do init antes de preparar ensaio temporario autorizado.
Nenhuma carga, novo boot image, flash ou funcionalidade radio no aparelho.

### SDIO IRQ: ownership por funcao no MMC nativo, sem contador EIRQ LG

Entrega pretendida no aparelho: claim/release SDIO usa ownership do MMC
nativo, sem manter contador global de EIRQ de outro host. Aceite offline:
claims de duas funcoes independentes, falhas de CMD52/IRQ get e release,
handler e referencia nativos preservados; STP nao permanece marcado on se
claim falhar. PM/alimentacao nao incluidos, sem acesso fisico ou carga.

Reuso: Linux 6.18.58 revisao 2926d88bb7fc4608fd942453d929c39e4e5ec006,
drivers/mmc/core/sdio_irq.c GPL-2.0-or-later e host/mtk-sd.c GPL-2.0-only;
LG hif_sdio.c e
wmt_build_in_adapter.c GPLv2-only, MSDC ComboA MT6765. Mainline e caminho
mais completo para host nativo: sdio_claim_irq configura IENx e handler,
sdio_card_irq_get conta host por card, release retira handler/referencia e
IENx; MTK nativo usa enable_sdio_irq/ack_sdio_irq e ativa NOTHREAD quando
MMC_CAP_SDIO_IRQ, nao mt_sdio_ops/contador adapter. Triagem pmaports anterior
reusa esse MMC; Qualcomm host diferente nao substitui MT6765. Nao adicionar
novo protocolo de IRQ ou retomar gambiarras weak/stubs de adapter LG.

No LG, mt_sdio_ops[3] e atribuido pelo msdc_cust.c sob CFG_DEV_MSDC3 e
MSDC_EXT_SDIO_IRQ. Adapter usa sdio_claim_irq_enable_flag apenas para filtrar
EIRQ externo antes de chamar host LG. Contador HIF atual e independente
de sucesso do claim, ainda decrementado em varios caminhos e resetado em
init/exit. Nenhum MMC nativo consulta esse estado. Adaptacao: retirar somente
essa contabilidade e chamadas do HIF, preservando sdio_claim/release_irq
reais e gate sdio_irq_enabled do cliente. Nao retirar backend SDIO ou criar
globals de fachada para satisfazer modpost. API/ABI do adapter LG nao e
alterada; patch e para kernel nativo, nao para MSDC/EIRQ LG antigo.

Falha concreta adicional: STP publica on_by_wmt antes de validar func/claim;
em erro, tentativa seguinte recebe already-on. Corrigir retorno para estado
off nos erros anteriores a probe de cliente. Nao afirmar recuperacao de
release falho, callbacks reentrantes, worker concorrente, remove ou PM.

Resultado: wmt-hif-sdio-native-irq-v1.patch aplicado no staging, fuzz=0;
originais LG e MMC nativo intocados. Fonte HIF antes SHA256
9045576ba3f1424ae9b0169c68db6cba8b2886947f37319ea8a7f594d7b23d28;
apos aa62197dbe85e348c706f7b8509032b226fbf7fd5b8bf08eb094bccf573b0350.
Core nativo sdio_irq.c SHA256
fd5785b240e66db8f658eaaedc22cd647535ea305a9179e7f66b9ae2527deabe;
host mtk-sd.c 9ea249225918ac0bc51e90ac326b6d77ad524748d21e258bbfd003eab1961e0b.
Nenhuma API SDIO retirada; contador/gate do cliente sdio_irq_enabled permanece.

Teste test_wmt_sdio_native_irq.py passou em
work/wmt-sdio-native-irq-host-20261028-c.log. Compila get/put/single_irq/
claim/release reais do MMC e STP/WiFi on/off reais do HIF com -Werror,
ASan+UBSan, doubles CMD52/host/thread/client. Duas funcoes compartilham host
com uma ativacao e ultima desativacao; IENx de uma funcao nao apaga outra;
single_irq acompanha ultimo consumidor; claim duplicado nao incrementa ref.
Falhas de leitura/escrita CMD52 preservam errno, nao chamam probe; STP volta
a off e pode tentar novamente. Retorno get/thread ENOMEM limpa handler/ref
mas IENx fica programado, exatamente como core real; retry bem-sucedido e
close confirmam caminho normal, nao recuperacao eletrica. Falha do cliente
faz release; erros de CMD52 durante release retornam EIO com handler/ref
retirados, sem afirmar que bit de card foi limpo. Card removido e cliente
nao registrado nao deixam on_by_wmt indevido.

Comparacao executa STP-on anterior real com mesmo MMC: claim falho deixava
on_by_wmt e contador/gate LG ativos e segunda tentativa retornava already-on.
Patch corrigido nao deixa esse estado. Fixture reverse/reapply fuzz=0 confirma
hash anterior e bytes finais. Tentativas a/b do harness recusaram extracao
que pegava forward declaration e macro CLTCTX que descartava parametros;
corrigidos extrator e double de contexto sem relaxar warnings ou sanitizers.

ARM32 -Werror recompilou HIF e LD wmt_drv.o. Modpost contra exports reais
continua falhando, agora com quatro simbolos de PM/EIRQ legado:
wmt_export_mtk_wcn_cmb_sdio_disable_eirq, wifi_irq,
mtk_wcn_cmb_sdio_pm_cb, mtk_wcn_cmb_sdio_pm_data. Log
work/wmt-sdio-native-irq-modpost-20261028-a.log, make exit 1; sem
KBUILD_MODPOST_WARN ou symbol stub. hif_sdio.o SHA256
016a3818bfe7725621bee614ac1854c1e246558c95e70f28807c95d7254776c8;
wmt_drv.o 77e1e5c2e656d28477f2ebfed907316b48ad98afe692ac611bc72f79fd467cc3.
Nao recompilar kernel inteiro: fonte nativa/exports nao mudaram.

Limites: teste nao executa IRQ, threads MMC, CMD52 ou host reais. Caminho
registro tardio ainda agenda worker antes de conferir claim; remove HIF e
clientes podem correr com outras APIs. Release dentro de callback so e
compativel com NOTHREAD desse host; outro host com ksdioirqd pode esperar
a si mesmo. Politica de erro/recuperacao e serializacao desses caminhos
permanecem gates antes de carga. PM legado tenta desligar EIRQ e invocar
callback externo, sem equivalente demonstrado no MMC atual; proxima etapa
deve localizar host/perfil real, nao atribuir callback dummy ou fake success.
Nenhum WMT .ko aprovado, nova funcionalidade comprovada no aparelho, carga
ou flash nesta etapa.

### GPIO STEP: reaproveitar leitura do pinctrl MT6765 nativo

Entrega pretendida no aparelho: acao GPIO de STEP mostra o pino pedido sem
alterar mux/direcao/pull e retorna erro quando nao pode le-lo. Aceite offline:
formatter upstream chamado uma vez para pin unico; recursos/ref/lock liberados
em todas as saidas; ausente/unbound/ocupado/atomic e erro do formatter nao
viram sucesso nem executam callback extra. Nenhuma operacao fisica.

Reuso: Linux 6.18.58 revisao 2926d88bb7fc4608fd942453d929c39e4e5ec006,
drivers/pinctrl/mediatek/pinctrl-paris.c e .h GPL-2.0. mtk_pctrl_show_one_pin
ja EXPORT_SYMBOL_GPL e presente no kernel atual PINCTRL_MT6765=y; le MODE,
DIR/DO/DI, drive, SMT/IES e bias pelos campos do descritor nativo MT6765.
LG GPLv2-only gpio_dump_regs_range chama versao ancestral do mesmo formatter,
mas usa loop i<end: pedido start=end de STEP nao imprime nenhum pino.
Nao preservar esse falso sucesso. gpiolib get_value/direction sozinho nao
mostra mux/drive/pulls e requisitar o GPIO para diagnosticar poderia alterar
ownership. Pmaports usa framework upstream ja triado; nenhum adapter legado
confirmado. Qualcomm pinctrl tem hardware distinto, nao e substituto.

Adaptar backend LG existente common_detect/wmt_gpio.c e header GPLv2-only;
STEP continua generico, chamando backend int em vez de wrapper void. Pequeno
header privado de compatibilidade declara somente prototype exportado atual
e tipo opaco, sem copiar layout interno ou algoritmo de formatter. Nao criar
driver/export novo, scanner ou mapa MMIO paralelo. Lookup somente compatible
mt6765-pinctrl; ref do platform device e device_trylock protegem estado do
provider durante leitura. Recusar atomic/IRQ antes de lookup; trylock evita
esperar lock de driver em diagnostico disparado por outro contexto. Sem nova
DT, configuracao de pin ou fallback que simule suporte.

Resultado: wmt-gpio-native-pinctrl-v1.patch aplicado ao staging sem tocar
originais LG ou pinctrl nativo. Formatter Paris SHA256
94848be20fd43e443398b5975829534ef95fa1f2df9cd1f835939616b0643502;
prototype do header privado confere byte a byte com declaracao nativa.
mtk_hw_get_value le campos, bias_get_combo chama getters; nao adicionar
request/select/set de GPIO. Fonte anterior wmt_gpio.c
be286b3134b36f9378842abf40241a6cf9ece07bd7e93dd46087f375ab95ef71;
final e5bc178f6cf9bc5697565c84a0c4bcb3e64dbb7f1a983dec422497641696546c.
wmt_step.c anterior 11e41f54798e2305840c621d80daeaf81ef6f6804f09bf1b0e2e8210e750658a;
final ab393780ca3109c3e0b5b55127dfec88db98c9ced49ffa14af368e1f8c2bb197.
wmt_gpio.h final b24f908dab06f9aabae18d48e7f36e12fb8ab44c3f627cc9014740dee9bcd285;
mtk_pinctrl_native.h 61e105eba771ad744f7c1f7d708bb3e807838aab58df19770ea1a5f0d083cc49.

Teste test_wmt_gpio_native.py passou em
work/wmt-gpio-native-host-20261028-a.log: compila backend e acao STEP reais
fixados por SHA com -Werror, ASan+UBSan/pthreads. Pin unico chama formatter
uma vez; escrita continua recusada; atomic/IRQs recusam antes de lookup;
provider ausente/unbound/driver incorreto/sem drvdata e lock ocupado retornam
erro sem formatter ou callback extra; EINVAL/EIO/erro delegado e comprimento
invalido propagam, com refs/lock liberados. Reader pausado mantem lock/ref;
unbind simulado espera e nova leitura recebe EBUSY; apos unbind recebe
ENODEV; callback extra so apos sucesso e fora do lock. Patch revertido e
reaplicado fuzz=0 em copia temporaria, com bytes finais identicos.

Build ARM32 -Werror recompilou objetos afetados e ligou wmt_drv.o em
work/wmt-gpio-native-modpost-20261028-a.log. Modpost real contra
vmlinux.symvers/BTIF Module.symvers agora recusa apenas cinco simbolos SDIO:
wmt_export_mtk_wcn_sdio_irq_flag_set,
wmt_export_mtk_wcn_cmb_sdio_disable_eirq, wifi_irq,
mtk_wcn_cmb_sdio_pm_cb e mtk_wcn_cmb_sdio_pm_data. Rechecagem so de modpost
em work/wmt-gpio-native-modpost-20261028-b.log retorna exit 1; comando a
incluia hashes apos make e seu exit externo 0 nao equivale a build aprovado.
Sem KBUILD_MODPOST_WARN. mtk_pctrl_show_one_pin e EXPORT_SYMBOL_GPL real
do vmlinux; nenhum stub/novo export, nem nova recompilacao ampla de kernel.
Objetos SHA256: wmt_gpio.o
4c7aa2ea90fb2dc9bd3a678f0218f7245c19e1a40f85bffbd9e275ef087c5cd7;
wmt_step.o 5def7835c0987ebd652d498d8d6d2cfaf24006ecbb26091cb36c4f499fc34428;
wmt_drv.o 27674ccae1d039aa94f6d1d75d07d7fc02376e3a5d94f734d80d610b44c14c1a.

Limites: teste nao executa formatter/MMIO/pinctrl/driver core Linux reais.
Formatter upstream pode mostrar errno em campo nao suportado e ignora alguns
erros de bias; comprimento positivo nao certifica todos os campos validos.
Snapshot nao e atomico entre campos nem mede sinal eletrico. Device trylock
impede unbind local durante leitura, nao substitui lifecycle WMT/BTIF ainda
pendente. Contextos inseguros retornam erro explicito; dispatcher STEP LG
ignora retorno da acao mas ela registra falha e nao chama extra. Nao ha
WMT .ko aprovado ou funcionamento no aparelho. Proximo bloqueio de link:
SDIO legado exige integracao MMC real, nao globais de fachada. Sem carga/flash.

### XO: readback pelo PWRAP existente e erro propagado ao WMT

Entrega pretendida no aparelho: WMT usa automacao CONN herdada do preloader
apenas se o provider confirmar o contrato MT6765/MT6357, preservando NFC.
Aceite offline: nenhuma escrita DCXO/CW00 ou novo ioremap; falhas de leitura,
identidade, INIT_DONE, tabela PWRAP, modo XO e BBLPM recusadas antes do power
seguinte; caminho de sucesso LG continua sem gate manual. Sem carga/flash.

Reuso: PWRAP/regmap/device_link Linux 6.18.58 revisao
2926d88bb7fc4608fd942453d929c39e4e5ec006 (GPL-2.0-only); fonte LG MT6765
mtk_clkbuf_hw.c SHA256 6021b7cb5395394318989bd8e166ac8015039731d64cf2dabdf1bea2ef59f2b1,
GPLv2-only, valores e campos confirmados no upmu_hw.h MT6765 e registers.h
MT6357 upstream. Mainline/pmaports/MediaTek/Qualcomm ja triados: nao ha
provider XO MT6357 confirmado; clkbuf de outros PMICs/CCF gate nao substitui
handshake. Evidencia historica PL e limitacoes estao na secao seguinte.

Adaptacao pequena no proprietario de MMIO PWRAP, com API de validacao
regmap e header Linux, somente sob opt-in K40S existente. Nao mapear wrapper
de novo no WMT. Callback MT6765 passa a usar esse retorno int, sem alterar
ABI void connectivity_export_clk_buf_ctrl LG nem fingir bool dessa API.
Reguladores e device link gerenciado ao PWRAP sao adquiridos no probe antes
da publicacao do consumidor; ponteiros limpos antes de devres. Nenhum novo
protocolo, controle BBLPM ou variante de outro aparelho.

Equivalencia pretendida: LG clk_buf_ctrl(CONN) apenas registra pedido para
politica BBLPM, nao comuta gate fisico nesse perfil. Sem provider BBLPM
nativo, validar BBLPM desativado e modo XO2=3/CLKSEL_MAN=0 nas transicoes,
mantendo automacao e sequencia de power LG. Registro de usuarios BBLPM e
otimizacao suspend nao sao implementados nem declarados equivalentes.
Recuperacao PWRAP existente permanece obrigatoria; falha nao e reparada.

Integrado no staging: mtk-pwrap-k40s-xo-readback-v1.patch estende driver
PWRAP e adiciona include/linux/soc/mediatek/mtk-pmic-wrap.h GPL-2.0-only;
wmt-mt6765-xo-readback-v1.patch adapta somente mt6765.c LG GPLv2-only.
API int mtk_pwrap_mt6357_xo_validate aceita regmap vivo do provider, exige
MT6765/MT6357 e flag de handoff publicada somente apos politica K40S aceita.
Confere INIT_DONE2/WACS2, EN CONN+NFC e oito palavras de automacao. Le
SWCID/CW00/CW14 por regmap nativo sem cache (config16 nao define cache),
sem exigir valor fixo de SRCLKEN_IN3 que muda com automacao. EN alheios e
bits PMIC nao relacionados nao sao alterados nem usados para recusa.

WMT probe adquire link DL_FLAG_AUTOREMOVE_CONSUMER ao supplier do regmap,
valida antes de publicar reguladores/map, e limpa map junto aos ponteiros
antes de devres. Link gerenciado usa ordenacao do driver core, nao novo
mutex global nem device_lock sob mutex de power; nao prova remove sob fault.
Callback valida tanto pedido on quanto off, propagando errno exato. Header
retorna -EOPNOTSUPP quando provider/opt-in nao sao alcancaveis, nao sucesso.

Teste tools/tests/test_wmt_xo_readback.py compila provider, acquire, clear e
callback reais fixados por SHA, com ASan+UBSan e doubles de MMIO/regmap/
device_link/devres. Passou em work/wmt-xo-readback-host-20261028-c.log:
contrato PL aceito sem mutacao de memoria de MMIO; ausencia/map ERR_PTR,
identidade/supplier/tipo/handoff invalidos; INIT_DONE ausente; cada palavra
de automacao incorreta e EN incompleto; erro exato em cada leitura PMIC;
SWCID errado, modos XO2 0/1/2, BBLPM/CLKSEL_MAN ativos; bits nao relacionados;
probe falho antes de publicar, falha de link/action, sucesso/reprobe e callback
apos clear recusado. Teste faz reverse/reapply fuzz=0 em copias temporarias
dos dois patches e confere bytes exatos. Nao testa kernel device_link/regmap
ou hardware reais. Primeira tentativa do harness recusou parametro data
nao usado de callback LG; flags host alinharam -Wno-unused-parameter com
fixtures existentes, mantendo erros C restantes e sanitizers obrigatorios.

Regressao de erro do core/VCN28 passou em
work/wmt-xo-core-gates-host-20261028-a.log, sem ampliar suite. Confirma que
erro de XO impede os passos seguintes do reg_ctrl; nao e WMT em execucao.

Build ARM32 Linux 6.18.58 concluiu vmlinux, exportacao e modpost nativo com
KCFLAGS=-Werror em work/pwrap-xo-readback-build-20261028-a.log (exit 0).
A flag adicional provocou recompilacao ampla, nao apenas do PWRAP; nao
repetir esse custo para alteracoes sem dependencia. vmlinux SHA256
85be3789cc8d760f4dce559069302e09148d34f8e32e86a8641bcbff7a4ee22e;
vmlinux.symvers 064ba198273392e633bd7cade0bc545dcfbbd5d4cadf6fca784b7c22e0ac60f1;
mtk-pmic-wrap.o e2b004c17ff41ec755a3a342cd049215908c2f7fe1d71175b36c5088e9df0eba.
Nova API aparece como EXPORT_SYMBOL_GPL no vmlinux.symvers real.
Fonte PWRAP SHA256 76829d48977f8d075f0dd33a94c1169a2a43e92533cd4da1ed0c5dc50bb666df;
fonte mt6765.c 5024674208d7e4f5832df7019caee7cadf43bdc3560804d58b2fd765f65216d2.

WMT backend e composite compilaram ARM32 com -Werror, logs
work/wmt-xo-readback-object-20261028-a.log e
work/wmt-xo-readback-composite-20261028-a.log. mt6765.o SHA256
44b74ae16e7c84ee57a9e24e270c79ebcb4b9594a2bbbfd9ebfabbfd3c3afdd3;
wmt_drv.o f2eabb789561f63a060f49a975ba596042b4b93b9d23857aba7fcfedd38fd529.
Modpost WMT contra vmlinux.symvers real novo e BTIF/Module.symvers resolveu
XO, sem KBUILD_MODPOST_WARN ou symbols artificiais. Ainda falha com seis:
connectivity_export_dump_gpio_info, wmt_export_mtk_wcn_sdio_irq_flag_set,
wmt_export_mtk_wcn_cmb_sdio_disable_eirq, wifi_irq,
mtk_wcn_cmb_sdio_pm_cb e mtk_wcn_cmb_sdio_pm_data. Evidencia:
work/wmt-xo-readback-modpost-20261028-a.log; make terminou com erro,
nao ha WMT .ko novo aprovado. Aviso build/Module.symvers ausente permanece,
com exports fornecidos explicitamente por KBUILD_EXTRA_SYMBOLS.

Resultado funcional ainda offline: validacao de handoff XO integrada e
dependencia antiga void retirada do backend MT6765, nao oscilacao, power-on
ou Wi-Fi/Bluetooth demonstrados. Nao houve carga, flash ou novo boot image.
Proximo bloqueio de link: integrar SDIO legado real/diagnostico GPIO sem
stubs; gates fisicos de recuperacao WMT/BTIF e suspend/BBLPM permanecem.
Device link nao resolve teardown em falha nem consumidor que descumpra
contrato de lifetime; nenhum desses limites foi declarado como recuperado.

### XO: confirmar handoff LK antes de integrar provider nativo

Entrega pretendida: provider XO do K40s preservar automacao CONN e NFC do
bootloader, sem trocar handshake por gate PMIC deduzido. Aceite desta etapa:
confrontar fonte LG, log historico e fluxo estatico do LK rev8; identificar
o que o PWRAP Linux preserva ou reprograma. Nenhum acesso ao aparelho.

Reuso: fonte LG GPLv2-only mtk_clkbuf_hw.c MT6765, SHA256
6021b7cb5395394318989bd8e166ac8015039731d64cf2dabdf1bea2ef59f2b1;
PWRAP Linux 6.18.58 revisao 2926d88bb7fc4608fd942453d929c39e4e5ec006.
Triagem mainline/pmaports/MediaTek/Qualcomm para XO ja registrada abaixo:
nenhum backend MT6357 substituto confirmado. REA 6.5.0 binary_session confirma
Ghidra Windows P0 sem ARM raw; sem reparo/instalacao. Reusar Ghidra 12.1.4
direto e projeto privado existente, readOnly/noanalysis, como auditoria LK A/B.
Isso nao e Evidence REA. Estender filtro do K40sLkAbReport existente para XO,
sem novo scanner/framework; modos A/B e reset preservados. Esforco pequeno,
somente relatorio estatico. Nao alterar fonte LK nem executar seu codigo.

Alvo confirmado: work/backup-installed-rev8-20261019-061044/lk_a.bin,
SHA256 973bd9ad54a53b1c4c8e9595260c0e908dabd1fa9637041f4e297a441dcaed91.
O caminho revision7-btm do scanner antigo nao existe; nao usar como alvo.
Log artifacts/lk-log-20261022.txt linhas 158..163 observa status PMIC
2/1/1/2/0/0/0, CONN ADR0/WDATA0/ADR1/WDATA1=0x44a/0/0x44a/1,
NFC=0x78c/0x100/0x78a/0x100 e EN=3. Isso coincide com ramo LG sem
CLKBUF_CONN_SUPPORT_CTRL_FROM_I1, mas e historico, nao readback atual nem
prova de preservacao pelo kernel nativo.

Resultado: script compilou/executou em projeto readOnly/noanalysis, log
work/ghidra-lk-rev8-v1/xo-headless-v1.log; terminou com exit 0. Relatorio
xo-handoff-v1.txt no mesmo diretorio, SHA256
e7210c0098ededf9e42ae5027957a53ec26cce966ccddb97289334b238a177fb,
confirma hash do alvo, ARM:LE:32:v7 e 2195 funcoes da analise anterior.
Filtro ASCII clk_buf/dcxo/srclken encontrou somente
PMIC_AUXADC_MDRT_DET_SRCLKEN_IND no offset 0x8b844/address 0x4808b644,
sem xref reconhecida. Nao produziu funcao de inicializacao XO decompilada;
nao inferir ausencia de codigo de uma busca negativa de strings.

Correcao de proveniencia: artifacts/lk-log-20261022.txt contem PL e LK
concatenados (cabecalho explicito pl size/lk size). O bloco XO linhas 158..163
precede [BLDR] jump to 0x48000000, linha 365. Portanto o registro e do
preloader, nao do LK. SHA256 do log
ff08a373618bb41e33f2bdca71fc8173351658b93bc4789ec43ad9c4371647b1.
Nao procurar a inicializacao apenas no LK nem atribuir implementacao a ele.

Fonte PWRAP staging atual SHA256
0fa348738753cde57ff0b9c095c1fbcd9077c49f8441f92631db17f5b301b367:
CONFIG_MTK_PMIC_WRAP_K40S_HANDOFF=y na build atual. Para MT6765, probe
chama k40s_pwrap_handoff e salta a k40s_handoff_done antes de DCM/init/WDT/
timer/INT_EN; handoff le INIT_DONE2/WACS2_RDATA e recusa estado invalido.
Isso demonstra preservacao pela fonte do probe nesse perfil, nao readback
atual dos registradores XO nem garantia contra outros consumidores depois.

Decisao: proxima implementacao XO deve validar o contrato herdado de
preloader no provider proprietario PWRAP/PMIC, mantendo CONN e NFC, antes
de admitir WMT. Nao reprogramar CW00/DCXO global para compensar uma
reinicializacao que esse perfil nem executa; nao substituir por gate CCF.
Ainda faltam readback validado no backend, politica de suspend/BBLPM e
propagacao do resultado bool LG que o adapter void descarta. Nao houve
mudanca de driver/modulo, ensaio no aparelho ou nova compilacao de kernel:
esta etapa fechou proveniencia e caminho de preservacao, nao o provider XO.

BTIF remove: fonte LG tem DMA_HARD_RST apenas definido e comentado no
init, sem sequencia de recuperacao confirmada. APDMA upstream confirma
FLUSH/STOP/EN, mas nao prova reset BTIF compartilhado seguro. Nao liberar
devres apos timeout nem mascarar o problema com clock off; gate de carga
permanece. Controles legados SDIO possuem implementacao real no adapter LG,
mas dependem de integracao MMC e lifetime ainda nao portados; nao adicionar
globais/stubs so para resolver os cinco simbolos SDIO restantes.

### BTIF: ownership unico entre WMT, cdev e controles de teste

Entrega pretendida no aparelho: cdev/sysfs nao fecham, mudam modo ou substituem
notify de canal WMT em uso. Aceite offline: dono serializado por ops_mtx;
OPEN de outro dono falha sem hardware/notify; close apenas do dono; cdev
associado ao file que abriu sessao; release tenta close e, na falha, retém
ownership sem ponteiro de file liberado; DMA mode so muda fechado; sysfs
nao entra sobre WMT/cdev. Sem carga ou flash nesta etapa.

Reuso: ops_mtx/enable/lista LG e core open/close existentes, primitivas Linux
6.18.58 (revisao 2926d88bb7fc4608fd942453d929c39e4e5ec006). Triagem anterior
mainline/pmaports/MediaTek/Qualcomm nao confirma substituto BTIF. Adaptar
mtk_btif.c, mtk_btif_exp.c e inc/mtk_btif.h LG GPLv2-only, sem sessao paralela
de hardware ou novo framework. Enum de dono e file pointer somente enquanto
descritor vivo, protegidos pelo mutex ja existente. Public API continua com
seu ID/gates SRCU; cdev mantem ABI ioctl e chama core existente sob ownership.

Codigo novo justificado: evitar falso sucesso E_BTIF_ALREADY_OPEN no cdev,
que antes instalava notify mesmo apos open de outro consumidor; arbitrar
ioctls/testes e API open pelo mesmo estado. Quarentena de release falho nao
afirma recuperacao; bloqueia novo dono ate mecanismo de recuperacao real.
Modo DMA/PIO muda somente sem enable/fault/dono; isso preserva configuracao
de teste valida sem trocar flags que determinam teardown de DMA ainda ativa.
Helpers test no-id so publicados por sysfs local, nao EXPORT_SYMBOL; wrapper
sysfs toma ops e rejeita dono WMT/cdev. Contexto callback nao toma novo mutex;
esperas/IRQ/DMA continuam nas funcoes LG ja auditadas.

Limites: recuperacao fault/remove, callback reentrante em controles sincronos,
poll de descritor sem sessao e ownership de todos os testes alternativos ainda
precisam verificacao antes de carga. Nao desabilitar controles para obter link
nem alterar protecoes/checagens; operacao que conflita retorna erro explicito.

Resultado: btif-control-owner-v1.patch e btif-owner-mode-errors-v1.patch
aplicados ao staging isolado, sem alterar originais LG. Teste de ida/volta
reverte ambos na ordem inversa e reaplica com fuzz=0 em copia temporaria,
confirmando bytes identicos em core/API/header. Build ARM32 Linux 6.18.58
com -Werror e modpost contra exports reais passou em
work/btif-lts-control-owner-20261028-d.log; nao usado KBUILD_MODPOST_WARN.
O aviso de build/Module.symvers ausente persiste: exports fornecidos por
KBUILD_EXTRA_SYMBOLS=vmlinux.symvers. lg_btif.ko SHA256
a03595faee8fe508c9f602b56fc55bffd0711254d98ad5d41be7fd2aaa562a9d;
Module.symvers segue 516b10f53e2e18d7caeeddbec72e0d43a9259d32cec6bf9f6ac95e8dbb01ac14.
Fontes finais: mtk_btif.c
70bf828ab3c69b9e0a282f021a881e20384d96a0ee1041e605d9e1cc6a18d1a0,
mtk_btif_exp.c bde9e8cf76cd10b3e6d3b9bf5231f2a416a3289188434b56406dc2e6f4312180,
inc/mtk_btif.h ba47899078b79ebaa4307d8bc17111dacec07613210750fc2f0751fa642482c9.

Teste test_btif_control_owner.py compila controles reais extraidos da fonte
fixada por SHA, com ASan+UBSan/pthreads e doubles de hardware/lifetime.
Passou em work/btif-control-owner-host-20261028-c.log: WMT bloqueia cdev e
sysfs sem chamar hardware; cdev exige mesmo file; API WMT e dois descritores
nao tomam sessao alheia; corrida OPEN WMT/cdev admite uma unica abertura;
release errado nao fecha hardware; close falho mantem owner e remove ponteiro
de file; fault rejeita controles; modo ativo nao muda; modo fechado permanece
configuravel. Quarentena e reiniciada apenas pela fixture, nao e recuperacao.

Regressoes afetadas passaram: membership (...membership-host-20261028-d.log),
session close (...session-close-host-20261028-c.log), API SRCU
(...api-srcu-drain-host-20261028-h.log), cdev
(...cdev-disconnect-host-20261028-c.log) e callback RX
(...rx-callback-drain-host-20261028-b.log), todos com prefixo work/btif-.
A regressao membership detectou retorno indevido -EBUSY no segundo close;
corrigido para preservar E_BTIF_INVAL_PARAM quando nao ha dono. -EBUSY
continua reservado a conflito com outro dono, sem relaxar verificacoes.

Limite de aceite: nenhum IRQ/DMA ou uso WMT no aparelho foi executado.
Release em fault ainda fica em quarentena sem recuperacao. Remove ativo/fault
continua inseguro: callback void nao pode impedir liberacao devres retornando
erro. Proxima entrega necessaria e quiescencia/recuperacao antes de liberar
recursos; tambem faltam referencias de usuarios vivos, poll sem sessao e
auditoria dos controles alternativos. Sete simbolos WMT ainda indefinidos;
nao ha WMT .ko aprovado, carga ou flash nesta etapa.

### BTIF: callback RX retirado e drenado antes de close

Entrega pretendida no aparelho: consumidor RX nao chama callback ja retirado
ou usa estado externo liberado depois de unregister/close. Aceite offline:
dispatch usa snapshot com lifetime SRCU, unregister espera callback antigo,
close bloqueia novos registros e despublica callbacks antes de esperar, sem
state_mtx durante a espera; pacote circular mantem mesmo callback nas duas
partes; notify segue protegido; close falho nao readmite callback por acidente.
Sem carga, flash ou ensaio fisico autorizado nesta etapa.

Reuso: SRCU/RCU/mutex Linux 6.18.58 ja auditados, revisao
2926d88bb7fc4608fd942453d929c39e4e5ec006. Triagem mainline/pmaports/MediaTek/
Qualcomm anterior nao fornece substituto BTIF confirmado. Adaptar dispatch,
registro e close LG GPLv2-only existentes, sem fila/worker/protocolo novo.
Fonte staging anterior mtk_btif.c SHA256
9f996464da5a52304fbb67ed85c0be20be2767c1a3c21edbf7bf8bfdff64d702.
Header mtk_btif.h LG GPLv2-only recebe flag de admissao de callbacks; origens
anteriores abaixo. Duas primitivas estaticas de callbacks para porta unica
do perfil, nenhuma exportacao nova. Reaproveitar ponteiros e buffer circular.

Codigo novo justificado: snapshot SRCU por batch RX, escritores publicam sob
mutex curto e esperam fora dele; close bloqueia registro/despublica antes de
tomar state_mtx. Falha de close deixa callbacks retirados e nao libera DMA
por inferencia. Novo open bem-sucedido readmite registro, nao restaura ponteiro
antigo. Port_deinit idle drena antes de contextos/buffers. Nao guardar mutex
de registry enquanto chama consumidor nem state_mtx enquanto espera SRCU.

Contrato: registro/unregister/close sao controle em contexto de processo e
nao podem esperar sincronicamente o proprio callback que os invocou. RX
continua executando no contexto escolhido LG; nao habilitar tasklet/RT/debug
alternativos para testar. Gate nao resolve callback retido para sempre pelo
consumidor, cdev concorrente com sessao WMT, workers pendentes ou recuperacao
de remove com DMA fault. Esses continuam bloqueios antes de carga.

Resultado: btif-rx-callback-drain-v1.patch aplicado/reverse dry-run fuzz=0.
Build ARM32 passou com -Werror e modpost contra vmlinux.symvers real em
work/btif-lts-rx-callback-drain-20261028-a.log. lg_btif.ko SHA256
77faa944b79c9f6f533ee75d920fe9471f182a096948a72917586a951bf786ef;
Module.symvers permanece 516b10f53e2e18d7caeeddbec72e0d43a9259d32cec6bf9f6ac95e8dbb01ac14,
sem exports novos/removidos. Fonte mtk_btif.c SHA256
23286fc546071280c5a49d3de2f30ea3c17a183b5beeb4c33d5b86dc18c3a861;
mtk_btif.h 67c66eb5fcce2363c54774a19a4e8d77a11ddb7403330760346227fbb131b641.

Teste test_btif_rx_callback_drain.py compila registry/start/stop, consumer RX
e core close reais da fonte staging fixada por SHA. ASan+UBSan/pthreads com
SRCU/mutex/hardware doubles passaram em work/btif-rx-callback-drain-host-20261028-a.log:
buffer vazio, linear, wrap e limite final mantem ordem de bytes/rd_idx;
callback pausado antes do wrap mantem snapshot antigo nas duas partes mesmo
quando novo pointer ja publicado; unregister espera antigo e novas batches
nao o chamam; close drena callback e notify antes de hardwarefree; callback
retoma e toma state_mtx sem deadlock durante espera do close; registros novos
recusados enquanto close espera; timeout deixa callbacks retirados e flag
blocked; helper start readmite registro em fixture, nao demonstra recuperacao
fisica apos falha. Assercoes conferem port_deinit drenar antes de parar RX e
novo open readmitir somente depois de enable bem-sucedido.

Regressoes diretamente afetadas passaram com pins de fonte atualizados,
sem remover verificacoes: exports/SRCU em work/btif-api-srcu-drain-host-20261028-f.log
e cdev em work/btif-cdev-disconnect-host-20261028-b.log. Nenhuma suite ampla.
Limites: nao executa kernel SRCU, IRQ/DMA reais ou consumidor WMT inteiro;
callbacks devem terminar e respeitar contrato de nao executar teardown
sincrono de si mesmos. Espera nao segura registry/state, mas close exportado
mantem ops_mtx apos drenagem da sessao; reentrada nas APIs normais nessa fase
e recusada pelo gate da sessao antes do backend. Direct/cdev API que burle
esse contrato ainda exige ownership unificado com WMT. Remove sob fault,
buffers/IRQ residuais e users vivos continuam sem aceite fisico. Sete simbolos
WMT permanecem indefinidos; nenhum modulo carregado, flash ou acesso fisico.

### BTIF: cdev retirado de servico com descritores antigos

Entrega pretendida no aparelho: poll/ioctl de descritor existente deixa de
acessar recursos apos disconnect e nao passa a controlar dispositivo reprobed.
Aceite offline: waitqueue valida antes de ioctl OPEN; poll registra espera
antes de verificar ready; disconnect retira ready/acorda pollers e espera
SRCU; ioctl e sysfs antigos drenam antes de cleanup; novos acessos retornam
-ENODEV ou POLLERR|POLLHUP; cookie por instancia rejeita descritor antigo.
Nenhuma carga fisica/flash ou habilitacao de read/write antigos.

Reuso: file_operations, DECLARE_WAIT_QUEUE_HEAD, poll_wait, wake_up_interruptible
e SRCU Linux 6.18.58 (revisao 2926d88bb7fc4608fd942453d929c39e4e5ec006),
ja presentes no driver LG/API lifetime anterior. Triagem mainline/pmaports/
MediaTek/Qualcomm anterior nao confirma substituto BTIF MT6765; estender
mtk_btif.c LG GPLv2-only existente, sem criar device/protocolo paralelo.
Novo codigo justificado: wrappers curtos de fops/sysfs usando guard existente,
fila estatica (nao reinitializar com pollers inscritos), cookie de geracao
sem alocacao por file, incrementado antes de publicar cdev. Nenhuma mudanca
de ABI ioctl/comandos ou sequencia eletrica. Fonte anterior SHA256
35e3513035ab862782e4df1e59156f371db1fd404d78f0cccdb9e06a1f87ea3a.

Limites: cdev ainda possui comandos diretos que podem concorrer com sessao
WMT, configuracao de modo/testes e callbacks precisam ownership proprio;
esta etapa protege lifetime contra remove, nao autoriza tais comandos.
read/write ativos retornam 0 como LG; branches #if 0 continuam desativados.
Cookie unsigned long nao deve dar wrap durante vida de um descritor; nao e
identificador persistente de hardware. DMA fault/remove continua bloqueio.

Resultado: btif-cdev-disconnect-v1.patch aplicado/reverse dry-run fuzz=0.
Build ARM32 passou com -Werror e modpost contra vmlinux.symvers real em
work/btif-lts-cdev-disconnect-20261028-a.log. lg_btif.ko SHA256
e5bd8b8f08305821db81d78c4859ea29b140599510097239cc1a8b6a11116222;
Module.symvers continua 516b10f53e2e18d7caeeddbec72e0d43a9259d32cec6bf9f6ac95e8dbb01ac14,
sem alterar exports. mtk_btif.c SHA256
9f996464da5a52304fbb67ed85c0be20be2767c1a3c21edbf7bf8bfdff64d702.

btif_read_inq passa a DECLARE_WAIT_QUEUE_HEAD e nao e reinicializada pelo
ioctl OPEN; disconnect fecha ready, acorda essa fila e btif_wq e espera SRCU.
Poll registra antes do gate, retorno desconectado POLLERR|POLLHUP. File open
nao inicializa hardware: associa cookie da instancia sob lifetime; release
somente descarta cookie, sem tocar recursos. Ioctl/compat e sysfs set mantem
retornos/dispatch existentes mas recebem guard de lifetime; compat delega uma
vez ao ioctl protegido. Read/write continuam no comportamento LG #if 0/return0.

Teste test_btif_cdev_disconnect.py fixa fonte staging por SHA e compila os
guards/disconnect/fops/compat/sysfs wrapper reais e o incremento de geracao
extraido do init. Backends de ioctl/poll/sysfs, waitqueue e SRCU sao doubles.
ASan+UBSan/pthreads passaram em work/btif-cdev-disconnect-host-20261028-a.log:
antes de ready open/ioctl/sysfs indisponiveis, poll com erro; instancia valida
preserva retorno/dispatch; disconnect acorda antes de esperar; ioctl pausado
impede retirada de terminar, novas chamadas recusadas; retirada entre registro
poll e check e observada; descritor antigo rejeitado apos novo cookie; release
nao acessa hardware; geracao evita zero no wrap. Teste nao demonstra ausencia
de ABA depois de um ciclo inteiro de unsigned long nem progresso de epoll real.

Regressao de exports/getter com mesmo disconnect passou em
work/btif-api-srcu-drain-host-20261028-e.log; pin atualizado e wake helper
modelado no teste de exports, cujo comportamento e testado no novo teste cdev.
Sem suites amplas repetidas ou alteracao de protecoes. Ainda nao provados:
vfs/kernfs/kernel SRCU reais, cdev contra sessao WMT simultanea, serializacao
dos comandos de modo/log, callback RX ativo e recuperacao de DMA fault/remove.
Esses bloqueios precedem carga. Sete dependencias WMT seguem indefinidas.
Nenhum modulo carregado, DT ativado, flash ou acesso ao aparelho nesta etapa.

### BTIF: admissao por sessao e close depois das operacoes admitidas

Entrega pretendida no aparelho: fechar sessao BTIF sem desligar DMA/IRQ sob
uma operacao de transporte ainda admitida. Aceite offline: ID publicado apos
open; close retira ID antes de esperar leitores SRCU da sessao; rejeita novas
operacoes, aguarda as antigas fora de ops_mtx, depois desliga hardware; erro
retém handle mas sessao permanece fechada para uso; close concorrente nao
executa teardown duas vezes. Sem carga, flash ou ensaio fisico nesta etapa.

Reuso: SRCU Linux 6.18.58 GPL-2.0-or-later e mutex/lista LG ja auditados nas
secoes anteriores. Revisao 2926d88bb7fc4608fd942453d929c39e4e5ec006. SRCU
separado do lifetime de dispositivo porque close e ele mesmo leitor daquele
lifetime; esperar a mesma instancia dentro de close causaria auto-deadlock.
Triagem mainline/pmaports/MediaTek/Qualcomm anterior nao confirma substituto
BTIF; pequena extensao do API layer mtk_btif_exp.c LG GPLv2-only existente,
sem novo transporte/driver/framework. Staging anterior SHA256
8a4f013b47aabb0a5245422be437b4a99e17e663ba9301b845f5165f0573b32c.

Novo codigo justificado: gate por ID da sessao, wrappers das dez operacoes
que dependem de usuario (open/close so usam SRCU do dispositivo), publicacao
release/acquire, flag closing serializada por ops_mtx. Close toma ops, valida
membership, despublica sessao e marca closing, SOLTA ops, synchronize_srcu,
retoma ops e fecha. Assim getter ja admitido pode tomar ops para adquirir ref
da task sem deadlock. Open concorrente ve lista nao vazia; segundo close ve
closing e retorna -EBUSY. Nao limpar handle em timeout nem reabrir gate sem
novo open bem-sucedido. Sem alterar sequencia eletrica de close ja auditada.

Limites: close nao pode ser chamado sincronicamente de dentro de uma operacao
protegida da mesma sessao/callback executado por ela: isso esperaria a si mesmo;
close e API de controle em contexto de processo. Sem nova espera nos callbacks
IRQ. Cdev/testes internos fora de exports, callbacks RX assincronos, workers,
ID por endereco/ABA e remove com DMA fault ainda precisam integracao antes
de carga. Gate nao equivale a recuperacao nem autoriza remover devres ativo.

Resultado: btif-session-close-drain-v1.patch aplicado/reverse dry-run fuzz=0.
Rebuild ARM32 passou com -Werror/modpost contra vmlinux.symvers real em
work/btif-lts-session-close-20261028-a.log. lg_btif.ko SHA256
b96326d299edd35b0164ca69c6ce0d47e6b08e43757cf1992adb4689604d0d06;
Module.symvers continua 516b10f53e2e18d7caeeddbec72e0d43a9259d32cec6bf9f6ac95e8dbb01ac14,
sem mudar exports. Fonte mtk_btif_exp.c SHA256
9438f8c0d20b6a95795106a3939bbba649c0b99eed433d22e55535530aa74d32.

Teste test_btif_session_close.py compila guard de sessao, lookup/open/close
e wrappers open/close/write reais da fonte staging fixada por SHA. Modelo
SRCU/pthreads e backends de hardware/alloc sao doubles, reutilizando modelo
membership existente. ASan+UBSan passaram em work/btif-session-close-host-20261028-a.log:
ID zero/incorreto recusado sem backend; retornos positivos/erro preservados;
writer admitido pausado, close chega a synchronize com ops solto e nao chama
hardware; novas operacoes recusadas, segundo close -EBUSY, novo open nao
substitui usuario; writer retoma, toma ops sem deadlock e termina antes do
teardown; close sucesso libera usuario, timeout preserva handle mas gate segue
fechado; retry de close pode concluir; open falho nao publica ID de sessao.

Regressoes diretamente afetadas passaram: membership log
work/btif-user-membership-host-20261028-b.log e guard dos doze exports/getter
work/btif-api-srcu-drain-host-20261028-d.log. Pins atualizados para fonte atual
e helpers/modelo acrescentados sem remover verificacoes; ambas instancias
SRCU sao balanceadas. Nenhuma suite ampla repetida. Fixture membership testa
membership sem readers ativos de sessao; fixture nova exerce a espera real
do modelo e ordem de teardown. Nao confundir doubles com RCU/kernel/DMA reais.

Limites atuais: protocolo cobre exports com ID, nao cdev/direct helpers nem
producao de callbacks assincronos/worker apos API retornar. Remove usa close
core apos drenar lifetime de exports, mas ainda nao recupera DMA fault nem
resolve users vivos/refs de modulo automaticamente. Proximo bloqueio concreto:
retirada das interfaces cdev/poll/ioctl e callbacks antes de soltar recursos,
depois recuperacao segura de remove sob falha. Sete simbolos WMT continuam
indefinidos; nenhum modulo carregado, flash ou alteracao fisica nesta etapa.

### BTIF: lookup de usuario concorrente com close

Entrega pretendida no aparelho: chamadas do transporte nao percorrem usuario
ja removido/liberado por close. Aceite offline: lookup e link/unlink protegidos
pelo mesmo spinlock, copia somente ponteiro da porta estatica antes de sair;
vfree/close/alloc nao ocorrem sob spinlock; close falho mantem ID; closes
concorrentes revalidam lista sob ops_mtx e somente um remove/libera usuario.
Nenhum ensaio fisico, carga ou flash autorizado por esta etapa.

Reuso: primitivas Linux 6.18.58 spin_lock_irqsave/list, revisao
2926d88bb7fc4608fd942453d929c39e4e5ec006, e ops_mtx/lista existentes LG.
Escolha spinlock curto para traversal/mutacao em vez de mutex dormivel em
lookup potencialmente usado no caminho de transporte. SRCU anterior protege
porta/recursos contra remove, mas nao impede vfree de usuario por close
concorrente; nao usar SRCU como se fosse exclusao mutua da lista. Triagem
mainline/pmaports/MediaTek/Qualcomm anterior nao confirma substituto BTIF;
adaptar mtk_btif_exp.c LG GPLv2-only existente, sem novo catalogo/handle backend.
Origem original 9f040ad26e7bcd49f9e175ce1d2d43418ef2f065aaf0a32e3633db40d45b32e6;
staging anterior 58147218cfd639395f56175173d040c72df6afb2e5dd5bf26b4a267cacdfa52c.

Novo codigo justificado: um spinlock estatico de membership e secoes curtas
em lookup/add/del existentes, sem alocacao, espera ou log sob lock. Ordem de
escrita ops_mtx -> user_lock; lookup solta user_lock antes de qualquer ops_mtx,
nao inverter essa ordem. Leituras debug de open e revalidacao de close seguem
sob ops_mtx, que ja serializa os escritores. Copiar g_btif estatico nao e
reter p_user; nenhum p_user sai do lock. Erro de segunda tentativa de close
usa o mesmo E_BTIF_INVAL_PARAM da busca inicial, nao sucesso ficticio.

Limites: isso resolve lifetime da entrada da lista, nao serializa todas as
operacoes do hardware contra close depois de lookup. Nao manter ops_mtx sobre
todas as APIs: algumas esperam RX mutex/callbacks e podem reentrar no transporte.
Reuso de endereco de usuario como ID (ABA), callbacks, cdev e recuperacao de
remove em falha continuam pendentes; nao inferir compatibilidade universal.

Resultado: btif-user-membership-lock-v1.patch aplicado/reverse dry-run fuzz=0.
Rebuild ARM32 passou com -Werror e modpost contra exports reais do vmlinux em
work/btif-lts-user-membership-20261028-a.log. lg_btif.ko SHA256
910cb319650dd6a692753bb357cd5596d1ab64b217cad64d7ada47ba83feb2ff;
Module.symvers permanece 516b10f53e2e18d7caeeddbec72e0d43a9259d32cec6bf9f6ac95e8dbb01ac14,
nenhum export alterado. mtk_btif_exp.c agora SHA256
8a4f013b47aabb0a5245422be437b4a99e17e663ba9301b845f5165f0573b32c.

Teste test_btif_user_membership.py compila lookup/open/close reais da fonte
staging fixada por SHA, com lista/locks pthread e hardware/alloc doubles.
ASan+UBSan passaram em work/btif-user-membership-host-20261028-a.log: usuario
ausente, ready=false, falha alloc/open com unwind, open duplicado, timeout de
close retendo entrada; leitor pausado sob membership lock impede close de
obter entrada/libera-la; dois closes ja com ponteiro da porta, primeiro
pausado no backend, segundo espera ops_mtx e revalida lista vazia apos unlock,
sem segunda chamada de hardware nem segundo free. Assercoes exigem add/del
sob ambos locks e nenhuma alocacao/espera de hardware/log/free sob spinlock.

O teste SRCU foi reexecutado por tocar o mesmo API layer, com pin de fonte
atualizado para o novo corpo LG+membership, sem mudar verificacoes: passou em
work/btif-api-srcu-drain-host-20261028-c.log. Doze wrappers e getter permanecem
balanceados. Nenhuma suite ampla repetida; source pins/test-catalog atualizados.
Testes nao provam IRQ/spinlock kernel reais, transporte fisico ou todas as
interleavings. A porta retornada e estatica e esta protegida do remove pelo
SRCU externo, mas close concorrente pode mudar enable/modo apos lookup.
Proximo bloqueio concreto: admissao de operacoes contra fechamento da sessao,
sem segurar mutex durante callbacks reentrantes, mais cdev e DMA fault/remove.
Sete dependencias WMT permanecem indefinidas; nenhum modulo carregado/flash.

### BTIF: retirar APIs exportadas e esperar chamadas admitidas

Entrega pretendida no aparelho: remove nao libera buffers/MMIO enquanto uma
API exportada admitida ainda os usa. Aceite offline: APIs recusam ready=false,
remove despublica ready e aguarda leitores SRCU, chamada antiga termina antes
da limpeza e nova chamada nao entra no backend; getter nao precisa de probe
lock enquanto remove espera. Sem carga fisica ou flash nesta etapa.

Reuso: Linux 6.18.58, revisao 2926d88bb7fc4608fd942453d929c39e4e5ec006,
include/linux/srcu.h e kernel/rcu/srcutree.c GPL-2.0-or-later por seus notices:
SRCU permite leitura que dorme e synchronize_srcu espera leitores anteriores.
Usar lifetime nativo ja empregado nas pontes WMT desta auditoria. Triagem
mainline/pmaports/MediaTek/Qualcomm existente nao fornece driver BTIF MT6765
substituto confirmado; adaptar core/API LG GPLv2-only existentes, nao criar
framework ou protocolo paralelo. API get/put internos ao mesmo modulo, sem
EXPORT_SYMBOL novo. Fonte staging antes: mtk_btif_exp.c
34650b1f6de7ef514cf4ad86315a58a00389ed4c1e017d972c74646f9059b1d5;
demais originais/revisoes abaixo. Licenca SRCU confirmar pelos arquivos locais.

Codigo novo justificado: pequenos wrappers das doze funcoes EXPORT_SYMBOL
existentes; preservam argumentos/retornos/corpos LG no sucesso. Entradas int
indisponiveis retornam -ENODEV, bool false, getter task NULL, open limpa ID.
Read-side nao mantem mutex global nem muda contexto permitido das APIs.
Remove fecha entrada e espera SRCU antes de close/port_deinit; NAO chamar
remove sincrono a partir de uma API protegida. Getter deixa probe lock e usa
ops_mtx dentro da secao SRCU; core verifica ops_mtx para ownership. Ordem
probe->synchronize SRCU sem leitor depender de probe lock. Sem locks que
possam dormir acrescentados aos callbacks de IRQ.

Limites: nao serializa lookup user_list contra close concorrente; isso precisa
tratamento proprio. Cdev/sysfs/test APIs locais nao exportadas, callback RX,
worker e users vivos nao sao automaticamente leitores desse SRCU. Active/fault
remove, reset/recuperacao e devres continuam bloqueios antes de carga; nao
apresentar drenagem de exports como solucao completa de unload.

Resultado: btif-api-srcu-drain-v1.patch aplicado e reverse dry-run fuzz=0.
Build ARM32 passou com -Werror/modpost contra vmlinux.symvers real em
work/btif-lts-api-srcu-20261028-a.log. lg_btif.ko SHA256
2fc963e875f7982c06643407c32cb2a02c7b21b463f6b8d8d93a4e44460cfeb1;
Module.symvers permanece 516b10f53e2e18d7caeeddbec72e0d43a9259d32cec6bf9f6ac95e8dbb01ac14,
sem exports novos/removidos. mtk_btif.c SHA256
35e3513035ab862782e4df1e59156f371db1fd404d78f0cccdb9e06a1f87ea3a;
mtk_btif_exp.c 58147218cfd639395f56175173d040c72df6afb2e5dd5bf26b4a267cacdfa52c;
mtk_btif.h 8d8cb6542672d7a495234076e57c8f1e3c25b3d983dd5aa033f17d1231f7d5f1.
SPDX local srcu.h/srcutree.c confirmado GPL-2.0+; drivers/base/core.c usa
device_links_srcu/read_lock/read_unlock/synchronize_removal como exemplo de
API interna ao core e retirada de estruturas. Nenhum codigo copiado desse
driver core, somente reutilizadas as APIs SRCU.

Teste test_btif_api_srcu_drain.py fixa fontes staging por SHA e compila guard,
disconnect e todos os doze wrappers reais; getter core e backend exportado
reais tambem incluidos, sem mutex probe no modelo. Demais backends sao doubles
para testar encaminhamento/lifetime, nao funcionamento de transporte. UBSan
e pthreads passaram em work/btif-api-srcu-drain-host-20261028-b.log: argumentos
e retornos int positivos/negativos/bool/task preservados, indisponivel nao
entra em backend e limpa ID do open; getter adquire ops_mtx e ref balanceada;
chamada write antiga pausada no backend impede disconnect de terminar;
novas chamadas de todas as APIs sao recusadas durante espera, liberacao ocorre
apenas apos chamada antiga sair; contagem SRCU balanceada. Logs a/b passaram;
b inclui getter real. Fonte fixada nao e portable fixture de checkout sem LG.

Limites confirmados no codigo atual: read/write do cdev estao sob #if 0,
nao ha leitura bloqueante ativa a acordar nesse perfil; poll/ioctl e sysfs
continuam acessando estado e ainda precisam retirada/drenagem propria. Nao
habilitar os branches antigos de read/write. Os wrappers nao resolvem races
de user_list/close entre APIs admitidas nem callback que use recursos apos
retornar da API. Remove ainda nao e seguro em DMA fault; gate fisico segue
fechado. Proximo incremento concreto: ownership de usuarios e close concorrente,
seguido de cdev/poll/ioctl e recuperacao de remove. Sete simbolos WMT ainda
indefinidos; nenhum modulo carregado, acesso fisico, DT ativado ou flash.

### BTIF/STP: referencia da tarefa RX entre modulos

Entrega pretendida no aparelho: metadados da thread RX permanecem validos
enquanto o STP os usa, inclusive apos parada da thread; close nao deixa task
pendente nem libera referencia durante leitura diagnostica. Aceite offline:
getter adquire ref sob locks de probe/usuarios; STP open/close serializados;
close falho retém handle/ref; close bem-sucedido retira ponteiro e espera
leitores RCU antes de put; dump/PID tomam ref antes de sair de RCU. Sem carga.

Reuso: Linux 6.18.58, revisao 2926d88bb7fc4608fd942453d929c39e4e5ec006,
get_task_struct/put_task_struct e RCU existentes, mutex de probe BTIF e
ops_mtx LG ja existentes. Triagem mainline/pmaports/MediaTek/Qualcomm anterior
nao fornece substituto BTIF confirmado; adaptar core/API/STP existentes, nao
criar framework de handles ou transporte paralelo. Arquivos LG GPLv2-only
mtk_btif.c, mtk_btif_exp.c, inc/mtk_btif{,_exp}.h e WMT stp_btif.c/osal.c/
wmt_ctrl.c: identidades originais/staging registradas abaixo/etapas anteriores.

Busca dos consumidores C/H em LG kernel-4.9/drivers/misc/mediatek/btif e vendor
connectivity encontrou apenas stp_btif.c chamando mtk_btif_exp_rx_thread_get;
API layer e helper core internos compoem a cadeia. Mudar contrato desse getter
para referencia possuida (caller put_task_struct) e atualizar consumidor e
header: manter assinatura/export, mas NAO alegar compatibilidade de ownership
com binarios Android externos nao auditados. Perfil atual so usa WMT portado.
Mutex de probe passa a ser compartilhado entre objetos do mesmo modulo, sem
EXPORT_SYMBOL de lock; getter toma probe -> ops, protegendo lookup e p_task
contra close/remove. STP publica pointer por RCU e libera apenas no close
sucesso. Close de rollback sem task nao inventa referencia. Nome e copiado
antes da publicacao. RCU leitores copiam ref e soltam RCU antes do dump/log.

CONFIG_SCHEDSTATS=n no kernel atual: caminho privado opcional de schedstats
nao e validado nem habilitado. Os consumidores atuais da task STP sao mark/
unmark (sem acesso a task nesse perfil) e log PID; dump OSAL recebe a mesma
protecao RCU. Outros OSAL threads ainda dependem de seus donos, nao afirmar
correcao universal de destroy. Grace period de todas as APIs, live users e
DMA fault/remove continuam bloqueios separados antes de qualquer carga.

Resultado (consolidado em 2026-10-28): btif-rx-task-reference-v1.patch e
wmt-btif-task-reference-v1.patch aplicados/reverse dry-run fuzz=0. BTIF
recompilou completo com -Werror e modpost contra vmlinux.symvers real em
work/btif-lts-rx-task-reference-20261027-a.log. lg_btif.ko SHA256
8a5d081cbb5d0b34628aa7862c6a846fc94c09dbe7f26ccd1bed78057b53c2d8;
Module.symvers permanece 516b10f53e2e18d7caeeddbec72e0d43a9259d32cec6bf9f6ac95e8dbb01ac14.
WMT compilou stp_btif/osal/wmt_ctrl e linkou wmt_drv.o, mas modpost continua
falhando com os mesmos sete simbolos em work/wmt-lts-btif-task-reference-20261027-a.log;
nenhum WMT .ko aprovado. O header privado WMT tambem documenta ownership
referenciado, sem substituir o original LG. Sem KBUILD_MODPOST_WARN.

Teste test_btif_wmt_task_reference.py reconstrui patches sobre originais LG
fixados por SHA e compila getter core/exportado, STP open/close, dump OSAL e
log PID reais. UBSan/pthreads passaram em
work/btif-wmt-task-reference-host-20261027-c.log. Casos: getter invalido/nao
pronto/task ausente ou ERR_PTR, open falho e rollback close falho, close
falho mantendo ID/ref, close repetido, leitores com refs balanceadas, dois
opens concorrentes (so um admitido), dois closes (so uma liberacao). Corrida
forcada pausa leitor apos carregar ponteiro em RCU e antes de get_task_struct;
close chega a synchronize_rcu e nao termina; referencia do dono BTIF e retirada,
STP mantem ultima ref; leitor adquire ref, sai de RCU e faz dump antes do put
final. Teste usa RCU/task doubles e sincronizacao pthread, nao kernel real.
Tentativa a falhou por misleading-indentation no auxiliar do teste, corrigida
sem relaxar -Werror; b/c passaram, c inclui header privado sincronizado.

Limites persistem: esse contrato protege task_struct, nao callback executando,
MMIO, buffers, user_list concorrente ou unload. _btif_rx_btm_deinit mantem sua
ref propria ate stop_put; o STP agora mantem outra ref independente ate close.
Proximo bloqueio: todas as APIs exportadas precisam ser retiradas de servico
e drenadas antes de remove liberar recursos. O getter atual e protegido pelo
mutex de probe, mas demais APIs apenas testam ready/lookup e podem estar em
andamento quando remove comeca. Nao manter probe lock ao esperar leitores que
tambem precisem desse lock; nao colocar lock que possa dormir no callback IRQ.
Cdev read/poll e callbacks precisam estrategia de desconexao/acordar antes da
drenagem. Remove com DMA fault continua sem recuperacao comprovada e nao pode
vetar devres com retorno void. Nenhuma carga fisica/flash neste incremento.

### BTIF: inicializacao por dispositivo, nao por module_init

Entrega pretendida no aparelho: probe adiado por IRQ/clock nao deixa uma
porta incompleta; APIs so acessam buffers/contextos depois de inicializacao
inteira. Aceite offline: module_init apenas registra driver; probe adiado
retorna errno sem publicar ready; falha em cada aquisicao desenrola recursos
adquiridos, retry funciona; interfaces/ready sao publicados por ultimo; idle
remove drena contextos/log works antes dos buffers. Ainda sem carga fisica.

Reuso antes de implementar: driver core platform/deferred probe e devres do
Linux 6.18.58, revisao 2926d88bb7fc4608fd942453d929c39e4e5ec006, e fluxo de
probe/remove do mtk-uart-apdma.c MediaTek GPL-2.0 (identidade abaixo). Reusar
HAL, filas, VFIFO, IRQ, CCF, cdev e helpers LG existentes, reorganizando sua
ownership. Triagem mainline/pmaports/MediaTek/Qualcomm anterior nao confirma
substituto BTIF MT6765; nao criar framework ou backend paralelo. Helpers
locais port_init/deinit representam uma porta fisica existente, nao catalogo
universal. Manter BTIF_PORT_NR=1 do perfil LG, sem generalizar outro hardware.

Arquivos LG GPLv2-only: mtk_btif.c, mtk_btif_exp.c, btif_plat.c e headers
HAL/core, identidades originais/staging abaixo. Novos trechos justificados:
deslocar SW init para probe, ready publicado com release/acquire, unwind por
estagio, deinit de FIFO HAL existente e limpeza de cdev antes incompleta.
HAL info_get passa a propagar falha em vez de logar e continuar; nenhuma
API/export de transporte removida. Sem enable/reset/acesso eletrico no init;
ativacao do canal continua exclusiva de open ja existente.

Limites de escopo desta integracao: ready impede uso antes do primeiro probe
ou durante falha, mas sozinho nao garante grace period de chamadas ja em
andamento no remove. Remove ativo/fault e lifetime de users/ponteiro STP ainda
requerem protecao/recuperacao antes de carga; nao tratar um return no remove
void como veto ao desmapeamento devres. Esse gate fisico permanece fechado.

Resultado: btif-per-device-init-v1.patch aplicado/reverse dry-run fuzz=0.
Substitui o gate sincrono anterior: BTIF_init agora apenas registra o driver;
um dispositivo ausente/adiado deixa APIs indisponiveis, nao cancela o driver.
Probe serializado adquire recursos/clocks, inicializa SW e cria interfaces;
drvdata e ready sao publicados por ultimo. HAL FIFO usa GFP_KERNEL no probe,
propaga errno e libera header se dados falham. Cdev desfaz cada etapa e remove
idle libera device/class/cdev/region; contextos/log works drenam antes dos
buffers, VFIFOs e FIFO HAL, antes de unprepare. Nenhum DMA enable no probe.

Build ARM32 completo passou com -Werror/modpost contra vmlinux.symvers real em
work/btif-lts-per-device-init-20261027-a.log. lg_btif.ko SHA256
869e8fede6a8aaed12ea373b0544208414d3df248e226c919c09e9665bccf892;
Module.symvers permanece 516b10f53e2e18d7caeeddbec72e0d43a9259d32cec6bf9f6ac95e8dbb01ac14,
sem alterar exports. Fontes staging: mtk_btif.c
1272bbf2f94ed1f9ec6320d1e675d2cb63f9bf3824ed2dc11eb7d27df4b35322;
mtk_btif_exp.c 1bce93c7869e86163ed33f4ad12333032e8ff6dc8557a5aece436e911f58347d;
btif_plat.c f1576065d7b16874668891bff2211370b0aec6e2eb2866eae365cc067f2e2192;
mtk_btif.h aa1f06f627cc11c72d9996c6b273af11e26fa1d80a26803095d0dfd86191f329;
btif_pub.h 14128222bd9ed666a966721f7cb8973a5e35f214b268dc018490077bfe745bcf.

Teste test_btif_per_device_init.py reconstrui a sequencia sobre originais LG
fixados por SHA. Compila port_init/deinit, probe/remove, init/exit, cdev,
FIFO/info_get/deinit HAL, core open e open/lookup exportados reais. Operacoes
filhas de DMA/thread/CCF/devres sao doubles (cobertas separadamente nas etapas
anteriores). UBSan passou em work/btif-per-device-init-host-20261027-c.log:
falha em cada aquisicao do probe sem vazar buffers/FIFO/VFIFO/contexto/CCF ou
interface, seguido de retry; -EPROBE_DEFER em IRQ/clock conserva registro do
driver e aceita probe posterior; APIs antes do probe retornam indisponivel
sem mutex/lista nao inicializados; core open so admite inicializacao depois
de ready; remove idle drena e libera o adquirido. Protecao de port_deinit
recusa fault sem liberar buffers; NAO equivale a provar remove em fault.
Teste a encontrou variavel usada so em log eliminada pelo modelo; sink de log
foi corrigido sem relaxar -Werror. b/c passaram; c inclui core open real.

Limites: nenhum driver core real, fila kernel, DMA ou recurso fisico executado
pelo host; deferred retry foi modelado, nao observado no aparelho. Live users,
readiness versus chamadas concorrentes e ponteiro emprestado ao STP ainda
precisam grace period/ref apropriadas. Remove ativo com parada falha nao pode
ser tornado seguro por retorno void: o driver core ainda libera devres. Esse
e proximo bloqueio concreto antes de carga, junto da recuperacao sob fault;
nao habilitar ensaio so porque init e remove idle passaram. Sete dependencias
de link WMT permanecem. Nenhum modulo carregado, DT alterado/ativado ou flash.

### BTIF: aquisicao de recursos no probe por APIs nativas

Entrega pretendida no aparelho: transporte BTIF somente com MMIO/IRQ validos,
sem acesso via private_data NULL ou mapas nao verificados. Aceite offline:
probe mapeia/reserva recursos e traduz IRQs antes de publicar dispositivo;
falhas de mapa/IRQ/clocks preservam erro; getters HAL nao mapeiam novamente;
init atual recusa probe ausente/falho antes de qualquer buffer/HAL. Nenhum
ensaio/carga autorizado; a mudanca completa de init/deferred probe ainda sera
necessaria, nao afirmar que esse ultimo gate ja a implementa.

Reuso: mtk-uart-apdma.c Linux 6.18.58, revisao/licenca/SHA abaixo, usa
devm_platform_ioremap_resource e platform_get_irq. Reaproveitar essas APIs e
HAL LG, nao criar tradutor DT/MMIO nem copiar driver UART sobre BTIF. Triagem
mainline/pmaports/MediaTek/Qualcomm anterior nao confirma substituto BTIF.
MediaTek LG mt6765.dts e backup overlay-0-id0-rev6.merged.dts concordam:
reg[0] 0x1100c000/0x1000, reg[1] 0x11000880/0x80, reg[2] 0x11000900/0x80;
IRQs SPI 112/132/133, level-low. Manter indices/core-TX-RX e validar tamanhos
do perfil; usar platform_get_irq para traducao IRQ-domain e flags ja definidas
pelo firmware, IRQF_TRIGGER_NONE no request. Nao copiar indices 2/5/8 de
interrupts nem 1/5/9 de reg, que dependem de #*-cells e nao sao API generica.

Arquivos LG GPLv2-only: mtk_btif.c, btif_plat.c, btif_dma_plat.c e headers
publicos HAL. Identidades anteriores abaixo; btif_pub.h original SHA256
289b4a7ae4c6a12225a6d135409acb57b3c875d7f8ce8274b49ca73cb09645fc.
Codigo novo pequeno: transformar rotinas de mapeamento existentes em hooks
internos de probe, sem nova exportacao de modulo; getters passam a consultar
estado ja adquirido. devres do driver core libera mapas no probe falho/remove;
nenhuma escrita de registrador, enable, reset ou IRQ request nesta aquisicao.
Reserva exclusiva por sub-bloco protege contra controlador concorrente.
Backup tambem tem ap_dma@11000000 abrangendo 0x1000: se um driver reservar esse
bloco inteiro, o probe BTIF deve falhar -EBUSY, nao remapear sem exclusao.
Particionamento DT/ownership deve ser resolvido antes de ativar no aparelho.

Limite planejado explicito: o module_init LG ainda depende de probe sincrono.
Gate sem private_data evita crash e desfaz registro, mas -ENODEV nessa borda
nao e suporte a deferred probe nem prova de hardware pronto. Mover buffers e
publicacao para probe e tratar remove/unload continuam etapas obrigatorias.

Resultado: btif-probe-resources-v1.patch aplicado e reverse dry-run fuzz=0.
Rebuild ARM32 completo passou com -Werror/modpost contra vmlinux.symvers real,
sem novos exports nem erro relaxado, em work/btif-lts-probe-resources-20261027-a.log.
lg_btif.ko SHA256 082581585e3722ef8714ef4d60db184f92fca61414f403b9e15583397ba6c6a7;
Module.symvers continua 516b10f53e2e18d7caeeddbec72e0d43a9259d32cec6bf9f6ac95e8dbb01ac14.
Fontes staging: mtk_btif.c dfb28aba42d7bea0ece6fea305593adbe23209adcc8a11994892a57d5c9f95cb;
btif_plat.c 47b0755d0c59853b2255e0e5aa72e12657c3a9459fe9159a11b39d091de07f6b;
btif_dma_plat.c d4988c367863b2b907f3456e170d10c0f90619e21815b66732593eff6574eb41;
btif_pub.h b6cda6e28a2b93b5d1cdee79a32bd1c50457711c90498fefc9916393eec61a55;
btif_dma_pub.h aa30aa524f667312951633434127062fa82d6df417c132641386ee0c3e236205.

Teste test_btif_probe_resources.py aplica patches sobre originais LG fixados
por SHA, compila hooks/probe reais e o prefixo exato de module_init ate o gate
antes de sysfs/buffers. UBSan passou em work/btif-probe-resources-host-20261027-a.log:
falhas de mapas -ENOMEM/-EBUSY/-EIO e IRQ -EPROBE_DEFER sem publicar dispositivo,
recursos ausentes/truncados, IRQ zero rejeitada, erro de clock antes de publicar,
retry apos liberacao simulada pelo driver core, indices e IRQs traduzidas
preservados, IRQF_TRIGGER_NONE, probe duplicado sem tocar recursos, init sem
dispositivo desfaz registro antes do caminho SW. Getters nao chamam of_iomap.

Limites: doubles nao provam traducao GIC real, contencao de regiao, devres real,
nem probe/DT no aparelho. Liberacao devres em probe falho e contrato do driver
core, simulada no teste; ponteiros HAL internos podem ficar obsoletos apos erro
parcial, mas dispositivo nao e publicado e gate impede init SW nessa situacao.
Nao provar a limpeza de toda BTIF_init com teste de prefixo; esse e o proximo
bloqueio: mover alocacoes/publicacao para probe e desenrolar recursos em falha
ou defer, inclusive FIFO HAL/CCF/maps, sem depender da ordem de module_init.
Remove/unload e recuperacao de fault ainda pendentes; sete dependencias WMT
continuam indefinidas. Nenhum modulo carregado, DT ativado, flash ou acesso
fisico nesta etapa; compilacao nao equivale a transporte funcionando.

### BTIF: recursos RX/TX assincronos na inicializacao parcial

Entrega pretendida no aparelho: transporte disponivel apenas com thread/queue
validas e limpeza de inicializacao sem task ERR_PTR, double free ou trabalho
acessando FIFO liberado. Aceite offline: errno de kthread_create preservado,
sem wake/stop de ponteiro invalido; mutex/ref de task balanceados; falhas TX
de queue/estrutura FIFO/dados FIFO desfazem somente o adquirido; deinit pode
ser repetido ou chamado apos falha; agendamento RX encerrado antes da drenagem.
Essa e uma dependencia da mudanca maior de probe/init, nao sua conclusao.

Reuso: Linux 6.18.58, revisao 2926d88bb7fc4608fd942453d929c39e4e5ec006,
kernel/kthread.c GPL-2.0-only documenta retorno ERR_PTR de criacao e
kthread_stop_put para thread com referencia adicional via get_task_struct;
ambas as APIs disponiveis no kernel nativo. kthread_stop atual sinaliza
TIF_NOTIFY_SIGNAL e acorda a thread: manter completion interruptible LG,
sem introduzir polling periodico ou fila de espera paralela. Workqueue core
existente drena trabalhos antes de destroy_workqueue retornar. Usar APIs
Linux de lifetime/sincronizacao, spinlock RX ja existente e dois flags de
recurso, sem novo framework, driver ou diagnostico. Triagem anterior de
mainline/pmaports/MediaTek/Qualcomm nao fornece substituto BTIF confirmado.

Arquivos LG GPLv2-only: mtk_btif.c e inc/mtk_btif.h, originais identificados
abaixo. Staging anterior mtk_btif.c
4686d9d0d82e09d5fda6fc60019a32680b15b5d829827786ceae823379c9db29;
header e562bab18c251a6e671372e0ea6d5a064343bf7d3e6e1ba850a54fb2c1029713.
Codigo novo justificado: ownership explicito nos init/deinit existentes;
thread RX passa a ter ref propria ate stop_put, flags publicados somente
apos sucesso, RX sched revalida sob spinlock antes de enfileirar e deinit
fecha a entrada antes de esperar. Flags nao substituem quiescencia DMA/IRQ
nem protegem automaticamente ponteiro de task emprestado ao STP. Sem parte
nova especifica de PMIC/SoC ou generalizacao para outro aparelho.

Resultado: btif-context-lifetime-v1.patch aplicado/reverse dry-run fuzz=0.
Build ARM32 passou com -Werror e modpost contra exports reais do vmlinux em
work/btif-lts-context-lifetime-20261027-a.log. kthread_stop_put esta exportado
no kernel 6.18 nativo; nenhuma exportacao BTIF alterada, Module.symvers
516b10f53e2e18d7caeeddbec72e0d43a9259d32cec6bf9f6ac95e8dbb01ac14.
lg_btif.ko SHA256 87fe48d0038cb4aff3d2eb93fb2694f260c986ea892d814b19c697ddfd7e34ab;
mtk_btif.c 299b03665bbd6a9f5bbf2f8d44c958261fe65559cc93f621069a00d91fb55a3c;
inc/mtk_btif.h 8a72fcf021926b1bd715d9a957efa7b33c90c7f8b904200ffc381dc221d6d26c.

Teste dirigido test_btif_context_lifetime.py aplica o patch sobre originais
LG fixados por SHA e compila init/deinit/sched reais, com doubles de task,
queue/FIFO/mutex/spinlock. UBSan passou em
work/btif-context-lifetime-host-20261027-b.log: ERR_PTR(-ENOMEM/-EINTR/-EPROBE_DEFER)
e NULL sem wake/stop invalido; criacao posterior valida; ref de task protegida
mesmo se a thread ja saiu; agendamento thread/queue/tasklet antes de fechar;
interleaving forcado fecha contexto entre leitura de ready e aquisicao do
spinlock, segundo check rejeita enqueue; deinit bloqueia novo enqueue durante
stop/cancel/drain; falhas TX de queue/header FIFO/dados FIFO nao deixam ponteiro
pendente; retries, init duplicado e deinit repetido; TX USER sem novos recursos.
Logs a/b passaram; b inclui agendamento normal de todos os contextos RX.

Limites: doubles nao provam execucao de thread kernel, concorrencia SMP real,
progresso de callback externo ou ownership do ponteiro emprestado ao STP.
O dono deve serializar init/deinit entre si; flags/spinlock protegem a entrada
de RX sched, nao tornam deinit concorrente reentrante nem autorizam liberar
recursos com DMA/IRQ ativos. RT/debug continuam no perfil existente (RT off,
BTIF_DBG_SUPPORT=0); nao inventar validacao dessas variantes. Ainda pendente:
inicializacao completa no probe, erro/defer sem acesso por private_data NULL,
rollback de buffers/mapeamentos/CCF e remove/unload usando parada confirmada.
Nenhuma carga de modulo, flash ou operacao no aparelho; sete simbolos WMT
continuam indefinidos e funcionamento fisico nao foi demonstrado nesta etapa.

### BTIF: parada confirmada antes de liberar IRQ/clock

Entrega pretendida no aparelho: fechar/suspender BTIF somente com DMA parada;
timeout deve manter IRQ, callback, clock e handle ainda necessarios. Aceite
offline: EN=1 preso retorna -ETIMEDOUT; STOP=0 com EN=1 nao e sucesso; sucesso
exige EN=0 antes de retirar IRQ/clock; falha chega a close/suspend/rollback e
API exportada sem descartar handle; TX tardio recusa fault ou porta fechada.
Sem autorizacao de carga/flash ou ensaio fisico.

Reuso antes de implementar: Linux 6.18.58 mtk-uart-apdma.c GPL-2.0, revisao e
SHA registrados abaixo, documenta STOP=1, esperar EN=0, STOP=0 e so depois
mascarar/sincronizar IRQ. Reusar essa sequencia e iopoll.h GPL-2.0-only, nao
copiar a limpeza upstream que continua apos timeout. HAL LG existente ja tem
STOP/FLUSH/EN, IRQ e CCF. Triagem mainline/pmaports/MediaTek/Qualcomm anterior
nao confirma substituto completo para BTIF MT6765. Nao criar driver paralelo.
TX LG proibe STOP e FLUSH simultaneos: aguardar FLUSH em andamento terminar
antes de STOP; nao introduzir novo flush nem descartar dados arbitrariamente.
Intervalo 10 us e teto nominal 10 ms como a etapa de reset, sem depender de
jiffies avancando em contexto suspend. Teto por fase: TX pode esperar ate
10 ms por FLUSH e mais 10 ms por EN. Nao e prazo eletrico confirmado.

Arquivos adaptados LG GPLv2-only: btif_dma_plat.c e mtk_btif.c (originais e
staging anterior identificados na secao IRQ abaixo), mtk_btif_exp.c original
SHA256 9f040ad26e7bcd49f9e175ce1d2d43418ef2f065aaf0a32e3633db40d45b32e6.
Pequenas extensoes no HAL, free/close/suspend/rollback e API ja existentes.
Motivo: codigo anterior lia STOP em vez de EN e devolvia sucesso no timeout;
free removia callback/IRQ antes de parar DMA; close exportado removia usuario
antes de fechar e sempre retornava 0. Mudar somente isso, manter separacao
HAL/core/API, sem novo diagnostico, transporte ou suporte de outras placas.
Fallback PIO tem free sem operacao retornando 0, nao falha artificial.
Nao substituir codigo fisicamente validado. Unload/remove e ownership de init
permanecem bloqueios separados antes de carga, mesmo com close corrigido.

Resultado: btif-dma-stop-confirm-v1.patch aplicado/reverse dry-run fuzz=0.
Rebuild ARM32 com -Werror e modpost contra vmlinux.symvers real passou em
work/btif-lts-stop-confirm-20261027-b.log, sem novos exports ou supressao de
erro. lg_btif.ko SHA256
74e0150a4259d67d47b973aa6c03f42a38f7b2907a64060457c255e5d58b25f7;
Module.symvers permanece 516b10f53e2e18d7caeeddbec72e0d43a9259d32cec6bf9f6ac95e8dbb01ac14.
Fontes staging atuais: btif_dma_plat.c SHA256
9cfca5408c447d98416a8cc70f2d539bdc08b6e5f33e7bbed480a20c01d20b7b;
mtk_btif.c 4686d9d0d82e09d5fda6fc60019a32680b15b5d829827786ceae823379c9db29;
mtk_btif_exp.c 49990dd60b61a502f9dead3acfb9e03a61eecc90401c260ef33cf84ec48129e9.

Durante a revisao, confirmado que IRQ TX pode iniciar FLUSH: free agora usa
_btif_irq_ctrl_sync(false), que chama disable_irq (drena handler), depois
mascara IER e so entao tenta STOP. No timeout, IRQ continua registrada mas
desabilitada/mascarada, callback e clock retidos; nao prometer interrupcoes
funcionando no estado de falha. O worker TX usa state_mtx: envio tardio apos
close/fault agora retorna erro antes de tocar MMIO/reinicializar a porta.
_btif_suspend deixou de sobrescrever erros ao liberar TX/RX e so muda estado
apos todos passarem. API exportada fecha antes de remover usuario e retorna
errno, preservando handle em falha; log deixa de afirmar delecao antecipada.

Teste test_btif_dma_stop.py compila funcoes reais HAL ctrl, IRQ sync/free,
DMA free/wrappers, close, suspend, rollback/init, envio e close exportado sobre
originais LG fixados por SHA; usa iopoll nativo fixado por SHA. UBSan passou
em work/btif-dma-stop-host-20261027-c.log: parada imediata/tardia, EN preso
mesmo com STOP lendo zero, FLUSH preso sem emitir STOP, handler drenando um
flush antes da parada, recursos/handle retidos em timeout TX/RX, falha chega
a suspend/rollback, mutex balanceado, PIO free=0, close normal e envio tardio
rejeitado. Build/test a/b eram incremento inicial; c inclui drenagem IRQ.
Teste a revelou constante ausente no modelo, corrigida sem relaxar -Werror.

Limites: estado de hardware sintetico, sem DMA/IRQ reais ou concorrencia SMP;
nao prova todos os trabalhos/callbacks drenados. Quando RX falha, TX pode ja
estar parado/liberado; latch impede repetir teardown parcial. Recuperacao de
fault nao esta pronta, nao limpar latch automaticamente. BTIF_exit/remove
ainda liberam buffers fora deste protocolo e init ainda tem unwind parcial
e dependencia de probe sincrono. Esses sao os proximos bloqueios concretos
antes de carga; tambem sete simbolos WMT continuam indefinidos. Nenhum acesso
ao aparelho, flash, carga de modulo ou ensaio fisico nesta etapa.

### BTIF: IRQ registrada antes de habilitar DMA

Entrega pretendida no aparelho: TX/RX DMA com handler valido antes de EN=1,
sem aparentar sucesso quando request_irq falha. Aceite offline desta etapa:
RX permanece mascarado ate callback, IRQ e modo prontos; erros de registro
chegam ao open sem fallback silencioso; falha antes de EN desfaz somente os
recursos adquiridos; falha apos tentativa de EN preserva recursos com latch;
timeout de reset anterior continua impedindo enable/retry. Sem carga fisica.

Reuso: Linux 6.18.58, revisao e identidade mtk-uart-apdma.c abaixo, registra
IRQ em alloc_chan_resources antes de issue_pending habilitar canal e devolve
erro quando request_irq falha. APIs IRQ/CCF e HAL LG ja existem; nao criar
backend paralelo nem copiar um driver UART sobre BTIF. Triagem existente
mainline/pmaports/MediaTek/Qualcomm nao confirma substituto BTIF MT6765.
Adaptar o caminho LG completo: mtk_btif.c, btif_dma_plat.c e
plat_inc/btif_dma_pub.h, GPLv2-only por arquivo, originais/versoes staging
identificados abaixo. Tornar visivel entre objetos do mesmo modulo a rotina
HAL de IER ja existente; nenhuma exportacao publica de modulo nova.

Codigo novo justificado: reordenacao curta de funcoes existentes, checagem
de errno e unwind antes de habilitar canal. RX hw_init nao habilita IER por
padrao; setup habilita depois de request_irq, callback, modo e DMA. TX preserva
IER inicialmente desligado (TX o ativa no envio). Fallback PIO por falha de
clock e mantido explicitamente; erro de IRQ/modo nao deve ser convertido em
sucesso pelo wrapper. Sem alteracao de registradores/endereco DMA/timing ou
perfil de outra placa. _btif_irq_reg nao publica handler em falha e rejeita
registro duplicado; IRQ obrigatoria ausente nao e sucesso. Esforco pequeno,
sem substituir implementacao previamente validada no aparelho.

Origem adicional: plat_inc/btif_dma_pub.h LG GPLv2-only SHA256
2c5ba3ffb223632762ff1dced732fea1c7650941e28a595cd96619f2a739c2f6.
Resultado: btif-dma-irq-order-v1.patch aplicado e reverse dry-run com fuzz=0.
Rebuild ARM32 completo passou com -Werror e modpost contra vmlinux.symvers
real, sem relaxar erro, em work/btif-lts-irq-order-20261027-a.log.
lg_btif.ko SHA256 e0801e0cefe54b60f5bf2213409410f0b718e537bcd2243aba7e0e9faf2a8111.
Module.symvers permanece 516b10f53e2e18d7caeeddbec72e0d43a9259d32cec6bf9f6ac95e8dbb01ac14.
Fontes staging atuais: mtk_btif.c SHA256
716dfb6082ed463673e35d6d77d1e6f64a481211c21c8e480f4b140f9b285696;
btif_dma_plat.c 6c6a49d44c1ff8bf125d69b16844c8521462982068a8cf8d85eae3ccd24af6c7;
plat_inc/btif_dma_pub.h 1877a9c559711ee56c034d287ba5b9d62647a096d66f6fe7f0b8fdc3b3d9aeb6.

Teste dirigido test_btif_dma_irq_order.py aplica reset-timeout e irq-order
sobre originais LG fixados por SHA e compila _btif_irq_reg/free, HAL reset,
setup/wrappers/init/open reais. Reusa modelo de doubles do teste de reset e
iopoll nativo fixado por SHA; nao reimplementa as funcoes testadas. UBSan
passou em work/btif-dma-irq-order-host-20261027-b.log: request_irq verifica
IER=0 e EN ainda nao habilitado; RX so desmascara depois de callback/IRQ/modo
e enable; falhas -EIO/-ENOMEM/-EBUSY/-EPROBE_DEFER propagadas sem PIO; modo
falhando libera IRQ e referencia de clock; retry pre-enable funciona; falha
apos tentativa de enable mantem IRQ/clock e latch; timeout continua sem IRQ
ou canal habilitado; open recebe erros; registro duplicado/IRQ ausente rejeitados.
Tentativa a falhou no extrator do modelo (funcoes de uma linha); corrigido
somente no helper do teste, sem alterar verificacoes ou avisos do compilador.

Limites: doubles de IRQ nao provam entrega de interrupcao, IRQ concorrente,
DMA fisica ou pinagem DT. Rollback de RX em _btif_init pode parar TX ja ativo;
esta fixture nao prova essa parada. Caminho stop LG ainda pode relatar sucesso
apos timeout, e free/remove/unload ainda nao garantem quiescencia antes de
soltar buffers/recursos. Esses sao bloqueios antes de carga. Sete dependencias
WMT continuam indefinidas; nenhum modulo carregado, flash ou ensaio fisico.
Proximo incremento: parar DMA com confirmacao de EN=0, propagar timeout e
reter IRQ/clock/buffers quando parada nao puder ser comprovada.

### BTIF: reset DMA limitado e erro sem fallback indevido

Entrega pretendida no aparelho: abrir WMT/BTIF ou devolver erro sem espera
infinita e sem habilitar canal/IRQ quando o reset DMA nao terminou. Aceite
offline: sucesso preserva programacao LG; RX/TX presos em EN=1 retornam
-ETIMEDOUT antes de VFIFO/IER/enable/callback; erro chega ao open, sem PIO,
sem duplo unlock; nova tentativa falha antes de MMIO se DMA ficou incerta.
Nenhuma carga ou ensaio fisico autorizado por esta etapa.

Reuso: driver MediaTek mtk-uart-apdma.c Linux 6.18.58, revisao/licenca/hash
registrados na secao seguinte, usa VFF_WARM_RST e polling de VFF_EN via iopoll,
com erro antes de request_irq. include/linux/iopoll.h GPL-2.0-only (Linux
Foundation/Qualcomm) fornece read_poll_timeout_atomic sem dependencia do
timekeeping, apropriado tambem para o caminho suspend LG. Triagem existente
mainline/pmaports/MediaTek/Qualcomm nao demonstra equivalencia do UART DMA
para o controlador BTIF; manter HAL LG e reusar apenas API de polling, sem
novo driver/diagnostico. Origem btif_dma_plat.c LG GPLv2-only original SHA256
531e41fdd19df5b67277dd5a59cfb39a73ae8d9d149cb8afd406ca0c64b90906,
staging antes da etapa e58846d47d1660aa8e06b1d369a15cbef8fcfab8ba9fe314589e2f3701c77813.
Origem mtk_btif.c e seu staging anterior identificados na secao DMA abaixo.
inc/mtk_btif.h LG GPLv2-only recebe somente estado de falha por controlador.

Escolha limitada ao perfil atual: polling atomic com intervalo 10 us e teto
nominal 10 ms (orcamento de parada ja usado pelo HAL LG), em vez de copiar
o teto UART de 100 us sem prova BTIF. Nao e limite de datasheet nem prova de
tempo fisico; iopoll atomic limita iteracoes/delays, nao promete deadline real.
No timeout manter referencias de clock/recursos e latchear dma_fault; nao
inferir DMA parada por errno nem liberar buffers. Nova inicializacao/idle e
suspend recusam o estado incerto. Nao limpar latch sem recuperacao comprovada.
Probe/remove/unload e parada DMA ainda precisam integracao antes de carga.
Pequenas extensoes no driver LG existente, sem abstracao ou transporte novo.
Correcoes de mutex limitadas a _btif_init: seus chamadores continuam donos do
lock e fazem o release, inclusive em falha. Nao substituir codigo fisicamente
validado nem afirmar equivalencia de timeout com a antiga espera infinita.

Resultado: btif-dma-reset-timeout-v1.patch aplicado e reverse dry-run com
fuzz=0. Rebuild ARM32 completo BTIF passou com -Werror, modpost e exports
reais do vmlinux, sem KBUILD_MODPOST_WARN, no log
work/btif-lts-reset-timeout-20261027-a.log. lg_btif.ko SHA256
0bc7845dfa531f992649948e423f71e5b313d75c9c8457f401085b7151860187;
Module.symvers permanece 516b10f53e2e18d7caeeddbec72e0d43a9259d32cec6bf9f6ac95e8dbb01ac14,
sem alteracao de exports. Fontes staging depois do patch:
btif_dma_plat.c c8f3178228ccbfdc180930d12eb9a9ce39be8cc25ecf36a68d0d1c474e318c9c;
mtk_btif.c 6e5249ecd32cd91658e2acf36d6eaa51b109c30de444849ddcdbeb4cd68d608e;
inc/mtk_btif.h e562bab18c251a6e671372e0ea6d5a064343bf7d3e6e1ba850a54fb2c1029713.

Teste dirigido test_btif_dma_reset.py compila HAL/setup/open/suspend/idle
reais sobre originais LG fixados por SHA. Usa o iopoll.h nativo fixado por SHA,
nao um polling reimplementado. Com doubles MMIO/clock/lock e UBSan, passou
em work/btif-dma-reset-host-20261027-c.log: escritas de sucesso iguais ao LG
para RX/TX, branches high/enable_4G, EN liberando de imediato ou apos espera;
EN preso termina sem programar VFIFO/IER do canal afetado; -ETIMEDOUT chega
ao open, sem PIO, enable ou registro de IRQ DMA do canal afetado; retries,
suspend e idle recusam latch; mutex liberado uma unica vez pelo chamador.
Falha de controller_setup tambem preserva erro e lock balanceado. A tentativa
a passou com escopo inicial; b revelou macro de log ausente no modelo ao
incluir suspend/idle, corrigida em c sem suprimir warning ou relaxar teste.

Limites: timeout RX pode acontecer depois de TX ja habilitado; o teste verifica
que seus recursos sao RETIDOS, nao que esse TX esta parado. Sem parar DMA nao
e seguro liberar buffers, desmapear, desabilitar clocks ou descarregar modulo.
Latch nao e mecanismo de recuperacao final. Unload/remove LG e rollback WMT
acima do BTIF ainda precisam preservar recursos/energia ate parada confirmada.
Tambem pendentes: IRQ DMA e habilitada antes de request_irq com erro ignorado,
parada/flush, unwind de init e ciclo probe/remove. Nenhuma carga fisica nesta
etapa. Sete dependencias de link WMT continuam presentes; este build nao prova
Wi-Fi nem transporte no aparelho. Proximo bloqueio concreto: ordenar registro
de IRQ antes de habilitar canal e propagar falhas sem DMA ativa sem handler.

### BTIF: negociar DMA antes de publicar o dispositivo

Entrega pretendida no aparelho: transporte WMT/BTIF com buffers VFIFO acessiveis
ao DMA, sem alocacao usando dispositivo ausente. Aceite desta etapa offline:
probe negocia mascara antes de clocks/publicacao; falha preserva errno e nao
publica; VFIFO sem dispositivo retorna -ENODEV sem chamar alocador; sucesso
mantem tamanho, flags de zero e endereco retornado pela DMA API. Nao autoriza
carga, operacao eletrica ou ensaio; reset/DMA/IRQ/remove ainda serao bloqueios.

Rastreamento SDIO anterior: wmt_func_wifi_on/off usa SDIO somente para
WMT_CHIP_TYPE_COMBO; para SOC chama mtk_wcn_wlan_probe/remove. Reset em
wmt_core.c distingue WMT_HIF_SDIO de BTIF fullset; wmt_detect_sdio_pwr_ctrl
depende de MTK_WCN_COMBO_CHIP_SUPPORT. Logo os cinco simbolos da ponte MSDC
nao devem ser fabricados para conseguir link, nem a ponte deve ser confundida
com WLAN/AXI integrado. Permanecem sete dependencias WMT; esta etapa passa a
tratar o bloqueio DMA no transporte BTIF realmente requerido pela placa.

Reuso antes de implementar: Linux 6.18.58, revisao
2926d88bb7fc4608fd942453d929c39e4e5ec006, driver MediaTek existente
drivers/dma/mediatek/mtk-uart-apdma.c, SPDX GPL-2.0, SHA256
ff37208b4262c0d1b1bed10e89804a141cee0d46949c867683c0cc047582493a,
ja usa dma_set_mask_and_coherent com 32 bits por padrao e erro de probe.
Esse driver e para UART APDMA/dmaengine, nao substitui automaticamente o HAL
BTIF LG nem prova compatibilidade de registros, IRQ ou suspend. A triagem
mainline/pmaports/MediaTek/Qualcomm existente abaixo nao fornece substituto
BTIF MT6765 confirmado; reaproveitar a DMA API existente e adaptar o driver LG
completo, nao criar alocador, driver ou backend de transporte paralelo.

Origem LG: kernel-4.9/drivers/misc/mediatek/btif/common/mtk_btif.c GPLv2-only,
SHA256 original 442f4fe1e19b4375fb42f57f6d1cbfb28e5cb3a8446735cd1e1ee89d8623ae67.
O staging antes desta etapa tem SHA256
08544252c42378b2f60e5693b6dd65c598a19d39277ee0b2b27a8c506fe2dfd5.
Kernel atual ARM32 sem ARM_LPAE e sem traducao enable_4G LG; selecionar DMA
de 32 bits para esse perfil, sem introduzir suporte a enderecos altos/33 bits
nao validado. DMA mask e contrato do dispositivo, GFP_DMA/GFP_DMA32 nao o
substituem. Mantidos HAL, MMIO, clocks, VFIFO e API DMA nativa. Parte especifica
da placa: limite conservador do perfil ARM32 atual; outros perfis adiados.
Esforco pequeno em funcoes existentes. Nao substitui caminho ja validado no
aparelho; equivalencia sob sucesso e falhas afetadas sera verificada no host.

Resultado: btif-dma-device-mask-v1.patch aplicado/reverse dry-run com fuzz=0.
Rebuild ARM32 com -Werror e modpost usando vmlinux.symvers real passou;
work/btif-lts-dma-mask-20261027-a.log. Novo lg_btif.ko SHA256
edadfb644e5772aaba6d6c29e55c3f869efcb3358e8f65a9e102334fdea5a0c5;
Module.symvers permanece identico (nenhuma exportacao removida/alterada), SHA256
516b10f53e2e18d7caeeddbec72e0d43a9259d32cec6bf9f6ac95e8dbb01ac14.
Fonte staging mtk_btif.c agora SHA256
956e185e3ae1112082bab78fc30b58412354614cd929064b6783d93fc386e35e.

Teste dirigido test_btif_dma_device.py aplica a sequencia de patches sobre
originais LG fixados por hash e compila as funcoes reais. UBSan passou no log
work/btif-dma-device-host-20261027-b.log: falhas DMA mask/clock -EIO, -ENOMEM e
-EPROBE_DEFER sem publicacao; probe duplicado nao toca DMA/clocks; VFIFO sem
dispositivo nao aloca; sucesso preserva flags/tamanho/endereco proximo ao limite
de 32 bits e buffer zerado; alocacao falha e repetida conservam erros LG.
Tentativa a falhou por misleading-indentation nos doubles, corrigido sem
relaxar -Werror. Teste nao executa DMA, IOMMU, clocks, bus ou probe real.

Pendente antes de carga: inicializacao LG ainda aloca buffers fora de probe,
tem unwind parcial e remove incompleto; negociar mascara e rejeitar dev NULL
nao resolve deferred probe/ownership nem permite liberar buffers com DMA ativa.
HAL ainda contem warm reset sem timeout; propagacao de erros do HAL, parada
de DMA, drenagem de IRQ/thread/work e lifetime/remove precisam integracao.
Nenhum .ko carregado, nenhuma mudanca no aparelho e sete simbolos WMT ainda
indefinidos. Proximo incremento funcional: limitar reset DMA e propagar sua
falha sem habilitar canal/IRQ, antes de tratar carga fisica autorizada.

### OSAL: diagnostico existente de tarefa/stack por API scheduler nativa

Entrega pretendida no aparelho: manter estado/stack da tarefa nos caminhos de
falha WMT, sem depender do scheduler privado 4.9. Aceite offline: nome invalido
nao acessa tarefas, prefixo escolhe a primeira tarefa como no LG, referencia
protege a tarefa durante o dump e OSAL delega a API nativa. Nao acrescenta
telemetria: adapta duas rotinas existentes. Nenhum aceite fisico nesta etapa.

Reuso: Linux 6.18.58, revisao 2926d88bb7fc4608fd942453d929c39e4e5ec006,
kernel/sched/core.c (GPL-2.0-only), sched_show_task EXPORT_SYMBOL_GPL: usa
try_get_task_stack/put_task_stack e mostra estado/flags/pid/tgid/ppid/stack.
LG osal.c GPLv2 original SHA256
5a51d57b09d97503a85b4910ce1f916b6a6d1c0fe7139e44a8f179017c366c5a.
O adapter LG connectivity_build_in_adapter.c (identidade abaixo) acessava
rq->curr/on_cpu/preempt_count privados e show_stack(tsk,sp) antigo nao exportado.
A triagem mainline/pmaports/MediaTek/Qualcomm vinculada nesta auditoria nao
oferece uma API estavel equivalente para esses campos privados. Escolhida a
API nativa em vez de copiar o scheduler ou exportar show_stack arbitrariamente.
Limitacao explicita: nao mostra curr de outra CPU nem preempt_count privado;
nao afirmar equivalencia desses campos. Nao substitui implementacao 6.18
funcional previamente validada no aparelho. Nenhuma parte nova especifica de
SoC/PMIC/placa; alteracao pequena no OSAL, sem novo modulo/framework.

Preservados limite de nome 255 e primeiro prefix match LG. strnlen limitado a
256; get_task_comm sob RCU faz copia limitada (rename concorrente continua
possivel); get_task_struct antes de soltar RCU; sched_show_task fora de RCU;
put_task_struct ao terminar. O ponteiro recebido por osal_thread_show_stack
continua exigindo garantia de vida pelo dono da thread; get_task_struct nao
conserta ponteiro ja liberado. Ausencia de match loga explicitamente. Nenhuma
escrita PMIC/SDIO/reset, nem mudanca de probe/remove ou recuperacao eletrica.

Resultado: wmt-osal-native-task-dump-v1.patch aplicado e reverse dry-run fuzz=0.
Header privado isolado deixa de redeclarar show_stack com assinatura 4.9;
original LG intacto. Tentativa a detectou esse conflito, corrigido na tentativa b.
osal.o ARM32 compilou com -Werror, SHA256
20385b9354c5a083befba1fe2103245e276c211c471087db1ea9aa1874b26be6.
LD wmt_drv.o passou; modpost ainda falha, agora com sete simbolos indefinidos,
em work/wmt-lts-native-task-dump-20261027-b.log. Usa vmlinux.symvers e exports
BTIF reais, sem KBUILD_MODPOST_WARN. Ainda nao existe WMT .ko aprovado.
Teste dirigido test_wmt_osal_task_dump.py passou com UBSan e doubles de
tarefa/RCU: NULL, nome 255/256, ausente, vazio, primeiro prefixo, referencia
balanceada e dump fora de RCU; log work/wmt-osal-task-dump-host-20261027-a.log.
Nao prova scheduler concorrente real, lifetime no callsite, Wi-Fi ou hardware.

Proximos bloqueios de link: connectivity_export_dump_gpio_info,
connectivity_export_clk_buf_ctrl, wmt_export_mtk_wcn_sdio_irq_flag_set,
wmt_export_mtk_wcn_cmb_sdio_disable_eirq, wifi_irq, mtk_wcn_cmb_sdio_pm_cb e
mtk_wcn_cmb_sdio_pm_data. Nao inserir stubs para aparentar compatibilidade.
Probe/remove, IRQ/DMA, limites eletricos e recuperacao continuam pendentes
antes de qualquer ensaio autorizado; nenhum modulo carregado ou flash nesta etapa.

Resultado abortoSDIO: patches sdio-abort-function-api-v1 e
wmt-hif-sdio-native-abort-v1 aplicados/reverse dry-run fuzz0. Kernelvmlinux
recompilou com sucesso em work/lts-sdio-abort-vmlinux-20261027-a.log e
vmlinux.symvers publica sdio_abort_func EXPORT_SYMBOL_GPL. SHA256vmlinux
f958e31de48d8acff8388d049d10f8872beca7fa2cc16d3b60f34bedeb6e58b0.
Alteracao so no workspace6.18 isolado: NAO reconstruido/gravado/ensaiado bootimg,
nao substitui evidencias das imagens anteriormente testadas no aparelho.
HIF recompilou -WerrorARM32 SHA256
0fa5bbfca817070bdeeb4902915cc2c677871af386331b8bf030ddac10ab890b;
LDwmt_drv.o passou e modpost reduziu10 para9 dependencias em
work/wmt-lts-native-sdio-abort-20261027-a.log, ainda semkoWMT aprovado.
Rebuild de dependentes do headerSDIO ocorreu peloKbuild; sem suiteampla.

Identidades de origem6.18 antes do patch: drivers/mmc/core/sdio_io.c SHA256
2f9db1b81f01d359faa689fb7609c04d6a9fdd7d833d16e201f74d7201e51e44,
include/linux/mmc/sdio_func.h SHA256
35a4f06a40c80d425eb459d00a6fedce6963ab2b5a9c12b386465ebd2d0b6b79;
fonteLG hif_sdio.c GPLv2 SHA256
db9b379ccda4902d2cfc5662694b194c6687ecd6daf2df86eca5bcfdee273ef2.
Teste tools/tests/test_wmt_sdio_abort.py fixa esses consumidores e fontecore
atualSHA31b2a524, extrai helperC real e aplica patchHIF a fonteLG original.
CMD52/host sao doubles: func1..7 gera claim/read0xbc/abortCCCR06fn0/release;
NULL/cardNULL/func0/8 nao enviaCMD; EIO/ETIMEDOUT/ENOMEDIUM da leitura bloqueia
CMD52 e libera host, errosdeCMD52 tambem liberamhost e preservamerrno. Contexto
HIFinvalido nao claim. Passou -Werror/UBSan em
work/wmt-sdio-abort-host-20261027-b.log. Tentativaa revelou extratorC incapaz
de lidar com bracesalternativos #ifHIF_SDIO_UPDATE; fixture preserva funcaointeira
ateEXPORT_SYMBOL e deixa preprocessorC selecionar ramo1 como buildreal, sem
relaxar verificacoes. ComentarioSPDX do C gerado corrigido para GPL2only pois
combina fonteLG; nenhuma logica alterada apos teste.

Prova cobre encaminhamento/erro, nao respostaR5 fisica, cartaoSDIO ou recuperacao
no aparelho. Quirklenient e sdio_f0_writeb intactos. Nove dependencias restantes:
SDIOIRQ/PMlegado, diagnosticsvendor e XO/PWRAP. Proximas integracoes devem
preservar ownership do host/IRQ e evitar aborto/desligamento concorrentes.
Nenhum comandoSDIO, reset, carga ou operacao fisica realizado.

### Aborto SDIO: extensao pequena do core existente, sem quirklenient

Entrega pretendida no aparelho: recuperacao de transferenciaSDIO quando o
caminhoSDIO for usado, sem comandoapos leitura preparatoria falha. Aceiteoffline:
CMD52mesmoLG fn0/CCCR_ABORT/valuefuncnum, func0/8/NULL recusados e errno
preservado; callerLG para no readl0xbc falho e sempre solta host. Isto nao
autoriza aborto/reset fisico nem prova que Wi-FiAXI usaSDIO naK40S.
Auditoria: Linux6.18.58 sdio_io.c GPL-2.0-or-later fornece f0write limitado a
0xf0..ff e sdio_disable_func desabilitaIOEx, nao aborto. mmc_io_rw_direct de
sdio_ops.c GPL-2.0-or-later ja executaCMD52 com erro/R5/SPI nativos, mas nao
exportado. LGadapterGPLv2 apenas o exportava genericamente. Alternativas
pmaports/MediaTekLG/Qualcomm triadas abaixo nao tornam desabilitarfunc ou
quirklenient equivalente ao abort, nem transportar CMD52 por BROM/DA.
Preferir novo helper sdio_abort_func no coreSDIO existente a driverparalelo,
export generico de registerwrite privado ou implementacaoCMD52 duplicada.
Helper recebe sdio_func valido1..7 e pressupoe hostclaimed como APIread/write;
nao inventar politica de retry/reset. Read0xbc do firmware fica noHIFvendor,
nao contaminar core generico com protocoloMTK. Reusar fontes/LinuxAPI fixadas
no workspace6.18 ja auditado, GPL porarquivo preservada; mudanca pequena,
buildkernel dirigido e testecallback real com doubles deCMD52 e host.
HIFLG SHA original e registrado com teste antes de adaptar. Semmodificar
quirks ou DT/dispositivo. Provider/SDIOIRQlegado e XO continuam dependencias
reais separadas, nao stubs.

Resultado ponteplataforma: patch wmt-platform-bridge-srcu-v1.patch aplicado e
reverse dry-run fuzz0. ObjetoARM32 -Werror SHA256
1f14318462f0a8a3eeccebce1c27f3bab2e60f5db4417a18c9e3010a090b0283;
LD wmt_drv.o passou e nm confirma cinco simbolosT reais de register/unregister
e consultasthermal/assert/clockdump. Modpost reduziu12 para10 dependencias
vendor em work/wmt-lts-platform-bridge-20261027-a.log; WMTko ainda nao existe.
As remanescentes sao clk_buf_ctrl/dump_gpio_info/dump_thread_state/show_stack/
mmc_io_rw_direct via connectivity_export, wifi_irq, mtk_wcn_cmb_sdio_pm_cb/data,
wmt_export_mtk_wcn_cmb_sdio_disable_eirq e sdio_irq_flag_set. Nao stubar ou
remover funcionalidades para esconder esses erros.

Teste tools/tests/test_wmt_platform_bridge.py aplica patchreal em fixture e
fixa headerLG porSHA57b97fe5, usa o modeloSRCU pthread ja existente do teste
logcallbacks (nao algoritmoRCU proprio deproducao). Retornos de thermal111/222,
assert-12/-34 e contagemdump preservados; semcallbacks retorna-1/log comoLG,
triggerassert mantem backtrace (double, nao assertfisico). Callbackthermal
suspenso impede unregister/substituicao de concluir; eventosnovos veem conjunto
novo/NULL completo durante espera, sem snapshotparcial. Copia da struct nao
depende do lifetime do argumento e dois slots suportam reutilizacao apos grace
period; NULLregister preserva ponteexistente. Passou -Werror/UBSan/pthread em
work/wmt-platform-bridge-host-20261027-a.log.
Isso nao valida consumidoresCPUthermal ou clockdebug reais, reset eletrico,
unloadWMT, nem setterslegados cmb_stub concorrentes. PonteSRCU nao protege
automaticamente seus callbacks AIF/deepidle ou settersinternos fora da ponte.
Proximo: integrar dependencias restantes sem contrariar equivalenciaSDIO/XO
e completar lifecycleBTIF antes de qualquer ensaio. Nenhum modulo/DT ativado.

### Ponte de plataforma LG: portar callbacks reais para o modulo WMT

Entrega pretendida: thermal/assert/clockdump de plataforma chegam ao WMT,
unregister nao deixa consulta de ponte em voo antes de soltar callbacks.
Aceite offline: APIsregister/unregister resolvidas no proprio modulo, consultas
retornam callbacks/erros reais, chamadas ausentes falham explicitamente e
unregister espera leitores. Sem assert/reset fisico.
Reusar trechoBridge de kernelLG4.9 connectivity/common/wmt_build_in_adapter.c
MediaTek2016GPLv2 SHA8b5cfed22b3025427fa802afe7546c9a0be6e7a2f59a6f5ff2aced090b6f7be2
e headerpublicoGPLv2 ja auditado, sem copiar o MSDC legado do mesmoarquivo.
Linux6.18 SRCU/mutex existentes permitem callbacks que dormem, no lugar dos
ponteirossemprotecaoLG. Mainline/pmaports/Qualcomm ja triados nao implementam
ABItermica/assertWMT; pequena extracaoLG num objeto do common e necessaria pois
adapter4.9 embutido nao existe no kernel nativo. Nao novo driver, provider,
protocolo ou stub: chamadas invocam callbackWMT real e ausencia intretorna-1
comoLG; clockdumpausente loga explicitamente comoLG. Manter dump_stack antes
de triggerassert. Branchregister_pg_callback era somenteMT6779, naoMT6765;
nao copiar dependencia de clockdebug4.9 para outroSoC.

Dois slots estaticos de structbridge, mutexwriter e SRCU: copiar para slot
inativo, publicar snapshot inteiro e graceperiod antes de permitir reuso;
sem alocacao que falhe silenciosamente na APIvoidLG. NULLregister conserva
no-opLG, unregister publicaNULL e espera leitores sem travas de consumidor.
Consultasexportadas pinam moduloWMT pelas regrasnormais; callback nao pode
registrar/remover a propria ponte (graceperiod recursivo). Os setterslegados
de cmb_stub e demais callbacks AIF/deepidle nao sao automaticamente cobertos;
avaliar lifecycleglobal antes da carga. Esforco pequeno/medio, teste dirigido
com callback suspenso e build real, nao framework novo de callbacks.

### Transporte WMT: validar RXthread BTIF antes de registrar callbacks

Entrega pretendida: STP abre controladorBTIF com threadRX valida e falha de
open/thread nao publica transporte quebrado. Aceiteoffline: preservar erroopen,
recusar NULL/ERRthread antes de comm, fechar handle adquirido e nao registrar
callbacksTX/pending em erro; falha doclose preserva handle para diagnostico/
recuperacao, nao declarar fechado. Reusar LG stp_btif.c GPLv2 SHAoriginal
cf6a3e066fba1cb185fdc97d560008b6def61c3ebff80345c7b2ea6d5c9fbb97 e API
mtk_btif_exp_rx_thread_get real. Esta retornaNULL em IDinvalido; lifetime de
thread apos get ainda precisa serializacao do controlador, nao se resolve
com testeNULL. Nao driver paralelo ou frameworknovo, pequena adaptacao do
open existente com IS_ERR_OR_NULL/PTR_ERR nativos, manter callbacks de sucesso.
Alternativas upstream/pmaports/Qualcomm da triagem nao mudam essa ABIWMT.
Teste dirigido de open real e falhas de unwind; buildARM32 STP-BTIF.

Triagem dos12 simbolosrestantes: mmc_io_rw_direct e privado no6.18;
sdio_f0_writeb chama mesmoCMD52 mas rejeita addr fora0xf0..0xff sem quirklenient.
AbortoLG escreve SDIO_CCCR_ABORT apos readl0xbc: nao substituir cegamente,
nao habilitar lenient so para compilar. Diagnostics show_stack/dump_thread usam
schedprivado4.9; sched_show_task exportado e candidato, nao equivalencia de
CPUcurr/private_rq garantida. BridgeWMT e implementacao real disponivelLG,
SDIOlegado nao deve ser removido sem consumidores, XO/PWRAP ainda pendente.
Nenhuma acao fisica para completar essa triagem.

Resultado: wmt-stp-btif-open-thread-v1.patch aplicado/reverse dry-run fuzz0,
stp_btif.o ARM32 -Werror e LD wmt_drv.o passaram em
work/wmt-lts-btif-open-20261027-a.log. ObjetoSHA256
e8256bb2bc6a738eb37589970b46bdce51d3141dc10faad65ffe54a3ad3c7cae.
Modpost ainda recusa12 simbolos pontevendor/XO, usando vmlinux.symvers e
Module.symversBTIF reais, sem erroignorado nemkoWMT.

Teste tools/tests/test_wmt_btif_open.py fixa fonteLG original porSHA e aplica
patch; executa openC real com APIcontrolador e registradorescallback doubles.
EIO/ENOMEM/EPROBE_DEFER deopen preservados sempublicacao; RXthreadNULL/ERR
nos mesmoserros fecha uma vez e nao publica4callbacks. Falha doclose mantemID,
nova tentativa EBUSY sem reabrir. Closebem-sucedido permite nova tentativa,
sucesso publica4callbacks com thread/copia do nome validos. Passou -Werror/
UBSan em work/wmt-btif-open-host-20261027-a.log. Contagem de hunk corrigida
antes de aplicacao, sem fuzz. Nao prova lifetime da thread em closeconcorrente,
quiescencia dos callbacksSTP ou entrega de firmwarefisica. Getter nao adquire
taskref: controlar open/close concorrentes e retirar callbacks ao fechar ainda
e necessario antes de uso. Sem alteracao dos fallbacksfracos ou deIRQ/DMA.

Proximo bloqueio permanece bridge/SDIO/XO real, com restricoes de equivalencia
registradas; concluir ownership e callbacksSTP no transporte antes de carga.
Nao inferir que SDIOexterno e Wi-FiAXI sao o mesmo caminho. Nenhum acesso
fisico, carregamento de modulo ou alteracaoDT nesta etapa.

Resultado integrado BTIF nesta etapa: APIexp, HALDMA e HALBTIF passaram
ARM32 -Werror apos patches btif-exp-private-helpers-v1,
btif-dma-irq-timespec64-v1 e btif-hal-pio-enum-v1; reverse dry-run dos3 passou
fuzz0. Make gerou lg_btif.ko e Module.symvers usando vmlinux.symvers do MESMO
build6.18, sem warnings-only/erroignorado. Aviso de build/Module.symvers ausente
permanece, mas exports reais foram fornecidos por KBUILD_EXTRA_SYMBOLS e
modpost concluiu sem unresolved. Log work/btif-lts-hal-api-20261027-c.log.
lg_btif.ko SHA256
c3c577de587d673bb69bcd750027b78af429bdc96cf89e912a5ee6de91c87da5;
Module.symvers SHA256
516b10f53e2e18d7caeeddbec72e0d43a9259d32cec6bf9f6ac95e8dbb01ac14.
Isto e compilacao/linkagem offline, NAO aprovacao de carga. Nao carregar este
ko enquanto probe/remove/DMA/timeoutwarmreset e efeitos de init estiverem
pendentes. Coretransport nao foi substituido por UART nem fallbacks fracos.

WMT agora recebe vmlinux.symvers e Module.symversBTIF reais via mecanismo
Kbuild;12 exportsBTIF resolvidos, modpostWMT volta a recusar12 dependencias
pontevendor/XO em work/wmt-lts-with-btif-symbols-20261027-a.log. Contagem24
anterior incluia o controlador faltante, agora implementado e compilado; nao
suprimir dependencias residuaisSDIO/bridge sem rastrear consumidores.

Teste tools/tests/test_btif_dma_irq_time.py fixa fonteLG SHA531e41fd e aplica
patchtimestamp, executa callbackIRQ C original/portado:511 flushes sem cutoff,
512 limpa flag e desabilitaIER, VFIFOvazia reseta contador, proximaIRQ inicia
timestamp novo; valid_size8 nao entra noflush. Trace/retornos equivalentes,
-Werror/UBSan passou em work/btif-dma-irq-time-host-20261027-a.log. RAM/MMIO/
spinlock/time sao doubles, nao prova IRQfisica ou comportamentoDMA real.
Haltime somente reporting, protecao512 preservada. Nao repetir suites amplas
por correcoes delinkage/literalPIO. Proximo bloqueio concreto funcional:
portar bridgevendor restante e integrarXO/PWRAP, mantendo gate de carga por
DMA/probe/remove doBTIF. Nenhum DT consumidor ou dispositivo ativado.

BTIF HAL enum: hw_init passa false para enum modoPIO/DMA; headerGPLv2
btif_pub.h define BTIF_MODE_PIO=0 e DMA=1. Usar BTIF_MODE_PIO nas duas chamadas
preserva bitclearTX/RX e ordem, sem cast ou supressaoenum-conversion.
Pequena correcao no backendLG, sem nova funcao/teste espelho para aliasliteral.

BTIF DMA IRQtime: hal_tx_dma_irq_handler usa timeval so para registrar inicio/
fim de512 interrupcoes de flush continuo; decisao de protecao e por contador,
nao elapsedtime. Reusar timespec64/ktime_get_real_ts64, micros em tv_nsec/1000
e sec%lld. Manter limiar512, clearflag e disableIRQ identicos. FonteLG
btif_dma_plat.c GPLv2/SHA531e41fd ja auditada; nao novo diagnostico, relogio ou
driver. Testar callbackC real com511/512 e resetcounter na condicaoVFIFOvazia;
DMAfisico/timeoutwarmreset continuam fora desse aceiteoffline.

BTIF LPAE: reutilizar headerLG MediaTek2016GPLv2 mtk_lpae.h SHA256
03409c075844250dd25fc66e1bc8c04c359efe2f87af9abdb7e1529842aa2c2e
somente no vendor-api privado. Build6.18 atual ARM_LPAE=n e nao possui
MTK_LM_MODE; ramooriginal enable_4G retorna0 (configuracaoNaoLM), nao stubnovo
para dependenciasausentes. HAL escreve basehigh por phy_addr>>32 no caminho
normal e usa traducao/protocoloMTK4G somente no ramoLM. Nao habilitarLM nem
reutilizar conversao4G em outroSoC por deducao. Para esseARM32 com DMA32,
manter caminhoLG existente; DMA mask, validacao de endereco/limites e timeout
dos loopswarmreset ainda exigidos antes de ativar. Headernao implementaDMA.
Se LM vier a ser requerido, ramo com weakenable4G nao e suporte comprovado.

### BTIF APIexp: linkage privado preservando API WMT

Entrega pretendida: implementacao exportada realBTIF para STP/WMT. Aceiteoffline:
APIexp compila sem reduzir verificacao, exportsWMT preservados e proximo
backend compilado. FonteLG mtk_btif_exp.c GPLv2 SHA9f040ad26e7bcd49f9e175ce1d2d43418ef2f065aaf0a32e3633db40d45b32e6
ja auditada. Busca C/H no controladorisolado encontra btif_exp_srh_id e seis
helpersno_id somente nesseC, sem export; torna-losstatic preserva corpos,
falhas e chamadas. btif_wakeup_consys_no_id possui prototipoheader existente,
nao muda. Nao esconder APIWMT exportada nem remover diagnosticos para compilar.
Reusar linkage C no mesmo driverLG; mainline/pmaports/Qualcomm ja comparados,
nao ha driver paralelo ou nova abstracao nesta etapa. Esforco minimo: build
-Werror, nm dos exports e reversepatch suficientes para linkage sem logica.

Resultado coreBTIF API6.18: btif-core-linux618-api-v1.patch e
btif-dma-zalloc-api-v1.patch aplicados/reverse dry-run fuzz0. Objeto mtk_btif.o
ARM32 -Werror compilou SHA256
bc7557e7ac12458305be4d05f301ba46d59b771a08ca3290fab649d2c028f75b.
Logs work/btif-lts-core-api-20261027-a.log (DMAalias ainda faltante) e
work/btif-lts-core-api-20261027-b.log (core compilado, proximo APIexp).
Sem moduloBTIF linkado ou ativado. Compatibilidade de removevoid nao resolve
teardown incompletoLG; sysfsdebug0644 ainda exige politica de ativacao segura.

Teste tools/tests/test_btif_time_api.py aplica dependenciaclock e patchAPI a
fontesLG fixadas porSHA, extrai detectorRX C real original/portado. Compara100
combinacoes de nanos0/999/1000/123456789/999999999 e deltasegundos-1/0/1/2;
retorno e gaps coincidem, limiar exatamente1s nao acusa stall,2s acusa e recuo
declock nao acusa. Passou -Werror/UBSan em work/btif-time-api-host-20261027-a.log.
FormulaLG de borrow aparenta somar micros no sentido nao convencional, mantida
para separar portAPI de mudanca de politica; investigar em entrega posterior
sem inferir validacao funcional por equivalencia de codigo. Timeoutdeepidle
conserva segundos/retries por inspecao e compilacao; nao foi simulado completo.
Logs wallclock/monotonic compilados64bits, sem alterar dominii/unidades.

Proximo bloqueio concreto: mtk_btif_exp.c tem missing-prototypes em
btif_exp_srh_id e helpersno_id. Primeiro e usado internamente, helpersno_id
tem consumidores no proprioC e possivelmente core; auditar refsC/H antes de
marcarstatic/adicionar prototipos. Nao enfraquecer -Werror. HALDMA/BTIF ainda
nao foram compilados neste build. Nenhum teste fisico/IRQ/DMA/clock no aparelho.

BTIF DMA alias: LinuxLG4.9 include/linux/dma-mapping.h654 implementa
dma_zalloc_coherent como dma_alloc_coherent(...,flag|__GFP_ZERO), sem outra
politica. Usar essa chamada explicita no6.18, mesmo dev/tamanho/dma_handle e
GFP_DMA|GFP_DMA32 existentes, acrescentando __GFP_ZERO. Reusar alocadorDMA
nativo, nao shim novo. Transporte/endereco/cache/mask e unwind nao mudam;
warnings de coherent_dma_mask e eventual devNULL devem ser resolvidos antes
de ativar. Buildalias nao validaDMA fisico. GPLv2LG e APIsLinux ja auditadas.

### BTIF core: API6.18 sem desligar tempo/recovery

Entrega pretendida: controladorBTIF real com espera/deepidle/logs funcionais;
aceite offline: core compila com API6.18 e limites/unidades originais mantidos.
Reusar Linux timekeeping/timespec64, class_create(nome), __ATTR e removevoid,
fonteLG GPLv2 ja auditada. Sem driver ou relogio proprio; mainline/pmaports/
Qualcomm da triagem nao substituem protocoloBTIF, APIsLinux sao as alternativas
compativeis. Registrosinternos logtimer/monotonic passam timespec64 (sem ABI
userspace exposta), realtime permanece realtime, monotonic permanece monotonic.
Microsegundos usados no detectorRX e logs sao tv_nsec/NSEC_PER_USEC, sem
alterar formulaLG de borrow ou threshold1s nesta adaptacao. Waitdeepidle usa
somente segundos como antes, agora64bits; nao trocar clock/limiar junto do port.
Formatossec64 ajustados para nao truncar; tsnanosecond64 com castlong onde
formato%ld exige noARM32. CallbackRXnotify so usado no mesmoC passa static.
Remove antes retornava0: adaptar void sem prometer teardownIRQ/DMA completo.
Sysfs flag0644 conserva callbacks, charclass conserva nome/erro; nao ativar
diagnosticosdestrutivos. Esforco pequeno/medio, testar detectorRX real contra
original, compilacao com -Werror e verificar proximo erro concreto.

Resultado BTIF desta etapa: workspaceisolado criado preservando origem4.9,
wrapper em artifacts/staging-btif-lts-20261027-v1. Build inicial para em header
mtk_io.h (work/btif-lts-initial-20261027-a.log). Apos headersprivados, erros
reais sao timeval/timespec incompletos, assinaturaremove, class_create2args,
DRIVER_ATTR antigo e helpersemprototipo em work/btif-lts-headers-20261027-b.log.
Nao ha objetoBTIF completo nem ko novo aprovado. Funcoes de tempo servem a
recovery/deepidle/logs, nao devem ser desligadas para compilar.

Patch btif-clock-probe-unwind-v1.patch aplicado e reverse dry-run fuzz0.
Teste tools/tests/test_btif_clock_probe.py fixa fontesLG porSHA, extrai
funcoesCCF/probeC reais: EIO/ENOMEM/EPROBE_DEFER nos doisgets/doisprepares
impede publicacao, falha segundo prepare desfaz primeiro, nova tentativa
obtem ambos e probe duplicado recusaEBUSY sem nova aquisicao. Passou
-Werror/UBSan em work/btif-clock-probe-host-20261027-c.log. Tentativaa rejeitou
contextoassimetrico do patch, corrigido sem fuzz; b detectou fixturedevice local
escapando por global, agora lifetimeestatico como device real. Sem supressoes.
Isso cobre aquisicao, nao remove/DMA; release de preparacao bem-sucedida ainda
requer lifecycle completo. Nenhum teste fisico ou ativacao deBTIF.

Proximo bloqueio: APIs tempo/remove/classe/sysfs em mtk_btif.c preservando
timeoutdeepidle/RX, depois APIexp/halBTIF/halDMA e seus recursos nativos reais.
WMT perfilBTIF real ainda exige24 simbolos; nao voltar aos fallbacks fracos.
XO/PWRAP segue outra dependencia antes de funcionamento no aparelho.

IncrementoBTIF de clocks: reusar CCF e ordemLG getbtif/getapdma/preparebtif/
prepareapdma. Falha no segundo prepare desfaz primeiro; probe retorna erro
antes de publicar drvdata/private_data. Sem alterar enable/nomesDT/voltagem.
Teste das funcoesC reais com erro/defer e nova tentativa; nao adaptar remove
geral ate auditar IRQ/DMA. PortAPI de tempo/sysfs/remove continua bloqueio de
build, nao desabilitar logging/timeouts. Mudanca pequena GPLv2LG nos arquivos
ja auditados, sem novo driver ou diagnostico.

### Controlador BTIF LG: workspaceisolado e dependencias de headers

Entrega pretendida: BTIF MMIO/DMA entregando comandos/eventosSTP reais; aceite
offline inicial: buildcontrolador original contra6.18 revela bloqueio concreto,
sem headerLinux4.9 nem fakeexports. C/SHA dos quatro objetos auditados na entrada
Transporte real abaixo. Workspace staging-btif-lts-20261027-v1 reaproveita
separacaoLG core/APIexp/halBTIF/halDMA e wrapperKbuild apenas; -Werror mantido.
CabecalhosLG copiados, GPLv2 conforme aviso individual, snapshot semcommit:
inc/mtk_btif.h SHA79f49640795659226494be48286a664f9895a51dc4da95187bf3623678bec0b5;
inc/mtk_btif_exp.h SHA28d7bbe6ec3f83f7dd644d55123b1b15b511b7b06384b15231b52cad50d7be78;
plat_inc/plat_common.h SHAf2ad10bd2e3ebfc18efc9b384c3df2c58f358ed49807edbd126126e8a3a840c9;
btif_pub.h SHA289b4a7ae4c6a12225a6d135409acb57b3c875d7f8ce8274b49ca73cb09645fc;
btif_priv.h SHA14edbe39bd58a0d4d7d3a10ccf0a8e734c3f1a65deb74ce8f4a23bb12d07427a;
btif_dma_pub.h SHA2c5ba3ffb223632762ff1dced732fea1c7650941e28a595cd96619f2a739c2f6;
btif_dma_priv.h SHAbdb1670c24fbc1c0442b3467471ad75bdf3baa851ebba5f76f0f2a763984a639.
Primeiro build para em mtk_io.h. Esse headerLG GPLv2 so define IOMEM em ARM64,
sem efeitoARM32; sync_write.h ja auditado com barreiras no WMT sera reutilizado.
Busca completa encontrou mt_irq_dump_status nos doisHALs (btif_plat.c1185 e
btif_dma_plat.c1304), portanto mtk-gic-extend.h NAO e dependencia inutil.
Tentativa de removerinclude foi revertida e patchdescartado antes de entrega.
Preservar headerLG GPLv2 SHA1429dbaba7b2d20f8499d2e91dc13a3a02513eee01847c64e444d6a6fcd77eba
somente como interface privada; funcao real continua exigida no modpost ate
adaptacao do diagnosticoIRQ existente, sem stub. mtk_io.h GPLv2 SHA256
707d297290f2f3a1ad827c14867c3ca09d32a2a74b9be9adce8674eb1ac1c9cb.
Nenhum comportamentoIRQ real e alterado. Mainline
irq/CCF/DMA sao frameworks a usar; outras stacks pmaports/Qualcomm/serdev
ja triadas nao fornecem equivalencia do protocolo/controlador e seguem nao
substitutas comprovadas. Nenhum novo driver ou diagnostico, so portar fonteLG
mais completa. LPAE/DMA e lifetime de probe/remove ainda anteriores a carga.

### Transporte real MT6765: incluir STP-BTIF, nao validar fallbacks fracos

Entrega no aparelho: comandos/eventos WMT trafegando pelo BTIF do SoC, anterior
ao Wi-FiAXI funcional. Aceite offline inicial: compilar adaptadorSTP-BTIF LG
real e tornar dependencias do controlador visiveis no modpost. Build anterior
sem CONFIG_MTK_BTIF usa weak fallbacks stp_core.c/wmt_ctrl.c/wmt_lib.c; portanto
nenhuma conclusao de transporte podia ser tirada do LD wmt_drv.o anterior.
DefconfigsLG muse6765_hdk_q/mmh4x entre outros habilitam CONFIG_MTK_BTIF=y.
Reusar common_main/linux/stp_btif.c MediaTek2016 GPLv2 original SHA256
cf6a3e066fba1cb185fdc97d560008b6def61c3ebff80345c7b2ea6d5c9fbb97.
Header/ABI mtk_btif_exp.h ja copiado e auditado abaixo. WrapperKbuild local
seleciona objeto original via CONFIG_MTK_BTIF:=y, sem fingir suporte na config
do kernel nem definir macro global. ControladorLG kernel4.9/btif/common e
candidato reutilizavel; Linux6.18 drivers/bluetooth/serdev/mtk-uart e mt76 nao
comprovam equivalencia deste transporteMMIO/DMA/WMT; QualcommSDIO e protocolo
externo tampouco. Auditar controlador/API/SoC antes de portar, nao desabilitar
SDIO/UART so para eliminar simbolos. Nenhum driver/diagnostico novo nesta
inclusao: selecionar fonte existenteGPLv2 e compilar -Werror proporcionalmente.
No aparelho load/flash/reset continuam nao autorizados por esta etapa.

Primeiro buildSTP-BTIF real para em missing-prototypes do helper
mtk_wcn_consys_stp_btif_rx (linha200). BuscaC/H no common encontra somente
definicao, sem export nem consumidor; tornarstatic preserva corpo/logging e
evita API global nao declarada. Build seguinte revela unused-function; inspecao
completa mostra corpo apenas return0, sem sequer dump deRX. Remover esse
placeholder vazio nao chamado/exportado, nao adicionar maybe_unused nem suprimir
warning. CallbackRX real passa por mtk_wcn_btif_rx_cb_register e permanece.
Reusar fonteLG, alteracao minima GPLv2. Nome do patchprivate-rx preservado como
identidade, conteudo final remove o placeholder inutil em vez de torna-lo API.

Resultado: wrapperlocal agora inclui CONFIG_MTK_BTIF:=y apenas noKbuild do
common. stp_btif.o compilou ARM32 -Werror, SHA256
3d2883dab4b8b85ec06fba9d1a5ec78809f78e9cf16aba532fe01b3f32d8c21d.
LD wmt_drv.o passou, nm confirma tiposT fortes em
mtk_wcn_consys_stp_btif_open/close/tx/parser_wmt_evt, nao W fracos. Modpost
agora recusa24 dependencias totais, nao12, em
work/wmt-lts-real-btif-20261027-c.log; comando seguinte nm retorna0 mas make
falhou, nao tratar como buildcompleto aprovado. As12novas dependencias sao
mtk_btif_exp_{rx_has_pending_data,rx_thread_get,tx_has_pending_data},
mtk_wcn_btif_{close,dbg_ctrl,dpidle_ctrl,loopback_ctrl,open,parser_wmt_evt,
rx_cb_register,wakeup_consys,write}. Nao substituir por no-op para recuperar
contagem antiga. Patchprivate-rx aplica/reverse dry-run fuzz0; nenhuma
funcaoRX real foi removida, placeholderreturn0 sem refs nao exige harnessnovo.

Triagem do controladorLG kernel4.9 btif/common, avisosGPLv2 por arquivo,
snapshot semcommit: mtk_btif.c SHA256
442f4fe1e19b4375fb42f57f6d1cbfb28e5cb3a8446735cd1e1ee89d8623ae67;
mtk_btif_exp.c SHA256
9f040ad26e7bcd49f9e175ce1d2d43418ef2f065aaf0a32e3633db40d45b32e6;
btif_plat.c SHA256
d3d076957ca30aa12d6b05cdfe7f52c6d6a51cb09f31c0e567355acf3dba17bf;
btif_dma_plat.c SHA256
531e41fdd19df5b67277dd5a59cfb39a73ae8d9d149cb8afd406ca0c64b90906.
Separacao existente e adequada: APIexp/core, backendhal BTIF e backendDMA;
perfilMT6765DT informa base1100c000/1000, TXDMA11000880/80,RXDMA11000900/80,
IRQsSPI112/132/133, CCF infracfg BTIF/AP_DMA nomesbtifc/apdmac. Candidato
preferido por compatibilidade de placa e ABI; nao reimplementar sobre UARTsem
demonstrar equivalencia. Licencasheaders/dependencias ainda confirmar ao copiar.

Bloqueios reais a portar antes de carga: mtk_btif_probe publica private_data
e ignora retorno hal_btif_clk_get_and_prepare; hal prepara dois clocks e nao
desfaz primeiro se segundo falhar. Remove apenas zera drvdata/private_data,
nao drena IRQ/DMA/thread explicitamente. of_iomap usa busca global noshal,
DMA depende de mtk_lpae.h, ownership/cache/mask e unwind precisam verificacao
com DMAAPI6.18. Erros de openSTP tambem precisam tratar rxthreadNULL antes de
ler comm. Proxima entrega concreta: copia isolada do controladorLG auditado,
compilar e adaptar aquisicao/IRQ/DMA no caminho real; nao novos diagnosticos.
Nada carregado ou ativado no aparelho nesta etapa; transporte segue nao
funcional, mas buildagora exige a implementacao que faltava em vez de fallback.

### Probe WMT: falha de log propagada e recursos anteriores gerenciados

Entrega pretendida: WMT so publica pronto com log/coredump inicializados; falha
na aquisicao desfaz recursos e preserva errno antes de qualquer pedidoON.
Aceite offline: EPROBE_DEFER/ENOMEM/erroIRQ percorrem backend/probe, sem
panelstart/abertura de energia, log drena antes de liberar coredump e mapas
anteriores liberados por devres. Sem probe ou ensaio no aparelho.
Reusar fonteLG GPLv2 mt6765/core e APIs Linux6.18 platform_get_irq,
of_address_to_resource/devm_ioremap/devm_add_action_or_reset. Alternativas
mainline/pmaports/Qualcomm ja comparadas: APIs nativas servem para ownership,
nao substituem layout de registradores/firmwareMT6765. Nenhum driver/framework
novo. devm_of_iomap/recurso exclusivo nao e equivalente a of_iomap LG para
SPM/INFRA/RGU compartilhados: manter mapping nao exclusivo, DT traduzido e
checado MEM/tamanho, sem adicionar donos de MMIO ou novas escritas.
Montar struct local e publicar conn_reg somente apos11 mapas validos; acao
devres zera campos antes dos unmaps. Falha anterior nao publica mapas parciais.
Clock/genpd/supplies ja gerenciados ficam no unwind automatico do probe.

Backendlog usa platform_get_irq(2) com erro/defer real, utilinit checado; se
charlog opcional falhar, drenar util e retornar erro (nao habilitar opcaoAndroid
aqui). Core checa coredump/log e mantem flag de log realmente inicializado.
Cleanup unico drena log, depois unmapcoredump, antes de apagar globals; em erro
primeiro pararpanel/energia. Coredump recusa ponteiroNULL/duplicado e retorna
ENOMEM na falha de map. Admission inicialmente fechado e reaberto so ao fim
probe; rebind nao limpa fault. Pequenas extensoes nos doisC existentes, origem/
licencas ja fixadas, teste dirigido de init/unwind e build proporcional.

Resultado: wmt-probe-log-unwind-v1.patch aplicado/reverse dry-run fuzz0.
Backend/core ARM32 -Werror e LD wmt_drv.o passaram no comando de aplicacao;
modpost continua recusando12 simbolos vendor, nenhumko.
Backend fonteSHA256
1c8d1ffc0321edb64cccf9e3fcc034355fd77a1fdf1c20740bf6f5b45bcbab8d,
objetoSHA256
2e580b9bb51cedb7321e8b18f855acdf2cb5de145b78e6d4f7e5aab0e3a906cf;
core fonteSHA256
1f3610e6aa79cc36867885f34fb0319e8a5c4e46068a1760652d65ae4aa93270,
objetoSHA256
6590b6e49953e0effa65cba229889492f6b33efc0d2c5421a1fc6f3da3d90f20.

Teste tools/tests/test_wmt_probe_init.py fixa fontesintegradas, originalbackend
LG e header porSHA, executa funcoesC reais de mapper/log/coredump/probe/remove.
Compara campos de mapa ao sucesso4.9 original, nao tabela duplicada do port.
Falha em cada um dos11 mapas, resource naoMEM/curto/desalinhado, translate/defer
e registrodevres preservam erro e nao publicam mapas parciais. Reserve/PMIC/
panel/domain, limpezaEMI, MPU, coredump, IRQ e utilinit falhos nao abrem energia
nem panelstart. Cleanup libera log antes de coredump, zera globais e devres
limpa conn_reg antes dos unmaps. Sucesso/remove tambem verificados. Os dois
ramos da chamada charlog compilados, mas fw_log_wmt_init/deinit sao doubles:
isso NAO porta nem valida a implementacaoAndroid opcional (continua desativada
no build nativo). -Werror/UBSan/pthread passou em
work/wmt-probe-init-host-20261027-a.log.

OF/MMIO/devres/firmware/PMIC/domain sao fornecedores simulados nesse teste; nao
executa probe real, MPU, remap fisico ou callbacks de IRQ no aparelho. Fixtures
genpd/admission e EMI atualizaram apenas SHA de dependencia e passaram em
work/wmt-probe-native-genpd-host-20261027-a.log e
work/wmt-reserved-memory-host-20261027-j.log, criterios anteriores mantidos.
Recurso de pinctrl/GPS opcional conserva comportamentoLG, nao e prova de GPS.
Faltam unwind eletrico sob falhas de power, acessosdebug diretos e integracao
da ponte/transporte e XO/PWRAP nos12 simbolos ainda ausentes. Proximo foco deve
ser esses caminhos reais da placa, sem criar stubs ou confundir link com Wi-Fi.
Nenhuma alteracao de DT de boot ou operacao no aparelho nesta etapa.

### Callbacks log: lifetime entre modulos via SRCU Linux

Entrega pretendida: descarregar consumidor de logs sem executar callback no
texto ja liberado. Aceite offline: unregister/substituicao aguarda callback
antigo em voo, novos eventos usam ponteiro novo/NULL e callback pode dormir/
reentrar APIread. Reusar DEFINE_STATIC_SRCU/srcu_dereference/rcu_assign_pointer/
synchronize_srcu Linux6.18 (CONFIG_TREE_SRCU=y no build), nao contador ou
frameworkRCU proprio. FonteLG connsys_debug_utility.c GPLv2 apos lifecycle
f62f3cf668f9a0e2466a986f737c4873bf2239363b6120cf26a4bd87ee92959b.
Mainline/pmaports/Qualcomm triados nao substituem ABI de logsMT6765, mas SRCU
e o framework compatvel para callback de worker que pode dormir. Inspecao dos
consumidoresLG WMT/WiFi/BT/GPS encontrados mostra callbacks de wakeup de fila,
init/deinit em contexto de processo; nao registram/removem callbacks de dentro
do proprio callback. Essa ultima operacao seria deadlock de grace period e
nao e contrato suportado. Mutex de atualizacao serializa register/unregister,
sem segurar mutexAPI nem spinlocks durante synchronize_srcu.

Publicar ponteiro novo diretamente, depois aguardar antigos: nao introduzir
janelaNULL que perca wakeup durante substituicao. Deinit usa mesma API comNULL.
Callback executa sob read-sideSRCU e verificaactive, preserva fechamento/drain
do lifecycle. Substituicao/unregister retorna quando pointerantigo nao pode
mais executar; nao faz teardown de EMI ou garante ownership de pointercru.
Pequena extensao no arquivo existente; teste pthread de callback suspenso e
unregister/replacement bloqueados, buildARM32 com exportsSRCU reais.

Resultado: wmt-connsys-log-callback-srcu-v1.patch aplicado/reverse dry-run fuzz0.
Utilitario ARM32 -Werror e LD wmt_drv.o passaram; exportsSRCU resolveram com
vmlinux.symvers do mesmo build, modpost ainda recusa12 simbolos vendor em
work/wmt-lts-log-srcu-20261027-b.log. Fonte utilitarioSHA256
3f5c247eb6babdd2a52cfb090b2dfb2b3f040ff3a391ad9d0e0aaebb27292195;
objetoSHA256
2afb4ee5440027684d86da053d6ad15ac5ceceb45fcf23460753df77b3be6a89.
Primeiro build detectou static duplicado (DEFINE_STATIC_SRCU ja contem static);
corrigido no patch sem alterar macro/framework ou relaxar -Werror. Dry-run
anterior tambem detectou contagem errada no hunk, corrigida sem aumentar fuzz.

Teste tools/tests/test_wmt_log_callbacks.py reaproveita hashes/fixturesLG do
teste lifecycle e aplica os tres patches; executa funcoesC reais de evento,
registro/deinit e sizeAPI. ModeloSRCU pthread de duas epocas representa grace
period, nao o algoritmoLinux. Callbackantigo fica suspenso e reentraAPIread;
unregister so retorna apos termina-lo e novos eventos nao o chamam. Na
substituicao, callbacknovo recebe eventos durante a espera pelo antigo, sem
janelaNULL/wakeup perdido no modelo. Indiceinvalido recusado, activefalse nao
chama callback. Passou -Werror/UBSan/pthread em
work/wmt-log-callback-srcu-host-20261027-a.log. Nao houve modulo ou callback
fisico; nao se demonstrou unloadreal ou encerramento completo do consumidor.

Proximo bloqueio concreto permanece nos chamadores: backend
consys_dedicated_log_path_init e probeWMT ignoram falha de initlog. Propagar
erro e limpar coredump/recursos anteriores sem liberar recurso ainda publicado;
sem isso, retorno correto do utilitario nao prova falha segura do probe.
XO/PWRAP e outros12 simbolos ainda pendentes. Nenhuma acao no aparelho.

### CONSYS log: fechar produtores e drenar antes de liberar EMI/cache

Entrega pretendida: logsfirmware WMT e remove/falha sem callback tocando memoria
liberada. Aceite offline: fechar active, impedir agendamento/rearme, cancelar
alarme fora de spinlock, sincronizarIRQ/timer/work antes de unmap/free e
desfazer init parcial. FonteLG debug_utility/connsys_debug_utility.c GPLv2
original8dbe8597 e portAPI anterior ja auditados abaixo. Reusar utilitarioLG,
mutex/spinlock, alarm_cancel/free_irq/timer_shutdown_sync/cancel_work_sync
Linux6.18; mainline/pmaports/Qualcomm nao fornecem layoutEMI equivalente, conforme
triagem anterior. Nenhum driver, protocolo, diagnostico ou framework novo.

Mutexinit serialize init/deinit; mutexAPI protege leitores/controles de processo
e publica active. Fechar active sob mutexAPI+irqspin antes do drain, soltar
mutexAPI enquanto espera work (callback pode chamar API), depois liberar sob
mutexAPI. Spinlocks globais estaveis, flagsIRQ locais: nao reinicializar locks
contra chamadas concorrentes. Alarm callback rearm apenas active/enable/blank0;
APIenable/disable/blank serializadas e cancel fora de alarmspin. Recusar periodo0
para nao criar wakeup/rearm imediato infinito. Inicializar timer/work/alarm antes
de IRQ, rastrear IRQ realmente registrado. Falhas map/cache/requestIRQ retornam
erro real e limpam recursos; nao apagar logs ou desativar alarm para compilar.

Leitores/dump/size de processo recebem gate e mutexAPI; validar indice/bounds
antes de formar ponteiro. Getter de EMI crua e contrato de emprestimo: retorna
NULL fora deactive, mas pointer entregue antes de stop exige quiescencia do
consumidor. Remocao de callback de outro modulo tambem exige verificar lifetime;
READ/WRITE_ONCE evita dupla leituraNULL, nao substitui sincronizacao de unload.
Essas lacunas continuam bloqueios de carga, nao criar abstrao universal para
esconde-las. Esforco medio focado nas falhas reais; teste dirigido de callbacks,
ordemdrain e falhasinit, buildARM32 antes da integracao de consumidores.

Resultado: wmt-connsys-log-lifecycle-v1.patch aplicado/reverse dry-run fuzz0.
Utilitario ARM32 -Werror e LD wmt_drv.o passaram em
work/wmt-lts-log-lifecycle-20261027-a.log; modpost continua recusando12 simbolos
vendor, semko. Fonte utilitarioSHA256
f62f3cf668f9a0e2466a986f737c4873bf2239363b6120cf26a4bd87ee92959b;
objetoSHA256
9771d9ae19095b6e1b42cc07e5905b9a6d0b5bb833cd0e0dab3f0cc27acd6a39.

Teste tools/tests/test_wmt_log_lifecycle.py fixa originalC e headersLG GPLv2:
connsys_debug_utility_emi.h SHAae2fd874949fd2d8d9c65afdcaef0e58644ae3926fa0d7f390a39b0229ee8dd5,
connsys_debug_utility.h SHA220f1703df48b42eec431e745ba7531c6d91a105b4f554acf4c627e51b7c61be.
Aplica patchAPI e lifecycle, extrai structs/tabelas/constantes e funcoesC reais.
OF/MMIO/IRQ/timer/work/allocator sao doubles, nao placa. Falha map, cada uma
das5 alocacoes e requestIRQ limpam tudo e preservam errno. Dois ciclosinit/
deinit, rejeicao de init duplicado e deinit repetido sem efeito. Trace real
deinit fecha active antes de freeIRQ/alarm_cancel/timer_shutdown/cancel_work,
depois5 frees e unmap. Doubles entregam ISR/alarm/timer/work durante drain e
verificam ausencia de novo schedule/rearm; callback em drain reentra APIread
sem mutexAPI segurado. Periodo0 recusado, UINT_MAX valido; disable/blank impedem
rearm e cancel ocorre sem spinlock. Worker ativo exercita seu rearm guardado.
Dumpindices/bounds e getter fora deactive nao acessam mapa. Passou -Werror/UBSan/
pthread em work/wmt-log-lifecycle-host-20261027-b.log; tentativa a apenas faltava
sys/types.h para ssize_t no harness, corrigido sem suprimir warnings.

Busca nos C/H connectivityLG fornecidos nao encontrou consumidor do getter de
EMI crua. Os consumidores get_buf_size encontrados sao poll de arquivo em
fw_log_wmt/gps/wifi/bt, contexto de processo sem spinlock nesses callsites;
mutexAPI e compativel com eles. Isso nao comprova outros binarios/consumidores
futuros. Callbackunregister entre modulos ainda nao espera callback em voo;
READ/WRITE_ONCE nao prova lifetime do codigo do consumidor. Proximo bloqueio:
coordenar esse unregister e propagar falha do initlog em consys_dedicated_log_path_init
e probeWMT (ainda ignoram retorno), com cleanup de coredump/recursos anteriores.
Leitoresread/to_user foram compilados e revisados, nao se executou copiauser real
ou ringtransport real. Nenhuma IRQ/timer fisica ou operacao no aparelho.

### Paldo/power/remove: admissao compartilhada e falha parcial explicita

Entrega pretendida: transicoes de alimentacaoWMT nao competem com paldo ou
remove e erro parcial nao e repetido como ciclo novo. Aceite offline: mesma
trava para entradas de energia, parada fecha novas chamadas antes de liberar
recursos, erro real chega ao chamador e latchcore bloqueia reexecucao. Sem
recuperacao eletrica ou operacao fisica autorizada nesta etapa.
Reusar mutex/ops e corposLG GPLv2 ja integrados, sem driver/scheduler novo.
Mover mutex de sequencia para estado do core, adicionar stopping/fault; retirar
mutex de wrappers internos usados pela propria sequencia (efuse no reg_ctrl)
para nao causar recursao. Wrappers publicos bt/wifi/vcn28/efuse passam pela
mesma trava e exigem dominioativo via preflightOFF nativo (nao executaOFF).
Outros perfis sem callback mantem caminhoLG, com errosint agora propagados.
Falha preflight EALREADY/ENODEV nao vira falha parcial: nao houve efeito.
Falha apos reg_ctrl/GPIO ou paldo real registra faultcore, sem alegar railsOFF.
Reset falho conserva status/PDMA anteriores. Remove adquire a trava, fecha
admissao e solta antes de cancelarpanel/recursos: nao esperar work sob mutex.
Probe so reabre admission ao fim; rebind nao limpa fault nem equivale a recovery.
Alternativas mainline/pmaports/Qualcomm triadas nao fornecem esta politicaWMT;
mutexLinux e gate no core existente sao extensao pequena, sem generalizacao.
Testes dirigidos ampliam harnessgenpd existente para paldo vs power, stop e
erroPMIC com dominio ainda saudavel. Log workers, acessosdebug diretos e unwind
eletrico continuam a revisar antes de carga; stopping nao promete desligamento.

Resultado: wmt-connsys-paldo-quiesce-v1.patch aplicado e reverse dry-run fuzz0.
Core ARM32 -Werror e LD wmt_drv.o passaram no comando apos aplicacao; modpost
continua recusando12 simbolos vendor, nenhumko. Log
work/wmt-lts-paldo-quiesce-20261027-a.log corresponde somente a modpost antes
de aplicar (dry-run inicial rejeitou indentacao de um hunk); nao conta como
recompilacao. Corrigida tabulacao sem mudar fuzz, comando seguinte recompilou
core e LD. Core objetoSHA256
b5fb096b19aa3b4c15542a35e8cb1529227f6ef44a0d0c970c17b38441efbee8;
fonteSHA256
6b6be5694a46a05c30e76ede939474360de8f6d01bbc4a56f6db8f299de71744.

Harnessgenpd/admission existente atualizado por esseSHA e inclui wrappersC
paldo publicos/privados e quiesce reais. Railcallbackdouble exige dominioativo:
paldo concorrente com OFF completa antes dele ou recebeEALREADY depois,
sem acesso a dominioOFF. FalhasEIO em BT/WiFi/VCN28/efuse reais propagadas
e latchcore impede PMIC/STEP em repeticao. Efuse co-clock0 permanece no-op LG.
ErroPMIC simulado antes de pedirgenpd (backendgenpd semfault) agora bloqueia
as entradaspublicas. ErroGPIOon impedeJTAG; GPIOoff e erro de reset tambem
latchamcore. ResetONfalho conserva status/PDMA sem anunciar recuperacao.
Quiescefecha power/on/off/reset e paldo comESHUTDOWN antes de efeitos; releases
do backend sao exercitados separadamente. Testes anteriores de attach/PMref
e admissao mantidos. -Werror/UBSan/pthread passou em
work/wmt-paldo-quiesce-host-20261027-b.log. TesteEMI dependente porSHA passou
em work/wmt-reserved-memory-host-20261027-i.log, criterios inalterados.

Limites: a prova de admissao substitui o corpo reg_ctrl/GPIO por doubles, nao
energizaPMIC nem garante rollback; operacoes de log/debug diretas nao entram
nessa trava. Parar nova energia nao para timer/IRQ/work existentes. Proxima
entrega offline deve drenar esses produtores antes de iounmap/free, reutilizando
o utilitarioLG e APIsLinux, e consolidar unwind de rails. XO/PWRAP e restante
dos simbolos vendor seguem pendentes. Nenhum acesso ao aparelho nesta etapa.

### Entrada de power/reset: preflight antes de PMIC e serializacao

Entrega pretendida no aparelho: falha incerta ou transicao duplicada nao repete
alimentacao/STEP/MMIO antes do gate genpd. Aceite offline: preflight real do
backend ligado a corepwr_on/off/rst, duas entradas simultaneas so executam uma
transicao, falha para antes de efeitos iniciais. Sem operacao fisica.
Reusar mutexLinux no coreLG GPLv2 e estado native-genpd ja integrado; nao novo
contador paralelo, scheduler ou framework de recovery. Vetorops interno recebe
callbackint preflight com tipoHW_POWER_CTRL ja existente; apenas6765 preenche,
demais perfis continuam caminhoLG com retorno0 de preflight ausente.
Backend consulta dev/fault/active sob mutex e retorna ENODEV/EUCLEAN/EALREADY;
controlePM real conserva rechecagem. Core usa mutex de sequencia nos tres
entrypoints publicos, corpoLG em helpers locked; reset preflightOFF antes de
status/PDMA, on/off antes de STEP. Ordem de sucesso preservada. Mainline,
pmaports e Qualcomm triados nao fornecem politica especificaWMT; mutex e
ops existente sao extensoes pequenas ao caminho completoLG, sem driver novo.
Wrappers paldo avulsos e remove/workers ainda nao compartilham essa transacao;
nao declarar todo o lifecycle serializado. Teste dirigido no harnessgenpd real
existente com entrypointsC reais e doubles apenas para corpo reg_ctrl/GPIO,
build por dependenciaheader proporcional antes da proxima integracao.

Resultado: wmt-connsys-power-admission-v1.patch aplicado e reverse dry-run
fuzz0; objetos dependentes do headerops recompilados -WerrorARM32, LD wmt_drv.o
passou. Modpost continua recusando12 simbolos vendor em
work/wmt-lts-power-admission-20261027-a.log, semko.
Core objetoSHA256
4bb90570c877d72a4afd57a0c9f4d19cc1e91636f51d7fb5f850c340742be740;
core fonteSHA256
b31a7348da522cb8edf521124515d072a3eaa6b8c05adc247623b8d21b298052;
backend fonteSHA256
7461c4943e7479d87e90fc5ae9e5e974c2b0d80255c08dedd856d285062bc1a1.
Power-off externo tambem deixa de executar GPIO depois de reg_ctrl falho,
mantendo retorno original em vez de somar outro erro.

Harnessgenpd anterior ampliado com metodo que fixa essas duas fontesintegradas
porSHA (fixtures privadas, inclui patches previos) e extrai preflight/entradas/
helpersC reais e backendgenpd real. Doubles apenas para reg_ctrl interno, GPIO,
STEP e efeitos de reset: contadorPMIC e incrementado antes do callbackpower,
permitindo verificar ausencia desse efeito apos preflight falho. Dois threads
de power-on/off passam uma unica transicao e umaEALREADY, uma referenciaPM,
GPIO e STEP unicos; reset normal executa off/on e restaura calibracao no modelo.
ENODEV sem attach, EALREADY em off/reset inicial e EUCLEAN apos faultgenpd
impedem novos STEP/PMIC/status/PDMA. Falha do off nao chamaGPIO. Ausencia de
ops recusaENODEV; callbackpreflight ausente preserva fallbackLG. -Werror/UBSan/
pthread passou em work/wmt-power-admission-host-20261027-a.log, incluindo os
testes anteriores de attach/PM/cleanup. TesteEMI dependente reexecutado comSHA
novo em work/wmt-reserved-memory-host-20261027-h.log, criterios inalterados.

Limites: latchgenpd nao registra sozinho falhasPMIC anteriores ao pedidoON.
Falha apos dominioOFF mas antes de railsOFF exige fase/unwind explicitos;
EALREADY nao pode ser interpretado como recuperacao da alimentacao. Paldo
avulso e remove/workers ainda podem competir com a sequencia, logo lifecycle
e falhas parciais ainda bloqueiam carga. Harness nao executa reg_ctrl/MMIO real
nessa prova de admissao, nem confirma recuperacao eletrica. Nenhum DT ou
dispositivo foi ativado. Proximo: coordenar esses consumidores e estado parcial,
depois XO/PWRAP e restante das dependencias antes de ensaio.

### MT6765 WMT: attach explicito e runtimePM no provider genpd existente

Entrega pretendida: dominioCONN nativo acionado na posicao LG apos rails/reset,
nao por um clockMTCMOS inexistente. Aceite offline: attach/releaseOFF sem ON,
resume/put balanceados, falhas propagadas e retry bloqueado no backend quando
estado incerto. Sem alterar DT de boot nem ensaio fisico nesta etapa.
Reusar of_genpd_add_device/pm_genpd_remove_device e runtimePM Linux6.18.58
GPL-2.0/exportsGPL no providerMT6765 ja adaptado/testado abaixo. Alternativas
mainline/pmaports/Qualcomm comparadas abaixo nao mudam o hardware nem tornam
CCF uma API de dominio; nao criar segundo driverSPM ou novo sequenciador.
BackendLG mt6765.c GPLv2 recebe somente glue de recurso/estado; core mantem
ordem ja existente e os gates de erro anteriores. Remover branch manualSPM
desativado e clockMTCMOS do backend para nao duplicar controle/protecoes do
provider genpd (timeout, ACKs, isolamento, bus protection ja testados).

ReferenciaDT de staging: mediatek,conn-power-domain = <&controller 0>, provider
compatible mediatek,mt6765-power-controller, um argumentoCONN0. Proibir
power-domains no noWMT: platform faria ON antes do probe. Prop custom minima
transporta spec padrao #power-domain-cells para attach explicito sem power_on;
nao inventar dominio extra para escapar attach automatico. Nenhum enderecoSPM
hardcoded novo. Necessaria validacaoDT antes de qualquer boot; rejeicao no
probe nao desfaz efeitos que platform ja tenha feito com DT errado.
Attach exige PMruntime ainda desabilitado e nenhum pm_domain anterior; marcar
suspended sem write e habilitar PMruntime. Devres registrado depois dos supplies
remove dominio antes de liberar handlesPMIC. Mutex serializa controle/cleanup;
estadoactive evita get/put duplicado. resume_and_get balanceia erro de get;
put_sync_suspend decrementa usage mesmo em erro: restaurar get_noresume antes
de registrar fault, nao autorizar nova transicao incerta. Cleanup em falha nao
tenta novo acesso de energia: desabilita PM e remove associacao sem alegar OFF.
Fault mantido bloqueia rebind no mesmo modulo; reload/reboot nao sao recovery
comprovada. Lib/PMIC workers e gate de retry antes das etapasPMIC ainda pendem
auditoria; isso e integracao offline, nao permissao de carga. Esforco medio,
teste dirigido do glue real e build com provider/simbolos do mesmo kernel.

Resultado: wmt-mt6765-native-genpd-v1.patch aplicado/reverse dry-run fuzz0.
Backend6765 ARM32 -Werror e LD wmt_drv.o passaram; as APIsgenpd/runtimePM
resolvem com vmlinux.symvers do mesmo build. Modpost ainda recusa12 simbolos
vendor em work/wmt-lts-native-genpd-20261027-a.log: semko carregavel.
Objeto6765 SHA256
540713f5131fe1d2b1d8aa80fc2559082af783cb380addf4f21b94235a61ed1a.
Nenhum clock conn sintetico ou segundo acessoSPM implementado, providerOFF
validado e suas protecoes permanecem inalterados.

Harness tools/tests/test_wmt_native_genpd.py fixa fonteLG porSHA, aplica hunk
backend do patchpower-clock anterior e patchgenpd; extrai estado/funcoesC reais.
OF/runtimePM/devres doubles verificam attach/releaseOFF sem resume/suspend,
phandle/cells/compatible/status/DTautomatico errados, PM ou dominio preexistente,
provider ausente/defer, falhas set_suspended e registrodevres. Sucesso0/positivo
PM normalizado; activecleanup faz uma suspensao. Dois threads pthread ON e OFF
simultaneos deixam um sucesso e umEALREADY, uma referencia por ciclo. Falha de
resume nao aumentausage; falha de put restaura referencia, latch bloqueiaretry;
cleanup balanceia uso sem novo acessoHW e mantemfault atraves de rebind.
RemoveEAGAIN e explicito, nao success. Passou -Werror/UBSan/pthread em
work/wmt-native-genpd-host-20261027-b.log; tentativa a detectou indentacao
ambigua somente nos doubles, corrigida sem relaxar flags.

Limites: doubles nao executam callbacksgenpd reais, OFlookup, sleep/suspend ou
MMIO. Remocao com fault pode deixar dominio/rails fisicamenteON; balancear uso
PM e remover associacao nao e rollback eletrico. Falha de remove deve ser
tratada junto de teardown/worker e mecanismo de recuperacao antes de carga.
Backendlatched nao impede por si so que core tente PMIC/pinmux antes de chegar
ao callbackpower; gate na entrada de transicao ainda e proximo bloqueio.
Nao ha DT consumidor ativado nem boot/ensaio fisico. XO/PWRAP continua separado.

### Dominio nativo: ordem de attach e erros de power/clock

Entrega pretendida: CONNSYS energiza apenas depois de PMIC pronto e falha de
dominio/clock nao permite ler chip/soltar reset ou remover rails ainda usados.
Aceite offline desta etapa: erro dos callbacksint existentes chega ao chamador,
sucesso mantem sequenciaLG; sem attach ou pedidoON fisico.
Inspecao Linux6.18.58 GPL-2.0 drivers/base/platform.c platform_probe chama
dev_pm_domain_attach com PD_FLAG_ATTACH_POWER_ON antes de drv->probe.
drivers/pmdomain/core.c genpd_dev_pm_attach, para exatamente1 power-domain,
chama __genpd_dev_pm_attach(...,true) e genpd_power_on antes do probeWMT.
Portanto nao basta colocar power-domains no noWMT: isso inverteria PMIC/dominio.
of_genpd_add_device e APIexportadaGPL existente que so associa dispositivo;
nao chama genpd_power_on. Candidata para attach explicito apos adquirir recursos,
com referenciaDT separada que nao dispare attachautomatico, runtimePM e
pm_genpd_remove_device em teardown. Nao implementar DT artificial multi-domain
ou desabilitar protecoes do provider para contornar ordem. ProviderOFF ja
validado abaixo continua intocado; nenhum novo driver/provider e necessario.
Reusar mainline/genpd e fonteLGGPLv2; alternativas pmaports/Qualcomm ja triadas
nao trocam esta ordem eletrica por uma chamada CCF. A escolha de referenciaDT,
lifecycle/fault latch e unwind ainda deve ser integrada antes de carga.

Bloqueio concreto no consumidor atual: core ignora retornos de clock_buffer,
hw_power e ahb_clock em ambos sentidos, embora backend6765 ja devolva erro
de clk_prepare_enable. Adaptar somente esses seis pontos existentes para
propagar erro antes de proximo callback; nao alterar ordem ou acrescentar
write. Backend nao deve logar sucesso de clk_prepare_enable quando falhou.
Teste dirigido no harnessC de core existente, build dos objetos afetados;
isso nao implementa genpd nem garante unwind de rails anteriores.

Resultado: patch wmt-connsys-power-clock-error-gates-v1.patch aplicado e reverse
dry-run fuzz0. Backend/core ARM32 -Werror e LD wmt_drv.o passaram; modpost ainda
recusa12 simbolos vendor em work/wmt-lts-power-clock-gates-20261027-a.log.
Core objetoSHA256
54b3ff75d73ab4c062d6a9d8df6c1f90cf482c39fa37d322691f0f8455768e4f;
fonteSHA256
5cb0375dc778fe1ffb95a22fc6f54e408ebdbf10359357760b8f7a5c54e6962e.
HarnessC VCN28 existente ampliado para os seis callbacks reais de reg_ctrl:
sucesso coincide com funcao anterior com/sem co-clock, on/off. EIO/ETIMEDOUT em
XO/power/AHB sao devolvidos exatamente, sem callback seguinte/chipid/soltar
reset; falhas no off nao continuam ate remover18. Funcoes e patchesC reais
extraidos dos originaisLG com SHAs fixados, nao copia da implementacao em Python.
Passou -Werror/UBSan em work/wmt-power-clock-gates-host-20261027-b.log; tentativa
a detectou include string.h ausente apenas no harness, corrigido sem suprimir
warning. TesteEMI da fonte dependente atualizado e passou em
work/wmt-reserved-memory-host-20261027-g.log, criterios de memoria mantidos.

Limites: callback6765 clock_buffer ainda devolve0 pois adapterLG descartava bool,
e disable do antigo clockMTCMOS e void. Os novos gates nao inventam falhas que
backend nao reporta, nao implementam providerXO ou runtimePM. Estado apos erro
nao e comprovadamente recuperado; rails anteriores podem permanecer ligados.
Attach explicito e fault/retry/unwind devem ser integrados antes de ensaio.
Sem alteracao de DT de boot, providerOFF validado ou qualquer acao no aparelho.

### Rail VCN28: nao mascarar falha regulator no backend/core

Entrega pretendida no aparelho: railVCN28 a2.8V para efuse/FM/GPS, erro interrompe
sequencia antes de reset/SPM ou remocao de18. Aceite offline: equivalencia do
sucessoLG, retorno set_voltage/enable/disable preservado ate core/wrappers e
compilacao dos objetos atingidos. Sem operacao fisica autorizada.
Reusar reguladorMT6357 nativo6.18 e fonteGPLv2LG mt6765/core ja fixada porSHA;
nao criar controle paralelo nem alterar constraint2.8V. Framework trata
contagem enable e propagacao, nao adicionar segundo contador local para duplicar
estado. Primeiro verificar handle, set_voltage e so depois enable; disable
devolve erro sem continuar removendo rail18. WrappersVCN28/efuse e core devem
devolver erro antes de log de sucesso/proximo passo. Co-clock0 nao usa efuse
separado como antes; preservar opcionalidade de ops para outros perfis.
wmt_plat_soc_paldo_ctrl ja retorna iRet dos dois wrappers, sem mudanca necessaria.
Alternativas mainline/pmaports/Qualcomm triadas abaixo: regulator API nativa e
compativel; nao substituir este rail por API PMICgenerica, stub ou mt76. Mudanca
pequena nos doisC existentes, mesma origem/licenca, teste dirigido em harness
VCN28 existente em vez de suite ampla. Rollback de18/pinmux/XO apos falha ainda
precisa consolidacao; este gate nao equivale a recuperacao eletrica completa.

Rastreamento adicional: wmt_ctrl_soc_paldo_ctrl e wmt_core_ctrl ja devolvem
erro, mas wmt_ic_soc.c apos "turn off VCN28 after reading efuse" ignora iRet e
continua init. Acrescentar guard imediato no fluxoLG GPLv2 ja auditado e
compilar objeto; tres linhas de propagacao nao justificam novo simulador de
init de firmware. Nao desabilitar osal_assert existente em wmt_core_ctrl.
Guard nao transforma essa chamada em recuperacao completa nem valida firmware.

Resultado: patch wmt-mt6765-vcn28-rail-errors-v1.patch aplicado/reverse dry-run
fuzz0. Backend/core e LD wmt_drv.o passaram -WerrorARM32; modpost continua
recusando12 simbolos em work/wmt-lts-vcn28-rail-20261027-a.log. mt6765.o SHA256
2c2e8252ef81dcee71f89e4cf1243f8e9e316d6e2a9197730779ec60d40f6df4;
core fonteSHA256
50082ee1e61a4efb650a981c55899005bd3791a096b359ef694154a5ce4532ed.
FixtureEMI atualizada por dependencia e passou em
work/wmt-reserved-memory-host-20261027-f.log, sem alterar criterios.
HarnessVCN28 existente ampliado para backendrail e wrappers/coreC reais;
sucesso original/portado tem voto2800000 e enable/disable na mesma ordem.
EIO de set_voltage nao chama enable; EIO de enable/disable preservado, disable
falho mantem contagem no modelo. Handle ausente recusaENODEV. Nos dois modos
co-clock, falhas no on nao chegam a resetbit e falha no off nao desliga18.
WrappersFM/GPS/efuse propagam erro; efuse com co-clock0 continua sem operacao.
Passou -Werror/UBSan em work/wmt-vcn28-rail-host-20261027-a.log; criterios
anteriores de modo/rollback preservados, sem suite ampla repetida.

Guard em wmt_ic_soc.c revisado no fluxo real e patch
wmt-soc-efuse-off-error-v1.patch aplicado/reverse dry-run fuzz0. ObjetoSoC
recompilou e LD passou em work/wmt-lts-efuse-off-20261027-b.log; modpost ainda
recusa12 dependencias, semko. Logsuffixa foi apenas modpost sem recompilacao,
pois primeira versao do patch era rejeitada por contexto assimetrico; corrigido
contexto sem relaxar fuzz. Nao foi executado sw_init completo com firmware.
Ninguem tocou nas protecoes/asserts existentes ou no aparelho. Unwind de
alimentacao anterior, estado de falha/retry e providerXO/genpd continuam
necessarios antes de qualquer ensaio.

### VCN28 HW0: preservar campos via regmap com retorno de erro

Entrega pretendida no aparelho: selecao de modoVCN28 correta durante power-on;
aceite offline deste incremento: regmapMT6357 e bit1OP_EN/OP_CFG equivalentes
ao LG, erro impede proximo passo e restaura campos afetados quando possivel.
Reusar regmap/regulator/MFD existentes6.18, fonteLG mt6765.c GPLv2 e offsets
MT6357 ja auditados. APIregulator nao oferece este seletorHW0; nao reinterpretar
REGULATOR_MODE_NORMAL como HW0. Qualcomm/pmaports/mainline clk/regulator da
triagem nao fornecem ABI upmuMT6357, portanto pequena adaptacao no backendLG.
Ambos campos sao bit1 (mascara1 shift1 LG), offsets0x1b8a e0x1b90.
Usar update_bits BIT(1) conserva demais bits como pmic_set_register_value,
nao confundir com full-write1 empregado para18/33. Confirmar regmap doVCN28
igual ao18 e CID0x57; guardar bits antes e restaurar so esses bits na falha.

Ops antigo de modo e void e usado por6761/6755/6739; manter seu contrato sem
editar plataformas fora do escopo. Acrescentar ao fim da ops interna um callback
checked com tipo int ja existente; somente6765 preenche. Core prefere checked,
fallback chama funcaoLG real (nao stub) nos demais perfis. Pequena extensao
necessaria para transportar erro, nao framework novo nem generalizacao de board.
Falha no modo deve impedir enableVCN28/reset/SPM no on, ou desligamento seguinte
no off. Outros efeitos18/pinmux/XO ja anteriores nao sao rollback completo:
manter bloqueio de carga e tratar unwind/retry antes de uso fisico. Esforco
pequeno/medio; teste de equivalencia dos campos e erros, buildARM32 dirigido.

Resultado: wmt-mt6765-vcn28-mode-regmap-v1.patch aplicado e reverse dry-run
fuzz0. Headerops mudou, por isso dependentes WMT foram recompilados peloKbuild,
todos objetos e LD wmt_drv.o passaram -Werror. Modpost recusa12 simbolos vendor
em work/wmt-lts-vcn28-mode-20261027-a.log; chamada ativa a
connectivity_export_pmic_set_register_value foi eliminada por acesso real ao
regmap, nao por no-op. Objeto mt6765.o SHA256
bcd1474852f3cca61a34ec4e35c4d294d56d8ce3c636d308d727cb9a611866ae.
Fonte core atual SHA256
4c2d7e1d833390ce2f510c732bbcea6d19d385b8a2728b2bc216eb47a475232f;
fixtureEMI atualizada conforme dependencia e passou novamente em
work/wmt-reserved-memory-host-20261027-e.log.

Teste tools/tests/test_wmt_vcn28_mode.py fixa os tres originaisLG porSHA e
aplica dependencia core-linux618-api (torna helperstatic) antes do patch novo.
Executa callbackC real LG/novo e core reg_ctrl/helper reais. Compara campos
HW0 nos dois sentidos com sementes0/ffff/a5a5/5a5a para EN e CFG, incluindo
bits alheios preservados. EIO nas tres leituras e duas atualizacoes, com/sem
modelo de escrita efetivada antes do erro, interrompe e restaura os bits no
modelo. Mapas ausentes18/28, diferentes, CID errado e handles ausentes recusados;
falhas na restauracaoCFG/EN logadas, sem declarar recuperacao. Core nao continua
a enableVCN28/efuse apos erro de modo, checked tem prioridade sobre legado;
fallback executa callbackLG real e ausencia conserva opcionalidade original.
Passou -Werror/UBSan em work/wmt-vcn28-mode-host-20261027-d.log. Tentativasa/b
revelaram dependencia do patchstatic faltante na fixture; incluida sem relaxar
hash/fuzz. Versaoc passou antes de adicionar falhas de rollback.

Limite: retorno de modo agora existe, mas falha ainda pode deixar alimentacao18/
pinmux/XO das etapas anteriores; nao chamar isso rollback de power-on. Controle
enable/disableVCN28 ainda ignora erros de voltage/enable e seus wrappers tambem;
proximo incremento deve propaga-los e integrar unwind/retry antes de carga.
XO/PMIC-PWRAP e genpd permanecem bloqueios separados. Sem DT ativador, novo
probe, reset ou qualquer outra operacao no aparelho nesta etapa.

### XO real e reset: bloquear continuidade apos power failure

Entrega no aparelho: reset WMT recupera somente apos off/on concluidos; falha
nao escreve calibracao nem libera PDMA/reset como se recuperado. Aceite desta
etapa offline: sequencia de sucessoLG preservada e falhas retornadas antes
das operacoes posteriores. Nenhum reset fisico autorizado.

RastreamentoXO na fonteLG GPLv2 MediaTek2017
drivers/misc/mediatek/base/power/clkbuf_v1/mt6765/mtk_clkbuf_hw.c SHA256
6021b7cb5395394318989bd8e166ac8015039731d64cf2dabdf1bea2ef59f2b1:
clk_buf_ctrl(CLK_BUF_CONN) normalmente so registra pmic_clk_buf_swctrl[XO_WCN]
para BBLPM, exige estadoSW e pwrap_dcxo_en_flag bit1. Nao e gate fisico simples.
Programacao DCXO_CONN_ADR0/WDATA0/ADR1/WDATA1 (PWRAP0x18c..0x198),
DCXO_ENABLE0x188 e inicializacao de modosPMIC estao sob #ifndef __KERNEL__:
dependem de firmware anterior ao kernel (o log PL/LK acima localiza o registro
no preloader, nao no LK). Caminho sem CLKBUF_CONN_SUPPORT_CTRL_FROM_I1 usa
PMIC_RG_SRCLKEN_IN3_EN, nao simplesmente EXTBUF2_EN_M. O clk_buf_ctrl_internal
(outra API) altera esses recursos; nao confundir com a chamadaWMT exportada.
Linux6.18 local nao tem driverMT6357 clkbuf nem inicializacaoDCXO em
mtk-pmic-wrap.c. CCF generico e Qualcomm SPMI clock divider nao comprovam
compatibilidade; mainline/pmaports/Qualcomm triados abaixo nao substituem essa
automacao por existencia de clock API. Nao adicionar gateCCF/stub ou escritas
globaisCW00 por deducao. IntegracaoXO requer confirmar/configurar handshake
PMIC/PWRAP no provider proprietario de transporte, preservando NFC/outrosXOs.
Isso e bloqueio concreto de integracao, nao justificativa para ensaio fisico.

Enquanto isso corrigir falha real do coreLG GPLv2 ja fixado: hw_rst soma erros
de off/on, restaura calibracao mesmo apos off falho e limpa status/PDMA apos
on falho. Reusar retorno existente, nao novo framework: nao acumular erros;
na primeira falha retornar exatamente o erro com mensagem e manter
chip_reset_status=1 e PDMA force-high ja elevado. Nao executar limpeza de PDMA
que faz leituraMMIO apos on falho. Status fica publicado, mas busca no common
nao encontrou consumidor do getter; integrar leitoresWiFi e gate persistente
ainda e necessario. Nao e prova de isolamento eletrico ou rollback completo. Sucesso continua
mesma sequenciaLG, callback opcional permanece opcional. Esforco pequeno,
teste dirigido de sequencia/falha e build suficientes antes de integrar restantes.

Resultado: wmt-connsys-reset-error-gates-v1.patch aplica/reverse dry-run fuzz0;
ARM32 -Werror recompilou core e LD wmt_drv.o. Modpost ainda recusa os mesmos13
simbolos vendor: work/wmt-lts-reset-gates-20261027-a.log (make termina com erro;
sha256 posterior no mesmo comando nao converte isso em build aprovado).
Objeto core SHA256
6349a6e59a3896cfc8f8e6fe7efc2db27dcbe4bd0d9597a9021471ea8ad68412,
fonteSHA256
9b3b147b2b7819fbee3bfb32ffa02558444257bdb813497689281d88e6686c07.
Teste tools/tests/test_wmt_reset_errors.py aplica patch ao originalLG SHA fixado
e executa resetC real original/portado. Sucesso coincide no trace com todos os
callbacks opcionais e sem eles; EIO/ETIMEDOUT/ENOMEM e retorno positivo nonzero
em off e on preservados, sem etapas posteriores; flagsPDMA/status mantidas e
um log de falha. Passou -Werror/UBSan em work/wmt-reset-errors-host-20261027-b.log.
Tentativaa recusada por patch com contexto unilateral; corrigido contexto
antes/depois sem aumentar fuzz ou relaxar teste. FixtureEMI atualizada pelo
hashcore e passou em work/wmt-reserved-memory-host-20261027-d.log.
Os doubles nao demonstram power transition fisica, rollback ou recuperacao
de rail ativo. Faltam ainda propagacao dos outros erros no reg_ctrl, gate
de retry apos falha e lifecycle antes de ensaio. Nenhum teste fisico realizado.

### VCN18/VCN33 MT6357: SW mode via regmap nativo, com erros

Entrega pretendida: primeira etapa de power-on WMT alimentada e falha interrompe
sequencia antes de pinmux/XO/SPM. Reusar regulator_get_regmap (API consumer
exportadaGPL), regmap_read/write e regulator API6.18; nao criar adapter generico
upmu. Mainline MT6357 registra os mesmos offsets OP_EN mas nao oferece operacao
regulator de selecaoSW/HW. VCN18_OP_EN0x1a5a e VCN33_OP_EN0x1b1e valor1 devem
permanecer escritas integrais como LG, nao update_bits que preservaria bitsHW
antes apagados. Reusar CID do MFD: SWCID0xa bits15:8 == MT6357_CHIP_ID0x57;
exigir mesmo regmap para VCN18/VCN33 quando rail33interno. Ler/salvar OP_EN antes
de alterar, restaurar em erro e desfazer enable18 se etapa33 falhar. Retorno
original preservado e falhas de rollback explicitas. Tensoes1.8V/3.3V e ordemLG
permanecem, modo sucesso continua persistente no disable como vendor. Nenhuma
operacaoPMIC fisica agora. So backendMT6765 recebe adaptacao, licencaGPLv2;
headers/adaptersLG e fontesmainline ja fixados nas entradas anteriores.
Alternativas pmaports/Qualcomm/mt76 nao implementam esta sequenciaMT6357;
regmap/regulator nativos sao o transporte existente compativel. Esforco medio:
teste de sequencia/erro e build proporcionais; outros rails, XO, teardown e
recuperacao geral continuam bloqueios de carga. Nao declarar eletricamente
validado por simulacao nem remover restante de PMICAPI com no-op.

Resultado: patch wmt-mt6765-vcn18-regmap-v1.patch aplica/reverte dry-run com
fuzz0, recompilou backend/core ARM32 -Werror e LD wmt_drv.o. Modpost agora
recusa13 dependencias: connectivity_export_upmu_set_reg_value deixou de ser
necessaria porque chamada real foi substituida por regmap, nao stub. Evidencia
final work/wmt-lts-vcn18-regmap-20261027-b.log; mt6765.o SHA256
26bbdf01a4df41c4da21cde6310f113ec23c8df9d61ea42c8aed29e1c71b7b45.
Core fonte SHA256
de2300ebbffd638d81b544430a38e50aefbcfe6850242fe980dd2ab790bf2aa8;
fixtureEMI atualizada por dependencia, teste passou novamente em
work/wmt-reserved-memory-host-20261027-c.log, criterios inalterados.

Teste tools/tests/test_wmt_vcn18_regmap.py fixa originaisLG de backend/core,
aplica patch e executa callbacksC reais antigo/novo. Com rail33 interno/externo,
trace de escritas/voltagens/enable/disable coincide no sucesso. Injetar EIO em
cada leitura/escrita/set_voltage/enable (9 etapas interno,5 externo) interrompe
e restaura modos/contagens no modelo. Rejeita regmap ausente para18 ou33,
mapas distintos, CID errado e handles ausentes antes de escrita. Falha no
rollback disable18 deixa18 ativo emSW com log explicito; falha na restauracao
de modo deixa modo alterado com log, sem declarar recovery concluida. Disable33
falho nao desliga18 a jusante. Wrapper power_onC real recusa EMI ausente e
nao chamaGPIO/JTAG em erro de reg_ctrl. Passou -Werror/UBSan em
work/wmt-vcn18-regmap-host-20261027-b.log. Versaoa testava mesmo backend antes
de ampliar propagacao ao wrapper e erro individual do regmap33.

Limites ainda obrigatorios: fault injection de regmap nao prova efeito fisico
de escrita com erro ou regulator_enable parcialmente aplicado; consumidores
podem manter voto de voltagem apos falha. Contagem/recuperacao persistente em
falha do rollback e serializacao com remove/reset continuam por integrar;
nao repetir power-on fisico nesse estado. Reset vendor soma erros e continua
sequencia, power-off geral ainda ignora outros retornos. VCN28_HW0, XO e
genpd/MTCMOS ainda precisam integracao; nenhum rail ou carga foi ativado.

### WMT MT6765: adquirir reguladores antes de efeitos do probe

Entrega no aparelho: alimentacao WMT com falhas detectadas e recursos validos;
aceite deste incremento offline: erros/defer de supplies impedem MMIO/EMI,
sem ponteirosERR publicados; release limpa ponteiros antes de regulator_put.
CoreLG e mt6765.c GPLv2 ja fixados abaixo, backend antes desta mudanca SHA256
df3778a99ca851d9734526875e30b704b1259059ac57707ee8460ae26530062e.
Reusar devm_regulator_bulk_get e devm_add_action_or_reset Linux6.18.58
(drivers/regulator/devres.c GPL-2.0-or-later), array estatico pois devres guarda seu
endereco; API bulk faz unwind de aquisicao parcial e nao habilita reguladores.
Mesmos quatro supplies LG vcn18/vcn28/vcn33_bt/vcn33_wifi, mesmas voltagens e
ordem eletrica ainda inalteradas. Publicar somente sucesso e zerar via devres
antes da liberacao bulk; propagar retorno do backend no core antes de panel,
MMIO e limpezaEMI. Nao introduzir backend paralelo, DT ou escrita nova.
Alternativas mainline/pmaports/Qualcomm ja triadas: framework regulator e a
reutilizacao compativel, nao copiar API PMIC4.9. Esforco pequeno; teste dirigido
de sucesso, erro/defer e cleanup suficiente nesta fase, sem prova eletrica.
MT6357 nativo habilita CON0 bit0; vendor escreve VCN18_OP_EN0x1a5a e
VCN33_OP_EN0x1b1e com valor1, e VCN28_HW0_OP_EN/CFG em0x1b8a/0x1b90 bit1.
Logo regulator_enable nao demonstra equivalencia OP_EN/OP_CFG, manter essas
dependencias reais ate integrar modos e providerXO; nao troca-las por no-op.

Resultado: wmt-mt6765-regulator-acquire-v1.patch aplicado/reverse dry-run fuzz0.
Build ARM32 -Werror recompilou backend e core, LD wmt_drv.o; modpost continua
recusando14 dependencias vendor em work/wmt-lts-regulator-acquire-20261027-a.log.
Objetos SHA256 mt6765.o
76bfd1d02bf048652eaeb8d4d71ce0e6beef6979de6e23d2a570b6629d436e86,
mtk_wcn_consys_hw.o
6aa386dbd64181d5a6aa62a6e4f63eea4264db99dbc48556f1d9d124fe300449.
Fonte core passa a SHA256
2a2a79dd5ac2328241f2c1edfd44c5a3028e064dbf5b9d1800dc811a599de68b;
fixture de testeEMI atualizada por essa dependencia e teste reexecutado com
sucesso em work/wmt-reserved-memory-host-20261027-b.log, sem mudar criterios.

Teste novo dirigido aplica somente hunkMT6765 a fonteLG fixada e executa array
e funcoesC reais de aquisicao/clear. Verifica nomes/indices dos4 supplies,
ENOMEM/ENODEV/EPROBE_DEFER/EIO retornados sem publicar consumidores, falha ao
registrar acao limpa imediatamente e sucesso limpa antes do bulk release,
incluindo novo bind. -Werror/UBSan passou em
work/wmt-regulator-acquire-host-20261027-a.log. Doubles devres nao provam
unwind interno do framework (inspecionado em devres.c) ou concorrencia com
power workers. Nao foram alterados enable/disable, OP_EN/OP_CFG, tensoes ou
XO, nem ativado hardware. Proximo: modoPMIC/XO e propagacao de erros do power-on
que ainda ignora retornosVCN18/clock; unwind deve preceder qualquer ensaio.

### Integracao EMI WMT: reserva por dispositivo, sem endereco inventado

Entrega no aparelho continua WMT/Wi-Fi e logs reais, com EMI reservada fora da
RAM normal; aceite offline deste incremento: resolver os dois simbolosEMI com
dados OF validados, recusar ausencia/perfil invalido antes de MMIO e nao limpar
NULL quando ioremap falhar. Nao ha DT consumidor nem ensaio fisico autorizado.
LG4.9 connectivity_build_in_adapter.c MediaTek2016 GPLv2 usa
RESERVEDMEM_OF_DECLARE para publicar gConEmiPhyBase/gConEmiSize. LG mt6765.dts
especifica consys no-map, size4MiB, alignment16MiB; mt6765.c reusa somente bits
base>>24 para remap e mapeia coredump0x68000+96KiB e logs0x36500+192KiB.
Reusar mainline6.18 of_parse_phandle/of_reserved_mem_lookup e validar compatible,
no-map, base nao zero, alinhamento16MiB, tamanho exatamente4MiB e fim32bits.
Sem fallback a busca global, alocacao runtime ou copiar endereco do stock.
Selecionar perfil existenteMT6765, nao framework multi-SoC. Definir globais no
core WMT existente (consumidores somente no modulo), sem exportAPI novo.
Probe exige phandle memory-region antes de registrar panel ou tocar hardware;
falha/remove limpam publicacao. O lifecycle restante continua bloqueio de carga.
Alternativas mainline/pmaports/Qualcomm ja triadas nao fornecem protocoloEMI
MT6765; RE nao e necessario pois ha fonte. Pequena extensao ao coreLG GPLv2,
sem novo driver. AdaptadoresPMIC/clkbuf LG nao sao copiaveis como stubs: precisam
provider nativo e propagacao de erros. A ponteSDIO LG e para MSDC legado, enquanto
Wi-Fi6765 usa AXI; nao eliminar STP/BTIF sem rastrear consumidores BT/GPS/FM.

Identidades adicionais da auditoria, snapshotLG sem commit, GPLv2 conforme
cabecalho dos doisC (DTS integra arvoreLG, confirmar aviso individual antes de
redistribuir): connectivity_build_in_adapter.c SHA256
d3e1668093d4d88ce59daa4556b3da1291e021bac08bd6d354f75a9087ef4507;
wmt_build_in_adapter.c SHA256
8b5cfed22b3025427fa802afe7546c9a0be6e7a2f59a6f5ff2aced090b6f7be2;
arch/arm/boot/dts/mt6765.dts SHA256
cf608e7d9c2de0a48d2bb6cc8a3d3031a30e46ed16f5d98601064c0a00c57efb.
Nao copiar esses adaptadores inteiros: incluem sched privado, MSDC/PMIC legado,
registradores e funcoes que nao possuem equivalencia automatica no6.18.

Patch wmt-connsys-reserved-memory-v1.patch aplicado com fuzz0 e reverse dry-run
passou. Core ARM32 compilado -Werror SHA256
a91b87b7e18f91b3cd86b1005d31961f093ce9198bfc89be7fe3cba19bc9a9f5;
fonte integrada SHA256
38a3af48d7b8fef46394034704ad4aca08214e7009662088fdabeeeb3453ceb2.
LD wmt_drv.o passou novamente; nm mostra gConEmiPhyBase/gConEmiSize definidos,
modpost com vmlinux.symvers do mesmo build agora para em14 simbolos vendor,
sem criar ko. Nenhum simbolo falso nem verificacao desativada.
Teste tools/tests/test_wmt_reserved_memory.py fixa a fonte integrada porSHA
(fixture privada com patches previos) e executa o resolverC real com doublesOF:
reserva valida e maior base alinhada32bits aceitas, ausencia de phandle/reserva,
disabled, compatible errado, no-map ausente, reusable, base0/desalinhada,
tamanho menor/maior e overflow32/64bits recusados sem publicar dados;
referenciaOF liberada tambem nas falhas. Passou -Werror/UBSan em
work/wmt-reserved-memory-host-20261027-a.log. Nao testa allocatorOF real ou
teardown concorrente. ioremapNULL agora retornaENOMEM em vez de memsetNULL;
probe secundario nao substitui g_pdev. Demais falhas de recursos permanecem.

Proximo bloqueio: mt6357-regulator.c6.18 ja oferece VCN18/28/33_BT/33_WIFI,
mas nao comprova equivalencia das escritasOP_EN/OP_CFG vendor. Comparar modo
SW/HW, controleXO e erros antes de adaptar chamadasPMIC/CCF. ClockMTCMOS antigo
tambem nao equivale diretamente ao genpd; nao combinar sequencias sem ownership.

### CONSYS dedicated log: APIs6.18 e bloqueios de ciclo de vida

Entrega pretendida no aparelho: logs reais do firmware durante WMT/Wi-Fi e
encerramento seguro; aceite desta etapa apenas offline: objeto compilado e
equivalencia dos callbacks/UTC. FonteLG MediaTek2016 GPLv2
debug_utility/connsys_debug_utility.c SHA256
8dbe8597228798f6470e1bdc60c60bb6fafc3cb7652ca8d6a7da528ada037f93.
Reusar a implementacao LG e APIs mainline Linux6.18.58 alarmtimer/timer/RTC/
timekeeping; alternativas upstream/pmaports/Qualcomm da triagem vinculada abaixo
nao implementam este layout EMI e protocolo de logs MT6765. Nenhum driver ou
protocolo novo. Mudanca pequena: callback alarm void (mantem rearm explicito),
timer_setup com timer_list* (argumento antes ignorado), rtc_time64_to_tm e
ktime_get_real_ts64 com nanos/1000 preservando ABI sec/usec unsigned32;
ioremap e helper de alocacao privado, sem alterar tamanhos/fluxo EMI.
APIs reaproveitadas GPL-2.0 conforme arquivos da arvore mainline fixada; mapping
ARM ja auditado nas etapas anteriores. Nao substituir por relogio monotonic,
nao remover alarm/log para compilar. Comparacao de erro/remove identificou
defeitos preexistentes: alarm_cancel sob spinlock tambem usado pelo callback,
rearm incondicional, iounmap antes de free_irq, sem timer/work drain, falhas de
alocacao nao propagadas. Port de API nao corrige nem aprova esses caminhos;
correcao de lifecycle com falhas concorrentes e obrigatoria antes de carga.

Resultado: connsys_debug_utility.o ARM32 compilou com -Werror, SHA256
9d26186d6756eba06b2613410cb43ea3e2ba9fe3d07349a6a82971134d9831e6.
Todos objetos WMT chegaram a LD wmt_drv.o, mas nao existe wmt_drv.ko aprovado.
Log work/wmt-lts-connsys-log-api-20261027-a.log: modpost sem Module.symvers
na pasta build nao resolve nem APIs comuns. O mesmo build possui vmlinux e
vmlinux.symvers; fornecer esse ultimo via KBUILD_EXTRA_SYMBOLS (API Kbuild,
sem warnings-only ou relaxar verificadores) resolve APIs mainline e isola16
dependencias vendor ausentes em work/wmt-lts-modpost-vmlinux-20261027-a.log:
connectivity_export_{clk_buf_ctrl,dump_gpio_info,dump_thread_state,
mmc_io_rw_direct,pmic_set_register_value,show_stack,upmu_set_reg_value},
gConEmiPhyBase, gConEmiSize, mtk_wcn_cmb_sdio_pm_cb,
mtk_wcn_cmb_sdio_pm_data, wifi_irq,
wmt_export_{mtk_wcn_cmb_sdio_disable_eirq,mtk_wcn_sdio_irq_flag_set,
platform_bridge_register,platform_bridge_unregister}.
Nenhum stub criado. Proxima integracao exige comparar a bridgeLG original com
providers nativos PMIC/CCF/EMI/SDIO e funcoes realmente exigidas pela placa.

Teste dirigido tools/tests/test_wmt_connsys_log_api.py aplica patch em fonteLG
com SHA fixado e executa funcoesC reais originais/portadas com doubles:
UTC segundos0/1793132427/2147483648/4294967295 e nanos0/999/1000/123456789/
999999999 mantem micros; callback timer agenda uma leitura sem contadorIRQ;
alarm mantem ordem schedule/rearm e intervalos1/60/UINT_MAX segundos.
Passou -Werror/UBSan em work/wmt-connsys-log-api-host-20261027-a.log,
reverse dry-run passou fuzz0. Os doubles nao provam RTC fisico, entrega de
logs, alarm cancel concorrente ou deinit seguro. Inspecao do alarmtimer.c6.18
confirma callback void e cancel aguardando callback, reforcando o bloqueio
de spinlock ja identificado. Nenhum ensaio fisico nesta etapa.

### STP debug: reporter Android opcional e timestamps6.18

Etapa antes de implementar: compilar stp_dbg.c LG GPLv2 original SHA
b16c418dd0e694b9f22b8a4e807111a052db99334e61204582bd9a25e20994eb.
Reusar guard IS_ENABLED(CONFIG_MTK_AEE_AED) ja auditado em Motorola common
e6cfe39 osal.c/osal_typedef.h GPLv2 e no patch OSAL local. STP ja distingue
reporterUI/AEE de compressor/coleta/reset por STP_DBG_AEE_EXP_API; acrescentar
configAEE a selecao, sem desligar logs/debug ou alterar dados do compressor.
Flush preserva post_handle/out/reset e retorna EOPNOTSUPP quando nao ha sinkAEE,
com mensagem explicita; nao reportar envio aprovado sem destino. O ramo ftrace
exclusivamenteAEE recusa antes de mudar hostAssert/fwInfo, nao criar no-op de
captura. Consumidores antigos ignoram alguns retornos: coleta nativa efetiva e
propagacao completa continuam pendentes antes de carga, nao aprovadas por build.

Header de log usa timeval somente para sec/usec: reusar timespec64 e
ktime_get_real_ts64, mantendo sec32 dos registros, usec=tv_nsec/1000 e tempo
localOSAL separado. Sem novo relogio/parser/protocolo. Alternativas mainline,
pmaports/Qualcomm ja triadas nao fornecem ABI AEE para esta placa; nao portar
stackAndroid para compilar. Esforco pequeno e teste dirigido de timestamp,
flush semAEE/ramo habilitado e rejeicao sem estado alterado. Nenhum novo driver
ou diagnostico, probe/remove fisico nao mudam.

STPdebug compilou em work/wmt-lts-stp-debug-20261027-a.log. Harness reutiliza
function/cc/unittest sobre callbacksC reais, fonte fixado pelo SHA acima;
timestamp usa0/999/1000/123456789/999999999ns, EINVAL nao le relogio, flags/campos
do registro preservados. Flush com/sem AEE e com/sem timeout mantem sequencia
lock/post/unlock/out/reporter(se disponivel)/compressorDeinit/reset. SemAEE
retorna EOPNOTSUPP; ftrace nao altera host/fwInfo. ComAEE preserva erros de
parametro/assert existente/fwInfo e ambos destinos de info. Passou -Werror/UBSan
em work/wmt-stp-debug-host-20261027-b.log. Tentativa a extraiu prototype em vez
de definicao; extrator seleciona ultima ocorrencia agora, sem relaxar checks.
API doubles nao entregam dump real nem provam recovery fisica.

Proximo wmt_step.c LG GPLv2 original SHA
b32a031aa35f7cd47f1bb526f7e6ca6279a6b3dd02d7a6d515a2a60731133c74:
tres ioremap_nocache seguem equivalenciaARM ja auditada, manter tamanhos e
barreiras. parse_act_id compara ponteiro a '\0' como NULL duplicado: corrigir
para *str=='\0' com curto-circuitoNULL, mantendo retorno NO_DEFINE antes de ler
quatro caracteres. Dois helpers sem export/consumidores externos passam static:
_wmt_step_do_register_action e wmt_step_setup. Reusar fonte/framework existente,
nenhum novo diagnostico/driver, mesmas alternativas auditadas; nao mudar sequencias
de acessoMMIO/reset. Politicas destrutivasSTEP exigem revisao antes de ativar.

Resultado final desta etapa: stp_dbg.o SHA
5ed80a2c0fafa29b7918be7afaf95107d04d8b56cd6673be163adaa0efbeff8c,
fonte staged SHA12c4ebafa8b978a85c20735be73b016c7bdbcb9e4c0b41fd8384ea9d2cfcf9aa.
wmt_step.o SHA05abefb6940126f208a3ec2977d18b4a5f9b8f8e740c4f2980ee46b4dec656d7.
Logs work/wmt-lts-stp-debug-20261027-a.log e wmt-lts-step-api-20261027-a.log
comprovam build ARM32 com -Werror, avancando tambem ring.o/ring_emi.o.
Reverse dry-run dos dois patches passou sem fuzz. Teste STP debug final passou
com AEE0/1 e UBSan; catalogo inclui dependencia de fonteLG privada. Nao houve
ensaio fisico ou alteracao das imagens4.9/protecoes.

Proximo bloqueio concreto: debug_utility/connsys_debug_utility.c tem prototype
ausente cache_allocate; alarmtimer_restart foi removido (callback atual void),
rtc_time_to_tm/timeval/init_timer e ioremap_nocache obsoletos. Comparar alarm
rearm/cancel/workqueue antes de adaptar, preservar prazo/unidade/UTC e teardown;
nao remover utilitario inteiro apenas para atingir link. O modulo completo
continua sem link/modpost, e clockbuffer/PMIC/EMI, transporte real e recovery
sob falha permanecem anteriores a carga no aparelho.

### UART: adaptar line discipline ao TTY6.18

Etapa antes de implementar: compilar UART preservando filas/parsing e erros;
aceite offline exige assinaturas TTY reais sem casts de callback, init/exit
coerentes e ioctl obsoleto recusado explicitamente. Entrega final WMT6765 no
aparelho continua pendente, nao inferir UART funcional de compilacao.

| Funcao | Reuso / revisao / licenca | Compatibilidade / falha / decisao |
| --- | --- | --- |
| STP UART | LG stp_uart.c GPLv2 SHAe3cc12a36d958d31681ccea4d701edd141aa62e9d3eb5e1f0121faa96ebc8a0d, snapshot sem commit | Adaptar fonte existente, sem novo transporte. MIN/MAX locais nao tem consumidores: remover duplicatas. receive usa const u8 flags e size_t; read ganha cookie/offset, mantendo EOF intencional. ioctl segue n_tty_ioctl_helper(tty,cmd,arg). init usa ops.num e register(ops); unregister void, sem inventar retorno. Buffers e parser preservados; lifecycle completo ainda requer validacao |
| Modelo API UART6.18 | LTS2926d88 drivers/bluetooth/hci_ldisc.c GPL-2.0-or-later SHA575887415bc7318e5d5d40a982058e4990319d405145d27c69244be7dfd8d3ef, tty_buffer.c GPL-2.0 SHA00e7891b4d21891ba643d01b85ed3b06487cce7fe63f04cc0ab6b9fcae5a06d6, tty_ldisc.c GPL-2.0 SHAb90e454ff9202bc17efd3181fa76f0d40cb790d64e6bad8939b978dd51f9d5bd | Reusar contrato das APIs/assinaturas como HCI upstream, nao protocolo HCI para STP. Flip buffer6.18 sempre enfileira em system_unbound_wq; low_latency nao existe. Nao simular sucesso para controle removido: HCIUARTSETPROTO legado retorna EOPNOTSUPP. Recepcao normal usa TTY atual; latencia precisa ensaio proprio |

N_MTKSTP LG=16 colide com N_GIGASET_M101 no UAPI atual. N_DEVELOPMENT=29 e
reserva upstream para ensaio manual fora da arvore; usar somente nesta copia
staging, sem alterar launcher/modulo4.9 recuperavel. tty_register_ldisc6.18
sobrescreve slot sem verificar dono; nao coexistir com outra disciplina de
desenvolvimento e nao carregar o resultado apenas por compilar. Procura local
em sources/tools/boards e conn-src nao encontrou fonte do launcher: adaptar
cliente6.18 ao numero29 e retirar solicitacao low_latency obsoleta antes de
qualquer uso UART. Isso e lacuna explicita de integracao, nao permissao para
usar launcher4.9 ou RE sem necessidade. Mainline/pmaports/Qualcomm/Motorola
triados nao fornecem protocoloUART STP substituto comprovado para esta placa;
esforco pequeno no driver, integracao userspace separada ainda pendente.

Tabela tty_ldisc_ops antes static local em init passa a static de arquivo:
unregister6.18 exige o mesmo ponteiro, nao numero. Lifetime continua modulo,
sem copiar tabela temporaria. Primeira compilacao expôs esse escopo em exit;
corrigir antes de nova tentativa, sem cast nem suprimir erros.

UART compilou em work/wmt-lts-stp-uart-20261027-b.log; objeto ARM32 SHA
3a7105387c37f13573c9287f0269d8765f1795507ba11135914749100a066b72.
Teste de callbacks reais ioctl/read passou em work/wmt-uart-api-host-20261027-a.log:
low_latency EOPNOTSUPP sem chamadaTTY, demais comandos/args e retornos0/EINVAL/EIO/17
preservados; read continuaEOF sem escrever buffer/cookie. UBSan ativo. Harness
nao modela latencia, recepcaoFIFO, linha ativa ou ownership de slot29; build
ARM32 comprova assinaturas. C gerado preserva avisoGPLv2. OriginalLG inalterado.

Proximo wmt_dbg.c GPLv2 SHA
c9b3f33cea8267e8429ddcb8d7063c50ee5d7549642b6fbc9f9a1e6b285fbe72
requer ioremap no lugar do aliasARM ioremap_nocache (duas chamadas4bytes) e
proc_ops para procCreate, mesma adaptacao ja auditada no backend e wmt_dev.
Reusar APIs LTS; nao novos diagnosticos, permissoes ou comandos. Preservar
callbacks/read/write/cleanup e barreiras; acesso debug cru ja existente nao
sera exercitado no aparelho. Exposicao desse proc e comandos destrutivos deve
ser revisada antes de qualquer payload, compilacao nao aprova acessoMMIO.

wmt_dbg.o compilou SHA446dbe8d9fd345ac63f7c8063c1c744d02eb7f87f6beecdf72c2838d0017a19d
em work/wmt-lts-debug-api-20261027-a.log; proximo stp_dbg.c exige AEE Android
(aee_kernel_dal_show/aed_combo_exception) e timeval removido no header de log.
Consultar guardAEE ja auditado e doador antes de adaptar, preservando captura,
logs e recuperacao sem reporter Android. Nao criar stub/no-op de coleta.
Reverse dry-run dos patches UART/debug passou sem fuzz. UART staged fonte SHA
487daba8851744bc90795bc11fbda5e39beb8b4dffc5fcc5e8661ad8466d4ae5.
Nenhum novo ensaio fisico, modulo completo/link/modpost ainda pendentes.

### STP SDIO: tempo/procfs/declaracoes6.18

Proximo incremento: compilar stp_sdio.c preservando timeout semACK e recuperacao;
entrega funcional ainda e WMT6765 no6.18. Fonte LG GPLv2 original SHA
fc59d810fa5ceca02541ef9003793b7ea42b1bd981848566d158c064e53c631f.
Reusar timespec64/ktime_get_real_ts64 como OSAL/PSM ja portados: old/now usam
apenas tv_sec e condicao >5, em ambos ramos TXRING. Nao mudar para relogio
monotonic, >=, retries ou outra sequencia de assert/recovery. Atualizacao de old
apos envio mantida no mesmo ponto. Procfs usa proc_ops/proc_read/proc_write nos
tres arquivos existentes, com nomes, permissoes e callbacks/cleanup preservados.
own_ctrl, tx e seis setup/remove sao privados pelo levantamento de chamadas,
incluindo registro de tx como callback: static sem alterar funcao/corpo.
Init/exit exportados recebem declaracao em stp_sdio.h; wmt_dev.h exit corrigido
de int para VOID conforme implementacao, sem novo export ou retorno ficticio.

Alternativas mainline/pmaports/Qualcomm/Motorola ja comparadas abaixo; APIs MMC,
procfs e tempo LTS sao o reuso compativel, nenhum driver paralelo e necessario.
Esforco pequeno. Testar borda5/6seg e a mesma sequencia de recuperacao antes de
qualquer futura ativacao. Compilacao nao comprova IRQ/MMC/BTIF ou protocoloAXI.

Build apos APIs revelou flush_scheduled_work global no exit. Inspecao real do
HIF mtk_wcn_hif_sdio_client_unreg mostra que ele limpa listas/contextos mas NAO
chama removeSTP (apesar do comentario). Em OWN_THREAD1, exit podia liberar os
buffers com thread viva. Reusar stp_sdio_remove antes do unreg se host_count>0;
esse caminho desabilita ingressIRQ, remove if_tx e usa osal_thread_destroy.
No ramo work usar cancel_work_sync apenas TX/RX locais em vez de flush global.
Mover deinit do fake_coredump_lock para depois de parar thread/work, pois o
worker pode usa-lo. Desregistrar callbacks debug/own antes de parar host.
Sem host, nao cancelar work nao inicializado. Depois unreg e bufferfree no
fluxo existente. Esforco localizado, fonte GPLv2 acima e APIs OSAL/workqueue
LTS ja existentes; nao criar fila/driver novo ou suprimir warning.

Aceite desta mudanca: callback remove e exit reais em harness dirigido devem
mostrar stop antes de destruir lock e liberar buffers, sem host nao deve tocar
em thread/work. A flag IRQ do HIF nao sincroniza todos callbacks em voo;
concorrencia MMC, erro de probe/registro e unreg ainda exigem reparo/validacao
do lifecycle completo antes de carga. Nao alegar equivalencia fisica de teardown
so por esses testes. Patch adicional wmt-stp-sdio-local-cleanup-v1.patch.

Resultado: stp_sdio.o ARM32 compilou com -Werror, SHA
6dfe8078e9521b0c4f9faacbdbb7f669f98cfc42663dbc1ee1f385c41a1def83,
fonte staged SHA8dd04def8bb61afa996055e137201528f5c0d640143317d322af0d429207116e.
Log work/wmt-lts-stp-sdio-cleanup-20261027-a.log tambem compila bgw_desense.o
SHA5ed8924ac1e3c86758d5449ed16c4c4ce83b735ff8bcb22ea5d43f3436f993f8 e
wmt_idc.o SHAd71323456a39660c7b0266ba657c93ac382d9304045be24084023eec122152d4.
nm mantem ktime_get_real_ts64/OSAL thread destroy reais; sem flush global.
Reverse dry-run dos dois patches passou sem fuzz. Originais/payloads4.9 intactos,
nenhum modulo completo linkado nem operacao no aparelho.

Teste test_wmt_stp_sdio.py reutiliza harness function/cc/unittest e snapshots
fixados, sem transporte. Header baseSTP SHA
bd46a90e598a54c122574baa868eecd2df396e05c85aafff32beb544b94a27fa,
headerWMTbase SHAd0e8c2eb51d7054762e5395fe583d450c9cd43238b85a974646e22f37cae9833.
Callback C real de timeout extraido antes/depois, constantes de timeout/FIFO
extraidas dos fontes; cobre diferencas de tempo -1/0/4/5/6/100, fifo/full flag,
reset de contador e retorno verdadeiro/falso do assert, mantendo sequencia.
Remove/exit C reais verificam contextoinvalido, hostausente, fechamento dos
callbacks, stop antes de destruir lock/reset/unreg/free, nos ramos thread/work.
Passou -Werror/UBSan em work/wmt-stp-sdio-host-20261027-c.log. API doubles nao
executam threadsOSAL, workqueue kernel ou IRQ/MMC reais. Tentativa a recusou
indentacao no stub do proprio teste, corrigida sem relaxar flags; b passou,
c e a versao final que deriva constantes de producao.

Proximo erro concreto e stp_uart.c: macros MIN/MAX duplicam minmax6.18,
tty_port.low_latency e tty_ldisc_ops.magic removidos; read/receive/ioctl e
register/unregister_ldisc mudaram assinaturas. Adaptar ao TTY upstream e
comparar buffering/lifetime, nao criar headers4.9, casts de callbacks ou
stubs que escondam a incompatibilidade. Recursos genpd/PMIC/EMI e lifecycle
completo ainda precedem a entrega WMT/Wi-Fi no aparelho.

### Estado de tela WMT por DRM panel follower

Etapa antes de implementar: entrega observavel futura e WMT reagindo ao painel
DRM real com as flags LG de sleep/LPBK/blank; aceitar offline callbacks ON/OFF,
registro com painel ja ligado, ausencia de propriedade panel (laboratorio
headless), erro/defer sem MMIO posterior e stop/remocao sem work pendente.
Nao exigir painel para primeiro Wi-Fi headless nem declarar tela fisica pronta.

| Funcao | Reuso / origem / licenca | Compatibilidade / lifecycle | Decisao |
| --- | --- | --- | --- |
| Notificacao de display6.18 | LTS2926d88 drivers/gpu/drm/drm_panel.c SHA384d6629b2bca1c1e7667c51f3f153820d627d69029df61f794cdbf73d4381d9 e include/drm/drm_panel.h SHAbdf2a6559ca06d773068f39154cd4d3badc1dfcfeee0151ee97c151a7e8dd6d4, ambos permissao MIT NVIDIA preservada | panel_enabled apos painel/backlightON, panel_disabling antesOFF; add pode chamar enabled sincronamente. Registro usa propriedade panel; remove sincroniza callbacks via follower_lock e chama disabling se ligado | Reusar API, sem notifier paralelo ou restaurar numero FB_EVENT_BLANK. Mainline e LTS oferecem o framework; pmaports/Qualcomm/Motorola nao fornecem melhor equivalencia comprovada para K40S conforme triagem existente |
| Cola especifica WMT | wmt_dev.c LG GPLv2 f79b77ff e core CONSYS GPLv2 c04f4846, patches anteriores preservados | Mutex curto serializa ready/flags/schedule; work criado antes de wmt_lib_init. Probe registra follower antes de MMIO, propaga erro/defer e remove em falha de reg/clock. Ready somente ao fimWMT; stop bloqueia agendamentos e cancel_work_sync fora do mutex antes de destruir recursos. Remove follower antes de hardware cleanup | Pequena adaptacao nos arquivos existentes, nao driver/abstracao nova. Preservar flags LG e adiamento hif_info0. Aceite separado do lifecycle restante ainda falho e de firmware/PMIC; sem carga fisica |

Build6.18 tem DRM=y/PANEL=y. Verificar propriedade panel diretamente antes de
add, para nao converter painel configurado com erro em ausencia silenciosa.
Somente ausencia do vinculo e headless. O ramo Android EARLYSUSPEND nao existe
no6.18 usado; troca do ramo de tela e especifica a esta copia de port, original
LG4.9 preservado. Registro/teardown seguem singletonCONSYS ja existente.

Resultado de integracao: wmt-drm-panel-follower-v1.patch aplica sem fuzz sobre
os tres snapshots pre-painel preservados em artifacts/staging-wmt-lts-20261027-v1.
wmt_dev.panel-base.c SHAe3ef0023c22d2dea7416fd060c27c205f57acb136c90752fba7948aa674f964c,
core base SHA548f389000878fe2dc59568d79fd0749927687303b1528e6926132fe17c013d6,
header base SHAff1f04bb0f1c59298778229dafe4ca76d5ef06f6ba2011716fca2bb86aa23dbe.
WMT front e core CONSYS compilaram ARM32 com -Werror em
work/wmt-lts-panel-follower-20261027-a.log. wmt_dev.o SHA
410dc8fe2604b4b0b145decb2c59d0f4eea223ba3e760cb9a2e1d795bf591ad8,
core.o SHAfdad6e8d2eaeab31fee9999d3c551f3b8e72d01ec99b19c527a89269f49b32a9.
nm mantem drm_panel_add/remove_follower, cancel_work_sync e queue_work_on reais.
Reverse dry-run passou. Nenhuma alteracao de DT, imagem, config de kernel ou
aparelho nesta etapa. O modulo completo ainda nao chegou a link/modpost.

O gate tem duas prontidoes: WMT e probeCONSYS concluido. Isso cobre callback
imediato em add com painel ja ligado tanto antes quanto depois de WMT_init.
Mutex serializa flags/ready/bound e schedule; stop fecha ready e cancela fora
do mutex. Unregister fecha bound/attached, remove follower fora do mutex e
cancela; remove/deinit repetidos nao duplicam removeDRM. Hooks de probe anteriores
a reg/clock propagam erro e soltam follower nessas falhas. Outros erros de
PMIC/EMI/probe e outros produtores de work ainda requerem auditoria antes de
carga; esta prova nao certifica o lifecycle inteiro do WMT.

Teste test_wmt_panel_follower.py aplica patch aos snapshots fixados e compila
os callbacksWMT com as funcoes reais add/remove de drm_panel.c fixadas por SHA.
Pthread fornece mutexes reais; OF lookup, referencia/lista e fila work sao
doubles. Passou -Werror/UBSan em work/wmt-panel-follower-host-20261027-b.log
(versao final com os avisos de licenca no C gerado; tentativa a tambem passou).
Cobre panel ligado sincronamente, panelOFF inicial, inicioWMT/probe em ambas
ordens, hif_info0/late flag, headless, EINVAL/ENODEV/EPROBE_DEFER, duplicataEBUSY,
remove repetido e callbacks produtor pthread concorrendo com stop. Nenhuma
fila pendente apos stop/remocao. Teste confere wiring de INIT_WORK antes de
lib_init e stop antes dos locks, registro anterior a I/O no probe e seus dois
gotos de cleanup; nao executa probe OF completo nem worker de energia real.
Codigo C gerado inclui avisos GPLv2 LG e MIT NVIDIA preservados.

Build agora para em stp_sdio.c: timeval/do_gettimeofday no timeout TX semACK,
prototypes ausentes e tres proc_create ainda usam file_operations. Esse e o
proximo bloqueio concreto; preservar timeout, propriedade de transporte e
recuperacao ao adaptar. Sucesso de callbacksDRM offline nao prova painelJD9365D,
CONSYS ligado, suspend ou Wi-Fi no aparelho.

### Camada Linux HIF SDIO

Etapa atual: compilar a camada Linux do WMT mantendo wake-up e lifecycle;
entrega final continua WMT6765 no6.18, nao modulo4.9 nem stub. hif_sdio.c LG
GPLv2 original SHAdb9b379ccda4902d2cfc5662694b194c6687ecd6daf2df86eca5bcfdee273ef2.
Alternativas mainline/pmaports/Qualcomm/Motorola continuam conforme triagem
abaixo: APIs MMC upstream usadas pelo proprioHIF, sem substituicao comprovada
do protocolo. Reusar codigo LG e interfaces6.18, esforco minimo de declaracoes.

irq_flag_set e somente referenciada no mesmoC: static sem alterar atomics/IRQ.
drv_init e driver_exit sao exportados e consumidos por wmt_dev: declarar em
hif_sdio.h GPLv2 SHA f5c8626d5e6ff8ba9cd267cf236f82d6e5fe1ab6d390c8f8f1901d073bb26d66.
driver_exit real e VOID, header wmt_dev.h o declara int por engano: corrigir
somente essa assinatura, preservando cleanup e chamadas. Header GPLv2 original
SHA0cdefeaf878e52d0e77d23448da75a8b8d51c15beb692897ee1cc95b507f0897.
Reindentar o loopCCCR de timeout sem trocar tokens C/escopo: read/log/reset
permanecem no loop8, if/else continuam controlando somente log. Aceite imediato
build com -Werror e diff de fluxo, sem mudar falha/limites ou recuperar por no-op.
Patch wmt-hif-sdio-declarations-v1.patch, nao valida probe/remove fisico ou MMC.

HIF SDIO, stp_dbg_soc/combo e OSAL compilaram em work/wmt-lts-hif-sdio-20261027-a.log.
Proximo wmt_dev.c GPLv2 original SHA
f79b77ff90454fc92da29b04b955b5be651e7007f208a043905d97d26f171c69.
APIs independentes: proc_create6.18 exige proc_ops/proc_read/proc_write, removendo
owner obsoleto so das duas tabelas proc (manter file_operations do char device).
Usar class_create(name), como no detector portado. Quatro callbacksWMT e helpers
de proc/bgw sao internos ao mesmoC, portanto static; compat_ioctl tambem e
interno. Entradas globais file_exist e tra_btif/uart sem consumidores locais
identificados recebem prototype no wmt_dev.h, mantendo ABI/corpos em vez de
inventar stubs ou apagar comportamento. Nomes/permissoes/reads/writes/cleanup
preservados; nao habilitar interfaces novas. Reuso procfs/device/OSAL do LTS,
mesmas alternativas auditadas; pequena adaptacao ao driverLG, nao novo driver.

Bloqueio de tela confirmado: FB_EVENT_BLANK foi removido mesmo com FB_NOTIFY=y.
DRM panel follower6.18 fornece panel_enabled/panel_disabling e sincroniza lista
de seguidores, candidato real para substituir notificacao blank. Exige device
com propriedade panel e ordem correta de init/remocao/cancel_work; WMT cria work
depois de registrar core hardware e nao expoe device ao front. Nao definir numero
do evento antigo nem retirar politica de energia para compilar. A integracao
DRM/DT/probe deve ser decidida com a fonte da tela nativa e lifecycle.

Outro bloqueio independente e timeval no cache termicoWMT. Substituir somente
tipo por timespec64 e leitura por ktime_get_real_ts64, igual ao PSM/OSAL LTS.
Politica usa apenas tv_sec: preservar REFRESH_TIME300 com > estrito, atualizacao
por historico quente/trafego, sensor enable/read/disable, indice e locks.
sizeof usa o novo tipo e logs usam segundos64. Nao mudar para monotonic nem
diminuir verificacoes termicas. Patch wmt-dev-thermal-timespec64-v1, mesmo fonte
GPLv2 acima, APIs mainline existentes; teste do callback real deve comparar
cache, refresh e historico com fonte LG antes de aceitar futura ativacao.

Resultado: work/wmt-lts-dev-api-20261027-a.log registra somente erro
FB_EVENT_BLANK neste arquivo, sem erros residuais de procfs/tipos/tempo/classes.
wmt_dev.c staged SHAe3ef0023c22d2dea7416fd060c27c205f57acb136c90752fba7948aa674f964c;
objeto ainda nao compilado e modulo nao chegou ao link. HIF SDIO ARM32 objeto
SHA8ebbcb4fe6b9b004efcd5363d12d0ee6c736d6b54b8fa3fd9b4d976208359c19,
OSAL SHAb292032a3b79a84fcf11ab6e443bfbb073592c2f66f0cf96370e80a5bb7550c1,
igual a primeira provaOSAL. diff -w do HIF mostra somente static no helperIRQ;
fluxo wake-up manteve tokens. Reverse dry-run dos tres patches desta etapa
passou sem fuzz.

Teste test_wmt_dev_thermal.py reutiliza function/cc/unittest com callback real
extraido do fonte GPLv2 fixado, antes/depois do patch de tempo, e doubles somente
para relogio/trafego/sensor/locks. Passou -Werror e UBSan em
work/wmt-dev-thermal-host-20261027-a.log. Aceite offline: cache frio nao le sensor,
sentinela99/historico quente mantem leituras, gatilho de trafego, exatamente300s
usa cache e301s atualiza, recuo de relogio atualiza, temperatura0x85 vira-5,
sequencia enable/read/disable e sensor fora do spinlock. Nao prova sensor real,
concorrencia com remove nem protecao de carga; nenhuma operacao no telefone.

Proximo incremento concreto e ligar estado de tela ao WMT por API DRM real,
com INIT_WORK anterior a qualquer callback e cancelamento sincronizado no
teardown. Fonte de sequencia JD9365D e controlador6765 ja inventariada em
hardware-source-and-re-audit-20261027.md; nao existe justificativa para recuperar
essa sequencia por RE ou criar evento framebuffer ficticio. O uso headless de
laboratorio nao comprova politica de tela; ausencia de painel nao deve virar
pre-requisito artificial para Wi-Fi, mas o caminho de painel deve permanecer
explicito e verificavel. Integracao de clocks/reguladores/genpd/EMI e lifecycle
continua pendente antes de carregar WMT.

### STP: consistencia da assinatura PSM

Etapa seguinte: avancar WMT completo contra6.18 sem alterar protocolo de energia.
Reusar enum LG MTKSTP_PSM_ACTION_T, ja empregado pela implementacao de
mtk_wcn_stp_psm_notify_stp e por stp_psm_notify_stp. Header stp_core.h GPLv2
SHA503ba84175ad45dbc256fe589832e219d82eab0da2461257722ed3a8150d98fb
declara UINT32; callback local em wmt_core.c GPLv2
SHA119b653327849872ff86f2d909e43b7e0fa6c36c9218d4a04887a4c60b87cd74
declara INT32. Unificar ambos ao enum real, mantendo implementacao stp_core.c
SHAe347e59f79693bab4191529a32d3b7c33c909423b7cc233d9b4d75d32a1a3e85
intocada. Enum0..4, limite5; nenhum valor, pacote, timeout ou retorno alterado.
Mainline/pmaports/Qualcomm e Motorola ja triados nao substituem esse protocolo
vendor; ajuste minimo de tipos ao codigo LG existente, sem novo driver/API.
Aceite imediato: objetosSTP/WMT compilam com -Werror; carga depende do modulo
inteiro e lifecycle/recursos. Patch wmt-stp-psm-signature-v1.patch, snapshot sem
commit, licencas GPLv2 preservadas. Nao ha alteracao de probe/remove nesta etapa.

STP compilou; proximo erro e missing-prototypes de wmt_ctrl_ul_cmd. Busca em
todosC/H confirma chamadas apenas no mesmo wmt_ctrl.c LG GPLv2 original SHA
bc0565dfba16a3b854f9fce64aaa0514622dfd9bfd1e7c88d1872eb39cf5b860.
Aplicar linkage static somente nesse helper privado (wmt-ctrl-private-helper-v1),
sem trocar nomes publicos, timeout6000, buffer, wait ou retornos. Compilar objeto
com -Werror; nao novo framework ou protocolo. Mesmo criterio de reuso acima.

wmt_ctrl.o passou; wmt_func.c GPLv2 original SHA
cf2389ee805d68c43fc1143acb94625da40519c05ba547d72743a625f76542e6
requer inline no inicio de declaracao. Reordenar _osal_inline_/INT32 em BT/ANT
sem mudar linkage ou corpo; _osal_inline_ no OSAL e inline. Helper wifi_ctrl
tem chamadas apenas nas funcoes on/off do mesmoC, sem export: static. Patch
wmt-func-declarations-v1.patch, mesmas alternativas e justificativa de reuso;
nao e nova implementacao de controle nem alteracao de falha/probe/remove.

wmt_func.o compilou. wmt_core_rx_flush e wmt_core_opid_handler sao definidos e
chamados somente no mesmo wmt_core.c (referencia externa e comentario #if0).
Linkage static dos dois em wmt-core-private-helpers-v1.patch elimina
missing-prototypes sem mudar flush/dispatch, handlers ou erros. Fonte e licenca
do wmt_core.c ja fixados acima, mesmas alternativas de reuso; aceitar por build
ARM32 mantendo warnings fatais e todos os caminhos existentes.

PSM seguinte: psm_core.c GPLv2 original SHA
5d91c50d5826932215203de6e064fa54dde3cf114d0226e3553d9bca50e58ef7
usa quatro helpers _stp_psm_* sem consumidores externos: get_free_op,
put_act_op, hold_data, has_pending_data. Linkage static preserva todas as
filas/locks/retornos. timeval/do_gettimeofday removidos do6.18 ocorrem no
detector de densidade e dois escritores de log. Reusar timespec64 e
ktime_get_real_ts64 do LTS (a mesma API do OSAL ja portado); manter relogio real,
SAMPLE_DURATION, comparacao estrita >, contador e limite de trafego. Dividir
tv_nsec por NSEC_PER_USEC tanto na comparacao quanto nos logs preserva o
arredondamento de microssegundos4.9; nao trocar por monotonic ou mudar algoritmo.
Campos de log32 preservados; janela de densidade ganha segundos64. Sem novas
implementacoes de tempo. Mesmas alternativas STP acima; code existente e mais
compativel que qualquer protocolo generico. Esforco pequeno com prova dirigida
da borda temporal antes de carga; probe/remove nao mudam.

PSM compilou em work/wmt-lts-psm-timespec-20261027-a.log. Harness
test_wmt_psm_time.py reutiliza function/cc/unittest como os testes anteriores;
compara o callback LG original e patchado, com tempo/flags/monitor simulados.
Fonte/header fixados por hash; psm_core.h SHA
3d5944f25676735bb0452a1545d4ef58ae34e9d379035b8d030b3fe08daa2e85.
Passou com -Werror e UBSan em work/wmt-psm-time-host-20261027-a.log: mesmo
microssegundo nao expira, proximo microssegundo expira, limite50000 estrito,
RX/TX, relogio recuado, proximo segundo e janela baixa limpando flag apos alta.
Nao testa concorrencia, suspensao fisica ou threadPSM inteira.

Proximo arquivo wmt_ic_soc.c LG GPLv2 original SHA
6f4d845657449efecb3f229979d5237c237512d2a87cb938ead9d3833a1ffa5e
tem cinco chamadas ioremap_nocache removidas. Reusar ioremap pela equivalencia
literal do alias ARM4.9 ja auditada; preservar enderecos, tamanhos, checks,
conteudo de firmware/calibracao e iounmap. Patch wmt-ic-soc-ioremap-v1.patch,
nenhum novo protocolo, acesso ou suporte a firmware inferido por build. Analise
de limites EMI/firmware e falhas continua anterior a carga no aparelho.

wmt_ic_soc.o compilou. wmt_lib.c GPLv2 original SHA
3a7ae26ce86d46b94c3ad09e3e0722b05933a4299498b828282513e8807e3295
e o proximo bloco: dois callbacks wait_event, utc_time_sync, rstmsg_snd e
state_init possuem referencias somente no mesmoC: tornar static, preservando
esperas e recuperacao. def_patch_name nao tem consumidor encontrado; conservar
entrada global existente e acrescentar prototype ao header, sem novo export.
MMIO MET tem uma chamada ioremap_nocache: mesma equivalencia ARM auditada.

Politica BT de reset as2h: substituir do_gettimeofday por
ktime_get_real_seconds, mantendo subtracao sys_tz e cast ULONG32 existente;
usar rtc_time64_to_tm sobre esse mesmo valor32, que no6.18 substitui
rtc_time_to_tm. Nao mudar politica de reset/horario ou disparar reset nesta
triagem. Reuso LTS timekeeping/RTC estabelecido, sem algoritmo de calendario
proprio; APIs de regulacao/SoC/probe permanecem independentes, esforco minimo.

wmt_lib.o compilou. stp_exp.c GPLv2 original SHA
c7de032dbadca5c06d560333adb7dfddda5929f14aaff5874ddc52558d607c46
exporta mtk_wcn_stp_sdio_wake_up_ctrl mas omite prototype. Preservar esse
export/corpo e acrescentar declaracao no stp_sdio.h junto a stp_sdio_wake_up_ctrl.
Header GPLv2 original SHA9e0304a45b7feda8108ad2310974a443f59a844b94cc3d4d98f47d46311f9657;
ja inclui hif_sdio.h que define ctx. Patch wmt-stp-sdio-wakeup-prototype-v1,
sem adicionar implementacao ou mudar erro/probe/remove, build com -Werror.

stp_exp.o passou; wmt_exp.c GPLv2 SHA
35d9cd25dc6e60d931b02af2d2f3cdc3c1673571e3e7503bbaa1f1060e67210f
tambem exporta setter de versao Wi-Fi sem prototype. Declarar assinatura existente
em wmt_exp.h GPLv2 SHAee2c8ed422a47df3ddc231fc470fe09ce1db2cbe0abf8fae7f835c0b8c42845e,
junto a wifi_fem_cfg_report; preservar corpo/export e informacao de versao.
Patch wmt-wifi-version-prototype-v1, nenhuma implementacao paralela ou efeito
de probe/erro/remove. Reusar ABI vendor e -Werror continua sendo o aceite offline.

wmt_exp.o passou. btm_core.c GPLv2 original SHA
ac4f002d0939ffb752ffacc02c7df68f2340e2392f1a469a41752292ed9a6a7f
tem get_free_op/put_act_op com uso apenas interno. Aplicar static mantendo
filas e recuperacao, sem reduzir checks de compilacao; patch
wmt-btm-private-helpers-v1.patch. Mesmo reuso de codigo LG/OSAL e nenhuma nova
API/protocolo ou efeito de probe/erro/remove.

Resultado: build work/wmt-lts-core-progress-20261027-h.log atravessou todos os
objetos de common_main/core e passou btm_core.o/wmt_ic_6630.o, depois parou na
camada Linux hif_sdio.c. Erros atuais: prototypes ausentes irq_flag_set,
drv_init/driver_exit e misleading-indentation em _hif_sdio_wake_up_ctrl linha505.
Inspecionar consumidores e fluxo antes de alterar esse trecho; nao suprimir
warnings nem remover o transporte por ser diferente de HIF Wi-Fi AXI.

Objetos ARM32 finais desta etapa: STP SHA2656e410da2fbebac9d4de41dc4ef4bc4605d786336b00af447e736acfd365a2,
WMT core SHAd118b572aa5ae16405778c9987ae27962ed29e9f81d6733ec2f2ee54d103d7a5,
PSM SHA54cb4dece45397fd12d01b4f4ebbd128bad04a86f5853ee87e4e216dbf5f72fd,
ICSoC SHAabe486f2beb866ba94b8bca1a096ce528f9c4927c67d6df22b0d3b507a916823,
lib SHA13bb1bfc2acfa1b2d3cd08f17c6249fa7f7d90513b170425b15272304eb65278,
exp SHAe36b7fdc7f4e06d6da1c8e862187074dd778f1f7a8b3ff3f56ad5d61986610f6,
BTM SHAcbb843586ccaa407ef1e1b806c8670c8823280ec8850f12cd96f2e7967bd7ba1.
stp_core.c comparado byte-a-byte ao original, igual. Reverse dry-run dos patches
assinaturaPSM, timespecPSM e APIlib passou sem fuzz. O teste de borda temporal
ja passou apos a mudanca correspondente, sem repeticao de suites amplas.
Nenhum modulo linkado/aprovado, nenhum kernel/imagem alterado ou novo ensaio
no aparelho. Integracao genpd, PMIC/XO/EMI e lifecycle/falhas ainda pendentes
antes da entrega WMT/Wi-Fi funcional no6.18.

### Backend WMT MT6765: interfaces MMIO e DMA

Etapa seguinte (antes de implementar): entrega no aparelho continua WMT6765
com alimentacao/clock/EMI reais; aceite offline e compilar o backend preservando
as barreiras LG e expor dependencias restantes sem stubs. Reutilizar o header
sync_write.h LG GPLv2, SHAb72d53e2b5626e3fd932ff1d84eaebbb1da2ac352cd7deecd4ac0c5ad5f5c08e,
snapshot sem commit, copiado byte-a-byte para vendor-api. Ramo kernel usa
__raw_write{l,w,b} mais mb; Linux6.18 fornece essas APIs. Build ARM32 e LE,
MMU/SMP/ARM_HEAVY_MB=y: mb em ARM passa por dsb/arm_heavy_mb. Nao mudar a
sequencia por writel sem barreira posterior. Sem novo codigo de MMIO ou probe;
licenca preservada, escopo somente backend LG, esforco minimo. Alternativas
mainline/pmaports/Qualcomm e doador Motorola ja comparadas na triagem abaixo;
nenhuma exige substituir esse helper para compilar este hardware.

O adapter LG declara connectivity_arch_setup_dma_ops com struct iommu_ops*
sem declaracao antecipada. Adicionar somente struct iommu_ops; ao header GPLv2
ja auditado fixa o tipo C sem implementar DMA. Linux6.18 ARM arch_setup_dma_ops
agora recebe (dev, coherent), contra cinco argumentos4.9; nao chamar essa API
diretamente de modulo nem descartar parametros ate verificar seus consumidores
e a configuracao OF/DMA do dispositivo. Link/modpost deve exigir simbolos reais.

Continuidade da triagem: a funcao DMA antiga nao tem consumidores no common LG
(busca em todosC/H); ela pertence ao adapter compartilhado com outros modulos.
Nao implementar sua conversao sem consumidor. Apos sync/forward, compilacao
para em mtk_btif_exp.h incluido pelo header stp_dbg; preservar tipos BTIF que
tambem pertencem ao transporte BT/GPS/FM, sem inferir que HIF Wi-Fi AXI substitui
esse caminho. Copiar interface GPLv2 LG exata, SHA
28d7bbe6ec3f83f7dd644d55123b1b15b511b7b06384b15231b52cad50d7be78,
sem copiar driverBTIF nem introduzir stubs.

Headers adicionais para compilar o bloco6765, todos GPLv2 conforme
avisos de cada arquivo LG, snapshot sem commit: upmu_common.h SHA
5113b94bcf5ba69b8901518c75ca95fc5ec62884c1d6b1048d9c94188cb4bf66,
mach/upmu_sw.h SHA21cec69f51972bf7d0c218a151043d395d83a38a6fbd709cc7c058ad08b00ae5,
mach/upmu_hw.h SHAce55730f6a0b1201e25084e9a6c17e4778946105e6d4683b5e7490696ab51855,
clkbuf_v1/mtk_clkbuf_ctl.h SHA077e25751fc95a0158e629837c8c439018b716749fde11eed268e0046b60bb42,
mt6765/mtk_clkbuf_hw.h SHacaafbaff6f08c2532c9cdad4d583885b7560898cc5f3fa2d468a5b3d0a1372fb.
Copias selecionadas preservam tabelas/enum e chamadas externas reais de PMIC e
XO. Wrapper de triagem seleciona CONFIG_MACH_MT6765=1 somente nos objetos WMT,
pois autoconf6.18 usa MACH_MT6765_K40S_EARLY e nao o nome legado. Isso garante
que header clkbuf escolha o SoC certo e adapter declare KERNEL_clk_buf_ctrl;
nao habilita driver no kernel nem inventa suporte runtime. Mainline/regulator/CCF
continuam o destino da integracao; copying headers nao fornece implementacoes.
Probe LG ainda tem regulator_get verificado por NULL em vez de IS_ERR, e clock
conn ainda representa MTCMOS4.9; esses caminhos exigem adaptacao antes de carga.

Proximo erro real: quatro chamadas ioremap_nocache no backend6765 (tres ativas,
uma AFE desabilitada). LG arch/arm/include/asm/io.h define literalmente
ioremap_nocache como ioremap; Linux6.18 ARM conserva ioremap, MT_DEVICE e retorno
NULL na falha. Reusar essa API com mesmo endereco/tamanho/checagem/iounmap;
patch wmt-mt6765-ioremap-v1.patch troca apenas o nome. Backend GPLv2 original
SHA0c55b27dbe1f6174a23933d629bd13665e2a1d264e0b512ff14eac13cc215ecc,
sem novo helper, efeito de probe/erro/remove preservado para esses mapeamentos.
Compilacao com -Werror e comparacao reversa do patch bastam para essa troca de
alias; seguranca das escritas e lifecycle inteiro ainda nao sao aprovados.

wmt_plat_alps.c GPLv2, original SHA
c84fd6da1924fb3dafe37c010e3cf1cdf6734ccd983ff58fc51bf2ecc931a80d,
usa somente osal_wake_lock*, nao chama API Android wake_lock*. Remover include
obsoleto linux/wakelock.h reutiliza OSAL portado/LTS wakeup_source, sem desligar
CFG_WMT_WAKELOCK_SUPPORT. RTC PIN_RTC e chamado somente por mtk_wcn_cmb_hw.c;
backend6765 usa XO_WCN. Condicionar include, declaracao, entrada de tabela e
funcao RTC a MTK_WCN_COMBO_CHIP_SUPPORT preserva o ramo combo e elimina dependencia
nao usada por CONSYS. Dispatcher existente testa callback NULL e retorna -2:
uma solicitacao PIN_RTC indevida no build SoC continua falhando explicitamente,
sem simular sucesso nem no-op32k. Nao muda a selecao dinamica de chip ou clocks
CONSYS. Init plataforma ainda ignora erro de wakeup allocation e hardware;
correcao desse lifecycle e pre-requisito concreto antes de carregar WMT.

Plataforma, proximo ajuste estritamente C: ISR BGF somente registrado via
request_irq no mesmo arquivo passa a static. wmt_plat_sdio_ctrl recebe UINT32
conforme header publico e consumidores wmt_ctrl.c; preserva valor32bits ARM e
chamada board_sdio_ctrl. Funcoes existentes irq_ctrl/ps_ctrl (retornam -1 e nao
tem consumidores encontrados) recebem declaracao no header publico GPLv2 para
preservar nomes/assinaturas em vez de suprimir missing-prototypes. Nenhum corpo
de controle alterado; patch wmt-platform-prototypes-v1.patch complementa OSAL/RTC.

Core CONSYS GPLv2 original SHAc04f4846bc82e397b86fa8bd1c7b1004d49eb07abff54d7e7c1916a6c2f2bc67:
proximo incremento compila contra platform_driver.remove void do6.18, mantendo
cleanup que antes sempre retornava0. Helpers reg_ctrl/gpio_ctrl sao internos ao
mesmoC, portanto static; restore so e registrado sob CONFIG_MTK_HIBERNATION,
declarar/compilar nesse mesmo guard. ioremap_nocache usa o alias ARM ja auditado.

O diagnostico mtk_wcn_consys_reg_ctrl calcula VLA index*4+4 e assume dois cells
por endereco/tamanho. Limite antigo usa size < offset e permite acesso32 no fim.
Reusar of_address_to_resource (LTS drivers/of/address.c GPL, export GPL) com
struct resource/IORESOURCE_MEM, sem novo parser nem allocator. Aceite: dispositivo,
node e valor presentes; index dentro enum existente; traducao DT valida; recurso
MEM com inicio<=fim, pelo menos4bytes, offset alinhado e <=size-4 antes de ioremap.
Getter nao modifica value na falha. Preservar leitura/escrita sincronizada e
iounmap no sucesso. Mesma finalidade/layout6765, suporta cells/ranges do OF;
falhas agora recusam endereco invalido antes do MMIO. Mainline/Qualcomm/pmaports
nao substituem o backend6765, mas a API OF existente elimina esta logica privada.
Esforco pequeno; validacao de falhas e carga ainda deve preceder uso no aparelho.

Validacao direcionada reutiliza extrator function do harness RTC/bateria e
cc/unittest ja usados, sem transporte. Teste do callbackC real extraido do fonte
LG fixado, aplicando patches API/OF em copia temporaria. Doubles apenas para
OF/ioremap/MMIO: exercitar sucesso read/write, erros e limites; nao comprovam
traducao OF real ou comportamento eletrico. Header do enum original GPLv2
SHA7d479560e50b7cefa66b48d2865cabc006cf583f0b2b607a23334674ed443a59.
Nenhum novo parser/driver de producao ou diagnostico no aparelho.

Resultado desta etapa: mt6765.o SHA4596109a63d5dc6962374391d19a3d1bbe3f40eede82ccfccc6c26f209c3c9b3,
wmt_plat_alps.o SHAd9c8459ab250006e783f9258c5d380b4ba32434959fd2a82b430d31b4cc2a856,
mtk_wcn_consys_hw.o SHA3901491244ff49b89064b2837aed6420e0cabae0784b4d465c1715a421463e98.
Compilacao ARM32 com -Werror em work/wmt-lts-connsys-core-20261027-a.log,
avancando depois tambem cmb_hw, wmt_ic_6628 e wmt_conf. Modulo completo para
em stp_core.c:1623: definition MTKSTP_PSM_ACTION_T versus header UINT32 em
mtk_wcn_stp_psm_notify_stp. Nao houve link/modpost ou modulo carregavel aprovado.
nm no backend mantem dependencias reais connectivity_export_clk_buf_ctrl,
connectivity_export_pmic_set_register_value/upmu_set_reg_value, regulator e CCF.
objdump ARM mostra dsb sy seguido de arm_heavy_mb nas escritas; sync_write.h
copiado tem SHA original. Reverse dry-run dos patches MMIO/core/OF passou sem
fuzz. Isso comprova geracao de barreiras ARM, nao comportamento eletrico.

Teste host passou em work/wmt-connsys-resource-host-20261027-a.log: callback
real aplicado a copia do fonte fixado, cc -O2/-Werror e UBSan sem diagnosticos.
Leitura/escrita em todos indices do enum, ultimo acesso valido, recurso4bytes,
endereco acima4GiB sem truncar; falhas para device/node/value ausentes, indices
negativo/alemdoenum, traducao OF com erro, recursoIO/invertido/curto/desalinhado,
offset desalinhado/no fim/alemdo fim/UINT32_MAX e ioremapNULL; nenhuma escrita
ou alteracao da saida de leitura nesses erros. OF e MMIO sao doubles; nao prova
parserOF real, IRQ, concurrency com remove, PMIC ou WMT no aparelho. Nao houve
operacao fisica nem mudanca de boot/kernel4.9 ou protecoes de recuperacao.

### WMT: detector integrado compilado contra o provider CONN

Incremento offline apos a sessao do provider: entrega futura no aparelho e
inicializar WMT6765 com recursos reais e recuperacao. Aceite imediato deste
incremento: compilar o detector preservando a classificacao SoC/combo, sem
arrastar a energizacao RTC/GPIO de chip externo para CONSYS_6765. O modulo
completo e seus caminhos de init/falha/exit continuam pendentes.

Reuso continua conforme a triagem WMT abaixo: LG e o caminho funcional do
hardware, LTS2926d88 fornece APIs de dispositivo/CCF/genpd/regulator; mainline,
postmarketOS, Qualcomm e o doador Motorolae6cfe39 nao demonstram substituto
compativel para CONSYS AXI6765. Nao ha lacuna que justifique engenharia reversa
ou novo driver nesta etapa. Fonte original LG preservada em conn-src no Linux;
mudancas aplicadas apenas a module-workspaces/staging-wmt-lts-20261027-v1.

| Funcao | Origem / revisao / licenca | Compatibilidade e efeitos | Esforco / decisao |
| --- | --- | --- | --- |
| Selecionar energizador externo | Makefile LG SHA b8ef228b1da839a3f6659bddbd43155d28920e10a7d5599f810254f2616e05c0, snapshot sem commit, sem aviso de licenca proprio; wmt_detect.c SHA8351877a4a1f162ac0c0a08a432aa7162a14379640b0a7cc1d47de47e31090db e wmt_detect_pwr.c SHA1b059f82dc606f1c8d73667fb824738266df1636e672df729e8bc3be14db87cc, ambos GPLv2 | Todas as chamadas ao objeto pwr estao sob MTK_WCN_COMBO_CHIP_SUPPORT no detector. Makefile ja calcula COMBO_CHIP_SUPPORT=false para CONSYS_6765. Detector e init/exit permanecem; somente objeto externo passa a seguir essa selecao. Caminho combo conserva o objeto; sem alteracao de sequencia eletrica ou RTC | Minimo: wmt-combo-power-object-conditional-v1.patch, aplicado ao Makefile.vendor da copia isolada. Licenca do Makefile ainda nao confirmada por arquivo; nao redistribuir a arvore vendor como pacote aprovado |
| API do detector no6.18 | Mesmo wmt_detect.c GPLv2; include/linux/device/class.h do LTS2926d88 GPL-2.0-only declara class_create(name) | Remover argumento owner obsoleto; cdev.owner e file_operations.owner preservados. Callback write usado somente no mesmoC passa a static, corpo igual. Sem mudar init/exit, ioctls ou nomes de dispositivos | Minimo: wmt-detect-linux618-api-v1.patch; validar por build ARM32 com -Werror |

O build usa agora a build lts-6.18.58-native-connsys-v1 e seu autoconf atual.
Triagem explicita adicionou via KCFLAGS os dois diretorios LG connectivity/common
e include/mt-plat. Isso amplia o include antes restrito ao OSAL: o detector precisa
mtk_wcn_cmb_stub.h (GPLv2, SHA35ba235d8bb730b6250cc819d1b0aa9cdf103ac3299f60abe895fac96f900221)
para enums/callbacks e prototipos. Nao adiciona implementacoes de adapters ao
kernel6.18. Esse include amplo e somente triagem; nao e receita aprovada para
payload. mtk_rtc.h contem macros vazias sem CONFIG_MTK_RTC e nao deve ser usado
para obter sucesso artificial de build. O objeto que o exigia foi condicionado
pela selecao real de hardware, sem habilitar CONFIG_MTK_RTC ficticio.

Evidencia: work/wmt-lts-combo-conditional-20261027-a.log avanca alem do objeto
pwr e recusa mtk_wcn_cmb_stub.h; tentativa b, com header LG, revela class_create
e callback sem prototype. Apos patch de API,
work/wmt-lts-detect-api-20261027-a.log compila wmt_detect.o e sdio_detect.o,
e para em mtk_wcn_stub_alps.c:436, faltando prototype de
mtk_wcn_cmb_stub_do_reset(unsigned int). O simbolo e EXPORT_SYMBOL no LG,
portanto nao torna-lo static para esconder o erro. -Werror permanece ativo.
Modulo nao chegou ao link/modpost; dependencias reais de clock-buffer, PMIC,
EMI/DMA e genpd ainda precisam integracao. Nenhuma nova operacao no aparelho.

Proximo ajuste de declaracao (antes de implementar): preservar o export de reset
LG com a assinatura existente, acrescentando somente o prototype ao header GPLv2
mtk_wcn_cmb_stub.h copiado em vendor-api na arvore isolada. Patch
wmt-cmb-reset-prototype-v1.patch; corpo e EXPORT_SYMBOL permanecem inalterados.
Reusar interface vendor evita inventar API de reset. Copiar somente esse header,
connectivity_build_in_adapter.h e wmt_build_in_adapter.h (todos GPLv2) permite
retirar os includes amplos da triagem anterior. Wrapper privado em
artifacts/staging-wmt-lts-20261027-v1/Makefile usa apenas vendor-api e a config
da build CONN; nenhuma macro de RTC ou implementacao vazia nova. Callbacks,
registro, erro e remove ainda dependem do modulo completo.

Resultado com include restrito: work/wmt-lts-vendor-api-20261027-a.log compila
os dez objetos common_detect e drv_init, incluindo mtk_wcn_stub_alps.o; corpo
desseC manteve SHA82df6864fabfa243f722101473956f96b847ee770b19736783cc293a93c45a67.
Header de reset derivado SHAb3c0d2d9776146df09d6118f80c36eb7e4b5dc03f3f3c4204fda8644b843b2a1;
wmt_build_in_adapter.h original SHA57b97fe5fa8a26a66f4c2b058b256f3c4f8acf7805f47ecd18ed03ac980377ac.
Verificacao make -n -p confirmou wmt_detect_pwr.o ausente no ramo CONSYS e
presente com COMBO_CHIP_SUPPORT=true. Os patches combo/API aplicam em copia
limpa dos originais LG com --dry-run --fuzz=0. Sem suites amplas repetidas.

Bloqueio atual do build: mt6765.o encontra falta de declaracao antecipada de
struct iommu_ops no adapter antigo e falta de sync_write.h no header de hardware.
Inspecao LG: sync_write.h GPLv2 faz __raw_writel seguido de mb() no ramo kernel.
LTS ARM writel aplica barreira antes da escrita; logo trocar cegamente por writel
nao preserva a barreira posterior LG. Reusar o header exato e candidato para
triagem; qualquer adaptacao MMIO deve preservar ordenacao e ser validada antes
de carga. Nenhuma alteracao de MMIO, clock, regulador ou imagem nesta etapa.

### CONNSYS por genpd: provider OFF validado, consumidor WMT pendente

A pedido do usuario, nova sessao residente iniciada em 2026-10-27 ~16:07 local
para testar no6.18 sem restaurar4.9 entre verificacoes. Mesma imagem validada,
ramdisk com limite3600s conferido no cpio, --resident-minutes60 e watchdog intacto.
Log work/connsys-resident-long-session-20261027-a.log confirmou SSH residente;
uname6.18 e CONN off-0 conferidos. Sessao nova apos ensaio aprovado, nao retry de
candidato falho. Nao e instalacao permanente: o ciclo continua responsavel por
captura/restauracao ao fim ou k40s-resident.py end. Revalidar processo real e
SSH antes de continuar; o estado deste registro nao prova que segue ativa.

Ensaio fisico do provider OFF aprovado (2026-10-27, nao WMT/Wi-Fi): kernel
compilado na copia lts-6.18.58-native-connsys-v1, config identica a baseline,
zImage SHA262f1d21a510a60405943d1d93b1b337dfd2321f2f7122fb13a6c352cbfc97c7.
SPDX/patches anteriores preservados, nenhum driver do watchdog alterado. Build
final work/connsys-provider-kernel-build-20261027-c.log concluiu zImage; tentativas
anteriores foram interrompidas (comando de patches mal expandido e alvo amplo
modules desnecessario), sem uso de imagem incompleta. Cinco patches aplicados,
c/h resultantes iguais aos staged auditados; original validado mantido intacto.

Overlay de placa mt6765-k40s-connsys-provider-overlay.dts acrescenta somente tres
nos, teste libfdt/DTC passou e reservas/propriedades/phandles anteriores iguais.
DT resultante SHA90287ff88fe91ef3fd99f70e1c35ce4dd5ae5abca631a51da6bebb5e8e4a5694;
schema sem diagnosticos, seis entradas LK dtbo_a passaram (--native-touch).
Cmdline preserva exatamente a baseline PM, incluindo mtk_wdt.k40s_keep_on_suspend=1.
Imagem b7cd790ac10c056c7114a40a56ca3444363653ebe2382b393766257f0395d510,
em artifacts/native-connsys-provider-boot-20261027-v1; extracao reversa conferiu
kernel/ramdisk/DTB/enderecos/cmdline. Ramdisk23978a97 inalterado, limite3600s.
__log_buf=c1e8a284/20000, _end=c1ee8a10 iguais a baseline; captura41e8a000/21000.

Sessao work/connsys-provider-session-20261027-a.log, captura dram-20261027-160027:
driver mtk-power-controller vinculado ao filho SPM e genpd conn em off-0, sem
consumidores, tambem no follow-up. Leitura selecionada read-only por debugfs
regmap: SPM180=000fdf4c,184=000fdf4c,32c=00000112; BIT1 OFF nos dois ACKs,
controle baixo1f=12. Nenhuma solicitacao ON/WMT. V/I/T atualizaram de
4390301uV/-24800uA/363 para4390631uV/-18800uA/362; eMMC ro=1, mounts so RAM.
Primeiro comando de leitura terminou1 por grep de mount sem correspondencia;
follow-up terminou0 e listou mounts, sem falha dos getters. Logs physical-readonly
e physical-followup preservados. Console USB confirmou8 CPUs, emmc_ro e rootfs_ro
PASS, sem WARNING/BUG/Oops/panic observados. Nao comprova carga nem gating ON/OFF.

Encerrado por k40s-resident.py end, ciclo terminou0, 4.9.190-k40s-bringup de volta
por SSH, boot_a SHA5ffea913232fbde0673c3b2a946a9fab26b422e5ed03662d81a7096afd783de7.
A/B antes/depois SHA9f3448025c92cbb4e1feb4f020b7fea5deb50222962832b8fe408d753f92a117
iguais. Temperatura no4.9=359. Proxima entrega: consumidor WMT usando esse genpd,
clocks/reguladores reais e caminhos de erro; nao clock conn ficticio.

Integracao DT/probe de laboratorio (2026-10-27): entrega observavel e CONN
registrado OFF em genpd no6.18, sem consumidor nem chamada power_on. Aceite:
DT preserva byte-a-byte nos/propriedades/phandles/reservas preexistentes, apenas
novo SPM10006000 e filho controller/CONN; config igual ao kernel conhecido,
recuperacao intacta; probe estrito rejeita ACK/controle incertos sem energizar.

| Funcao | Atual | Reuso / origem / revisao / licenca | Compatibilidade e efeitos | Esforco | Decisao |
| --- | --- | --- | --- | --- | --- |
| Provider CONN na placa K40S | Profile privado dc17ae62 validado nao tem sleep/SPM; INFRA nativo e syscon e simbolo mt6765_infracfg ja existe | genpd/syscon/simple-mfd e driver LTS2926d88 GPL-2.0-only, patches CONN acima; DTC/fdtoverlay1.7.0, dt-schema2026.9 e adaptador libfdt portkit.core.devicetree existente. LG identifica SPM10006000 e area1000. Pmaports/Qualcomm nao substituem esse mapa | Novo no SPM nao deve disputar nodo existente; compat mt6765-scpsys nao consta no mtk-scpsys legado deste LTS. Filho power-controller usa match correto e OFF estrito, sem clocks/supplies/IRQs/WMT. Syscon so mapeia; probe le ACKs/controle. Sem unbind e sem callbacks ON durante registro | Pequeno DT; build isolado e ensaio curto depois das verificacoes | Overlay de placa referencia simbolo INFRA ja existente sem rotular novamente. Reusar DTC/fdtoverlay/libfdt e teste de preservacao, nao parser/driver novo. Copiar arvore6.18 conhecida e aplicar cinco patches genpd; nao alterar build/fonte/boot4.9 recuperavel. Primeiro ensaio nao inclui carga nem controle do charger |

Resultado descriptor MT6765 (2026-10-27): header unico em
kernel/components/socs/mediatek/mt6765-pm-domains.h, SHA
9a47cd510a7765d3880c9c5eb06c3e9621cdaab1cab104569c12b8af3dad0f0f;
instalado pelo workspace no diretorio do driver. Fixture KUnit nao mantem mais
copia da tabela de bus nem redefine os offsets/politicas do descriptor.
Patch mt6765-connsys-descriptor-v1.patch SHA
c0da5da0b79c8ddc1543cf2839c358c88fd7d8b8756414e5edcf095415d8d9ae;
schema derivado SHAa269f7a8f65c4ba4adf20231fc05c2d0b56611147324c374c5622b440fd5649e.
ARM32 objeto SHA66332bbde2a218dd42c3352734282d374a7ef40ac06f0bcdafdf69920988bfa9,
work/connsys-descriptor-arm32-build-20261027-b.log. O objeto contem dados6765 e
match novo; nao altera compatible legado mt6765-scpsys nem habilita DT de boot.

KUnit61/61 passou,17 CONNSYS, workspace kunit-connsys-descriptor-20261027-v2,
runs/first/verified.json; kernel UML SHA
d6d007042b5ef36ccaa3e03924edf70d50e1884cf454acd99886237c4285fb7f,
log SHA0a5c27c0a590b53bd5ae30470ded4c31e79ffc026c75294bdb3963c87bd1cccf.
Inclui callbacks reais com tabela de producao e getter recusando phandle
ausente antes de I/O; nao e execucao de probe OF completo. Sem WARN de MMIO
no log final. Oito testes host do runner passaram (descriptor-host-b).
Primeira versao de dados tambem passou60/60, antes da protecao adicional do
fallback, preservada em kunit-connsys-descriptor-20261027-v1.

DTC1.7.0 e dt-schema2026.9 usados diretamente no fixture
kernel/tests/devicetree/mt6765-connsys-schema.dts (nao arvore de boot).
dt-doc-validate, dt-mk-schema, DTC e dt-validate positivos sem diagnosticos;
JSON positivo/legado vazio, sem controlador recusado por required e dois
recusados por maxItems. Fixture MT8183 com dois controladores segue aceito.
Evidencias em artifacts/staging-mt6765-connsys-descriptor-20261027-v1/schema-*.json
e work/connsys-descriptor-schema-*.log. Primeiro dt-doc-validate avisou caminho
incompativel com $id; executado novamente no caminho canonico
Documentation/devicetree/bindings/power, log schema-doc-b vazio. Nao ignorar
diagnosticos mesmo quando o utilitario retorna0. Schema SPDX dual preservado.

Nenhum novo kernel/imagem foi carregado, nem profile de boot/recuperacao alterado.
lts-auto-cycle.py SHA85bc5649e428ac6e63a0a17531ee66a65e79ba95821b4d2e7cbec7c8ca888f1d
preservado. Proximo bloqueio: integrar provider no DT de laboratorio, verificar
handoff real OFF e conectar o consumidor WMT por runtimePM/genpd, nao clock conn
ficticio. Isso ainda nao e Wi-Fi funcionando nem suporte eletrico comprovado.

Integracao de dados MT6765 (2026-10-27, antes da implementacao): entrega futura
no aparelho e registrar somente CONN, inicialmente OFF, no genpd upstream.
Aceite imediato: build ARM32, mesmos testes usando o descriptor instalado no
driver (nao copia no fixture), schema upstream estendido e DT compilavel sem
habilitar provider/consumidor na imagem atual. Nenhuma operacao fisica nesta etapa.

Revisao do caminho de DT invalido: o probe upstream permite fallback legado se
access-controllers nao existir. Esse fallback pode montar zero regmaps enquanto
CONN precisa de INFRA. Nao depender apenas de dt-schema para evitar isso em
runtime: acrescentar require_access_controllers nos dados SoC, default false
para preservar os antigos, true em MT6765. O probe entao usa o getter upstream
que recusa contagem ausente/errada antes de acessar mapas. Pequena extensao ao
mesmo framework GPL-2.0-only, nao implementacao paralela nem fallback ficticio.

| Funcao | Implementacao atual | Reuso / revisao / licenca | Compatibilidade, probe/erro/remove | Esforco | Recomendacao |
| --- | --- | --- | --- | --- | --- |
| Dados do dominio CONN MT6765 | Somente fixture local; LG clk-mt6765-pg.c GPLv2 SHA3702686b documenta ctl32c, ACK180/184 BIT1 e tres passos de bus | LTS2926d88 mtk-pm-domains e modelo mt6735-pm-domains.h GPL-2.0-only; binding existente mt6765-power.h SPDX GPL-2.0 SHA60d509be3ac41335c370d6c80d5c64c6ea0feedc5a0a88a3c63f43bc60dd536c, CONN0. Schema mediatek,power-controller.yaml GPL-2.0-only OR BSD-2-Clause SHA935497f9a52e928187aabaf07581c6b11a58557bc7b9a8ecc5dabb25fa53c352 | Mainline d135ab45 e pmaports/Qualcomm ja triados nao fornecem descriptor equivalente comprovado. Nao reutilizar SPM_CONN_PWR_CON generico280 (aqui32c), nem power-status60c (aqui180). Somente CONN, sem SRAM/RTFF/clocks ficticios. Um access-controller INFRA real. Probe usa politica estrita OFF; driver ja suppress_bind_attrs e callbacks/cleanup auditados acima | Pequeno, dados e match; medio para DT/consumidor real | Acrescentar header de dados SoC e compatible correto ao driver existente, sem novo driver. Reusar ID upstream e schema; requer access-controllers com um phandle. Nao habilitar outros dominios/DT/WMT nem inferir funcionamento fisico dos dados |

Etapa ON/rollback/handoff (antes da implementacao, 2026-10-27): a entrega futura
no aparelho e ligar/desligar CONN sem inicializar WMT ainda. Bloqueio atual: o
callback upstream ignora escritas ON e desliga clocks/supply mesmo se o dominio
ficou parcialmente ligado; KEEP_DEFAULT_OFF apenas avisa quando herdado ON e
declara o genpd OFF. Aceite desta etapa ainda offline: callbacks reais com RAM
regmap, sucesso ON/OFF, falha ON restaura OFF confirmado ou trava novas operacoes
ate recuperacao; probe estrito rejeita ON/misto/erro sem energizar.

Validacao de recursos: reutilizar clk_hw_register_gate sobre uma palavra RAM e
clk_hw_get_clk_kunit, nao criar ops CCF paralelas nem fakear clk_bulk_*.
LTS2926d88 drivers/clk/clk-gate.c SPDX GPL-2.0 SHA
c08b69d9ec300b05de9955f8e9662e594721eb7a31900077cd5af3b55f323338;
clk_kunit_helpers.c SPDX GPL-2.0 SHA
9a8e1022bd04a0e32be5be6892d22e1271803f5c11106c61cdf6ecf60960be34.
COMMON_CLK precisa estar y no UML, verificado antes de executar. Gate RAM permite
observar CCF ligado apos rollback incerto e desligado apos OFF confirmado.
Supply e clocks fisicos da placa ainda nao sao comprovados por esse teste host.

Correcao do fixture apos execucao: UML usa INDIRECT_IOMEM e recusou cast RAM
para MMIO do clk-gate; v3 registrou WARN e falhou2/60 casos, sem aprovacao.
Nao desligar INDIRECT_IOMEM nem adicionar emulador para esse teste. Reusar
clk_hw_register_fixed_rate (GPL-2.0, mesmo LTS, SHA
dbccbf5193cdef69443864d745fd7d026341d6bc66c2491012bef2fd3ec837c4),
clk_hw_get_clk_kunit, __clk_get_enable_count e clk_hw_is_prepared. Assim o
CCF real mostra referencias retidas/liberadas sem MMIO, ops de clock proprias
ou novos providers de hardware. Nao comprova gating eletrico nem supply real.

Alternativa upstream mais antiga tambem inspecionada: mtk-scpsys.c LTS2926d88,
GPL-2.0-only SHAfb590c27a3bfbf1ef5317edc42008bfb156e375700c877ec2734288dfaf7ecfe.
Seu bus_prot_mask e um passo unico, nao expressa os tres passos/dois bancos/ACK
baixo de CONN; cleanup ON tambem libera clocks sem confirmar OFF. Nao oferece
substituicao pronta que elimine a extensao pequena do driver baseado em regmap.
Handoff estrito verifica tambem requestsON0, RST_B0, ISO1 e CLK_DIS1: ACK OFF com
pedido ON pendente nao sera aceito como estado seguro.

Resultado lifecycle final: ARM32 compilou em
work/connsys-lifecycle-arm32-build-20261027-b.log, objeto SHA
47ad861f443ad44dd4f6907bbccab88280ded8029546c378932d8d87100b23c7.
Patch mtk-pmdomain-strict-lifecycle-v1.patch SHA
0e907e2d93e9e555d0bcac83ffc7bb89884c2048926c41b91c614d07dfba9b4f.
KUnit/UML passou60/60 (16 CONNSYS) em
kunit-connsys-lifecycle-20261027-v4/runs/first/verified.json;
kernel SHAa2dd3b9fa1abe9b69cff27604faa8b93a4e13256f61421d6164dfcbc284cf0ae,
config SHAe673fcc12bdcc77ccb5b9012c027705bac127bb89d9d3a343552bc6f3a469895,
log SHA2402c0e1899d7ae1dfed4e66705b1527b753bc7857c21721cc023fdb8c2e58e0.
CCF COMMON_CLK=y verificado antes da execucao, drivers normais SCPSYS recusados.
Sem WARN de MMIO ou clock preparado no log final. Os oito testes host passaram
(work/connsys-lifecycle-host-20261027-d.log), incluindo recusa de COMMON_CLK ausente.

Aceite demonstrado: callbacks ON/OFF com controle regmap real; falha antes do
primeiro pedido ON e na liberacao do bus restauram OFF e permitem nova chamada
explicita; ACK OFF preso retorna a falha original, mantem referencias CCF de
clocks principal/subsistema e bloqueia ON/OFF posteriores antes de I/O. Nao ha
retry automatico de ON. O teste de handoff exercita helper usado por probe, nao
probe OF inteiro. Protecao contra estado desconhecido nao equivale a suporte
fisico do dominio, dos reguladores ou de Wi-Fi. Politica continua opt-in, sem
descriptor6765, match, DT, autoload ou alteracao do kernel no aparelho.

Falhas preservadas: v1 nao compilou por atribuicao de struct com membro const
no fixture; usar inicializacao C valida, sem retirar const do driver. v2 recusou
ciclo Kconfig envolvendo select COMMON_CLK; agora e dependencia explicita, com
config e verificador exigindo y, sem relaxar isolamento. v3 falhou nos dois
fixtures MMIO citados acima. Nao foram aprovadas nem repetidas sem correcao.
Driver embutido ja tem suppress_bind_attrs=true; nenhum remove/unbind novo.
Recuperacao lts-auto-cycle.py mantem SHA85bc5649e428ac6e63a0a17531ee66a65e79ba95821b4d2e7cbec7c8ca888f1d.

Proxima integracao: dados CONN do MT6765, usando binding de power-domain ja
existente e descricao LG dos offsets/mascaras, sem duplicar os callbacks.
Somente depois integrar DT/provider e consumidor WMT real; nao carregar este
staging como se ja tivesse Wi-Fi ou validacao eletrica no aparelho.

| Funcao | Implementacao atual | Reuso / revisao / licenca | Compatibilidade e efeitos de erro/probe/remove | Esforco | Recomendacao |
| --- | --- | --- | --- | --- | --- |
| Ligacao CONN e falha parcial | LG clk-mt6765-pg.c GPLv2 SHA3702686b: ON primario/secundario, ambos ACK, CLK_DIS0/ISO0/RST_B1; sem rollback limitado. LTS2926d88 e mainline d135ab45 mantem cleanup sem confirmar OFF | Estender mtk-pm-domains.c/.h GPL-2.0-only usando regmap, CCF, regulator e genpd ja existentes; helpers de bus e OFF recem-testados. postmarketOS/Qualcomm nao demonstram substituto compativel para SPM6765 | Politica estrita opt-in por dominio, somente sem RTFF/SRAM/modem/buck externo nesta etapa; validar configuracao, ACK herdado OFF, proteger bus antes de ON. Em falha, reafirmar bus, isolar e desligar na ordem da placa, confirmar ambos ACK OFF antes de liberar recursos. Se cleanup falhar, reter recursos e bloquear novas chamadas ate reset, sem retry automatico. Probe estrito nao liga dominio e nao aceita estado desconhecido. Sem of-match/DT/provider, remove fisico ainda fora do aceite | Pequeno/medio focado em CONN | Reusar fluxo existente, sem driver paralelo nem clocks/reguladores falsos. Propagar cinco escritas ON comuns. Defaults de outros SoCs preservados para politica/cleanup; erros ON deixam de ser silenciosos. Testar falha antes da primeira escrita ON, depois de ON e no rollback; nenhuma carga fisica autorizada por estes testes |

Atualizacao 2026-10-27: bus/status final (ACK_LOW em bit5) passou os53 casos
UML, workspace kunit-connsys-status-20261027-v2, runs/first/verified.json.
Kernel UML SHA5a9bbea36523de63df8be62f8a8f20fe6f31880fd2ae0d1dcfe369def81d4fea;
patch bus SHAbe5b1f6b242e156b3a935f37fd79c6dada50950ad707c9e9bc09be4e49238742.
Mainline comparado d135ab453a7400a34930bdda1ef4bdc8acfac80e: bit4 ja e
BUS_PROT_IGNORE_SUBCLK; bit5 evita colisao. O patch continua especifico ao
LTS2926d88, nao cherry-pick cego para structs mais novas. Primeira configuracao
UML recusou PM_GENERIC_DOMAINS ausente; Kconfig agora seleciona a dependencia,
como o driver oficial. Fixtures host foram corrigidas por nome, sem relaxar gates.

Entrega seguinte: expressar a ordem LG de remocao de PWR_ON antes de PWR_ON_2ND
nos dados do dominio upstream. Aceite offline: trace no regmap real com RAM,
default secundario/primario inalterado, erro de escrita interrompe a sequencia.
Isso desbloqueia parte da futura alimentacao CONN; nao e Wi-Fi funcionando.

| Funcao | Atual | Alternativa / origem / revisao / licenca | Compatibilidade e efeitos | Esforco | Decisao |
| --- | --- | --- | --- | --- | --- |
| Ordem dos bits OFF CONN | LG clk-mt6765-pg.c, SHA3702686bf804d606ba83355e4a48e7a7cafabd45114550acdcf78ab1d406c5b4, GPLv2, primario depois secundario | mtk-pm-domains.c/.h LTS2926d88 GPL-2.0-only; extensao pequena de dados, regmap existente; mainline d135ab45 ainda secundario depois primario | Sem RTFF em CONN; nao copiar polls infinitos LG. Qualcomm/pmaports nao comprovam uma sequencia substituta para este SPM. Probe/remove/provider nao alterados; nao carregar. Erros do trecho OFF comum precisam chegar ao callback antes de declarar OFF ou desligar recursos restantes | Pequeno | Booleano opcional por dominio, default antigo; retornar erros no trecho comum e respeita-los no callback. RTFF, caminho modem e rollback/handoff continuam fora do aceite desta etapa; nenhuma escrita no telefone |

Resultado da ordemOFF: ARM32 compilou, objeto SHA
a15ade4501e410619ded6573aff9181e4d565a57066e0cafc1d4e2d9be75296d,
log work/connsys-off-arm32-build-20261027-a.log. Patch
mtk-pmdomain-primary-off-order-v1.patch SHA
9aee100d9dda32acf7b05306c05d8e34e283ec2ebd082b363d9abc7793e69b3a.
KUnit executou55/55 casos, workspace kunit-connsys-off-20261027-v2,
runs/first/verified.json, kernel UML SHA
a3dac1856d1b87481dc7243984eebebe2b282357217bfd0417dbd60e9b815e96,
log SHA3954284a798915a3d090ac2e6dec85d9c7a8568c08050e3252468f3cb4e88a69.
Novos casos exercitam ordem LG/default, preservacao de bits alheios e erro em
cada uma das cinco leituras/escritas do trecho OFF comum. Callback agora retorna
erro desse trecho antes de esperar ACK/desligar clocks principais e supply.
Nao significa rollback de estado parcial; RTFF e modem continuam nao auditados
para este aceite, e CONN nao usa RTFF. Sem novo match/provider/DT nem telefone.
Primeira preparacao falhou por ordem de patches (OFF antes de status); evidencia
preservada em work/kunit-connsys-off-prepare-20261027-a.log. Ordem corrigida para
bus -> status -> OFF; nova preparacao limpa aplicou sem fuzz e passou. Os oito
testes host do runner passaram; mecanismo lts-auto-cycle.py permanece SHA
85bc5649e428ac6e63a0a17531ee66a65e79ba95821b4d2e7cbec7c8ca888f1d.

Proximo bloqueio real: ligar CONN com erros propagados e tratamento de estado
parcial, depois handoff/probe sem energizacao automatica. Os patches presentes
ainda nao autorizam ativar o dominio, WMT ou Wi-Fi no6.18.

Extensao de status antes de energizar: driver2926d88 usa boolis_on e espera
!is_on no desligamento, aprovando estado misto (umACK aindaON). Leituras regmap
tambem nao tem erro propagado nessa funcao. Reusar regmap/readx_poll_timeout e
framework existente: estadoON exige todos bits nos doisACKs, OFF exige ambos0,
misto e estado interno positivo2 ate limite; erro de I/O sai como erro, nunca estado.
Nao usar errnoEAGAIN para misto: EAGAIN real do regmap nao pode virar retry. Defaults
validosON/OFF preservados; falhas deixam de ser silenciosas. Testar matriz,
erros no primeiro/segundo read e timeoutOFF misto com regmapRAM. Sem novo driver,
acesso cru, mudanca de offset ou poll ampliado. Ainda nao autoriza provider/DT.

| Funcao | Atual | Reuso / licenca / versao | Compatibilidade e limites | Esforco | Decisao |
| --- | --- | --- | --- | --- | --- |
| Protecao do bus CONN | LG clk-mt6765-pg.c GPLv2: assert A(bit13),B(grupo1 bit18),C(bits14/16); release C,A,B; B esperaACK0 no assert | mtk-pm-domains.c/.h LTS2926d88 GPL-2.0-only, regmap/genpd/polls existentes; MediaTek LG e candidato acima. Qualcomm/pmaports nao provam essa sequencia | BUS_PROT_INVERTED troca escritaSET porCLR: NAO equivale a ACK baixo. Release upstream e reverse array, diferente de LG. Getter CLOCKconn LG liga MTCMOS, nao e clock fixo | Pequeno para expressar sequencia; medio para domain completo | Acrescentar flagACK baixo apenas no pollSET e ordemCLR opcional validada antes de I/O. Defaults antigos preservados. Propagar falhas de escrita antes de poll/ignoreACK. KUnit usa helpers reais com regmapRAM e trace de enderecos/mascaras; nenhum C paralelo de controle |

Bloqueios ainda anteriores a qualquer providerMT6765/DT/carga: duas confirmações
de status devem estar ambasOFF, erros de regmap nao podem significarON/OFF,
ordem de desligamento primario/secundario LG difere do default, handoff/probe
nao pode ligar dominios por conveniencia. Fonte LG tem polls sem timeout e
sequencias/erros que nao devem ser copiados cegamente. Esta etapa nao implementa
power_on/off de MT6765, nao altera RTC/SPM/PMIC do aparelho e nao remove gates.

Resultado offline: OSAL e ring agora compilam ARM32 contra6.18.58, com -Werror
preservado. Patches pequenos: wmt-aee-optional-v1, wmt-osal-linux618-api-v1 e
wmt-ring-private-helper-v1. No6.18 o macro e timer_container_of, nao from_timer
do doador mais antigo. Nao mudar atraso/arredondamento, ABI do callback ou o
tratamento de retornos dos consumidores nesta etapa. Wakeup source sem memoria
retornaENOMEM antes de marcar init, falha que deve ser propagada pelos chamadores
antes de qualquer carga futura. Nao foi executado teste de lifecycle WMT no
telefone nem aprovado o modulo completo.

Log `work/wmt-lts-osal-linux618-api-20261027-a.log`: objetoOSAL SHA
b292032a3b79a84fcf11ab6e443bfbb073592c2f66f0cf96370e80a5bb7550c1;
fonte staged SHA228073717db2ed2eafb3f9f7d12c56259e51cc38c15a60003e3e2af4da20a6d1.
Ring recompilado em `work/wmt-lts-ring-private-helper-20261027-a.log`.
Link relocatable dos dois objetos concluiu, sem substituir simbolos externos.
nm ainda exige connectivity_export_dump_thread_state/show_stack e demais
dependencias reais; nenhum stub/no-op foi criado. Fonte hardware mt6765.c
permanece identica ao LG por SHA0c55b27dbe1f6174a23933d629bd13665e2a1d264e0b512ff14eac13cc215ecc.
Proximo bloqueio do modulo completo: separar caminho CONNSYS AXI do detector
de chip externo e ligar RTC32k/clocks/reguladores/DMA por APIs reais do6.18,
preservando init/falha/exit. Nao carregar apenas porque um objeto compilou.

Ring buffer vendor permanece reutilizado, sem implementar outro buffer:
ring.c GPLv2 tem helper __ring_segment_prepare referenciado apenas no proprioC.
Build6.18 reclama missing-prototypes; marcar somente esse helper static preserva
algoritmo, chamadas e APIs publicas, sem suprimir warnings. Validacao atual e
compilacao.o; concorrencia/uso final ainda dependem do WMT completo.

Primeiro build isolado recusou mtk_rtc.h e mtk_wcn_cmb_stub.h, interfaces vendor
ausentes, log `work/wmt-lts-baseline-build-20261027-a.log`. Nao copiar headers
internos4.9 indiscriminadamente: mtk_rtc.h tem macros vazias quando CONFIG_MTK_RTC
nao existe, o que esconderia o controle fisico32k. Build separado do objetoOSAL
identificou dependencia AEE antes de qualquer MMIO, log
`work/wmt-lts-osal-baseline-20261027-a.log`.

Depois do guardAEE, somente o objetoOSAL consulta a declaracao publica original
connectivity_build_in_adapter.h (GPLv2, SHAd1358cd8ff8f6f6f8e1895e79608da8d604abf9577c38eadd0fb7867569fbebb).
Esse diretorio nao contem headersLinux, nao copia autoconf4.9 nem implementa
as funcoes declaradas. Os dois consumidores OSAL sao dump_thread_state e
show_stack; simbolos continuam obrigatorios no link/modpost. Nao promover esse
include especifico a outros objetos, nem interpretar compilacao.o como modulo
funcional. O modulo completo continua bloqueado por RTC32k/vendor adapters.

| Funcao | Atual | Alternativa / revisao / licenca | Compatibilidade / risco | Esforco | Decisao |
| --- | --- | --- | --- | --- | --- |
| Reporter Android AEE opcional | osal_typedef inclui aee.h e assert chama reporter sempre em ALPS | Motorola common e6cfe39, osal.c/typedef.h GPLv2, IS_ENABLED(CONFIG_MTK_AEE_AED) ja usado pelo doador | Apenas reporter complementar; preservar osal_err_print, retorno e assert, nao desligar ALPS globalmente nem criar no-op para RTC/clocks. Sem hardware/probe/remove afetados | Minimo | Reusar guard de configuracao nas duas referencias AEE, preservando logs e comportamento do ramo habilitado. Fonte hardware LG continua intocada; compilar objeto para localizar proximo bloqueio |
| OSAL: timers, wakeup, wall time e FIFO privados | APIs init_timer/data/del_timer, wakeup_source_register1arg, timeval removidas | LTS2926d88 timer_setup/from_timer/timer_delete(_sync), wakeup_source_register(NULL,name), ktime_get_real_ts64; Motorolae6cfe39 usa timer_setup, wakeup2args e timespec64; GPLv2/GPL-2.0-only | Callback ponte preserva handler(unsigned long) e dado, sem trocar ABI dos consumidores. Time mantem segundos32/useg e retorno, nao monotonic. FIFO _osal_* tem referencias somente no mesmoC: linkage static, sem suprimir warnings. Wakeup falha deve retornarENOMEM sem init_flag | Pequeno offline; medio para verificar consumidores/lifetime | Adaptar apenas OSAL em staging, nao hardware; mesmo arredondamento/delay e sync dos timers, callbacks/contexto preservados. Compilacao.o nao aprova lifecycle ou modulo inteiro. Sem reset/clocks/PMIC, sem no-op para dependencia ausente |

| Funcao | Atual | Alternativa / origem / revisao / licenca | Compatibilidade e efeitos | Esforco | Decisao |
| --- | --- | --- | --- | --- | --- |
| WMT/CONNSYS MT6765 | LG4.9 funcional; common+adaptor+gen4m AXI, launcher/firmware privados | LG snapshot local sem commit; mt6765.c GPLv2 SHA0c55b27dbe1f6174a23933d629bd13665e2a1d264e0b512ff14eac13cc215ecc; osal.c GPLv2 SHA5a51d57b09d97503a85b4910ce1f916b6a6d1c0fe7139e44a8f179017c366c5a. Mainline2926d88 cfg80211/mac80211/mt76; pmaports e Qualcomm nao fornecem equivalencia desse WMT integrado | Module WMT controla clocks/resets/EMI/PMIC e nos char; nao carregar antes de auditar init/falha/exit. mt76 nao e substituicao comprovada de HIF AXI6765. cfg80211/mac80211 ja estao m na config atual | Alto, identificar primeiro erro real | Copia isolada do common, configurar somente selecao6765 com autoconf atual, compilar sem headers4.9, sem stubs nem supressao de erros. Preservar fonte/modulos4.9 validados |
| Referencia WMT mais recente | Sem integracao6.18 | Motorola oficial common commit e6cfe39b53a6057ef0423ef5835501cc6c66d65c, gen4m1e0e34805117168dd3265835ebb58d16a69a73e8, android16 w1ve; cabecalhos/licencas ainda a verificar por arquivo antes de copiar | Tree common consultada nao contem mt6765.c; ref Android12 MMI-S3SG32.39-191R2 documenta AXI/CONNAC6765. Nome gen4m/versaoAndroid nao prova protocolo, ABI firmware nem suporte6765 | Medio para selecionar doador | Candidatas, nao atualizar checkouts existentes nem trocar bloco hardware LG. Reusar apenas adaptacoes Linux comprovadamente equivalentes apos comparar fontes/licencas |

Fontes primarias: [Motorola common](https://github.com/MotorolaMobilityLLC/vendor-mediatek-kernel_modules-connectivity-common),
[Motorola gen4m](https://github.com/MotorolaMobilityLLC/vendor-mediatek-kernel_modules-connectivity-wlan-core-gen4m),
[build oficial MT6765](https://github.com/MotorolaMobilityLLC/readme/blob/master/MMI-S3SG32.39-191R2).
Refs fixadas por git ls-remote, logs work/motorola-*-refs-20261027.txt.
Wrapper de build temporario apenas fixa variaveis Makefile, MIT; nao e novo
framework/transporte nem permite carregar o resultado. Nenhum novo firmware,
servico Android, modulo4.9 ou arquivo privado sera incluido no Git.

Levantamento de fontes, binários e volume potencial de engenharia reversa do
K40S (2026-10-27): [mapa de hardware e lacunas de fonte](hardware-source-and-re-audit-20261027.md).
Pesquisa offline; não autoriza integração ou carga de drivers/firmware.

Controle de carga: [auditoria MT6371 de probe, escritas, limites LG e remove](mt6371-charger-bringup.md).
Driver continua fora dos payloads; corrigir mutex antes da PS e uma etapa
offline,nao aprovacao das escritas ou de toda inicializacao/teardown.

## Coexistência da composição nativa já validada (2026-10-26)

### Integracao de entrada/backlight no boot PM nativo — 2026-10-27

Entrega: dispositivos FT5446, keypad, PMIC-keys e backlight registrados sem
insmod manual no boot6.18 atual. Reusar exatamente os cinco drivers/patches,
revisao2926d88 e licencas da tabela abaixo; nao reimplementar entrada/painel.
Mainline/MediaTek/pmaports ja auditados; Qualcomm nao substitui estes chips.
Comparar build contra o kernel PM atual e hashes do recibo de coexistencia.
OpenRC0.63.2 commitb3a99e01c8bda7e5c2b9a8975a6d36ec3eff370e/BSD-2-Clause
ja fornece ciclo de servico; modules.in nao fornece gates hash/RO/identidade
do laboratorio. Wrapper MIT pequeno de placa, opt-in, separado de bateria
e RTC; deixa MFD compartilhado existente e drivers ate reset validado.
Sem driver C novo, charger, OVL, gesto sintetico, brilho ou politica PM novos.
Probe/reset/debounce/DTdefault e remove sao os auditados abaixo, nao passivos.
Aceite: hash/gates antes de carga, dispositivos presentes/valores DT preservados,
V/I/T/RTC/WDT/USB intactos; nao alegar gesto humano nem PM sem novo ensaio.
Falha de bind nao autoriza reload/retry; encerrar pelo ciclo de recuperacao.
Esforco pequeno, integracao de componentes existentes, nao framework novo.

Build contra PM/WDT atual concluiu sem erros de modpost. Quatro .ko iguais
ao recibo de coexistencia; edt3e3f8c4a difere de9bcebc53 apenas no caminho
ucopysize.h da string de aviso (disassembly de todas secoes executaveis igual).
Fontes identicas. Servico iniciou em RAM:FT5446 LG/fw20,3 inputs,backlight679/679,
V/I/T presentes,header/crc0. Primeira chamada host usou basenamekbox invalido
para timeout e parou ANTES de insmod; corrigida para BusyBox multicall existente,
sem repetir carga de driver. Logs native-input-service-live-20261027-a/b.log.
Quinze testes de servico direcionados passaram,nao suite completa.

Antes de ensaiar PM com os inputs: touch nao anuncia wakeup na DT atual.
Callback upstream existente envia hibernate,desabilita IRQ,assert reset164 e
regulator_disable(vcc);iovcc opcional ausente nao e acessado. Resume reaplica
mesma alimentacao/reset,espera300ms e restaura parametros. Nao mudar tensao
ou sequencia,nao adicionar controle userspace. PMICkeys so habilita/desabilita
wake de press/release se wakeup-source;keypad/backlight nao adicionam callback
de sistema nesta revisao. Primeiro pm_test=devices limitado5s,RTCsemalarme,
WDT15/coletorativo;examinar falhas e identidade/errorcounters aposretorno.
Se falhar,nao recarregar nem insistir:sair pelo ciclo existente. S2idle real
com esses drivers ainda NAO validado por testes anteriores sem inputs.

PMdevices493,197->498,654s voltou no mesmo boot;USB/SSH caiu durante
callback mas retornou,trap restaurou pm_testnone. Touchmodelo/fw20,
header/crc0,backlight679 e V/I/T responderam. Log
`work/native-input-pm-devices-followup-20261027-a.log`. Um voltage_now
rejeitado com-110 aposretomada,consultas posteriores validas;nao e prova de
disponibilidade continua sem erro. Tentativa de executar o script s2idle
nesse mesmo boot foi RECUSADA antes de I/O pela marca host-ack do ensaio RTC
anterior;nao apagar marca nem relaxar gate para repetir. Nenhum novo s2idle
com inputs ocorreu nesse boot. Novo coldboot tera seu proprio ensaio unico.
Imagem candidata0c20c76063cb67b99bc7ab600df0d88af4e3077128d8835d692d96df6b4c3d1f,
ramdisk06773090a20f7dabc38126a3e41d92f7314a5afa16e222506c422efa0eeb0e5c;
kernel/DTB/cmdline inalterados,extracao/overlay passaram.

Recuperacao83335 concluidaexit0:4.9.190/boot_a5ffea913 conferidos pelo ciclo,
captura dram-20261027-115731,A/Bbefore/after9f3448025c92cbb4e1feb4f020b7fea5deb50222962832b8fe408d753f92a117.
Nenhuma alteracao ao mecanismo de recuperacao. Novo coletor80031 iniciado
somente depois desse termino para a imagem de startup input acima.

Aceite fisico coldboot80031:sem insmod manual,OpenRC iniciou bateria5,939s,
RTC6,470s,input/backlight7,065s;os tres servicos continuam started apos PID1.
FT5446 LG/fw20,3inputs,header/crc0,brilho679/679,V4392608uV,I8100uA,T34,9C.
WDTactive/rootfsRO1. Log `work/native-input-startup-acceptance-20261027-a.log`,
SHA256f7209c1fa36178f6e6a73952f41a98f3607ec073d878c0b9baf2e23f09ddbd80.

Ensaio UNICO s2idle nesse coldboot,script inalterado:entrada28,967s,
saida33,330s;RTC1910->1,parent174,alarme desarmado. USB/SSH retornaram,
ACK/returned presentes. Log `work/native-input-startup-s2idle-20261027-b.log`,
SHA256035b98403ad59969e52bbb727fc03ec8cbb9f716350f44b3c4362b532ae37c0d.
Primeira observacao host expirou durante reenumeracao,segunda leu mesma
execucao. Aposretorno modelo/fw20,header/crc0,brilho679/679,3inputs e servicos
presentes,V4392773uV,I2500uA,T34,8C. Alarmevazio,pm_testnone,debug0,
UDCconfigured,WDTactive,rootfsRO1. Log
`work/native-input-startup-final-20261027-a.log`,SHA256
6049e48976862ced68ef261e7279b0bd8e6ecb663475a19bd42c20758a7612c9.
Frames559970384/606223231ns rejeitados comETIME/latch0,consumer registrou
um read-channel-error correspondente;nao publicar framesatrasados nem
alegar ausencia de erros transitorios. Nenhuma falha PM touch encontrada.
Avisos preexistentes MFD/DMAmask e nos sound/ADC/charger/flash/TCPC ausentes
continuam visiveis. Sem novo gesto/botao humano,consumo,deep,teste prolongado
ou controle de carga. Kernelnovo permaneceativo,sessao80031 com coletor;
recuperacao desta ultima sessao ainda pendente. Logs em
`work/native-input-startup-session-20261027-a.log`.

Sem novo driver, módulo C ou ferramenta. Antes de combinar os binários já
testados individualmente e o V/I/T que passou no fluxo host-once. Usar a
imagem residente existente468c04db… com DT2a98667d…; kernel88b5438b… inalterado.

| Função | Implementação existente / origem / licença | Compatibilidade e efeitos já conhecidos | Decisão / limite |
| --- | --- | --- | --- |
| Touch | edt-ft5x06 do Linux6.18.58 commit2926d88bb7fc4608fd942453d929c39e4e5ec006 + três patches LG auditados; GPL-2.0; módulo9bcebc53… | DT VCL27/reset164/IRQ1, alimentação explícita sem inventar IOVCC. Probe alimenta/reseta e lê ID; remove tem a sequência já auditada. Captura anterior do dono comprovou eventos reais | Mesmo binário, não recompilar/adaptar de novo. Confirmar bind e modelo nesta composição; sem alegar novo teste de gestos |
| Teclas | mt6779-keypad upstream SPDX GPL-2.0, módulo68b01726…; mtk-pmic-keys SPDX GPL-2.0-only + patch MT6357 v2, módulo4eb0f58d… | Keypad usa CCF/KPD; PMIC usa MFD/regmap/IRQ e máscaras MT6331/IRQs de soltura comprovadas. Probe pode escrever debounce/reset-long-press; não são drivers passivos. Valores DT já testados, sem mudar TOP_RST_MISC por nova política | Reusar módulos/DT exatos. Confirmar dispositivos/IRQs, não simular botão nem inferir evento físico sem o dono |
| Backlight | mt6370 MFD + mt6370-backlight upstream SPDX GPL-2.0-only, módulos282fee16…/a1346b4e…, mesma revisão | I2C5/MT6371F4, canais15, teto679 preservando proteções LK. Probe altera bits/controla brilho conforme DT existente; charger/regulator/TCPC/flash não têm drivers. Avisos DMA mask das células são conhecidos, não ocultar | Carregar só MFD/backlight. Não mexer em brilho/OVP/OCP/PWM nem remover estes drivers no ensaio; ficam até reset/recuperação já demonstrados |
| Bateria | Continuous nativo GPL-2.0-only, módulo b68c5544… de6e68bcc | Mesmas sete escritas ADC/FG por aquisição, sem charger/reset/calibração; exclusividade: nenhum outro MT6357 IIO/bateria. V/I/T não é SOC/controle térmico |18 leituras com demais drivers ligados, depois remover somente o módulo de bateria; preservar estado no primeiro erro, sem retries |
| Tela | simple-framebuffer/fbcon builtin GPL-2.0, mesmo kernel e DT | Leitura do framebuffer reservado pelo LK, sem novo painel/DRM. A correção alfa OVL é um módulo separado com MMIO e não é necessária para este ensaio de coexistência | Somente verificar registro/geometria; não carregar OVL nem prometer nova confirmação visual ou port DSI completo |

As alternativas mainline/pmaports/MediaTek/Qualcomm e os efeitos de cada
driver já estão nas auditorias de touch, teclas, I2C5/backlight e bateria
abaixo. A tarefa nova é coexistência, não outra implementação. Nenhuma
licença/compatibilidade é transferida por analogia a Qualcomm. Dependências
dos cinco módulos upstream estão vazias no modinfo da build fixada; conferir
vermagic/hash antes do envio e manter recuperação automática. Caso bind falhe,
não repetir carga; encerrar a sessão e examinar os registros.

## Bateria nativa: integração no fluxo host-once existente (2026-10-26)

Antes da extensão dos preparadores/verificadores. A captura nativa já foi
observada no manifesto mt6357-native-continuous-20261026.json; não adicionar
outro driver, serviço residente, transporte ou rotina PMIC.

| Função | Atual | Alternativa / revisão / licença | Compatibilidade e efeitos | Recomendação |
| --- | --- | --- | --- | --- |
| Seleção e pacote nativo | Builder --continuous --native validado; hook/preparador limitados a atomic | get_variant, prepare-k40s-rootfs-test, battery-continuous e advance-k40s-lts existentes em6e68bcc; ferramentas MIT e módulo GPL-2.0-only; kernel Linux6.18.58 commit2926d88bb7fc4608fd942453d929c39e4e5ec006 | Selecionar o artefato nativo por variante fechada; conferir fontes/módulo/kernel. Mesmo hook18 rodadas, mesma aquisição/remoção. Token do módulo segue par exato por release | Estender os caminhos existentes, não adicionar novo builder ou módulo |
| Autorização física | host-once com nonce, ledger durável, sem retransmissão; originalmente atomic | k40s_host_once e host-once-gate MIT existentes, OpenSSH já fixado no payload | Exceção nativa somente para continuous exclusivo. Demais probes, resident, variantes desconhecidas e combinações seguem bloqueados. Nenhuma escrita antes do permit verificado | Reusar protocolo integralmente; não alterar ledger, gate, DA ou ciclo |
| Verificação de release/clocks | Wrapper tem RELEASE antigo e exige markers de placeholder MSDC que não existem no nativo | APIs do ciclo e evidências ARMPLL/SMP existentes no kernel fixado | Passar o release da variante cujo kernel foi identificado por SHA. Atomic mantém verificação anterior. Native deve exigir ARMPLL prepared/native_ops e8CPUs, ausência de placeholder MSDC/falhas, além de eMMC/rootfs/SSH/permit/A-B | Extensão explícita de assess; não descartar clock check nem aceitar só a presença do USB. Não afirmar medição de frequência |
| Frameworks e alternativas | Orquestração já separada do módulo e dos transportes | KUnit/kselftest para lógica kernel/interfaces; OpenRC para futuro runtime; Linux/pmaports e MediaTek/Qualcomm auditados nas seções anteriores | Aqui só há alteração de montagem/verificação host. Nenhum framework upstream executa a política específica do laboratório, mas todos os componentes de transporte/driver já existem. Qualcomm não herda BROM/DA | Python apenas para orquestração/evidências; shell já existente para hook. Runtime permanente/IIO seguem trabalho distinto |

Probe/remove/erro do módulo não são alterados; helpers de aquisição, esquema
de calibração e binário nativo permanecem os já verificados. Comparar o pacote
gerado e realizar uma execução automática curta antes de alegar integração.
Não habilitar carregador, estimar SOC nem escrever no rootfs instalado.

### Revisão após o primeiro ciclo automático

Captura dram-20261026-084740:18 leituras, attempts18/fault0, unload e
batch_done válidos, mas confirmação HTTP ausente no limite padrão25s.
O lote ocupou23.54s entre accepted e done; o supervisor só publica a nova
fotografia HTTP depois de hardware_hooks e da sua iteração. Logo o limite
atual é insuficiente para uma confirmação robusta, embora a aquisição tenha
passado. Primeiro resultado/ledger permanecem reprovados, sem reenvio.

Reuso: wait_host_once já oferece o argumento seconds e deadline monotônico.
Estender somente a seleção CLI de observação com escolhas25 (padrão exato)
e40 (opt-in, somente host-once + release native fechado). A chamada antiga
permanece literal no ramo padrão. Não mudar deadline75s do telefone, função
de espera, reset, coleta, flash, readback, ledger ou qualquer comando PMIC.
Provar em replay de relógio/HTTP simulado que25 continua falhando no lote
tardio,40 confirma, e regressão de uptime aborta sem novo envio. Criar
pacote/nonce novos somente após esse teste; nunca reutilizar o permit gasto.
Isso altera a observação opt-in no arquivo do ciclo, não sua recuperação;
registrar essa distinção explicitamente no manifesto.

## MT6357 V/I/T no kernel nativo: reaproveitar aquisição validada (2026-10-26)

Auditoria anterior à extensão do build e ao overlay C. A captura contínua
existente já teve18 rodadas físicas no6.18 pwrapdiag, conforme
manifests/battery-continuous-phone-verification-20261025.json. Esse resultado
não prova o transporte/ownership no6.18 nativo.

| Funcionalidade | Atual | Alternativa, revisão e licença | Compatibilidade / probe / erro / remove | Esforço / recomendação |
| --- | --- | --- | --- | --- |
| Corrente FG MT6357 e compensação de temperatura | current-sequence/current-decode, temperature-acquire/model e módulo continuous já existentes; GPL-2.0-only, hashes nos manifestos de25/10 | Fonte LG mt6357_gauge.c SHA791da3263f0ece0f91c7fe91fcc2f079a053f1441cd9ceab326330afb9a12c4a; backup BMW confrontado. Linux6.18.58 commit2926d88bb7fc4608fd942453d929c39e4e5ec006 fornece regmap e power_supply. Busca adicional mainline/pmaports não confirmou outro FG MT6357 completo | Reutilizar apenas o módulo existente, sem duplicar sequências. Init verifica ID57 e estado antes de comandos; erro bloqueia novas capturas, release/cleanup são os existentes; unregister precede put_device. Latch/ADC fazem escritas de comando, não são operações somente leitura | Pequeno overlay de gate para release nativo e token distinto; original C/binário continuam preservados. Não prometer SOC ou controle de carga |
| BATADC/NTC upstream | Aquisição LG existente com SET/CLR restritos e timeout | drivers/iio/adc/mt6359-auxadc.c GPL-2.0-only, mesma revisão; suporte mediatek,mt6357-auxadc; patches staging já auditados na matriz | Provider upstream faz reset no probe e tem diferenças de canal/alias/escala registradas anteriormente. Não substituí-lo por suposição, nem ativar em paralelo com captura direta | Destino arquitetural segue IIO + power_supply + regmap. Primeiro comprovar aquisição reutilizada sobre transporte nativo; migração IIO separada, não copiar outro provider |
| Transporte nativo | PWRAP/MFD/regmap MT6357 já usados por reguladores e teclas no6.18 nativo | Drivers Linux nativos fixados no mesmo kernel; nenhuma necessidade de novo MMIO/DA/REA. Qualcomm FG depende de outro PMIC/transporte e não é substituto | IRQ de teclas não implica ownership de ADC/FG. Antes de carga, rejeitar módulos de bateria existentes, provider IIO MT6357 e supply duplicado. Não desmontar MFD/reguladores/teclas | Usar sessão residente/ciclo existente; nenhuma alteração em BROM/DA, ciclo ou registro de kernels |
| Build e identificação | Builder já seleciona atomic; registro fechado já tem native com SHA88b5438b… | tools/build-k40s-battery-snapshot.py MIT, interface get_variant/workspace_for já existente | Native opt-in somente com continuous; usar release/exports/hash da variante selecionada. Imagem/artefatos anteriores não são sobrescritos. Original --continuous permanece selecionando atomic | Estender builder existente com --native, saída própria e patch de gate aplicado na cópia; não criar ferramenta/driver paralelo |

Nova busca consultou fontes primárias Linux (mt6359-auxadc e binding MT6357),
pmaports e Qualcomm; não confirmou alternativa FG adicional com revisão/licença.
Limite da busca não significa inexistência. Fontes e limitações anteriores
continuam aplicáveis. Parte realmente específica: sequências FG/NTC e calibração
nominal LG; o overlay de identificação é política do laboratório K40S.
Nenhum efeito novo de probe/remove ou comando PMIC autorizado pelo overlay.
O teste físico curto deverá confirmar captura, erro/remoção observável e
restauração; tolerância a falhas elétricas/firmware concorrente não está provada.

## Status do consumidor ADC: tratamento de supplier desconhecido (2026-10-26)

Auditoria antes de qualquer alteração C. Escopo: corrigir o consumidor existente,
não implementar outro driver de bateria nem controlar carga.

| Funcionalidade | Implementação atual | Alternativa / origem / revisão / licença | Compatibilidade, efeitos e limitações | Esforço / recomendação |
| --- | --- | --- | --- | --- |
| Status sem supplier ou com erro | generic-adc-battery trata retorno negativo de power_supply_am_i_supplied como verdadeiro | Linux6.18.58 commit2926d88bb7fc4608fd942453d929c39e4e5ec006; drivers/power/supply/generic-adc-battery.c SPDX GPL-2.0, SHA8df38519335c3cbc7bbb4293af80f1d1c08528db591cb46909bdb0a899b138d9; power_supply_core existente | -ENODEV significa supplier ausente, não evidência de corrente. API do core retorna outros erros também. Nenhuma mudança no transporte, probe/remove, escrita de PMIC ou aquisição IIO | Extensão mínima: status UNKNOWN para retorno negativo, preservar zero e positivo; inicialização UNKNOWN até a primeira observação. Apenas staging/offline |
| Correção já proposta | Não há correção na árvore local fixada | Pesquisa de generic-adc-battery upstream e patch público 'fix status with no supplier' de 2026-10-12 identifica proposta <=0; merge/commit não confirmados nesta auditoria | Proposta resolve falso Charging, mas transforma erro e ausência em Discharging. Para este aparelho o controle de carga ainda não foi integrado; não tratar essa inferência como observação elétrica. Não copiar patch de origem/revisão não confirmadas | Reutilizar driver/API fixados; limitar extensão à semântica de erro conhecida. Sem alegar correção aceita upstream |
| Alternativas de projetos móveis | pmaports e drivers Qualcomm/MediaTek pesquisados; matriz anterior já compara IIO/power_supply/FG | Linux power_supply genérico é reutilizável; providers Qualcomm dependem do PMIC/protocolo Qualcomm, não equivalem a MT6357/MT6371. Busca pmaports desta etapa não confirmou implementação adicional com commit/licença | Nenhum firmware Android, REA ou driver de carga é necessário para corrigir esta decisão de status; pesquisa negativa é limitada, não prova inexistência | Não trocar de framework nem criar backend Qualcomm. Parte específica de placa: nenhuma neste patch |
| Validação e recuperação | Ciclo físico anterior aguardava USB na auditoria; depois terminou com boot_a/4.9/A-B conferidos, sem reiniciar coletor | Testar gab_work real com interfaces power_supply/GPIO/workqueue simuladas, aplicar sem fuzz em cópia e compilar módulo ARM32 completo com kernel fixado | Prova comportamento do código e integração de build, não prova carga real, GPIO ou probe/remove em hardware. Não alterar ciclo ou imagem validada | Manter patch fora das séries de boot; teste físico do patch continua não realizado |

Fontes consultadas: árvore local fixada e
https://github.com/torvalds/linux/blob/master/drivers/power/supply/generic-adc-battery.c .
O resultado de busca do patch público é apenas uma pista; não atribuir commit
ou copiar conteúdo sem confirmar a fonte primária. Probe, IRQ, devres e remove
do consumidor permanecem os da versão fixada. GPIO charge_finished e seus erros
não são corrigidos nesta alteração e não estão configurados no DT K40S.

## Bateria no 6.18 nativo: ADC MT6371 + consumidor padrão (2026-10-26)

Auditoria antes de retomar o rascunho de DT iniciado após backlight. Sem driver
C novo: Linux6.18.58 commit2926d88bb7fc4608fd942453d929c39e4e5ec006.

| Função | Implementação atual | Alternativa open source / licença / revisão | Compatibilidade e efeitos | Esforço / recomendação |
| --- | --- | --- | --- | --- |
| Aquisição VBAT do sub-PMIC | I2C5/MFD/backlight já observados; bateria DT ainda rascunho | drivers/iio/adc/mt6370-adc.c, GPL-2.0-only, mesma revisão; SHA945589e23447fc93ba3fc6f74ef59170b69673c513f1ab79182d433dddd031d0 | MT6371 DEVINFO F4, ADC usa VID F e escala VBAT5mV, igual ao fator5000uV do fonte LG. Probe lê DEVINFO e escreve somente CHG_ADC0x121=0. Read seleciona canal/start nesse mesmo registro, espera35ms e poll até105ms; dados0x14c..d. ICHG/AICR só lidos para escala de outros canais. Sem charger driver ou set_voltage/current | Reusar módulo upstream intacto; nenhuma alteração no controle de carga |
| Publicação da tensão | Rascunho propõe voltage+current | drivers/power/supply/generic-adc-battery.c, GPL-2.0, SHA8df38519335c3cbc7bbb4293af80f1d1c08528db591cb46909bdb0a899b138d9, mesma revisão | IIO processed mV multiplicado por1000 para uV. Binding adc-battery exige que corrente opcional seja de saída da bateria; IBAT do carregador é não assinado e essa equivalência não foi demonstrada. Não fornece SOC. Sem supplier, power_supply_am_i_supplied retorna -ENODEV; o consumidor testa esse retorno como booleano e pode publicar Charging. Status não é prova de carregamento | Só VBAT em power_supply neste ensaio; manter IBAT acessível pelo provider IIO, não inventar sinal/calibração. Não aprovar esse consumidor como bateria completa enquanto status/erros de supplier não forem tratados |
| Probe/erro/remove | Frameworks IIO e power_supply | devm_iio_device_register, devm_power_supply_register, devm_delayed_work_autocancel | ADC serializa conversões por mutex, erros retornam sem inventar leitura; não tem remove com escrita de charger. Consumidor tem work cancelado por devres. Sem charged-gpios para evitar request/IRQ de GPIO desconhecido. Provider ADC não deve ser removido enquanto consumidor ativo | Manter módulos até fim do ensaio; preservar recuperação. Não afirmar tolerância elétrica/falhas não testadas |
| Alternativas | MT6357 FG/IIO e captura LG já auditados anteriormente; Qualcomm FG distinto | Frameworks power_supply/IIO existentes, postmarketOS usa os mesmos; registro específico FG MT6357 não se confunde com ADC MT6371 | ADC do carregador não substitui fuel-gauge, calibração, temperatura, corrente assinada, carga acumulada ou SOC | Caminho de tensão parcial agora, FG continua requisito do port; não reduzir objetivo à telemetria |

Preservar imagens/DTs anteriores e corrigir apenas rascunho ainda não validado:
retirar IBAT do mapeamento generic-adc-battery. Dados simple-battery são
metadados do BL-T44 informado pelo4.9; não comandam carga e não provam SOC.
No ensaio, conferir explicitamente ausência de mt6370-charger e registrar
que status/capacidade/corrente continuam sem validação. Usar ciclo e sessão
residentes existentes, com restauração/readback/A-B; não mudar recuperação.

## Sessão residente do 6.18 por SSH — auditoria antes da implementação (2026-10-25)

| Função | Atual | Alternativa open source / revisão / licença | Compatibilidade / efeitos | Esforço / decisão |
| --- | --- | --- | --- | --- |
| Shell remoto para trabalho com módulos | SSH só exec, 75 s, sem PTY nem /proc /sys /dev | OpenSSH do Alpine já fixado no payload (BSD-like/ISC por arquivo); BusyBox estático já no initramfs (GPL-2.0-only) com insmod/dmesg/i2c-tools; devpts/devtmpfs do kernel | Mesmo binário, mesma host key de teste e mesma chave pública; só PermitTTY e `pty` na chave. Dropbear ou getty no ACM seriam um segundo servidor sem pin já validado | Pequeno: hook `resident-prepare` e config derivada. Sem servidor novo |
| Sessão longa e fim pedido pelo PC | Supervisor com 75 s fixos e `/cgi-bin/done` | Mesmo supervisor/watchdog e mesmo ciclo DA comprovados | Limite lido só com marcador opt-in; padrão 75 s preservado byte a byte, provado em `test_portkit_core` | Dois hunks revisados no init e três no ciclo |
| Cliente no PC | Verificação SSH embutida no ciclo | ssh.exe do Windows (OpenSSH, BSD-like) com as mesmas opções/pin do ciclo | `k40s-resident.py` (MIT) só monta o comando; sem transporte novo | Pequeno ajudante; nenhum protocolo próprio |

Detalhes, riscos e imagem: [lts-resident-session.md](lts-resident-session.md).

## IOVCC explícito ou não gerenciado — auditoria antes da extensão (2026-10-25)

Correção de proveniência: Makefile LG seleciona touch_hwif_mtk.o para
CONFIG_LGE_TOUCH_CORE_MTK=y; touch_hwif.c é o ramo QCT. O caminho GPIO lido
anteriormente não muda, mas os fallbacks de regulador não são equivalentes.
Preservar os registros anteriores e usar touch_hwif_mtk.c SHA
b24a5d9204353bc80e8b62b4da0c41cefc55792ef0ed8f890a373eca4f3560a5
nas conclusões sobre a configuração MTK.

Skill reverse-engineer-anything: análise estática GNU objdump ARM do mesmo ELF
BMW SHA1ca93464...; provider REA Windows ARM/ELF já rejeitado anteriormente,
sem repetir setup/rejeição. Não são Evidence IDs REA. ft5446_power em c0acb094
mostra sequência ON em c0acb1ac: helper VCL(1), msleep5, reset(1), msleep200;
OFF em c0acb13c: reset(0), msleep5, helper VCL(0), msleep5. Helper em c0ac6648
usa gpio_to_desc -> gpiod_direction_output_raw no ramo de GPIO válido; ramo
alternativo consulta regulator_is_enabled antes de enable/disable, como MTK.
Nenhuma equivalência de todos os globais/paths ou da árvore completa é alegada.

Fdtget lista integralmente propriedades do nó original
/i2c0@11007000/focaltech,ft5446@38: vcl-gpio27/reset-gpio164, sem vdd-gpio ou
propriedade *-supply para esse nó. Ausência não identifica a fonte física de
I/O; não autoriza regulador dummy, tensão presumida ou escrita no PMIC.

| Função | Atual | Alternativa open source / revisão / licença | Compatibilidade / efeitos | Esforço / decisão |
| --- | --- | --- | --- | --- |
| Não controlar I/O não declarado | edt requer iovcc e pode receber dummy | API devm_regulator_get_optional + device_property_present existentes em Linux6.18.58 commit2926d88..., mesma licença do consumidor GPL-2.0-only; sem novo provider | Só LG: quando iovcc-supply ausente, não adquirir/enable/disable outra fonte. Se declarada, get_optional e preservar ENODEV/EPROBE_DEFER/erros; nunca transformar erro de fonte declarada em ausência | Extensão pequena ao consumidor, não à placa/core/transporte. Guardar todas as operações IOVCC inclusive PM/cleanup |
| Evitar VCC fictício no LG | get normal pode aceitar dummy se ausente | Propriedade vcc-supply explícita e framework regulator existente | Recusar LG sem vcc-supply antes de request/reset/fontes. Chips antigos mantêm get e semântica atuais | Binding/DT futuros devem declarar VCL real; sem voltage setting |
| Alternativas | Inventar fixed1v8, copiar helper vendor, userspace GPIO | pmaports/mainline/frameworks já auditados; sem necessidade de provider SoC novo | Inventar fonte não prova rail; userspace não integra ownership/erro. Qualcomm mantém framework consumidor, não herda wiring MTK | Preferir fornecimento explícito ou não gerenciado. Não alegar IOVCC eletricamente validado |

Testar prefixo/action reais com I/O presente/ausente, fonte declarada com erro
permanente/defer, ausência VCC e paridade do legado. Compilar módulo inteiro.
Guardas NULL em suspend/resume não provam tempos/protocolo PM LG corretos:
estes, falhas de disable, IRQ, regmap e DT continuam gates para bind físico.

Resultado: ft5446-lg-optional-iovcc-v1.patch (SHA 21fa1e74…, revisão sem a
linha em branco antes de chave da primeira versão) aplica com fuzz 0 sobre
frame-v2 + power-prefix-v1. Cinco casos reais de prefixo/action passaram
(I/O ausente sem get/enable/disable, VCC ausente recusado antes de qualquer
recurso, EIO/ENODEV/EPROBE_DEFER de fonte declarada preservados, sequência e
unwinds LG declarados iguais, legado idêntico com/sem propriedades) e PM só
difere pelas guardas. Módulo ARM inteiro compilou e ligou com W=1 e modpost
normal no workspace separado -r2 contra o Module.symvers do native-i2c-identity;
zImage inalterado; checkpatch sem avisos de código. Não copiado nem carregado.
Provas e limites: manifests/ft5446-optional-iovcc-verification-20261025.json.

Kbuild completo dos módulos terminou sem erro no workspace separado e gerou
Module.symvers real. A extensão edt-ft5x06 ligou como módulo ARM, sem suprimir
modpost, contra essa configuração; zImage permaneceu byte-idêntica. Não foi
copiada nem carregada no aparelho. Provas e limitações do prefixo:
manifests/ft5446-power-prefix-verification-20261025.json.

## Extensão staging do consumidor: prefixo LG e ownership no unwind (2026-10-25)

ft5446-lg-power-prefix-v1.patch, após frame-v2, usa somente APIs existentes.
Reset LG obrigatório é adquirido afirmado antes dos reguladores e antes da
action gerenciada, de modo que o unwind LIFO ainda o mantém enquanto a action
afirma reset/espera5ms/desliga VCC/espera5ms/desliga IOVCC. Os chips antigos
continuam pedindo reset opcional na posição antiga, sem waits novos no cleanup.
Tests compilam o prefixo real do probe até input_allocate e a action real,
não uma implementação paralela de power e não o probe inteiro. Nove seletores
de falha/sucesso cobrem aquisição de recursos, enable e action_or_reset;
trace do legado é igual antes/depois. Suspend/resume/remove/ISR continuam
byte-idênticos: isso preserva legado, mas não prova PM LG adequado. Falhas
elétricas e falha de regulator_disable ainda não são modeladas; não vincular
no telefone nem alterar DT/perfil ativo nesta etapa.

Fonte touch_hwif.c doador SHAdf0e1667230d8d406fb3dbd9acfedc9534641a0935931232e538ff860a7accd5
mostra power_init requisitando VCL/VDD; touch_power_3_3_vcl usa diretamente
gpio_direction_output(vcl_pin,value) quando válido. Ft5446_power inspecionado
chama esse helper, não controla VDD nesse caminho. Isso não identifica a
alimentação IOVCC física nem autoriza criar um regulador fictício/voltagem.
Conferência adicional contra backup e DT/supplies continua necessária.

177 testes seguros e611 na suíte WSL(21skips) passaram. Objeto ARM compilou;
primeiro modpost não ligou porque Module.symvers faltava no workspace. Não
usar KBUILD_MODPOST_WARN para ocultar esse erro. Gerar a tabela com Kbuild
padrão no workspace separado native-i2c-identity antes de verificar o módulo
completo. Imagens e recuperação não foram substituídas.

## FT5446: aquisição/limpeza de reset antes das fontes — auditoria prévia (2026-10-25)

| Função | Atual | Alternativa / revisão / licença | Compatibilidade / efeitos | Esforço / recomendação |
| --- | --- | --- | --- | --- |
| Sequenciar touch LG | Patch FT5446 frame-v2 sobre edt-ft5x06, ainda não vinculado | Linux6.18.58 commit2926d88bb7fc4608fd942453d929c39e4e5ec006, edt-ft5x06.c SHA81817c94769417d6510981374a19411e28e4018a31d6d7bfa3e1c424fdab8ce9, GPL-2.0-only | Probe atual liga IOVCC/VCC antes de pedir reset. Cleanup gerenciado só desliga fontes; reset adquirido depois da action é liberado antes dela no unwind LIFO. Não equivale à ordem LG reset-low/5ms/VCL-off/5ms | Extensão pequena gated por lg_ft5446: reset obrigatório e afirmado antes de ligar fontes; mesma action existente afirma reset e espera antes de desligar VCC. Não criar módulo de power |
| Controlar VCL GPIO27 | Nenhum no mainline; readback baixo confirmado | drivers/regulator/fixed.c SHAf691182b3832402cacd2aa32c77bcec85e2b3c18d69ef018a4e52da6882f11b3, mesma revisão, GPL-2.0-or-later conforme cabeçalho | Sem boot-on, probe pede GPIO output-low; core assume lifecycle do descritor e registro devm. Startup-delay existe. Não usar always-on/boot-on para contornar consumidor; não inventar tensão/IOVCC ou reprogramar PMIC. Unregister/probe-failure do core e DT ainda exigem conferência específica | Reusar regulator-fixed em DT futuro; nenhum driver paralelo |
| Alternativas | GPIO sysfs/libgpiod, pwrseq, implementação vendor inteira | Frameworks upstream/MediaTek/pmaports já comparados nesta matriz | GPIO userspace não acompanha probe/unwind/IRQ; pwrseq não é consumido por este driver; copiar touch LG inteiro duplicaria input/regmap. Qualcomm não muda a semântica do consumidor, mas usa outro GPIO provider | Estender consumidor upstream, preservar variante antiga e recuperação |

Primeira alteração staging deve provar ordem do prefixo real do probe e action
real de cleanup, inclusive reset indisponível e erro de alimentação/action,
além de paridade dos chips antigos. Não é autorização de bind. IOVCC não
identificado, DT/supplies, suspend/resume/shutdown, IRQ e transações regmap
continuam gates antes de teste físico. Preservar patch frame-v2 e imagens
consumidas. Tempos base LG: VCL-on/5ms/reset-release/200ms; reset-assert/5ms/
VCL-off/5ms. Espera upstream300ms de startup é conservadora, não reduzir para
acelerar o ensaio. Novos códigos apenas no consumidor existente, não no core
reutilizável ou backend de transporte.

## Readback nativo: VCL/reset baixos no mainline, sem escrita (2026-10-25)

Observer pins-v3 passou, com kernel/DT nativei2c1 byte-idênticos. Debugfs padrão
pins retornou GPIO27 e164 com prefixo0100: MODE0, DIR1, DO0, DI0. Ambos estavam
em modo GPIO, saída, latch baixo e entrada digital baixa. Não decodificar os
campos posteriores como se todos os getters tivessem sido validados; não é
medida de tensão/corrente. Init apenas leu o arquivo e não requisitou GPIO,
não alterou direção/valor e não fez transação I2C. Oito CPUs, CCF, adapter e
pinmux observados.174 testes seguros/608 WSL(21skips) passaram antes do ensaio.

Restaurou automaticamente: boot_a/readback/SSH/A-B conferidos, sem intervenção.
Fonte LG associa27 alto a VCL ligado e164 alto a reset liberado. Estado baixo
no candidato é consistente com touch sem alimentação e reset mantido; contrasta
com alto/alto no4.9 conhecido. Isso torna alimentação/reset a próxima hipótese
prioritária, não prova causa única de ENXIO. O callback ft5446_shutdown no
fonte doador apenas retorna0: não atribuir os níveis baixos a esse callback.

Próximo gate é revisar probe/erro/remove dos frameworks regulator-fixed,
reset GPIO e edt-ft5x06, além de DT da placa, antes de qualquer controle desses
pinos. Reutilizar o driver já adaptado, não criar um módulo de power/reset.
Preservar níveis iniciais observados, recuperação e permissões consumidas.
Provas: manifests/mt6765-native-i2c-pins-v3-physical-20261025.json.

## Leitura de MODE/DIR/DO/DI do touch — antes de implementar (2026-10-25)

| Função | Atual | Alternativa / revisão / licença | Compatibilidade e limites | Esforço / decisão |
| --- | --- | --- | --- | --- |
| Observar GPIO27/164 sem request/direção/escrita | Estado conhecido apenas no Linux4.9; identidade mainline retornou ENXIO | Linux6.18.58 commit2926d88bb7fc4608fd942453d929c39e4e5ec006; pinctrl/core.c SHA87b5af12..., pinctrl-paris.c SHA94848be20fd43e443398b5975829534ef95fa1f2df9cd1f835939616b0643502, pinctrl-mtk-common-v2.c SHAf8615055a2df94dd69e57c8dc7e1be59ab7cceddd50163f6de0c5a239a1565e4, GPL-2.0-only | Arquivo pins no diretório device-descriptor já confirmado. .pin_dbg_show chama mtk_pctrl_show_one_pin. Campos iniciais MODE/DIR/DO/DI são getters via mtk_hw_get_value -> mtk_r32/readl; cross-field usa duas leituras. Helpers bias_get também só obtêm campos; nenhum setter/probe/remove é acrescentado. Ler o arquivo percorre todos os pinos, mesmo filtrando duas linhas | Reutilizar debugfs, initramfs e kernel/DT do observer2 byte-idênticos; nenhum módulo C |
| Interpretar registro da placa | Números globais legados não portáveis | Formato upstream literal %03d: %1d%1d%1d%1d%02d%1d%1d%1d%1d | Primeiro4 campos são mux/dir/out/in. DIR1 é output, MODE0 é GPIO; DO é latch, DI é leitura digital, não medida de tensão. Campos posteriores podem conter errno negativo, pois o formatter ignora alguns erros: não fingir validar pull/drive por comprimento fixo | Guardar linha bruta; interpretar só quatro campos iniciais válidos, não adivinhar níveis esperados |
| Alternativas de aquisição | gpioget/libgpiod ou sysfs export | UAPI GPIO existente, porém leitura por request pode selecionar input/alterar ownership/direção; pinctrl já tem provider MediaTek | pmaports/mainline usam os frameworks existentes. Backend Qualcomm teria outro provider/formato; não generalizar o formatter Paris. REA não é necessário com estes fontes completos | Preferir observação existente sem request. Evitar /dev/mem, nova rotina MMIO ou driver paralelo |

Novo pacote/versionamento de observação e permissão próprios; conservar a falha
identity e permissões consumidas. Zero clientes/transações I2C, zero alterações
de touch power/reset, nenhuma mudança de kernel/DT ou instalação permanente.
Testar consumidores e formato offline antes de habilitar operação física.

## Primeira transferência nativei2c-id1: ENXIO e recuperação confirmada (2026-10-25)

Uma tentativa física, sem repetir. Kernel6.18.58 executou init com oito CPUs,
providers, PIO/I2C0 e pinmux82/83; dois snapshots CCF completos. A invocação
fixa i2ctransfer selector0xa3 para0x38 retornou ENXIO. Gate interrompeu antes
do RX, sem resposta/irq_after e sem PASS. Driver MT6765 associa ACKERR/NACKERR
capturados a ENXIO; não é prova de ondas nem causa elétrica específica.
Não reclassificar como sucesso nem interpretar os gates globais false do
wrapper como ausência de boot ou ausência da tentativa TX. Resultado original
e permissão consumida foram preservados.

Coletor capturou logs e restaurou boot_a automaticamente; readback, SSH normal,
hash e A/B conferidos, sem intervenção. Consulta posterior pelo debugfs padrão
do Linux4.9: lge_touch vinculado; gpiochip base332, offsets1 IRQ input-high,
27 VCL output-high e164 reset output-high. Isso corrobora nomes/offsets do
doador, não o estado desses pinos no candidato mainline. Não transportar os
números globais333/359/496 para DT upstream.

Próximo gate é auditar e reutilizar leitura pinctrl/debugfs upstream dos pinos
27/164 e sequência original, sem novo módulo C e sem presumir alimentação.
Não fazer scan, alterar rails/reset ou repetir imagem para contornar ENXIO.
O provider Paris tem .pin_dbg_show -> mtk_pctrl_dbg_show ->
mtk_pctrl_show_one_pin; portanto investigar o arquivo padrão pins, não presumir
que pinconf-pins forneça esses valores. Auditar getters/registro da placa antes
de novo ensaio. Manifesto: manifests/mt6765-native-i2c-identity-physical-20261025.json.

## Gate do executor para nativei2c-id1, antes de habilitar (2026-10-25)

Reutilizar test-k40s-native-ccf-once.py e seu ciclo/DA congelados, não criar
transporte ou novo programa C. Evidência específica não é fornecida por
i2c-tools: o host deve cruzar release/hash fixados, marcadores distintos,
providers/SMP/pinmux existentes, seletor a3 e RX1 na ordem, e IRQ MT_SYSIRQ84
antes/depois com contadores não decrescentes e incremento total mínimo2.
Isso é validação de evidência de placa, não substituição do framework I2C.
Separar resposta de um byte de identidade de chip comprovada. Rejeitar logs
misturados, versões antigas, truncados, duplicados, erro/warning, retorno
parcial ou ausência de incremento IRQ. Manter liberação create-only pelo novo
release e nenhuma repetição automática. Nenhuma alteração comportamental dos
experimentos anteriores nem dos helpers lts-auto-cycle/k40s-da-session.

## Candidato i2c-dev ARM compilado, ainda sem operação física (2026-10-25)

Perfil separado native-i2c-identity usa os mesmos patches, DT e fontes de
drivers MT6765. Diff das configurações finais contém somente I2C_CHARDEV e
LOCALVERSION. DTB byte-idêntico ao adapter-only aprovado. Empacotamento
conferiu kernel/ramdisk/DTB por extração e seis overlays stock. Initramfs
reutiliza i2ctransfer4.4, duas chamadas individuais fixas, saída verbose exata,
erro no seletor bloqueando RX; logs IRQ antes/depois, sem scan/retry ou
alimentação/reset/charger. RAM-only, sem instalar sistema ou tocar armazenamento
no init. Wrapper ainda não habilita este candidato: falta integrar avaliação
de evidência de transferência e permissão própria antes do ensaio físico.

168 testes offline passaram sem transporte; suíte WSL602,21skips, sem falhas.
Falhas iniciais de integração foram preservadas: fixture não podia executar
sh arbitrário na suíte segura e cinco allowlists ainda aceitavam só o perfil
adapter-only. Fixture temporária revisada e nome exato do novo perfil resolvem
sem ampliar guard de execução nem relaxar política boot=forbidden/staging.
Novo teste comprova equivalência integral de perfil exceto fragmento e objeto
i2c-dev adicionais. Ciclo, DA, registry e init antigo mantêm SHA. Provas:
manifests/mt6765-native-i2c-identity-build-20261025.json.

## Preparação da leitura FT5446 com UAPI existente (2026-10-25)

Integração planejada: novo perfil derivado byte a byte dos mesmos patches/DT,
acrescentando apenas fragmento I2C_CHARDEV e release próprio. Initramfs usa
duas invocações fixas do i2ctransfer4.4 intacto, 0/0x38/a3/RX1, somente após
gates de oito CPUs, providers, adapter, ausência de clientes, pinmux e chardev.
Invocações separadas preservam as fronteiras de transferência do doador;
sem concorrentes neste initramfs, sem retry, sem -f, sem scan. Validar saída
verbose exata incluindo tipo/endereço/comprimento/byte e falhar em qualquer
erro/warning/retorno parcial. Novo código é apenas orquestração shell e teste
host de fronteiras, não implementação do transporte nem driver. Testes host
devem cobrir falhas no seletor impedindo RX e respostas parciais/malformadas.
Não remover nem relaxar testes da observação v2; novo ensaio exige nova imagem,
release, manifestação e permissão antes de operação física.

Auditoria antes de implementar outro diagnóstico. Nenhuma nova rotina C.

| Funcionalidade | Implementação atual | Alternativa open source / revisão / licença | Compatibilidade e efeitos | Esforço / recomendação |
| --- | --- | --- | --- | --- |
| Transporte de identidade em userspace | Nenhum; ensaio nativei2c1 sem chardev/transferências | Linux6.18.58 i2c-dev.c, commit2926d88bb7fc4608fd942453d929c39e4e5ec006, GPL-2.0-or-later conforme cabeçalho | ARM32 UAPI nativa; attach cria cdev/device, erro desfaz referências, detach remove cdev/device. Essas rotinas não iniciam transações. I2C_RDWR copia buffers e marca DMA_SAFE; driver MT6765 já deve isolar esses buffers conforme auditoria DMA anterior. Abrir o nó não valida alimentação nem garante barramento saudável | Baixo: habilitar I2C_CHARDEV somente em candidato separado; não mudar o ensaio validado |
| Enviar mensagem fixa sem driver paralelo | Fonte LG usa touch_i2c_read | i2c-tools4.4, https://git.kernel.org/pub/scm/utils/i2c-tools/i2c-tools.git, commit c20cd0b4be78e7b84104452b7fc9c570f00f92bf; tools/i2ctransfer.c, tools/i2cbusses.c e tools/util.c GPL-2.0-or-later | I2C_FUNCS antes de transferir, I2C_SLAVE sem force para rejeitar cliente ocupado, uma chamada I2C_RDWR por invocação; sem scan. Retorno parcial imprime Warning mas pode sair0: o gate deve exigir saída exata e ausência de warning, não apenas exit0 | Baixo: compilar upstream intacto estaticamente ARM; não criar utilitário C próprio |
| Equivalência da leitura de registrador | BMW touch_i2c_read em c0ac4c94 | Fonte LG touch_i2c.c GPL-2.0-only; backup confirma duas chamadas i2c_transfer(...,1), c0ac4d18/c0ac4d2c | Seletor e RX são transferências separadas, não dois msgs em uma chamada. Preservar STOP entre elas; sem concorrentes/clients. Não copiar retries LG. Primeira seleção a3 e RX1; não presumir valor esperado nem provar a alimentação por esta análise | Usar duas invocações fixas e abortar antes do RX se TX falhar; não usar comando combinado por suposição |
| Alternativas pmaports / MediaTek / Qualcomm | Framework I2C padrão e backend MT6765 já auditados nesta matriz | Não foi identificado requisito para ferramenta de transporte específica da distribuição ou SoC; pmaports/community MT6765 e frameworks mainline auditados nas seções anteriores | Mesma UAPI não torna controlador Qualcomm equivalente ao MediaTek; clocks/DMA/reset continuam no backend correspondente. Não importar driver de outro SoC para userspace | Reutilizar i2c-dev/i2ctransfer; nenhum novo backend |

Fontes oficiais: https://www.kernel.org/doc/html/latest/i2c/dev-interface.html
e checkout imutável acima. Não é autorização de scan, charger ou reset de touch.
Build e execução de -V/-h no QEMU são offline, não provam ioctl nem transferência.
Antes do ensaio físico: candidato/permit próprios, invariantes e recuperação;
não relaxar a exigência de zero chardev do ensaio anterior.

## Backup BMW: identificação FT5446 conferida, sem novo diagnóstico (2026-10-25)

Conferência estática adicional em docs/bmw-kernel-touch-re.md: o binário BMW
chama o helper existente para a3/9f/a6/a8/a1/a2, um byte por leitura, como no
fonte LG. Não é necessário inventar registradores nem criar módulo C para
obter identidade. Isso ainda não é auditoria concluída de i2c-tools/i2c-dev,
autorização de transferência ou prova da alimentação do touch. REA conectado
rejeitou ARM/ELF no provider Windows P0; a evidência adicional é GNU objdump
no WSL. Nenhum driver, ferramenta ou rotina de diagnóstico foi implementado.

## Pinmux e adapter nativos observados, sem transferência (2026-10-25)

O ensaio de observação v2 passou sem mudar kernel/DT/drivers do nativei2c1.
Leitura do debugfs padrão confirmou82/83 com mux_owner11007000.i2c,
function func1 e group GPIO82/GPIO83. O texto GPIO UNCLAIMED é a ausência de
claim GPIO separado, não falta de ownership do mux. Isso confirma seleção no
framework; não mede os níveis elétricos, pull-ups ou ondas no barramento.
Driver PIO e adapter i2c-mt65xx vinculados, IRQ MT_SYSIRQ84 cadastrada, oito
CPUs e dois snapshots CCF. Nenhum cliente/transferência I2C foi solicitado.

O wrapper confirmou os marcadores v2 e recuperação por readback/SSH/hash/A-B,
sem intervenção. A permissão e a falha v1 permanecem preservadas e não foram
reclassificadas como sucesso. Provas e limites:
manifests/mt6765-native-i2c-observe-v2-physical-20261025.json.

Próximo gate é uma leitura de identidade FT5446 restrita por endereço/registrador,
preferindo ferramentas Linux I2C existentes. Não fazer scan, copiar driver de
touch completo, alterar power/reset ou habilitar charger para contornar erro.
O bind não prova uma transferência DMA nem entrega de IRQ no controlador.

## Observação pinmux v2 — antes de corrigir o diagnóstico (2026-10-25)

Reusar o kernel/DT e drivers exatos de nativei2c1; o problema é consumidor do
debugfs padrão, não implementação GPIO/I2C. Linux6.18.58 commit2926d88...,
drivers/pinctrl/core.c SHA87b5af12d1965798fae39390c7d9a4e2220433ec7f8229fec3a704613e4f4038,
GPL-2.0-only: pinctrl_init_device_debugfs usa device-name-descriptor-name.
Descriptor Paris=KBUILD_MODNAME, pinctrl_paris nesta build. Alternativas já
auditadas (postmarketOS/MediaTek) usam o mesmo framework; Qualcomm tem outro
provider/descriptor, portanto não fixar esse nome no core genérico do projeto.
Não é preciso REA, módulo C, sysfs paralelo ou reconstruir um kernel idêntico
apenas para trocar o consumidor debugfs no initramfs.

Novo initramfs separado busca o nome exato da build, preservando o anterior,
sem mudar hardware/probe/remove. Novo pacote terá SHA fixado e marcador de
observação version2, permissão durável própria explícita e testada; a permissão
nativei2c1 continua consumida. O wrapper deve rejeitar logs version1 para esse
ensaio, inclusive se conterem PASS. O release do kernel continua igual porque
seus bytes serão conferidos idênticos; identidade da observação não é release
de kernel. Não relaxar critérios de pinmux nem fingir nova build kernel.
Na interface Paris os nomes são func0..func15, não SDA0/SCL0. Conferir
func1 e group GPIO82/GPIO83, além do owner11007000.i2c; a tabela upstream
já auditada associa função1 nesses pinos a SDA0/SCL0. Isto é ownership do
framework, não medição elétrica dos pinos. Rejeitar outra função/grupo.

Antes de outro bind, teste a função upstream real de nomeação (com stubs de
debugfs/alloc) e casos negativo/duplicado de evidências. Mantêm-se zero clientes,
zero transferências, sem alimentação/reset de touch ou carregador e recuperação
já demonstrada. Isso é correção do ensaio de integração, não teste físico para
completar apenas uma auditoria. Somente observação válida autoriza o passo I2C.

## Primeiro bind PIO/I2C: resultado parcial e diagnóstico de caminho (2026-10-25)

Uma tentativa nativei2c1 registrou mt6765-pinctrl, i2c-mt65xx, adapter i2c-0
e IRQ Linux190/MT_SYSIRQ84; CPUs0–7 online, dois snapshots CCF e nenhum cliente
ou transferência I2C solicitado. O ensaio NÃO passou: pinmux_debug_missing.
Código padrão pinctrl/core.c:pinctrl_init_device_debugfs concatena device-name
e descriptor-name quando diferentes. pinctrl-paris.c usa KBUILD_MODNAME; o
comando de compilação real fixa pinctrl_paris. Portanto o diagnóstico deveria
procurar10005000.pinctrl-pinctrl_paris/pinmux-pins, não o diretório sem sufixo.
Essa é evidência estática do nome esperado, não leitura dos pinos no candidato.

Não enfraquecer PASS, trocar FAIL por sucesso nem apagar a permissão para
repetir a mesma imagem. Corrigir o consumidor da API debugfs padrão numa nova
identidade de ensaio, sem módulo C/sysfs/parser alternativo; depois confirmar
ownership de82/83. Binding/IRQ registrada não prova entrega de IRQ, forma de
onda, touch ou transferência DMA. Reguladores, reset/power touch e carregador
continuam fora do ensaio.

Captura e restauração automáticas passaram: readback, SSH normal0–7, hash e
A/B idênticos. Dados brutos privados preservados, somente hashes/resumo no Git:
manifests/mt6765-native-i2c-physical-20261025.json.

## Primeiro bind pinctrl/I2C e segurança do probe — antes da integração (2026-10-25)

| Função | Implementação / alternativa / revisão / licença | Compatibilidade e efeitos | Decisão |
| --- | --- | --- | --- |
| PIO/EINT e mux SDA0/SCL0 | pinctrl-mt6765, pinctrl-paris e mtk-eint do Linux6.18.58 commit2926d88bb7fc4608fd942453d929c39e4e5ec006, GPL-2.0-only; binding upstream já auditado/backportado; postmarketOS/comunitário já comparados | Probe EINT escreve dom_en/mask_set=0xffffffff em todos os ports e cria domínio/handler; remove desliga handler, synchronize_irq e descarta mappings, não restaura estado LG. Pinos82/83 função1 vêm do backup/doador. IRQ171 nível alto; sem cliente EINT/touch ativo | Reusar drivers e grupos DT, sem módulo C GPIO. Habilitar somente PIO e I2C0; nenhum GPIO de alimentação/reset, drive-strength, pull novo ou outro cliente. Não fazer unbind/suspend nesse primeiro ensaio |
| Adapter I2C0 | i2c-mt65xx upstream + native-v2 + dma-lifetime-v2 já auditados, GPL-2.0-only; CCF nativo com oito CPUs agora comprovado | Probe prepara clocks, programa/reset e publica adapter. Dois recursos0x11007000/0x11000080, IRQ84, clocks IFR3/27, divisor5/400kHz. Sem filho OF e class de detecção zero, não iniciar varredura/transações | Integrar patches existentes e header único; I2C_CHARDEV n, sem i2cdetect/transferência nova. Cadastro não comprova comunicação com touch; IRQ elétrica/transferência ficam gates separados |
| Timeout no probe / ordem de reset | mtk_i2c_mt6765_quiesce/quarantine existentes, polling DMA/START e CCF Linux; sequência APDMA upstream já põe warm reset antes de reset do controlador | Encontrada lacuna: init nativo faz reset I2C antes de DMA idle e probe desabilita clocks/libera buffer mesmo se init expira. Caminhos transfer/resume já colocam timeout em quarentena. __clk_put do CCF fixado não chama disable/unprepare, provider nativo builtin continua vivo | Pequeno delta no driver existente: quiesce limitado antes de configurar/resetar I2C, e timeout do probe segue quarentena antes de qualquer disable/unprepare/free. Não desenvolver outra máquina de estados ou controlador. Testar função init e probe real completos antes do bind |

Em falha de probe, devres ainda libera struct/mappings/handles; não alegar que
get_device preserva devres. Antes de pedir IRQ/publicar adapter não existe
callback registrado apontando para esse contexto. Memória coerente não-devm,
enable/prepare dos clock cores builtin e referência device/module ficam retidos
intencionalmente até reboot; poison impede novo probe nativo. Nenhum caminho
posterior deve usar o contexto liberado. Isso não certifica DMA herdado ativo
ou ordenação elétrica: primeira validação física será só bind sem transações,
com watchdog/BROM e restauração preservados. Carregador permanece desativado.

Empacotamento: reusar build-lts-test-boot.sh e check-k40s-lk-overlay.py,
com opção explícita --native-i2c-adapter. O modo padrão continua exigindo
PIO disabled; a opção exige PIO/I2C okay, nós nativos, recursos/IRQ/clocks/pinos
fixados e nenhum filho no adaptador, em todos os overlays. Não retirar a
checagem antiga nem aceitar status arbitrário. DTC/dt-schema continuam sendo
os validadores gerais; código próprio só cobre invariantes específicas da placa.

## ARMPLL nativo early/late: oito CPUs comprovadas (2026-10-25)

O ensaio nativeccf2 corrigiu a limitação do nativeccf1 sem reativar o provider
local: BROM armado0.007079s → autorização0.007184s → preparo pelo CCF
nativo0.007249s → oito processadores0.019048s → userspace com0–7 online.
Os três providers nativos vincularam e dois snapshots mantiveram uma entrada
armpll com referências1/1. PCW foi conferido inalterado; nenhuma medição de
frequência, política DVFS ou tensão nova foi introduzida.

Captura e restauração foram automáticas, sem intervenção. SSH confirmou o
Linux4.9 com0–7 online, hash boot_a esperado e A/B idêntico; atomic segue
byte-idêntico. Não substituir o kernel validado por este teste RAM sem USB,
eMMC ou periféricos ativos. Provas, hashes e limitações:
manifests/mt6765-native-ccf-early-physical-20261025.json.

O próximo incremento pode reutilizar as integrações pinctrl/I2C já auditadas
sobre essa base CCF, mantendo touch/charger desativados até validação própria.
Não generalizar o hook de autorização da placa para Qualcomm/BROM genérico.

## Resultado físico CCF e próxima integração early/late (2026-10-25)

O ensaio nativo terminou sem intervenção: três providers clk-mt6765 vinculados,
dois snapshots e conclusão RAM às9.413s; captura DRAM e restauração com
readback/SSH/hash/A-B confirmados. Somente quatro CPUs subiram: CPU4–7 falharam
antes de CCF, com ARMPLL_CON0=0x190 e PWR=0x2 observados em leitura pré-CPU4.
O driver nativo é arch_initcall; a preparação local antiga era early_initcall.
Não confundir o marcador PASS do CCF com SMP completo nem substituir atomic.
Linux normal voltou com0–7 online. Manifesto novo preserva a limitação e hashes:
manifests/mt6765-native-ccf-physical-20261025.json.

| Função planejada | Reuso / revisão / licença | Compatibilidade e efeitos | Recomendação / código realmente específico |
| --- | --- | --- | --- |
| Preparar ARMPLL antes de SMP | mtk_clk_register_pll(), mtk_pll_ops e tabela plls do próprio Linux6.18.58 commit2926d88bb7fc4608fd942453d929c39e4e5ec006, GPL-2.0-only | API individual já é pública em clk-pll.h e aceita dev NULL; não é necessário inventar struct device temporária ou outro driver de PLL. Registro crítico chama prepare e escreve potência/isolação/enable, portanto não é leitura passiva | Reusar a entrada ARMPLL da tabela nativa e o callback já testado; hook de placa só autoriza e escolhe a fase após BROM armado. Não copiar algoritmo de frequência/voltagem nem modificar DA/BROM |
| Transferência early/late | clk-mt8173-infracfg.c e clk-mt6797.c upstream, mesmos commit/licença, já compartilham onecell early/late com entradas EPROBE_DEFER | Padrão upstream existe. mtk_clk_register_plls() pula entrada pré-preenchida com warning e seu rollback pode retirar entradas anteriores que não registrou: não usá-lo cegamente sobre ARMPLL retido | Uma instância do clock/registradores, mesmo hw na publicação APMIXED posterior. Unwind deve distinguir propriedade early/late, nunca desregistrar PLL necessário às CPUs ou criar nomes/providers paralelos |
| Fase e recuperação | CLK_OF_DECLARE_DRIVER e early_initcall existentes | of_clk_init padrão pode ocorrer antes do early_initcall que arma BROM. Migrar tudo para CLK_OF_DECLARE sem guard reduziria recuperabilidade; não mover BROM por conveniência | Preservar ordem BROM confirmado → preparo ARMPLL nativo → SMP → restantes providers. Conferir root clk26m e nó DT/opt-in antes de escrever. Gate staging com testes de erro/handoff e nova imagem única antes de outro ensaio |

Implementação staging escolhida: API early pequena no driver MT6765 existente,
mtk_clk_register_pll(NULL, entrada_ARMPLL, base), sem publicar outro provider.
O hook da placa reutiliza k40s-armpll-policy-v2.h para estado/rate/readback e
confere BROM armado. Não contém PLL ops nem algoritmo de programação novo.
Registro critical retém hw/mapeamento para sempre após sucesso; erro posterior
não desregistra esse clock, e late probe só limpa prefixo/sufixo que registrou.
Não passar entrada retida para rollback global de mtk_clk_register_plls.
Falha de readback após possível escrita é fatal antes de SMP, com recuperação
armada; não tentar unprepare/rollback de PLL crítico por nova rotina paralela.
Falha anterior à escrita não autoriza CPU/SMP completo. Gate Kconfig próprio,
opt-in exato e perfil novo; caminho sem handoff mantém registro antigo.

## Ciclo RAM sem USB — antes da implementação (2026-10-25)

| Função | Implementação atual / alternativa aberta | Compatibilidade, limites e esforço | Decisão |
| --- | --- | --- | --- |
| Orquestração sem gadget | lts-auto-cycle.py, DaProcess, recover_unconfirmed_test, flash-boot-auto-brom.py e inspect-k40s-ab.py existentes; ferramentas próprias MIT | Recuperador já restaura e confere SSH/hash/A-B sem afirmar sucesso USB. Seu modo normal espera60s por USB, impróprio para kernel sem gadget. Alterar esse modo arriscaria recuperação validada | Wrapper experimental pequeno reutiliza funções existentes, não muda seus bytes nem implementa transporte; coletor começa assim que o escritor termina, sem atraso arbitrário nem USB adicional |
| Logs de kernel | debugfs/printk/ramoops Linux6.18.58 commit2926d88bb7fc4608fd942453d929c39e4e5ec006 GPL-2.0-only, decoder LG já existente MIT | Captura pode interceptar BROM pré-boot e recuperar antes do ensaio. Ausência do release e marcadores completos deve ser inconclusiva. Pstore pode conter dados antigos: restringir a pacote com SHA fixado e permissão durável de tentativa única, consumida antes de armar | Sem módulo C, parser FDT/RAM novo, dispositivo USB ou alegação de frequência medida; decodificar a zona console pelo helper existente e exigir sequência completa de dois snapshots |
| Alternativas de boot/log | kexec/kdump e pstore do Linux; fluxo de boot postmarketOS e backend MediaTek existentes já auditados | kexec depende de suporte da plataforma/firmware e não testa o mesmo handoff LK. Qualcomm EDL/Firehose não é substituto BROM/DA. Ghidra/binutils não são transporte ou prova de boot | Reusar ciclo LG demonstrado, sem importar outro BSP ou generalizar protocolo. Sem novo driver/checkpoint DA. Não repetir automaticamente imagem inconclusiva |

Permissão de tentativa única não impede reinícios internos do hardware; impede
reenvio automático pelo host. Retorno/captura BROM não prova que o candidato
executou. A restauração/hash/A-B deve ser confirmada antes de avaliar os logs.
Perfil de compilação permanece forbidden para instalação permanente; execução
temporária requer o wrapper explicitamente solicitado e todas as validações.

Pré-condição adicional sem código kernel: clk_flags de armpll, armpll_l, ccipll,
mainpll e mpll no Linux4.9 vivo foram lidos via SSH e retornaram0x00000800 para
os cinco. No fonte LG CLK_IS_CRITICAL=BIT(11) e PLL_AO vira essa flag; os cinco
PLL_AO do driver nativo coincidem com a política crítica atualmente operante.
O wrapper confere novamente esses valores antes de preparar/armar. Isso não é
leitura do efuse30 nem prova de estado herdado do LK, nem de todas as tabelas;
evita assumir a política alternativa com armpll não crítico. Sem módulo novo,
leituras de NVMEM/devinfo completo, IDs privados ou alteração de clocks.

## REA: conferência dos clocks contra o backup original (2026-10-25)

Aplicação explícita da skill reverse-engineer-anything. Investigação estática,
sem transporte do telefone, execução do Android, flash ou alteração dos backups.
O doctor REA6.5.0 confirmou registro Codex alinhado, mas não há ferramentas REA
conectadas nesta sessão. A rejeição anterior do ELF ARM pelo provider Windows
P0 permanece em work/bmw-kernel-re-20261025-v1/rea-current.json. Não repetir
essa operação sem mudar o provider/host; não reinstalar nem alterar MCP.
As observações novas abaixo são GNU binutils, não Evidence IDs REA.

Identidades reconferidas por SHA-256 nesta investigação:

- boot_a original: 9b807d13eefc6fde818e5aae74df4697e384f0b89bc5132c70fadcf707e07fca;
- kernel.raw: 68bd6d0b27ecfbba513bf301a61ce122a5b58a49dd0c7434cd135dd3dfae24fe;
- ELF sintético atual: 1ca934648a7f1da852d619fe1d264bfa3093ae281f545310ec06f7f21d24da61;
- fonte doador drivers/clk/mediatek/clk-mt6765.c da árvore LG4.9:
  b4082cee7d7112676cf28fa904a76874a38c568e75b10fc86120119ce060f425.

O ELF sintético não é a imagem original, não tem identidade de importação Ghidra
igual ao hash atual e nunca deve ser usado para boot. A igualdade anterior da
seção .kernel com kernel.raw está documentada em bmw-kernel-touch-re.md.

| Funcionalidade | Implementação original observada / fonte doador | Alternativa open source | Compatibilidade e esforço | Recomendação |
| --- | --- | --- | --- | --- |
| Inicialização APMIXED | BMW mtk_apmixedsys_of_clk_init_driver em c1532e30, span até c1532f60; doador ELF tem função de tamanho0x130 no mesmo endereço | clk-mt6765 upstream já auditado, commit21a7f44fd0765fcc5194130b28767786eba1d1e7, GPL-2.0-only | BMW escreve base+0x0c com AND0xffffffe1, +0x44/+0x48 com AND0x01041041. Mesmas operações diretas no fonte doador e upstream. BMW contém dsb sy e chamada arm_heavy_mb após cada store. Não prova equivalência de readl/writel/helpers modernos nem das tabelas/globais | Reutilizar provider upstream e preservar auditoria de barriers/probe/erro. Não transplantar todo CCF vendor nem remover as proteções de unwind/PMIC |
| Inicialização TOPCKGEN | BMW mtk_topckgen_of_clk_init_driver em c1532f60, span até c1533090; doador ELF tamanho0x130 no mesmo endereço | Mesmo driver upstream, GPL-2.0-only | BMW faz OR0x3ef em base+0x200 e OR1 em +0x204; mesmos offsets/máscaras no doador e upstream. OR0x3ef aparece em duas instruções OR0x3ec/OR3. Literal pools no fim do span não são instruções válidas a executar | Não criar sequência C paralela para esses cinco writes. Validar integração do driver existente; máscaras iguais não autorizam probe físico |
| Seleção de PLL por variante | BMW chama get_devinfo_with_index(30) e compara resultado com8/15 antes de escolher uma entre duas tabelas de dez PLLs; fonte LG explicita plls/plls_no_armpll_ll | CCF upstream e providers já existentes, não copiar a API devinfo Android | Tabelas apontadas não comparadas integralmente nesta passagem; valor real do efuse não adquirido. Possível diferença de política por variante continua aberta | Conferir flags/tabelas e variante real antes de concluir equivalência de ARMPLL ou importar a ramificação. Nenhuma leitura nova de efuse/PMIC |

Reprodução da observação estática: usar arm-linux-gnueabihf-objdump -d com
--start-address=0xc1532e30 --stop-address=0xc1533090 sobre o ELF sintético
identificado acima; arm-linux-gnueabihf-nm -S no vmlinux doador para os tamanhos.
Endereços virtuais pertencem ao BMW4.9, não devem virar endereços do LTS.
O disassembly foi inspecionado nesta sessão; não foi criado um novo decoder,
módulo C, diagnóstico no telefone ou prova de execução dessas funções.

Conclusão delimitada: os cinco read-modify-write finais já existem no driver
upstream. Permanecem por comparar tabelas de PLL/mux/gates, variante efuse,
helpers/barreiras e efeitos de registro dos clocks críticos. Similaridade de
dois spans e máscaras não prova equivalência de toda a árvore HM/BMW/mainline.

## Ensaio CCF isolado — antes da preparação (2026-10-25)

Correção de integração antes da compilação: olddefconfig descartou
COMMON_CLK_MT6765 porque o Kconfig upstream exige ARM64 ou COMPILE_TEST.
O K40S executa ARM32. Reusar o mesmo driver com ampliação restrita da condição
para MACH_MT6765_K40S_EARLY evita habilitar COMPILE_TEST globalmente ou criar
outro driver. Delta somente Kconfig, GPL-2.0-only, sobre Linux6.18.58 fixado;
não modifica probe/remove ou tabelas, mas permite que esses caminhos sejam
ligados pela primeira vez neste perfil. PHY_K40S_USB2_BOOT_TEST deve ficar n:
depende do provider USB local explicitamente desabilitado. Workspaces de
configuração rejeitados são preservados; nova preparação recebe versão nova.
O verificador host precisa reconhecer a serialização padrão de olddefconfig:
bools invisíveis podem ser omitidos, em vez de escritos como comentário n.
Ausência equivale apenas a n; exigências y/m/strings continuam falhando quando
ausentes. Reusar o formato .config do Kconfig upstream, sem contornar uma
exigência y descartada. Testar também y/m inesperados e ausência de y.

Composição real com DTBO: quinze placeholders sem compatible na base recebem
status okay do firmware, não somente parâmetros. Dois também recebem os
compatibles mediatek,md1_sim1_hot_plug_eint-eint e
mediatek,md1_sim2_hot_plug_eint-eint. Busca literal recursiva em drivers/ da
árvore LTS preparada não encontrou esses dois IDs. Os demais continuam sem
compatible; nenhum dos quinze ganha reg. Os testes exigem exatamente esses
dois IDs, nenhum recurso reg novo nesses nós, e nenhum delta nos providers
nativos. Isso não equivale a afirmar que todo status continua disabled.
I2C/PIO/USB/MMC/PWRAP bindáveis não são ativados. Nenhum módulo vendor SIM é
importado para satisfazer esses placeholders.

| Função | Reuso / versão / licença | Compatibilidade / risco | Decisão |
| --- | --- | --- | --- |
| Compilação isolada | kernel-workspace.py existente, Linux6.18.58/ARM e perfil preservado no build-report atomic; ferramentas próprias MIT | Nova árvore extraída do tarball fixado, patches de unwind/proteção PMIC já auditados; não modificar fonte/build/hash atomic. Providers CCF nativos escrevem prepare/enable de PLLs críticos e cinco registradores no probe | Perfil novo offline/forbidden, consumidores I2C/PIO/USB/MMC/PWRAP disabled; iniciar só providers/raízes. Manter fontes/regras antigas para recuperação |
| Observação | debugfs clk_summary do CCF Linux6.18.58, shell/BusyBox/printf e pstore já existentes; kernel GPL-2.0-only | Summary lê taxas/contagens do framework, não prova oscilação física. Confirmar bindings pelo symlink de driver e publicar somente linhas selecionadas no console RAM; sem escrita em clock sysfs/registradores | Initramfs RAM de duração limitada por watchdog; nenhum módulo C, protocolo ou validador binário novo. Sem mount de armazenamento, serviço, rede ou cliente PMIC |
| Retorno/coleta | k40s-test-brom early arm + watchdog + k40s-da-session e restaurador existentes | Auto-cycle atual pressupõe USB e espera60s; iniciar coletor cedo pode capturar o BROM pré-boot, tarde pode perder janela. Erro USB não prova falha de CCF. Captura depende de logbuf da build exata | Preservar recuperador, não alterar comportamento por conveniência. Primeiro pacote/DT/ramdisk/hashes offline e plano de coleta RAM específico antes de qualquer flash; não usar conclusão USB para declarar sucesso CCF |
| Layout | build-lts-test-boot.sh, gen_init_cpio, build-boot-image.py, check-k40s-lk-overlay.py existentes | Compara conteúdo extraído, seis overlays e memória; não certifica a segurança dos PLLs ou firmware. Sem AVB bypass novo, sem tocar partições neste passo | Reusar builder; novos artefatos em diretório exclusivo, perfil NÃO vira autorização de instalação |

postmarketOS/referência comunitária já fornecem o driver/DT usados na auditoria
anterior; não é necessário copiar outro runtime de testes ou usar código
Qualcomm para capturar debugfs/pstore MediaTek. Fonte completo dispensa REA.

## Consumidores nativos USB/eMMC/PWRAP — antes da implementação (2026-10-25)

| Função | Origem / API / licença | Compatibilidade e efeitos | Decisão / esforço |
| --- | --- | --- | --- |
| Clocks USB | clk-mt6765 + CCF Linux6.18.58 commit2926d88..., GPL-2.0-only; PHY local e MUSB já auditados | main→USB_TOP_SEL118=62.4MHz; mcu→IFR_ICUSB0=156MHz; univpll→UNIVPLL3_D4_32=62.4MHz. CCF pode abrir/fechar gates, ao contrário do provider de handoff que os retém. PHY mantém guard/recuperação e sequência própria, sem set_rate | Migrar apenas refs DT, não reescrever PHY/MUSB. Sem prova física da nova combinação; providers e consumidores disabled |
| Clocks eMMC | mtk-sd e CCF existentes; TOP_MSDC50_0_60, IFR_MSDC0_20, IFR_MSDC0_SRC56 | source/hclk/source_cg preservam nomes e taxa herdada~384/273MHz. mtk-sd local não chama clk_set_rate/parent; CCF real poderá gatear em runtime/error, enquanto provider antigo mantinha gates abertos | Migrar refs; preservar limites52MHz/8bits, constraints3.0/1.8V always-on e caminho original. Não alegar equivalência de gating/PM nem substituir imagem validada sem teste |
| Clock PMIC vivo | CLK_IS_CRITICAL e guards clk_core_disable/unprepare upstream; gate PMIC_AP64 já presente no workspace | devm_clk_bulk_get_all_enabled libera refs em falha. Gate PMIC_AP não pode perder último voto e fechar o barramento PMIC. Flag crítica cria voto inicial e bloqueia último disable/unprepare; registro pode escrever enable. Não é registro passivo nem snapshot restore | Delta de uma entrada no driver existente após unwind-v2; sem clock provider paralelo. Conferir guards CCF reais e manutenção das tabelas restantes antes de usar |
| Reset PWRAP | devm_reset_control_get_optional_exclusive, reset core e guard K40S existentes; schema mediatek,pwrap.yaml já permite resets ausente | Native CCF não oferece reset e MT6765 exige handle no driver. Somente CONFIG handoff + MT6765 + autorização atual permite lookup optional; erro/defer de provider ainda deve propagar. O caminho MT6765 guardado nunca entra em cold-init/reset, mesmo se a autorização cair depois | Pequeno helper de seleção da API no driver PWRAP existente; não criar fake reset bem-sucedido nem generalizar null-reset para outros SoCs/configurações. Legacy obrigatório preservado |
| Referências externas | postmarketOS encaminha adomerle/linux-mt6765 commit5be6e646 já fixado; seu DT tem TOP26M/IFR_PMIC_AP no PWRAP sem reset. Qualcomm usa outros clock/reset providers | DT comunitário não prova comportamento deste driver guardado/placa LG. APIs comuns e schemas nativos já atendem; não instalar ferramentas ou importar BSP inteiro | Código específico só nos guards existentes e DT da placa; nenhum backend Qualcomm, novo módulo C ou substituição dos experimentos anteriores |

A matriz não autoriza ativação: transição de PLLs críticos, origem de clocks,
IRQ e falhas dos consumidores precisam compor um pacote recuperável. Carregador
MT6370/MT6371 continua desabilitado; não habilitar EINT/IRQ do PMIC por arrasto.

## CCF MT6765: registro transacional — antes da correção (2026-10-25)

| Função | Alternativa / revisão / licença | Compatibilidade e efeitos | Recomendação |
| --- | --- | --- | --- |
| Publicação APMIXED/TOP/IFR | clk-mt6765.c e mtk_clk_register/unregister_* do Linux6.18.58 commit2926d88bb7fc4608fd942453d929c39e4e5ec006, GPL-2.0-only; mtk_clk_simple_probe já faz unwind para gates/mux/factors | Probes específicos ignoram retorno de PLL/gates/fixed/factors/muxes; v1 só impedia writes após erro do provider. Helpers existentes retornam erro e limpam registros parciais próprios. simple_probe não oferece PLLs/APMIXED nem os cinco writes de hardware deste SoC | Estender probes existentes com checagem de retorno e unwind reverso pelos helpers existentes, sem provider/allocator paralelo. Preservar tabelas e trace de sucesso. Não acrescentar remove genérico ou afirmar restauração de PLL/gates |
| Referência mais nova | torvalds/linux commit21a7f44fd0765fcc5194130b28767786eba1d1e7 clk-mt6765.c GPL-2.0-only, arquivo isolado por URL imutável | Probes continuam ignorando erros. Diferença local relevante é gate PMIC_AP adicionado ao workspace antigo, que deve ser preservado; não trocar o arquivo inteiro por versão nova. postmarketOS encaminha à árvore comunitária, não comprova unwind LG; Qualcomm usa outros providers | Correção específica pequena sobre fonte LTS efetivamente auditado, não atualização de checkout ou importação de nova árvore |
| Frequências herdadas | clk_summary do CCF4.9 via SSH estrito somente leitura em2026-10-25T21:08:48Z | Observado i2c_sel←univpll3_d2=124.8MHz e axi_sel←syspll_d7=156MHz. Contagens podem mudar entre leituras; não é registro físico nem frequência medida. Divisor DT5 implica24.96MHz de entrada do cálculo I2C | Preservar seleção herdada; não inventar assigned-clocks/rates. Evidência privada em artifacts, resumo sem dados privados no manifesto; sem sysfs writes/reboot |
| Fiação DT nativa | Schemas mediatek,apmixedsys/topckgen/infracfg.yaml já incluem MT6765 no LTS; clocks fixed-clock, i2c binding staging e pinctrl já auditados | BMW usa TOP10000000, IFR_AO10001000 (não IFR1020e000), APMIXED1000c000. Referência comunitária coincide; clk32k BMW é32000Hz e não32768 da outra placa. Novo target substitui, não soma, providers locais ARMPLL/USB/PWRAP | Reusar schemas/CCF existentes. DT SoC genérico separado do I2C0/IRQ da placa, todos disabled. Nó i2c@ separado do alvo LK vendor i2c0@, sem clientes copiados. Sem assigned-clocks/rates; primeiro verificar composição e refs com DTC/libfdt/dt-schema |

Registro de clocks críticos pode chamar prepare/enable e escrever hardware
antes da publicação. Unregister libera objetos/domínio lógico, não restaura
snapshot herdado; falhas de regmap seguem limites já auditados. Patch permanece
staging, sem bind físico, charger ou mudança nos scripts de recuperação.

## Pinos I2C0/touch e binding MT6765 — antes da integração (2026-10-25)

| Função | Implementação / origem / licença | Compatibilidade / efeitos | Esforço / decisão |
| --- | --- | --- | --- |
| GPIO/pinmux/EINT | Linux6.18.58 commit2926d88bb7fc4608fd942453d929c39e4e5ec006 pinctrl-mt6765.c, pinctrl-paris.c e mtk-eint.c, GPL-2.0-only; fonte LG auditado como doador | Driver já existe. SDA0/SCL0=GPIO82/83 função1; IRQ touch=GPIO1 função0; reset164 e VCL27 função0. Probe EINT mascara linhas e instala domínio/handler, não é leitura passiva. Estados pinctrl só escrevem quando selecionados; remover driver não restaura estado herdado | Reusar integralmente driver/framework, sem módulo C de GPIO novo. Primeiro grupos DT disabled e contrato de pinos. Não habilitar EINT/clients por causa de testes de schema |
| Binding MT6765 | torvalds/linux commit21a7f44fd0765fcc5194130b28767786eba1d1e7 Documentation/devicetree/bindings/pinctrl/mediatek,mt6779-pinctrl.yaml, GPL-2.0-only OR BSD-2-Clause | Snapshot atual já documenta MT6765 e nomes iocfg0..7/eint, força nove recursos e drive-strength específico. LTS6.18.58 não o documenta. Patch v10 do autor Yassine Oudjana explica a inclusão; não há motivo para criar schema paralelo | Backport do arquivo upstream exato, sem escrever validador novo. Atenção: schema novo usa grupos *-pins/pins*, não nomes antigos *-0/*-pins. Validar grupos novos e restrições com dt-schema/DTC/libfdt existentes |
| Outras bases | postmarketOS wiki MT6765 aponta adomerle/linux-mt6765; referência comunitária fixa5be6e646 já registrada | Status geral de outra placa não prova recursos BMW. Qualcomm usa TLMM/irqchip diferente, não fornece substituto do provider MT6765 | Compartilhar contrato/testes host, manter bancos e pinos da placa no perfil K40S. Nenhuma implementação Qualcomm nova |
| Reset e alimentação | gpiod, regulator-fixed e regulator core existentes; touch_ft5446.c/h e touch_hwif_mtk.c LG | VCL GPIO27 é ativo alto; POWER_ON aguarda5ms antes de soltar reset físico164 e200ms após. IRQ0x2002 mistura IRQF_ONESHOT0x2000 com falling2. IOVCC não está identificado no DT; não inventar rail/dummy1.8V nem concluir equivalência do probe edt | Grupos reset/VCL sem output-high/low, sem consumidor touch ativo. Auditar sequência completa/rails antes de converter VCL em supply; este passo não instala novo driver nem autoriza reset/power |

Origem pública fixada:
https://github.com/torvalds/linux/blob/21a7f44fd0765fcc5194130b28767786eba1d1e7/Documentation/devicetree/bindings/pinctrl/mediatek,mt6779-pinctrl.yaml
e discussão do autor (não prova de inclusão no LTS):
https://lore.kernel.org/linux-gpio/20260925-mt6735-pinctrl-v9-v10-4-cc042983c565@protonmail.com/
Consulta postmarketOS: https://wiki.postmarketos.org/wiki/MediaTek_Helio_P35_(MT6765).
Escopo Qualcomm comparativo, não equivalência de protocolos/IPs.

Compatibilidade do backport: o snapshot upstream exato rejeitou #address-cells0
do EINT existente. Delta separado admite somente0, mantendo diagnóstico/teste
em vez de suprimir warnings do DTC ou alterar a ABI. Nenhuma escrita/probe.

## Binding I2C nativo — antes da integração (2026-10-25)

| Função | Implementação / origem | Compatibilidade / limites | Esforço / recomendação |
| --- | --- | --- | --- |
| Contrato DT MT6765 | Linux6.18.58 commit2926d88bb7fc4608fd942453d929c39e4e5ec006 Documentation/devicetree/bindings/i2c/i2c-mt65xx.yaml, GPL-2.0-only OR BSD-2-Clause; dt-schema/DTC existentes | Dois blocos MMIO, clock-div e clocks main/dma já descritos. Falta compatible nativo. Fallback comunitário MT8183 não representa offsets/MCU; candidato aceita somente1–400kHz e divisor1–8, sem have-pmic | Baixo: ampliar schema existente, não criar binding/validador paralelo. Validar positivo e negativos com dt-schema diretamente. Schema não escreve hardware e não autoriza bind/boot; fontes CCF/pinctrl/energia continuam gates físicos separados |

Guard offline permite somente os três executáveis dt-schema revisados no mesmo
ambiente do interpretador. Não abre Python arbitrário, rede ou transporte;
ausência de ferramentas/fontes gera skip explícito WSL/Linux, não fallback de
validação própria. Como antes para DTC/cc, guard é defesa adicional, não sandbox
para executáveis hostis nem isolamento herdado por subprocessos.

## Lifetime DMA MT6765 — antes da implementação (2026-10-25)

| Função | Alternativa / revisão / licença | Compatibilidade / efeitos | Recomendação |
| --- | --- | --- | --- |
| Memória de transferência | dma_alloc/free_coherent e barreiras DMA Linux6.18.58 commit2926d88bb7fc4608fd942453d929c39e4e5ec006 GPL-2.0-only; LG i2c-mtk.c do contrato já usa buffer coerente persistente | i2c_get_dma_safe_msg_buf pode retornar diretamente memória do chamador com DMA_SAFE. Apenas passar xferred=false não protege essa memória de DMA preso. LG remove libera sem comprovar quiescência, não copiar essa parte | Reutilizar alocação coerente persistente por controlador, TX/RX separados; copiar RX somente após sucesso/idle/sync. Não criar transporte ou allocator paralelo |
| Cancelamento / IRQ | completion, spin_lock_irqsave, synchronize_irq e polling limitado existentes; APDMA é canal dedicado por MMIO, não há provider DMAengine associado neste driver | dmaengine_terminate_sync não controla esse canal sem provider real. Máscara deve ser drenada antes de sync; acumular status tardio até parar DMA/START e só depois encerrar active. Nada de waits infinitos | Estender somente chip MT6765. Fazer erro/timeout/quiesce antes de liberar buffers; comparar caminho legado completo |
| Reset que não termina | DMA API não autoriza free enquanto dispositivo acessa memória; get_device/CCF existentes | Erro fatal retém uma alocação8KiB, referência device e referências de clock, bloqueia novos xfers/suspend; remove não tenta liberar memória incerta. Reboot é recuperação, não retry automático | Quarentena limitada por controlador, explícita no log; não garantir unload/PM normal após falha fatal. Guard continua NOT FOR PHONE até testes de lifetime e integração restantes |

postmarketOS usa essas APIs, não oferece política de cancelamento específica
para este canal LG. Qualcomm/EDL e DMAengine de outro IP não substituem reset
APDMA. Fonte completo torna REA desnecessário. O doador BMW/HM já auditado é
referência das operações, não prova de equivalência integral de teardown.
O delta novo deve preservar o patch de configuração e o transporte de recuperação.

Revisão v2: try_module_get no probe, antes da publicação, e module_put apenas
no descarte normal/erro inicial. Um pin adquirido somente durante erro fatal
poderia chegar depois do início do unload. Dispositivos nativos saudáveis
precisam de unbind antes de rmmod; a quarentena retém o pin e impede novos
probes nativos até reboot. Essa política experimental não equivale ao teardown
normal upstream e ainda não autoriza uso físico. Não requer instalar biblioteca,
outro framework DMA ou ferramenta nova.

## Variante I2C MT6765 — antes da implementação (2026-10-25)

| Função | Alternativa / versão / licença | Compatibilidade / efeitos | Recomendação |
| --- | --- | --- | --- |
| Transporte nativo | i2c-mt65xx.c Linux6.18.58 commit2926d88bb7fc4608fd942453d929c39e4e5ec006 GPL-2.0-only; i2c-core, DMA API, completion, CCF existentes | Reutilizar registro/transferências, não o adaptador FIFO de diagnóstico. Nova chip data MT6765 isolada; offsets/temporização não equivalem a MT8183. Probe/resume/reset escrevem hardware e não restauram snapshot | Candidato staging, sem perfil/DT ativo; primeiro aquisição em100/400kHz e mensagens WR/RD/WRRD, não prometer HS/SMBus completo |
| Temporização | i2c-mtk.c LG archive4d3f7766..., GPL-2.0-only, hashes no contrato; calculate_speed e trecho standard/fast set_speed disponíveis | Reaproveitar busca sample/step e cnt_constraint, duty45%, divisor espelhado, timeout2ms e EXT_CONF. Somente integração ao mtk_i2c atual; não outro controlador/framework. Não copiar falhas silenciosas ou extensões Android | Helper específico do IP doador, testes de equivalência contra função LG real; recusar entradas fora da primeira faixa suportada |
| Referência comunitária | adomerle/linux-mt6765 commit5be6e64697351f1f6b1397743ded815af54bcc4a, GPL-2.0-only, fonte baixado por URL imutável sem atualizar checkouts existentes | DT usa MT6765 com fallback MT8183; i2c-mt65xx não tem chip data MT6765 nem cnt_constraint/MCU_INTR específicos. Confirma endereços/IRQ/divisor, mas status de outra placa não prova todos os efeitos LG | Reusar topologia conferida, não copiar fallback para mascarar lacunas. postmarketOS aponta esse projeto, não um driver LG pronto. Qualcomm usa outro IP/transportes |

Pesquisa pública repetida nesta etapa encontrou a referência comunitária; a
inspeção do commit exato não revelou implementação específica que substitua a
adaptação. Projeto arquivado e branches móveis não serão usados como versão.
Fontes completas dispensam REA nesta etapa. DMA em timeout, ordenação antes de
unmap, IRQ tardia e remove continuam gates obrigatórios antes de teste físico;
não declarar o candidato pronto só por compilar configuração/tempo/IRQ.

## Callbacks CCF e integração I2C0 — antes dos testes (2026-10-25)

| Funcionalidade | Implementação aberta / revisão / licença | Compatibilidade / efeitos | Recomendação |
| --- | --- | --- | --- |
| Clocks main/dma | clk-mt6765.c + clk-gate/mux/pll.c e CCF Linux6.18.58 commit2926d88bb7fc4608fd942453d929c39e4e5ec006, GPL-2.0-only | I2C_AP→i2c_ck→i2c_sel→parent selecionado; AP_DMA→axi_ck→axi_sel. Registro de PLL_AO vira CLK_IS_CRITICAL e CCF chama prepare/enable. Prepare PLL escreve mesmo se herdado ligado; unprepare pode desligar parent compartilhado | Reusar CCF, não promover clock-lease próprio nem presumir registro passivo. Compilar callbacks reais com MMIO/regmap stub e registrar offsets/ordem, incluindo erro de escrita e reparent pendente |
| Mapa/configuração I2C | i2c-mt65xx.c upstream vs i2c-mtk.c/h LG archive4d3f7766..., GPL-2.0-only; DT do backup BMW | MULTI_DMA0xf8c não0x8c; MCU_INTR0x40, HW_TIMEOUT0x4c, TIMING bit0, divisor espelhado e regra cnt_constraint. Leitura touch63bytes já usa DMA no vendor, não cabe no ensaio FIFO de8bytes | Extensão mínima ao driver existente requer cobrir esses deltas e reset/IRQ. i2c-gpio é alternativa upstream de diagnóstico, não prova de suporte ao controlador nativo; não emprestar compatible MT8183 |

postmarketOS reutiliza CCF/I2C do kernel, não elimina diferenças do IP. Clocks
Qualcomm/RPMh têm outro controle de ownership e não substituem o MT6765.
Fontes completas disponíveis: REA não é necessário para estes callbacks.
Testes de interface host com funções reais e stubs não provam estado elétrico,
core CCF completo, concorrência nem restauração física. Não há novo driver,
bind, DT ativo, DMA/IRQ real ou escrita no telefone nesta etapa.

Correção staging admissível nesta revisão: clk_mt6765_apmixed_probe/top_probe
continuam com três/duas escritas diretas após of_clk_add_hw_provider falhar.
Adicionar retorno no ramo de erro já existente (GPL-2.0-only, mesmo commit),
sem alterar caminho de sucesso, arrays, clocks, reset ou bindings. Comparar as
funções reais antes/depois com registro stubado. Isso não desfaz efeitos dos
callbacks anteriores nem resolve o unwind completo das alocações/registro.

## Testes da extensão FT5446 — antes da execução (2026-10-25)

| Funcionalidade | Alternativa / revisão / licença | Compatibilidade / efeitos | Recomendação |
| --- | --- | --- | --- |
| Exercitar parser e identificação | ISR/identify reais de edt-ft5x06.c Linux6.18.58 commit2926d88bb7fc4608fd942453d929c39e4e5ec006 GPL-2.0-only; infraestrutura unittest/cc/patch já usada no projeto MIT | Compilar funções extraídas do original e do patch contra stubs regmap/input. Sem parser novo, sem dispositivo/transportes. Stubs não provam o core MT, concorrência, probe/remove ou hardware. Cobrir ID15 inclusive evento reservado, IDs10–14, palma, zero, pressão e falhas | Reusar funções reais e comparar traces legados; testes host para esta integração, futura cobertura no kernel deve usar KUnit, não criar biblioteca própria de parsing |

Os testes continuam offline; nenhuma escrita de PMIC/I2C/firmware, novo driver,
reset ou mudança de recuperação. Problemas encontrados devem corrigir somente
o caminho FT5446 staging e preservar o candidato anterior como histórico.

## Conferência binária BMW do touch — antes da análise (2026-10-25)

| Funcionalidade | Implementação / origem / licença | Compatibilidade / efeitos | Recomendação |
| --- | --- | --- | --- |
| Confirmar o doador FT5446 no backup real | ELF BMW já recuperado, GNU binutils e Ghidra12.1.4 Apache-2.0; reporter MIT K40sLkFunctions existente | Fonte HM não comprova binário BMW. REA6.5.0 tem registro alinhado, mas nenhuma ferramenta conectada nesta sessão; Windows P0 já recusou ARM. Analisar somente ft5446_irq_abs e reg_read no ELF de SHA conhecido, sem executar o alvo | Reutilizar reporter/decompiler; pequeno seed MIT com SHA, limites, prologue e assinaturas anotadas a partir do doador. Sem novo parser, driver, transporte ou acesso ao telefone |

O objetivo desta exceção focalizada à preferência por fonte é verificar que o
firmware BMW contém a rotina doadora, não reconstruir C já disponível. Tamanhos,
calls e instruções constituem evidência estática; igualdade parcial não prova
equivalência integral nem funcionamento físico da extensão upstream staging.

## Touch FT5446 LG — antes da extensão upstream (2026-10-25)

| Funcionalidade | Atual / alternativa aberta / versão / licença | Compatibilidade e efeitos | Esforço / recomendação |
| --- | --- | --- | --- |
| Contatos multitouch | LG touch_ft5446.c/h, GPL-2.0-only, fonte HM archive4d3f7766...; backup BMW configura LGE_TOUCH_FOCALTECH_FT5446 e contém ft5446_irq_abs. edt-ft5x06.c no Linux6.18.58 commit2926d88bb7fc4608fd942453d929c39e4e5ec006, GPL-2.0-only, já lê0x00/63bytes, offset3, passo6, X/Y12bits, evento2bits/ID4bits | LG interpreta bit4 de XH como palma e encerra em ID15; aceita IDs10–14 apesar de tdata[10], não copiar esse risco. Upstream não implementa palma desse firmware nem valida IDs antes de selecionar slot | Médio: estender driver existente com chip data FT5446, preflight de frame, INPUT_MT_DROP_UNUSED/sync_frame e pressão; nenhum parser/driver paralelo, alterações só no chip novo |
| Identificação | Upstream tenta EDT em0xbb e heurística vendor0xa8; fonte LG lê ID alto0xa3, versão0xa6 | Vendor ID não identifica modelo EDT no firmware LG. Rota FT5446 explícita lê família0x54 e versão, mantém GENERIC_FT para formato/regs. Família0x54 não prova sozinha modelo ou firmware compatível | Baixo: rota somente leitura para chip data novo; não executar bootloader/update nem copiar firmware de outro modelo |
| IRQ/reset/alimentação | Input MT/regmap/I2C/regulator/gpiod mainline; GPIO/EINT/clock/pinctrl MediaTek e DT BMW | Backup: I2C0/0x38, IRQ GPIO1 com flags vendor0x2002, reset164 físico ativo baixo e VCL GPIO27. Não copiar flags IRQ vendor nem reset-gpio flags0 como bindings modernos. max_x/y719/1559 prevalecem sobre propriedades FocalTech genéricas antigas480x854 | Alto: separar da extensão de protocolo. Não criar node ativo ou forçar compatible de FT5426. I2C0/clock/EINT/supplies precisam integração própria |
| Probe/remove/PM | edt-ft5x06.c pinned: enable iovcc depois vcc, GPIO reset, leitura identificação/defaults, escrita de parâmetros somente se propriedades presentes, pedido IRQ; remove debugfs e devres IRQ/regulators; suspend escreve PMOD e pode desligar alimentação | Ordem de alimentação/reset LG não comprovadamente equivalente; dummy regulator não substitui GPIO27. debugfs/sysfs existentes podem escrever configuração. Nenhum novo efeito elétrico autorizado por essa compilação | Não habilitar bind/autoload antes da auditoria elétrica/clock e ensaio temporário. Preservar kernel/DT/recuperação atuais |

Pesquisa upstream encontrou discussão original de2022 sobre FT5446 próximo de
FT5426 e atraso de inicialização, não prova de suporte ao firmware LG:
https://lists.openwall.net/linux-kernel/2022/12/02/585 . postmarketOS reutiliza
input/DT e não fornece aqui um provider diferente comprovado. Qualcomm usa o
mesmo protocolo FocalTech em alguns aparelhos, mas suas GPIO/I2C/energia não
se transferem ao MT6762. Fontes completas estão disponíveis; REA não é necessário
para reescrever o parser e não vamos descompilar onde já há fonte.

Patch novo será staging GPL-2.0-only, sem perfil/DT ativo. Testar ISR/identificação
reais, trajetos legados com flag false, IDs inválidos/sentinela/palma/pressão,
erro de transporte e estado de slots. Tipos de framework nos testes são stubs,
não prova de pinagem/IRQ, qualidade de toque ou equivalência integral LG.

## Integração física temporária da bateria por demanda — 2026-10-25

| Função | Implementação reutilizada / revisão / licença | Efeitos / limites | Recomendação |
| --- | --- | --- | --- |
| Pacote/permit/coleta/restauração | prepare-rootfs, host-once-gate/ledger, run-verified e advance existentes em adc7895, MIT; scripts initramfs existentes | Acrescentar opção exclusiva e hook com hashes, somente SSH/atomic/host-once. Ciclo lts-auto-cycle.py, DA, reset e endereços permanecem byte-idênticos. Novo resultado validado pelo wrapper após coleta | Reutilizar pipeline, não novo transporte ou ciclo |
| Ensaio da variante contínua | power_supply/sysfs e hook shell no estilo battery-coulomb/telemetry, mesmo projeto/revisão MIT | 18 rodadas V/I/T com sleep1, descarrega módulo, sem outros ADC/FG. Cabe no permit25s nas durações anteriores (~0.24s/captura); atraso pode reprovar e segue restauração, nunca aumentar timeout/repetir automaticamente | Teste curto de integração, não soak de confiabilidade nem prova contra firmware externo |

Verificador adicional deve limitar todos os marcadores CONTINUOUS ao intervalo
do token, conferir18 rodadas ordenadas/unidades/faixas, tentativas>=18, fault0,
ausência de FAIL e retirada da interface. O verificador legado não conhece o
prefixo novo; não tratá-lo como prova suficiente. Nenhum módulo novo nesta etapa.
Init recebe somente callback condicional de três linhas e o validador host-once
recebe o nome desse hook em duas listas. Esses dois arquivos não ficam
byte-idênticos: teste inverte exatamente esses três hunks e exige o SHA original
para todos os bytes restantes, sem atualizar baseline. Ciclo/DA/registry ficam
inteiramente byte-idênticos. Ausência do hook conserva o caminho legado.

## Bateria contínua por demanda — antes da implementação (2026-10-25)

| Funcionalidade | Atual / alternativa aberta / revisão / licença | Compatibilidade e efeitos | Esforço / recomendação |
| --- | --- | --- | --- |
| Publicação contínua V/I/T | power_supply e drivers/power/supply/generic-adc-battery.c, Linux6.18.58 commit2926d88bb7fc4608fd942453d929c39e4e5ec006, GPL-2.0; módulo V/I/T próprio finito408bd6f GPL-2.0-only | Generic ADC requer providers IIO de tensão/corrente/temperatura já calibrados. Não faz latch FG/compensação LG; publicar três canais ADC brutos não equivale. postmarketOS usa essas APIs, Qualcomm FG tem outro mapa/firmware | Médio: reutilizar power_supply e captura LG já existente; nova variante por demanda sem expiração global/limite de tentativas, não framework paralelo |
| Aquisição hardware/calibração | telemetry-capture, current-sequence/decode, temperature-window500/model, NTC e BATADC existentes, GPL-2.0-only; doador LG auditado contra cinco funções BMW | Não mudar sete comandos por captura nem calibração. Cache com CLOCK_BOOTTIME inclui suspensão; origem monotônica interna do bundle não será misturada com cache. Sem worker/novos comandos PMIC, sem retry após falha e sem thermal/charger | Baixo: incluir headers existentes sem copiar algoritmos; disponibilidade ilimitada não significa dados frescos comprovados contra firmware nem uso de segurança |
| Ciclo de vida | power_supply_register/unregister, device_lock e referências OF/devices do kernel atual | Primeira captura antes de register; falha de register libera referência. Exit bloqueia getters antes de unregister e só então put_device. Requisições inválidas não adquirem hardware. Sem callback periódico/worker para cancelar | Baixo: adaptar cola existente em variante separada, preservar fontes/binários das versões15s/30s; não substitui futuro driver MFD/PM/runtime-PM completo |

Variante opt-in de laboratório, sem autoload, sem registro no ciclo físico nesta
etapa. Probe/init pode fazer aquisição (sete escritas de requests/latch, não
charger/reset), não é leitura passiva. Remove apenas retira interface; nenhuma
tentativa de reset/reparação. Falhas impedem amostra velha e novas aquisições.
Não iniciar hardware só para cumprir auditoria. Não exigir corrigir canais
upstream irrelevantes antes de integrar as sequências específicas já testadas.

## Kernel do backup BMW como referência binária — 2026-10-25

| Função | Alternativa aberta / versão / licença | Compatibilidade / limites | Recomendação |
| --- | --- | --- | --- |
| Extrair boot original | AOSP unpack_bootimg.py já presente em tools/aosp-mkbootimg; Apache-2.0 | Lê boot v2, materializa componentes em diretório novo, não executa kernel nem escreve no telefone. Identidade por SHA do boot instalado, nunca pelo zImage recompilado HM | Reutilizar ferramenta, sem novo parser |
| Recuperar símbolos/ELF | marin-m/vmlinux-to-elf1.4.0, https://github.com/marin-m/vmlinux-to-elf, commit29eac31a38db48b51c0dc6aae3be0162237601eb, GPL-3.0-or-later conforme pyproject.toml | Suporta ARM e kernels4.9 com kallsyms; recuperação heurística não dá fonte C/debug nem prova endereços sem checar mapeamento. Apenas host offline | Instalar isolado, usar para localizar funções BMW e comparar com doador LG antes de portar |
| Descompilar cinco funções | Ghidra12.1.4 Apache-2.0 e scripts K40sLkFunctions já existentes; API DisassembleCommand/Function.setBody | REA6.5.0 recusou ELF ARM no Windows P0; usar headless direto já validado para análises ARM anteriores. Script pequeno só ancora SHA/base/prologue e limita cinco corpos pelos símbolos adjacentes; sem autoanálise global, execução do alvo ou mudança no backup | Reutilizar decompiler e reporter existentes; novo seed estritamente específico do artefato, não novo motor/parser |

Linux scripts/extract-ikconfig e GNU readelf/nm/objdump disponíveis também
devem ser preferidos a extratores/disassemblers próprios. Não criar novo
driver nesta etapa. REA doctor informou registro Codex alinhado, sem ferramentas
conectadas; nenhuma configuração alterada. Evidências desta rota são de
ferramentas shell, não Evidence REA. postmarketOS/Qualcomm não substituem o
formato boot/kallsyms do backup MediaTek. Saída extraída fica privada/ignorada.

## ABI e remoção IIO — antes dos testes de exposição (2026-10-25)

| Funcionalidade | Atual / alternativa aberta / commit / licença | Compatibilidade / efeitos | Esforço / recomendação |
| --- | --- | --- | --- |
| Nomes/permissões sysfs | industrialio-core.c, __iio_device_attr_init, Linux6.18.58 commit2926d88bb7fc4608fd942453d929c39e4e5ec006, GPL-2.0-only | O core deriva nomes de tipo+ID DT, não da posição no array ou scan_index. RAW tem efeito físico mesmo com modo0444. Label e escala não fazem aquisição neste driver | Baixo: compilar a função real com as tabelas reais, não inventar API/nome novo nem varrer todos os arquivos raw no telefone |
| Unregister/devm | Mesmo core, iio_device_unregister e __devm_iio_device_register; devres Linux padrão | Remove interface e invalida info; não restaura PMIC nem elimina request deixado por falha de stop. Sem callback remove específico no ADC. Locks/sysfs sincronizam interfaces, não masters GPS/MD | Baixo: verificar sequência real com stubs; não adicionar remove que escreva banco inteiro/reset. Falha de limpeza permanece bloqueio para teste físico |
| Aquisição limitada da bateria | Driver upstream MediaTek + dez patches auditados; API iio_read_channel_processed_scale (inkern.c, mesma revisão/licença) | Somente BATADC e BAT_TEMP são candidatos iniciais; demais canais não devem ser lidos por varredura. Nenhum consumer contínuo ativado. power_supply/NTC permanecem consumidores separados | Médio: contrato explícito da variante física, sem supor que arquivos read-only sejam passivos |
| Stop ordinário com erro | read_adc do mesmo driver já invalida amostra e marca timed_out; read_imp já guarda cleanup_error | Latch reset_error existente deve guardar primeiro erro de stop somente sob shared_reset, antes de retornar erro primário da amostra. Aquisição seguinte falha antes de I/O; SCALE continua metadado. Nenhuma escrita nova, probe/remove/reset ou outra política alterada | Baixo: estender latch existente em patch staging separado; testar falhas antes/depois de commit, erro primário+cleanup e paridade não compartilhada. Não inventar retry/reset/remove reparador |

Referência ABI primária: [documentação IIO Linux](https://kernel.org/doc/html/v6.18/admin-guide/abi-testing.html).
postmarketOS reutiliza a ABI/kernel; nenhum framework de distribuição corrige
essas tabelas MediaTek. Drivers Qualcomm têm outros PMICs/regmaps e não são
substitutos. A fonte disponível basta; REA não agrega prova neste caso.
Fixture host testa nomes/permissões e ordem de teardown, não concorrência real,
acesso ao PMIC, rollback ou compatibilidade elétrica. Manifesto de exposição
registra13 canais e impede que o sucesso do build seja tratado como aprovação.

## MFD/DT opt-in para IIO real — antes da integração (2026-10-25)

| Função | Atual / alternativa aberta / revisão / licença | Compatibilidade e efeitos | Esforço / recomendação |
| --- | --- | --- | --- |
| Criar filho ADC real | mt6397-core.c Linux6.18.58 commit2926d88bb7fc4608fd942453d929c39e4e5ec006 GPL-2.0-only já tem cell mt6359-auxadc/mediatek,mt6357-auxadc; gate K40S0018 só cria regulador sem IRQ | Reutilizar devm_mfd_add_devices e OF child. Novo Kconfig default n + token auxadc-v1 + gates board/BROM existentes + único child compatível/ativo. Array apenas regulator+ADC; sem recursos IRQ, RTC, keys, charger ou reset novo | Médio: estender gate existente, não fabricar platform_device/compat nem provider paralelo |
| DT do teste | DTS USB/eMMC validado + binding upstream mediatek,mt6359-auxadc.yaml (GPL-2.0 OR BSD-2-Clause) | Incluir DTS base e acrescentar apenas adc compatible e #io-channel-cells=1 sob PMIC real. Sem IRQ/calibração/mux novo. Checar DTC/libfdt e schema ADC; isso não certifica todo o DT de bringup | Baixo: reutilizar base e binding, invariantes próprias só para delta estrutural/gates |
| Build explícito de staging | kernel-workspace.py MIT já tem prepare/configure/build isolados e boot_policy forbidden | Permitir paths staging somente com staging_integration=true, mantendo board_support=false/boot proibido. Perfil IIO separado incorpora patches por hash sem duplicá-los. Guard de staging aceita apenas esse perfil offline explícito; defaults/registry/series automáticas seguem vedados | Médio: extensão do orquestrador, não novo builder/flash/transporte |

Provider IIO usa os dez candidatos auditados, inclusive shared_reset. Compilar
como módulo, nunca built-in/autoload antes do permit do laboratório. Neste lote
somente preparar/build offline; registro fechado de kernels e recuperação não
mudam. Exposição/ABI e callbacks ainda precisam política antes de teste físico.
postmarketOS fornece exemplos/frameworks MFD/DT; Qualcomm/REA não substituem
esta topologia conhecida. Testar gates e OF refs com C real, equivalência do
prefixo MFD com flag nova desligada via preprocessor GNU, config/patch/profile
identidades e ausência de escritas/filhos extras. Preservar0018 e o atomic.

## Reset compartilhado MT6357 — antes do décimo candidato (2026-10-25)

| Função | Implementação / alternativa / origem / licença | Compatibilidade e efeitos | Esforço / recomendação |
| --- | --- | --- | --- |
| Probe sem tomar reset global | Estender chip data e probe do mt6359-auxadc.c Linux6.18.58 commit2926d88bb7fc4608fd942453d929c39e4e5ec006, GPL-2.0-only; LG4.9.190 pmic_auxadc_chip_init não faz reset global incondicional | MT6357 possui reset, mas wk_auxadc_reset recompõe requests CH7/GPS; pulsá-lo isoladamente afeta recursos fora deste provider. Capability privada shared_reset só MT6357, distinta de no_reset. Probe apenas lê0f90 e exige registro inteiro zero/sem erro antes de registrar IIO; não só bits0/3 do pulso upstream | Médio: preservar handoff do firmware, não inventar no_reset nem novo parâmetro/binding DT |
| Recuperação após timeouts | Mesmo driver, guard mutex e latch reset_error já existentes | Primeiro timeout mantém história; repetição MT6357 trava aquisições com ETIMEDOUT, sem escrever reset/GPS nem retry. Reset helper recusa EPERM sem I/O mesmo chamado diretamente. Outros modelos preservam política anterior | Baixo: usar estado existente; SCALE segue metadado. Reprobe explícito não equivale a recuperação física comprovada |
| Reset framework | Documentation/driver-api/reset.rst, mesmo Linux, API reset_control_get_shared/exclusive | Contagem de referências coordena consumidores que usam o controller Linux; não contabiliza masters MD/GPS externos. Não há provider reset-controller AUXADC MT6357 integrado aqui | Não criar controller/shim fictício: referência compartilhada do Linux não prova posse contra firmware |

Provas anteriores: fonte LG fixa na auditoria de canais, ensaio BATADC/AP LTS
`mt6357-batadc-ap-lts-verification-20261025.json` mostra aquisição pelo handoff
sem reset de ADC. Não prova que todos os canais funcionem nem a posse do PMIC.
postmarketOS usa esses frameworks; Qualcomm/REA não substituem a evidência
MediaTek disponível. Testar reset/probe/read_raw reais, erro/ocupado no probe,
timeouts e bloqueio sem I/O, preservação de modelos não compartilhados e
nenhuma mudança em tabelas/DT/séries. Compilar ARM32; sem bind físico neste lote.
Exigir zero é a política conservadora já usada pelo ensaio finito: bits1/2/4/5
etc. também pertencem a resets no header LG. Estados reservados não zero de
outras placas podem ser recusados; compatibilidade universal não é alegada.

Bloqueio adicional confirmado: kernel atomic usa
CONFIG_MFD_MT6397_K40S_REGULATOR_ONLY=y. Não criar filho ADC falso nem desativar
essa proteção para conseguir teste verde. Integração física exigirá variante
opt-in de MFD/DT com revisão de exposição de canais, mantendo recuperação atual.

## Comparação BATADC/AP no LTS — antes da instrumentação (2026-10-25)

| Função | Existente / origem / licença | Compatibilidade / efeitos | Recomendação |
| --- | --- | --- | --- |
| Comparar saída genérica/AP durante um request finito | Ensaio k40s-battery-adc já validado, GPL-2.0-only; regmap Linux6.18.58 commit2926d88bb7fc4608fd942453d929c39e4e5ec006; mapa LG fixado10b6 | Acrescentar duas leituras10b6, antes do SET e depois do poll genérico. Exatamente as duas escritas originais1110/1112 bit0, mesmo timeout/unwind/checks. Não carregar provider IIO staging, que ainda tem reset/ownership pendentes | Patch observacional sobre cópia de build do ensaio, sem módulo/driver paralelo nem modificar fontes/artefatos históricos |
| Build e pacote | build-k40s-battery-snapshot.py, prepare-k40s-rootfs-test.py e advance-k40s-lts.py MIT do projeto | Novo modo opt-in isolado, hash de fonte original+patch+ko+kernel; output novo, sem sobrescrever v2. Exigir SSH/atomic/host-once e impedir combinação com outros escritores | Estender fluxo existente; lts-auto-cycle.py, init, hooks, gate, token e recuperação permanecem byte-idênticos |
| Evidência da comparação | Decodificador de logs e runner verificado existentes MIT; re/json/unittest da stdlib Python (PSF) | Marker próprio com os quatro valores e extra_reads=2/extra_writes=0/fresh_proven=0; validar somente após ciclo aprovado/retorno/A-B. Igualdade é observação, não requisito nem prova de freshness | Pequeno parser específico junto da orquestração existente, não novo transporte/decoder/framework. Nunca rejeitar conversões só por igualdade nem inventar baixa de RDY |

Mainline/postmarketOS IIO não fornece esse relatório de regressão específico;
Qualcomm/REA não substituem fonte e regmap disponíveis. A instrumentação não
reimplementa aquisição: só observa o ensaio existente enquanto a substituição
IIO é preparada. Manter fontes v1 e artefatos v2 intactos; testes devem verificar
as mesmas escritas e cleanup em cada erro novo. Falha de leitura AP depois do
SET deve ir obrigatoriamente ao cleanup original. Pode registrar RDY baixo/AP
diferente: resultado do ensaio, não falha artificial da aquisição genérica.
Não executar ciclo físico antes de compilar, testes offline e checagens do
pacote. Classificação: compilação C/offline; execução no telefone é escrita
temporária de boot/request com recuperação obrigatória, nunca "read-only".

## Erros do callback de impedância — antes do nono candidato (2026-10-25)

| Função | Atual | Alternativa / origem / licença | Efeitos e limites | Recomendação |
| --- | --- | --- | --- | --- |
| Start/read/stop MT6357/MT6358 | mt6358_read_imp ignora falhas das duas configurações iniciais, leitura de resultado e quatro operações de stop | Estender as três funções existentes no mt6359-auxadc.c Linux6.18.58 commit2926d88bb7fc4608fd942453d929c39e4e5ec006 GPL-2.0-only; regmap e latch privado já existente | Sequência normal preservada. Primeiro erro prevalece; stop tenta todas as quatro operações mesmo após erro; amostra não publicada se read/stop falhar. Falha no primeiro setup tenta apenas desfazer DCM; após tentativa de IMP1, stop completo é necessário pois transferência pode ter cometido | Corrigir funções existentes, sem provider/daemon/state machine novo |
| Estado incerto após cleanup | Próxima chamada pode continuar após stop falho | Reusar reset_error como latch de falha de recuperação, já verificado sob mutex de read_raw | Cleanup falho registra latch; futuras aquisições recusadas antes de I/O. Não executar reset automático se o latch já indica estado incerto; leitura atual mantém erro primário | Estender a semântica documentada do campo, não duplicar estado. SCALE continua metadado; somente reprobe explícito pode liberar nova instância |

Auditar fonte upstream é suficiente para falhas ignoradas, sem REA nem driver
alternativo Qualcomm/postmarketOS. Referência LG não torna os bits IMP CLEAR
fisicamente seguros. Não habilitar esse callback por causa dos testes. Sem
alterar outros callbacks, DT, tabelas, endereço IMP ou sequência normal.
Testar funções reais com regmap antes/depois de possível commit, erro duplo,
sentinelas vbat/ibat, cleanup completo e ausência de reset/retry após latch.
Teste é na fronteira da API, não equivalência física de bits/masters. Código
novo limita-se a propagar retornos/unwind e usar estado já existente.

## Observação passiva das saídas AP no kernel conhecido — antes da coleta (2026-10-25)

| Função | Alternativa existente / origem / licença | Compatibilidade e efeitos | Recomendação |
| --- | --- | --- | --- |
| Comparar registradores genérico/AP sem outro driver | pmic_access do vendor LG4.9.190, upmu_debugfs.c GPL-2.0-only SHA837463edc0cfcdb4f6183677521d4eb86d6308c73ab8ad89f0cd7e3b2b5a7f89; upmu.c SHAc68ef2daedd6d59ee4b523c154929a6b07c8e1a50bbb69f4d0b2027502d1d81e | store com somente um token hex sem espaço seleciona pmic_read_interface; dois tokens chamam pmic_config_interface e são PROIBIDOS nesta coleta. pmic_read_device usa pwrap_read, sem pmic_write. show retorna valor global salvo; store ignora status de erro e pode haver corrida com outro leitor | Reutilizar SSH autenticado e interface existente; sem nova ferramenta/módulo, insmod, acesso bruto I2C, trigger, reset ou flash |

Limitar seleção a quatro dígitos hex sem espaço/newline:0f90,110e,1114,
1088,10b6,108a,10ba,108c,108e. São controles de request/reset e saídas ADC já
auditados; não fazer dump integral. A escrita de seleção no sysfs NÃO deve
conter valor de registrador; é comando ao driver para ler, não escrita no PMIC.
Não ler atributos IIO raw/input aqui: eles iniciam conversões e podem acionar
reset no timeout. Três passagens finitas, sem trigger próprio. Dados são
observações passivas sob os masters do kernel4.9, não prova de conversão nova,
atomicidade/coerência V/I/T ou validade do driver6.18. Ler dmesg filtrado para
detectar erros reportados; ausência deles não corrige status ignorado/corridas.
Guardar prova fora de firmware/backups e conservar caminho de recuperação.

## Saídas AP e dados de tensão MT6357 — antes do oitavo candidato (2026-10-25)

| Funcionalidade | Atual | Alternativa / origem / licença | Compatibilidade e efeitos | Esforço | Recomendação |
| --- | --- | --- | --- | --- | --- |
| BATADC para consumidor IIO | ADC0 genérico1088,15bits,ratio3/1; captura finita v1 também usa1088 | Dados do provider IIO existente Linux6.18.58 commit2926d88bb7fc4608fd942453d929c39e4e5ec006 GPL-2.0-only; saída AP PMIC_AUXADC_ADC_OUT_CH0_BY_AP10b6 no header LG fixado | Índice compacto23 resulta10b6; ID DT, label, bits, ratio e requestbit0 preservados. Referência LG não comprova equivalência da saída genérica com AP na placa BMW | Baixo | Candidato de dados somente, não substituir captura v1 ou ativar driver; comparação física entre saídas permanece necessária |
| ISENSE como tensão do sense | ADC1 genérico108a,12bits,CURRENT e requestbit0 | Mesmo provider; LG map seleciona CH1_BY_AP10ba,15bits e requestbit1; common retorna IIO_VOLTAGE | Índice compacto25 resulta10ba. Não publicar leitura bruta como corrente; unidade de corrente continua responsabilidade de calibração/FG. Tipo muda nomes sysfs | Baixo | Corrigir conjuntamente saída/resolução/tipo/request, preservar ratio3/1 e avg128, exigir revisão ABI |
| VCDT como tensão | Endereço108c correto, mas TEMP e requestbit0 | Mesmo provider e header/map LG: tensão12bits,requestbit2 | Não precisa novo driver, mux, calibração ou escrita de probe. Tipo muda ABI; tensão não mede temperatura | Baixo | Corrigir tipo/request apenas; preservar demais metadados e todos os outros canais/PMICs |

Proveniência e macros compiladas constam em
`manifests/mt6357-auxadc-channel-audit-20261025.json` (quatro hashes LG,
GPL-2.0-only, referência HM4.9.190, não equivalência física BMW). Reutilizar
IIO/regmap e estender apenas dados MT6357; não portar provider Android nem
adicionar shim. postmarketOS/bindings/frameworks Qualcomm/REA não substituem
essas particularidades documentadas do PMIC. Nenhuma rotina nova de
probe/remove/transportes; algoritmos de aquisição/reset inalterados. Testar
tabelas reais de antes/depois, identidade DT, preservação dos demais canais e
PMICs, e compilar ARM32. DCXO/mux, VDCXO, impedância, ownership e freshness
continuam bloqueando ativação: corrigir três canais não resolve o provider todo.

## Mapa completo e freshness AUXADC — antes de novas correções (2026-10-25)

| Função | Atual | Alternativa / origem / licença | Compatibilidade e efeitos | Esforço | Recomendação |
| --- | --- | --- | --- | --- | --- |
| Descritores MT6357 | Sete candidatos corrigem escala/erros/aliases, não garantem o mapa inteiro | Tabelas mt6359-auxadc.c do Linux6.18.58 commit2926d88bb7fc4608fd942453d929c39e4e5ec006 GPL-2.0-only; mapa do driver LG4.9.190 e upmu_hw.h GPL-2.0-only, hashes nos manifests anteriores | Endereço ADC não é número de canal físico: enumeração vendor contém lacunas. BATADC AP e ISENSE AP têm saídas dedicadas; DCXO usa mux; VBAT usa callback de impedância | Médio | Comparar tabela/macro reais compiladas com referência completa, sem novo provider nem trocar endereços pelo nome do ADC. Não corrigir apenas requestbit |
| Garantia de conversão nova | Poll RDY alto após request e atraso | Caminho IIO upstream e get_auxadc_out LG usam RDY alto; polling MDRT vendor observa baixo→alto apenas em outro monitor/caminho | Não existe garantia temporal transferível automaticamente para BATADC. Valores iguais podem ser conversões novas; RDY sempre alto também pode representar cache no modelo adversarial | Alto, depende de documentação | Teste negativo no fixture existente; não criar detector próprio por diferença de valor, nem impor RDY baixo sem especificação |
| Reset e coexistência GPS | Upstream assert/deassert simultâneo bits0/3 | wk_auxadc_reset LG pulsa bit0 depois bit3 e refaz requests CH7/GPS DCXO | Header identifica nomes dos bits; sequência e efeitos de múltiplos masters não equivalentes. Restaurar requests GPS por cópia seria nova escrita não autorizada | Alto | Preservar bloqueio físico; nomes documentados reduzem incerteza, não provam reset seguro/rollback |

Referência LG LMX430HM não comprova equivalência total à placa BMW. Source DT
mt6357.dtsi SHA c1a1a9b5f2c7a9d998b789d3700c4d62c4572974701f037e06cedcc117b81a2b
GPL-2.0-only fornece resolução/ratio/avg com defaults do common, não confirmação
da configuração efetiva do telefone. postmarketOS reutiliza bindings/IIO; não
resolve este mapa por um framework adicional. Código Qualcomm e ferramentas
REA não substituem fontes MediaTek disponíveis. Reutilizar cc/unittest e o
fixture regmap já existente para a auditoria, não adicionar driver/ferramenta
de aquisição. Nenhum novo efeito de probe/remove ou escrita física permitido.

## Erros de reset AUXADC — antes do patch (2026-10-25)

| Função | Atual | Alternativa / origem / licença | Compatibilidade e efeitos | Esforço | Recomendação |
| --- | --- | --- | --- | --- | --- |
| Propagar falhas do reset | mt6359_auxadc_reset void ignora todos os retornos regmap; probe pode registrar IIO após falha | Estender a função e os dois callers do driver existente, Linux stable6.18.58 commit2926d88bb7fc4608fd942453d929c39e4e5ec006, GPL-2.0-only, ADC SHA74b50fc1602bbf9a180950c77485ad687818e0385e5154b60ed99a876d2eb146 | Reutilizar regmap e dev_err_probe; não novo provider. Tentativa de assert exige deassert mesmo se transferência falhou após commit; tentativa de unlock exige relock. Preservar primeira falha | Médio | Reset retorna int; probe falho não publica IIO; no_reset legítimo mantém zero I/O. Não marcar MT6357 como no_reset |
| Falha de recuperação em runtime | timed_out sozinho permite futuras tentativas mesmo após reset desconhecido | Pequeno erro latched privado ao mesmo driver, sob mutex existente | Retornar timeout original na leitura que falhou, registrar falha do reset e bloquear aquisições seguintes sem I/O até reprobe explícito; SCALE continua metadado | Baixo | Não adicionar daemon, tentativas automáticas ou máquina de estados paralela. Novo campo reset_error é estado mínimo da falha; não certifica rollback físico |

postmarketOS não oferece outra posse de PMIC; Qualcomm/REA não substituem fonte
MediaTek disponível. Testar funções reais reset/read_raw/probe com stubs de
framework/regmap: falha antes/depois de commit em unlock/assert/deassert/relock,
erro duplo e prioridade, registro IIO só após sucesso, bloqueio da leitura após
recuperação falha. Mesma sequência normal de escritas, sem retry. Não escrever
mais registros em caso de unlock falho além da tentativa de relock. NENHUM
resultado autoriza reset no telefone: bits0/3 continuam sem finalidade totalmente
documentada; prova de amostra nova/RDY é independente e continua pendente.

## Requests MT6357 por aliases — antes do patch (2026-10-25)

| Funcionalidade | Atual | Alternativa / revisão / licença | Compatibilidade e efeitos | Esforço | Recomendação |
| --- | --- | --- | --- | --- | --- |
| Preservar requests de outros canais | Driver IIO escreve banco inteiro e zero; ensaios K40S usam SET/CLR | Estender dados MT6357 e chamadas regmap_write/read já existentes, mesmo Linux stable 6.18.58 commit 2926d88bb7fc4608fd942453d929c39e4e5ec006, GPL-2.0-only | upmu_hw.h LG SHA ce55730f6a0b1201e25084e9a6c17e4778946105e6d4683b5e7490696ab51855: RQST0/SET/CLR=110e/1110/1112; banco1114/1116/1118. SET/CLR +2/+4 e máscaras por canal documentados. Não confundir nome upstream RQST1 com RQST2 do vendor | Médio | Capability privada só MT6357; usar aliases para máscara, não RMW próprio; outros PMICs mantêm sequência atual |
| Recusar canal já requisitado | Ensaio finito recusa banco ocupado; upstream sem pré-checagem | regmap_read e -EBUSY padrão, mesmo driver | Ler o banco antes de qualquer request/cleanup; se próprio bit ocupado ou erro, não escrever nem limpar. Outros bits preservados | Baixo | Pré-checagem fail-closed, sem tratá-la como posse atômica |

Proveniência LG: archive SHA4d3f77663a1839d5c9ffd53ee040e6c95eff0f6fd41605762dba7b77ce6017c8,
kernel4.9.190 GPL-2.0, header de registradores; pmic_auxadc.c SHA
4e1e52c836632619baf954d7311ee4c32da3f7c951e93555b239ed41c0a4b54d
contém requests AP/MD/GPS e calibração/monitoramento compartilhados. Não assumir
que mutex Linux exclui esses agentes. postmarketOS/Qualcomm não fornecem posse
universal de PMIC; regmap_field RMW também não resolve concorrência externa.

Não adicionar daemon, API ADC ou driver paralelo. Testar bancos110e/1114,
sucesso/falhas antes/depois de commit, bit já ativo, erro de pré-leitura e
atividade concorrente em outro bit. Demonstrar também a corrida no MESMO bit
entre read e SET: continua bloqueador físico. READY antigo/freshness e resets
não são resolvidos por aliases. Capability falsa deve conservar o caminho
anterior; nenhuma mudança em probe/remove. Só staging, sem imagens/telefone.

Revisão de tabela antes da integração: canais como VDCXO aparecem na tabela IIO
MT6357 sem desc preenchido. Um desc zero não é um request válido. O candidato
deve rejeitar máscara zero e índices fora de RQST0/RQST1 antes de qualquer I/O,
com -EOPNOTSUPP. Isso evita aplicar offsets SET/CLR sobre ADC0 acidentalmente;
não é prova de compatibilidade dos canais restantes. Validar com função real
read_adc e descritores inválidos, sem criar validador/driver paralelo.

## Tipos/unidades AUXADC e consumidor — antes do patch (2026-10-25)

| Funcionalidade | Atual | Alternativa / origem / licença | Compatibilidade e efeitos | Esforço | Recomendação |
| --- | --- | --- | --- | --- | --- |
| Tipo BATADC/BAT_TEMP | Upstream anuncia RESISTANCE/TEMP apesar de RAW e escala de tensão | Corrigir somente dois descritores MT6357 no mt6359-auxadc.c, Linux stable 6.18.58 commit 2926d88bb7fc4608fd942453d929c39e4e5ec006, GPL-2.0-only | BATADC 15 bits/5400mV e BAT_TEMP 12 bits/1800mV; preservar IDs DT, labels, endereços e resoluções. Mudam nomes sysfs derivados do tipo: alteração ABI candidata, não aprovada upstream | Baixo | IIO_VOLTAGE para esses dois canais apenas, sem conversão NTC em ADC nem alterar os demais PMICs |
| Conversão mV/uV para consumidores | Diagnósticos próprios multiplicam/dividem raw | iio_read_channel_processed[_scale], iio_convert_raw_to_processed_unlocked e iio_multiply_value, mesmo Linux, inkern.c GPL-2.0-only SHA efe82f50976cc73251d86669bb02cc9c71e4978b05af84f8f9eb5cfa567f3115 | API scale=1000 preserva frações de mV ao gerar uV; scale=1 mantém truncamento em mV usado pelo modelo NTC LG. Sem novo wrapper de conversão | Baixo | Testar funções reais e usar API padrão no consumidor futuro; SCALE corrigida é pré-requisito |
| Consumidor bateria/NTC pronto | Capturas finitas e calibração LG | generic-adc-battery.c, ntc_thermistor.c e APIs IIO/power_supply, mesmo commit Linux, licenças por arquivo | generic-adc-battery multiplica mV já truncado por1000; não prova compensação NTC/corrente, SOC nem janela V/I/T. ntc_thermistor exige IIO_VOLTAGE e já usa processed_scale1000, mas tabela LG68k/62k e calibração não são intercambiáveis por nome | Médio | Reutilizar APIs/aquisição; não habilitar esses consumidores como substitutos completos sem equivalência |

Fonte LG disponível confirma processed como tensão (raw * razão *1800 >>bits)
e calibração posterior de BAT_TEMP. Não portar o driver Android inteiro.
postmarketOS usa bindings/frameworks candidatos; Qualcomm não substitui esta
pinagem/PMIC. Nenhuma ferramenta REA necessária havendo fonte. Tipos e API não
alteram probe/remove/reset/request, portanto não resolvem ownership. Patch só
staging; compilar driver completo e testar tabela real, IDs, tipos e unidades,
erros de leitura sem publicar amostra e todos os códigos 12/15 bits.

Revisão complementar de `thermal-generic-adc.c` e binding generic-adc-thermal:
sem tabela assume milliCelsius; com tabela interpola e clampa extremos. Isso não
equivale à rejeição de circuito inválido nem à compensação NTC/corrente LG.
Não trocar modelo por tabela genérica sem prova de erros e unidades. Fonte
ntc_thermistor.c é GPL-2.0-or-later; thermal-generic-adc.c GPL-2.0-only no commit
fixado. Scope deste lote continua aquisição IIO, não temperatura final ou SOC.

## Serialização AUXADC — antes do patch (2026-10-25)

| Funcionalidade | Atual | Alternativa / origem / licença | Compatibilidade e efeitos | Esforço | Recomendação |
| --- | --- | --- | --- | --- | --- |
| Serializar aquisição, recuperação e timed_out | scoped_guard cobre só aquisição; reset/atualização ficam fora | guard(mutex), include/linux/cleanup.h e mutex.h, Linux stable 6.18.58 commit 2926d88bb7fc4608fd942453d929c39e4e5ec006, GPL do kernel por arquivo; driver GPL-2.0-only | Mesmo mutex existente, escopo até todo return do read_raw. ADC/read_imp já eram chamados sob ele; reset usa apenas regmap e não read_raw. Probe reseta antes do registro IIO, sem leitor publicado. Não é lock global para firmware | Baixo | Extensão mínima no driver MediaTek; não criar lock/state framework paralelo, nem driver postmarketOS/Qualcomm para outro PMIC |

Auditoria de chamadas no arquivo fixado: read_adc é interno a read_raw; reset
é chamado por read_raw e pelo probe. Sem callback remove próprio; não inventar
rollback. Patch mantém escala sem lock/I/O e mesmos erros, histórico, writes e
política de reset sequencial; muda somente exclusão e duração do lock. Locks
Linux são reutilizados diretamente no candidato. Teste host usa pthread e
cleanup do compilador como modelo de escopo: não é prova de lockdep, scheduler
kernel ou exclusão com outro master. Compilar objeto ARM32 com headers reais;
testar liberações em sucesso, falha, retorno antecipado e escala, mais contenção
determinística. Nenhuma imagem/bind/IRQ do aparelho autorizada nesta etapa.

### KUnit IIO existente — antes da integração no runner

Reutilizar `drivers/iio/test/iio-test-multiply.c` (GPL-2.0-only, mesmo commit
stable, SHA c833162009c0a683bca81ab93cb6c3b1bee22c64038da12d909744a32ded0bc1)
e `iio_multiply_value` do core. Só habilitar CONFIG_IIO e
CONFIG_IIO_MULTIPLY_KUNIT_TEST no workspace UML isolado e verificar hashes.
Não escrever outro teste kernel de multiplicação. Runner existente mantém
timeouts, isolamento de rede/hostfs/módulos, validação exata de suites/casos e
proibição de retry. Seleção '*' executa apenas as três suítes configuradas;
KUNIT_ALL_TESTS deve ser recusado. IIO não implica carregar o driver AUXADC:
sem CONFIG_MEDIATEK_MT6359_AUXADC, DT, plataforma real ou acesso ao telefone.
Essa suíte valida o core upstream, não os patches ADC nem efeitos elétricos.

### Complemento prévio: distinguir timeout anterior do erro atual

Reutilizar o mutex e a flag timed_out existentes, sem nova máquina de estados:
capturar a flag sob o lock antes da aquisição e consultar essa história na
decisão de reset. Assim um stop que acaba de falhar não é, sozinho, prova de
dois timeouts. Origem/commit/licença são os mesmos da linha AUXADC abaixo;
patch separado e GPL-2.0-only, sem nova API, probe ou remove. Comparar primeira
e segunda leituras, erro duplo e sucesso após falha. O processamento de erro
continua fora do mutex no upstream: concorrência global e serialização de
reset/flag permanecem pendências, não cobertas por stubs sequenciais.

## Erro de stop AUXADC — antes do patch (2026-10-25)

| Funcionalidade | Implementação atual | Alternativa / revisão / licença | Compatibilidade / efeitos | Esforço | Recomendação |
| --- | --- | --- | --- | --- | --- |
| Rejeitar amostra se falhar stop | Ensaio ADC K40S já retorna cleanup_error; upstream read_adc retorna sucesso com stop falho | Estender mt6359_auxadc_read_adc do Linux stable 6.18.58, commit 2926d88bb7fc4608fd942453d929c39e4e5ec006, GPL-2.0-only, fonte SHA 74b50fc1602bbf9a180950c77485ad687818e0385e5154b60ed99a876d2eb146 | Código MediaTek já disponível; postmarketOS não requer outro provider; Qualcomm/REA não substituem a função deste PMIC. Sem novas escritas ou mudanças no probe/remove; retorno em erro muda intencionalmente | Baixo | Patch mínimo no driver existente, staging separado do patch de escala; preservar erro de aquisição prioritário, não publicar out e não esconder falha no stop |

Testar funções reais sample_adc_val/read_adc/read_raw com regmap simulado,
incluindo erro antes/depois do commit, timeout, erro duplo, conteúdo inicial do
banco e sequência de duas leituras. Comparar trace de I/O original/candidato:
não adicionar writes/retries em read_adc. A propagação de -ETIMEDOUT no stop
pode alcançar o reset já existente em read_raw; demonstrar esse efeito, não
declará-lo equivalente ou seguro. Esse reset continua bloqueador para bind. MT6357 não usa
ext_sel; não alegar prova de cleanup de GPIO para PMICs SPMI. ARGUMENTOS: stubs
não validam exclusão, concorrência, regcache, timing ou propriedade do barramento.
Reutilizar KUnit upstream para lógica IIO; harness host verifica contrato e
injeção de falhas, não é driver, framework ADC ou teste físico novo.

## Reutilização efetiva AUXADC/IIO — antes do patch (2026-10-25)

| Funcionalidade | Atual | Alternativa / origem / licença | Compatibilidade e efeitos | Esforço | Recomendação |
| --- | --- | --- | --- | --- | --- |
| Escala ADC para consumidores IIO | Diagnósticos próprios calculam raw * referência * razão / 2^bits | mt6359-auxadc.c e inkern.c, Linux 6.18.58, commit 2926d88bb7fc4608fd942453d929c39e4e5ec006, GPL-2.0-only | MT6357 já suportado. read_raw(SCALE) publica referência sem dividir pela resolução; iio_multiply_value não supõe resolução. Fonte ADC SHA 74b50fc1602bbf9a180950c77485ad687818e0385e5154b60ed99a876d2eb146 | Baixo para correção aritmética; alto para habilitação segura | Patch pequeno no driver existente, somente staging, sem novo driver/provider; provar contra função real do core IIO e oráculos locais |
| Substituição dos ensaios ADC/NTC por IIO | Requests SET/CLR por bit, guardas e limpeza verificada | Mesmo driver MediaTek upstream; postmarketOS candidato a consumidor de mainline, não outro ADC confirmado; drivers Qualcomm não equivalem a MT6357 | Probe/timeout resetam; request/stop escrevem banco inteiro; stop com erro pode publicar amostra. Tipos BATADC/BAT_TEMP exigem revisão. REA não substitui fonte disponível | Alto | Bloquear bind/DT e retirada dos ensaios até fechar exclusão, tipos/unidades, reset e erro/remove; preservar recuperação |

O patch de escala não altera probe, remove, aquisição, reset, locks ou MMIO;
portanto também não resolve os riscos existentes nesses caminhos. Não alterar
no_reset do MT6357 como atalho. Testes host compilam funções upstream extraídas
de fontes hasheadas em diretório temporário; não há I/O do telefone. Patch não
entra nas séries de imagem/registry. Testar 12/15 bits e denominadores r_ratio,
inclusive mais de um, antes de considerar o resultado numericamente correto.

### Comparação AUXADC confirmada na fonte fixada

| Aspecto | Ensaios K40S validados | Driver IIO existente | Decisão |
| --- | --- | --- | --- |
| BATADC | 0x1088, 15 bits, razão 3, 128 médias, 1280–1600 us | ADC0+2*0, 15 bits, razão 3/1, 128*10 us | Aquisição é reutilizável após fechar ownership/cleanup; não reimplementar ADC |
| BAT_TEMP | 0x108e, 12 bits, razão 1, 8 médias, 80–120 us | ADC0+2*3, 12 bits, razão 1/1, 8*10 us | RAW é tensão do divisor, não temperatura calibrada da célula |
| RDY/timeout | bit15, poll100 us, timeout32000 us | Mesmos parâmetros no caminho PWRAP | Não confundir SPMI 8 bits com PWRAP 16 bits |
| Request/stop | SET0x1110/CLR0x1112 somente bit0 ou bit3, readback | Escreve máscara e depois zero no banco0x110e | Falta exclusão com firmware/outros consumidores; mutex local do IIO não prova exclusão global |
| Falha no stop | Erro impede publicar resultado; verifica controles | read_adc pode retornar sucesso apesar do erro no stop; read_raw limpa timed_out após sucesso | Não são equivalentes; patch de escala não altera este comportamento |
| Probe/erro/remove | Sem reset, aquisição finita, limpeza explícita | Probe reseta0x0f90 bits0/3; erro repetido pode resetar; não há callback remove explícito, registro IIO é devm | devm retira interface, não prova rollback de controles/reset; bind bloqueado |
| Tipos/unidades | BATADC em uV; NTC/calibração LG separada | BATADC IIO_RESISTANCE, BAT_TEMP IIO_TEMP, SCALE sem resolução | Revisar tipos antes de consumer power_supply; não interpretar RAW como grau Celsius |

Patch `patches/kernel/staging/mt6357-auxadc-scale-v1.patch` corrige somente a
fração de escala via IIO_VAL_FRACTIONAL_LOG2/FRACTIONAL. Aplicação fuzz0 em cópia
isolada e compilação do objeto ARM32 aprovadas. Teste usa read_raw real, antes e
depois do patch, e iio_multiply_value real do core (inkern.c SHA256
efe82f50976cc73251d86669bb02cc9c71e4978b05af84f8f9eb5cfa567f3115).
Para raw16384/BATADC, o original publica escala que resulta em88473600 mV;
nominal esperado2700 mV. Candidato reproduz os oráculos em todos os códigos
12/15 bits e razões com denominadores1/2/3 (110592 comparações); SCALE não
inicia I/O. Isso prova aritmética, não precisão elétrica ou tipo/unidade final.

O próprio kernel já fornece `drivers/iio/test/iio-test-multiply.c`, suíte KUnit
`iio-multiply` e CONFIG_IIO_MULTIPLY_KUNIT_TEST. Reutilizar essa suíte na próxima
prova UML; não criar implementação de multiplicação nem runner C próprios.
Execução desta suíte upstream ainda não realizada nesta etapa. O harness host
é só comparação do contrato driver/core, não substituição de KUnit.

Fontes públicas: [driver v6.18](https://github.com/torvalds/linux/blob/v6.18/drivers/iio/adc/mt6359-auxadc.c),
[core IIO v6.18](https://github.com/torvalds/linux/blob/v6.18/drivers/iio/inkern.c).
Versão/hashes efetivamente testados são os locais fixados, não a tag pública.

## Extração do latch CAR MT6357 — antes do código (2026-10-25)

| Funcionalidade | Implementação atual | Alternativa open source | Compatibilidade | Esforço | Recomendação |
| --- | --- | --- | --- | --- | --- |
| Aquisição CAR e limpeza após falha | Sequência K40S congelada, máscara 0x000f | Linux stable 6.18.58, commit 2926d88bb7fc4608fd942453d929c39e4e5ec006: regmap_read/update_bits/read_poll_timeout; licença do kernel preservada. LG mt6357_gauge.c GPLv2, SHA256 791da3263f0ece0f91c7fe91fcc2f079a053f1441cd9ceab326330afb9a12c4a | Reutilizar regmap, não criar transporte. A rotina LG não substitui a proteção atual: sua máscara 0x1f05 alcança outros campos. Qualcomm e ferramentas de engenharia reversa não fornecem equivalência deste PMIC. Nenhum driver postmarketOS confirmado nesta auditoria | Baixo | Extrair apenas a sequência existente para componente GPL-2.0-only; manter veto de bits desconhecidos no adaptador K40S |

Contrato: chamador mantém exclusão, identidade do PMIC e autorização; helper não
faz probe/remove, registro de driver, reset ou habilitação de carregador. Polls
permanecem 100/32000 us; limpeza READ1/CLEAR8/IDLE0 preserva a primeira falha e
verifica CON0/CON1. Comparar retorno, amostras, registros finais e trace de I/O
contra fonte congelada, inclusive erros antes/depois da escrita. Não alterar
originais nem artefato v1; nova build v4 apenas offline, não selecionada pelo
preparador físico. KUnit desta sequência permanece pendente até execução real
no runner upstream; testes host não são evidência física nem KUnit.

## Extração CAR bruto MT6357 — antes do código (2026-10-25)

| Função | Atual | Alternativa / origem / licença | Compatibilidade e efeitos | Esforço | Decisão |
| --- | --- | --- | --- | --- | --- |
| CAR bruto: dois registradores, sinal e sentinelas | coulomb-decode.h mistura bits e escala | Fonte LG mt6357_gauge.c, GPL-2.0-only, arquivo SHA 791da3263f0ece0f91c7fe91fcc2f079a053f1441cd9ceab326330afb9a12c4a; archive SHA catalogado | Layout MT6357, sem regmap/probe/remove/latch/MMIO no helper | B | Extrair aritmética bruta para kernel/components/pmics/mt6357; API antiga delega; RFG/tune/unidades ficam no adaptador |
| Interface de carga e testes | power_supply e oráculo LG de 2^21 payloads | Linux 6.18.58 commit 2926d88bb7fc4608fd942453d929c39e4e5ec006, power_supply/KUnit, GPL por arquivo | Não há gauge MT6357 em power/supply desta árvore; MFD/regulador não substitui decoder; outro mt63xx não prova equivalência | M | Reutilizar frameworks, sem nova classe de bateria ou módulo de aquisição |

Pesquisa pública: binding MFD MT6357 e power_supply não fornecem implementação
comprovadamente intercambiável deste decoder. Referência de unidades:
https://docs.kernel.org/power/power_supply_class.html. Bitfields comuns não cobrem
costura, sentinelas e magnitude: helper puro específico é justificado. Calibração
diferente continua recusada. Header/teste C GPL-2.0-only, sem I/O. Builder cria
artefato novo e preserva v1/imagens/seleção física. Comparar resultados e erros
sem alterar out, bits ignorados e todos os payloads antes de uso físico.

A revisão do consumidor encontrou pin de fontes v1 no preparo de rootfs. Portanto
o header/Makefile v1 ficam byte-idênticos e a ponte nova fica em
kernel/devices/lg-k40s/mt6357-car-units.h, mapeada pelo builder para v3. O build
intermediário v2 foi preservado, nunca selecionado/carregado. Não enfraquecer o
pin existente para fazer a refatoração passar.

## Composição por componentes — antes da implementação (2026-10-25)

| Função | Atual | Alternativa / versão / licença | Compatibilidade / efeitos | Esforço | Decisão |
| --- | --- | --- | --- | --- | --- |
| Descrever componentes e composição da placa | Perfil K40S e fontes/ensaios com paths históricos | Device Tree/bindings Linux e separação ASoC; Linux 6.18.58 commit 2926d88bb7fc4608fd942453d929c39e4e5ec006, licenças por arquivo | DT continua sendo a descrição executada pelo kernel; não gerar bindings/driver framework paralelo. Sem probe/remove | M | Catálogo host apenas referencia código/subsistemas existentes e distingue instância/placa de chip |
| Validar catálogo e dependências offline | Sem catálogo de componentes | jsonschema 4.26.0 (MIT), já fixado no venv; Python 3.12.3 json/pathlib/hashlib (PSF-2.0) | JSON Schema valida estrutura; código próprio só verifica identidade, referências, DAG, paths e evidências que schema não garante. Sem transportes | B | Reutilizar biblioteca, schemas locais sem resolução remota; comando adicional no kernel-workspace, sem alterar plano/build existente |

Referências: https://docs.kernel.org/devicetree/usage-model.html e
https://docs.kernel.org/sound/soc/overview.html. Definições próprias são MIT;
fontes e patches de kernel não mudam de licença. Alternativas upstream por chip
ficam como candidatas, não suporte comprovado. Wi-Fi/codec ainda sem identificação
fechada ficam em pendências da placa, não em componentes genéricos inventados.
Não mover módulos históricos, alterar fingerprints ou caminhos de recuperação.

Revisão de retomada do hardware: [I2C upstream, clocks e lifecycle K40S](k40s-i2c-upstream-integration-audit.md).
Arquivo upstream fixado por commit, licença e hash; matriz probe/erro/remove/
resume, incompatibilidade DMA/FIFO e decisão de extensão antes de implementação
paralela. Nenhum driver novo ou bind foi implementado por essa auditoria.

Defaults de identificação/captura: reutilizar `portkit.backends.mediatek` MIT
(base 6a4dcfe) e inteiros/JSON da stdlib Python 3.12.3 PSF-2.0 para extrair hwcode
e atomic_logbuf do perfil. Não há nova leitura de chip, parser binário ou driver:
identificação real e bounds CLI continuam na sessão DA legada. Manter hash do DA
e framing/reset no backend. Comparar todos os bytes restantes após desfazer as
substituições de defaults/diagnóstico em memória. Esforço baixo, zero probe/remove
e nenhuma mudança no caso K40S; não é suporte a outro MediaTek ou Qualcomm.

## Continuação: nome da pasta e configuração SSH (2026-10-25)

| Funcionalidade | Atual | Alternativa open source | Compatibilidade | Esforço | Recomendação |
| --- | --- | --- | --- | --- | --- |
| Configuração SSH do ciclo | Identidade privada literal e alvo normal no helper legado | Loader JSON/pathlib/ipaddress Python 3.12.3 PSF-2.0; portkit.profiles MIT, base 6a4dcfe; OpenSSH existente do host | Apenas caminho da identidade e alvo normal; sem parser SSH, transporte novo, probe/remove ou alteração do pin USB | B | Reutilizar config local ignorada; carregamento lazy obrigatório, sem fallback privado embutido; testar argv exato e falha antes de rede |
| Compatibilidade da pasta renomeada | Caminhos antigos nos scripts e manifestos privados | Junction NTFS do Windows via PowerShell New-Item | Alias do mesmo diretório, sem copiar dados ou reescrever evidências; WSL também deve resolver | B | Preservar alias antigo até migrar consumidores; não alterar runtime Linux /home nem hashes históricos |

Mainline/postmarketOS não gerenciam a identidade SSH privada deste laboratório.
Usar o OpenSSH existente; não substituir autenticação/pin, nonce, ledger ou
recuperação por cliente próprio. O ciclo configura a instância importada do
helper legado sem reescrever sua CLI standalone, que continua congelada.
IP USB/porta/user permanecem presos ao initramfs atual; não aceitar configurações
que contradigam esse contrato. Matriz não autoriza acesso ao telefone.

## Continuação: geometria e capturas DA (2026-10-25)

| Funcionalidade | Atual | Alternativa open source | Compatibilidade | Esforço | Recomendação |
| --- | --- | --- | --- | --- | --- |
| Geometria boot_a, hash de recuperação e regiões DRAM | Literais no início de k40s-da-session.py | portkit.profiles deste projeto, MIT, commit 3999759; JSON/pathlib Python 3.12.3, PSF-2.0 | Valores K40S já catalogados; validação local sem importar USB; não muda probe/remove, framing/reset, verificações GPT ou readback | B | Estender loader existente, reverter hunk em memória e comparar hash original; manter protocolo/DA no backend legado |

Não há ferramenta/driver/API nova de transporte. mtkclient (commit e licença em
manifests/third-party.json) continua executando o DA; Linux/postmarketOS não
substituem as regiões privadas de captura nem o layout GPT desta placa. Nenhuma
atualização de checkout, generalização para EDL ou operação física é necessária.
Validar tipos (sem bool), limites, alinhamento e sobreposição antes do transporte.
SHA do binário DA/reset continua no backend, não é configuração de outra placa.

## Continuação: configuração do ciclo, primeiro passo (2026-10-25)

| Funcionalidade | Implementação atual | Alternativa open source | Compatibilidade | Esforço | Recomendação |
| --- | --- | --- | --- | --- | --- |
| Caminho de restauração e release normal do ciclo | Dois literais em lts-auto-cycle.py | portkit.profiles já existente neste projeto, MIT, base Git 39e3b89; json/pathlib Python 3.12.3 PSF-2.0 | Mesmos dois valores do K40S; validação local antes de qualquer transporte; sem probe/remove | B | Reutilizar loader e validar caminhos/release; não alterar comandos, DA, prazos, ledger ou fallback |

Não há protocolo, framework ou ferramenta nova: apenas configuração da placa.
Mainline/postmarketOS não fornecem o caminho privado da imagem deste laboratório.
Equivalência exigida por testes de valores e regressão do ciclo com mocks.
Constantes DA/DRAM, verificações de hardware e SSH permanecem legadas nesta etapa;
esta migração não prova segurança física nem autoriza novo boot.

Extensão dos três casos KUnit existentes: reutilizar o mesmo KUnit Linux 6.18.58
(commit/licença fixados abaixo), sem novo framework ou módulo. Trazer a cobertura
do oráculo C host já preservado: IRQ terminal repetida, cada bit de erro,
cancelamento antes/depois, erro desconhecido tardio, zero/RS e ponteiros nulos.
Somente assertions/testes GPL-2.0-only, sem mudanças no helper, probe/remove ou
MMIO. Não retirar o oráculo host: UML e compilação ARM32 continuam complementares.

Data: 2026-10-25. Escopo: port mainline do LG K40S LM-X430BMW e futura
reutilização do ferramental em MediaTek e Snapdragon.

## Resultado e limites

Recomendação: concentrar o port em extensões dos subsistemas existentes, não
transformar a coleção de ensaios finitos em uma segunda pilha de drivers.
As prioridades são comparar/estender `i2c-mt65xx`, reutilizar CCF/irqdomain,
integrar AUXADC/IIO e conservar `power_supply` como interface da bateria.
Não foi comprovado um driver aberto pronto que resolva todo o K40S.

Esta entrega só acrescenta documentação e instruções de trabalho. Nenhum código
de driver, imagem, serviço, partição, dependência ou configuração do telefone foi
alterado; nenhum teste físico foi iniciado. O trabalho de implementação pausado
não foi retomado por esta auditoria.

Base local consultada: Linux **6.18.58**, workspace atomic fixado em
`tools/k40s_kernel_variants.py`; kernel normal **4.9.190-k40s-bringup**; fonte
LG `sources/vendor-lg/kernel-4.9`; documentação e artefatos de ensaio existentes.
Fontes web foram consultadas em 2026-10-25. Links Linux `v6.18` são referências
públicas da série, não alegação de identidade byte a byte com 6.18.58 local.
Não se trocou a versão do kernel durante a pesquisa.

Níveis: **confirmado no código** não significa confirmado no aparelho;
**candidato** exige revisão adicional antes de integrar. Ausência nesta busca
significa “não encontrado”, não uma prova de inexistência global. Repositórios
com leitura incompleta não foram promovidos a soluções compatíveis.

Esforço relativo: B = baixo (configuração/integração pequena), M = médio
(adaptação e testes de lifecycle), A = alto (SoC, protocolo ou dependências ainda
incompletas). Não são estimativas de prazo.

## Matriz de decisão

As versões/licenças dos identificadores S01–S15 constam no catálogo abaixo.

| Funcionalidade | Implementação atual | Alternativa open source / origem | Compatibilidade e lacuna específica | Esforço | Recomendação |
| --- | --- | --- | --- | --- | --- |
| Controlador I2C5 | `k40s-i2c5-adapter`, provider de bateria e FIFO limitado | S01 `drivers/i2c/busses/i2c-mt65xx.c`, I2C core | Driver presente, mas sem match MT6765 explícito na árvore auditada; offsets DMA, HS-only/push-pull, timeout e handoff diferem. O genérico usa DMA/reset; nosso ensaio não | A | Auditar uma extensão do driver existente com dados/quirks MT6765. Não ampliar um segundo controlador antes de documentar por que essa extensão não atenderia |
| IRQ do I2C e término de transferência | `k40s-i2c5-irq-policy`, engine/runtime só offline | S01 generic IRQ, irqdomain, `irq-mtk-sysirq.c`, completion e handler de `i2c-mt65xx` | SPI130, LEVEL_LOW via sysirq identificado; mapping Linux não é número fixo. Polarity write antes da falha do parent não é revertido automaticamente. Engine própria só compilada, sem prova física | M/A | Suspender expansão paralela do engine; comparar requisito por requisito com handler upstream. Reutilizar IRQ core; política de ensaio permanece fora do driver de produção |
| Clocks, gates e runtime PM | Guard de handoff e lease de gates puro offline | S01 CCF, `clk-mt6765.c`, `clk_bulk_*`, runtime PM | Suporte MT6765 existe; probe TOP/APMIXED e callbacks podem escrever em clocks herdados. Ownership/parents e compartilhamento de gates ainda incompletos | A | Estender/revisar providers existentes e referências reais dos consumidores; não criar um framework de clocks por MMIO nem clocks fictícios |
| PWRAP / acesso MT6357 | Driver upstream com patches restritos de handoff | S01 `mtk-pmic-wrap.c`, regmap, MFD `mt6397-core.c` | Já há reutilização substancial. Inicialização genérica não equivale ao handoff LK; patch evita reset/escritas desnecessárias | M | Manter extensão pequena documentada; preparar justificativa upstream. Não criar acesso PMIC paralelo ou `/dev/mem` |
| Reguladores e IRQ do PMIC | MFD/regulator upstream com modo de teste sem IRQ | S01 `mt6357-regulator.c`, `mt6358-irq.c`, regulator/irqchip | Cleanup pode desligar rail sem consumidor; inicialização IRQ precisa pinctrl/EINT e revisão do topo. Modo sem IRQ não é suporte completo | M/A | Reutilizar drivers; completar DT/consumidores/IRQ e preservar USB/eMMC durante migração |
| Tensão e ADC da bateria | Helpers específicos, capturas V/I/T finitas | S01 `drivers/iio/adc/mt6359-auxadc.c` com `mediatek,mt6357-auxadc`, IIO consumer API | Match MT6357 e tabela de canais confirmados em 6.18.58. Probe chama reset; timeout pode resetar; unidades, escalas e conversão de cada canal precisam comparação | M/A | Prioridade alta: adaptar o driver IIO existente para requisitos demonstrados; não criar outro driver ADC. Não ativar o probe atual sem revisão |
| Temperatura NTC compensada | Tabela/interpolação LG, pullup 62k/1,8V e compensação por corrente | S01 IIO, `ntc_thermistor.c`, `generic-adc-thermal.c`, thermal; fonte LG 4.9 | Frameworks disponíveis, mas não provada equivalência à compensação LG, truncamentos e janela V/I/T. Tipo IIO_TEMP não implica temperatura já calibrada da célula | M | Reutilizar aquisição e APIs; manter apenas modelo/calibração da placa que não caiba em propriedades/framework existente |
| Corrente e contador de coulombs MT6357 | Latch FG limitado e decoder validado contra C LG; `CHARGE_COUNTER` relativo | S01 power_supply/regmap; fonte LG `mt6357_gauge.c` e S03 como referência | Nenhum fuel-gauge MT6357 completo confirmado nesta auditoria. AUXADC não substitui CAR. Drivers Qualcomm/PMICs diferentes não são compatíveis por analogia | A | Código específico de FG ainda justificável, limitado a registros/latch/conversão e inserido nas APIs padrão; reutilizar testes LG. Não duplicar toda a política Android |
| Percentual/SOC e saúde | Não implementados no 6.18 | S01 `power_supply_battery_info`, `simple-battery`, tabelas OCV/resistência; FG LG como referência | Metadados não constituem estimador pronto. Faltam referência, continuidade/reset/rollover, capacidade e compensação. CAR=0 não significa 0% | A | Usar dados/framework existentes, mas só publicar CAPACITY após modelo validado; não inventar porcentagem por tensão ou CAR isolado |
| Estado e controle do carregador MT6371 | Leitura limitada ID/STATUS no endereço 0x34; sem controle de carga | S01 MFD `mt6370.c`, `mt6370-charger.c`, `mt6370-adc.c`, power_supply/regmap-irq | Família identificada como MT6371/rev4, mas equivalência completa de registros/proteções não provada. MFD cria filhos/IRQ; charger configura carga e OTG, não é leitor passivo | A | Estender a família existente se diferenças exigirem; revisar todas as escritas/defaults/limites de bateria antes de bind. Preservar leitor restrito até equivalência |
| Refresh/cache/concorrência da bateria | Módulo de três capturas/15s, mutex e expiração; sem uso contínuo | S01 power_supply, IIO consumer, workqueue/delayed_work, runtime PM | Interfaces já usadas; falta driver contínuo com lifetime e energia. Core não fornece automaticamente atomicidade do conjunto V/I/T | M | Um único consumidor com cache/lock necessário; não manter vários módulos semelhantes como drivers finais. Arquivar ensaios com evidência, não apagá-los |
| DT, overlays e validação | DTC/fdtoverlay + parsers/asserts e auditors próprios | S01 `dtbs_check`; S05 dt-schema e DTC/libfdt | Reutilizável em ambos SoCs; schema não verifica handoff, calibração nem equivalência de valores. Checks de reservas/ordem de overlay continuam específicos | B/M | Usar schema/libfdt antes de novo parser; manter só invariantes não cobertas. Comparar saída antes de substituir parsers existentes |
| Painel, brilho e imagem | 4.9 mtkfb funcional; 6.18 sem port de painel | S01 DRM MediaTek, MIPI DSI, DRM panel/bridge/backlight; S07 gerador QCOM | Framework serve, pipeline MT6765 e painel exato não comprovados. Gerador lê DT QCOM MDSS, não LCM MediaTek diretamente | A | Reutilizar DRM; portar dados/sequência/alimentação do painel. Avaliar extensão do gerador só após comparar formato; não escrever stack DSI nem supor gerador universal |
| Touch FT5446 | Driver LG no 4.9; sem port 6.18 | S01 `edt-ft5x06.c`, input MT, touchscreen properties | I2C0/0x38 documentado; família FT5x é candidata, sem match FT5446 explícito encontrado. Protocolo de eventos, ID, reset/IRQ e firmware LG precisam comprovação | M/A | Comparar protocolo com driver existente; acrescentar dados/quirk se equivalente. Não mascarar o chip como outro compatible apenas para forçar bind |
| Power, volume, tela apagada | Funcionais no userspace/driver antigo; não portados integralmente | S01 `mtk-pmic-keys.c`, gpio-keys, input; política de sessão via userspace | PWRKEY PMIC exige IRQ/pinctrl; volume depende fiação DT. Apagar painel não desativa necessariamente touch | M | DT e drivers padrão; política de tela/sons no userspace. Não criar leitor de botão direto por registrador |
| Áudio/microfone | ALSA/driver vendor no 4.9 | S01 ASoC MediaTek, codec `mt6357.c`, DAPM e machine drivers | Codec MT6357 existe; isso não prova AFE MT6765, DMA, clocks e rotas da placa. Amplificação/calibração são específicas | A | Reutilizar codec/ASoC; completar SoC/DT/machine data, evitar transportar toda HAL Android ou criar API de áudio própria |
| Wi-Fi / Bluetooth | WMT + `wlan_drv_gen4m`, firmware/serviços vendor no 4.9 | S01 cfg80211/mac80211/mt76 e Bluetooth HCI/btmtk; S02/S03 referências MediaTek | Nome MediaTek não torna CONSYS MT6765 compatível com mt76/btmtk de outro transporte. ID de FM MT6631 não prova transporte BT discreto | A | Identificar transporte, alimentação, protocolo e firmware primeiro; comparar patches comunitários. Lacuna explícita, sem prometer substituição plug-and-play |
| GPU GE8320 | Renderização vendor isolada em Bionic no 4.9; sem GPU mainline funcional | S01 DRM Imagination + S08 Mesa PowerVR; libhybris como compatibilidade separada | Mesma marca/Rogue não prova suporte do BVNC, firmware e ABI ARM32. GE8320 não aparece como suportada na página Mesa consultada | A | Auditar BVNC/firmware/UAPI antes de esforço novo; preservar software rendering. libhybris não porta o módulo 4.9 para 6.18 |
| USB device/host, OTG e console | NCM/SSH e recuperação próprios; funcionalidade no 6.18 já ensaiada | S01 MUSB/PHY MediaTek, gadget configfs NCM/ACM, usb-role-switch; getty/SSH userspace | Stack padrão reaproveitável; ID/VBUS, regulador, role e recuperação dependem placa. Host/charging simultâneos não decorrem de software genérico | M/A | Reutilizar gadget/USB core e login autenticado. Não criar protocolo de console próprio; manter canal de recuperação independente |
| Boot image, rootfs e empacotamento | AOSP mkbootimg, scripts/profiles próprios e Alpine | S04 pmbootstrap/pmaports/deviceinfo; AOSP mkbootimg já presente | Ferramentas genéricas cobrem build/empacotamento, não demonstram nosso fallback A/B, DRAM ou reset de DA | M | Aproveitar pacotes/perfis, integrar por wrapper; não trocar instalador/ciclo seguro de uma vez |
| BROM/DA e flash MediaTek | mtkclient + sessões, checkpoint/reset e verificação próprios | S09 mtkclient 2.1.4 local, CLI/biblioteca existente | Transporte já reutilizado. DA/SoC/LK e reset são específicos; código aberto do host não implica DA redistribuível nem recuperação universal | M | Manter mtkclient como backend; isolar só extensões realmente necessárias, fixar revisão e não substituir ciclo validado por comando genérico |
| Boot/recuperação Snapdragon | Ainda não implementado neste projeto | S10 qdl (EDL/Sahara/Firehose), lk2nd e fastboot conforme dispositivo | Não se aplicam ao K40S; lk2nd atende plataformas listadas, não todo Snapdragon. Programmer assinado/autorização e reset dependem modelo | A por dispositivo | Backend separado sob contrato comum; nunca reutilizar endereços, DA, BROM ou regras A/B do K40S |
| Automação de ciclos e recuperação | Orquestrador, nonce/ledger host-once, backup/hash/A-B e retorno 4.9 | S11 labgrid; LAVA como opção de laboratório | Labgrid oferece controle/estratégias, não prova nossa autorização única nem rollback. LAVA maior que a necessidade atual | M | Avaliar labgrid como camada externa, mantendo backend e invariantes atuais; não migrar imediatamente nem adotar LAVA só para um aparelho |
| Testes de driver e regressão | Python unittest + execução de C real com mocks; testes físicos limitados | S01 KUnit/kselftest, fault injection; i2c-stub e regmap tests | KUnit cobre lógica kernel; i2c-stub modela operações SMBus, não temporização/DMA/IRQ física MT6765 nem toda transferência I2C raw | M | Reutilizar testes upstream e acrescentar KUnit para mudanças destinadas a upstream; manter fixtures/hashes e oráculos vendor onde acrescentam cobertura |
| Engenharia reversa e análise binária | Ghidra, extrações e emulações locais já existentes | S12 Ghidra, S13 Unicorn, S14 QEMU; binutils/readelf/objdump | Reutilizáveis ARM/ARM64; CPU emulada não modela PMIC/CONSYS/PWRAP/boot completo do telefone automaticamente | B para uso; A para modelo HW | Utilizar ferramentas prontas; escrever só loaders/modelos/harness que faltarem, com justificativa. REA é interface/ferramental, não prova de licença dos alvos |
| RTC, sensores, câmeras, modem e gestão térmica completa | Fora da integração mínima atual; identificação parcial no backup | S01 RTC MT6397, IIO, V4L2/media, thermal, remoteproc/rpmsg; S02/S03 e S10 exemplos | Frameworks presentes não comprovam drivers para cada sensor/ISP/modem desta placa. Firmware e calibração exigem inventário próprio | A/indefinido | Antes de cada implementação, expandir esta matriz com ID exato e driver candidato. Não criar subsistemas paralelos; não bloquear bateria por esses itens |

## Catálogo de origem, versão e licença

Licenças abaixo registram o observado, não relicenciam arquivos locais. Antes de
copiar código, conferir SPDX/copyright da revisão fixada e de suas dependências.
Código-fonte de driver e firmware são itens distintos. Nenhuma biblioteca GPLv3
do host deve ser copiada automaticamente para módulo do kernel GPLv2.

| ID | Origem / versão examinada | Licença / estado da verificação | Limitações da evidência |
| --- | --- | --- | --- |
| S01 | Linux 6.18.58 local; links públicos v6.18 abaixo | Kernel GPL-2.0; `i2c-mt65xx`, AUXADC e charger MT6370: SPDX GPL-2.0-only. DRM Imagination possui arquivos GPL-2.0-only OR MIT; conferir cada arquivo | Não equivale a certificar todo subsistema ou hardware; extensões locais têm hashes próprios |
| S02 | [Helio-P22/linux-mainline, branch mt6765](https://gitlab.com/Helio-P22/linux-mainline/-/tree/mt6765) | Derivado Linux; licença/commit dos patches individuais ainda não fixados nesta busca | A interface web só expôs navegação; candidato de alta afinidade, não código validado/importável automaticamente |
| S03 | [mtk-mainline/mt6768/linux](https://gitlab.com/mtk-mainline/mt6768/linux), página do projeto consultada | Derivado Linux; licença por patch e commit a fixar | Projeto declara MT6768/MT6769Z/Volla Phone 22; não é suporte MT6765 nem MT6357 FG comprovado |
| S04 | [pmbootstrap](https://gitlab.postmarketos.org/postmarketOS/pmbootstrap) / [pmaports](https://gitlab.postmarketos.org/postmarketOS/pmaports), projeto corrente consultado, sem checkout fixado | GPLv3 indicado na distribuição pmbootstrap; revisão e sufixo only/or-later a conferir no fonte antes de integrar. Pmaports tem licenças por pacote | Página de licença direta não pôde ser lida pela ferramenta; não aprovado para cópia nesta auditoria |
| S05 | [dt-schema](https://github.com/devicetree-org/dt-schema) e [DTC/libfdt](https://github.com/dgibson/dtc), repositórios consultados; versão instalada não inventariada | dt-schema usa licenças distintas para ferramentas/schemas; DTC GPL e libfdt dual permissiva/GPL conforme arquivo. Validar SPDX da versão selecionada | Somente recomendação de uso; não houve instalação/mudança de parser |
| S06 | Fonte LG 4.9 local, pacote LMX430HM Kernel Q; baseline aparelho 4.9.190 | GPLv2 do kernel; verificar cabeçalho e compatibilidade da variante em cada arquivo. Blobs não herdam GPL do kernel | Oráculo do comportamento, não driver mainline pronto nem prova de equivalência HM/BMW |
| S07 | [linux-mdss-dsi-panel-driver-generator](https://github.com/msm8916-mainline/linux-mdss-dsi-panel-driver-generator), master consultado, commit não fixado | COPYING GPLv2 confirmado | Gerador QCOM MDSS DSI; não conversor MTK LCM pronto |
| S08 | [Mesa PowerVR](https://docs.mesa3d.org/drivers/powervr.html), documentação corrente consultada; sem revisão Mesa fixada | Projeto majoritariamente MIT, conferir arquivos; firmware tem licença própria | Página exige correspondência de BVNC, e descreve suporte parcial/inexistente de vários cores |
| S09 | [mtkclient](https://github.com/bkerler/mtkclient), **2.1.4** em pyproject local; main remoto consultado | LICENSE GPLv3 e classifier GPLv3 confirmados; registrar commit local + alterações ao integrar | Não atualizar checkout validado durante migração; DA e payloads exigem verificação própria |
| S10 | [qdl](https://github.com/linux-msm/qdl), master consultado; [lk2nd](https://github.com/msm8916-mainline/lk2nd), repositório consultado | qdl LICENSE BSD-3-Clause confirmado. lk2nd é composto de fontes com licenças por arquivo; não assumir licença única sem revisar checkout | Nenhum commit ou conjunto de aparelhos Snapdragon foi fixado; candidatos de backend, não usados |
| S11 | [labgrid](https://github.com/labgrid-project/labgrid), master consultado; LAVA projeto/documentação como alternativa secundária | COPYING LGPL-2.1 confirmado para labgrid, sufixo e arquivos a conferir; LAVA possui histórico de licenças mistas, revisar versão antes de seleção | Nenhuma dessas ferramentas foi instalada; LAVA não foi selecionado |
| S12 | [Ghidra](https://github.com/NationalSecurityAgency/ghidra), upstream consultado; versão local não revalidada | Apache-2.0 do projeto, dependências/notices separados | Sem nova análise de binários nesta auditoria |
| S13 | [Unicorn](https://github.com/unicorn-engine/unicorn), upstream consultado, sem commit fixado | GPL-2.0 do core; bindings/componentes têm avisos próprios | Reutilização de emulação CPU, não modelo pronto do telefone |
| S14 | [QEMU](https://www.qemu.org/), candidato não instalado nem versionado nesta etapa | GPLv2 do projeto com componentes sob outras licenças; auditar versão escolhida | KUnit/QEMU não demonstra boot completo do K40S; nenhuma máquina K40S pronta foi confirmada |
| S15 | AOSP mkbootimg já em `tools/aosp-mkbootimg`; utilitários existentes do sistema | Licença e commit da cópia usada devem ser anexados ao manifesto de distribuição; não presumir uma licença comum a todo `tools/` | Nenhum empacotador foi substituído |

Revisão pendente é um bloqueio para **incorporar/copiar** essa alternativa, não
um motivo para escrever um equivalente novo. Fixar commit/hash/licença é parte
da próxima etapa de integração de cada candidato, não tarefa implicitamente feita.

## Achados que mudam a prioridade

### 1. AUXADC existente: evitar novo driver, sem ativação cega

Na cópia 6.18.58, `mt6359-auxadc.c` já tem `mt6357_chip_info`, canais,
registradores e compatible MT6357. `mt6359_auxadc_probe()` chama
`mt6359_auxadc_reset()`; a configuração MT6357 não tem `no_reset=true`.
O reset escreve `PMIC_HK_TOP_RST_CON0` (0x0f90), bits 0 e 3; há também
recuperação por reset no caminho de erro. A presença desse driver reduz o
trabalho de aquisição, mas não atende automaticamente ao ensaio que proíbe reset.

A próxima proposta deve comparar canal por canal: request/ready/stop, escala,
tipo IIO, referência, timeout, concorrência, efeitos no probe/erro/remove e
compensação NTC. Uma exceção de handoff precisa justificativa de hardware e
aceitabilidade upstream, não um parâmetro genérico para ignorar erros.
Referência: [driver AUXADC v6.18](https://github.com/torvalds/linux/blob/v6.18/drivers/iio/adc/mt6359-auxadc.c).

### 2. I2C: extensão no driver padrão é a primeira opção

A auditoria existente já demonstra por que o perfil genérico não é equivalente:
MULTI_DMA 0xf8c vendor versus 0x8c upstream; DCM ausente no caminho LG;
HS-only/push-pull e configuração herdada do LK; DMA/reset do driver padrão.
Isso justifica o diagnóstico FIFO restrito, mas não justifica por si só manter
um controlador geral paralelo. O primeiro estudo de patch deve avaliar dados
de compatibilidade, timing e eventual caminho PIO no driver upstream. Um caminho
PIO novo só será necessário se o DMA existente não puder ser integrado com
equivalência e recuperação demonstradas.
Referência: [i2c-mt65xx v6.18](https://github.com/torvalds/linux/blob/v6.18/drivers/i2c/busses/i2c-mt65xx.c).

O engine IRQ próprio em `k40s-i2c5-irq-engine` tem prova de compilação ARM32 v3,
com `phone_load_forbidden=true`; isso não é teste funcional nem autorização de
ativação. Preservar como experimento até a comparação com o driver existente.

### 3. Fuel gauge é uma lacuna distinta de ADC e carregador

Não foi confirmado nesta busca um driver mainline completo para FG MT6357.
A página comunitária MT6765 lista o gauge como não mainlined, mas pode estar
desatualizada e não substitui inspeção da árvore. Um driver de Qualcomm ou outro
MT63xx fornece padrões arquiteturais, não compatibilidade de registros.
Referência: [status comunitário MT6765](https://wiki.postmarketos.org/wiki/MediaTek_Helio_P35_%28MT6765%29).

O decoder atual de coulombs tem comparação exaustiva contra o C LG e prova
física de snapshot, não referência de carga absoluta nem continuidade entre boots.
Reutilizar esse conhecimento como driver pequeno de medição via regmap e API
padrão, sem portar o gerenciador inteiro de bateria Android.

### 4. Projetos comunitários são referências, não certificações

Helio-P22/mt6765 é a pista mais próxima de SoC encontrada; MT6768 é útil como
referência de integração MediaTek. O conteúdo/commit do primeiro não foi
integralmente acessível nesta consulta. Antes de qualquer cherry-pick é preciso
obter a revisão, verificar autoria/licença, comparar IP/register layout e executar
os testes de equivalência. O port não muda de SoC porque o nome comercial parece próximo.

Para Qualcomm, lk2nd e o gerador de painéis mostram soluções reutilizáveis, mas
escopo de SoCs e formatos devem ser respeitados. Não se deve portar a solução
MediaTek inteira para um aparelho Snapdragon, nem o contrário.

## O que realmente deve continuar específico

| Camada | Parte específica | Parte a compartilhar |
| --- | --- | --- |
| Placa K40S | DT, reservas de memória, fiação GPIO/IRQ, rails, painel, NTC/calibração, limites e identidade | Bindings e subsistemas Linux; perfil de dados, não cópias dos frameworks |
| SoC/PMIC MediaTek | Compat data/quirks MT6765, handoff PWRAP, FG MT6357, diferenças MT6371 comprovadas | Drivers MediaTek existentes, regmap, I2C, IIO, CCF, power_supply, IRQ core |
| Recuperação MediaTek | BROM/DA/LK, sequência de reset, mapas e checkpoints comprovados | mtkclient como transporte; contrato de sessão, verificação e recuperação |
| Snapdragon futuro | Bootloader suportado, programmer/EDL, mapa/AB, PMIC/GPU/firmware por modelo | Core de build/evidência; drivers QCOM existentes, qdl/fastboot/lk2nd quando aplicáveis |
| Host genérico | Só adaptadores inevitáveis para ferramentas e fixture física | Manifestos, hashing, artefatos imutáveis, logs, deadlines, testes, autorização única e estratégias de retorno |

Não foi criada agora uma nova biblioteca nem separado um projeto: isto é a
fronteira recomendada para futura extração. Interfaces de alto nível podem ser
comuns; endereços MMIO, comandos de flash, partições e recuperação não são.

## Ordem recomendada e critérios antes de substituir

1. Fixar revisão/licença da alternativa escolhida; mapear exatamente requisitos
   atendidos, não atendidos e efeitos de inicialização/erro/desligamento.
2. Priorizar estudo de extensão do I2C upstream e CCF/IRQ; em paralelo conceitual,
   comparar AUXADC existente com os oráculos ADC/NTC. Isso ainda não é autorização
   de teste físico nem solicitação de agentes paralelos.
3. Reutilizar `power_supply`/IIO; conservar código específico de FG/calibração só
   onde a alternativa não cobrir a função. Auditar charger antes de qualquer bind.
4. Para cada patch, testar valores/unidades/arredondamento, sign/overflow,
   sequência de I/O, timeout, late IRQ, concorrência, probe parcial, remove e
   liberação de recursos. KUnit e testes existentes são complementares.
5. Validar offline DT/reservas/overlays e hashes/empacotamento. Só depois planejar
   um teste físico curto com retorno conhecido; sem migrar duas dependências
   críticas de uma vez.
6. Não aposentar o caminho anterior até a alternativa provar os mesmos requisitos
   e recuperação; conservar imagens, relatórios e resultados negativos.

Invariantes que não podem se perder na adoção de ferramenta pronta:

- Preservar backup e boot normal 4.9 conhecido, conferência de boot_a e A/B.
- Preservar nonce/ledger e gate host-once; ferramenta de laboratório não autoriza
  replay de escrita nem retry de comando cujo resultado seja incerto.
- Guardas de identidade, hashes, whitelist, prazo total e limite de transações.
- Captura de evidência/DRAM e sequência de reset/retorno já demonstrada; ausência
  de resposta USB/SSH não é autorização para repetir flash.
- Nenhum reset PMIC/ADC, controle de carga, clock/PLL ou DMA novo entra só porque
  está no probe de um driver upstream. Requer revisão específica.
- A automação não pode prometer recuperar falhas físicas que não foram provadas.

## Fontes adicionais e evidência local

Fontes primárias:

- [MFD MT6370](https://github.com/torvalds/linux/blob/v6.18/drivers/mfd/mt6370.c) e
  [charger MT6370](https://github.com/torvalds/linux/blob/v6.18/drivers/power/supply/mt6370-charger.c).
- [Touch EDT/FocalTech](https://github.com/torvalds/linux/blob/v6.18/drivers/input/touchscreen/edt-ft5x06.c).
- [KUnit](https://kernel.org/doc/html/latest/dev-tools/kunit/) e
  [i2c-stub](https://cdn.kernel.org/doc/html/latest/i2c/i2c-stub.html).
- [Critérios de ports postmarketOS](https://docs.postmarketos.org/pmaports/main/packaging/device-categorization.html).
- [Linux power_supply](https://github.com/torvalds/linux/blob/v6.18/Documentation/power/power_supply_class.rst).
- Catálogo S01–S15 acima contém as demais origens e licenças consultadas.

Evidência local utilizada (sem nova coleta do telefone):

- `docs/lts-current-status.md`, `inventory/device-inventory.md`.
- `docs/lts-i2c5-mt6370.md`, `docs/lts-i2c5-clock-irq-preparation.md`.
- `docs/lts-pwrap-mfd-write-audit.md`, `docs/lts-mt6357-regulator-audit.md`.
- `docs/lts-battery-temperature.md`, `docs/lts-battery-i2c-refresh.md`,
  `docs/lts-battery-coulomb.md`.
- `artifacts/lts-i2c5-policy-proof-v3/build.json`: compilação apenas, não carregável.
- `docs/wifi-alpine.md`, `docs/display-alpine.md`, `docs/gpu-bringup.md`.
- `tools/mtkclient/pyproject.toml` e `LICENSE`: versão local e licença do backend.

## Registro obrigatório para a próxima funcionalidade

### Execução KUnit isolada — 2026-10-25

Reutilizar `tools/testing/kunit/kunit.py` (configure/build/exec/parse/JSON) e UML
do Linux 6.18.58, commit 2926d88bb7fc4608fd942453d929c39e4e5ec006, GPL-2.0
conforme cada arquivo; fonte fixado pelo tarball já catalogado. Python 3.12.3
stdlib (PSF-2.0), subprocess/process groups, e helpers existentes de extração,
SHA-256 e evidência cobrem a preparação e controle. Não criar parser KTAP, kernel
emulator ou runner C paralelos. O adaptador MIT próprio somente prepara uma árvore
nova, conecta o teste KUnit existente ao Kbuild, limita tempo/processos e exige
os três casos PASS no JSON oficial. Não há novo driver, probe/remove ou MMIO.

Compatibilidade: UML testa lógica C no kernel host, não IRQ físico, ARM32, DMA ou
carregamento do K40S. Fonte/build Linux em workspace isolado, sem rede/hostfs/
módulos carregáveis; nenhum diretório ativo de recuperação é alterado. Esforço M.
Manter a prova ARM32 e os oráculos Python/C; execução UML não os substitui sem
comparar cobertura. Nenhuma alteração no ciclo do telefone é autorizada por isso.

### Continuação: perfis e leitura DT offline — 2026-10-25

| Funcionalidade | Atual | Alternativa / revisão / licença | Compatibilidade e efeitos | Esforço | Decisão |
| --- | --- | --- | --- | --- | --- |
| Constantes IRQ e diretório de build nas ferramentas offline | Literais em auditores e kernel-workspace | JSON/pathlib da Python 3.12.3, PSF-2.0, perfis já existentes | Mesmos valores; não executa probe/remove nem transporte. Mantém registry/ciclo físico congelados | B | Estender o perfil, sem nova abstração de transporte |
| Leitura FDT no staging | Parser Python próprio compartilhado com coleta histórica | libfdt/pylibfdt 1.7.2.post2; DTC v1.7.2 base commit 2d10aa2afe35527728db30b35ec491ecb6959e5c (tag peeled verificado por ls-remote); libfdt dual GPL-2.0-or-later/BSD-2-Clause, conferir arquivos | Biblioteca já instalada no venv; check_full e APIs de nós/propriedades/reservas, sem I/O no telefone. Pin de wheel e base upstream são proveniências distintas | M | Adaptador pequeno para formato de saída existente; adotar apenas no staging após equivalência sintética e seis DTBs; nenhum fallback silencioso para parser antigo |

O código novo é política/integração host MIT, não parser binário novo nem driver.
Libfdt poderá rejeitar entradas malformadas antes aceitas; isso deve ser explicitado
e testado, nunca relaxado para produzir sucesso. Qualquer divergência em DTB válido
bloqueia a substituição. Mantêm-se as verificações de reservas e alterações fora
do nó autorizado, além do controlador disabled e proibição de boot/flash.

### Organização do repositório solicitada em 2026-10-25

Conversão de testes de lógica pura: usar KUnit do Linux 6.18.58 local (arquivo
fonte upstream, commit stable 2926d88bb7fc4608fd942453d929c39e4e5ec006,
identificado também pelo tarball SHA256
069b19f9032c4dac8149ae4b6520c35debca0f42a9f6d52ee55ba6ca9b818013),
`include/kunit/test.h` e APIs KUNIT_CASE/KUNIT_EXPECT, licenças preservadas do
kernel, em vez de criar framework C de teste. Novo arquivo próprio de teste
GPL-2.0-only exercita somente a política IRQ já existente; sem probe/remove,
MMIO, request_irq ou transporte. kselftest reutiliza contrato TEST_PROGS/TAP
para testar interfaces do host; não substitui diagnóstico físico nem altera
driver. Prova inicial é compilação ARM32, não execução KUnit no telefone/QEMU.

Antes de implementar ferramentas de organização: reutilizar Git (status/diff,
patches e exclusões), Python 3.12 stdlib (hashlib, json, pathlib, subprocess,
unittest, typing.Protocol) e DTC/dt-schema/libfdt já identificados acima.
Git é GPL-2.0, Python PSF-2.0; versões exatas serão registradas na baseline.
Essas APIs cobrem hashing, manifestos, subprocessos e interfaces: não criar
formatos criptográficos, runner de testes ou transporte USB paralelos.
Código próprio se limita a políticas de seleção/segurança, esquema de evidência,
perfis e adaptadores, com licença MIT escolhida pelo usuário; kernel próprio
GPL-2.0-only, derivados preservam licença. Probe/remove: não aplicável às
ferramentas offline; proibição de acesso ao telefone é requisito verificável.
Esta nota não aprova novo driver nem altera a política do carregador.

### Alpine com escrita e OpenRC como PID 1 no 6.18 — 2026-10-26

Requisito: rodar o Alpine instalado (`mmcblk0p53`) com escrita e com o init
dele no 6.18 nativo, mantendo a recuperação por watchdog/BROM.

Reutilizado sem alteração:
- o `/sbin/init` do próprio Alpine 3.24.2 (BusyBox, GPL-2.0) e o OpenRC
  0.63.2 (BSD-2-Clause), com os scripts `devfs`, `dmesg`, `udev*`, `swclock`,
  `hostname`, `bootmisc`, `syslog` e `sshd` dos pacotes instalados;
- o remount de emergência do kernel (`sysrq` s/u, GPL-2.0) como fallback;
- o mesmo supervisor, o SSH RAM na porta 2222 e o ciclo BROM/DA já validados.

Alternativas avaliadas:
- `switch_root` do initramfs do 4.9: descartado, porque apaga o initramfs e
  levaria junto o supervisor que segura o watchdog.
- `unshare` com namespace de PID: descartado, porque `CONFIG_NAMESPACES` está
  desligado no kernel nativo e exigiria recompilar.
- postmarketOS (`postmarketos-initramfs`): faz `switch_root` com a mesma
  limitação, e o projeto não prevê recuperação por watchdog.

Código novo (MIT), só cola de shell:
- `alpine-rw-prepare`: deixa gravável só a p53 (as demais partições com flag
  ro própria) e faz bind de inittab/runlevels reduzidos a partir da RAM. Nada
  do disco é editado, e os serviços do 4.9 não sobem.
- `alpine-rw-stop`: TERM/KILL nos processos com raiz no Alpine, depois `sync`
  e remount ro antes do reset.

Probe/erro/remove: uma falha no prepare desmonta tudo e volta a eMMC para ro.
O supervisor continua fora do chroot, com o fd do watchdog. Nada específico
de SoC além do layout de partições já fixado no `rootfs-readonly`.
Decisão: reutilizar o init e o OpenRC do Alpine; o código novo é limitado a
esses dois hooks.

### IRQ do MT6357 e teclas do PMIC no 6.18 — 2026-10-26

Reutilizado: `mt6358-irq.c` (MT6357, GPL-2.0), a EINT do `pinctrl-mt6765`
(descritor interno 180 = EINT144, patch 0013) e `mtk-pmic-keys.c`
(`mediatek,mt6357-keys`, GPL-2.0), todos do Linux 6.18.58.

Achado no upstream: `mt6357_regs` usa as máscaras de reset do MT6397, e a
homekey passa `MTK_PMIC_HOMEKEY_INDEX` (BIT(0)). Pelo `upmu_hw.h` vendor, o
`TOP_RST_MISC` (0x14c) do MT6357 segue o layout do MT6331: bit 0 é
`RG_WDTRSTB_EN`, os bits 8/9 são `HOMEKEY/PWRKEY_RST_EN` e os bits 13:12 são
`PWRKEY_RST_TD`. O probe sem correção alteraria o reset por watchdog e o
reset por pressão longa.

Segundo achado: as máscaras de intsel `0x5`/`0xa` ligam também as
interrupções de soltura, e o MFD fornece `powerkey_r`/`homekey_r`, mas
`mt6357_regs` não define `key_release_irq`. Resultado: só o primeiro
"pressionado" de cada tecla é relatado, e nunca o "solto".

Extensão mínima: `k40s-mt6357-pmic-keys-v2.patch`, candidata a upstream:
- reaproveita as constantes `MT6331_*` que já existem no driver;
- liga `key_release_irq`, como no MT6358.

O DT usa modo 2 e tempo 1 para reproduzir o `0x1325` deixado pelo LK; no
aparelho o valor ficou igual antes e depois do probe. O módulo é externo
(`4eb0f58d…`) e carregado só por `insmod`. Validado no aparelho: 3× Vol−
(114) e 3× Power (116), cada um pressionado/solto (ver
`lts-native-resident.md`).

### I2C5, MT6371 e backlight no 6.18 — 2026-10-26

Reutilizado sem alteração, tudo do Linux 6.18.58:
- `drivers/mfd/mt6370.c` + `mt6370.h` (GPL-2.0), que aceita
  `VENID_MT6371`; DEVINFO lido `0xF4`;
- `drivers/video/backlight/mt6370-backlight.c` (GPL-2.0);
- o `i2c-mt65xx` já usado no I2C0 nativo.

MFD e backlight foram compilados como módulos externos, com o mesmo método
do keypad. Código novo: só DT.

Efeitos de probe/erro, conferidos na fonte:
- o MFD lê o DEVINFO e mascara as IRQs do MT6371;
- o backlight só faz OR em PWM e BSTCTRL, ajusta `BL_EN` com os canais do
  DT e grava o brilho inicial.

Com os canais 15 e o brilho 679 (o máximo do 4.9 = LG), os registradores
`0xA0`–`0xA5` ficaram idênticos antes e depois. `mt6370-charger` (que
mudaria USBCHGEN/ILIM/ICHG/IINLMTSEL) e `mt6370-regulator` (bias do
display) não foram carregados: carga continua decisão do dono.
Decisão: reutilizar.

Antes de código novo, acrescentar uma linha/nota com: requisito; implementação
atual; projeto e arquivo alternativo; versão/commit/hash; SPDX/licença;
compatibilidade exata (SoC/IP/PMIC/placa/ARM32); dependências; escritas de
probe/falha/remove; testes de equivalência; impacto na recuperação; parte
específica inevitável; esforço; decisão reutilizar/estender/novo com justificativa.
Pendências devem permanecer explícitas. Nenhuma linha desta matriz, sozinha,
aprova ativação de hardware.

### MT6357 IIO: preservar verificacao de bancos completos — 2026-10-27

| Funcionalidade | Implementacao atual | Alternativa aberta | Compatibilidade | Esforco | Recomendacao |
| --- | --- | --- | --- | --- | --- |
| Recusar conversao com AUXADC ocupado e verificar limpeza | Captura LG/regmap validada verifica RQST0=0x110e, RQST2=0x1114 e reset=0x0f90; candidato IIO verifica apenas o bit solicitado | Linux stable 6.18.58 `drivers/iio/adc/mt6359-auxadc.c`, commit `2926d88bb7fc4608fd942453d929c39e4e5ec006`, GPL-2.0-only, SHA256 `74b50fc1602bbf9a180950c77485ad687818e0385e5154b60ed99a876d2eb146`, mais os onze patches staging existentes | MT6357/ARM32 via MFD/PWRAP/regmap; nao e exclusao atomica contra SCP/GPS; nao generalizar a Qualcomm/SPMI | Pequeno: leituras antes/depois da aquisicao e testes C de falhas | Estender o driver existente somente para `shared_reset`, manter outros PMICs e recuperacao intactos; nao criar provider paralelo |

Auditoria anterior dos canais e licencas: `manifests/mt6357-auxadc-channel-audit-20261025.json`.
Origem upstream da familia:
https://lists.infradead.org/pipermail/linux-mediatek/2024-May/079757.html .
Busca complementar mainline/postmarketOS/MediaTek em 2026-10-27 nao confirmou
outro provider com essa politica; resultado limitado a busca, nao prova de ausencia.
Drivers Qualcomm VADC usam SPMI e outro protocolo: referencia de framework IIO,
nao substituto do MT6357. Fonte LG e backup continuam referencias da placa.

Extensao planejada `mt6357-auxadc-quiescent-banks-v1.patch`: sem novas escritas,
sem mudanca no probe/remove, sem reset/retry automatico. Antes da conversao,
erro de leitura ou banco ocupado impede qualquer SET/CLR. Depois do CLR, erro
ou banco/reset nao-zero invalida o resultado e trava novas aquisicoes pelo
`reset_error` existente. Erro de amostragem precede erro de limpeza; o primeiro
erro latched nao e apagado. A exclusao contra outro mestre permanece pendente.
Os efeitos de conversao e CLR sao os ja auditados; nenhuma carga/flash autorizada
por esta nota. O caminho de recuperacao e o modulo continuo validado nao mudam.
Escopo: caminho ordinario `read_adc`, nao o callback de impedancia `read_imp`.
Nao ler canais de impedancia/VBAT nem presumir que todos os 13 canais expostos
tenham adquirido essa protecao; BATADC e BAT_TEMP sao os proximos candidatos.
Resultado offline: modulo ARM32 linkado para o kernel nativo, 222 testes seguros
e 666 testes WSL (21 pulados), sem falhas. Manifesto com hashes, limites e
recuperacao preservada: `manifests/mt6357-auxadc-idle-banks-offline-20261027.json`.
Ainda sem DT ativado, bind, leitura fisica ou equivalencia de freshness.

### MT6357 IIO: integracao DT nativa — 2026-10-27

Reutilizar a celula `mt6357_devs` ja presente em `drivers/mfd/mt6397-core.c`
no mesmo commit Linux 6.18.58 acima; SPDX GPL-2.0-only. O caminho IRQ nativo
do perfil de teclas ja cria a celula pelo compatible, sem o shim regulator-only
usado pelos primeiros ensaios sem IRQ. Binding existente:
`Documentation/devicetree/bindings/iio/adc/mediatek,mt6359-auxadc.yaml`,
SPDX (GPL-2.0 OR BSD-2-Clause). Requer apenas `compatible` e
`#io-channel-cells = <1>`. Codigo especifico novo: somente um no DT sob o
MT6357 e um DTS de ensaio separado; nao alterar MFD, base validada ou ciclo.

O modulo externo com as doze correcoes auditadas permanece carregado apenas
por insmod explicito no ensaio. Probe le reset e registra IIO; nao converter
durante o probe, nao carregar modulo LG simultaneamente, nao ler todos os
atributos raw em lote. Remove via devm, sem reset/charger; a verificacao fisica
de limpeza ainda e necessaria. O DT nao adiciona consumidor de bateria,
politica de carga, corrente ou temperatura calibrada. Esforco pequeno;
decisao reutilizar binding/MFD/IIO e validar com DTC/dt-schema existentes.

Resultado fisico: `manifests/mt6357-native-iio-acquisition-20261027.json`.
Provider MT6357 registrado; tres pares BATADC/AP + BAT_TEMP lidos por sysfs,
sem modulo LG concorrente. BATADC 26690/26691 (aprox. 4,398 V), NTC 1635
(718,506 mV), nao temperatura calibrada. Unload removeu modulo e dispositivo;
retorno automatico ao 4.9, hash boot_a e A/B preservados. Nenhum outro canal
raw foi lido; nao prova freshness, calibracao, exclusao contra firmware ou
restauracao completa de registradores no remove.

Correcao da auditoria historica de exposicao (manifesto de 2026-10-25 mantido):
raw/scale sao 0644, nao 0444. A construcao real de info-mask instala store;
`iio_write_channel_info` recusa -EINVAL se `write_raw` esta ausente, como neste
driver. O teste antigo passou NULL e concluiu a permissao errada. Teste agora
compila o callback real e verifica a recusa antes de qualquer parser. Nao foi
tentada escrita fisica e nao e necessario mudar o driver para essa correcao.

### MT6357 IIO -> power_supply existente — 2026-10-27

| Funcionalidade | Implementacao atual | Alternativa aberta | Compatibilidade | Esforco | Recomendacao |
| --- | --- | --- | --- | --- | --- |
| Publicar tensao de bateria por interface padrao | IIO MT6357 BATADC fisicamente lido; modulo LG separado publica V/I/T | `drivers/power/supply/generic-adc-battery.c` do Linux 6.18.58, commit `2926d88bb7fc4608fd942453d929c39e4e5ec006`, SPDX GPL-2.0, SHA256 `8df38519335c3cbc7bbb4293af80f1d1c08528db591cb46909bdb0a899b138d9`, com patch supplier-errors-v1 ja testado/linkado | Consumidor IIO independente de SoC, ARM32; binding exige tensao entre terminais; BATADC/AP e candidato medido, nao FG/SOC | Pequeno: DT e ensaio do modulo existente | Reutilizar, mapear somente voltage; nao criar consumidor paralelo |

Pesquisa adicional mainline/Android common/postmarketOS: o consumidor generico
ja existe no upstream e no Android common; busca postmarketOS nao confirmou
um substituto especifico MT6357 com calibracao LG. Qualcomm pode reutilizar
esse consumidor IIO, mas seus providers SPMI nao substituem PWRAP/MT6357.
Proveniencia, patch, modulo e licenca preservados em
`manifests/generic-adc-battery-status-offline-20261026.json`.

Probe: obtem apenas canais nomeados no DT, registra power_supply e trabalho
de status. O uevent inicial do power_supply pode chamar get_property e iniciar
conversoes BATADC durante/apos o probe; nao classificar registro como passivo.
Nao ha charged-gpios, supplier, current/power/temperature nem comandos de carga
no DT deste ensaio. Status sem supplier deve permanecer Unknown pelo patch.
Falha de canal/registro retorna erro; recursos devm e delayed_work autocancel
limpam na retirada. Descarregar consumidor antes do provider IIO.

Limites: gab_read_channel multiplica o valor IIO processado por 1000 para a
interface em microvolts (perde a fracao de milivolt do IIO processado inteiro).
Nao mapear BAT_TEMP como temperature: e tensao NTC, ainda sem conversao/calibracao;
alem disso o fonte fixado multiplica tambem GAB_TEMP por 1000, conversao que
nao corresponde a millidegree IIO -> decigrau power_supply e exige auditoria
propria antes de usar temperatura. Nenhum controle eletrico, estimativa SOC ou
kernel de recuperacao alterado. O modulo LG validado continua preservado, sem
executar em paralelo com essa composicao.

Ensaio concluido: `manifests/mt6357-native-power-supply-20261027.json`.
Tres leituras `voltage_now=4396000` uV via power_supply e `status=Unknown`;
uevent confirma ambos, sem current/temp/capacity/charge_counter expostos.
Consumer removido antes do IIO; ambos desapareceram e a recuperacao automatica
restaurou 4.9/boot_a/A-B conhecidos. Sao leituras nominais, nao injecao de falha,
prova de freshness, suspend/resume ou garantia de ausencia de corridas.
Nenhum C novo: modulo consumidor e patch anteriormente linkados reutilizados.

### Temperatura: reutilizar correcao upstream de unidades — 2026-10-27

| Funcionalidade | Atual | Alternativa aberta | Compatibilidade | Esforco | Recomendacao |
| --- | --- | --- | --- | --- | --- |
| Converter IIO_TEMP processado para POWER_SUPPLY_PROP_TEMP | generic-adc-battery 6.18.58 multiplica todos os canais por 1000 | Commit upstream `6bca94e64255053ab2aa56f2588fda73d399b790`, Svyatoslav Ryhel, aplicado por Sebastian Reichel; mesmo `generic-adc-battery.c`, SPDX GPL-2.0 | Independente de SoC/ARM32; exige temperatura ja calibrada em milliCelsius, nao tensao BAT_TEMP | Pequeno backport apos supplier-errors, testes de unidades/erros e link ARM32 | Reutilizar patch publicado, sem reimplementar conversor |

Commit e diff conferidos na API do repositorio torvalds/linux em 2026-10-27:
https://github.com/torvalds/linux/commit/6bca94e64255053ab2aa56f2588fda73d399b790 .
Mensagem original: https://patch.msgid.link/20260926142905.206215-2-clamor95@gmail.com .
Nao atualizar checkout nem selecionar automaticamente o modulo novo.
Probe/erro/remove, canais, GPIO e status nao mudam; apenas gab_read_channel
retorna erro imediatamente, divide GAB_TEMP por 100 e preserva x1000 para os
outros canais. Nenhuma nova escrita PMIC ou politica de recuperacao.

O thermal-generic-adc ja exporta IIO_TEMP no fonte fixado (SHA256
`79fb9b36ee3280632880b46cb552bacf960bfb5bf81a1c38b9e4fe70d69112b6`,
GPL-2.0-only), mas sua interpolacao por tensao/clamp nao e a interpolacao por
resistencia/rejeicao de falhas e compensacao por corrente da LG. O teste deve
comparar o algoritmo real, nao presumir equivalencia por ambos lerem NTC.
Reutilizar a sequencia FG e modelo LG ja verificados; eventual cola IIO deve
consumir o AUXADC existente, sem criar outro escritor concorrente no ADC.
O modulo continuous validado permanece intocado. Nao publicar BAT_TEMP como
temperatura apenas porque o erro de unidade do consumidor foi corrigido.

Comparacao executada dos algoritmos reais: 4096 codigos NTC, 3333 aceitos pelo
modelo LG; a tabela de 21 pontos convertida para mV diferiu em 3284, erro maximo
600 milliCelsius; os 763 codigos rejeitados pela LG viraram endpoints no lookup.
Isto rejeita esta tabela simples, nao toda possivel tabela densa. Com raw0x86cb,
o modelo compensado retorna 339/347/330 deciC para FG0/3200/62335. Sem FG nao
ha equivalencia a temperatura LG compensada. Manifesto:
`manifests/mt6357-temperature-reuse-20261027.json`.

Efeito adicional conferido antes de expor TEMP: power_supply_core.c
(SHA256 `743ddce90195018e1860d0eec42442b6428e1d2db49d26a907fe8628676a7ea7`)
registra e habilita zona thermal se TEMP existir e no_thermal for falso.
thermal_core.c (SHA256 `3d6c52007ffe71f4f9e4d61941145c5acc7a5ca94475efb9274c74a939310c65`)
cria zona tripless com zero trips e intervalos zero; habilitar pode ler a
temperatura. Portanto generic-adc-battery com TEMP nao equivale ao antigo
modulo continuous com no_thermal=true. Nao adicionar trips/controle de carga
nem presumir probe passivo; revisar essa diferenca na integracao seguinte.

### Cola IIO para temperatura LG compensada — antes do C, 2026-10-27

| Funcionalidade | Implementacao atual | Alternativas e revisao/licenca | Compatibilidade | Esforco | Decisao |
| --- | --- | --- | --- | --- | --- |
| Publicar temperatura compensada como IIO_TEMP processado | continuous usa sequencia FG e temperature-model LG ja verificados; AUXADC upstream le BAT_TEMP com lock proprio | IIO consumer/provider, regmap, platform_driver e devm no Linux `2926d88bb7fc4608fd942453d929c39e4e5ec006`; ntc_thermistor GPL-2.0-or-later e thermal-generic-adc GPL-2.0-only comparados; modelo LG/FG GPL-2.0-only ja existente | Somente K40S/MT6357/ARM32 e calibracao auditada 62k/1,8V/Rfg100/tune1000/comp75+100; nao Qualcomm, nem outro NTC por nome | Medio, cola pequena e testes de fronteiras/lifecycle | Novo C somente para coordenar APIs existentes e modelo da placa; nao copiar algoritmo, sequencia FG ou protocolo ADC |

Buscas adicionais mainline/postmarketOS/Android MediaTek em 27/10 nao confirmaram
um conversor MT6357 com a compensacao LG. Product brief confirma existencia de
FG mas nao define esse algoritmo. A comparacao quantitativa anterior demonstra
por que tabela simples nao e substituto equivalente. Framework Qualcomm/SPMI
nao fornece a sequencia PWRAP/FG nem calibracao desta placa.

Planejado `kernel/modules/k40s-temperature-iio`: input BAT_TEMP via
`iio_read_channel_raw`, com identidade/canal/escala/ancestralidade conferidos;
FG via `current-sequence.h` existente sob device_lock do MFD e chip-id validado;
resultado via `temperature-model.h` existente, em milliCelsius. Cache usa
`continuous-policy.h` existente (1s, CLOCK_BOOTTIME); par NTC/FG rejeitado apos
500ms de boottime, inclusive suspensao. Esta guarda e mais estrita que a janela
monotonica antiga, nao uma relaxacao. Falha invalida cache e bloqueia retry ate
reprobe. Nao e exclusao atomica contra firmware nem captura simultanea.

Probe: somente obtencao/validacao de referencias, tipo/escala e MFD; sem ADC/FG
conversion ou escrita. IIO register, nao power_supply/thermal register. Remove
marca stopping sob mutex antes de devm unregister/release; leituras futuras
falham. Acesso concorrente/unbind do supplier exige testes proprios; nao
autorizar remover MFD/ADC enquanto este consumidor estiver ligado. Novo DT
compatible e token de laboratorio, nenhum binding/serie/auto-load selecionado
nesta fase. O modulo continuous, seus headers e recuperacao permanecem intactos.

Resultado staging: driver completo compilado em ARM32 e com APIs simuladas;
25 falhas de probe, 26 cenarios de captura em dois modos de commit, todos os
11 passos I/O do FG, fronteiras de cache/timeout e devm/owner/refcounts.
230 testes seguros e 674 WSL (21 pulados) passaram. Nao houve acesso ao aparelho.
Hashes, licencas, limites e pendencias:
`manifests/k40s-temperature-iio-offline-20261027.json`. Nenhum DT ativado.

### DT de laboratorio para temperatura IIO — 2026-10-27

Reutilizar o binding AUXADC MT6357 do Linux fixado e as propriedades IIO
`io-channels`, `io-channel-names`, `#io-channel-cells`; referencia PMIC por
phandle `lge,pmic` para a cola K40S ja auditada. Novo schema local apenas
descreve esse contrato, nao uma API upstream aceita. Sem mantenedor upstream
atribuido (maintainers vazio), sem parametros de calibracao novos e sem
alterar MFD/regmap. GPL-2.0-only para o schema/DT proprios.

O DTS separado deriva do ensaio IIO nativo ja validado, mapeia BAT_TEMP (ID3)
para thermistor e MT6357 para lge,pmic. Nao inclui adc-battery, thermal-zones,
charger ou auto-load. Binding/probe/remove e limites sao os do candidato
`a9ccf59`; a validacao DTC/dt-schema deve anteceder um unico ciclo recuperavel
com insmod autenticado. Remover primeiro a cola e depois o AUXADC. Nao testar
unbind concorrente de fornecedores nem usar estas medidas para controle.

Ensaio IIO concluido com o modulo a6d30bc8 inalterado: 38100/38100/38000
milliCelsius, tres leituras imediatas de cache iguais, contador de remove
attempts=3 fault=0. Cola removida antes do ADC; nenhuma power_supply/thermal
registrada. Recuperacao automatica confirmou 4.9, hash boot_a e A/B iguais.
Schema positivo e tres copias negativas passaram nas verificacoes esperadas;
isto nao transforma o binding local em API upstream nem prova precisao com
termometro, exclusao de firmware ou suspend/unbind concorrente.
Evidencias: `manifests/k40s-temperature-iio-phone-20261027.json`.

### power_supply TEMP: contexto valido no caminho de erro — 2026-10-27

| Funcao | Existente / origem | Compatibilidade / efeitos | Esforco | Decisao |
| --- | --- | --- | --- | --- |
| Log de erro IIO durante exposicao/registro da bateria | generic-adc-battery.c GPL-2.0, Linux `2926d88bb7fc4608fd942453d929c39e4e5ec006`, apos supplier-errors e fix de temperatura upstream6bca94e6 | Core protege primeiras leituras por use_cnt, mas o ponteiro retornado adc_bat->psy so e atribuido apos register; callback recebe psy valido independentemente desse campo. Nao assumir que toda leitura ocorre apos a atribuicao | Pequeno, dois callbacks e testes C reais | Usar o psy recebido em get_property no helper de leitura/log, sem novo campo, lock ou driver |

Buscas em mainline/Android common/listas nao confirmaram correcao equivalente
fixada; nao atualizar checkout. Mudanca planejada: gab_read_channel recebe psy,
obtem drvdata pela API existente e usa psy->dev; os quatro chamadores passam
o contexto existente. Dados/unidades/status, probe/remove e IO permanecem iguais.
O teste deve diferenciar a guarda inicial real (-EAGAIN/-ENODEV, sem consulta
ao sensor) do estado pos-use_cnt antes de adc_bat->psy ser atribuido. Uma
reproducao em C desse estado nao prova corrida observada no telefone.
Sem injecao de falha fisica para investigar o log; preservar modulos anteriores.

Integracao DT planejada: manter BATADC e simple-battery da composicao validada,
adicionar somente IIO_TEMP canal0 do conversor compensado como temperature.
Reutilizar adc-battery.yaml e schema local do conversor; nenhum canal current,
power, GPIO charged ou supplier/charger novo. power_supply registra por padrao
zona thermal tripless (zero trips/polling), que sera explicitamente observada;
isso nao configura controle de carga nem protecao termica. Unload na ordem
consumidor power_supply -> conversor -> AUXADC, antes da recuperacao.

Integracao fisica concluida: tres amostras de voltage_now=4392000 uV,
power_supply temp=358 deciC e IIO/thermal=35800 milliC. Status Unknown;
current_now, capacity, charge_counter e trip_point_0_temp ausentes. Remocao
ordenada retirou power_supply/thermal antes dos fornecedores; conversor
terminou attempts=5 fault=0. Recuperacao automatica e verificacao SSH
independente confirmaram 4.9 e boot_a conhecida; A/B preservado. O teste
controlado de contexto de callback usa C/UBSAN no host, nao prova uma corrida
observada no telefone. Regressao: 233 testes offline e 677 WSL (21 pulados).
Hashes e limites: `manifests/k40s-battery-temperature-phone-20261027.json`.

### Corrente FG via IIO: sinal e precisao antes do codigo — 2026-10-27

| Funcionalidade | Implementacao atual | Alternativa / revisao / licenca | Compatibilidade e efeitos | Esforco | Recomendacao |
| --- | --- | --- | --- | --- | --- |
| Expor corrente ja capturada para compensar NTC | Cola K40S descarta magnitude/sinal apos calcular temperatura; continuous antigo publica uA | IIO_CURRENT e iio_read_channel_processed_scale, Linux `2926d88bb7fc4608fd942453d929c39e4e5ec006`, inkern.c GPL-2.0-only SHA efe82f50976cc73251d86669bb02cc9c71e4978b05af84f8f9eb5cfa567f3115; generic-adc-battery GPL-2.0 | FG/calibracao e cache existentes podem ser compartilhados sem outro latch. PROCESSED fracionario em mA preserva 0,1 mA; consumidor atual trunca mA antes de multiplicar por1000 | Pequeno para extensao; requer testes de ambos callbacks/cache/falhas | Reutilizar captura/cache e API scale=1000; nenhum novo modulo FG ou power_supply paralelo |
| Gauge pronto alternativo | MT6357 FG ja auditado a partir do fonte LG | Linux mesmo commit, mt6359-auxadc e pm8916_bms_vm; projetos postmarketOS/pmaports e MediaTek pesquisados | Nao encontrado gauge MT6357 pronto confirmado nesta arvore/buscas limitadas. AUXADC nao e o latch FG; PM8916 usa outro PMIC/protocolo, nao intercambiavel. Fontes downstream de outro PMIC exigem auditoria propria | Alto para substituicao desnecessaria | Nao trocar provider nem inferir compatibilidade por nome MT63xx |

Inconsistencia a resolver explicitamente antes de ligar o canal: adc-battery.yaml
descreve corrente saindo da bateria, mas Documentation/ABI/testing/sysfs-class-power
exige CURRENT_NOW positivo carregando e negativo descarregando; o consumidor
nao inverte sinal. Manter a ABI e o sinal ja validado no continuous, documentar
esse descompasso do binding em vez de inverter silenciosamente. Nenhuma nova
politica de status deve ser inferida da corrente. Precisao nao implica exatidao
eletrica ou calibracao externa.

Teste previo de contrato: compilar iio_multiply_value real e current-decode.h
inalterado, enumerar os 65536 payloads, comparar fracao mA x1000 com uA e
quantificar a perda do caminho anterior. Reutiliza teste host existente,
nao novo programa no telefone; KUnit IIO existente continua sendo a cobertura
do core, este complemento valida a composicao com o decoder da placa.
Nao muda probe/remove, DT, driver ou transporte nesta etapa.

Fontes consultadas: Linux local fixado; [generic-adc-battery upstream](https://github.com/torvalds/linux/blob/master/drivers/power/supply/generic-adc-battery.c),
[PM8916 BMS](https://linux.googlesource.com/linux/kernel/git/torvalds/linux/+/077ab8985ee278c3d8618182d335b0f0cd919e16/drivers/power/supply/pm8916_bms_vm.c)
e buscas em postmarketOS/pmaports sem candidato confirmado. REA/Ghidra sao
uteis se faltasse o decoder, mas nao substituem APIs do kernel e nao ha motivo
para decompilar novamente uma funcao com fonte e equivalencia ja registrados.

Resultado do contrato host: 65536 payloads preservados pelo caminho fracionario,
58978 perdiam precisao pelo caminho mA inteiro, erro maximo 900 uA. Sanitizador
UBSAN sem erro. Regressao: 234 testes seguros e 678 WSL, 21 pulados, zero
falhas. Logs privados `work/fg-iio-contract-{offline,full}-20261027-a.log`,
SHA-256 respectivamente 49397075bdecdcf38cde6ef67ad9bb948f3b232388de1a16d335fcbcd6eeaf06
e 20b529460a3293cd47f1ec6700d360f635141cde651f9988b37bce4305c1f477.
Mensagens de telefone nessa suite sao mocks, nao eventos fisicos. Este teste
nao liga o canal current nem valida precisao eletrica, cache concorrente ou
o dispatch completo de iio_read_channel_processed_scale no kernel em execucao.

Extensao planejada: adicionar ao mesmo provider o canal1 IIO_CURRENT PROCESSED
fracionario (magnitude assinada em decimos de mA /10), mantendo canal0 e nome
existentes. Compartilhar mutex, amostra/cache, limite de idade e falha latched;
invalidar ambos juntos. Probe/remove nao ganham I/O ou dependencias. Nenhuma
nova sequencia FG, calibracao ou politica. O consumidor staging usa scale1000
somente para current; voltage/power/temp preservam o caminho ja validado.
Testar cache cruzado, sinais, canais invalidos, falhas/teardown para ambos.

Extensao compilada ARM32 e validada: 235 testes seguros, 679 WSL, 21 pulados.
No 6.18, current_now=6900/7500/10600 uA concordou com IIO=6,9/7,5/10,6 mA;
temperatura 34,4 C e tensao ~4,393 V. Remocao ordenada dos tres modulos e
recarga no mesmo boot passaram; fault=0. Sessao de 3600s mantida ativa por
pedido do usuario, com coletor confirmado vivo; recuperacao deste ciclo ainda
nao e alegada. Sinal de descarga foi testado no host, nao fisicamente, e nao
ha referencia externa para exatidao. Status permanece Unknown; sem SOC ou
controle de carga. Receipts: `manifests/k40s-current-iio-offline-20261027.json`
e `manifests/k40s-current-iio-phone-20261027.json`.

A mesma sessao tambem registrou os cinco modulos de touch/teclas/backlight
inalterados do recibo de coexistencia de 2026-10-26, sem a antiga aquisicao LG
paralela. Tres leituras V/I/T com esses drivers ativos passaram; erros de
header/CRC do touch ficaram zero, framebuffer simple 720x1560, brilho 679/679.
Nao houve novo gesto/botao humano nem teste de remove desses cinco drivers.
Observada uma corrente negativa -600 uA, mas sem referencia externa ou cabo
desconectado: nao e validacao fisica independente do sentido da corrente.
Avisos MFD de DMA mask/nos filhos ausentes registrados, nao ocultados. Todos
permanecem no kernel novo junto do coletor de recuperacao da sessao residente.

### SOC: auditar helper upstream antes de novo estimador — 2026-10-27

| Funcionalidade | Implementacao atual | Alternativa / origem / licenca | Compatibilidade e limites | Esforco | Decisao |
| --- | --- | --- | --- | --- | --- |
| Estimar porcentagem | Ausente; V/I/T padrao e CAR relativo antigo nao sao SOC | Linux `2926d88bb7fc4608fd942453d929c39e4e5ec006`, adc-battery-helper.c SHA 4d4f202f002cb9ed7f876f8b84c9035f02a083f5a079b55d59f3974d5087d4db e .h SHA b23e24efc1da2c21934ef2e298b04e5b16e274ead20c32c2d05947d5b6b9e58e, SPDX GPL-2.0+ | API pronta para V/I pareado, resistencia e OCV; usa 25C fixos, worker 5s/30s e cache. Nao usa CAR. Requer identidade/perfil, resistencia, CV e OCV confirmados | Medio | Reutilizacao preferencial, nao habilitar antes de validar falhas/supplied/cancelamento e metadados |
| Tabelas de bateria | simple-battery apenas nominal | Fonte LG lge/battery_BL-T44.dtsi SHA 3fa66d6ba23a78550de34acf8d11b601fece3ec2a40edcff3468ed27da049ee0; DTB/overlays backup ja verificados | Perfil LGE (LGC/TOCAD), nao jdm de mesmo nome: fabricantes/valores diferem. mmh55lm inclui lge e mapeia LGC_GEN2=0, TOCAD_GEN2=1. Coluna de descarga nao e porcentagem pronta. Licenca especifica desse arquivo sem SPDX ainda precisa comprovacao antes de redistribuir dados | Medio | Inspecao privada e comparacao com backup; nao publicar tabela convertida por suposicao |
| Drivers completos alternativos | FG MT6357 especifico | ug3105_battery e intel_dc_ti_battery do mesmo Linux, usuarios do helper; PM8916 BMS e postmarketOS pesquisados | UG3105 usa I2C/reset/standby de outro hardware; Intel/Qualcomm nao servem como driver deste PMIC. Pesquisas postmarketOS nao confirmaram substituto direto. REA nao necessario para helpers com fonte disponivel | Alto para copiar driver incompativel | Reutilizar helper/framework, nao comandos eletricos de outros chips |

Efeitos upstream: init chama leitura pelo worker e agenda refresh; suspend
cancela trabalho sincrono, resume reinicia medias. devm_delayed_work_autocancel
cuida do cancelamento na liberacao; ordem com unregister deve ser preservada.
Em erro de aquisicao worker pula atualizacao, reagenda e deixa capacidade/OCV
antigos; getters dessas estimativas nao verificam idade. supplied recebe int
diretamente em bool: retorno negativo vira true. Testar funcoes reais isoladas
antes de decidir correcoes; observacao host nao prova falha fisica.

Fontes: [helper upstream](https://kernel.googlesource.com/pub/scm/linux/kernel/git/bpf/bpf-next/+/master/drivers/power/supply/adc-battery-helper.c),
[usuario UG3105](https://code.googlesource.com/linux/torvalds/linux/+/de03b17ec046d81c4713bc54306579b9024fc513/drivers/power/supply/ug3105_battery.c).
A revisao usada para testes e a local fixada acima, nao master mutavel.

Reproducao host confirmou -ENODEV convertido para true e status FULL quando
OCV supera CV-38mV; 100 falhas de leitura consecutivas mantem CAPACITY/OCV
antigos enquanto CURRENT_NOW retorna erro. API simulada nao prova falha em
uso real. Correcao staging proposta somente para supplier: -ENODEV significa
nenhum fornecedor cadastrado (false); outros erros mantem STATUS_UNKNOWN e
nao atualizam estimativas nessa rodada. Sucesso nao negativo deve preservar
comportamento. Sem nova escrita, probe/remove ou worker extra. Validade/idade
de estimativas e inicializacao continuam bloqueadores separados, nao resolvidos
por esse patch. Nao selecionar em perfil nem carregar no telefone.

Comparacao privada com libfdt confirmou 10 perfis completos (300 cells cada):
battery0/1 x t0..t4 do fonte LGE, identicos aos bytes do DTB Android mesclado
SHA dc789caca5ac0451d15e5d933ceb125d5614f49125ae7ae86c1926931368a311.
Indices2/3 do backup nao estao nesse arquivo: sao dados herdados, nao atribuir
todos os quatro indices a essa BL-T44. A primeira expectativa de 20 perfis foi
rejeitada pelo teste e corrigida para os 10 realmente definidos. Isto vincula
as tabelas a placa, nao identifica qual fabricante esta fisicamente instalado.
Nenhuma tabela inteira foi copiada para Git ou convertida em porcentagem.

Licenca do helper GPL-2.0+ preservada (nao relabel como only). Fonte LG sem
SPDX: COPYING raiz declara GPLv2, mas origem/licenca individual dos dados deve
ser registrada antes de publicacao. Para a futura integracao, ainda exigir
callback V/I com janela temporal delimitada, guardas antes de qualquer callback
pre-init, invalidacao/idade dos estimadores e cancelamento antes de unregister.
Nao usar o boot atual carregando como prova de 100%, capacidade ou ciclo completo.

Prova desta etapa: modulo helper corrigido compilou ARM32 contra vmlinux.symvers
do kernel nativo, sem suprimir erros de modpost. Testes: 237 seguros e 681 WSL
(21 pulados), zero falhas. Comparacao usa libfdt diretamente: rascunho com
fdtget foi corretamente rejeitado pelo offline_guard, cuja lista nao mudou.
Recibo `manifests/adc-battery-helper-reuse-20261027.json`. Nao houve carga do
helper/novo SOC no telefone; sessao nativa continua ativa, recuperacao pendente.

### Validade das estimativas do helper — antes do patch (2026-10-27)

| Funcao | Atual | Reutilizacao / revisao / licenca | Limites e efeitos | Esforco | Recomendacao |
| --- | --- | --- | --- | --- | --- |
| Rejeitar SOC/OCV sem amostra ou apos falha | Helper mantem inteiros sem idade | adc-battery-helper existente, Linux `2926d88bb7fc4608fd942453d929c39e4e5ec006`, GPL-2.0+; mutex existente, ktime_get_boottime_ns e erros padrao power_supply | Estado pequeno de validade/erro/tempo, sem estimador paralelo. Falha invalida, sucesso worker revalida; consultas nao renovam idade. Prazo de laboratorio 60s, nao especificacao da bateria | Pequeno | Patch staging apos supplier-errors; nao carregar antes de completar lifecycle/metadados |

Comparacao adicional mainline/listas nao confirmou substituto pronto que
resolva validade neste helper fixado; postmarketOS, Qualcomm e MediaTek nao
substituem esse contrato generico. Inicializacao do mutex antes de registro
continua exigencia do futuro chamador; este patch NAO torna callbacks pre-init
seguros e nao altera probe/remove. Testar amostra inicial ausente, erros de
worker e getters V/I, cache expirado, limite exato e suspend via boottime,
recuperacao apos sucesso e equivalencia da estimativa quando valida.
Nao adicionar timer, thread, retry ou transporte. O worker existente continua
reagendando; nao alegar mudanca da politica de retry do provider K40S.

Patch compilado ARM32 sem suprimir modpost. Testes com funcoes/struct reais
verificaram ausencia inicial, erro e expiracao no limite, outputs preservados,
sucesso recuperando validade, resultado capacity invalido e -ENODEV de supplier
aceito sem confundir com erro de aquisicao. 237 testes seguros e 681 WSL
(21 pulados), zero falhas. Timestamp e do calculo da media, nao prova idade
de cada amostra da janela. Nenhuma mudanca em init/remove/suspend: callbacks
antes do mutex e ordem unregister/cancel continuam bloqueadores reais.
KUnit/concorrencia pendentes; nenhum SOC habilitado. Recibo:
`manifests/adc-battery-helper-validity-20261027.json`.

### Lifecycle do helper: preparar antes de publicar callbacks — 2026-10-27

| Funcionalidade | Atual | Alternativa reutilizada / revisao / licenca | Efeitos e limites | Esforco | Recomendacao |
| --- | --- | --- | --- | --- | --- |
| Callbacks pre-init e cancelamento final | Helper init e chamado apos registro da power_supply; mutex/work ainda nao existem durante callbacks anteriores | smp_load_acquire/store_release, mutex_init, devm_add_action_or_reset e cancel_delayed_work_sync do Linux `2926d88bb7fc4608fd942453d929c39e4e5ec006`; helper GPL-2.0+ | Gate false retorna EAGAIN sem lock; publicado somente apos init. Quiesce fecha entrada sob mutex e cancela fora dele. Worker/externals nao podem reagendar apos stopping. Sem nova API, transporte ou operacao PMIC | Pequeno/medio, testes de init/falhas/actions | Estender helper; preservar assinatura e dados/algoritmo validado |

Usar mutex_init convencional em vez de devm_mutex_init: a power_supply pode
ser registrada antes da inicializacao do helper; destruir o lock por devres
antes de unregister deixaria callbacks usando lock destruido. Como nos usuarios
upstream inspecionados, a struct do helper deve viver ate depois de unregister.
Nao destruir manualmente esse mutex durante quiesce. A nova action de quiesce
e registrada depois da action de autocancel, antes de iniciar o worker; ordem
inversa fecha callbacks/cancela antes da liberacao restante. Nao segurar lock
durante cancel_sync/flush. Falha anterior a publicacao deixa o gate fechado.

Comparacao dos dois usuarios upstream e APIs devm confirmou que nao e preciso
um novo framework de lifecycle. Testes devem executar funcoes C reais com
acoes LIFO, callbacks injetados antes/durante init, erros e callbacks tardios;
stubs sequenciais nao provam SMP/lockdep nem suspend concorrente. Sem habilitar
o helper no telefone apenas para completar essa auditoria.

Patch de lifecycle compilou ARM32 com fonte/header reais; oito cenarios de init,
callbacks antecipados/tardios e LIFO passaram com stubs que verificam lock e
cancelamento fora dele. 237 testes seguros e 681 WSL (21 pulados), zero falhas.
Sem promessa de SMP/lockdep/PM real; helper nao carregado. Recibo:
`manifests/adc-battery-helper-lifecycle-20261027.json`.

Na sessao nativa existente, leitura somente do campo chosen/lge,battery-id
retornou string NUL-terminated TOCAD_GEN2. O driver LGE original
lge_battery_id.c (SHA 6793439072d2e213281c19a34396be49634cb9a5591558b9215b373b0d0b819d,
GPLv2 explicita no header) interpreta esse campo como string e seleciona
profile-idx por correspondencia. Reutilizada essa interpretacao: fdtget no
backup Android fixado confirmou /odm/battery_id/TOCAD_GEN2 profile-idx=1,
manufacturer=TOCAD e model-name=BL-T44 herdado do pai. Nao carregar o driver
Android nem criar detector novo. Isso identifica o perfil informado pelo
firmware, nao prova fabricante por medicao externa, estado ou calibracao atual.

### KUnit do helper com APIs reais — antes do teste (2026-10-27)

| Funcao | Atual | Reutilizacao / origem / licenca | Compatibilidade e efeitos | Esforco | Decisao |
| --- | --- | --- | --- | --- | --- |
| Executar worker, locks e cancelamento sem stubs | C host sequencial | KUnit/kunit.py, UML, power_supply, devres groups, kthreads/completions/workqueue do Linux `2926d88bb7fc4608fd942453d929c39e4e5ec006`; runner proprio existente MIT, testes GPL-2.0-only, helper original GPL-2.0+ | Sem telefone/rede/hostfs/modulos. Root device e bateria sinteticos com tabela ficticia, nunca calibracao da placa. Incluir helper real no TU de teste exige CONFIG_ADC_BATTERY_HELPER desabilitado para nao duplicar simbolos | Medio | Estender runner isolado, nunca copiar logica do helper para um modelo paralelo |

O teste inclui fonte helper patchado diretamente apenas na arvore UML isolada;
nenhum arquivo GPL de terceiro e duplicado no repositorio. Aplica tres patches
auditados a fonte/hash fixados, verifica hashes antes do build e resultado
KUnit completo. Aquisicao e callback sintetico em RAM; locks/workqueue/core e
devres sao reais. Cancelar kthread antes de liberar fixture, liberar grupo
devres antes de root_device_unregister. Validar gate pre-init, estimativa OCV
com tabela simples, falha/recuperacao, expiracao, quiesce com leitor concorrente
e init sem metadados. Isto nao testa eletricidade, ARM/PMIC, suspend fisico
ou todos os interleavings SMP; preservar suites anteriores e recuperacao.

Resultado: a arvore UML v2 executou 18/18 casos em cinco suites, incluindo
os cinco casos reais do helper. O leitor completa ao menos uma consulta valida
antes do quiesce; kthread e encerrado antes de liberar grupo devres/fixture.
OCV usa tabela sintetica 4,2V=100/3,2V=0, retornando50 em3,7V, nao dados LG.
Gate pre-init, worker em erro/recuperacao, expiracao e init sem metadados passaram.
UP/sem lockdep: nao e prova SMP, suspend ou PMIC. Sem BUG/WARNING/Oops/panic
no filtro do log bruto; notices de console UML e falhas injetadas preservados.
v1 tambem passou e foi preservada; v2 melhora sincronizacao, nao retry automatico.
Evidencias: `manifests/adc-battery-helper-kunit-20261027.json`.

### Entrada V/I recente para consumidor SOC — antes do codigo (2026-10-27)

| Funcao | Atual | Reutilizacao / revisao / licenca | Compatibilidade/efeitos | Esforco | Decisao |
| --- | --- | --- | --- | --- | --- |
| Parear tensao e corrente para helper | BATADC separado, corrente pode ter cache de ate1s | MT6357 IIO upstream e iio_read_channel_processed_scale do Linux `2926d88bb7fc4608fd942453d929c39e4e5ec006`; cola K40S GPL-2.0-only existente | API IIO reutilizada, sem novo ADC/FG. Buffer IIO seria alternativa para captura continua, mas adicionaria trigger/buffer e nao tornaria ADC/FG atomicos. Qualcomm/REA nao fornecem protocolo comum para este PMIC | Medio | Acrescentar entrada opcional BATADC e saida voltage canal2 na mesma cola/cache |

Com BATADC opcional, validar mesmo IIO provider MT6357, canal0/15bits e
SCALE5400/2^15; usar processed_scale1000 para uV sem truncamento de mV.
Captura faz V, NTC e FG sob mutex da cola, janela total <=500ms em boottime;
reutiliza todas as sequencias e calibra LG sem alterar headers existentes.
Ler a saida voltage inicia captura NOVA, mesmo se o cache anterior ainda for
valido. I/T seguintes usam esse cache ou captura mais nova. O futuro consumidor
deve ler V primeiro, I depois e rejeitar callback inteiro acima de500ms: isso
limita idade relativa sem inventar promessa de conversao simultanea ou excluir
firmware. Nenhuma API nova paralela ao IIO. Sem entrada voltage, manter somente
os dois canais e operacoes existentes. Outros erros alem de ENODEV nao viram
fallback. Probe acrescenta validacao de referencia/escala, sem conversao; remove
invalida todos os outputs e libera refs devm. Nao auto-load/charger/reset.

Implementacao preparada e compilada ARM32. Testes do driver C completo mantem
vetores anteriores e acrescentam ausencia opcional,10 falhas de probe, nova
captura em V dentro do cache, I/T compartilhados, erros/range/deadline e
invalidacao sem retry. 237 testes seguros e681 WSL (21 pulados), zero falhas.
Schema aceita DT antigo/novo e rejeita contagem divergente; imagem de3600s
empacotada com mesmo kernel, componentes relidos e overlays conferidos.
Ainda nao iniciada: sessao anterior permanece no6.18. Nenhuma porcentagem
habilitada; callback V-primeiro/I-depois ainda precisa implementacao e teste.
Recibo: `manifests/k40s-paired-iio-offline-20261027.json`.

Validacao fisica posterior: sessao anterior encerrada com restauracao e A/B
verificados (`manifests/k40s-current-resident-recovery-20261027.json`). Na nova
imagem6.18, tres frames IIO retornaram4392,443/4392,938/4392,608mV,
-5,3/-3,1/-2,2mA e31,4C. Grupos power_supply separados produziram V/I/T;
cada leitura V inicia frame distinto, portanto nao comparar os dois grupos
como captura unica. O consumidor atual ainda arredonda V a mV. Remocao
ordenada PS/cola/ADC passou (7 capturas, fault0); todos recarregaram no mesmo
boot aos46,64s. Rootfs continua somente leitura. Sem referencia externa,
porcentagem, helper SOC ou controle de carregador. Sessao residente mantida
ativa com coletor de recuperacao existente, nao declarada restaurada.
Recibo: `manifests/k40s-paired-iio-phone-20261027.json`.

### Consumidor V/I para helper SOC — auditoria previa (2026-10-27)

| Funcao | Atual | Alternativa / revisao / licenca | Compatibilidade e efeitos | Esforco | Recomendacao |
| --- | --- | --- | --- | --- | --- |
| Callback V-primeiro/I-depois em uV/uA | generic-adc-battery le propriedades separadas; provider pareado ja medido | Linux `2926d88bb7fc4608fd942453d929c39e4e5ec006`: generic-adc-battery.c (GPL-2.0), adc-battery-helper (GPL-2.0+), intel_dc_ti_battery.c e ug3105_battery.c; IIO processed_scale e mutex/boottime existentes | Consumidores TI/UG3105 mostram contrato do helper, mas protocolos/registros nao sao MT6357. postmarketOS usa power_supply; backend Qualcomm FG nao compartilha este PMIC. REA nao substitui contrato IIO. Adicionar callback ao consumidor existente, nao novo driver/SOC | Pequeno para callback; integracao/helper/perfil posterior | Patch staging opt-in, default desabilitado, ensaiar callback via propriedades existentes antes do helper |

Modo experimental paired_input exige V e I do mesmo provider e tipos IIO
corretos; isso NAO prova pareamento em qualquer provider. Somente usar apos
validar contrato V-forca-captura/I-cache no perfil especifico. Mutex serializa
callbacks do consumidor, processed_scale1000 preserva uV/uA, boottime limita
callback inteiro a500ms. Resultados so publicados depois de ambas leituras e
deadline aprovados. Outros callers podem iniciar captura mais nova no provider;
nao prometer simultaneidade ou exclusao do firmware. Sem retry automatico.
Probe valida referencias/tipos antes do registro PS, sem nova leitura/escrita;
nenhum worker, IRQ, estado persistente, charger ou porcentagem novos. Remove
mantem devres e vida de canais ja existentes; mutex embutido sem devm_destroy
prematuro. Com opt-in desligado, todos os callbacks/efeitos anteriores devem
ser preservados. O callback tera assinatura do helper; conectar o helper e
metadados reais permanece etapa posterior. Nao selecionar na serie de boot.

Referencias conferidas no checkout fixado: intel_dc_ti_battery.c,
GPL-2.0-only, SHA25643798315f84e95b60e42acbbe20c05a014773ecdaf7755d834f65a364f050f12;
ug3105_battery.c, GPL-2.0+, SHA256b6eee6e7bc39cb525f508073873adb7cbccd0718030e37123712de677a84f5c5.
Fonte primaria online conferida para comparacao, sem substituir o pin local:
[generic-adc-battery upstream](https://github.com/torvalds/linux/blob/master/drivers/power/supply/generic-adc-battery.c).

Patch paired-input-v1 compilado ARM32 e ensaiado via getters existentes no
mesmo boot6.18: modo default retornou4392000uV; opt-in retornou4392608uV,
correntes600/1800/-5600uA e32,0C. Cada getter inicia callback diferente;
nao interpretar leituras de propriedades separadas como um unico par.
Remocao ordenada dos tres modulos e recarga passaram, provider14 capturas,
fault0. Suite offline238 e completa682 (21 pulados) passaram. Somente APIs
IIO/mutex/boottime existentes, sem conectar helper ainda. Arquivos de boot e
recuperacao inalterados; sessao residente mantida ativa. Recibo:
`manifests/generic-adc-battery-paired-input-20261027.json`.

### Conectar helper ao consumidor existente — auditoria previa (2026-10-27)

### Temperatura no estimador reutilizado — auditoria previa

### Composicao SOC e STATUS medido — auditoria previa2026-10-27

Offline concluido:24/24 KUnit no workspace kunit-adc-soc-status-20261027-v1,
incluindo fornecedor REAL power_supply emRAM,status0..4,erroEIO propagado
comoENODEV pelo core,outputintocado e capacidade independente50. Helper
inicializado,external_power_changed avanca poll_count e PM retornaestimativa.
Log work/kunit-adc-soc-status-run-20261027-a.log;nenhum telefone nesse ensaio.
24 testes direcionados servico/runner tambem passaram (nao suiteampla).
BuildARMhelperb4f00e7eddc6b267a00a9fabf116f5f5d22e6f3cfdc82ea438c51fe860adfd32,
consumer432c855a633e5c01de94b65cc673a960aa009d1d6c6376431ba9b8e418a231ea,
sem suprimir modpost. Servico mantemdefault anterior sem helper empacotado;
comhelper exigeTOCAD,5tabelas800bytes,hashes antes de I/O,carrega helper antes
do consumidor e remove consumidor antes do helper/provedores. SHA da identidade
04247282 incluiNUL e e verificado no manifestcontra DTlive. Nao altera offsets,
timers500ms/1s,retentativas,faultlatch,charger nem codigo de recuperacao.

Candidate imagem6b9855147ae7849d3090efed85542e93e1c1ef29cf75abbbde6b19432f738383,
ramdisk23978a974814dfc42cbe5952e5b69e191a0ad6b5a6265df8fda0041d23253c95,
DTBprivadodc17ae62. MesmozImage/DTmem/cmdline,pacoteextraidoidentico e
overlays passaram. Bootstaging contem copias somente dos3binarios necessarios;
nao e nova buildkernel nem modificacao de workspace nativo validado.
Kernel anterior encerrado por k40s-resident end,coletor80031 acompanha
recuperacao;nenhuma nova carga deSOC antes de conferirtermino/A-B/boot_a.

Aceite fisico basico SOC2026-10-27:recuperacao80031 terminouexit0,4.9.190 e
boot_a5ffea913 conferidos inclusiveSSH;captura dram-20261027-120831,A/B
before/after9f3448025c92cbb4e1feb4f020b7fea5deb50222962832b8fe408d753f92a117.
So depois inicioucoletor38296/imagem6b985514. Coldboot publicoucapacity99,
STATUSCharging (igualk40s-charge-state),OCV4391738uV,V4393103uV,I2800uA,
T33,3C. SOC1 no logstartup;parametros paired/estimate/status_from_supplierY.
Logs firstSHA05774c06e5b45641c2f029a83a51d65c995a26191f2a2ac90ecea843dbe395ce,
coexistencia emwork/native-soc-status-coexist-20261027-a.log;hashes de modulos
e chosen conferidos no aparelho. Touch/teclas/backlight/RTC seguem ativos.

Servico stop removeu generic e helper,PS ausente;MFD/RTC/touch preservados.
start voltou a publicar99/Charging,V4392608,I7800,T33,3C,WDTactive.
Log work/native-soc-status-restart-20261027-a.log,SHA
8ecd911bb1b827e732dba3eab375e28f2a4bfdd0d26db7877dfad6cef54ffefa.
Nao houve forceunload,retryautomatico ou escrita no rootfs instalado.

Ensaio unico s2idle com script INALTERADO:103,956->108,664s,RTC1910->1,
parent174,USB/SSH retornaram e ACKconfirmado. Capacity99 aposretorno,
Charging,V4392608,I-300,T33,3C. Logwork/native-soc-status-s2idle-20261027-b.log,
SHA6c587a32cbab2bfbc59e1942ad882b3ff3d3a7df45c8a92369f8995169dba9c6.
Primeira observacaoSSHexpirou na reenumeracao;segunda mesmaexecucao,nao
novo ensaio. Snapshotfinal153s:99,STATUSigualfornecedor,OCV4392752,
V4392443,I2800,T33,3C;alarmevazio,pm_testnone,debug0,UDCconfigured,
WDTactive,rootfsRO1,touchheader/crc0,brilho679. Log
work/native-soc-status-final-20261027-a.log,SHA
29741c1ff8507242a76aaaefc615cf3c0ff44939e2fcc133d7859b691fe927bc.
Frameinicial659953077ns rejeitadoETIME/latch0,preservando500ms/1s;
nao anunciar ausencia completa de erros transitorios. Sem WARNING/BUG/Oops
nesse filtro. Basico funcional aceito,nao calibracaoexterna,tracking de
descarga,aging,GM30,ensaioprolongado ou carga/thermalpolicydeproducao.
Percentual e estimado e nao deve comandar carregamento. Sessao38296 segue
no6.18 com coletorativo;recuperacao desta ultima sessao ainda pendente.
Proximo bloqueio de energia continua controle de carga/seguranca termica e
suspendprolongado com politicaWDTadequada;nao foram habilitados por esteSOC.

Entrega: porcentagem estimada e STATUS MT6371 medido na mesma PS,sem perder
V/I/T nem rollback. Reusar ambos patches ja ensaiados:helper opt-in e
supplier-status,em extensao de composicao do generic-adc-battery Linux2926d88
GPL-2.0. Nao alterar patches/binarios validados anteriores. Reusar
power_supply_get_property_from_supplier,helper PM/work/cancel e OpenRC.
STATUS fornecedor tem precedencia no getter;helper continua responsavel por
capacity/OCV,worker e PM. Caminho somenteSTATUS nao inicia worker/IRQ legado.
Falha fornecedor segue ENODEV do core,sem devolver estado presumido;nao
remapear para Charging ou estado interno do helper. Sem transporte PMIC novo.
Estimador interno ainda tem heuristica FULL por OCV;isso pode arredondar
capacity para100 enquanto STATUS medido dizCharging. Nao equivaler essa
estimativa a carga completa,GM30 ou entrada para controle eletrico.
Alternativas TI/UG3105/Qualcomm/pmaports nao implementam esse fornecedor
MT6371;API generica ja e a reutilizacao adequada. Esforco pequeno de
composicao,nao outro gauge. Verificar no KUnit com fornecedor/core reais:
precedencia,supplier em erro,estimativa permanece funcao independente,
external_power_changed e PM nao perdem o worker do helper. Depois buildARM,
perfil privado e ensaio temporario preservando imagem conhecida/recuperacao.

Entrega futura observavel: capacidade estimada a partir do perfil correto e
temperatura medida,nao25C presumidos. Linux2926d88 adc-battery-helper
GPL-2.0+ usa25C;power_supply_batinfo_ocv2cap ja seleciona a tabela de
temperatura mais proxima (nao interpola entre temperaturas). Reusar essa API
e POWER_SUPPLY_PROP_TEMP em deciC,sem segundo estimador/conversor IIO.
Users UG3105 e Intel TI auditados nao anunciam TEMP;mantem caminho25C.
GenericADC tem TEMP real e nao o encaminha de volta ao helper:sem recursao
do lock. Ler TEMP somente quando anunciado no descriptor,antes de atualizar
medias;erro invalida estimativa via caminho existente,sem fallback25 silencioso
em sensor quebrado. Probe/remove/trabalhos e default sem TEMP preservados.
Esforco pequeno,patch no helper existente,sem escrita PMIC. Teste com core
real deve distinguir tabelas25/50 e erro TEMP,outputs intocados;nao usar
tabela sintetica no telefone. Sem aprovacao de precisao/calibracao por mocks.
Alternativas MediaTek/Qualcomm/pmaports nao substituem o contrato generico.

Fonte LG aberta adicional localizada: mtk_battery_recovery.c,
SHA256a7c8e1dad9bb6b2da00d45c33f70c81225db958d1b0194acd5e0ac64b4b58b56,
GPLv2 explicita. fg_construct_battery_profile_by_qmax usa mah*10000/qmax
como profundidade de descarga,nao porcentagem restante. Codigo interpola
perfil/resistencia por temperatura e escolhe qmax/vboot conforme politica.
Portanto nao normalizar simplesmente pelo ultimo ponto nem copiar toda
politica de recovery (inclui comandos/IRQs/shutdown) para publicar SOC.
Perfis LG continuam privados ate proveniencia/licenca dos dados confirmadas;
essa fonte esclarece sem necessitar RE do daemon para essa regra especifica.

Perfil privado inicialmente recusado: tabela real tem plato33070 em linhas
consecutivas. Nao remover/resamplear pontos nem inventar tensoes para tornar
curva estritamente decrescente. Contrato alvo power_supply_ocv2cap_simple
aceita ordem nao-crescente:procura primeiro ocv>ponto e usa limites adjacentes;
fixp_linear_interpolate trata x0==x1. Testar funcoes REAIS com plato/limites
e UBSAN antes de ajustar a precondicao inicialmente estrita do novo conversor.
Aumentos de tensao ou mah nao-crescente continuam erros. Igualdade preserva
todos pontos e semantica do core,mas o salto na capacidade sobre plato e
uma limitacao explicita do modelo,nao calibracao/equivalencia GM30.

Preparacao do perfil privado: DTC/dt-schema/libfdt e adaptador existente
portkit.core.devicetree para validar/preservar DT. Nao ha conversor LG GM30
confirmado nas pesquisas mainline/pmaports/MediaTek/Qualcomm; ferramentas
genericas nao sabem a semantica mah/Qmax. Codigo MIT minimo de placa somente
para identidade/pins,unidades e DOD->capacidade. Input:backupdc789cac,
base6f4e2f1d e chosenTOCAD_GEN2capturado do proprio boot. Reusar regra LG
qmax*10 de mAh->0,1mAh e DOD=mah*10000/(qmax*10);capacidade restante
inteira clamp(100-DOD/100,0,100),voltagem10uV->uV. Nao normalizar pelo
ultimo ponto. Cinco tabelas100pontos cabem no binding LTS maxItems100;
nao aumentar limite nem resamplear dados. R inicial25C do primeiro ponto
em0,1mOhm->uOhm,helper depois estima R;nao e R constante calibrada em todaSOC.
CV4,43V e informacao do header LG,nao autorizacao para escreve-la no charger.
Toda tabela convertida permanece em artifacts privado;script/teste nao
carrega transporte,nao escreve checkoutvendor e nao altera DTfora battery-info.
Validar monotonia/tamanhos/identidade e invariantes com libfdt antes de salvar;
usar dt-schema diretamente. Perfil nao equivale a GM30 (aging,vboot,CAR,
pseudo1/100 e interpolacao termica nao portados),somente candidato estimado.

Pesquisa complementar2026-10-27: serie MT6397 AUXADCv5 deRyanBrue para
Amazon/MT8173 e RTC nvmem GPL-2.0-only sao candidatos de arquitetura,nao
substitutos register-compatible do MT6357. Cover RTC declara gauge ainda
nao pronto para envio;nao trocar implementacao local por analogia de nome.
https://lists.infradead.org/pipermail/linux-mediatek/2026-September/113562.html
https://lkml.rescloud.iu.edu/hypermail/linux/kernel/2610.3/00976.html

Resultado offline2026-10-27:composicao corrigida passou22/22 no workspace
kunit-adc-consumer-20261027-v2,sem mudarverificadores;log
`work/kunit-adc-consumer-run-20261027-b.log`,SHA25642cc9fca95682bfd9ec6fcd6fddf1c3e07809bb5e741fc28485eb663afb5f3de.
Com extensao TEMP,23/23 passaram em
kunit-adc-consumer-temperature-20261027-v1/runs/first/verified.json;
raw logSHAebbcd44affc1efafe477a9b2d409bc02252b1fc32eda61ac1f242eb55a64c340,
JSONSHA2d57c9806bf95092e4a3501487986ea7e31be13b767c2304fbdd73b206e435fb.
Teste novo observoucap50a32C/tabela25,cap30a50C eEIO comoutputintocado em
erroTEMP;recuperacao apos sucesso. Casos helper semTEMP continuaram25C.
Sem WARNING/BUG/Oops no verificador existente,sem telefone/SMP/PMIC.
Oito testes direcionados do runner passaram. PatchTEMP SHA
15d99995d4394e59b1054dc47a752fa5976064e10a9effddeb0b3cd6094ea8ec.
Modulos ARM32 contra kernelPM/WDT atual:helper
b4f00e7eddc6b267a00a9fabf116f5f5d22e6f3cfdc82ea438c51fe860adfd32,
consumer81d6be40f1a707e40e67c9d99e9f7357a15f2fd0c9daf3701695538ef7f44ffc.
ExtraSymbols do vmlinux exato,sem suprimir modpost;nao carregados.

Perfil privado gerado em artifacts/native-soc-tocad-profile-20261027-v1,
DTBSHAdc17ae62a4598c9ea94e0273e20cabbd66118b0b0a3051c177c3ffa56721eeb1.
Identidade capturada nesta sessaoTOCAD_GEN2 SHA
04247282d1b9227150bb81015ba1bf8bbaeaef0df7756c804b55e848a9897224.
Tres testes direcionados do conversor passaram,incluindo funcoes upstream
reais/fixp,plato e limites comUBSAN;log
`work/native-soc-profile-core-targeted-20261027-b.log`,SHA
0788b075416bfadb8b0c306742d88e9516be73d80e34b5435d859d5569564d01.
libfdt confirmou TODAS propriedades/nos/reservas fora das8 propriedades
adicionadas em battery-info identicos;5tabelas100pontos preservadas.
dt-mk-schema/dt-validate diretos com battery.yaml doLTS passaram (exit0,
nenhumdiagnostico). Log work/native-soc-tocad-schema-validation-20261027-a.log.
Validacao so do schema bateria;nao apaga erros MFD preexistentes da placa.
Catalogo698IDs nao e698testes executados.

SOC ainda NAO foi carregado/publicado. Antes de substituir o consumer atual,
integrar explicitamente preservacao do STATUS fornecedor (patch separado
status_from_supplier ainda nao composto com helper),metadados e limites
temporais do consumo V/I/T;nao deixar opcao desconhecida falhar no boot nem
trocar Charging medido por FULL inferido sem declarar diferenca. So entao
ensaio temporario com rollback da PS e ciclo existentes. Kernel residente
80031 continua inalterado,coletor ativo;nenhum reboot nesta etapa.

Retomada2026-10-27: a falha UML da composicao nao foi resolvida por relaxar
assertions. Reusar software_node_register/device_set_node do Linux2926d88
(drivers/base/swnode.c GPL-2.0) no fixture GPL-2.0-only: node registrado e
de vida explicita, nao managed compartilhado. Associar metadata primaria ao
parent ja registrado sem criar segunda notificacao sysfs; somente a nova
power_supply publica links desse node. Detach parent antes de unregister
e unregister node apos teardown da PS. Isso evita colisao de nomes parent/PS
e ownership managed duplicado,sem alterar driver real ou ignorar warnings.
Flush dos works deferred_register/changed da PS antes de medir cancelamento
do helper: preservar igualdade do contador e verificacao de teardown,nao
aceitar leituras tardias como verde. Sem nova API/driver/estimador ou ensaio
fisico. Auditorias mainline/pmaports/MediaTek/Qualcomm e licencas abaixo
continuam aplicaveis; prazo/validade/metadados do SOC nao serao removidos.

| Funcao | Implementacao atual | Alternativa / commit / licenca | Compatibilidade e efeitos | Esforco | Decisao |
| --- | --- | --- | --- | --- | --- |
| Estimativa OCV/capacity na bateria IIO | callback pareado validado, nenhum SOC | Linux `2926d88bb7fc4608fd942453d929c39e4e5ec006`, adc-battery-helper.c/h GPL-2.0+ com tres patches auditados/KUnit18 casos; consumidores UG3105 GPL-2.0+ e Intel TI GPL-2.0-only ja identificados acima | Layout helper-primeiro obrigatorio; usar callbacks/PM/devres existentes. Protocolos MediaTek/Qualcomm e tabelas postmarketOS nao substituem monitored-battery da placa. REA desnecessaria para este codigo-fonte disponivel | Medio | Estender generic-adc-battery (GPL-2.0), nao criar novo fuel gauge nem copiar estimador |

Plano staging: estimate_capacity opt-in separado e default-off, exige
paired_input. Helper deve ser primeiro campo de gab. Reutilizar lista de
propriedades upstream, deduplicar V/I ja presentes e manter TEMP/POWER pela
API anterior. Nao iniciar gab_work ou IRQ de charged no modo helper: usar
external_power_changed, worker/cancelamento e PM do helper. Adquirir GPIO
opcional com verificacao IS_ERR antes de registrar PS. Iniciar helper depois
do PS; metadados ausentes falham probe sem inventar tabela. Gate initialized
do helper protege callbacks pre-init; sua acao quiesce roda antes de liberar
PS/canais. Armazenamento gab alocado antes de todos eles sobrevive ao cleanup.
Kconfig deve selecionar ADC_BATTERY_HELPER para build in-tree; build modular
isolado passa a depender do modulo helper mesmo com opt-in desligado. Registrar
essa diferenca de dependencia, nao afirmar equivalencia binaria. Modo default
mantem callbacks/worker legado, nao registros/efeitoss de modulo identicos.
Nao carregar no telefone antes de verificar falhas de probe e lifecycle da
composicao; perfil real e temperatura/calibracao continuam requisitos separados.

Teste de composicao: reutilizar KUnit/UML, software_node/PROPERTY_ENTRY_REF,
IIO map e provider sintetico, power_supply e devres do mesmo Linux fixado.
Fixture GPL-2.0-only, runner MIT existente; fontes incluidas mantem licencas.
Provider somente RAM, sem regmap/transportes/telefone. Executar gab_probe real
com monitored-battery sintetico via API de propriedades padrao e verificar
metadados ausentes, erros de aquisicao/recuperacao, PM e cancelamento no teardown.
Desabilitar apenas autoregistro platform_driver na inclusao de teste; chamar
probe explicitamente. Helper normal e generic-adc-battery normais desabilitados
na config para nao duplicar objetos. Nao usar a tabela ficticia no aparelho.

### Entrega prioritaria: inicializacao V/I/T — 2026-10-27

Aceite: OpenRC inicia os tres modulos ja validados, power_supply publica V/I/T
atualizados, stop remove na ordem inversa e novo start funciona sem reboot.
Bloqueio atual: modulos sao carregados manualmente na sessao RAM. Percentual
nao e dependencia desta entrega; staging SOC/KUnit anterior permanece incompleto.

| Funcao | Atual | Reuso / versao / licenca | Compatibilidade / efeitos | Esforco | Decisao |
| --- | --- | --- | --- | --- | --- |
| Inicializar bateria IIO pelo init | insmod manual | OpenRC0.63.2 BSD-2-Clause e BusyBox do Alpine ja pinados; tres modulos dos recibos paired-iio/paired-input, Linux2926d88 e cola GPL-2.0-only | OpenRC gerencia start/stop; modprobe generico nao verifica confirmacao/identidades/RO do laboratorio. Sem driver ou daemon novo, somente servico MIT de placa com hash check, ordem de dependencias e rollback parcial | Pequeno | Reusar openrc-run, insmod/rmmod, verificar start/stop em RAM antes de incluir no boot |

Sem hooks novos de ADC/FG ou alteracao do ciclo de recuperacao. Servico nao
carrega helper SOC nem driver de carregador. Nao habilitar no rootfs permanente
nesta etapa. Fontes de modulos e hashes sao os recibos fisicos existentes.

Resultado funcional: servico `boards/k40s/openrc/k40s-battery-iio` iniciou,
recusou duplicacao sem descarregar modulos alheios e passou stop/start na sessao
RAM. Imagem temporaria `artifacts/native-battery-openrc-boot-20261027-v2/`
SHA25690cbcb59a169ae03b7568e30241a762aa989ff915b8fc0663d065f10bbe0b534
passou extracao/comparacao de kernel/ramdisk/DTB e overlays pelo empacotador
existente. Kernel88b5438 e DTBbb19f737 inalterados; somente payload RAM mudou.
O hook opcional em resident-prepare usa openrc-run, timeout4s e fd3 fechado;
imagens sem o arquivo de servico preservam o comportamento anterior.

No boot fisico, `battery_iio startup PASS` aos6,594s; servico listado em
OpenRC e V/I/T disponiveis antes de qualquer insmod manual. Tres consultas
seguidas deram4393103/4392608/4392773uV,6900/4700/4000uA e31,5C.
Propriedades444, rootfsRO1. `status=Unknown` permanece correto: deteccao de
alimentacao/estado ainda e proxima entrega, sem ativar carregador ou SOC.
Isto comprova atualizacao sob consulta; notificacao periodica uevent nao foi
adicionada nem alegada. Ainda e imagem de laboratorio, nao instalacao permanente.

Evidencias existentes (sem novo manifesto):
- `work/native-battery-openrc-autoboot-20261027-b.log`, SHA25670ccc477ae5ac751a562b4a02790634eb2d4116bf75e4e6ba5904a3226ac5eef;
- `work/native-battery-openrc-autoread-20261027-a.log`, SHA25645996c37449a6e11f7d17801905b62f005608c785dce116f7f1a0abacb4006fe;
- `work/native-battery-openrc-restart-20261027-a.log`, SHA256be0dedb30bbea74ee3f5e202c84d29237930afbeabefd7cd1599090b4915f770;
- testes direcionados do residente11/11 (`PYTHONPATH=tools`), log
  `work/native-battery-openrc-targeted-20261027-b.log`, SHA25600ca7b140ea7a254c3f44f69614645cba001b2e0ab39bf549690298aff859a0b.

Sessao anterior `native-paired-resident-session-20261027-a.log` terminou exit0,
Linux4.9/boot_a5ffea913 conferidos, A/B antes/depois9f344802 identicos;
log final SHA2562059b86c3b66b6b5580d0467ed7ec119cb7e9dfce286b417daf21f1c742dfbe9.
Sessao nova `work/native-battery-openrc-session-20261027-a.log` permanece ativa,
coletor10935 e limite3600s; restauracao desta nova sessao ainda pendente.

SOC permanece staging separado: o ensaio UML de composicao anterior executou
21/22 e encontrou compartilhamento indevido de software_node gerenciado no
fixture (warning/refcount) e uma assercao de suspend que confundia worker com
leituras feitas pelo core. Resultado falho preservado em
`work/kunit-adc-consumer-run-20261027-a.log` e workspace v1. Nao aprovado,
nao carregado nesta imagem, nao corrigido relaxando testes. Nao bloqueia V/I/T.

### Entrega: fonte USB presente no 6.18 nativo — antes da adaptacao

Aceite inicial: `k40s-usb/online` somente leitura, com cache limitado a1s,
coexistindo com V/I/T por mais que a janela antiga15s; erro nao devolve dado
antigo e unload remove a classe. Cabo permanece conectado: nao alegar transicao
fisica0/1 nem STATUS Charging apenas por haver alimentacao.

| Funcao | Atual | Reuso / revisao / licenca | Compatibilidade / efeitos | Esforco | Decisao |
| --- | --- | --- | --- | --- | --- |
| Presenca de alimentacao USB | k40s-usb-online, leitura LG CHRDET ja ensaiada no kernel diagnostico, limitada15s | Reusar esse modulo GPL-2.0-only e usb-online-read.h sem mudar registros; regmap/power_supply e MT6357_CHR_TOP_CON0 no Linux2926d88. MT6360 charger (SHAf5aa86b6) usa outro PMIC/protocolo; MT6370 charger (SHA5844f4b9, ambos GPL-2.0-only) configura carga no probe | Nenhum driver CHRDET MT6357 dedicado encontrado nessa arvore upstream; postmarketOS usa mesmos frameworks, Qualcomm FG nao e compativel. LG4.9 upmu_get_rgs_chrdet e fonte primaria existente; REA desnecessaria | Pequeno | Estender modo opt-in nativo do modulo existente; nao carregar charger upstream nem criar novo driver |

Preservar modo diagnostico/token antigo15s/4tentativas. Modo nativo exige
novo token+release nativo, cache por boottime e latch de falha; somente leituras
SWCID/0xa88. Sem IRQ/worker/limites/USB-type, sem registrar supply como fonte
da bateria (presenca nao prova corrente de carga). Exit fecha aquisicao sob
mutex antes de unregister/put. Politica temporaria antiga nao e generalizada ou
relaxada no verificador do ciclo. Estender testes existentes apenas nos caminhos
afetados, compilar ARM32 e ensaiar na sessao residente, sem novo flash.

Integrado no telefone: `k40s-usb/online=1`, typeUSB/mode444; consultas novas
apos43,7s (alem da janela legada), unload/recarga e coexistencia V/I/T passaram.
attempts3/failed0 no unload. Modulo242c761a9a7d, fonte8d9ab878b1df;
quatro testes direcionados passaram, incluindo modo antigo preservado e cache
por boottime/falha/stopping no novo. Evidencia e limites em
`docs/lts-usb-online.md`, sem novo manifesto ou suite ampla. Detector deixado
ativo so na sessao RAM; sem novo flash/boot, SOC, IRQ ou charger configurado.

### Estado real MT6371 por regmap nativo — auditoria previa

Aceite: STATUS lido pelo I2C nativo, identidadef4 e presenca externa coerentes,
sem MMIO/FIFO legado nem escritas de configuracao do carregador; classe somente
leitura, V/I/T preservados e unload limpo. Nao implica SOC100% quando Full.

| Funcao | Atual | Alternativa / revisao / licenca | Compatibilidade / efeitos | Esforco | Decisao |
| --- | --- | --- | --- | --- | --- |
| STATUS MT6371 | k40s-charge-state usa FIFO legado e snapshot5s | Linux2926d88 mt6370-charger.c GPL-2.0-only, get_status e enum/CHG_STAT14a6..7; decoder existente igual. LG4.9 define4a/maskc0 e leitura volatil. mt6370 MFD GPL-2.0-only modulo282fee16 validado fornece dev_get_regmap | Charger upstream escreve CHGCTRL no probe: nao carregar. Reusar MFD/I2C ja auditados e decoder existente. MT6360, Qualcomm e postmarketOS nao mudam protocolo deste chip; fonte disponivel dispensa REA | Pequeno | Estender modo nativo explicito do modulo existente; nao criar segundo transporte ou controlador |

Novo modo: token/release nativo exclusivos, obter I2C device pelo DT e usar
regmap do driver MFD associado sob device_lock; ler somente DEVINFO100=f4 e
CHG_STAT14a. Reutilizar presence MT6357 antes/depois e decoder, deadline500ms,
mutex e latch de erro. Nao registrar enquanto primeiro retrato falha. Teardown
fecha novas leituras e unregister antes de soltar refs dos dois pais. Modo
legado preservado e separado. A MFD reutilizada pode configurar mascaras IRQ
no seu probe ja auditado; nao chamar isso de ausencia de toda escrita I2C.
O leitor novo nao escreve PMIC nem inicia charger, ADC ou IRQ proprio.

Integracao no consumidor V/I/T: reutilizar
power_supply_get_property_from_supplier do mesmo Linux, GPL-2.0-only, em vez
de outra leitura de registros ou copia do decoder. API escolhe primeiro
supplier que responde a STATUS; topologia de laboratorio deve ter somente o
leitor MT6371 como supplier de adc-battery, USB-presenca permanece separado.
API converte falhas dos suppliers em ENODEV; nao esconder isso como estado
antigo. Patch staging status_from_supplier default-off; nesse modo nao iniciar
worker/IRQ legado de status, encaminhar notificacoes pelo power_supply_changed
e PM nao toca trabalho inexistente. V/I/T continuam IIO. O leitor anuncia
supplied_to=adc-battery apenas no novo modo; nenhum vinculo no legado.

Entrega no aparelho passou: STATUS Charging em adc-battery, com V/I/T e
USB online preservados; retirada do leitor causa ENODEV e nao estado antigo,
recarga restaura STATUS. Sem reboot ou novo controle de carga. Detalhes,
modulos/hashes e limites registrados em `docs/lts-charge-state.md`. Fontes
legadas/MMIO seguem preservadas, mas nao executadas no modo nativo.

### Boot automatico V/I/T + alimentacao + STATUS — antes da integracao

Reusar o mesmo servico OpenRC0.63.2 e seis modulos ja ensaiados. Entrega:
imagem RAM inicia USB online e STATUS em adc-battery antes do SSH, com stop/
start e hashes. Nenhum novo driver/API. Perfil antigo de tres modulos preservado
quando arquivo k40s_charge_state.ko nao e empacotado. Novo perfil tem seis hashes
e tokens nativos explicitos. MFD MT6370 compartilhado fica carregado ate reset:
nao inventar unload/reprobe do MFD, pois isso nao foi validado. Stop remove
consumer/status/USB/cola/ADC, e nao recursos de backlight/MFD alheios. Falha
parcial remove somente modulos cuja ausencia foi exigida no start_pre.
Reusar empacotador/overlays e ciclo existentes; sem relaxar recuperacao.

Entrega passou no boot: imagem181cf1feca1b50c69eacca40e4c687a75c778f3150058a068dd58d7e62ff17a0,
ramdisk27336f13d897d33025698d760c87add18f945df31c195f6adf3e2db7cddef452,
kernel/DTB inalterados e componentes extraidos/overlays verificados pelo script
existente. Aos5,897s o servico ja tinha iniciado USB-presenca e STATUS.
Primeira consulta aos37,38s: adc-battery Charging,4393762uV,-3100uA,30,6C;
k40s-usb online1; rootfsRO1. Sem insmod manual apos esse boot.

Start/stop do perfil completo passou, MFD compartilhado permaneceu carregado.
Ausencia injetada de um arquivo de modulo foi recusada pelo hash antes de
carregar recursos; arquivo restaurado permitiu start. Perfil antigo de tres
modulos tambem foi exercitado com o novo servico: V/I/T e statusUnknown,
sem fonte USB/STATUS; depois perfil completo restaurado e Charging/online1.
Onze testes direcionados do residente passaram; nenhum teste amplo repetido.

Evidencias, sem novo manifesto:
- `work/native-energy-openrc-autoboot-20261027-a.log`, SHA256324d3e01a3caabe8d034b3a00fd71012466d25cf1fe32f06996d350844272c20;
- `work/native-energy-service-lifecycle-20261027-a.log`, SHA256386da949a2c18b385d129763772ab3192da0e4eec406950897e8f37bdf9b92f6;
- `work/native-energy-legacy-profile-parity-20261027-a.log`, SHA256f5d3b293bc5593ab82c60dd924fd743600701f96ac69d971926256469abf104b.

Recuperacao da sessao anterior10935 concluida: boot_a5ffea913, A/B9f344802
antes/depois e Linux4.9 verificados. Log final
`work/native-battery-openrc-session-20261027-a.log`, SHA256726f093484f88714d08d0b32de86ededd6dd08aac894d431c383e21df082d6bb.
Nova sessao `work/native-energy-openrc-session-20261027-a.log`, coletor96118,
continua ativa com limite3600s; restauracao desta ainda nao verificada.

Proximo bloqueio concreto de PM, identificado somente por leitura:
sysfs oferece freeze/mem e s2idle/[deep], mas nao RTC, pm_test, cpuidle ou
politicas cpufreq ativas. CONFIG_PM_DEBUG esta desligado. O mtk_wdt_suspend
upstream desta arvore chama mtk_wdt_stop quando ativo: uma tentativa real de
suspensao pode remover o mecanismo atual de recuperacao. Nao executar echo
freeze/mem antes de preparar despertar/recuperacao compativeis. Nao foi
alterado PM nem declarada suspensao aprovada. Evidencia:
`work/native-energy-pm-capabilities-20261027-a.log`, SHA25667e07491540f56b36621b295a7c5926583bebb54b03b6fbac13727e71fd02bad.

### PM: primeiro teste com retorno automatico — auditoria previa

Entrega intermediaria: pm_test/freezer do kernel disponivel em build isolada,
para congelar/descongelar processos sem passar por suspend de dispositivos.
Isto desbloqueia o primeiro passo de PM; nao substitui suspend/resume real.
Watchdog ativo confirmado por misc/watchdog ->10007000.watchdog ->mtk-wdt;
atributos ausentes eram CONFIG_WATCHDOG_SYSFS=n, nao ausencia do watchdog.

| Funcao | Atual | Reuso / versao / licenca | Compatibilidade / efeitos | Esforco | Decisao |
| --- | --- | --- | --- | --- | --- |
| Testar congelamento sem RTC ou dispositivo suspenso | PM_DEBUG=n, sem pm_test | Linux2926d88, kernel/power/suspend.c (GPL-2.0), pm_test/freezer e CONFIG_PM_DEBUG; watchdog sysfs existente | Core volta apos espera padrao5s antes de suspend_devices_and_enter. MTK WDT so para na fase de dispositivos; notificador NO_PING nao e registrado por esse driver. Codigo comum a MediaTek/Qualcomm; nao ha protocolo board novo. Ferramentas postmarketOS/userspace nao substituem esse caminho do core; pm-graph e rtcwake exigem instrumentacao/RTC desnecessarios ou indisponiveis agora | Pequeno, config/build isolada | Reusar pm_test, sem novo modulo/diagnostico C ou patch de watchdog |

Fontes conferidas: suspend.c SHA2560f5cd354b1523364549e8cfc6dc4bbd781edc207b58a664617c4b971c119ae24;
kernel/power/Kconfig SHA25601b906bb84cdf3def02a6d7c120b6d27348a5f67da9dbc565761e7529a4fa0a6;
mtk_wdt.c SHA2566e8230dff7db590f16bdc83918220da48be57c8a594cd3f0917f4c0e0018da9b.
Documentacao primaria: https://docs.kernel.org/power/basic-pm-debugging.html .
Nao alterar mtk_wdt_stop/suspend, BROM ou ciclo validado. Habilitar apenas
PM_DEBUG/PM_SLEEP_DEBUG e WATCHDOG_SYSFS; desabilitar testes automaticos de
boot, PM_TRACE/RTC e DPM watchdog de panic. Conferir delta de config antes
do build. Modulos da nova imagem precisam ser recompilados contra essa config,
nao reutilizar binarios antigos so porque o vermagic tem mesmo nome.

Build isolada PM_DEBUG concluida em 2026-10-27, sem alterar o kernel anterior.
Fragmento `kernel/devices/lg-k40s/lts-6.18/native-pm-debug.config`;
config SHA256 f235cbcfac6bd2f1dac5669bbb422b6af5c2af8d9393c3773c82659e02db9246,
zImage 04f1a556cca6fd4ccba2770e82f4ffdcdc5b29864fa4eb00d89e8cc1afdac222.
Os oito modulos foram recompilados contra esse output: os hashes resultantes
coincidem com os anteriores, permitindo manter as listas de integridade existentes.
Falhas de includes e de module.lds preservadas nos logs A/B; includes corretos
e `make modules_prepare` resolveram a compilacao, sem suprimir erros de modpost.
Log concluido `work/native-pm-debug-modules-build-20261027-c.log`.
Imagem temporaria 3ce87b53435828a903d9e71a14a1eee5ac5ac0dfbe513ae1013cc099e051f8f5,
ramdisk 211c4e5cffa14e9330c245a292ae17d460fcece542a7816fdb3ef8394dd5d118;
extracao comparada e overlays aprovados pelo empacotador existente.
Ainda nao prova freezer, suspend/resume nem economia de energia no hardware.

Ensaio fisico freezer aprovado: `work/native-pm-freezer-20261027-a.log`.
Kernel novo iniciou com V/I/T, Charging e SSH; watchdog mtk-wdt ativo/15s,
pm_test inicialmente none e atraso upstream5s. Com verificacao explicita de
`[freezer]`, foi escrito freeze em power/state. Retornou de41,95s a47,01s;
log confirma freeze de userspace/tasks, espera5s, thaw e suspend exit.
pm_test restaurado para none; watchdog continuou ativo, V4393432uV,
I2800uA,T30,1C,Charging. Nenhum device suspend, deep sleep ou ganho de consumo
foi testado. Nao alterar o watchdog para avancar sem preservar recuperacao.

Uma notificacao power_supply apos retorno produziu voltage_now=-ETIMEDOUT.
Tres consultas completas seguintes passaram sem recarga dos modulos
(`work/native-pm-freezer-followup-20261027-a.log`). Nao houve mensagem de
falha/latch do provider. A leitura do codigo localiza outro retorno -ETIMEDOUT
no limite500ms do par do consumidor, sem latch; uma aquisicao atravessando
o freezer e compativel com esse resultado, mas nao foi rastreada para provar
a cronologia. Preservar o limite e a recusa de amostra, nao esconder o erro.

Sessao anterior96118 terminou com exit0: restauracao5ffea913, Linux4.9 e A/B
9f344802 antes/depois verificados. Sessao PM atual89389 permanece residente,
coletor ativo, imagem3ce87b53; recuperacao desta sessao ainda pendente.

Proximo candidato concreto de despertar: RTC upstream `rtc-mt6397.c` ja tem
compatible mediatek,mt6357-rtc nesta mesma revisao, GPL-2.0-only,
SHA256fa9fb999e4f22cde90b2a931e8ac547c87d3e267c94be6e6ab48f286fae2881c.
Leitura atual confirma cell mt6357-rtc e PMIC IRQ nativos criados; falta node
RTC/driver habilitado, nao o IRQ ausente dos primeiros perfis. Nao inventar
RTC paralelo nem presumir wakeup aprovado. Antes de integrar, registrar
efeitos do registro/IRQ/remove e conferir binding MFD mediatek,mt6357.yaml.

### RTC MT6357: integracao minima upstream, auditoria previa

| Funcionalidade | Atual | Alternativa / origem / revisao / licenca | Compatibilidade e efeitos | Esforco | Recomendacao |
| --- | --- | --- | --- | --- | --- |
| Relogio RTC para preparar despertar futuro | Cell mt6357-rtc sem node OF; RTC_DRV_MT6397=n | Linux6.18.58,2926d88bb7fc4608fd942453d929c39e4e5ec006,drivers/rtc/rtc-mt6397.c,GPL-2.0-only; binding MFD mediatek,mt6357.yaml,GPL-2.0-only OR BSD-2-Clause | Compatible MT6357 explicito,regmap MFD,base0x588/size0x3c/IRQ RTC fornecidos pelo core; ARM32 suportado. Probe requer OF data e IRQ; devm_request_threaded_irq desmascara IRQ PMIC. Registro le hora/alarme, inicializa fila RAM do alarme existente, pode ajustar hora do sistema via hctosys; nao chama set_time/set_alarm nesse caminho. IRQ de alarme pode escrever RTC_IRQ_EN e WRTGR para reconhecer/desarmar; portanto bind NAO e puramente passivo. Remove devm desregistra classe/IRQ, nao restaura arbitrariamente alarmes do firmware. Qualcomm rtc-pm8xxx e SPMI/PM8xxx, nao compativel com MT6357. Busca postmarketOS nao confirmou alternativa que melhore esse driver ja MediaTek/upstream; ferramentas RE nao necessarias com fonte disponivel | Pequeno, DT de ensaio e modulo externo sem alterar C | Reusar driver intacto. Primeiro somente ler hora, sem programar wakealarm/set_time nem suspender dispositivos; preservar watchdog e coletor. Teste de alarme/despertar separado |

Fontes externas consultadas: binding upstream
https://kernel.googlesource.com/pub/scm/linux/kernel/git/torvalds/linux/+/194fcd20ebccbc34bba80d7d9b203920087bb01d/Documentation/devicetree/bindings/mfd/mediatek%2Cmt6357.yaml
e driver Qualcomm https://github.com/torvalds/linux/blob/master/drivers/rtc/rtc-pm8xxx.c .
Comparacao efetiva e efeitos acima conferidos na revisao local fixada, nao
inferidos desses HEADs. rtc_initialize_alarm nesta revisao apenas adiciona
timer RAM se alarme futuro habilitado; classe hctosys le RTC, nao o ajusta.
Codigo especifico novo limitado ao node compatible sob o PMIC ja integrado.
Nenhum novo protocolo, modulo C proprio, varredura de registradores ou
alteracao do ciclo de recuperacao. Nao atualizar o checkout de terceiros.

Offline RTC: recompilacao da base pareada reproduziu exatamente DTBbb19f737;
diff via DTC da nova arvore altera somente o node rtc/compatible. DTC e
empacotador passaram, incluindo todos os overlays LK e reserved-memory.
dt-schema focado no MFD MT6357 reporta seis erros ANTES e DEPOIS, identicos
por node/propriedade/schema/mensagem (metadados de reguladores e adc nao
descrito no binding MFD). Nao declarar schema integral limpo nem suprimir
esses erros. Nenhuma falha adicionada pelo node RTC; arquivos
`work/native-rtc-{base-schema,schema}-20261027.json` preservados.
Modulo upstream intacto ARM32:3485dedd323d0bef9c730e3aa10e3f4d731037641c2893aaf08a6125a7f776f0.
Nova imagem2512aa0735903809dbdc680c4763a27785331ba22ba9269be291032017fbd44e,
mesmos zImage04f1a556/ramdisk211c4e5c; DTB6f4e2f1d3f6d592fccb341f9bd373d16d5fca4aa774fde2e90fa09af28f9728d.
O driver nao esta no ramdisk: carga manual em RAM depois dos gates de boot.
RTC_HCTOSYS e SYSTOHC ja estavam habilitados. Nao iniciar NTP/ajuste de hora:
SYSTOHC pode escrever RTC se relogio do sistema for marcado sincronizado.
O ambiente RAM de ensaio nao inicia daemon de sincronizacao de tempo.

Falha real encontrada no primeiro boot RTC: bateria iniciou aos6,68s e foi
removida aos8,08s pelo OpenRC ao entrar em k40s-empty. O servico iniciado
diretamente nao pertencia a esse runlevel; boot anterior nao prova ausencia
da corrida. Reusar os diretorios de runlevel OpenRC ja usados para ram-proof:
adicionar somente o servico opcional aos dois runlevels RAM e invalidar somente
o deptree RAM anterior, como faz o ensaio existente. Sem mudar modulo C,
transporte, ciclo, PID1/inittab ou o teste de start/stop do ram-proof.
Aceite: bateria permanece registrada depois de ambas as transicoes; o
ram-proof continua parado e o softlevel continua k40s-empty.

Integracao RAM da correcao passou com os dois openrc reais: Charging,
4393762uV,6200uA,29,9C,watchdog ativo; ram-proof stopped e softlevel
k40s-empty preservados. Onze testes direcionados passaram; teste estrutural
compara runlevels preparados com o inittab real, sem nova lista duplicada.
Imagem corrigida a1e0f4f9aefb0cf8a77ad084c57b99a8330cc7c001154840b5023101a6364420,
ramdisk9f5cfc06c8df78c1f571433ef712f9a977e23f922f7695fa88bdbb02f221f69f,
com mesmo kernel/DTB; boot frio da correcao ainda pendente neste registro.

RTC fisico: modulo upstream registrou rtc0; since_epoch3471206571->3471206574
em3s, sem programar alarme ou hora. IRQ de alarme desabilitado/nao pendente;
adjtimex modes0,status64 UNSYNC. Energia/SSH/watchdog permaneceram funcionais.
Porem data2079-12-31 NAO valida compatibilidade de epoca com LG/Android;
HCTOSYS ARM32 nao ajustou o sistema por exceder INT_MAX.
Evidencia `work/native-rtc-read-20261027-a.log`, SHA256
1a870c3b6cd73e59bdc3bedf58894883e04c7dc263aaa36358b14a830da37520.
Nao corrigir isso escrevendo automaticamente uma data no hardware.
Fonte LG `drivers/misc/mediatek/rtc/mtk_rtc_common.c` usa base1968/+68;
SHA2563676770d5013fc6f0239c128c03faa96609038627624d6b3cbc08eda6c55be42.
Core RTC6.18 usa range1900..2027 e expansao por start_secs, nao somar68
diretamente. Conferir a leitura do 4.9 conhecido antes de qualquer adaptacao.
Discussao previa upstream localizada, nao aplicar patches rejeitados nem
trocar driver com base somente no titulo:
https://lkml.iu.edu/2504.1/07431.html .

Recuperacao do primeiro RTC20595 concluida exit0 sem intervencao: boot_a
5ffea913,Linux4.9,A/B9f344802 antes/depois. Referencia fisica do 4.9:
mt-rtc,2020-01-01,00:00:55,alarme desabilitado/nao pendente,
`work/native-rtc-lg49-reference-20261027-b.log`. A data padrao2020 do LG
tambem nao e a data atual; nao confundir leitura do contador com relogio
sincronizado. Preservar essa evidencia antes de mudar tratamento de epoca.

Boot frio da correcao OpenRC aprovado na imagem a1e0f4f9: aos48,63s,
softlevel k40s-empty,ram-proof stopped,servico bateria started; V4393267uV,
I2800uA,T30,1C,Charging,watchdog ativo,rootfsRO1. Startup5,13s e prova
PID1 7,27s sem unload posterior dos modulos de bateria. Nenhum start manual
nessa sessao. Evidencia `work/native-rtc-energy-coldboot-20261027-b.log`.
Sessao40139 ativa com coletor e limite3600s; recuperacao desta ainda pendente.
O RTC permanece sem carga automatica; falta compatibilidade de epoca antes
de programar alarmes ou testar despertar. Nao foi testado suspend real.

### RTC: preservar epoca LG sem regravar o relogio — auditoria previa

| Funcao | Atual | Reuso / origem / licenca | Compatibilidade e efeitos | Esforco | Decisao |
| --- | --- | --- | --- | --- | --- |
| Interpretar ano LG no driver upstream | rtc-mt6397 intacto le2079; LG4.9 le2020 padrao | Mesmos Linux2926d88 GPL-2.0-only e LG LMX430HM_Android_Q fonte3676770d acima; conversao existente RTC_MIN_YEAR_OFFSET=68, read/set time e alarm. Core rtc_device_get_offset/DT start-year avaliados | Core6.18 expande range1900..2027 por128anos quando start1968 se sobrepoe; start-year1968 nao implementa a soma fixa68 do vendor. Remover start_secs de todos os aparelhos foi rejeitado upstream por compatibilidade. Qualcomm/postmarketOS nao fornecem tradutor da codificacao desse PMIC. Adaptacao preserva regmap/IRQ/devm/probe/remove; nao acrescenta escritas, reset, controle de carga ou novo RTC | Pequeno, opt-in no driver existente | Reusar a aritmetica LG nas quatro callbacks e range1968..2095, somente com parametro read-only k40s_vendor_epoch=1 e gates machine K40S/compatible MT6357. Default preserva upstream; nenhum rewrite do relogio para mascarar incompatibilidade |

Antes de carga: testar callbacks reais read_time/read_alarm/set_time/set_alarm,
modos original/opt-in, anos limite e falhas de regmap. Verificar compilacao
ARM32 e patch aplicado a fonte com hash fixado. Primeiro ensaio fisico somente
leitura; escrita e alarme futuros dependem de verificacao separada. Nao
alterar RTC core, inittab, watchdog, recuperacao ou hora persistente nesta etapa.

Ensaio da codificacao passou: modulo42adaf35f07b39be6b45fbf3cf00a0f45794bd5e87bce7a943cd4af630b73afe,
RTC2020-01-01 e contador1577837226->1577837229 em3s, mesma referencia do LG;
HCTOSYS ajustou somente hora do sistema, adjtimex permaneceu UNSYNC.
Sem set_time/set_alarm no ensaio; Charging,V4393267uV,I900uA,T30C,WDT ativo.
`work/native-rtc-epoch-read-20261027-a.log`. Testes dos callbacks originais,
patch default-off e opt-in passaram, incluindo falhas e anos1968/2020/2026/2095;
primeiras falhas do fixture preservadas A/B, corrigidas sem alterar driver ou
suprimir warnings. Log aprovado `work/native-rtc-epoch-targeted-20261027-c.log`.

Tentativa de unload recusada com EAGAIN, modulo refcnt1; NAO forcar rmmod nem
unbind. Fonte kernel/time/alarmtimer.c confirma try_module_get do primeiro RTC
wakeup-capable e referencia mantida pelo core. Nao e prova de remove aprovado;
trocar essa versao exige o ciclo de reset/recuperacao existente. RTC,energia e
WDT continuaram ativos apos recusa. Nenhum alarme foi programado ate aqui.

Proximo ensaio autorizado no escopo do port: alarme RTC pelo sysfs padrao
`wakealarm`, cinco segundos, sistema ACORDADO. Reusar rtc_set_alarm/IRQ handler
do mesmo driver/core, nao criar C/IOCTL/sonda direta. Antes: confirmar alarme
desabilitado/nao pendente e wakealarm vazio, WDT ativo15s e rootfsRO. API faz
escritas RTC_AL_*,AL_MASK,IRQ_EN e WRTGR ja lidas na auditoria; ISR desarma
one-shot e pode limpar IRQ_EN. Nao modifica hora, charger, reset ou flash.
Finalmente limpar wakealarm, verificar IRQ contabilizada e energia/SSH/WDT.
O timestamp inativo de alarme anterior pode ser substituido; nao alegar
restauracao bit-a-bit de AL_* nem despertar de suspend. Se alarme preexistente
ativo, recusar teste sem altera-lo. Real suspend continua bloqueado pelo stop
do watchdog em mtk_wdt_suspend, independente do sucesso deste teste.

Alarme acordado aprovado em `work/native-rtc-alarm-awake-20261027-a.log`,
SHA256635bad9ecfc92c647a857b45f67bba9e3e742df10275bd91b7b71dfe05ed3d6e.
RTC1577837374,programado1577837379; aos1577837381 IRQ191/mt6397-rtc
passou de0 para1, alarm_IRQ voltou a no e wakealarm ficou vazio depois da
limpeza. EnergiaV4393267uV,I4700uA,T29,9C,Charging e WDT ativo; SSH retornou.
Nao houve suspend, ajuste de hora ou consumo medido. O alarme inativo agora
contém00:09:39/2020-01-01, nao o timestamp historico anterior.

Compatibilidade da epoca LG fisicamente demonstrada somente para leitura da
data atual do contador e roundtrip do alarme acima. Limites1968/2095, falhas
e escrita de hora foram testados apenas offline, sem regravar RTC fisico.
O modulo continua opt-in manual/RAM, refcnt1 mantido pelo alarmtimer; nao
esta instalado na imagem permanente. Catalogo existente atualizado para688
IDs, nao significa688 testes executados/aprovados. Dois testes novos passaram
no WSL com compilador; nenhuma suite ampla foi repetida.

Proximo bloqueio funcional de suspend: mtk_wdt_suspend chama stop, retirando
a recuperacao caso um dispositivo trave. RTC/IRQ acordado nao resolve esse
risco. Auditar uma extensao minima de politica de watchdog antes de testar
pm_test/devices ou s2idle; nao desabilitar o watchdog, forcar unload do RTC,
ou executar deep sleep para contornar o bloqueio.

### PM de dispositivos: watchdog ativo no ensaio — auditoria previa

| Funcao | Atual | Reuso / revisao / licenca | Compatibilidade / efeitos | Esforco | Decisao |
| --- | --- | --- | --- | --- | --- |
| Preservar recuperacao durante pm_test/devices e futuro s2idle curto | mtk_wdt_suspend para timer; nowayout nao e consultado pela chamada direta | Linux2926d88bb7fc4608fd942453d929c39e4e5ec006,mtk_wdt.c GPL-2.0+ SHA6e8230dff7db590f16bdc83918220da48be57c8a594cd3f0917f4c0e0018da9b; watchdog.h/core,imx2_wdt.c e qcom-wdt.c da mesma revisao. LG4.9 tambem para no suspend. Busca postmarketOS nao confirmou politica alternativa | watchdog_stop_ping_on_suspend para o worker, nao evita callback MTK stop. imx2 mostra padrao manter timer/ping, mas IP/clock diferentes; Qualcomm nao substitui registradores MTK. Extensao usa somente mtk_wdt_ping existente e leitura do MODE ja mapeado; probe/remove/reset/timeout/resume permanecem iguais. Clock32k segundo mtk_wdt_set_timeout; sobrevivencia a suspend ainda precisa ensaio | Pequeno, opt-in no driver existente e build isolada | Parametro read-only k40s_keep_on_suspend defaultoff. Exigir machineK40S,estado s2idle,ativo,timeout15,pretimeout0,MODE habilitado semIRQ/dual; caso invalido retornar EBUSY SEM parar timer. Caso valido ping e nao stop. Resume upstream intacto |

Sem novo watchdog, keepalive worker, protocolo BROM ou relaxamento de timeout.
Endereco/armamento BROM continuam no perfil/codigo de placa existente; antes
do ensaio exigir marcador de armamento e coletor ja pronto. Driver nao escreve
BOOT_MISC/RST_CON nem aceita deep sleep nesse modo. Permanece lab opt-in,
nao politica de economia/producao: suspensao acima do prazo deve resetar.
Testar callbacks reais: default ativo/inativo, todos os gates, ping/falha,
resume e ausencia de stop/escritas de MODE no caminho opt-in. Build isolada
preserva kernel/DTB/recuperacao anteriores. Primeiro pm_test/devices com5s,
nao suspend real; interrupcao de USB e possivel, coletor deve recuperar se
nao houver retorno. Clock fisico e retomada nao comprovados por mocks.
Fontes externas: https://docs.kernel.org/watchdog/watchdog-api.html e
https://android.googlesource.com/kernel/common/+/refs/tags/android15-6.6-2024-08_r11/drivers/watchdog/mtk_wdt.c .

Build isolada concluida: zImage4a2e380164a0477fcf6b6c0cc1c1ef059f2451886dc6fa5480ef192aed12b1bf,
configf235cbcf inalterada, fonte MTK modificada5491d6678c663ca58d96797fe3813f8095d3b0d4d5ea72ec5d42a8caf143c784;
fonte antiga6e8230df preservada. Copia independente da arvore, sem atualizar
checkout anterior. Oito modulos de energia/RNG e RTC foram reconstruidos
contra essa arvore/headers e comparados byte-a-byte com os artefatos anteriores;
identicos, listas de integridade preservadas. O comando inicial de comparacao
teve erro de quoting do shell host, corrigido com comparacao nativa do host;
nao e erro de compilacao nem foi ignorada diferenca de binario.
Teste dos callbacks reais passou (default e oito recusas sem escrita,
keepalive grava apenas RST; resume inalterado reativa timer). Windows informa
somente WSL/Linux, nao falha ambigua; catalogo689 IDs, nao suite completa.

Imagem770b55038f30bf133c840c4badc9533844821b64d17aefd5acfb171959776b02,
mesmo ramdisk9f5cfc06/DTB6f4e2f1d, acrescenta somente opt-in na cmdline e
kernel novo. Comparacao extraida/overlays aprovados. Ensaio usa script RAM
`artifacts/native-wdt-pm-boot-inputs-20261027-v1/pm-devices.sh`, sysfs upstream
e trap para none; checks de armamento BROM/estado RO/WDT antes de PM. Nao
incluir na imagem permanente nem habilitar sleep durante o boot.

Janela de log ajustada SOMENTE no argumento desse ciclo: System.map informa
__log_buf=c1e8a284,128KiB(CONFIG_LOG_BUF_SHIFT17),correspondendo a41e8a284
fisico; usar41e8a000+0x21000 para cobrir integralmente. Janela anterior
41e88000+0x21000 truncava o final nessa build PM_DEBUG; evidencias SSH nao
sao afetadas, nao declarar captura DRAM anterior completa. Nao alterar
verificador, endereco de particao, ciclo ou politica BROM para esse ajuste.

Primeiro pm_test/devices recusado por EBUSY do proprio guard WDT; retornou
sem reset,pm_test voltou a none,energia/SSH/WDT ativos. Nao aprovado nem
repetido automaticamente. Fonte watchdog_dev.c confirma que, quando o LK
deixa WDOG_HW_RUNNING, abrir watchdog chama ping em vez de start: flags
hardware de IRQ/dual podem nao coincidir com pretimeout0 do software.
Isto ainda e hipotese ate observar MODE. Sysfs nao expoe esse registrador.

| Funcao | Atual | Reuso / origem / versao / licenca | Compatibilidade / limites | Esforco | Decisao |
| --- | --- | --- | --- | --- | --- |
| Discriminar recusa por estado hardware do WDT | Sysfs so informa estado do core; nenhum MODE | BusyBox devmem existente no kbox Ubuntu1.36.1-6ubuntu3.1,binarySHA bbfba254e6875bbb25e0cfbba21e4be95f1c5980ace66925559179b8674ed4a0; upstream1_36_1 commit1a64f6a20aaf6ea4dbba68bbfa8cc1ab7e5c57c4,miscutils/devmem.c,GPL-2.0-or-later | ARM32,/dev/mem existente. Com ADDRESS WIDTH sem VALUE abre O_RDONLY,mmapPROT_READ e volatileu32; MODE0x10007000 e o mesmo read32 comum do driver auditado, nao read-clear. Binario distro nao alegado bit-equivalente ao commit upstream; versao/package/hash fixados. Sem novo diagnostico C,varredura ou instalacao | Minimo | Uma leitura32 explicita de MODE,sem VALUE; alias temporario somente RAM e remover depois. Nao expor devmem em perfil permanente nem escrever MODE pelo userspace |

Fonte conferida: https://raw.githubusercontent.com/mirror/busybox/1_36_1/miscutils/devmem.c .
Nao usar dd/readb para um registrador32 nem desabilitar verificacoes para
contornar a recusa. Telemetria limitada ao valor necessario para decidir.

Leitura unica confirmou MODE=0x5d (EN/EXRST/AUTO/IRQ/DUAL), sem escrita;
alias RAM removido, WDT continuou ativo. Log `work/native-wdt-mode-read-20261027-a.log`.
Assim a recusa e a protecao correta, nao motivo para retirar o gate.

Extensao v2 planejada: no probe opt-in, depois das propriedades MTK, exigir
machine K40S,HW_RUNNING,MODE_EN,timeout15,pretimeout0; chamar mtk_wdt_start
existente, que grava LENGTH/RST e MODE mantendo EN e limpando IRQ/DUAL.
Conferir readback EN e ausencia IRQ/DUAL; erro recusa probe, nao chama stop.
Reutiliza os mesmos efeitos do resume upstream, mas em um momento controlado
antes de PM. Campo BROM/reset e endereco de particao nao mudam.
Manter exatamente o guard de suspend v1: se alguem alterar MODE depois,
continua recusando. Nao alterar watchdog core nem fazer devmem write.
Antes de qualquer novo pm_test/devices, fazer um ciclo APENAS boot/end para
provar que o modo normalizado ainda reseta para BROM, coleta/restaura boot_a
e volta ao4.9 com A/B identico. So depois retomar PM; v1 permanece historico.

Revisao previa a carga v2: falha da preparacao sera registrada, mas NAO
desregistrara o watchdog ja criado pelo probe. Preservar registro/open do
driver normal e mais seguro que falhar probe, especialmente se o timer
inicial vier desligado. O guard v1 permanece identico e recusa qualquer PM
com estado hardware/software inseguro. Isto substitui a proposta anterior
de retornar o erro da preparacao pelo probe, nao reduz os gates do ensaio.
Imagem offline da410fdc e anterior a essa revisao, nao foi usada no telefone.

Versao final offline da normalizacao: fonte5533e1af71c8082f25a820298e93cbf6bc94b595b28fc59147befd4fa8bfdb9e,
zImaged481ce8ddda48dc45bbd8a0b464ac87bf3e05a547cafc9948a86192f33c78633,
imagem325a31b4eb77e4205114477a20047bdc8bf116a5214f8d8a00c8d6630a9bc13b;
mesmo config/ramdisk/DTB/log window. Dois testes passaram, inclusive readback
ignorado simulado (retornaEIO sem desabilitar MODE_EN); todos os gates do
guard v1 seguem testados sem mudanca. Build incremental/empacotamento passaram.
Teste do guard v1 recuperado por ciclo6015 exit0,4.9/boot_a/A-B9f344802 iguais;
captura dram-20261027-102230. Nova rodada nao vai executar PM: provar primeiro
boot/end e retorno automatico com o modo hardware normalizado.

Recuperacao com normalizacao fisicamente aprovada: ciclo75094 exit0,
boot mostraMODE0x15/timeout15,energia Charging/30,9C. End pelo supervisor,
retorno BROM,coleta,boot_a5ffea913 restaurada/readback e Linux4.9 sozinho;
A/B9f344802 antes/depois. Log `work/native-wdt-normalized-recovery-session-20261027-a.log`,
captura dram-20261027-103752. Nenhuma tentativa de PM nessa rodada.
Assim nao dependemos de supor que limpar IRQ/DUAL preserve BROM: foi ensaiado.
Prosseguir com MESMA imagem325a31b4, sem nova compilacao, para pm_test/devices.

pm_test/devices fisicamente aprovado nessa mesma imagem: uptime32,89->37,99s,
marcador K40S_PM_DEVICES_RETURNED e arquivo de aceite presentes,log confirma
guard manteveWDT ativo/15s e espera padrao5s. pm_test voltou a none. USB
temporariamente not attached aos37,97s,configured aos39,99s; SSH retornou
sem reset. V4393597uV,I1200uA,T30,9C,Charging depois do retorno.
Evidencia `work/native-wdt-pm-devices-20261027-b.log`.
Outra notificacao voltage_now=-110 aos38,66s,como no freezer; consultas
diretas posteriores passaram,sem latch/provider capture failed. Preservar
limite500ms e nao publicar frame atraves da pausa; nao alegar ausencia de
erros transitorios nem cobertura de politica termica/carregamento.

Este aceite cobre PM de dispositivos com retorno simulado pelo core, NAO
entrada real em s2idle,despertar RTC ou deep sleep. RTC nao carregado nessa
rodada. Proximo passo: RTC/alarmes no mesmo kernel e s2idle curto, depois
de revisar caminho enable_irq_wake/parent e manter fallback WDT/coletores.
Sessao70690 permanece ativa,limite3600s; recuperacao desta ainda pendente.

### Primeiro s2idle real curto — auditoria previa

| Funcao | Atual | Reuso / revisao / licenca | Compatibilidade / limites | Esforco | Decisao |
| --- | --- | --- | --- | --- | --- |
| Dormir em s2idle e acordar por RTC5s | Freezer/devices aprovados,alarme acordado aprovado,WDT normalizado/recuperacao aprovada | Linux2926d88,PM suspend.c,RTC class e rtc-mt6397(GPL-2.0-only),mt6358-irq.c e mtk-eint.c(GPL-2.0),sysfs state/wakealarm/pm_debug_messages; patches RTC/WDT acima | MFD child usa IRQCHIP_SKIP_SET_WAKE; MFD habilita wake da EINT144 no init. RTC suspend habilita wake do IRQ filho. EINT armazena wake_mask. Pin driver MT6765 NAO liga PM ops Paris nesta arvore, logo nao afirmar filtragem sleep de EINT nem economia. Paris comum tem masks suspend_noirq/resume,mas nao habilitar novo codigo antes deste ensaio. Qualcomm/postmarketOS reutilizam o mesmo PM core/RTC API,nao substituem transporte/IRQ MTK | Pequeno,orquestracao RAM via APIs existentes | Ensaio unico freeze com pm_test none,alarme5s,WDT15 e coletor ativo. Exigir log entrada real s2idle,delta IRQ RTC e tempo de RTC; retorno cedo ou por outro IRQ nao equivale a despertar RTC. Nada de deep/CPU-off |

Hashes locais conferidos: mt6358-irq.c eb2a0304a58b57354db017611265e70d798268a8f602e34ab3b8c04062f0d005;
mtk-eint.c f545676fef293b8e575b90bb2d2674ab499dc0a1ab308fbcb36dc9e2e164a75a;
pinctrl-paris.c 94848be20fd43e443398b5975829534ef95fa1f2df9cd1f835939616b0643502.
Modulo RTC reconstruido contra build normalizada e byte-identico42adaf35.
RTC carregado em RAM;2020-01-01,PMIC parentIRQ174/RTC191,wakeup enabled.
pm_wakeup_irq antes de uma suspensao real retorna ENODATA,nao falha do RTC.
Nao setar hora nem iniciar NTP. Reusar sysfs em vez de novo rtcwake/C/driver.
Coleta minima antes/depois:RTC contador/IRQ,wakeup IRQ,logPM,energia e WDT.
Restaurar pm_debug_messages e limpar alarme no trap. Timestamp inativo de
alarme pode mudar,como no ensaio acordado; nao alegar restore bit-a-bit.

Primeiro s2idle real NAO aprovado: core entrou em suspend-to-idle aos533,117s
e voltou aos533,384s pelaIRQ198(MUSB),RTC191 ainda0. Script rejeitou retorno
cedo,sem marcador de aceite. Depois temperatura capture=-110 ficou latched,
ao contrario do erro transitorio so no consumidor dos ensaios anteriores.
Nao repetir automaticamente nem apagar fault. Logs `work/native-s2idle-rtc-20261027-a.log`
e `work/native-s2idle-failure-20261027-a.log`. End/ciclo70690 recuperou4.9,
boot_a e A/B9f344802 iguais; captura dram-20261027-104051.

Fontes revelaram dois problemas de interface alem do teste rejeitado:
MUSB chama enable_irq_wake no probe incondicionalmente(FIXME upstream);
simples power/wakeup disabled nao garante desligar esse IRQ. UDC soft_connect
ja oferece desconexao/reconexao logica padrao,alternativa a novo patch USB
para isolar o RTC no proximo ensaio; validar acesso/retorno antes de usar.
RTC core rtc_alarm_disable so chama ops.alarm_irq_enable,ausente em mt6397:
echo0 pode remover timer RAM sem desarmar hardware. RTC191 chegou a1 depois,
com sistema acordado. Nao afirmar que trap existente sempre desarma hardware;
precisa corrigir interface antes do proximo alarme,sem escrever por devmem.

### Bateria: quiescer aquisicao ao suspender — auditoria previa

| Funcao | Atual | Reuso / origem / licenca | Compatibilidade / efeitos | Esforco | Decisao |
| --- | --- | --- | --- | --- | --- |
| Impedir frame V/I/T atravessar PM | Cola k40s_temperature_iio sem hooksPM;falha latched apos primeiro s2idle | dev_pm_ops/DEFINE_SIMPLE_DEV_PM_OPS e mutex Linux2926d88; IIO consumer/provider e DT io-channels ja existentes; propria cola GPL-2.0-only baseada LG,nao novo ADC. Frameworks PM/IIO comuns tambem Qualcomm/postmarketOS | iio_device_claim_direct_mode trata buffer/direto,nao pausa demanda externa em suspend. Usar mesmo mutex de aquisicao para esperar operacao em curso,pausar novas leituras e invalidar cache. Read pausado retornaEAGAIN sem I/O/fault; resume permite frame fresco. Fault real e stopping mantidos. Nao tocar ADC/FG reset/calibracao/charger,nao mudar500ms. Causa exata do primeiro -110 ainda nao rastreada; nao afirmar resolvida so por acrescentar hooks | Pequeno,extensao no modulo existente | Reusar PM callbacks,sem worker/notifier/driver paralelo. Teste do driver real verifica pausa/retomada e preservacao de fault; primeiro build/offline,depois ensaio proporcional |

PWRAP/provider e consumidor ligados por DT/IIO; confirmar ordenacao no ensaio.
Nao liberar retries de falhas hardware para fazer teste passar. Mudanca
funcional de lifecycle,nao apenas log novo. Preservar modulo/binario anterior.

Resultado offline PM da cola: testes do driver inteiro passaram,incluindo
cache invalido/nenhum I/O em pausa,frame novo apos5s,e faultEIO persistente
apos suspend/resume. Sem mudanca nos headers LG/calibracao/limites500ms.
Modulo ARM32 compilado6391d363f67e184cbe2e702e922c71efdc6e17d1d1c3a31bac56624b70e27006,
`work/native-temperature-pm-build-20261027-a.log`; ainda NAO carregado nem
aprovado fisicamente. Versao anterior preservada nos artefatos/workspace.

### RTC: cancelamento real pelo callback padrao — auditoria previa

| Funcao | Atual | Reuso / origem / versao / licenca | Compatibilidade / efeitos | Esforco | Decisao |
| --- | --- | --- | --- | --- | --- |
| Desarmar hardware ao cancelar wakealarm | RTC core tira timerRAM,mt6397 nao implementa alarm_irq_enable | Linux2926d88,drivers/rtc/interface.c rtc_alarm_disable e API rtc_class_ops; driver mt6397 GPL-2.0-only ja tem sequencia IRQ_EN_ONESHOT_AL/update_bits e WRTGR no set_alarm(enabled=false). Outros RTCs implementam callback,mas nao compartilham offsets MT6357; busca upstream nao confirmou patch pronto especifico | Reusar exatamente a sequencia existente sob mutex: update_bitsIRQ_EN(maskAL/ONESHOT),write_trigger,propagar erro. Nao mudar hora,AL_*,probe/remove,epoca ou ISR. Core passa a conseguir limpar hardware; expiry pode gerar clear idempotente adicional | Pequeno,callback ausente no driver existente | Estender rtc_class_ops,nao novo RTC/IOCTL. Testar enable/disable,preservacao de outros bits e todos os erros; depois armar/cancelar acordado e provar ausencia de IRQ tardia antes de voltar a s2idle |

Sem raw-register write pelo host. Patch aplicado depois do opt-in de epoca;
manter modulo anterior e evidencias de alarme acordado. Compatibilidade
fisica do novo cancelamento ainda pendente,nao supor sucesso so pelo sysfs.

Cancelamento offline: tres testes RTC passaram,callbacks anteriores e novo
enable/disable com AL inicialmente habilitado,LP/outros bits preservados,
todos os tres erros propagados e timestamps intocados. Modulo ARM32
ed4f3a8d575c99095f30b1df79b35772ac57f44b7cb7de07462097765cc8e380,
`work/native-rtc-cancel-build-20261027-a.log`; ainda sem ensaio fisico.

Nova imagem de ensaio9ba33ff1ea77eae4d537e96fc5485f9969c75b7a16db4ec7ee48b83010b72872,
ramdiske8f80f3d43f2e1e766b0b64813d29d798ede39a1116a82755b2f04159f22d3cc;
kernel/DTB/cmdline/recuperacao iguais a325a31b4. Muda somente modulo de cola
PM e hash correspondente na lista especifica desse pacote; perfil anterior
preservado. Extracao comparada/overlays passaram. RTC novo nao autocarregado.
Proximos ensaios limitados: PM/devices e arm/cancel acordado,antes de novo
s2idle. Nao repetir o ensaio s2idle falho sem resolver os bloqueios reais.

Novos aceites fisicos parciais na sessao14109: boot9ba33ff1 iniciou V/I/T,
supplier link platform:mt6359-auxadc -> battery-temperature -> adc-battery
visivel no sysfs. PM/devices83,82->88,90s passou com modulo6391d363;
V4391455uV,I-24800uA,T34,2C,Charging,WDT ativo. Houve ainda -110 transitorio
no consumidor,depois consultas frescas passaram; nao houve latch do provider.
Isto NAO resolve/prova ainda o noirq/s2idle que falhou. Evidencia
`work/native-temperature-pm-devices-20261027-a.log`.
RTC moduloed4f3a8d: armar+5 ativou alarm_IRQ;echo0 desativou imediatamente;
sete segundos RTC depois IRQ191 permaneceu0. Cancela hardware de fato,
nao apenas timer RAM. `work/native-rtc-cancel-awake-20261027-a.log`.

### Isolar trafego USB durante ensaio de RTC — auditoria previa

| Funcao | Atual | Reuso / revisao / licenca | Compatibilidade / efeitos | Esforco | Decisao |
| --- | --- | --- | --- | --- | --- |
| Retirar trafego do PC sem retirar cabo/fallback | IRQ198/MUSB acordou s2idle;IRQ wake habilitado no probe independentemente da politica sysfs | Linux2926d88,drivers/usb/gadget/udc/core.c soft_connect_store,GPL-2.0; usb_gadget_disconnect/udc_stop e udc_start/connect existentes | Interface soft_connect padrao da classe UDC,independente de MediaTek/Qualcomm/postmarketOS; controlador deve suportar callbacks. Interrompe SSH/NIC USB enquanto desconectado,nao altera eMMC,VBUS externo,charger ou WDT. BROM apos reset reinicializa USB fora desse driver | Minimo,sysfs e script RAM | Primeiro disconnect2s/connect acordado com nohup/trap e coletor pronto;provar retorno SSH. So depois usar no s2idle. Nenhum novo driver USB,IRQ-disable ou devmem write |

Nao afirmar que isso corrige politica MUSB para producao: isola o ensaio
com cabo fisico ainda presente. Restaurar conexao inicialmente configurada.

Soft disconnect2s/connect acordado passou: UDC voltou configured e SSH
retornou;T34,2C e WDT ativos. `work/native-usb-soft-cycle-20261027-a.log`.
Script RAM exige ACK do host apos retorno; sem ACK pede end pelo mecanismo
existente para nao deixar sessao inacessivel alimentando WDT indefinidamente.
Fonte UDC core SHA a8ba93ee572401786918db9a46660f5898dc0835bf4a4bf31126a145414ce113.
Proximo s2idle usa apenas os componentes agora ensaiados: colaPM6391d363,
RTCcancel ed4f3a8d,UDC desconectado logicamente e WDT/BROM validados.
Nao mudar kernel,IRQ controller,pinctrl ou timeout. Exigir mesmos criterios
de RTC/tempo/IRQ mais energia e ACK/SSH; falha pede recuperacao,nao repeticao.

Segundo s2idle,USB quiescido: entrada535,019s,despertar539,033s porIRQ174
(EINT144/PMIC),RTC1910->1,contador1577837343->1577837348; alarme ficou
desarmado. USB/SSH voltaram. Despertar RTC real demonstrado nesta condicao,
mas ensaio completo REJEITADO: primeiro voltage_now falhou,cola latched-110
novamente. Hooks regulares de suspend/resume nao bastaram para esse caminho.
Sem marcador/ACK de aceite,script pediu end e coletor14109 restaurou4.9,
boot_a/A-B9f344802 iguais,captura dram-20261027-110713,exit0 sem intervencao.
Log `work/native-s2idle-quiesced-20261027-a.log`,SHA256
54531afb6526d1c598f463c6d0b926b74bfad401da5ec548f4297f36c7e62084.
Nao alegar bateria preservada em s2idle nem repetir com limites relaxados.

### Contexto minimo do erro V/I/T — auditoria previa

Atualizacao offline apos a auditoria: contexto compilado ARM32,modulo
537ee0816cfcc7e34fc0c94fc10b938e6aafc2d4a95f89d84cd98decb7b09ff8,
`work/native-temperature-pm-context-build-20261027-a.log`. Teste do driver
inteiro passou,verificando tambem etapas ntc-iio/voltage-iio/frame-deadline
nas falhas injetadas. Nenhum timeout aumentado,erro apagado ou retry criado.
Ainda nao carregado; a causa do -110 fisico permanece por determinar.
Telefone restaurado ao4.9 conhecido; nao ha ciclo fisico em andamento.

Ensaio do contexto realizado em imagem7f31c1a0520cdae216afdc209f79b1add0a8f21a38fc31403aad2cbcf3d98fa8,
ramdiskd874bb2a4fa67a5b06efcb039004128453180e1c1b299912c641a58a101c3657.
RTC acordou por174/child1910->1;falha exata:stage=frame-deadline,
elapsed_ns=726695308. Voltage/NTC/FG e cleanup retornaram sucesso antes desse
gate;nao foi timeout de I/O nessa aquisicao. Ensaio rejeitado,coletor41660
recuperou4.9/boot_a/A-B,exit0,captura dram-20261027-112559.
Evidencia `work/native-s2idle-context-20261027-a.log`.

### RTC automatico no perfil temporario — auditoria previa

Entrega: rtc0 disponivel no boot residente sem insmod manual, sem alarme
armado e sem alterar o relogio de hardware. Reusar o modulo rtc-mt6397
ed4f3a8d ja ensaiado; nao criar driver nem descarregar RTC preso por alarmtimer.

| Funcao | Atual | Alternativa / revisao / licenca | Compatibilidade e limites | Esforco / decisao |
| --- | --- | --- | --- | --- |
| Carregar RTC no boot | insmod manual em RAM | OpenRC modules.in 0.63.2, commit b3a99e01c8bda7e5c2b9a8975a6d36ec3eff370e, BSD-2-Clause; Linux rtc-mt6397 no LTS2926d88 GPL-2.0-only com patches epoch/cancel acima. postmarketOS usa carregamento padrao DT/modulos; transportes Qualcomm/MediaTek nao resolvem a inicializacao deste RTC | modules.in usa modprobe com depmod/blacklist e retorna sucesso inclusive em falhas; payload RAM nao tem essa infraestrutura nem verificacao de hash/RO/parametro epoch. Seu stop nao descarrega modulos. Reusar openrc-run/insmod existentes com wrapper MIT minimo de placa e gates, falhar fechado. Driver faz HCTOSYS como ja auditado; nao escrever data ou armar alarme no servico. Nao substituir driver ou recuperacao | Pequeno: servico RTC independente, opt-in explicito no payload, timeout e FD3 fechado como bateria; stop sem rmmod, reset validado remove o modulo. Default sem marcador permanece inalterado |

Fonte comparada: https://github.com/OpenRC/openrc/blob/b3a99e01c8bda7e5c2b9a8975a6d36ec3eff370e/init.d/modules.in .
Aceite: hash e gates recusam entradas erradas antes de insmod; modulo correto
inicia uma vez, sem force-unload; boot fisico publica rtc0 e preserva V/I/T,
WDT e acesso USB. Recuperacao da sessao anterior antes de novo ciclo.

Implementacao offline: servico separado `boards/k40s/openrc/k40s-rtc`,
opt-in em resident-prepare nos dois runlevels reais do PID1, timeout4s/FD3
fechado. Treze testes direcionados passaram em WSL com PYTHONPATH=tools;
primeira invocacao sem esse caminho teve erro de import no teste antigo,
nao falha do servico. Gates exercitados em shell real com hardware simulado:
release,RO,hash,erro insmod,duplicacao e stop sem unload. Log
`work/native-rtc-startup-targeted-20261027-a.log`. Catalogo693 IDs nao e
execucao de693 testes. Imagem e44f4cb6c0dac2d3d291b5466309245501416c7c25859c561bf4ce722ef41128,
ramdisk e9c1dd1195d5384d3d656247bd742f4cb7086c770716a9f9a04dfb476a6dba8c;
extracao kernel/DTB/ramdisk e overlays passaram. Ainda sem aceite fisico
do startup automatico; RTC manual e s2idle anteriores permanecem distintos.

Aceite fisico do startup concluido: servicos bateria e RTC ativos nos
runlevels apos PID1; rtc0 mt6397-rtc/mt6357-rtc,sem alarme pendente,sem
insmod manual. Battery startup5,554s/RTC6,119s. V4392773uV,I4400uA,T35,7C,
WDTactive/rootfsRO1. Log `work/native-rtc-startup-acceptance-20261027-a.log`,
SHA2565eecc89bfcdfd3d6aa4addf288575b0f72e8a456de2db96233f5bdf428a4816e.

Mesmo script s2idle quiescido INALTERADO passou neste boot:entrada34,787s,
saida38,899s,RTCirq1910->1,parent174;USB/SSH retornaram,marcador e ACK
presentes. V4392279uV,I900uA,T35,7C apos retorno;consulta posteriorI5900uA.
Frames579988461/737903846ns rejeitados comETIME/latch0,nenhuma amostra
atrasada publicada. Final:alarmevazio,pm_testnone,debug0,UDCconfigured,
WDTactive,rootfsRO1. Log `work/native-rtc-startup-final-20261027-a.log`,
SHA2562951b41d1d42f33f469481768fb989a28027d97da23f762c99328a6dd894a2e1.
Primeira observacao SSH expirou durante reenumeracao,segunda observou a
mesma execucao;nao houve nova tentativa fisica para contornar falha.
Nao e ensaio prolongado/deep/consumo/SOC/controle de carregamento.

Recuperacao da sessao anterior46365 terminouexit0,4.9.190 de volta e
boot_a5ffea913 conferida;captura dram-20261027-113623. A/Bbefore e after
ambos9f3448025c92cbb4e1feb4f020b7fea5deb50222962832b8fe408d753f92a117.
Ciclo de recuperacao permanece SHA85bc5649e428ac6e63a0a17531ee66a65e79ba95821b4d2e7cbec7c8ca888f1d.
Sessao83335 atual permanece no6.18 com coletor ativo;
`work/native-rtc-startup-session-20261027-a.log`. Recuperacao desta ainda
pendente. RTC nao e force-unloaded nem reiniciado pelo servico;para troca
de modulo usar o ciclo validado. Nao habilitar esse perfil de laboratorio
como suspend de producao:watchdog15/BROM limita a duracao de sono.

### Distinguir frame expirado de hardware incerto — auditoria previa

| Funcao | Atual | Reuso / versao / licenca | Compatibilidade / efeitos | Esforco | Decisao |
| --- | --- | --- | --- | --- | --- |
| Rejeitar frame lento sem bloquear para sempre um provider limpo | Cola grava fault para todoerro,inclusive limite temporal apos todas as operacoes limpas | Padrao ja usado no consumidor generic-adc-battery paired-input do mesmo projeto/Linux2926d88:erro de coerencia invalida saida sem latch hardware. IIO propaga errno a consulta; propria colaGPL-2.0-only. Nao ha driver externo que classifique a janela especifica do frame LG por ela | Manter500ms/1s e nunca publicar frame atrasado. Somente apos todas leituras/cleanup e modelo validos,retornarETIME sem gravar fault. Sem retry dentro da chamada; proxima consulta independente pode adquirir UMA amostra nova. Qualquer erro de I/O(ateETIMEDOUT),identidade,range,decode ou cleanup continua latched. Preservar fault anterior/stop/PM | Pequeno,correcao de classificacao do erro | Separar caminho stale do caminho hardware-fail; validar modelo antes do gate temporal para nao mascarar sensor invalido. Nao aumentar prazo,nem apagar fault,nem criar loop de retry |

Teste deve manter rejeicao500ms+1ns/aceite500ms,saida intocada/cache zerado
em stale,uma unica aquisicao por chamada,amostra nova posterior e latch dos
timeouts reais/limpeza. Alteracao da semantica de stale e explicita,nao
eliminar teste antigo nem aceitar amostra fora da janela para obter verde.
Script fisico de aceite inicialmente INALTERADO; se dados continuarem lentos,
nao ha aceite. Artefatos anteriores com politica estrita preservados.

Offline freshness: driver inteiro passou com500ms aceito/500ms+1ns recusado,
cache expirado sem saida e uma nova aquisicao somente em outra chamada.
Timeout ADC e voltage-IIO reais continuam latched;modelo invalido mesmo
com atraso continua ERANGE latched. Modulo ARM32
8a7654ed20e574269e21129f125b0e73ebfe7186c2168d0d4e08025efc8d4cd7.
Imagem de ensaio e630b16d4b23546185e661681b47d3e71de3fccd50d9b2aadfdd6a280ad66db7,
ramdiskd17714f9635f2ec547edc0feece6647bf1a2d8a71ad3bf35d82dcc28ab5242db;
mesmo kernel/DTB/cmdline. Extracao e overlays passaram; ainda sem aceite
fisico dessa classificacao. Catalogo permanece691 IDs,nao suite executada.

Aceite fisico freshness com script INALTERADO: s2idle119,461->123,880s,
RTC1910->1 e IRQ174 despertou; retorno e marcador de aceite presentes.
V4391784uV,I-2500uA,T35,9C,Charging;USB/SSH voltaram e ACK do host recebido.
Primeira observacao SSH expirou durante reenumeracao; segunda leu mesma
sessao,sem reiniciar teste. Log `work/native-s2idle-freshness-20261027-b.log`,
SHA2569b00a6f8f18ffd52c0f1bce2eddfadd4f8fb84bb171b64d2e1d257901ac58d62.
Houve frame737977154ns rejeitado comETIME/latch0;nao publicado nem repetido
dentro da chamada. Consultas independentes seguintes produziram valores.
Tres amostras adicionais:V4392114/4392279/4391784uV,I-6200/-4700/-2200uA,
T35,8/35,7/35,7C;thermal_zone0 acompanha35800/35700/35700mC. Nenhum novo
erro de I/O registrado nessa janela. pm_test none,pm_debug_messages0,alarme
vazio,UDCconfigured,WDTativo,rootfsRO1. Followup
`work/native-s2idle-freshness-followup-20261027-a.log`,SHA256
028fcd299e107622483d323e3b7e84f14d3bc8e8c7079be9c0ed55a6b2a75d6d.
Isto valida ciclo CURTO em laboratorio com USB quiescido. Nao comprova
longa duracao,consumo,deep sleep,SOC,controle de carga ou seguranca termica
completa. GuardWDT15 e BROM sao de ensaio;nao e politica de suspend de
producao. Sessao46365 ainda ativa,recuperacao desta ainda pendente.

| Funcao | Atual | Reuso / alternativa / licenca | Compatibilidade / efeitos | Esforco | Decisao |
| --- | --- | --- | --- | --- | --- |
| Distinguir timeout ADC,FG ou frame apos s2idle | Log existente so dizcapture-110;nao distingue quatro retornos | dev_err/ktime do Linux2926d88 e proprio log ja existente,colaGPL-2.0-only. Tracepoints/ftrace/kretprobe poderiam observar IIO,mas funcoes inlined e contexto da etapa exigiriam mais configuracao;nao e necessario novo modulo/sonda | Acrescentar etapa e elapsed_ns a UNICA linha de erro existente;sem novos reads hardware,novas aquisicoes,retries ou logs de sucesso. Fault permanece latched. Comum a diagnostico de provider IIO,mas etapas atuais sao especificas desta cola | Minimo | Instrumentar somente contexto da falha para escolher proxima correcao. Nao concluir causa nem trocar resume por complete/notifier sem evidencias |
