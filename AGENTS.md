# Prioridade de trabalho: sistema funcional e validacao proporcional

Instrucao do usuario, registrada em 2026-10-27.

O objetivo principal e fazer os recursos funcionarem no aparelho. Testes,
telemetria, auditorias e organizacao devem apoiar a entrega funcional e resolver
bloqueios concretos, com profundidade proporcional ao risco da mudanca.

1. Antes de cada etapa, definir uma entrega observavel no aparelho, seus criterios
   minimos de aceite e o bloqueio tecnico que a etapa pretende resolver.
2. Reaproveitar primeiro codigo LG/vendor disponivel e drivers/frameworks upstream.
   Adaptar o caminho existente mais completo e compativel. Usar engenharia reversa
   somente para lacunas de fonte, compatibilidade ou comportamento nao esclarecidas.
3. Trabalhar em incrementos pequenos: integrar, compilar, verificar os caminhos
   criticos, ensaiar temporariamente quando autorizado e corrigir o problema real.
   Nao exigir acabamento de framework universal antes da primeira entrega funcional.
4. Antes do ensaio, executar compilacao e verificacoes direcionadas a mudanca,
   incluindo falhas relevantes, limites eletricos e recuperacao. Aproveitar testes
   existentes; nao criar testes que apenas espelhem a implementacao nem repetir
   suites amplas sem mudanca, falha ou dependencia que justifique a repeticao.
5. Apos a primeira integracao funcional, consolidar as falhas encontradas em testes
   de regressao e ampliar cobertura, duracao e telemetria conforme necessidade.
   Validacao de carga, protecao termica e caminhos destrutivos precede sua ativacao;
   nao adiar esses controles em nome de uma entrega antecipada.
6. Coletar apenas a telemetria necessaria para decidir o aceite, diagnosticar a
   falha e verificar a recuperacao. Evitar novos diagnosticos, matrizes exaustivas,
   variantes e manifestos quando as evidencias existentes ja respondem a pergunta.
7. Adiar generalizacao especulativa, catalogos sem consumidor e infraestrutura
   sem utilidade demonstrada. Mecanismos comprovados uteis a proximos portes
   devem ser reaproveitados no KPF conforme a diretriz abaixo, sem bloquear a
   entrega funcional nem exigir novas abstracoes universais.
8. Reportar progresso pelo que passou a funcionar no aparelho, pelo que foi
   verificado apenas offline e pelo proximo bloqueio concreto. Quantidade de testes
   e evidencia complementar; compilacao ou mocks nao equivalem a funcionamento.
9. Para bateria, priorizar tensao, corrente e temperatura com atualizacao continua
   em power_supply, depois estado de carga e energia/suspend-resume. Percentual/SOC
   e controle de carregamento sao entregas proprias, salvo dependencia demonstrada.
10. Esta diretriz nao autoriza carga, flash, operacoes fisicas ou uso permanente.
    Respeitar a autorizacao vigente, backups, limites e mecanismos de recuperacao.
    Nao desabilitar testes/protecoes existentes nem relaxar verificadores para obter
    um resultado aprovado. Ao substituir codigo validado, aplicar a equivalencia
    funcional e sob falha exigida abaixo, focada nos comportamentos afetados.

# Primeira entrega: Linux 6.18 utilizavel com Wi-Fi e Bluetooth

Escolha do usuario, registrada em 2026-10-28.

1. Manter o kernel novo 6.18 como alvo. Primeira entrega: boot reproduzivel,
   armazenamento e userspace basicos, Wi-Fi e Bluetooth internos, rede USB/SSH,
   tela/touch basicos e energia com medicoes de bateria e carga protegida.
   Preservar os componentes ja validados
   e fechar somente os bloqueios que impedem essa composicao funcionar junta.
2. Wi-Fi e Bluetooth internos sao prioritarios na primeira entrega. Reaproveitar
   fontes LG/WMT/gen4m/BT e firmware existentes, adaptando somente dependencias
   necessarias. Entregar cada radio em incremento proprio, sem esperar o outro.
   Manter rede USB/SSH como acesso de desenvolvimento e recuperacao. Adiar GPU
   acelerada, cameras, modem/GNSS e audio completo, salvo dependencia concreta
   dessa entrega demonstrada por escrito.
   Preservar fontes, patches, testes e resultados dessas frentes sem expandi-las.
3. Preferir drivers upstream compativeis ou fonte LG/vendor com adaptacoes pequenas,
   conforme menor caminho comprovado para a entrega. Nao exigir upstreamizacao,
   reescrita arquitetural, migracao para pmbootstrap ou generalizacao para concluir
   o prototipo. Nao transportar a pilha vendor inteira para satisfazer um detalhe.
