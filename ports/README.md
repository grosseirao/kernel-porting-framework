# Portes de dispositivos

Cada diretório `ports/<aparelho>/` é um repositório Git independente, ignorado
pelo KPF. Não são submodules: clonar o KPF não obtém os portes automaticamente.
O primeiro consumidor é `lg-k40s`. Seu índice Git já acompanha as fontes do
aparelho; o índice do KPF deixa de acompanhá-las. Originais legados continuam
preservados no disco e em área ignorada, sem serem fonte canônica do framework.
Nenhum commit ou remoto foi criado por esta migração.

A separação das fontes foi aceita offline: o índice do KPF exporta 107 arquivos
sem conteúdo do aparelho, enquanto o porte acompanha 1276 fontes. As mudanças
estão preparadas nos índices, sem commit/publicação. A migração de configuração
privada e a operação física não fazem parte desse aceite.

Obtenha o repositório do aparelho de uma origem revisada e clone-o em
`ports/<aparelho>/`, ou em qualquer diretório externo. Nenhuma URL/remoto é
presumida. O diretório do porte deve ter seu próprio `.git/` e `.gitignore`.
Não use `git add -f` no KPF para incluir o porte, credenciais ou artefatos.

## Responsabilidades

- KPF: `portkit`, mecanismos reutilizáveis, componentes compartilhados e testes
  genéricos. Melhorias úteis descobertas nos portes devem voltar ao framework.
- Porte: perfil, DT, integração kernel, patches e políticas do aparelho,
  initramfs, workflows, testes de integração, manifestos e documentação.
- Cada Git do porte também ignora `.env`, chaves, backups e artefatos privados.
  Configuração real não deve ser copiada de outro workspace automaticamente.

O porte registra explicitamente a revisão ou o hash do artefato KPF consumido.
Use o pacote no ambiente Python configurado, nunca uma cópia de `portkit` nem
busca implícita pelo diretório pai. APIs/CLIs do framework recebem a raiz absoluta
do porte; adaptadores locais resolvem seus próprios arquivos pela localização do
script. Configuração local utiliza o loader existente de `.env`.

Os testes independentes do toolkit vivem somente no KPF, em
`tools/tests/toolkit/`; o porte mantém seus testes de integração. O aceite de
uma mudança nos dois projetos inclui os testes afetados de ambos, sem copiar
a suíte do framework nem considerar classificação por AST como execução.

## Migração e aceite

Copiar e conferir antes de retirar originais. Preservar atribuições, alterações
locais, pins, evidências e recuperação. Componentes compartilhados não devem ser
transferidos definitivamente ao porte apenas por aparecerem em seu grafo de
dependências; cópias transitórias devem ser identificadas até resolver o consumo.

No K40S, catálogo/schemas, headers compartilhados e biblioteca já são consumidos
externamente: não existem `components/`, `kernel/components/` ou `portkit/` na
árvore de fontes do porte. Os workflows recebem `--components-root` explícito;
fixtures usam a raiz nomeada `kpf` no mapa de fontes de testes existente. O
README do porte descreve a seleção, sem paths pessoais ou busca do checkout pai.

Verificar offline a equivalência dos fluxos afetados e suas recusas, também com
o porte fora de `ports/`. Não alterar hashes históricos para esconder diferenças.
Esta organização não comprova funcionamento no aparelho nem autoriza operação
física, publicação, configuração de remotos ou instalação permanente.
