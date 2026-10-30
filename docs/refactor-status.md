# Organização: progresso e limites

Este documento preserva relatos de etapas anteriores. Para localizar o código,
as fontes Linux e o próximo bloqueio vigente, começar pelo
[mapa atual](current-state.md). Não tratar os próximos passos históricos abaixo
como substitutos das prioridades atuais do AGENTS.md.

## USB/eMMC/PWRAP no CCF nativo: composição e guards — 2026-10-25

DT consumidor novo elimina providers locais de clock e mantém PHY/MUSB/MMC e
reguladores já usados. Nada ativo: todos disabled, nenhum perfil ou recuperador
alterado. Refs USB118/0/32, MMC60/20/56 e PWRAP0/64 traduzidas pelos símbolos do
header real. Schema PWRAP aceita reset ausente; não declarar os demais bindings
experimentais certificados. Seis overlays mantêm nós nativos intactos.

Flag CCF crítica preserva último voto PMIC_AP durante cleanup. Testes compilam
guards reais disable/unprepare, sem reimplementar clock provider. Pequeno helper
PWRAP permite lookup optional somente no handoff MT6765 autorizado/configurado;
outras configurações continuam obrigatórias, erros/defer propagam e cold-init
não foi alterado.40 combinações de lookup, quatro cenários de refs CCF e DT.
ARM builtin de clock/PWRAP compilou; não .ko carregado e não teste físico.

Migração de gating/PM não comprovada: antigo mantinha gates, nativo pode fechar
USB/MMC em runtime/error. PMIC protegido por flag crítica, não snapshot restore.
Falta revisar PLL/handoff, bindings consumidores, EINT/rails/reset touch e pacote
temporário completo. ULPOSC0Hz em CCF4.9 não é medição nem motivo para clock fake.
Manifesto: mt6765-native-consumers-verification-20261025.json.
Regressão140 seguros e573 WSL(21 skips), sem falhas; archive140/seis skips
com fontes/aliases públicos externos, kselftest host/TAP aprovado e checker729
fontes sem binários/chaves/raízes privadas. Recuperação e zImage atomic intactos.
Próxima etapa física deve começar por providers CCF isolados, consumidores
desabilitados e captura RAM/pstore com retorno automático; não é necessário
fechar touch/rails antes desse ensaio de clocks, nem ligar tudo de uma vez.

## CCF nativo: unwind corrigido, DT composto e taxas observadas — 2026-10-25

Telefone confirmado no Linux4.9 conhecido por SSH estrito; clk_summary lido sem
escrita/reboot. I2C reporta124.8MHz/univpll3_d2, DMA156MHz/syspll_d7. São dados
do framework4.9, não medição nem garantia para o handoff LTS; divisor5 dá24.96MHz
ao cálculo I2C. I2C enable/prepare0/0 não significa clock fisicamente ligado.

Delta staging v2 de clk-mt6765 verifica todos os retornos de registro, evita
provider incompleto e usa unregister/free existentes em ordem inversa. Preserva
v1, tabelas, gate PMIC_AP e writes de sucesso; não cria provider/remove paralelo.
Testes compilam probes reais:768 pares de sucesso,20 erros helper/provider e
seis falhas map/alloc. Fronteiras de registro/core CCF são stubs, não simulação
de efeitos elétricos ou restauração de PLL. Objeto ARM compilado, não carregado.

DT nativo completo agora separa recursos SoC TOP/IFR_AO/APMIXED da placa, usa
refs I2C0 main/dma3/27 e exclui providers locais ARMPLL/USB/PWRAP concorrentes.
Schemas upstream de clock + binding I2C validam a montagem e seis overlays
não alteram nós nativos. Tudo novo disabled, nenhum assigned-clock, touch ou
charger ativo, sem perfil automático. Não é uma imagem pronta: consumidores
USB/eMMC/PWRAP ainda precisam migrar junto e clocks críticos/EINT/rails/reset
exigem revisão de handoff antes do pacote físico. Fonte doadora mais nova
continua com erros ignorados; comparação registrada, sem atualizar checkout.
Manifesto: mt6765-ccf-unwind-verification-20261025.json.
Regressão:136 offline seguros e569 WSL(21 skips), sem falhas; archive Git136
com seis skips, fontes/aliases públicos externos presentes e overlays privados
ausentes. kselftest host/TAP passou; checker724 arquivos sem binários/chaves/
raízes privadas. Recuperador cycle/DA/registry e zImage atomic com hashes iguais.

## Touch: pinos reais e binding upstream reaproveitado — 2026-10-25

Sem módulo C novo: driver pinctrl MT6765 já existe. Backport exato do schema
upstream commit21a7f44..., mais delta separado admitindo #address-cells0 do
EINT existente. Não criar outro schema/driver. Grupos DT da placa: SDA0/SCL0
GPIO82/83 função1, IRQ1/EINT1 função0, reset164 e VCL27 função0. Nenhum nível
de saída, rail fictício, drive ou consumidor touch configurado automaticamente.

Quatro testes DTC/dt-schema/libfdt cruzam muxes com descritores mainline reais,
verificam estado disabled e seis variantes do binding (duas válidas/quatro
rejeitadas). DT completo compara reservas/memória/chosen/CPUs e status antes/
depois, inclusive após seis overlays do backup. Avisos LK históricos continuam
iguais; phandles podem ser renumerados, referências CPU são resolvidas por nó.
Overlays preservados não provam seis variantes de hardware independentes.

Top-level offline novo usa aliases do workspace preparado, não entrou em
perfil de boot. Fonte, licença e hash do schema em third-party.json; auditoria
e gates em docs/k40s-touch-pin-integration.md. Reuso revelou dois cuidados:
IRQ0x2002 mistura falling2 com IRQF_ONESHOT; IOVCC ainda não identificado.
Probe edt liga rails antes de adquirir reset, enquanto LG executa OFF/ON com
delays5/200ms: equivalência de alimentação/reset ainda não comprovada.
Próximos passos: CCF real, handoff EINT e alimentação, depois pacote temporário
com recuperação. Nenhum acesso ao aparelho ou alteração de recuperador.
Regressão:131 offline seguros,564 WSL(21 skips), zero falhas. Extração Git131
com seis skips e fontes/aliases públicos externos presentes; overlays privados
não estão no archive. kselftest host/TAP passou; checker719 arquivos sem
binários/chaves/raízes privadas. Cycle/DA/registry mantêm hashes aprovados.

## I2C: binding nativo e integração com dt-schema — 2026-10-25

Schema existente i2c-mt65xx ampliado com compatible MT6765 sem fallback MT8183.
Contrato inicial do candidato:1–400kHz, divisor1–8, sem have-pmic. DTC1.7.0 e
dt-schema2026.9 executam13 variantes (sete válidas/seis rejeitadas), incluindo
defaults e faixa antiga MT6577 sem regressão. Resultado exige diagnóstico JSON
correto, não só exit0. Fixture isolada contém providers placeholder e disabled:
não é DT de boot nem validação elétrica. Fontes/bindings vêm de Linux6.18.58.

Suíte segura127, completa560(21 skips), extração Git127(seis skips com fontes
públicas externas presentes), sem falhas. Entrada host kselftest/TAP passou.
Guard ampliado apenas aos três utilitários dt-schema do mesmo interpretador;
SSH, rede, shell e Python arbitrário continuam bloqueados e testados.
Nenhum transporte aberto, perfil ativo/recuperação/charger alterado.
Próxima integração: providers CCF/EINT/pinctrl reais e reset/alimentação touch;
o pacote temporário só deve sair após revisar essas dependências. Evidência:
manifests/mt6765-i2c-binding-verification-20261025.json.

## I2C MT6765: transferências e lifetime DMA — 2026-10-25

Delta staging v2 sobre native-v2 mantém driver upstream, mas troca somente a
variante MT6765 por memória coerente persistente TX/RX. Inclusive buffers
DMA_SAFE do chamador ficam isolados. Dados só retornam após sucesso e parada;
IRQ read/ACK/acumulação usa um mesmo lock. Falha fatal retém memória/clocks e
referências device/módulo, não tenta recuperar automaticamente ou liberar DMA
de estado desconhecido. Pin do módulo no probe exige unbind saudável antes de
rmmod; quarentena exige reboot e bloqueia novos probes nativos. v1 preservado.

