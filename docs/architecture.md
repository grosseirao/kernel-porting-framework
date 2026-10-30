# Kernel Porting Framework (KPF) — arquitetura

Estado após o corte de propriedade Git (2026-10-29): os caminhos de placa e
workflows legados descritos abaixo pertencem ao repositório independente do
porte, não a um clone do KPF. A biblioteca e os inputs compartilhados continuam
no framework. O detalhamento abaixo preserva o histórico técnico das extrações;
para uso vigente, consulte [portes](../ports/README.md) e [estado atual](current-state.md).

A raiz é descoberta pela localização dos scripts; não depende de nome de pasta
ou junction. Workspaces Linux externos são selecionados explicitamente ou por
`KPF_K40S_RUNTIME_ROOT` no `.env` local ignorado. Paths registrados em
evidências históricas permanecem intactos, mas não são defaults do host.

KPF é o nome do projeto; `portkit` continua sendo o pacote Python. K40S identifica
o perfil da placa, não o nome do framework. O nome foi escolhido em 2026-10-25;
esta adoção é documental, sem renomear pastas, imports, CLIs ou recuperação.

Direção de separação escolhida pelo usuário em 2026-10-29: este repositório
continua sendo KPF. Cada porte tem Git independente em `ports/<aparelho>/`,
ignorado pelo KPF, sem submodules. A cópia inicial `ports/lg-k40s/` existe,
mas a migração ainda não terminou: originais e dependências transitórias foram
preservados. Não se cria outro repositório para renomear/extrair o toolkit.
Ver [contrato dos portes](../ports/README.md). Mecanismos úteis devem voltar
ao KPF; características e políticas do aparelho ficam no consumidor. A utilidade
clara não exige um segundo aparelho, mas não justifica abstração especulativa ou
adiar a primeira entrega de Wi-Fi/Bluetooth. Melhorias de driver continuam
preferindo o framework upstream adequado.

Este documento descreve responsabilidades e contratos, incluindo as extrações
iniciadas em 2026-10-25. Para integração e bloqueios vigentes, consultar o
[estado atual](current-state.md); para resultados das extrações host, o
[histórico específico](host-tooling-status.md). Não é uma reescrita do ciclo.

| Camada | Local | Responsabilidade |
| --- | --- | --- |
| Core | `portkit/core` | SHA-256, manifestos explícitos, evidência JSON create-only, subprocessos sem shell/retry, estados/classificação e invariantes DT sobre libfdt |
| Backend | `portkit/backends` | Contratos de transporte/recuperação. MediaTek: BROM/DA, hwcode, shutdown/reset e mtkclient continuam implementados nas CLIs legadas validadas |
| Board | `boards/k40s`, `kernel/devices/lg-k40s` | Kernel/profiles, partições, hashes, DRAM, endereços, IRQ/DT e política específica |
| Configuração local | `.env` na raiz, modelo `.env.example` | Hosts, paths e runtime locais pelo loader existente; ignorado pelo Git. Chaves ficam fora do repositório |

## Toolkit e trabalho do dispositivo — 2026-10-29

A dependência é **workspace do dispositivo → toolkit**. `pyproject.toml`
empacota apenas `portkit` como distribuição `kpf-portkit`; não inclui boards,
CLIs de laboratório, patches, firmware, `.env`, builds ou evidências. Os imports
existentes continuam iguais. A versão inicial 0.1.0 identifica este recorte,
não estabilidade de todas as APIs nem suporte a outro aparelho.

O core não contém parâmetros K40S. Backends conservam contratos específicos
de transporte/SoC, sem importar CLIs nem abrir sessões. `portkit.profiles` e
`portkit.composition` consomem dados de um workspace explícito: não distribuem
perfis junto da biblioteca. As raízes recebidas pelas APIs devem ser absolutas;
não são resolvidas contra o cwd. `development_root` exige `project=` quando lê
`.env`; não procura configuração junto da instalação Python. Com override de
runtime explícito, não precisa de workspace nem lê configuração. Os chamadores
do porte fornecem a raiz descoberta pelos próprios scripts. Não há busca de
dispositivos ou fallback para um checkout vizinho.

As operações básicas usam a biblioteca padrão. DT exige libfdt/DTC e composição
exige jsonschema, já existentes no ambiente oficial; extras de empacotamento
declaram as bibliotecas Python, não instalam ferramentas de sistema. Instalar
o pacote não instala nem autoriza mtkclient/USB/SSH ou drivers no aparelho.

`tools/tests/toolkit/` inicia a suíte independente: os dois casos puros de
Kconfig e cinco contratos de hashes/manifestos/evidência/processos/resultados
foram movidos sem duplicação. O caso de processos usa paths temporários nativos,
sem executar subprocessos. Adaptação das CLIs e regressões de recuperação
permanecem nos testes de integração originais. A allowlist offline existente
inclui os novos módulos.
Para executar somente o recorte, na raiz do checkout:

```sh
python -m unittest discover -s tools/tests/toolkit -v
```

Esses testes não carregam perfil privado/real. O guard offline continua sendo
aplicado pelo runner integrado `tools/test-offline.py`. O limite estático de
imports é uma regressão direcionada, não sandbox nem prova de independência de
todos os caminhos dinâmicos. O pacote pode ser construído por um frontend PEP517
com setuptools/wheel disponíveis; não é necessário instalar ou publicar nada
para continuar os workflows atuais.

O mapa do porte fica em [boards/k40s/README.md](../boards/k40s/README.md).
Não se movem CLIs de build/transporte/recuperação, DT, patches ou pins. Separar
repositórios e extrair os demais testes ficam para recortes posteriores; a
entrega conjunta Wi-Fi/Bluetooth não depende dessa reorganização.

### Primeiro comando distribuído com o toolkit

O verificador existente de saved Kconfig foi extraído para
`portkit.cli.kconfig`; não há segunda implementação do parser ou do relatório.
O wheel publica `kpf-check-kconfig`, também executável como
`python -m portkit.cli.kconfig`. Fora do checkout, `--workspace` é obrigatório:
diretório absoluto existente, nunca inferido do cwd ou da instalação Python.
Inputs/outputs relativos são resolvidos nessa raiz; arquivos absolutos externos
continuam permitidos. Esse parâmetro é uma base de resolução, não sandbox.

```sh
kpf-check-kconfig --workspace "${DEVICE_WORKSPACE:?configure-o-workspace}" \
  --config build/.config --fragment kernel/required.config --output checks/kconfig.json
```

Não lê `.env`, perfil de placa ou dependências de transporte. O comando antigo
`tools/check-kconfig.py` permanece como adaptador com raiz pelo próprio script;
seus argumentos anteriores continuam válidos. `--workspace` explícito prevalece
também no adaptador. Códigos 0/2, ordem dos fragmentos, ausência de valores
privados e relatório create-only são preservados; 0 não significa boot válido.

