# controle-de-pedidos
gerenciador de pedidos que controla quantidade de produtos a serem produzidos

## fetures:
- [ ] listagem e manutenção de cidade
  - [ ] para o cadastro da cidade, basta o nome
  - [ ] pode ser alterado ou excluído (caso não tenha clientes relacionados)
  - [ ] a listagem deve conter nome e quantidade de clientes cadastrados para aquela cidades
  - [ ] a listagem deve permitir filtrar por nome
- [ ] listagem e manutenção de clientes
  - [ ] para o cadastro de cliente, deve ter obrigatoriamente o nome e a cidade, e opcionalmente o telefone
  - [ ] pode ser alterado ou excluído (caso não tenha pedidos relacionados)
  - [ ] a listagem deve conter o nome, telefone (com link para o whatsapp), cidade e quantidade de pedidos relacionas àquele cliente
  - [ ] a listagem deve permitir filtrar por nome, cidade e telefone
- [ ] listagem e manutenção de produtos
  - [ ] para o cadastro dos produtos, deve ter obrigatóriamente o nome, preço e unidade de medida (kg ou lata)
  - [ ] pode ser alterado ou excluído (caso não tenha pedidos relacionados)
  - [ ] a listagem deve conter o nome do produto, unidade de medida, preço e quantidade já vendida (status do pedido = "entregue")
  - [ ] a listagem deve permitir filtrar por nome
- [ ] listagem e manutenção de pedidos
  - [ ] para o cadastro de pedidos, deve ser escolhido um cliente, 1 ou mais produtos e uma quantidade para cada produto, além da data e hora do pedido (por padrão data e hora atuais), e o pedido também terá um status, sendo "em produção", "feito" ou "entregue" (por padrão o primeiro)
  - [ ] pode ser visualizado, excluído ou alterado somente o status
  - [ ] a listagem deve trazer o nome do cliente, a cidade do cliente, a data e hora (ordenando por este, descrescente), o e o valor total dos produtos
  - [ ] a listagem deve filtrar por padrão por status = "em produção" e permitir filtrar pelo cliente, nome da cidade do cliente ou intervalo de datas
- [ ] relatório de produtos a serem produzidos
  - [ ] o relatório/listagem de pedidos a serem feitos deve agrupar os produtos dos pedidos com status "em produção" com fim de demonstrar quantos produtos devem ser feitos
  - [ ] este relatório pode ser filtrado por cidade, mostrando apenas pedidos de cidadde específicas
