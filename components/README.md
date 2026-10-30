# Componentes do Kernel Porting Framework

Este diretório contém definições e proveniência, não uma segunda árvore de
drivers. Metadados próprios são MIT; drivers e patches mantêm suas licenças.
O código reutilizado deve permanecer no subsistema Linux apropriado.

```
components/architectures/<arquitetura>/component.json
components/socs/<soc>/component.json
components/controllers/<ip>/component.json
components/pmics/<chip>/component.json
components/chargers/<chip>/component.json
components/touch/<chip>/component.json
boards/<placa>/components.json
```

Definições descrevem identidade, alternativas upstream fixadas por origem,
limitações e código legado ainda acoplado. Instâncias da placa referenciam essas
definições e declaram dependências, campos de conexão e nível de validação.
Dois controladores da mesma família usam uma definição e instâncias diferentes.

Consulta offline, no venv oficial:

```sh
python tools/kernel-workspace.py components --board k40s
```

A saída traz grafo ordenado, campos da placa, pendências, hashes dos inputs e
fingerprint do inventário. Ela **não** habilita driver, altera DT/Kconfig, muda
o plano de build, carrega módulos ou autoriza flash. Ordem de dependências não é
ordem de probe. O fingerprint do build antigo permanece separado e igual.

O índice público de evidências históricas também é referenciado e hasheado.
Isso preserva a proveniência das validações relatadas, sem reler dumps/logs
privados nem afirmar que o aparelho foi testado novamente nesta etapa.

Schema local é validado por jsonschema 4.26.0, já fixado no ambiente WSL/Linux.
Não há resolução de schemas remotos. Referências, ciclos, duplicatas, origem,
paths e campos sensíveis têm invariantes adicionais. Não se lê lab.json, firmware
ou backups para consultar o inventário público. Catálogo aponta para paths de
origem; não baixa nem executa fontes de terceiros.

## Regras de migração

- CPU/arquitetura não é o mesmo que suporte completo ao SoC.
- SoC/IP/chip não contém pinagem, calibração ou limites de uma placa particular.
- Áudio deve separar DAI/controlador, codec, amplificador e rotas da placa;
  Wi-Fi precisa de chip, transporte, firmware e calibração identificados.
- Identidade desconhecida fica em `unresolved` da placa. Não criar um driver
  genérico fictício nem copiar um compatible de outro chip.
- `legacy_sources` é somente índice do experimento antigo, **não** prova de
  independência da placa ou código pronto para upstream.
- Antes de mover código, separar dependências efetivas, manter oráculos/hashes
  e provar equivalência. Os paths antigos continuam válidos nesta etapa.
- `components.json` não substitui Device Tree/bindings, Kbuild, ASoC, IIO,
  regmap ou power_supply. Extensões seguem esses frameworks existentes.
- Recuperação/BROM/DA/EDL pertencem ao backend e políticas da placa, não ao driver
  de Wi-Fi, áudio ou PMIC. Nada é transferível automaticamente a outro aparelho.

O catálogo inicial tem seis definições e sete instâncias no K40S. É uma primeira
composição executável pelo host, não migração completa dos drivers C nem suporte
novo de hardware. A fixture de segunda placa nos testes é sintética: não houve
teste com outro smartphone.

Primeira extração real de C: `kernel/components/pmics/mt6357/mt6357-car-raw.h`
decodifica somente CAR bruto. A conversão calibrada fica em
`kernel/devices/lg-k40s/mt6357-car-units.h`, referenciada em `board_sources` da
instância PMIC. `reusable_sources` no componente registra o código do chip e
seus hashes; `board_sources` só pode apontar para a área da placa selecionada.
O builder candidato v3 usa a ponte nova. Fontes/artefatos v1 e o preparo físico
que os exige permanecem intactos; v2 intermediário também foi preservado.