Os dois testes genéricos de CLI foram movidos para a suíte independente. O teste
de integração conserva execução do adaptador por cwd estrangeiro, compara os
bytes dos relatórios de sucesso/mismatch com a CLI empacotada e verifica recusa
de sobrescrita. Não foram movidos build, flash ou recuperação.

### Consumidor fixado e inspeção DT table

`boards/k40s/requirements-toolkit.txt` declara a dependência exata do workspace
por nome/versão, sem path de host ou checkout adjacente. Não é dependência inversa:
o wheel não inclui esse arquivo, o perfil K40S ou os workflows. A versão 0.1.0
continua de desenvolvimento; pin de versão não é garantia de artefato imutável
ou release publicada. Para consumo externo, usar wheel local revisado sem índice
de rede, conforme o procedimento no mapa da placa; não houve instalação agora.

O inspetor existente de Android DT table v0 também está no pacote como
`kpf-inspect-dt-table` / `python -m portkit.cli.dt_table`, com workspace absoluto
explícito. `tools/inspect-dt-table.py` permanece adaptador. Parser e relatório
são os mesmos; output existente/symlink é recusado antes de ler a captura.
Metadados não selecionam PCB, não exportam propriedades brutas nem autorizam boot.
A tabela vazia funciona só com stdlib; entradas FDT exigem libfdt já declarado
no extra devicetree. Os casos reais sintéticos anteriores continuam na integração
do adaptador; casos de raiz/output/containers inválidos rodam no pacote isolado.

### Analisadores textuais separados dos workflows do aparelho

Os corpos existentes de três CLIs estão no pacote, sem nova implementação de
parser ou diagnóstico. Os scripts antigos continuam adaptadores com raiz pelo
script e argumentos anteriores preservados; no pacote `--workspace` absoluto
e `--board` explícito são obrigatórios. As políticas vêm do perfil externo,
nunca de um K40S embutido ou da configuração SSH.

| Comando empacotado | Implementação | Adaptador preservado |
| --- | --- | --- |
| `kpf-analyze-stability-log` | `portkit.cli.stability` | `tools/analyze-stability-log.py` |
| `kpf-analyze-smp-log` | `portkit.cli.smp` | `tools/analyze-smp-log.py` |
| `kpf-analyze-register-snapshot` | `portkit.cli.register_snapshot` | `tools/analyze-register-snapshot.py` |

Todos interpretam apenas capturas existentes e publicam evidência create-only,
sem exportar linhas arbitrárias privadas. SMP retorna 0 por análise concluída,
não por boot aprovado; estabilidade retorna 2 para relatório incompleto/falho;
registradores só validam protocolo/valores permitidos, não semântica elétrica.
Nenhum comando executa teste, MMIO, carga, reset ou transporte.

A extração foi comparada às fontes anteriores guardadas em memória durante o
incremento: sucesso/vazio/NUL/UTF-8 inválido tiveram mesmos códigos e bytes de
evidência nos três comandos. Regressões do adaptador continuam na suíte do
workspace; testes com perfis sintéticos rodam também só com o wheel. Mocks dos
testes de integração apontam para o novo dono da implementação, não simulam um
segundo comportamento nos adaptadores.

### Decodificadores binários separados do layout K40S

`kpf-decode-ramoops-console` (`portkit.cli.ramoops`) e
`kpf-decode-session-logs` (`portkit.cli.session_logs`) distribuem os corpos
existentes de `tools/decode-ramoops-console.py` e `tools/decode-session-logs.py`.
Os scripts antigos são adaptadores; o específico `decode-k40s-session-logs.py`
continua no workspace, com sua opção logbuf e formato de relatório legado.

Nos comandos empacotados, workspace absoluto e board são explícitos. Assinatura,
ECC=0, tamanho da zona, offset da console e capturas/variantes vêm do perfil;
não são inferidos nem generalizados para outros formatos. Overrides repetidos,
desconhecidos ou fora das escolhas declaradas são recusados. Diretório de saída
existente/symlink é recusado antes de ler perfil ou captura. Entradas inválidas
não criam diretório parcial. O core e seus limites de tamanho foram preservados.

Diferentemente dos analisadores textuais filtrados, essas saídas contêm logs
brutos/privados e exigem destino privado novo. Não há reconstrução de ordem de
ring não-console, prova de correlação entre boots ou autorização de operação.
Comparação com fontes anteriores cobriu treze cenários, preservando códigos e
bytes de todos os arquivos. A suíte do pacote usa somente capturas/perfis
sintéticos; testes legados mantêm o contrato K40S sem exigir transporte.

### Snapshot, contrato estático e comparação DT distribuídos

O pacote também distribui os corpos existentes de três comandos DT, com os
adaptadores preservados nos caminhos anteriores:

| Comando | Implementação | Adaptador |
| --- | --- | --- |
| `kpf-inspect-boot-snapshot` | `portkit.cli.boot_snapshot` | `tools/inspect-boot-snapshot.py` |
| `kpf-check-dt-contract` | `portkit.cli.dt_contract` | `tools/check-dt-contract.py` |
| `kpf-compare-dtb` | `portkit.cli.dt_compare` | `tools/compare-dtb.py` |

Todos exigem workspace absoluto; os dois primeiros exigem board e política de
perfil explícitos. Comparação recebe dois DTBs, sem escolher placa. Libfdt valida
o FDT e DTC canonicaliza DTS, sem parser paralelo ou reescrita de valores para
fabricar equivalência. Snapshot continua omitindo chosen/bootargs e propriedades
não permitidas; a release fornecida é declaração do arquivo, não observação live.
Contrato estático não comprova driver/binding/semântica elétrica. Comparação
retorna 2 para diferenças e publica DTS/diff privados somente em diretório novo.

Destinos existentes/symlinks são recusados antes de inputs; FDT/contrato inválido
não publica saída parcial. As fixtures independentes usam FdtSw da própria
libfdt, não um novo gerador de formato. Ausência de libfdt/DTC deixa os casos
opcionais explicitamente skipped; a verificação deste incremento executou todos
com as dependências existentes, sem skips. O wheel e o sdist foram inspecionados:
sem board/workflows/capturas/.env, além dos metadados padrão e README público no
sdist. Isso não significa release publicada nem repositórios físicos separados.

### Aceite da fronteira toolkit ↔ K40S — 2026-10-29

Fronteira lógica e de distribuição concluída e verificada offline. Isso atende à
etapa de separar responsabilidades dentro do checkout atual, antes de criar
repositórios distintos; não é declaração de release publicada, portabilidade
universal ou funcionamento dos rádios no aparelho.