Sete testes novos compilam funções C reais contra stubs:600 transações,48
cenários de falha com pedido explícito seguinte e42 pares legados, além de
alocação/pin, PM/remove e DMA/START presos. Isso não prova ordenação física ou
todas as corridas SMP. ARM compilado,56 imports exportados, mesmo zImage atomic.
Regressão126 offline/559 WSL(21 skips), zero falhas; extração Git126/seis skips
com fonte Linux pública externa ainda presente. kselftest host/TAP aprovado.
Checker707 fontes sem binários/raízes privadas; hashes de cycle/DA/registry iguais.

Ainda NOT FOR PHONE: falta bindings/DT, parents CCF, EINT/pinctrl e alimentação/
reset do touch, pacote temporário e validação física protegida por recuperação.
Nenhum perfil ativo/initramfs mudou e nenhum transporte do aparelho foi aberto.
Manifesto: mt6765-i2c-dma-lifetime-verification-20261025.json. Catálogo agora
reconhece chamadas self.run_c como compilação C, sem importar módulos de teste.

## I2C MT6765 nativo: candidato compilado e KUnit executado — 2026-10-25

Variante nova no i2c-mt65xx, sem outro transporte. Inclui overrides dos offsets,
helper único de temporização derivado da LG, divisor espelhado, timeout, reset
warm limitado e IRQ/MCU. Preserva os caminhos legados nos traces testados e
recusa entradas/encodings inválidos. Limite inicial1–400kHz/WR/RD/WRRD explícito.
ARM compilado,45 imports conferidos;24 traces init e2048 IRQ antigos iguais,
512 status IRQ novos cobertos e20460 vetores comparados com função LG real.

Lógica pura foi para KUnit, não outro parser Python: UML oficial executou os
três casos novos mais dez existentes, todos aprovados. Objeto KUnit ARM também
compilado. Runner existente ampliado com arquivos/suite esperados e validação
de casos incompletos; workspaces antigos não são atualizados silenciosamente.

Ainda **NOT FOR PHONE**: corrigir/testar timeout DMA, quiescência antes de
unmap, dados em erro e IRQ tardia/teardown antes de ativar. Não foi transferido
frame touch físico nem mudou perfil/DT/image/recuperação. Artefatos v1 e v2
preservados, só fontes/patches entram no Git. Prova: manifesto native-offline.
Regressão:119 testes seguros e552 WSL (21 skips), zero falhas. Mensagens de
transporte na suíte completa são mocks, não operações no aparelho.
Extração limpa do Git:119 testes, seis skips de fixtures privadas, zero falhas.
Checker aprovou703 arquivos sem binários/chaves/backups; hashes de cycle/DA/
registry e zImage atomic continuam iguais aos de recuperação aprovados.
Entrada kselftest/TAP também aprovada, executando os119 testes de interfaces
host sob o guard offline; isso não é kselftest de hardware do telefone.

## I2C0: clocks traduzidos e callbacks CCF exercitados — 2026-10-25

Contrato do controlador cruzado com DT BMW e fonte LG: main/dma IDs11/38 no
vendor tornam-se3/27 no header upstream; gates físicos11/18 não mudaram.
MULTI_DMA0xf8c vs0x8c, MCU_INTR, timeout e temporização explicam por que não
basta usar MT8183. Leitura touch63bytes exige DMA no caminho doador, além do
antigo ensaio FIFO8bytes. Contrato é dado auditado, não gerador/DT de boot.

Sete testes novos verificam mapa e compilam gate/mux/PLL/probes reais. Mostram
escritas herdadas, update de mux pendente, falhas regmap não propagadas e que
unprepare de PLL não restaura snapshot. Core CCF crítico foi revisado na fonte,
não executado/simulado integralmente. Sem nova infraestrutura de clocks.

Patch staging corrige cinco escritas diretas que ocorriam mesmo após erro de
registro do provider. Sucesso preservado nos traces, objeto ARM compilado.
Não desfaz callbacks anteriores nem resolve unwind completo. Fora dos perfis,
sem bind/flash, recuperador e kernel atomic preservados. Detalhes e próxima
variante nativa em docs/k40s-i2c-upstream-integration-audit.md e manifestos CCF/I2C0.
Regressão:114 testes seguros e547 WSL (21 skips), sem falhas. As mensagens de
transporte na suíte completa são mocks; nenhum comando foi enviado ao telefone.
Extração limpa do Git:114 casos, cinco skips por fixtures privadas ausentes,
zero falhas. Checker aprovou697 fontes sem binários/chaves/backups. Hashes de
cycle/DA/registry e zImage atomic reconferidos, sem alteração.

## Touch: extensão upstream compilada e comportamento testado offline — 2026-10-25

Conferência binária BMW/doador preservada em bmw-kernel-touch-re.md. O candidato
estende edt-ft5x06.c Linux6.18.58, não cria parser ou framework multitouch novo.
Seis testes compilam ISR, identificação e parâmetros de frame reais, original e
modificado, contra stubs input/regmap. Cobrem contatos/pressão, perda de contatos,
release/zero, palma, IDs0–15, terminador, contagem inválida e falha de transporte;
2500 frames legados e1280 combinações vendor/erro de identificação, mais M06/M12.

Foi reproduzido bug do candidato v1: terminador ID15 com evento RESERVED era
ignorado no segundo loop, permitindo processar slot14 depois dele sem preflight.
v2 checa terminador antes do filtro de evento. Teste executa v1 e v2 e comprova
a seleção inválida somente no antigo. Ambos os patches e artefatos preservados.
Chips antigos não entram nesse ramo; traces dos caminhos testados são iguais.

v2 compilou módulo ARM;63 imports presentes em vmlinux.symvers e vermagic
6.18.58 conferidos. O warning de Module.symvers global ausente permanece
registrado: vmlinux.symvers foi fornecido explicitamente, sem suprimir erros.
Não houve instalação, autoload, bind ou mudança de DT/kernel do telefone.
107 testes seguros e540 na suíte completa passaram (21 skips na completa).
Extração limpa do Git passou107 casos, quatro skips por fixtures privadas
ausentes; checker source-only aprovou693 arquivos sem binários/chaves/backups.
Mensagens de DA/flash na suíte completa são mocks, não operações físicas.

Stubs não testam core MT real, CRC/regmap M06, concorrência, probe/remove ou
eletricidade. A identificação família54 não prova todo firmware FT5446.
Pendente: integração I2C0/clocks/EINT/pinmux e alimentação/reset da placa, depois
teste temporário com recuperação. Não declarar touch operacional a partir disso.
Evidência: manifests/ft5446-upstream-offline-verification-20261025.json.

## Provider de bateria no telefone:18 rodadas e recuperação aprovada — 2026-10-25

Novo módulo por demanda carregado no6.18.58 atomic em imagem temporária
58875f34..., após permit SSH único. Apenas esse ensaio ADC/FG foi empacotado.
18 rodadas V/I/T em23.12s; driver registrou18 capturas, fault0. Interface0444
retirada com sucesso após unload. Tensão4.3898–4.3911V, descarga16.6–25.4mA,
temperatura35.0–35.1°C conforme modelo nominal LG, sem comparar instrumento.
Isso excedeu os antigos limites15s/16 tentativas; não é soak de confiabilidade.

Retorno automático ao4.9.190-k40s-bringup sem botão/intervenção/retry. DA
conferiu restauração e leitura SSH independente confirmou boot_a5ffea913...;
A/B antes/depois9f344802... iguais. Resultado tem todos os checks aprovados,
incluindo readonly eMMC/rootfs, SSH autenticado e autorização host-once.

Não foi alterado um byte do lts-auto-cycle.py, DA ou registry. Init ganhou
callback condicional de três linhas e host-once reconhece o novo hook em duas
listas. Não são byte-idênticos: o teste inverte exatamente esses três hunks e
exige os hashes originais para todo o restante, sem atualizar baseline.
Validação da nova sonda fica no wrapper posterior à coleta/restauração.

Prova: `manifests/battery-continuous-phone-verification-20261025.json`.
Regressão final:101 testes seguros aprovados;534 WSL,21 skips, zero falhas;
extração limpa101 casos, quatro skips por fixtures privadas ausentes. O guard
offline continua sem permitir shell genérico: checagem sh -n foi executada
separadamente, não ampliamos privilégios do runner para fazer o teste passar.
Mantidos pending: estabilidade prolongada/PM, calibração externa, identidade
de conversão/exclusão contra firmware, SOC e integração persistente no LTS.
Nenhum autoload/charger/thermal policy foi instalado. Aparelho voltou ao kernel
conhecido; não confundir sucesso temporário com migração definitiva do sistema.