4. Aceite da primeira entrega deve registrar funcionamento conjunto, acesso USB/SSH,
   Wi-Fi associado com endereco IP e trafego, Bluetooth com descoberta, pareamento
   e comunicacao basica com periferico disponivel, tela/touch basicos e comportamento
   de bateria/carga, com recuperacao preservada. Registrar o perfil Bluetooth
   efetivamente validado; audio Bluetooth completo nao e requisito desta etapa.
   Preparacao offline, bind isolado ou status Charging sozinho nao comprovam carga
   efetiva nem autorizam uso permanente. Medir o proximo bloqueio contra esse aceite.
5. Esta escolha reorganiza prioridades; nao autoriza novos testes fisicos, flash,
   instalacao permanente, retirada de protecoes ou mudanca de limites eletricos.
   Depois do minimo funcional, escolher a proxima funcionalidade com o usuario.

# Portabilidade de paths e configuracao local

Instrucao do usuario, registrada em 2026-10-29.

1. Nao introduzir caminhos absolutos especificos da maquina/usuario no codigo
   executavel, scripts de build, instaladores ou defaults publicos. Exemplos:
   C:/Users/<usuario>, /mnt/c/Users/<usuario> e /home/<usuario>. Nao depender do nome antigo
   da pasta do projeto, de junctions ou do diretorio corrente do terminal.
2. Descobrir a raiz do projeto pela localizacao do script/modulo e resolver os
   arquivos internos relativamente a ela. Raiz de fontes externas, workspaces,
   toolchains, executaveis especiais, distribuicao/usuario WSL e identidades SSH
   devem vir de argumentos ou configuracao local explicita, ignorada pelo Git.
   Reutilizar loaders existentes e .env local; nao criar um sistema paralelo de
   configuracao nem guardar detalhes do host no perfil publico de hardware.
3. Precedencia: argumento explicito, configuracao local e, quando aplicavel,
   default portatil documentado. Variaveis de ambiente sao permitidas como entrada
   documentada, com precedencia definida. Configuracao explicita ausente/invalida
   deve produzir erro claro, sem fallback silencioso para o laboratorio antigo.
   Exemplos publicos devem usar placeholders ou paths relativos, sem chaves/dados
   privados. Preferir PATH para ferramentas comuns e permitir override explicito.
4. Converter paths Windows/WSL com mecanismos existentes, como wslpath, na fronteira
   apropriada; nao concatenar /mnt/c/Users/... nem presumir drive, distro ou usuario.
   Manter builds que exigem semantica Linux no filesystem Linux configurado.
5. Distinguir paths do host de paths de instalacao no telefone e interfaces Linux
   (/opt, /lib/firmware, /sys, /proc, /dev). Paths padronizados do alvo podem ser
   absolutos quando fazem parte do contrato de instalacao; documentar esse contrato.
   Fixtures sinteticas de paths invalidos/estrangeiros tambem nao sao defaults do host.
6. Preservar paths historicos em logs, manifestos e evidencias imutaveis. Nao fazer
   substituicao global nem alterar hashes/pins para esconder diferencas. Migrar
   consumidores ativos em passos pequenos, ao toca-los ou quando bloquearem o uso,
   sem desviar a entrega funcional para uma refatoracao geral de portabilidade.
7. Em caminhos de boot/flash/recuperacao, comparar arquivos resolvidos, hashes,
   argumentos e ordem das operacoes antes/depois da migracao. Resolver configuracao
   e validar destinos antes de transporte ou escrita. Preservar allowlists e recusas
   de path traversal; nao descobrir automaticamente backups/chaves por buscas amplas.
   Verificar a mudanca offline em raiz alternativa ou fixture temporaria quando
   afetar resolucao; esta regra nao autoriza operacoes fisicas nem novos testes amplos.

# Privacidade dos dados do ambiente de desenvolvimento

Atualizacao solicitada pelo usuario em 2026-10-29: a configuracao antes lida de
lab.json migra para .env na raiz do checkout, pelo loader existente. Argumento
CLI explicito prevalece. Nao executar .env como shell, interpolar valores ou
usar lab.json como fallback. O JSON antigo pode permanecer como backup privado,
nao como segunda fonte ativa. Paths no arquivo sao escolhas locais, nao defaults
publicos que presumem drive, usuario ou filesystem.

Instrucao do usuario, registrada em 2026-10-29.

1. Nao incorporar dados pessoais ou identificadores reais do ambiente em codigo,
   documentacao, exemplos, testes, nomes de artefatos ou metadados versionados.
   Inclui nome/login do usuario, email pessoal, hostname, paths da pasta pessoal,
   IPs da rede privada do laboratorio, SSIDs, MACs, numeros de serie do aparelho,
   identificadores de radio, tokens e credenciais. Ter acesso ao ambiente nao
   autoriza copiar esses dados para o projeto ou para servicos externos.