| Critério | Evidência de aceite |
| --- | --- |
| Toolkit autônomo | Wheel sem board/workflows/configuração privada; sdist inspecionado e reconstruído em wheel fora do checkout. Fontes Python reconstruídas comparadas byte a byte com portkit atual. |
| Dependência em um sentido | Suíte verifica imports sem dependência estática de tools/boards/installer/kernel e sem parâmetros K40S. Workspace público copiado sem portkit local consumiu somente o wheel reconstruído. |
| Consumidor explícito | requirements K40S fixa kpf-portkit==0.1.0; versão dos metadados do wheel confere. Nenhum path pessoal, checkout adjacente ou índice de rede é necessário no contrato. |
| Configuração e política separadas | Perfis externos, raiz absoluta, .env apenas no workspace; ausência de configuração recusada. Contrato SSH K40S está no perfil; host-key estrito e chave externa continuam obrigatórios. |
| Integração do workspace | Composição completa e plan do K40S idênticos ao checkout integrado; fingerprint congelado preservado. Dados de recuperação e runtime/configuração sintéticos verificados no consumidor externo. |
| Compatibilidade e falhas | Dez adaptadores mantidos; testes de comandos/integração e cenários antes/depois descritos acima preservam relatórios, códigos e recusas. Rodada conjunta de 151 testes passou sob guard; 28 testes do wheel passaram sem skips. |
| Escopo funcional preservado | Não mover build/flash/recuperação, fontes vendor, DT ou patches; não criar projeto MediaTek, novo protocolo ou obrigação de generalização para entregar Wi-Fi/BT. |

O ensaio final copiou somente fontes públicas permitidas pelo filtro existente,
sem portkit/pyproject do toolkit, fontes privadas ou .env real. A partir de cwd
vazio e Python -I, o consumidor usou o wheel reconstruído, validou os contratos
acima e carregou a ajuda dos dez adaptadores. Os cenários funcionais de cada CLI
foram exercitados pelas suítes do pacote e do workspace, não pelo --help sozinho.
O guard permaneceu ativo, sem transporte, rede, instalação ou build de kernel.

Limites deliberados: ainda há um checkout Git integrado; criar/mover repositórios
e publicar uma release são etapas próprias. 0.1.0 é versão de desenvolvimento,
não pin criptográfico de artefato. Testes de integração do aparelho podem exigir
fontes privadas explicitamente configuradas; eles não pertencem à suíte mínima
autônoma. A recusa existente de runtime sob /mnt e a allowlist do boot packer no
guard foram preservadas, não anunciadas como solução universal de filesystem ou
sandbox. Caminhos de dados como boards/, components/ e kernel/ são contratos do
workspace passado explicitamente, não imports nem discovery do K40S pelo toolkit.

Separar a camada MediaTek em outro projeto continua adiado até existir consumidor
concreto; seus contratos ficam no backend e o legado validado no workspace. A
próxima entrega funcional continua Linux 6.18 com Wi-Fi/BT e recuperação preservada,
dependente dos bloqueios técnicos e da autorização física já registrados.

### Primeiro mecanismo promovido do porte: candidatos DT

`portkit.core.devicetree.compare_dtb_candidates` reaproveita a seleção que estava
em `tools/compare-reference-dt.py`. Recebe uma referência binária, uma sequência
explícita de candidatos, callback de leitura e fallback explícito. Retorna o
candidato escolhido, metadados, DTS canônicos e diff. Não conhece diretórios,
nome de placa, IDs de overlays ou arquivos Android; a ordem vem do consumidor.

O workflow mantém no porte a leitura de boot-dtb/dtbo e o mapeamento do perfil.
O core reutiliza libfdt/DTC e recusa mais de um match canônico, valida todos os
candidatos mesmo após encontrar match e relê o selecionado como o workflow
anterior. Usar capturas imutáveis; não é detecção de compatibilidade de hardware.
Sem match, compara o fallback em vez de fabricar equivalência ou autorizar boot.

Quatro casos independentes cobrem match único, fallback, ambiguidade e candidato
corrompido. Seis cenários do consumidor comparados à fonte anterior preservaram
código, stdout, todos os arquivos e ordem de leitura. O mecanismo foi verificado
também no wheel sem o workspace da placa. Esse é o padrão de reaproveitamento:
extrair capacidade comprovada, preservar consumidor e falhas, manter política
específica fora do core, sem criar framework paralelo.

## Composição por hardware

### Metadados de fixtures por componente — 2026-10-28

`fixtures/pwrap_handoff.py` compartilha os checks v2/v3, não classes TestCase;
wrappers explícitos mantêm os mesmos sete IDs coletados (incluindo os antes
herdados em v3). `fixtures/wmt_caller.py` reúne os dados já usados por caller e
quiesce, sem importar o teste de init. A checagem AST em
`test_portkit_component_fixtures.py` exige ausência de imports estáticos entre
os módulos test_*.py, incluindo aliases e imports aninhados. Isso não prova
ausência de cargas dinâmicas, nem generalização total ou funcionamento físico.

I2C/DMA MT6765: `fixtures/mt6765_i2c.py` e `mt6765_dma.py` guardam modelos,
pins, preparo e runners sem TestCase. Três vetores já compartilhados com probe
viraram checks nomeados no harness; seus wrappers originais continuam casos
unittest. Dispatch de sources/fixture/run_c do consumidor foi preservado para
exercitar a implementação com o patch probe, sem chamar métodos de outro teste.
Quarentena, ownership, IRQ/PM e liberação de memória seguem regras específicas,
não qualificadas fisicamente por esses doubles.

CCF MT6765: `fixtures/mt6765_ccf.py` e `mt6765_ccf_unwind.py` oferecem modelos,
pins e mixins sources/run_c/compile_c sem TestCase. Os testes originais mantêm
aliases e métodos herdados; PLL, native-consumers e I2C probe usam suporte sem
importar testes de callbacks/unwind. Providers, binding IDs, parâmetros PLL e
regras de publicação/erro permanecem específicos de MT6765. Nada comprova CCF,
SMP ou restauração elétrica real a partir dessas fixtures host.

FIFO MT6370: `fixtures/mt6370_fifo.py` oferece os mesmos PRELUDE/CASES e
`check_sequence(sequence=None)`. Identificação usa o header original; estado de
carga passa o header adaptado explicitamente e reutiliza os casos, sem importar
outro TestCase, extrair seus literais por AST ou trocar Path.read_text global.
Modelos, seletores, IDs, limite de polls e comportamento de não restaurar uma
transferência ainda ativa são preservados. Não é backend FIFO universal nem
prova de identificação/carga no aparelho.

Bateria ADC/NTC e telemetria/soak: `fixtures/battery_adc.py` e
`battery_telemetry.py` contêm checks C parametrizados sem herdar TestCase ou
declarar casos test_*. Os testes originais mantêm seus wrappers/skips e os
consumidores NTC/soak usam os harnesses com suas próprias assertions. C gerado,
flags, prazos, escalas e restrições elétricas permanecem específicos e iguais;
compartilhar a fixture não fornece política genérica de carga/temperatura.

