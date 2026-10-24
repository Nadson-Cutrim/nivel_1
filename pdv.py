# Array vazio para armazenar o histórico de compras
historico_compras = []

print("=== SISTEMA DE PDV COM DESCONTOS ===")
print("Digite 0 no valor da compra para encerrar a sessão.\n")

# Loop principal do PDV
while True:
    entrada_valor = input("Digite o valor da compra (R$): ")
    
    # Validação  para garantir que foi digitado um número antes de converter
    # Substitui a vírgula por ponto se o usuário digitar com vírgula
    entrada_valor_limpa = entrada_valor.replace(".", "").replace(",", "")
    if not entrada_valor_limpa.isdigit():
        print("⚠️  Entrada inválida! Por favor, digite um número válido.\n")
        continue

    valor_bruto = float(entrada_valor.replace(",", "."))
    
    # Condição de parada
    if valor_bruto == 0:
        break
    
    # Validação de valor negativo
    if valor_bruto < 0:
        print("⚠️  Aviso: O valor da compra não pode ser negativo. Tente novamente.\n")
        continue

    entrada_idade = input("Digite a idade do cliente: ")
    
    if not entrada_idade.isdigit():
        print("⚠️  Entrada inválida! Por favor, digite um número inteiro para a idade.\n")
        continue

    idade = int(entrada_idade)
    
    # Validação de idade negativa
    if idade < 0:
        print("⚠️  Aviso: A idade não pode ser negativa. Tente novamente.\n")
        continue

    # Regra 1: Desconto por idade (>= 65 anos -> 20%)
    valor_com_desconto_idade = valor_bruto
    if idade >= 65:
        valor_com_desconto_idade *= 0.80

    # Regra 2: Desconto por valor (> 100 reais após desc. de idade -> 10%)
    valor_final = valor_com_desconto_idade
    if valor_com_desconto_idade > 100:
        valor_final *= 0.90

    desconto_total_compra = valor_bruto - valor_final

    # Armazena na lista usando .append()
    historico_compras.append({
        "bruto": valor_bruto,
        "desconto": desconto_total_compra,
        "final": valor_final
    })

    print(f"✅ Valor final da compra: R$ {valor_final:.2f}")
    print(f"✅Desconto aplicado nesta compra: R$ {desconto_total_compra:.2f}\n")

# === RESUMO FINAL DO DIA ===
print("\n" + "=" * 35)
print("        RESUMO FINAL DO DIA        ")
print("=" * 35)

qtd_compras = len(historico_compras)

if qtd_compras == 0:
    print("Nenhuma compra registrada no sistema hoje.")
else:
    total_bruto = sum(compra["bruto"] for compra in historico_compras)
    total_descontos = sum(compra["desconto"] for compra in historico_compras)
    total_final = sum(compra["final"] for compra in historico_compras)

    print(f"Quantidade de compras registradas: {qtd_compras}")
    print(f"Total bruto (sem descontos):      R$ {total_bruto:.2f}")
    print(f"Total de descontos concedidos:   R$ {total_descontos:.2f}")
    print(f"Total final arrecadado:           R$ {total_final:.2f}")

print("=" * 35)