## Bateria contínua por demanda implementada e compilada — 2026-10-25

Variante `kernel/modules/k40s-battery-continuous/` reutiliza os oito headers
existentes de captura BATADC/NTC/FG e calibração LG sem mudar algoritmos ou
comandos. A cola usa power_supply padrão, sem worker periódico: consultas
compartilham bundle V/I/T por menos de1s, novas consultas adquirem outro bundle.
Não expira após15/30s nem após4/16 tentativas; contador u64 satura sem bloquear.
CLOCK_BOOTTIME governa cache e duração externa, separado do clock monotônico
interno dos helpers, evitando reapresentar cache antigo após suspensão.

Qualquer erro de identidade/aquisição/idade invalida e trava o provider sem retry
ou fallback velho. Stop de software antecede unregister; referência do PMIC só
é liberada depois. Sem charger/reset/thermal policy, porcentagem ou SOC.
Não é driver de proteção da bateria nem prova de exclusão contra outro master.
Medição faz as sete escritas já existentes de request/latch por captura.

Builder existente ganhou somente opção explícita `--continuous`, usando o
kernel atomic fixado; fontes15s/30s, registry/ciclo/init de recuperação não foram
alterados. Módulo ARM32 linkado,27 imports encontrados nos exports da árvore e
vermagic conferido. Warning de Module.symvers global preservado; fornecido
vmlinux.symvers, sem aceitar símbolos ausentes. Ainda não carregado no telefone.

Fixture compila o módulo C inteiro com fronteiras de framework/captura stubadas:
2001 aquisições simuladas, limites do cache/boottime, contador saturado, falhas,
init recusado e referências/retirada da interface. Isso não simula hardware,
concorrência real ou gerenciamento de energia do kernel. Prova:
`manifests/battery-continuous-offline-verification-20261025.json`.

Regressão:99 casos seguros aprovados;532 na suíte WSL,21 skips, zero falhas.
Cópia limpa extraída do Git:99 casos, quatro skips por fixtures privadas
ausentes, zero falhas. Nova opção recompilada e segunda execução verificou
os artefatos imutáveis sem rebuild/telefone.

Próxima etapa é integrar teste temporário explícito, com hashes e exclusão de
outros consumidores ADC/FG, seguido de restauração automática; não habilitar
autoload nem instalar na imagem antes dessa validação física.

## Mudança de prioridade: kernel original BMW como referência — 2026-10-25

Backup boot_a reconferido e extraído com AOSP unpack_bootimg. Recuperados58128
símbolos e configuração ARM32 do4.9.190. A heurística de base do reconstrutor
falhou; ELF corrigido emc0008000 teve bytes comparados ao raw e prologue/PMIC
ancorados. Ghidra direto descompilou cinco funções, sem autoanálise global;
REA Windows P0 recusou ELF ARM e não forneceu Evidence dessa análise.

Cinco spans de funções bateria coincidem com tamanhos do ELF doador LG;
sequências de chamadas diretas também coincidem. Há diferenças de words,
endereços/globais e inferências não fechadas: não equivalência formal/full-tree.
Prova: `manifests/bmw-kernel-battery-re-20261025.json` e
`docs/bmw-kernel-battery-re.md`. Código específico já extraído de corrente,
coulomb e NTC será aproveitado com power_supply existente; todos os canais
AUXADC não são pré-requisito da primeira bateria contínua. Estratégia em
`docs/stock-first-port-strategy.md`. Nada foi instalado/gravado no telefone.

Trabalho anterior interrompido foi preservado: auditoria de13 canais e fixture
da ABI/teardown IIO; candidato stop-latch usa estado existente após erro de CLR
sob shared_reset, sem nova escrita/reset. Host testa36 combinações de falhas
antes/depois de commit e bloqueio de retry/SCALE. Esse11º candidato NÃO entrou
no perfil/kernel compilado nem no registry físico. Os dez candidatos anteriores
e a recuperação continuam intactos.

Regressão:97 testes seguros passaram; suíte WSL530 casos,21 skips, zero falhas.
Extração limpa do Git97 casos, quatro skips por fixtures privadas ausentes.
Verificador do índice confirmou somente fontes/metadados, sem binários/chaves.
Esses testes não provam equivalência semântica das funções binárias comparadas.

## Integração offline do provider IIO real — 2026-10-25

Nova árvore isolada Linux6.18.58 compilada com os dez candidatos AUXADC e
um gate MFD default-n. O perfil `lg-k40s-lts-iio-handoff.json` permanece
board_support=false, boot_policy=forbidden e fora do registry de testes físicos.
Não houve acesso ao telefone, empacotamento de boot ou flash nesta etapa.

O ramo regulator-v1 e os gates anteriores foram preservados. A seleção
auxadc-v1 exige configuração explícita, ADC modular, identidade da placa,
recuperação BROM armada e filho OF compatível disponível. Usa devm_mfd_add_devices
para registrar regulator+ADC, sem IRQ, RTC, teclas ou charger; não fabrica
platform_device e não acrescenta escritas PMIC/MMIO.

Comparação por libfdt: exatamente um nó ADC acrescentado; todos os nós,
propriedades e reservas anteriores preservados. A configuração muda somente
duas opções: novo gate=y e AUXADC=m. Schema upstream do ADC passou com
dt-schema2026.9, sem diagnósticos; validação filtrada, não de todo o DT.

zImage novo de245b0d... e módulo completo ARM32 compilados. Os22 imports do
módulo existem no vmlinux.symvers da árvore nova; vermagic confere. Foi necessário
executar modules_prepare para gerar scripts/module.lds antes do link externo.
Kbuild ainda avisa da ausência de Module.symvers global: foi fornecido
KBUILD_EXTRA_SYMBOLS=vmlinux.symvers, sem suprimir erros de símbolos. Isso não
prova carregamento, modversions ou funcionamento físico. zImage atomic anterior
c68ca21c... permanece byte-idêntico; ciclo, init e registry não foram alterados.

Suíte offline segura:95 casos aprovados. Regressão WSL:528 casos,21 skips,
zero falhas. Os testes C exercitam os gates reais e equivalência do ramo
anterior com o gate novo desabilitado. kselftest do host passou. Extração limpa
do Git:95 casos, quatro skips por fixtures privadas ausentes, zero falhas.
Prova e hashes:
`manifests/mt6357-iio-mfd-offline-verification-20261025.json`.

Próximo bloqueio técnico: revisar exposição/ABI e callbacks dos canais antes de
qualquer probe real. Depois será necessária uma variante física explícita com
símbolos/logbuffer e módulos auxiliares recompilados/pinados para esta árvore,
prova de bind/read/unbind e recuperação automática. Ainda não há provider IIO
validado no telefone nem consumidor power_supply contínuo.

## Lote autônomo: política de reset compartilhado do IIO — 2026-10-25

Décimo candidato `mt6357-auxadc-shared-reset-v1.patch`: MT6357 conserva
no_reset=false (hardware existe), mas ganha capability privada shared_reset.
Probe lê0f90 e exige zero antes de registrar IIO; não pulsa reset nem limpa
estado de firmware. Recusa EBUSY/erro sem escrita. A regra conservadora usa
o banco inteiro, como o ensaio finito: bits1/2/4/5 etc. também são reset no
header LG. Reservados não zero de outras placas podem ser recusados; isso
não é prova de compatibilidade universal nem interpretação de bits reservados.

Segundo timeout sob a política compartilhada guarda ETIMEDOUT no latch
existente, sem reset global/GPS. Aquisições seguintes retornam erro antes de
I/O até reprobe/recuperação explícita. Sucesso entre timeouts quebra a história.
Helper reset recusa EPERM sem I/O mesmo se chamado diretamente; no_reset não
o transforma em sucesso silencioso. SCALE segue metadado. Outros modelos
continuam com as políticas anteriores, verificadas pelos testes legados reais.

Fixture compila reset/probe/read_raw reais:16 cenários reset e32 probe legados
continuam passando no código novo;20 casos probe compartilhado (dez estados
PWRAP/SPMI),4 erros de leitura, recusa de reset direto e timeout/latch/SCALE/
reprobe. Mutex/IIO/regmap são stubs; não equivalência temporal nem prova física.
91 testes offline e524 na suíte completa (21 skips); kselftest do host passou.