Touch FT5446: `fixtures/ft5446_frame.py` e `ft5446_power.py` contêm os modelos,
fontes pinadas e mixins de preparo/compilação antes acoplados a TestCase.
Mixins não herdam unittest nem contêm casos de teste; usam as assertions do
consumidor. Métodos sources/run_c e aliases antigos continuam acessíveis nos
testes originais. Optional-iovcc usa o harness sem instanciar outro TestCase;
dispatch para sua etapa adicional de patch permanece preservado. Nenhuma
sequência elétrica ou lógica de frame/driver foi generalizada ou modificada.

`fixtures/wmt_library.py` compartilha o modelo host e a localização usados por
early/late init, ownership e async-stop WMT, sem carregar outros unittest.
Aliases antigos são mantidos. A extração não valida essas regressões quando o
pin da fonte staging diverge; é necessário preservar a recusa, não atualizar o
hash para obter PASS. A busca por dependências deve inspecionar também imports
por alias via AST, não só linhas `from test_*`.

WMT EMI/staging/debug: `fixtures/wmt_emi.py`, `wmt_staging.py` e `wmt_debug.py`
separam o modelo EMI já compartilhado, o path staging e o seletor da última
definição C dos testes de cada recurso. Sete consumidores deixam de importar
outros unittest. Seletor continua limitado ao formato revisado, não parser C;
modelo continua MediaTek-específico. Pins e gates não são ajustados para aceitar
staging divergente. Aliases públicos anteriores continuam disponíveis.

gen4m AXI/cache: `fixtures/gen4m_axi_dma.py`, `gen4m_axi_pool.py` e
`gen4m_cache_inputs.py` guardam os modelos/casos de pool e pins/patches já
compartilhados. Sete módulos deixam de importar testes de outro recurso. A ordem
de patches, bytes C, flags e casos permanecem os mesmos; são doubles específicos
para regressões host, não implementação de DMA/cache nem prova no hardware.

`fixtures/wmt_logging.py` reúne os mesmos pins/localização de logging e o modelo
de dois epochs já usado por callbacks, bridge e WLAN SRCU. O nome SRCU_MODEL não
o torna um teste da implementação Linux SRCU. `fixtures/drm_panel.py` localiza a
mesma fonte DRM usada pelas fixtures WMT/gen4m, sem depender de um teste WMT.
Aliases antigos continuam disponíveis; modelos, pins e flags não foram alterados.

WMT: `fixtures/wmt_btm.py`, `wmt_psm.py` e `wmt_stp_core.py` separam os modelos
host e localização das fontes dos testes de init/teardown. Os seis consumidores
não importam outros testes; aliases anteriores continuam disponíveis e strings C,
pins, flags e casos são preservados. Modelos permanecem específicos de ownership
e callbacks WMT; não comprovam execução de workers reais ou atividade de rádio.

`fixtures/libfdt_sources.py:kernel_source()` localiza a árvore usada pelos checks
C de handoff, identidade e pstore. `K40S_TEST_KERNEL` mantém prioridade exata;
sem ela, a árvore early-v2 é localizada pelo mapa `KPF_TEST_SOURCE_ROOTS` já
existente. Consumidores de ROOT usam suporte diretamente; pstore carrega seu
helper de produção sem importar o teste de recovery. Nenhum check C, perfil,
contrato de memória ou fluxo de recuperação foi generalizado por esse ajuste.

BTIF: `fixtures/btif_dma.py` e `fixtures/btif_users.py` guardam os modelos host
preexistentes de MMIO/clock/locks e sessão/usuários. Dez módulos podem usá-los
sem importar testes de DMA reset ou membership. Os módulos originais reexportam
os mesmos aliases; conteúdo C, casos de teste, flags e hashes de fonte foram
preservados. Esses stubs não modelam comportamento elétrico nem sincronização
real do kernel; continuam fixtures específicas de BTIF, não backend genérico.

`tools/tests/fixtures/` contém suporte compartilhado sem importar módulos unittest:
`gen4m_sources.py` localiza a árvore gen4m; `generic_adc_battery.py` mantém os
pins/patches da fixture de bateria. Os hashes continuam verificados pelos testes,
não substituídos por escolha automática de fonte. Arquivos C existentes nessa
pasta não foram alterados.

Consumidores gen4m não importam o teste cfg80211 keys para obter ROOT/SOURCE.
Bateria pareada não importa o teste de status; RTC/watchdog localizam diretamente
a árvore Linux que já usavam, sem associação artificial a um teste de bateria.
Aliases antigos nos módulos originais permanecem disponíveis. Configuração via
`KPF_TEST_SOURCE_ROOTS` deve preceder imports; `linux_source()` da bateria conserva
a resolução ao carregar/recarregar o consumidor, sem congelar o override em cache.
Isso separa localização/metadados de execução dos testes, não torna modelos de
driver ou políticas elétricas intercambiáveis entre componentes.

### Protocolo de snapshots de registradores — 2026-10-28

`portkit/core/register_snapshot.py` valida logs com um begin/read-only v1,
amostras e campos ordenados, máscaras de exportação e conclusão consistente.
Contrato explícito em `diagnostics.register_snapshots`: prefixo, marcadores,
quantidade de amostras e triplas `(banco, offset, bits permitidos)`.

```sh
python tools/analyze-register-snapshot.py --board k40s --contract pwrap --log captura.txt --output resultado-novo.json
```

Essa CLI só verifica o protocolo e exporta valores permitidos, não interpreta
registradores nem demonstra comportamento read-only no hardware. Exit 0 indica
formato completo; amostras diferentes podem ser um resultado completo com
`stable: false`, nunca aceite elétrico. Rejeitar bits fora da máscara, não apenas
removê-los silenciosamente. Captura textual limitada a 4 MiB/UTF-8 sem NUL;
saída create-only com identidade da entrada, sem linhas arbitrárias.

O analisador PWRAP legado continua decodificando AXI/PLL/WACS com os mesmos
limites e flags, a partir das duas amostras/dez campos originais. Seleção e
concordância das cópias pstore permanecem específicas; sua entrada binária ainda
usa o decoder e tratamento de texto anteriores. Não há execução de diagnóstico,
leitura de regmap/MMIO ou autorização de boot nesta ferramenta.

### Análise SMP por perfil — 2026-10-28

`portkit/core/smp.py:smp_findings` interpreta capturas de eventos SMP, releases,
marcadores de online e GICv3. Prefixos, limite de IDs de CPU e opção de inferência
ARM são explícitos em `diagnostics.smp`. Outra captura não precisa importar os
diagnósticos PLL/CCF/ATF K40S:

```sh
python tools/analyze-smp-log.py --board k40s --log captura.txt --output resultado-novo.json
```

