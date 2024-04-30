# controle-de-pedidos
gerenciador de pedidos que controla quantidade de produtos a serem produzidos

## features:
- [x] listagem e manutenção de cidade
  - [x] para o cadastro da cidade, basta o nome
  - [x] pode ser alterado ou excluído (caso não tenha clientes relacionados)
  - [x] a listagem deve conter nome e quantidade de clientes cadastrados para aquela cidades
  - [x] a listagem deve permitir filtrar por nome
- [x] listagem e manutenção de clientes
  - [x] para o cadastro de cliente, deve ter obrigatoriamente o nome e a cidade, e opcionalmente o telefone
  - [x] pode ser alterado ou excluído (caso não tenha pedidos relacionados)
  - [x] a listagem deve conter o nome, telefone (com link para o whatsapp), cidade e quantidade de pedidos relacionas àquele cliente
  - [x] a listagem deve permitir filtrar por nome e cidade
- [x] listagem e manutenção de produtos
  - [x] para o cadastro dos produtos, deve ter obrigatóriamente o nome, preço e unidade de medida (kg ou lata)
  - [x] pode ser alterado ou excluído (caso não tenha pedidos relacionados)
  - [x] a listagem deve conter o nome do produto, unidade de medida, preço e quantidade já vendida (status do pedido = "entregue")
  - [x] a listagem deve permitir filtrar por nome
- [x] listagem e manutenção de pedidos
  - [x] para o cadastro de pedidos, deve ser escolhido um cliente, 1 ou mais produtos e uma quantidade para cada produto, além da data e hora do pedido (por padrão data e hora atuais), e o pedido também terá um status, sendo "em produção", "feito" ou "entregue" (por padrão o primeiro)
  - [x] pode ser visualizado, excluído ou alterado somente o status
  - [x] a listagem deve trazer o nome do cliente, a cidade do cliente, a data e hora (ordenando por este, descrescente), o e o valor total dos produtos
  - [x] a listagem deve filtrar por padrão por status = "em produção" e permitir filtrar pelo cliente e nome da cidade do cliente
- [x] relatório de produtos a serem produzidos
  - [x] o relatório/listagem de pedidos a serem feitos deve agrupar os produtos dos pedidos com status "em produção" com fim de demonstrar quantos produtos devem ser feitos
  - [x] este relatório pode ser filtrado por cidade, mostrando apenas pedidos de cidadde específicas