Módulo IIO completo foi compilado e linkado ARM32 no workspace novo
mt6357-auxadc-shared-reset-v2,22 imports presentes no vmlinux.symvers fixado e
vermagic correto. Kbuild avisou que Module.symvers global está ausente; usado
KBUILD_EXTRA_SYMBOLS=vmlinux.symvers, sem suprimir warning ou aceitar imports
faltantes. Isso não certifica modversions/dependências de outra árvore nem
carregamento real. zImage atomic continua com SHA c68ca21c...; não foi refeito.

Intermediário v1, que só testava bits0/3 no probe, foi preservado com fontes,
objeto/ko e patch anterior; não selecionado após revisão dos demais bits.
Nenhuma imagem, DT, série automática ou telefone alterado neste lote. Prova:
`manifests/mt6357-auxadc-shared-reset-verification-20261025.json`.

Próxima integração exige variante opt-in MFD/DT: o atomic atual tem
CONFIG_MFD_MT6397_K40S_REGULATOR_ONLY=y e o ramo sem IRQ realmente cria somente
o filho regulator. Um insmod sem filho ADC não provaria probe funcionando.
Não fabricar dispositivo/compat falso para teste verde. Preservar esse ramo e
o boot de recuperação; definir separadamente exposição/ABI dos canais antes
de testar o provider IIO real e o consumidor power_supply contínuo.

## Lote autônomo: comparação BATADC/AP executada no LTS — 2026-10-25

Executado um único ciclo físico com o kernel6.18.58 atomic já validado, sem
rebuild de kernel nem bind do provider IIO staging. Overlay observacional
`k40s-batadc-ap-observe-v1.patch` aplicado somente à cópia de build do ensaio
BATADC: duas leituras10b6, antes do SET e depois do poll genérico. Fontes
originais, módulo/artefatos v2 e as mesmas duas escritas1110/1112 bit0 preservados.
Cada erro novo após SET passou pelo cleanup original nos testes C.

Resultado físico: generic/AP antes=e5aa/e5aa, depois=e842/e842, AP RDY alto.
Ambas as saídas mudaram após o request; valor nominal genérico4398376uV.
Isso valida a relação genérico/AP neste ensaio LTS e apoia os dados do oitavo
candidato. Não prova posse exclusiva, conversão identificada ou equivalência
sob todos os masters; freshness_proven continua false. Não foi exigido valor
diferente, igualdade entre saídas ou observar RDY baixo para aprovar o ensaio.

O fluxo reutiliza builder, preparador, pacote, hook battery-adc e runner
verificado existentes. Flag explícita --battery-adc-ap-compare força
SSH/atomic/host-once e impede outros escritores. Parser específico valida
marker único dentro da janela autorizada, após aprovação do ciclo/recuperação
e com a mesma SHA da imagem. Registra igualdade e RDY como observações, não
aprovação do provider. Runner não classifica esse modo como freshness provada.
Comandos sem a flag seguem usando v2. lts-auto-cycle.py, init, gate, hook ADC e
recuperação não foram modificados.

90 testes offline passaram; suíte completa523 (21 skips no venv,25 na suíte
legada do orquestrador). Provas ARM/OpenRC/PID1, pacote e validação prévia
passaram antes da operação física. No aparelho: autorização SSH de uso único,
snapshot, ADC, USB SSH, rootfs/eMMC RO e retorno/A-B aprovados. Nenhum retry.
Boot normal4.9 retornou automaticamente; hash de boot_a5ffea913... conferido
também por SSH independente. A/B antes/depois9f344802... idêntico.

Provas sanitizadas e hashes:
`manifests/mt6357-batadc-ap-lts-verification-20261025.json`. Logs, imagens e
artefatos privados permanecem excluídos do Git. Preparação sem execução usa
`tools/advance-k40s-lts.py --stage ssh --battery-adc-ap-compare` pelo Python
Windows do laboratório; --execute solicita um único ciclo físico, não monitor
nem repetição automática. Builds/testes C permanecem WSL/Linux.

Próximos bloqueios de integração: política de probe/reset e coexistência GPS,
posse/freshness dos canais, exposição/ABI e callbacks pendentes. Somente então
ligar o provider IIO ao consumidor power_supply contínuo; este ensaio não é
instalação permanente nem conclusão do port de touch/Wi-Fi/display.

## Lote autônomo: observação na placa e erros de impedância — 2026-10-25

SSH confirmou o kernel normal4.9.190-k40s-bringup ativo. Reutilizada a interface
pmic_access auditada: exatamente um endereço hex4 sem espaço/valor solicita
leitura; não usado o ramo de dois tokens que escreve no PMIC. Três passagens
finitas,27 seleções/leitura; sem IIO raw/input, triggers, módulos ou reboot.
BATADC1088/AP10b6=e8ca e ISENSE108a/AP10ba=e79a nas três passagens; reset0f90 e
requests110e/1114=0 nos pontos observados. Uptime avançou16543.67→16543.74s.

Essas observações na BMW apoiam a relação dos registradores e a resolução
ISENSE15bits; NÃO provam atualização, equivalência em todos os modos, posse ou
funcionamento6.18. Interface tem valor salvo global/status de erro ignorado;
nenhuma coincidência deve virar atestado de coerência. Prova sanitizada em
`manifests/mt6357-auxadc-passive-observation-20261025.json`. Captura com seleção
sysfs não é ausência de toda escrita no host/driver: é ausência de pedido de
escrita de VALOR no registrador PMIC; comandos específicos foram auditados.

Nono candidato `mt6357-auxadc-impedance-errors-v1.patch` estende as três funções
MT6358 reutilizadas pelo MT6357. Propaga falhas de setup/read/stop, mantém
primeiro erro, tenta os quatro passos de stop mesmo após falha e só publica
vbat/ibat após sucesso completo. Falha do primeiro setup só desfaz DCM;
depois de tentativa IMP1, stop completo cobre commit incerto. Cleanup falho
usa latch existente; read_raw não tenta reset automático sobre esse estado
e chamadas seguintes recusam aquisição antes de I/O. SCALE permanece metadado.

Teste compila funções reais stop/start/read_imp/read_raw.18 casos de operação
normal/falhas antes/depois de possível commit,8 casos de erro duplo, bloqueio
pós-cleanup, sentinelas e SCALE. Sequência normal/retorno/estado comparados com
as funções reais do oitavo candidato. Outros callbacks/tabelas/probe/reset são
byte-idênticos. Driver completo ARM32 compilado em workspace novo, sem link de
módulo, carga ou imagem. Esse patch compartilhado afeta MT6357 e MT6358, mas
nenhum dos dois foi fisicamente testado com o callback modificado.

Permanecem pendentes: semântica/posse dos bits IMP CLEAR, máscara RDY/dados e
escala do resultado de impedância, reset/GPS, freshness, canais DCXO/VDCXO e
política final de exposição. Preservar correntes/calibrações FG validadas;
o retorno ibat=0 legado do callback não é medição real de corrente. Prova em
`manifests/mt6357-auxadc-imp-verification-20261025.json`. Nada deste lote muda
o kernel instalado, carregador, DT, séries automáticas ou recuperação.

## Lote autônomo: dados AP para integração IIO — 2026-10-25

Oitavo candidato `mt6357-auxadc-ap-channel-data-v1.patch`: somente dados
BATADC/ISENSE/VCDT do provider IIO existente. BATADC passa de1088 para saída
AP10b6 (índice compacto23); ISENSE passa de108a para AP10ba (índice25), de12
para15bits, de CURRENT para VOLTAGE e de requestbit0 para1. VCDT passa de
TEMP para VOLTAGE e de requestbit0 para2. IDs DT, labels, ratios e averaging
preservados. A leitura ISENSE é tensão; não corrente calibrada do fuel gauge.

O teste compila tabela/macros/binding reais após os oito patches, compara
todos os13 canais com a auditoria e exige que só os dados desses três canais
mudem. Funções, callbacks, bancos, macros e todos os outros PMICs permanecem
byte-idênticos ao sétimo candidato. Nomes sysfs dos tipos novos requerem
revisão ABI, como o quinto candidato. Não é alteração aprovada upstream.