Exit 0 significa análise concluída, mesmo se vazia ou contendo falhas de boot;
não é aceite funcional. O JSON create-only inclui origem/hash e declara ausência
de acesso ao aparelho, autorização de boot, correlação de boots ou verificação
física de CPU online. Leitor limitado a 4 MiB/UTF-8 sem NUL, eventos limitados a
4096. Não exporta linhas arbitrárias, hostname/compiler do banner nem texto bruto.

A hipótese `arm_cpu_up_timeout_inference` só reproduz uma regra específica do
caminho ARM analisado; não deve ser habilitada para outra arquitetura/versão sem
verificação. Um timeout continua sem provar conclusão de firmware ou entrada C.
Releases/requests repetidos são sinalizados sem correlacionar boots automaticamente.
O wrapper antigo mantém o JSON completo e os diagnósticos específicos inalterados.

### Seletores de trechos C para fixtures — 2026-10-28

`tools/tests/support.py` oferece `c_function(code, declaration)` (terminador
exato, padrão `\n}\n`) e `c_brace_function(code, declaration)` (contador de
chaves, com newline final). O primeiro aceita terminador explícito quando uma
fixture já selecionava `\n}` sem newline final. São os algoritmos anteriores,
não parsers C; o contador pressupõe fontes revisados sem chaves em comentários
ou literais. Hash e revisão são verificados pelo consumidor antes da seleção.

Fixtures WMT/BTIF/gen4m não precisam importar testes de bateria ou netdev só
para esses helpers. Wrappers `function` dos sete módulos originais mantêm API
e erros para consumidores existentes. Modelos específicos compartilhados entre
testes de um componente permanecem específicos; não foram convertidos em core
de hardware nem usados para alegar equivalência elétrica ou integração física.

### Raízes de fontes para testes host — 2026-10-28

`tools/tests/support.py:source_path(name, relative)` localiza fontes externas por
um mapa explícito. Desde a migração de portabilidade de 2026-10-29, o arquivo
público `manifests/test-sources.json` contém apenas schema e mapa vazio, sem
default do laboratório. Precedência: argumento `configuration`, variável
`KPF_TEST_SOURCE_ROOTS`, arquivo ignorado `local/test-sources.json`, mapa público.
Configuração inválida selecionada nunca cai para a próxima opção. Paths relativos
do arquivo de configuração são ancorados na raiz do projeto, não no cwd.
Sufixos continuam selecionando revisões/workspaces explícitos de cada fixture;
hashes e compatibilidade continuam responsabilidade dos testes de componente.

Para outra máquina, um JSON privado pode substituir o mapa inteiro:

```json
{"schema": 1, "roots": {"development": "/srv/kpf-fixtures"}}
```

Em WSL/Linux, selecionar o arquivo antes de importar/executar os testes:

```sh
KPF_TEST_SOURCE_ROOTS=/caminho/privado/test-sources.json python -m unittest discover -s tools/tests -p test_portkit_test_sources.py
```

Esse exemplo executa somente o teste do resolver; os testes de hardware devem
ser selecionados conforme o impacto e, quando aplicável, sob a guarda offline.
O resolver não percorre diretórios, baixa fontes, relaxa hashes nem escolhe
aparelho. Configuração inválida ou raiz ausente é erro, não fallback. Ausência de
um arquivo no caminho válido continua sendo tratada pelos skips/assertions
originais. Caminhos relativos com traversal são recusados; raízes/symlinks
locais explicitamente configurados são confiados, não isolados por sandbox.

### Conjuntos KUnit declarativos — 2026-10-28

`tools/run-kunit-offline.py` separa o executor do conjunto padrão em
`manifests/kunit/host-policy.json`. Sem `--test-set`, os comandos antigos usam
os mesmos fontes, hashes, patches, símbolos e casos obrigatórios. Outro conjunto
revisado pode ser selecionado explicitamente em `prepare` e `run`:

```sh
python tools/run-kunit-offline.py prepare --workspace /tmp/kunit-exemplo --test-set manifests/kunit/host-policy.json
python tools/run-kunit-offline.py run --workspace /tmp/kunit-exemplo --test-set manifests/kunit/host-policy.json --attempt primeiro
```

`portkit/core/kunit_sets.py` valida descritores de dados confinados ao projeto:
archive/hash, versão, patch inicial, patches ordenados, mapeamento de fontes,
pins upstream, configuração, arquivos rastreados e suites/casos exatos. Não há
import de código de configuração, autodetecção de aparelho ou fallback de versão.
Novos workspaces e relatórios registram ID e SHA256 semântico do descritor;
mudança exige outro preparo. Workspaces legados sem essa identidade só são aceitos
com o conjunto padrão e conservam os gates anteriores.

O descritor não pode habilitar rede, HOSTFS, MCONSOLE, módulos ou todos os testes
indiscriminadamente. KUNIT e UML são sempre obrigatórios; restrições adicionais
pertencem ao conjunto. PASS exige suites, casos e contagens completos, sem skips.
Timeouts, ausência de retry, processo isolado e bloqueio de workspace existente
permanecem no executor. Os testes de outro conjunto usam fontes/toolchain
sintéticos e não qualificam um kernel ou componente físico.

### Overlays independentes offline — 2026-10-28

`portkit/core/dt_overlays.py:overlay_snapshots(base, overlays, snapshot)` recebe
bytes da base, pares `(label, bytes)` e o validador específico. Reutiliza DTC
via `run_bounded`, com timeout de 15 segundos, sem shell/retry. Cada overlay
é aplicado à base original, não à saída anterior; labels únicos preservam todas
as variantes. Arquivos brutos ficam somente em diretório temporário removido
também nas falhas. Falha de aplicação, timeout ou callback não retorna relatório.

Os coletores de clock/watchdog usam esse mecanismo, mas continuam responsáveis
por autenticar o backup, exigir seis variantes e verificar concordância. O core
não conhece IDs de PCB, hashes, endereços, IRQs ou políticas de hardware; executar
o helper não autoriza boot nem demonstra funcionamento do driver no aparelho.

### Contratos DT offline por perfil — 2026-10-28

`portkit/core/dt_contracts.py` reúne células, compatible único e status explícito.
O contrato SECURITY_AO fica em `diagnostics.dt_contracts.security_ao` do perfil:

```sh
python tools/check-dt-contract.py --board k40s --contract security_ao --fdt captura.dtb --output resultado-novo.json
```

A verificação compara propriedades binárias exatas no pai declarado; não traduz
endereços, interpreta IRQs nem comprova probe. A saída create-only omite os bytes
das propriedades e declara ausência de acesso ao aparelho e autorização de boot.
Watchdog e USB reutilizam helpers sem transferir suas regras específicas ao core;
o watchdog continua reportando status sem exigir disponibilidade.

### Parser de estabilidade reutilizável — 2026-10-28

`portkit/core/stability.py` interpreta capturas existentes sem transporte,
dependência de SoC ou execução de teste. A política é explícita: prefixo,
CPUs esperadas, duração e faixa do timeout reportado. No K40S esses valores
ficam em `boards/k40s/profile.json`, seção `diagnostics.stability`.

