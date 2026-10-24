# Desafio trilha Back-end | Python
## PDV com Descontos Progressivos

## O que o código faz
O script `pdv.py` simula o funcionamento de um Ponto de Venda (PDV) com aplicação automática de regras de descontos progressivos em compras. O programa processa descontos com base na idade do cliente e no valor da compra, armazenando o histórico de cada transação para exibir um resumo financeiro ao final da sessão.

## Como ele faz
1. **Entrada de Dados e Validação**: Solicita o valor da compra (convertido para `float`) e a idade do cliente (convertida para `int`). Caso o usuário digite valores negativos, o programa exibe uma mensagem de aviso e solicita os dados novamente usando a instrução `continue`.
2. **Regra de Idade**: Se a idade informada for maior ou igual a 65 anos, aplica um desconto imediato de 20% sobre o valor bruto (`valor_bruto * 0.80`).
3. **Regra de Valor**: Verifica se o valor resultante após o desconto de idade é maior que R$ 100,00. Se for, aplica um desconto adicional de 10% sobre esse valor intermediário (`valor_intermediario * 0.90`).
4. **Armazenamento**: Adiciona cada compra em uma lista principal usando `.append()`, salvando os dados no formato `[valor_bruto, desconto_total, valor_final]`.
5. **Encerramento e Resumo**: O loop é interrompido quando o usuário digita `0` no valor da compra. Em seguida, um laço `for` percorre o histórico, soma os totais acumulados e exibe a quantidade de compras, total bruto, total de descontos e o valor final arrecadado.

## Como rodar
Certifique-se de ter o Python 3 instalado em sua máquina. No terminal, acesse a pasta `nivel_1` e execute:

```bash
python pdv.py