Funções reais sample_adc_val/read_adc com descritores novos passaram73728
códigos RAW (BATADC15 + ISENSE15 + VCDT12 + BAT_TEMP12) e32 falhas: request,
poll, timeout, stop, pré-leitura, ocupado e erros duplos. Stubs conferem os
endereços AP, aliases SET/CLR, máscaras, atrasos e preservação de requests de
outros canais; erro preserva sentinela de saída. Falha de stop pode deixar
request ativo: nenhum rollback físico é alegado. Poll no fixture é síncrono,
não simulação temporal do ADC ou prova de freshness.

Driver completo compilado ARM32 em workspace novo `mt6357-auxadc-ap-data-v1`.
Nenhum módulo foi linkado/carregado e nenhuma imagem gerada. zImage ativo e
build.json/.ko coulomb v1 conferidos por SHA256, inalterados. Captura BATADC v1
continua usando1088; este candidato não substitui o caminho físico validado.

Antes de ativar: comparar saídas genérica/AP na placa, comprovar ownership e
freshness, resolver reset/GPS, fechar exposição dos canais e auditar callback
de impedância. DCXO/mux e VDCXO continuam pendentes, não habilitados por este
patch. Carregador, seleção física, séries, DT e recuperação inalterados.
Prova em `manifests/mt6357-auxadc-ap-data-verification-20261025.json`.

## Lote autônomo: mapa completo do AUXADC — 2026-10-25

Auditoria dos 13 canais expostos concluída em relação às fontes fixadas, não
à placa física. Os testes compilam tabelas/macros/binding reais do candidato
de sete patches e, separadamente, o header LG real, após verificar quatro
hashes de origem. A referência numérica fica no manifesto
`manifests/mt6357-auxadc-channel-audit-20261025.json`. Os testes reproduzem as
divergências; PASS não significa compatibilidade nem autorização de uso.

| Canal/grupo | Constatação | Próxima decisão necessária |
| --- | --- | --- |
| BATADC | Upstream e captura v1 leem1088; LG seleciona saída AP10b6 | Explicar relação entre saídas antes de substituir endereço validado |
| ISENSE | Request bit0 versus bit1 LG;12 versus15 bits;108a versus10ba AP | Resolver mapa/resolução/unidade conjuntamente, não só request |
| VCDT | Request bit0 versus bit2 LG; tipo TEMP apesar de tensão | Corrigir candidato de dados após fechar política de canais/ABI |
| BAT_TEMP | Banco/máscara/endereço/resolução conferem | Ainda requer posse/freshness e calibração/compensação do consumidor |
| DCXO_TEMP | Request bit10 versus bit4 LG; callback de mux AP ausente | Não copiar escrita de mux sem auditar coexistência e cleanup |
| VDCXO | Exposto sem descritor; RAW recusado pelo guard, SCALE ainda zero | Não tratar como canal utilizável; revisar exposição/ABI |
| VCORE/VPROC/DCXO/IMP | Endereços conferem após resolver macros LG | Não trocar índice compacto pelo número simbólico ADC do header |
| Outros canais de temperatura/resistência | Mapa pode conferir sem unidade física pronta | Scale de tensão não equivale a milliCelsius/ohms; revisar ABI/calibração |
| VBAT impedância | Saída10c4 confere; callback tem erros regmap ignorados | Auditar start/read/stop separadamente; não confundir com BATADC |

VBIF tem descritor mas não é exposto; hook LG altera BATON_TDET_EN. Não expor
simplesmente adicionando linha na tabela. A referência é HM, sem comprovação
integral de equivalência BMW ou dos overrides DT efetivos do aparelho.

No fixture existente, funções reais de aquisição aceitam duas leituras iguais
quando o modelo mantém RDY alto e resultado em cache, sem simular conversão.
Isso demonstra insuficiência desse contrato para provar freshness, não dado
obsoleto no telefone. Duas conversões reais iguais também seriam legítimas.
Não foi imposto requisito especulativo de observar RDY baixo. Polling MDRT
baixo→alto do vendor pertence a outro caminho e não foi transplantado.

Header LG agora identifica bit0 de reset como RG_AUXADC_RST e bit3 como
BANK_AUXADC_SWRST. Contudo, LG pulsa os dois separadamente e refaz requests
CH7/GPS DCXO; upstream pulsa simultaneamente e não recompõe esses requests.
Logo, nomes dos bits não encerram a auditoria dos efeitos/coexistência.

Nenhum novo patch de driver foi criado neste lote: corrigir só três bits
deixaria saídas, unidades e callbacks pendentes. Preservados os sete candidatos,
build ARM32 anterior, capturas finitas e recuperação. Sem alteração de DT,
imagens, séries, perfis, seleção física ou telefone. Próxima implementação:
fechar um subconjunto mínimo de canais com semântica de tensão e auditar
callbacks/efeitos necessários antes de integrar consumidor power_supply.

## Lote autônomo: falhas do reset AUXADC — 2026-10-25

Sétimo candidato staging: `mt6357-auxadc-reset-errors-v1.patch`, extensão do
driver IIO existente, sem novo provider. Reset agora retorna o primeiro erro
regmap; tenta deassert mesmo após assert incerto e relock mesmo após unlock
incerto. Se o reset do probe falha, IIO não é registrado. Após recuperação
falha em runtime, mantém o timeout original e bloqueia próximas aquisições
com o erro guardado, sem novo I/O, até reprobe explícito. SCALE permanece
metadado acessível. Nenhum retry ou reprobe automático adicionado.

Funções reais reset/read_raw/probe foram compiladas em fixture com stubs das
fronteiras regmap/IIO: 16 cenários de reset keyed/unkeyed, falha antes/depois do
commit e sucesso; 32 cenários de probe cruzados com topologia PWRAP/SPMI;
falhas duplas preservando prioridade; no_reset, falta de match/regmap/memória,
erro de registro, bloqueio pós-recuperação e recuperação bem-sucedida. O modelo
injeta falhas por chamada regmap, não simula todos os passos do barramento.
Mutex guard também é stub; a prova pthread anterior permanece separada.

Os sete candidatos compilaram objeto ARM32 em workspace novo, preservando o
anterior. Suíte segura: 82 testes; suíte WSL completa: 515 testes, 21 skips;
kselftest das interfaces do host passou. Nenhum desses resultados certifica
o reset físico. Não foi executado novo KUnit/UML do driver ADC; testes KUnit
anteriores do core IIO não devem ser atribuídos a esta alteração.

Bloqueios antes de habilitar: finalidade/posse dos bits de reset do MT6357,
conversão realmente nova/RDY, concorrência de outros masters, descritores
ISENSE/VCDT e ABI dos tipos IIO. Um valor igual ao anterior pode ser legítimo;
exigir valor diferente não prova freshness. Exigir observar RDY baixo também
precisaria de garantia temporal/documentação que ainda não temos. Não inventar
tais garantias nem substituir a captura finita validada. Carregador continua
desabilitado; sem alterações em imagens, DT, séries, seleção física ou telefone.

Proveniência, hashes e limites em
`manifests/mt6357-auxadc-reset-verification-20261025.json`.

## Lote autônomo: tipos, unidades e requests — 2026-10-25

Quinto candidato staging: `mt6357-auxadc-voltage-types-v1.patch` corrige somente
BATADC e BAT_TEMP do MT6357 para IIO_VOLTAGE. IDs DT, labels, ADC addresses,
resoluções e demais descritores preservados. BAT_TEMP é tensão do divisor, não
temperatura já calibrada; nomes sysfs derivados dos tipos mudam e exigem revisão
ABI antes de adoção. Driver completo compilado ARM32 em workspace novo.

Testes agora compilam tabela/macros/binding reais e APIs reais IIO
read_channel_processed, processed_scale e convert_raw_to_processed_unlocked.
73728 comparações (todos os códigos15/12 bits, saídas mV/uV) passaram; mantidas
110592 comparações de escala anteriores. A API scale1000 gera uV sem truncar
primeiro em mV; scale1 mantém o truncamento mV usado no modelo LG. Nenhum novo
conversor ou consumidor próprio. Erros EIO/ENODEV preservam sentinela do caller.