Uso por outra ferramenta host, a partir da raiz do projeto:

```python
from pathlib import Path
from portkit.core.stability import stability_findings
from portkit.profiles import load_board

board = load_board(Path.cwd(), 'k40s')  # Identificador da placa selecionada.
policy = board['diagnostics']['stability']
result = stability_findings(captured_text, **policy)
```

Outra placa precisa fornecer sua própria política do protocolo; não há fallback
silencioso para K40S. Não interpretar esses parâmetros como limites elétricos,
permissão de ensaio ou prova de reset real. O executor C, init e watchdog K40S
não foram generalizados. O wrapper `tools/analyze-k40s-smp-logs.py` conserva CLI,
API e saída anteriores; os parsers CCF/PLL/ATF específicos continuam ali.

`tools/tests/test_portkit_stability.py` testa o core sem importar helpers de
teste K40S; o segundo perfil é sintético, não cadastro de aparelho suportado.
As regressões específicas continuam em `test_lts_stability.py` e
`test_k40s_smp_logs.py`. Esta extração é o primeiro incremento solicitado pelo
usuário, não uma migração geral dos fluxos físicos.

### Ferramenta offline e suporte compartilhado — 2026-10-28

A entrada genérica não exige ATF nem importa analisadores específicos de SoC:

```sh
python tools/analyze-stability-log.py --board k40s --log captura.txt --output resultado-novo.json
```

`--board` é obrigatório. A política vem de `diagnostics.stability`; não há
fallback nem opções para relaxá-la na CLI. A saída registra placa, política,
hash/tamanho do arquivo e eventos filtrados, sem exportar o texto bruto.
Código de saída 0 indica relatório completo; 2 indica relatório incompleto,
falha ou entrada inválida. Ambos continuam sem autorização de hardware. Uma
análise válida mas incompleta gera evidência; uma entrada inválida não a gera.
Saída existente nunca é sobrescrita (`write_evidence` já existente).

`portkit/core/captures.py` concentra leitura UTF-8 estrita com teto de 4 MiB,
rejeição de NUL e identidade dos bytes, limitando também a leitura de arquivo
que cresceu depois do stat. `portkit/core/cpulist.py` concentra o subconjunto
decimal `N,N-M`, com limite explícito de IDs; não infere topologia nem promete
toda a sintaxe Linux. Os wrappers K40S mantêm seus limites anteriores.

`tools/tests/support.py` oferece ROOT, `load_tool` e a fixture FDT v17 já usada
nos testes. O loader continua sem cache, não chama `main` e recusa escape de
`tools/`; importar o suporte não carrega testes ou ferramentas de placa. A
fixture é só dado sintético; libfdt/DTC permanecem os caminhos de produção.
Os antigos nomes `module` e `fdt` continuam importáveis pelo teste early-port
para compatibilidade, mas seus consumidores agora usam o suporte diretamente.

### Console ramoops por perfil — 2026-10-28

`portkit/core/ramoops.py` decodifica uma zona já identificada: cabeçalho LE32,
ECC0, tamanho e assinatura obrigatórios. Não procura assinatura em dumps nem
calcula offsets de regiões; a assinatura deve incluir qualquer XOR de tipo.
O helper retorna bytes na ordem de `persistent_ram_save_old`, sem corrigir
cabeçalho ou alegar retenção de memória entre boots.

```sh
python tools/decode-ramoops-console.py --board k40s --console-dump console-zone.bin --output work/console-decoded-new
```

A entrada deve ser apenas a zona console, com tamanho exato declarado em
`diagnostics.ramoops_console`; não fornecer o pstore inteiro. A saída contém
`console.log` bruto e privado, além de `report.json`; escolher diretório novo
e não publicar seu conteúdo automaticamente. Não há argumentos para alterar
tamanho/assinatura na CLI nem fallback de perfil. `read_exact_capture` aplica
tamanho exato antes e durante a leitura, com teto host de 16 MiB.

`tools/k40s-pstore-layout.py` continua como adaptador do ABI LG observado,
mantendo tamanho fixo, metadados legados e layout dual-console separado.
Consumidores existentes permanecem compatíveis. Os endereços de coleta
continuam específicos; a extração não torna o layout LG equivalente ao ramoops
upstream nem amplia autorizações. O decoder de sessões foi separado abaixo.

### Sessões offline com layout de placa — 2026-10-28

```sh
python tools/decode-session-logs.py --board k40s work/capture-prefix work/decoded-new
python tools/decode-session-logs.py --board k40s work/capture-prefix work/decoded-exact --capture-size logbuf=0x20000
```

O core em `portkit/core/session_logs.py` lê somente os arquivos
`PREFIX-NAME.bin` declarados em `diagnostics.session_logs.captures`. Não exige
quatro arquivos, nomes LG ou ATF; a fixture de outra composição usa somente
`memory` e `trace`. Esse caso é sintético, não suporte físico a uma nova placa.

O perfil define offset/fonte do console e quais capturas recebem extração ASCII
desordenada; o codec vem de `diagnostics.ramoops_console`, sem duplicar assinatura
ou tamanho. Referências, nomes, limites e variantes são validados antes da
leitura. `--capture-size` só seleciona uma variante declarada: não adivinha o
tamanho nem ignora arquivos ausentes. Limites de host: 32 capturas, 16 MiB por
arquivo e 64 MiB pelo conjunto selecionado, sem significado elétrico.

As capturas são lidas/decodificadas antes de criar o diretório de saída, que
deve ser novo. A CLI genérica inclui placa, layout, codec e escolhas de tamanho
no relatório. `console.log` e os fragmentos `*-unordered.txt` são privados;
fragmentos legíveis não provam ordem de ring nem boot atual. Não publicar esses
arquivos automaticamente nem usar o resultado como autorização de hardware.

`tools/decode-k40s-session-logs.py PREFIX OUTPUT [--logbuf-size ...]` permanece
compatível, inclusive metadados/formato do relatório e escolhas antigas de
logbuf. Apenas lê esses valores do perfil e chama o core compartilhado. Coleta
de memória, endereços físicos, recuperador e scripts de boot não foram alterados.

### Requisitos Kconfig sem dependência de placa — 2026-10-28

`portkit/core/kconfig.py` compartilha o parser literal de `.config` e a comparação
de requisitos. Aspas e escapes permanecem raw; não há avaliação de shell,
normalização de números ou resolução de dependências. A última ocorrência vale.
O workspace continua exigindo os mesmos valores; n omitido pode corresponder a
n, mas y/m/string/número ausente não pode passar. A auditoria zImage conserva
seu wrapper com a view histórica sem aspas, sem mudar os gates ARM32/LK.

```sh
python tools/check-kconfig.py --config build/.config --fragment base.config --fragment board.config --output work/config-check-new.json
```