2. Exemplos e fixtures devem usar valores sinteticos, placeholders e paths
   relativos. Dados reais necessarios a execucao ficam em configuracao local
   ignorada pelo Git; segredos e chaves devem permanecer fora dos arquivos publicos.
   Reutilizar os mecanismos existentes, sem criar infraestrutura adicional so para
   cumprir esta regra. Nomes publicos de hardware/projetos e enderecos de rede
   padronizados do alvo nao sao dados pessoais por si mesmos.
3. Coletar e exibir somente o necessario ao diagnostico. Antes de incluir saidas
   em relatorios, commits ou compartilhamentos, remover identificadores pessoais
   e campos irrelevantes. Preferir trechos filtrados a dumps completos. Autorizacao
   para diagnosticar nao equivale a autorizacao para publicar ou transmitir dados.
4. Manter evidencias originais privadas intactas quando necessarias a integridade;
   produzir resumo sanitizado separado, com identificacao clara do que foi omitido.
   Nao reescrever logs/pins/hashes historicos silenciosamente. Se dados pessoais ja
   estiverem em arquivos publicos/versionados, apontar os locais e propor limpeza
   direcionada; nao apagar backups nem reescrever historico Git sem autorizacao.
5. Preservar creditos de autoria, copyright e avisos de licenca de terceiros.
   Nao confundir atribuicao legal/publica com detalhes pessoais do laboratorio.
   Nao alterar identidade Git global/local ou metadados de autoria automaticamente.

# Reaproveitamento dos projetos de porte no KPF

Instrucao do usuario, registrada em 2026-10-29.

1. KPF conserva seu nome e repositorio atuais. Cada porte tem Git independente
   dentro de ports/<aparelho>/, com LG K40S em ports/lg-k40s/. O Git do KPF ignora
   esses repositorios aninhados; nao usar submodules. Pode versionar ports/README.md
   com instrucoes. Nao copiar o toolkit: cada porte registra explicitamente a
   revisao/artefato do KPF usado e aceita raiz explicita fora de ports/ tambem.
   Configuracao .env, chaves e artefatos privados ficam ignorados pelo Git do porte.
2. Incorporar ao KPF o maximo de mecanismos criados nos portes que sejam uteis
   para proximos ports: parsers, verificadores, analises e operacoes reutilizaveis.
   Nao exigir segundo aparelho quando a utilidade e a fronteira forem claras.
3. Manter no porte os dados/politicas do aparelho: DT, enderecos, particoes,
   firmware requerido, limites eletricos, sequencias e recuperacao. Contratos
   de SoC/protocolo ficam identificados; MediaTek nao e Qualcomm generico.
4. Resolver a necessidade concreta, extrair o mecanismo comprovado, parametrizar
   as entradas e verificar equivalencia funcional e sob falha para o consumidor
   original. Nao criar framework universal antecipadamente nem bloquear os radios
   para terminar a generalizacao. Preferir frameworks/drivers upstream adequados
   quando a melhoria pertence a eles, nao necessariamente ao KPF.
5. Extrair incrementalmente, preservando fontes, licencas, pins e evidencias.
   Nenhuma dessas diretrizes autoriza operacao fisica ou publicacao de dados.

# Reutilizacao obrigatoria antes de implementar

Instrucao do usuario, registrada em 2026-10-25.

Antes de implementar novas ferramentas, drivers, modulos C ou diagnosticos:

1. Auditar alternativas no Linux mainline, postmarketOS, projetos MediaTek e
   Qualcomm e ferramentas abertas de engenharia reversa.
2. Comparar funcao, hardware, arquitetura, efeitos de probe/erro/remove,
   dependencias, licenca e versao. Existir um driver nao prova compatibilidade.
3. Preferir API/framework existente, DT e extensoes pequenas ao driver existente
   a implementacoes paralelas. Justificar por escrito qualquer codigo novo.
4. Registrar origem, revisao/commit, licenca por arquivo, limitacoes, esforco,
   parte realmente especifica de SoC/PMIC/placa e decisao na matriz
   `docs/open-source-reuse-audit.md` ou em auditoria vinculada a ela.
5. Nao substituir implementacao validada sem demonstrar equivalencia funcional,
   comportamento sob falha e preservacao dos mecanismos de recuperacao.
6. Manter separados core reutilizavel, backend de transporte/SoC e perfil da
   placa. Nao tratar BROM/DA MediaTek como protocolo Qualcomm generico.

A matriz inicial e uma triagem fundamentada, nao autorizacao de carga/flash.
Alternativas sem commit/licenca/compatibilidade confirmados continuam candidatas.
Nao iniciar testes fisicos so para completar uma auditoria de reutilizacao.
