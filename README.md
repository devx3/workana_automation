Workana's Propose Sender v1.0
=====
Envio automático de proposta Workana
-----

Informações básicas para enviar a proposta:
- [ ] Login e Senha da conta
- [ ] Número máximo de propostas por dia (Acima desse número, o web crawler não envia mais propostas)
- [ ] Definir respostas para as perguntas padrões
- [ ] Definir Caminho para a proposta

Fluxo da aplicação
-----
- [ ] Abre Webbrowser
- [ ] Faz login na conta do Workana
- [ ] Verificar quantidade de propostas disponíveis na plataforma
- [ ] Faz o cálculo da quantidade de propostas que vai enviar por dia, de acordo com o que resta
- [ ] Acessa a página de projetos (Redação de Conteúdos)
- [ ] Faz o fetch em todos os projetos, de página em página e seleciona projetos adequados (Que contenham o script padrão do Alex Vargas) OBS: é importante que o crawler identifique se já mandou a proposta para aquele projeto. (Pode ser feito, analisando no banco de dados, ou, analisando se o botão de enviar mensagem mudou de cor)
- [ ] Acessa a página de cada projeto, clica no botão de enviar mensagem
- [ ] Preenche os campos padrões (se houver) e inseri a copy da proposta
- [ ] Faz o envio da proposta
- [ ] Repete o envio até chegar no limite do dia
- [ ] Encerra a aplicação

IMPORTANTE
----
A aplicação não pode ser simplesmente executada de uma vez, ela deve ser executada, 3 vezes ao dia (pelo menos), para que tenha uma boa variação e chance de pegar mais projetos.
É necessário que a aplicação gerencie em algum local, a quantidade de propostas que já foram enviadas naquele dia, e resete sempre no fim de cada dia.