Essa ferramenta não precisa de `--board`: arquitetura, placa e símbolos vêm dos
fragmentos explícitos. A ordem dos fragmentos é significativa e a saída deve ser
nova. Exit 0 significa correspondência literal; 2 indica divergência/entrada
inválida. Divergências geram relatório; entrada inválida não. O JSON contém
identidades dos arquivos e nomes de símbolos, nunca seus valores, que podem
conter dados privados em CONFIG_CMDLINE ou strings semelhantes.

Kconfig/olddefconfig e verificações do workspace continuam responsáveis pela
configuração real. O relatório não prova dependências, build, hardware funcional
ou autorização de boot. Nenhum fragmento, default ou controle de build é alterado
pela CLI de comparação.

### Execução de fixtures C host — 2026-10-28

`tools/tests/support.py:run_c` centraliza fonte/binário temporários e execução
com argv explícito, por meio de `portkit.core.processes.run_bounded`. Exemplo
para um teste host independente de placa:

```python
from support import run_c

run_c(source_text, flags=['-std=c11', '-O2', '-Wall', '-Wextra', '-Werror'])
```

As flags são obrigatórias e pertencem ao teste. O helper não escolhe sanitizers,
stubs ou política de hardware e não remove flags em caso de erro. Compiler
default `cc`, prazo de compilação 30 s e execução 10 s; cada prazo deve estar
entre 0 e 60 s. Não há shell, retry, fallback ou skip interno. Falhas/timeout
propagam, e a fonte/binário temporários são removidos na saída.

Os testes charge-state, battery-i2c-refresh e gen4m netdev já usam o helper,
preservando `-pthread`/UBSan nos casos que os exigiam e seus asserts/código real.
Isso não generaliza os protocolos de seus doubles nem prova hardware funcional.
O helper executa C revisado, não código hostil: ele não é sandbox nem gestor de
árvores de processos. Continuar usando a guarda offline e revisar qualquer
fixture que pretenda criar processos reais ou abrir dispositivos.

### Comparação DT sem paths de placa — 2026-10-28

`portkit/core/devicetree.py` compartilha `canonical_dts`/`compare_dtb`: libfdt
valida o blob v17+, e DTC fornece a view ordenada (`-q -s -I dtb -O dts`).
Nenhum canonicalizador próprio, reescrita de propriedades/phandles ou
interpretação elétrica é introduzido.

```sh
python tools/compare-dtb.py --reference reference.dtb --candidate candidate.dtb --output work/dt-pair-new
python tools/compare-reference-dt.py --board k40s --output work/reference-comparison-new
```

A CLI do par exige dois DTBs explícitos, limita a leitura a 16 MiB por arquivo
e usa prazo de 30 s por DTC. Gera DTS privados, diff e metadados em diretório
novo; exit 0 indica igualdade canônica, 2 indica diferença/erro. Diferenças
geram evidência, entradas inválidas não criam a saída. Igualdade canônica e
identidade de bytes são campos separados; nenhuma delas valida bindings ou boot.

A comparação histórica em lote agora é segura para importar: não cria pasta,
lê backups ou executa DTC no import. Seus diretórios, base e mapa ID/candidato
vêm de `diagnostics.reference_dt_comparison`. O default K40S e os arquivos/
relatórios anteriores são preservados; `--board` e overrides explícitos de
diretório permitem outro conjunto sem editar código. IDs/revisões de firmware
não são inferidos, e o container Android histórico não é parser universal.

O lote conserva exit 0 ao terminar a comparação, mesmo havendo diferenças;
consultar `canonical_equal` em cada linha. Mais de um candidato canônico,
candidato ausente, mapeamento inválido ou saída existente fazem o lote falhar
antes de publicar artefatos. DTS/diffs podem conter identificação/calibração:
manter a saída privada. A comparação nunca aplica DT nem acessa o aparelho.

### Container Android DT/DTBO compartilhado — 2026-10-28

`portkit/core/android_dt.py:parse_dt_table` contém o parser de container antes
local ao inspetor de backup. Ele aceita somente v0 com entradas de 32 bytes e
FDT v17+ validado por libfdt, conservando ordem, bytes e metadados opacos. Não
suporta v1/compressão, não infere PCB e não verifica autenticidade/AVB.

```sh
python tools/inspect-dt-table.py --input dtbo.img --output work/dt-table-new.json
```

O relatório create-only contém identidades, offsets, tamanhos, IDs/revisões e
custom fields, mas não propriedades FDT. Um ID listado não é seleção da entrada
ativa. O helper de captura exige arquivo regular explícito e limita a 16 MiB.
Nada é extraído/aplicado nem lido do telefone.

O inspetor Android, comparador de referências e gerador LK usam o mesmo parser,
com adapters para suas APIs anteriores. O gerador mantém toda política LK/PCB
específica e agora valida o container inteiro antes de produzir a primeira
entrada; não gerar um resultado parcial com um payload posterior inválido.
O gerador também exige o venv com pylibfdt, sem fallback para um parser mais
permissivo. DTs com payload/versão não revisados são recusados, não normalizados.

### Snapshot de boot offline, separado de SSH — 2026-10-28

`portkit/core/boot_snapshot.py` filtra FDT/iomem já capturados, com libfdt. A
seleção literal de caminhos/prefixos vem de `diagnostics.boot_snapshot`; as
propriedades exportáveis são fixas no core, não configuráveis pelo perfil.
`/chosen` e descendentes são excluídos independentemente da seleção, e prefixo
global `/` é recusado. Não salvar FDT bruto, bootargs, serial-number ou tabelas
arbitrárias de calibração. O filtro não valida semântica elétrica de propriedades.

```sh
python tools/inspect-boot-snapshot.py --board k40s --fdt work/fdt.bin --iomem work/iomem.txt --kernel-release 6.18-fixture --output work/boot-snapshot-new.json
```

`--kernel-release` é uma afirmação da fonte da captura, não medição do aparelho.
A CLI aceita um token de release, registra origem offline e hashes das entradas,
e usa evidência create-only. Capturas podem estar desatualizadas ou pertencer a
boots diferentes. A ferramenta não tem opções de SSH, chave, host ou transporte.
Tamanhos são limitados pelos helpers de captura; RAM com intervalo invertido é
recusada e endereços acima de 32 bits não são truncados.

O wrapper `collect-k40s-boot-evidence.safe_snapshot` mantém seus campos e rótulos
anteriores, inclusive o uso pelo inspetor estático Android. O parser legado
exportado e o corpo de `main`/comandos SSH não foram alterados. A política de
execução física continua separada: essa extração não autoriza rodar o coletor
legado nem transforma arquivo estático em prova de boot.