Sexto candidato: `mt6357-auxadc-request-alias-v1.patch`, capability ligada somente
nos dados MT6357. Usa SET/CLR +2/+4 dos bancos110e/1114 documentados no header LG,
preserva requests de outros canais e retorna EBUSY/erro antes de qualquer escrita
se o próprio bit já está ativo ou a pré-leitura falha. Outros PMICs conservam o
caminho anterior (88 comparações de trace/retorno); caminho aliases passou88
combinações de banco/canal/falha/estado inicial. Atividade em outro bit entre
read/SET é preservada; corrida no MESMO bit continua demonstravelmente possível.
Aliases não são aquisição atômica de posse nem prova de dado novo/RDY.
Máscara zero ou índice de request fora dos dois bancos suportados retorna
EOPNOTSUPP sem I/O. A compilação inicial sem essa validação foi preservada como
intermediária, não selecionada; o candidato final usa workspace alias-v2.

Os seis candidatos juntos compilaram objeto ARM32. Preservados todos os
workspaces/artefatos e provas anteriores; nenhuma imagem, registry, DT, bind ou
telefone alterado. Ordem: escala → stop → história → lock → tipos → aliases.

Reutilização adicional revisada: ntc_thermistor já exige IIO_VOLTAGE e usa a API
processed_scale1000, mas modelos/calibração LG e truncamento não são automaticamente
equivalentes. generic-adc-thermal pode publicar/clamp temperatura a partir de
tabela e, sem tabela, assume milliCelsius: não serve diretamente para nosso RAW
de tensão com rejeição de falhas e compensação por corrente. Não habilitar tais
consumidores como substitutos completos nem copiar sua infraestrutura.

Bloqueios físicos explícitos: posse contra outros masters, freshness/RDY,
reset/rollback e revisão de todos os canais/callbacks expostos. ISENSE/VCDT
upstream usam requestbit0 enquanto mapa LG identifica bits1/2: indício adicional
a fechar antes de expor o driver completo; esta etapa não altera esses canais.
Manter ensaios finitos validados e carregador desabilitado.

Regressão WSL: 514 casos, 21 ignorados, zero falhas. Arquivo source-only passou81
com três comparações privadas ignoradas. Prova completa e hashes:
`manifests/mt6357-auxadc-types-alias-verification-20261025.json`.

## AUXADC upstream: escopo do mutex — 2026-10-25

Quarto patch staging `mt6357-auxadc-recovery-lock-v1.patch`: trocar scoped_guard
da aquisição por guard(mutex) de duração até o retorno do read_raw. Mesmo mutex
Linux, sem novo lock, driver, API ou máquina de estados. Ordem de aplicação:
escala → stop → história → lock. Nenhum patch entrou em série/registry/DT.

Comparação sequencial: 88 casos (dois canais, 11 falhas, dois estados iniciais de
request, dois históricos), com mesmo retorno, out, timed_out, registros e trace
do candidato anterior. Assertivas exigem lock durante todo I/O, inclusive reset,
e liberação em todos os retornos testados. SCALE não adquire lock nem faz I/O;
IBAT/VBAT não suportados retornam erro e liberam. Callbacks de impedância
simulados foram exercitados com sucesso/EIO/timeout e
histórico inicial ligado/desligado (24 combinações). Os callbacks reais de
impedância/registradores não são validados por esses stubs. Dois leitores pthread, oito
leituras cada: semáforos forçam o segundo a observar EBUSY enquanto o primeiro
segura o mutex; sem suposição de tempo/sleep para produzir contenção.

Driver completo compilado ARM32 com guard/mutex reais do kernel. O harness host
modela escopo com pthread e cleanup GCC: não prova lockdep, escalonador kernel,
IRQ/cancelamento ou exclusão com firmware. As suítes KUnit anteriores não foram
reexecutadas nem são prova deste patch de lock. Artefatos anteriores preservados.

Bloqueios restantes antes de bind físico: propriedade do banco de requests,
reset do probe/reincidência e restauração, tipos/unidades e efeitos em GPIO de
PMICs SPMI. Não tratar lock local como solução para masters externos. Kernel,
fontes ativos, recuperação e celular não foram alterados.

Verificação: 81 testes offline; regressão WSL514 com21 ignorados, zero falhas;
kselftest TAP aprovado. Arquivo Git source-only passou81 com três comparações
privadas ignoradas. Evidência: `manifests/mt6357-auxadc-lock-verification-20261025.json`.

## AUXADC upstream: falha de stop e história de timeout — 2026-10-25

Sem novo driver/provider: dois patches pequenos no driver existente, ambos
somente staging. `mt6357-auxadc-stop-error-v1.patch` impede publicar amostra
quando stop falha, preservando o erro de aquisição se ambos falham. Sua aplicação
isolada expõe reset imediato por timeout no stop: preservada como etapa parcial,
NÃO como candidato físico. `mt6357-auxadc-timeout-history-v1.patch` captura a
história anterior sob o mutex existente, distinguindo falha atual de reincidência.
Aplicar candidatos na ordem escala → stop → história; nenhuma série os inclui.

Funções reais upstream sample_adc_val/read_adc/read_raw testadas com regmap
simulado: 44 comparações de traces para BATADC/BAT_TEMP, requests inicialmente
livres/ocupados, falhas antes/depois de commit, timeout e erro duplo. No caminho
read_adc, mesmo I/O e nenhuma tentativa adicional; resultado intencionalmente
rejeitado nos erros de stop. Sequências completas provam primeira falha sem
reset imediato, segunda falha com recuperação existente e sucesso limpando a
história. Não há prova de concorrência nem exclusão com firmware.

Os três patches juntos compilaram o driver completo em objeto ARM32. Continuam
bloqueios de bind: reset de probe e após reincidência; banco compartilhado;
processamento de erros fora do mutex; tipos/unidades; cleanup GPIO de outros
PMICs. Não se alterou DT, recovery, preparador, kernel ativo ou telefone.

Runner UML agora REUTILIZA a suíte upstream `iio-multiply`, sem novo teste C:
dez casos passaram em três suítes (IRQ3 + CAR3 + IIO4). Hashes de inkern.c e
iio-test-multiply.c são verificados antes do build; configuração recusa rede,
hostfs, módulos, ALL_TESTS e o driver AUXADC. Esse KUnit prova somente lógica
do core/políticas, não execução dos patches ADC ou comportamento elétrico.

Verificação: 81 testes offline; regressão WSL514, 21 ignorados, zero falhas.
Prova: `manifests/mt6357-auxadc-error-verification-20261025.json`.

kselftest TAP passou; cópia Git source-only passou81, com três comparações
privadas explicitamente ignoradas. Fontes Linux externas fixadas continuaram
disponíveis no host para os testes upstream. Nenhuma evidência física nova.

## Prioridade upstream: AUXADC existente — 2026-10-25

Em vez de extrair mais um driver próprio, a comparação passou a executar
funções reais do driver IIO MT6357 já presente e do core IIO. Confirmada falta
do divisor 2^realbits em SCALE; candidato mínimo em
`patches/kernel/staging/mt6357-auxadc-scale-v1.patch`, fora de séries e registry.
110592 comparações numéricas aprovadas para 12/15 bits e denominadores1/2/3;
objeto do driver completo compilado ARM32 em cópia isolada. O kernel/fonte
ativos não foram modificados e nada foi carregado no telefone.

Isso NÃO autoriza substituir aquisição validada: probe/timeout resetam,
request/stop alteram banco compartilhado, erro no stop pode publicar amostra,
BATADC/BAT_TEMP têm tipos IIO que precisam revisão. Matriz detalhada na auditoria
de reutilização. Decisão: estender IIO existente, manter somente FG/calibração
inevitáveis; não ampliar provider ADC próprio. Próxima prova aritmética pode
reutilizar a suíte KUnit upstream iio-multiply, já existente, sem novo runner.

Verificação: 79 testes offline, 512 na regressão WSL (21 ignorados), zero
falhas. Cópia limpa source-only passou79 (três comparações privadas ignoradas;
fontes Linux fixadas disponíveis separadamente no host). Prova completa:
`manifests/mt6357-auxadc-upstream-verification-20261025.json`.

## CAR MT6357: aquisição por componente — 2026-10-25

Sequência de latch extraída para `kernel/components/pmics/mt6357/mt6357-car-latch.h`,
usando regmap upstream. Adaptador `kernel/devices/lg-k40s/mt6357-car-acquire.h`
retém veto dos campos desconhecidos da placa e API antiga. Não há framework de
I/O paralelo: exclusão, identificação do PMIC, tempo máximo e autorização
continuam com o consumidor existente. Os polls mantêm 100/32000 us.

Comparador host verifica retorno, amostras, registros finais e trace exato de
leituras/escritas contra sequência original hasheada: todos os 65536 padrões
CON1, 160 cenários (inclui erros de leitura, escrita incerta, timeout e drift),
argumentos inválidos sem I/O. A suíte offline passou 76 testes. Candidato v4
compilado ARM32 contra kernel atomic fixado, não carregado nem selecionado no
preparador físico. Fontes e artefatos v1 intactos; v2/v3 preservados.

Não é suporte contínuo de bateria, percentual/SOC ou carregamento. A nova
sequência ainda não foi executada em KUnit/UML nem no telefone. Próximo passo:
estender a prova KUnit antes de propor integração física explicitamente
versionada, preservando a recuperação v1.

Regressão WSL: 509 casos, 21 ignorados, zero falhas (transportes simulados).
kselftest TAP aprovado; arquivo Git source-only: 76 casos, três comparações
privadas ignoradas. Evidência: `manifests/mt6357-car-latch-verification-20261025.json`.

## CAR MT6357: primeira extração real — 2026-10-25

Helper C GPL-2.0-only independente em `kernel/components/pmics/mt6357`: monta
campos CAR, sinal e sentinelas, sem unidades, calibração, I/O ou registro de driver.
Adaptador K40S novo mantém RFG100/tune1000, arredondamento100uAh, recusa de outras
calibrações, API e erros. Código reutilizável e código da placa são hasheados em
campos separados do inventário; não há alegação de driver contínuo ou SOC.

A revisão encontrou pin de fontes no preparo v1: header, Makefile, aquisição,
artefato e seletor físico v1 foram mantidos intactos. Builder agora gera candidato
v3 com a ponte nova; v2 intermediário foi preservado, nunca selecionado/carregado.
Não criamos imagem nem enfraquecemos o verificador de fontes para aceitar v3.

Comparadores host passaram todos os 2^21 payloads na cadeia ponte nova→ponte v1
congelada por SHA→função LG original. KUnit UML executou seis casos em duas
suítes; objetos ARM32 e módulo candidato também compilaram. Isso não prova
funcionamento elétrico/runtime ARM32 no telefone. Nada foi carregado no aparelho.

## Implementação inicial por componentes — 2026-10-25

Catálogo independente com seis definições: arquitetura ARMv8/ABI ARM32, SoC
MT6762, controlador I2C MediaTek, PMIC MT6357, charger MT6371 e touch FT5446.
K40S passa a compor sete instâncias (inclui dois I2Cs da mesma definição), com
conexões referenciadas no perfil, dependências e estado de validação por instância.
Áudio/codec, Wi-Fi/Bluetooth, display e calibração permanecem pendências da placa.

Ação `kernel-workspace.py components --board k40s` valida schemas locais via
jsonschema existente, referências, DAG, origens, paths e campos da placa. Produz
inventário com hashes/fingerprint; não altera build, Kconfig, DT, registry ou
transporte. Fixture de segunda placa prova reutilização do catálogo apenas em
teste sintético, não compatibilidade física com outro dispositivo.

Código C legado e todos os paths de recuperação continuam onde estavam. Não
há alegação de extração completa de drivers: índice distingue fontes legadas
ainda acopladas de alternativas upstream e dados da placa. Fingerprint do plano
vendor preservado; ciclo, DA, flash, gate, registry e init não mudaram nesta etapa.

Verificação: 71 testes offline e kselftest TAP aprovados; regressões WSL/Windows
com 504 casos e 21/138 ignorados, zero falhas. Windows sem jsonschema informa
explicitamente a dependência do venv oficial. Cópia limpa: 71 casos, somente
três comparações privadas ignoradas. Paths candidatos upstream conferidos na
árvore fixada. Prova: `manifests/component-composition-verification-20261025.json`.

## Continuação autônoma — pasta, SSH e defaults MediaTek (2026-10-25)

Resumo histórico sanitizado em 2026-10-29: caminhos pessoais Windows/Linux foram
omitidos deste parágrafo. A organização preservou fontes, firmware, runtime,
venv e builds existentes. Os registros originais de evidência não foram alterados.
O código atual descobre o checkout e usa configuração local, sem exigir o alias.

O ciclo lê identidade SSH e alvo normal do lab.json local ignorado, sem fallback
com chave privada embutida. Carregamento lazy: clone público pode importar/testar
o código sem config privada, mas operações exigem configuração válida. O pin do
payload, autenticação, ledger/nonce, timeouts e política sem retry são mantidos.
A instância importada do helper normal recebe settings; a CLI standalone antiga
continua byte-idêntica à baseline e não foi generalizada.

Hwcode esperado e defaults atomic_logbuf vêm do perfil via backend MediaTek;
identificação real e protocolo permanecem na sessão DA. Bytes restantes dos dois
scripts são comparados com a baseline após desfazer apenas as mudanças aprovadas
em memória. Diagnóstico K40S e defaults continuam iguais.

Retomada do hardware começou pela auditoria I2C upstream de probe, erro, remove
e resume, registrada em `docs/k40s-i2c-upstream-integration-audit.md`. Bind direto
não é equivalente ao FIFO validado: há resets e DMA. Nenhum novo driver, bind de
charger, imagem, boot ou acesso ao telefone nesta etapa.

Pendências: consumidores standalone legados e movimentação física do histórico
podem esperar. Para o port, fechar callbacks CCF e mapa/quirks do I2C antes de
integrar IRQ/DMA/reset. Não afirmar driver contínuo de bateria por passar mocks.

Verificação: 63 testes offline, zero falhas; kselftest TAP aprovado. Regressões
WSL/Windows: 496 casos, 21/130 ignorados explicitamente, zero falhas. Cópia limpa
somente de fontes: 63 casos, três ignorados por fixtures privadas ausentes.
Auditoria CCF existente repetida na pasta nova produziu relatório byte-idêntico
e reconferiu o zImage atomic; continua sem cobrir todos os callbacks CCF.
Cadastro do projeto confirmado no caminho novo. Hashes e limites em
`manifests/renamed-root-lab-mtk-verification-20261025.json`.

## Nome do projeto — 2026-10-25

Nome adotado pelo usuário: Kernel Porting Framework (KPF). README, arquitetura
e ambiente de desenvolvimento passam a usar o nome. Esta etapa é exclusivamente
documental: diretório lg-k40s-linux-port, pacote portkit, scripts, perfis, hashes,
licenças/atribuições e caminhos de recuperação permanecem inalterados. Não houve
verificação de disponibilidade do nome, criação de remoto ou publicação.

## Continuação — geometria e capturas DA no perfil (2026-10-25)

`k40s-da-session.py` passou a ler `boot_a_sector`, `boot_a_bytes`, `sector_bytes`,
SHA da recuperação e regiões pstore/lklog/atflog do perfil fixo K40S. Valores e
ordem equivalem aos literais originais. Loader rejeita bool/não inteiros,
geometria inválida, SHA não canônico, desalinhamento, overflow e sobreposição.
Configuração inválida interrompe no import, antes de iniciar transporte.

O teste desfaz exatamente o hunk de configuração em memória e exige o SHA-256
original do restante da sessão DA. Não alteramos verificação GPT, readback,
fallback, framing, reset, prazos ou sequência de comandos. SHA do DA, hwcode,
logbuf e SSH seguem legados; não há backend Qualcomm nem seleção de outra placa.
Auditoria registrada antes do código; nenhum checkout de terceiro foi atualizado.

Entrada segura: 58 testes, zero falhas/ignorados. Regressão Windows: 491 casos,
130 ignorados explicitamente, zero falhas. Evidências complementares desta etapa
ficam em manifesto separado. Sem telefone, imagem de boot nova ou execução UML
nova: C/KUnit não foram modificados nesta continuação.

Regressão WSL: 491 casos, 21 ignorados, zero falhas. Extração limpa somente de
fontes: 58 casos, três ignorados por fixtures privadas ausentes, zero falhas,
nenhum transporte carregado. Prova e hashes:
`manifests/da-profile-verification-20261025.json`.

Pendências: migrar configuração SSH do laboratório com equivalência e sem chaves
no Git; avaliar separadamente hwcode/logbuf e demais consumidores legados. Os
históricos continuam preservados nos caminhos canônicos.