Primeiro C extraído: CAR bruto MT6357 em `kernel/components/pmics/mt6357`, sem
calibração, unidades ou acesso a hardware. A ponte de unidades fica na área K40S
e mantém API/recusas anteriores. O catálogo hasheia `reusable_sources` por chip
e `board_sources` por placa. O candidato v3 usa a ponte; fontes/artefatos v1 e
seleção física continuam intactos. O caminho legado não é substituído por um
symlink, nem seus hashes são relaxados para aceitar a versão nova.

`components/` agora contém definições independentes por arquitetura/SoC/IP/chip,
com origem, licença, alternativas upstream e limitações. O arquivo
`boards/k40s/components.json` instancia essas definições e mantém conexões,
dependências e estado de validação da placa; `boards/k40s/profile.json` aponta
para a composição sem alterar os defaults de recuperação.

`kernel-workspace.py components --board k40s` resolve e valida o grafo offline,
com schemas locais jsonschema e invariantes de referência/ciclo/path. Não lê
configuração SSH privada nem usa transportes. Os comandos plan/prepare/build
anteriores permanecem iguais: a composição é inventário, não gerador de drivers
ou autorização para habilitar hardware. Fingerprint próprio registra as fontes
e metadados; fingerprint do build legado não mudou.

I2C0 e I2C5 compartilham a definição do controlador mas têm instâncias e conexões
distintas. Calibração elétrica pertence à placa. Áudio/codec, Wi-Fi/Bluetooth e
painel ainda não identificados ficam em unresolved, não em módulos fictícios.
Código C legado não foi movido nem declarado genérico: o catálogo o indexa como
experimento ainda acoplado. Próximas extrações devem seguir subsistemas upstream,
sem copiar drivers para criar uma árvore de plugins paralela. Ver
[`components/README.md`](../components/README.md).

## Ferramental e recuperação preservados

`kernel-workspace.py --board k40s` já seleciona o perfil pelo board e usa hashes e
execução do core. `--profile` explícito permanece, validando a identidade do board.
O fingerprint default anterior é preservado; nenhuma série de patch foi alterada.

Migração de portabilidade de 2026-10-29: `development.runtime_root` fica em
`boards/<placa>/local/lab.json`, não no perfil público de hardware. O argumento
`--runtime-root` tem precedência e dispensa o arquivo; seleção inválida não cai
para default pessoal. O loader de lab é compartilhado, com validação do campo
de build independente da validação SSH. Plan/inventário não leem lab privado.
O valor local anterior foi preservado sem alterar argumentos make ou fontes.
Auditoria IRQ e staging offline leem a rota I2C5 do perfil (nó, specifier,
sysirq/GIC). Nenhuma dessas leituras foi introduzida no ciclo físico.

O staging agora usa libfdt/check_full, preservando o formato nodes/reservations.
Equivalência passou em fixtures sintéticas e nos seis DTBs merged preservados;
os seis overlays em ambas as ordens mantiveram o resultado. O DTB staged tem
o mesmo SHA-256 anterior. O parser histórico usado por coleta/recuperação segue
intocado; ausência de libfdt no staging não aciona fallback silencioso.

`lts-auto-cycle.py` agora lê somente `recovery.image` e `kernel.normal_release`
do perfil K40S, com rejeição de caminhos escapando do projeto e release inválida.
O teste reverte em memória exatamente esse hunk de configuração e exige o hash
original de todo o restante do arquivo. Defaults continuam iguais aos validados.
`k40s-da-session.py` lê geometria de boot_a, hash de recuperação e três regiões
DRAM (pstore/lklog/atflog) do mesmo perfil fixo K40S. Outro teste reverte apenas
seu hunk de configuração e exige o hash da baseline original para todo o resto.
Tipos, geometria, SHA, alinhamento e sobreposição são validados localmente.
Hwcode esperado e defaults atomic_logbuf também vêm do perfil, validados no
backend MediaTek sem inicializar USB. Identificação real, protocolo, framing/reset,
hash do DA e controles GPT/readback continuam legados. Não há seleção de outra
placa nessa CLI e logbuf explícito do ciclo continua obrigatório.
`flash-boot-auto-brom.py`, gate host-once, registry e init de recuperação continuam
byte a byte iguais à baseline. Não houve generalização do transporte nem prova
física nova. Configuração ausente/inválida interrompe antes do transporte.

SSH no ciclo: `load_lab` lê somente `.env` na raiz explícita do workspace quando
necessário, sem fallback para JSON ou ambiente do processo. Usuários, portas e
endpoint USB esperados pertencem a `ssh_contract` no perfil público da placa;
o toolkit valida formato e correspondência, sem política implícita. No K40S o
contrato continua root/22 e root/10.15.0.1/2222. Ausência/campos extras/política
inválida são recusados; o `.env` não pode escolher um contrato mais permissivo.
IPv4 normal, chave externa absoluta e host-key estrito continuam obrigatórios
independentemente da placa. O ciclo injeta
identidade/alvo normal na instância importada do helper legado; sua CLI standalone
continua congelada. O pin USB continua verificado pelo hash do payload, sem
desabilitar known_hosts, alterar ledger/nonce ou acrescentar retries. O exemplo
é público; configuração real e chaves não entram no Git.

O core não descobre aparelhos nem importa backends automaticamente. Importar uma
interface não abre USB. Não há backend Qualcomm implementado; o contrato
`RecoveryBackend` exige identidade, plano específico, timeout, autorização única,
evidências e recuperação verificada. EDL/Sahara/Firehose não são aliases de BROM/DA.
ADB/fastboot também só têm contrato nesta etapa, sem nova implementação paralela.

## Próximas fronteiras, sem implementação de drivers

1. Trocar constantes legadas por leitura do perfil, uma unidade por vez, exigindo
   os mesmos hashes/valores e testes de falha; não reescrever o ciclo inteiro.
2. Reduzir parsers FDT próprios apenas após equivalência: DTC compila/aplica overlay,
   libfdt lê a estrutura, dt-schema valida bindings. Código próprio verifica
   reservas/handoff/identidade/políticas não cobertos por schema.
3. Bateria futura: IIO para aquisição e unidades; regmap para PMIC; consumidor
   `power_supply` para STATUS/V/I/T/CAR; somente FG, calibração NTC e quirks reais
   como código específico. SOC não será inferido de CAR ou tensão isolados.
4. Carregador MT6370/MT6371 fica sem bind automático até auditoria completa das
   escritas de probe, defaults/limites elétricos, erros, workers e remove.
5. KUnit para lógica kernel; kselftest para interfaces; Python para host/evidência.
   A primeira conversão IRQ foi compilada ARM32 e executada em UML, sem aparelho.
   O adaptador reutiliza o runner oficial; core process_groups limita o ciclo de
   processos do build host, sem alterar subprocessos do ciclo de recuperação.
6. Depois da paridade e migração: outro MediaTek primeiro; Snapdragon depois.

Ver `open-source-reuse-audit.md` antes de qualquer módulo/ferramenta nova.