## Continuação — defaults do ciclo e cobertura IRQ (2026-10-25)

O ciclo passou a ler apenas caminho de restauração e release normal do perfil
K40S. Os valores anteriores são exigidos por testes; caminhos que escapam do
projeto e releases inválidas falham antes do transporte. Um teste desfaz somente
o hunk aprovado em memória e confere o SHA-256 original do restante do ciclo.
DA, flash, registry, ledger e init continuam byte-idênticos à baseline. Isso é
paridade offline, não validação física da configuração nova.

Cobertura KUnit ampliada sem alterar helper/driver: repetições após término,
todos os bits de erro, erro desconhecido tardio, cancelamento, zeros/RS e NULL.
Oráculo C host preservado. Objeto ARM32 compilado em saída nova, sem imagem para
o telefone. Provas UML e hashes desta continuação são registrados em manifesto
separado, sem sobrescrever as provas da versão anterior.

Entrada segura: 55 testes aprovados, sem transportes. Regressão Windows: 488
testes, 130 ignorados explicitamente, zero falhas. Os 12 grupos históricos ainda
têm consumidores; hashes de todas as fontes do catálogo agora são verificados
na suíte segura. Nenhum experimento foi movido ou apagado.

KUnit executou os três casos ampliados em UML; objeto ARM32 e kselftest TAP
também passaram. A primeira execução ampliada falhou por estado compartilhado
entre cenários do próprio teste; foi preservada, e a correção apenas reinicializa
a fixture. Nova árvore isolada executou tudo com sucesso. Regressão WSL: 488
casos, 21 ignorados, zero falhas. Cópia limpa: 55 casos, três ignorados apenas por
fixtures privadas ausentes. Hashes e limites em
`manifests/profile-cycle-kunit-verification-20261025.json`.

Pendências reais: migrar DA/DRAM/GPT/hashes/SSH em passos próprios; converter
outros helpers puros; atualizar consumidores antes de mover histórico. Não são
pré-requisitos para retomar o port e não justificam reescrever a recuperação.

## Continuação — execução KUnit/UML (2026-10-25)

O kernel UML 6.18.58 executou os três casos de política IRQ: 65.536 status,
erro tardio/notificação única e limite/cancelamento. Duas invocações explícitas
passaram, com os mesmos hashes do kernel, config e JSON oficial. Fonte extraído
do tarball fixado em uma árvore nova; árvore ARM/telefone/recuperação intocados.

`tools/run-kunit-offline.py` reutiliza `kunit.py build`/`exec`, verifica isolamento
antes de executar e preserva cada tentativa. Core ganhou somente controle POSIX
de prazo/limpeza de processos host. A entrada rápida offline passou 51 casos,
incluindo negativos de config insegura, resultados incompletos e timeout/falha.
Regressão: 484 casos no WSL (21 ignorados) e Windows (129 ignorados), zero falhas.
Cópia limpa do Git: 51 casos, três ignorados por fixtures privadas ausentes,
zero falhas e nenhum transporte carregado.

Prova: `manifests/kunit-uml-verification-20261025.json`. Isso não comprova hardware
nem dispensa ARM32/C/oráculos antigos. Migração das constantes do ciclo físico e
conversão dos demais testes continuam pendentes.

As seções abaixo preservam marcos anteriores; pendências mencionadas nelas
descrevem o estado da etapa correspondente.

## Continuação — perfis e libfdt (2026-10-25)

- Diretório runtime default do kernel-workspace vem do perfil, mantendo o valor
  anterior e a precedência da opção explícita; fingerprint preservado.
- Rota IRQ I2C5 usada pelos dois utilitários offline vem de `boards/k40s/profile.json`.
- Staging passa a usar libfdt/check_full, sem fallback; parser de coleta/recuperação
  permanece inalterado. Todas as propriedades/reservas equivaleram ao parser
  antigo nos seis DTBs reais e no caso sintético com reservas acima de 4 GiB.
- Seis overlays em ambas as ordens passaram; DTB staged manteve SHA-256
  `1f05ae734ac6975d1824991b0f5a8f09c57b42042bf1d6b381bbe49219b7a6c3`.
- Entrada segura: 44 testes, zero falhas/ignorados no laboratório. Regressão WSL:
  477 testes, 21 ignorados, zero falhas. Relatórios novos preservados no work,
  referências/hashes públicos em `manifests/profile-dt-verification-20261025.json`.
- Cópia limpa extraída do Git: 44 casos, três ignorados por fixtures privadas
  deliberadamente ausentes, zero falhas. Windows: 477 casos, 124 ignorados,
  zero falhas; os testes novos respeitam a classificação POSIX.

Sem acesso ao telefone, imagem de boot, ativação de IRQ/charger ou mudança nos
bytes do ciclo/DA/gate/registry/init. Ainda pendem migração das constantes do
ciclo físico com paridade e execução KUnit UML/QEMU.

## Primeira etapa

2026-10-25. Nenhuma operação no telefone foi executada nesta etapa.

| Itens do pedido | Estado |
| --- | --- |
| 1–3 Git/exclusões/baseline | Repositório local criado; commit anterior à refatoração, hashes de fontes/resultados físicos, versões, recuperação e limitações registrados |
| 4–5 terceiros e patches | Nove checkouts identificados por commit, origem/licença/motivo/limitações; três patches exportados e reverse-check sem escrita. Arquivos de distribuição sem Git identificados por release/hash, sem inventar commits |
| 6 licenças | MIT nas ferramentas/documentos próprios, GPLv2 kernel; sete C/H corrigidos; avisos de terceiros preservados. Anotações SPDX REUSE para fontes host mantidas byte-idênticas |
| 7–8 ambiente/Windows | WSL Ubuntu24.04 oficial; ambiente isolado de DT e lock; três falhas POSIX do Windows explicitamente ignoradas |
| 9–14 camadas/ciclo | Core extraído e usado em kernel-workspace; perfis e contratos criados. Ciclo/DA ainda na implementação legada byte-idêntica. Não há backend Qualcomm funcional nem transporte ADB/fastboot novo |
| 15 kernel-workspace | Seleção --board e perfil default K40S implementados, fingerprint preservado; não é suporte automático a outro aparelho |
| 16 DT | DTC/dt-schema/libfdt disponíveis diretamente; teste com libfdt e invariantes. Parsers antigos mantidos até equivalência, não substituídos em massa |
| 17–19 novos drivers/bateria/charger | Política registrada; arquitetura futura documentada. Nenhum novo driver habilitado, nenhum bind automático do carregador |
| 20 KUnit/kselftest | Primeira lógica pura IRQ portada e objeto ARM32 compilado; selftest TAP passou. Execução KUnit UML/QEMU e conversão dos demais casos ainda pendentes |
| 21–22 classificação/entrada offline | Catálogo AST com IDs, incluindo herança, e runner allowlist sem transportes. Suíte histórica continua separada, dependente do laboratório |
| 23–24 arquitetura/segundo aparelho | Arquitetura documentada; outro MediaTek antes de Snapdragon após paridade. Nenhum segundo aparelho iniciado |
| 25 histórico | Catálogo lógico com hashes/paths/evidências; sem apagar/copiar módulos. Movimentação física adiada para não quebrar consumidores/recuperação |

Pendências prioritárias: migrar leituras legadas de constantes para o perfil em
passos pequenos com paridade; executar KUnit num kernel de teste offline; expandir
allowlist apenas com revisão de dependências; terminar equivalência dos parsers
DT antes de retirá-los. Não trocar o ciclo físico de uma vez para concluir a lista.

Não confundir estes resultados com validação física da reorganização: preservamos
os bytes críticos e executamos regressão offline, sem novo boot/flash.

Verificação: entrada segura 35/35; regressão WSL no venv 470 casos, 21 ignorados,
zero falhas; Windows 470 casos, 120 ignorados, zero falhas. Selftest TAP aprovado;
objeto KUnit ARM32 compilado, sem execução. Hashes da imagem local de recuperação
e zImage atomic reconferidos e iguais aos fixados. Detalhes em
`manifests/organization-verification.json`.

Uma extração limpa de `git archive` também passou: 35 casos, dois explicitamente
ignorados por ausência das evidências privadas. Sem diretórios work/artifacts,
checkouts de terceiros, backups ou chaves na cópia. Nenhum transporte carregado.
