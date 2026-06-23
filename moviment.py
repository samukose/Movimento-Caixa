import os
import datetime

print("=" * 30)
print("   MOVIMENTO RESTAURANTE   ")
print("=" * 30)

while True:
    try:
        abertura = float(input("Quanto foi aberto o caixa? R$ "))
        vendas = float(input("Quanto foi o total de vendas do dia? R$ "))
        break
    except ValueError:
        print("Valor inválido! Por favor, digite apenas números.\n")

total_cartoes = 0.0

relatorio_maquinas = {
    'Rede': {},
    'Mercado Pago': {},
    'Infinite Pay': {}
}

print("\n--- LANÇAMENTO DE CARTÕES ---")
print("(Digite 'sair' na máquina de cartão para encerrar os cartões)")

while True:
    maquina_input = input("\nMáquina de cartão (Rede, Mercado Pago, Infinite Pay ou 'sair'): ").strip()
    
    if maquina_input.lower() == 'sair':
        break
        
    maquina = None
    if maquina_input.lower() == 'rede':
        maquina = 'Rede'
    elif maquina_input.lower() == 'mercado pago':
        maquina = 'Mercado Pago'
    elif maquina_input.lower() == 'infinite pay':
        maquina = 'Infinite Pay'
    else:
        print("Opção inválida. Digite Rede, Mercado Pago, Infinite Pay ou sair.")
        continue

    cartao = input("Forma de pagamento (deb, cred, vr, PIX ou 'sair'): ").strip().lower()
    if cartao == 'sair':
        break
    if cartao not in ['deb', 'cred', 'vr', 'pix']:
        print("Opção inválida. Digite deb, cred, vr, PIX ou sair.")
        continue
        
    bandeira = input("Digite a bandeira (Master, Visa, Elo, etc.): ").strip().upper() if cartao != 'vr' and cartao != 'pix' else 'VR'
    
    try:
        v_cart = float(input(f"Valor passado no {cartao.upper()} ({bandeira}) na {maquina}: R$ "))
        
        if cartao == 'vr':
            id_venda = "VR"
        elif cartao == 'pix':
            id_venda = "PIX"
        else:
            id_venda = f"{cartao.upper()} - {bandeira}"
            
        if id_venda in relatorio_maquinas[maquina]:
            relatorio_maquinas[maquina][id_venda] += v_cart
        else:
            relatorio_maquinas[maquina][id_venda] = v_cart
            
        total_cartoes += v_cart
        print(f"-> R$ {v_cart:.2f} adicionados à máquina {maquina}.")
    except ValueError:
        print("Valor inválido! Cartão não computado. Tente novamente.")

total_sangrias = 0.0
print("\n--- LANÇAMENTO DE SANGRIAS (SAÍDAS) ---")
print("(Digite 'sair' no motivo para encerrar as sangrias)")

while True:
    motivo = input("\nMotivo da sangria (padaria, quitanda, etc. ou 'sair'): ").strip()
    if motivo.lower() == 'sair':
        break
        
    try:
        v_sangria = float(input(f"Valor da sangria para '{motivo}': R$ "))
        total_sangrias += v_sangria
        print(f"-> R$ {v_sangria:.2f} subtraídos do caixa.")
    except ValueError:
        print("Valor inválido! Sangria não computada. Tente novamente.")

subtotal = abertura + vendas - total_sangrias
total_caixa_dinheiro = subtotal - total_cartoes

data_atual = datetime.datetime.now().strftime("%d/%m/%Y às %H:%M")

print("\n" + "=" * 45)
print(f"        FECHAMENTO DE CAIXA ({data_atual})")
print("=" * 45)

print("   DETALHAMENTO POR MÁQUINA DE CARTÃO")
print("-" * 45)
for maq, vendas_maq in relatorio_maquinas.items():
    print(f" Máquina: {maq}")
    if not vendas_maq:
        print("   (Nenhuma venda registrada nesta máquina)")
    else:
        subtotal_maq = 0.0
        for tipo, valor in vendas_maq.items():
            print(f"   > {tipo}: R$ {valor:.2f}")
            subtotal_maq += valor
        print(f"   * Total {maq}: R$ {subtotal_maq:.2f}")
    print("-" * 45)

print("\n" + "=" * 45)
print("               RESUMO GERAL")
print("=" * 45)
print(f"Abertura de Caixa:      R$ {abertura:.2f}")
print(f"Total de Vendas:        R$ {vendas:.2f}")
print(f"(-) Total Sangrias:     R$ {total_sangrias:.2f}")
print("-" * 45)
print(f"SUBTOTAL:               R$ {subtotal:.2f}")
print(f"(-) Total em Cartões:   R$ {total_cartoes:.2f}")
print("=" * 45)
print(f"TOTAL EM CAIXA (DINHEIRO): R$ {total_caixa_dinheiro:.2f}")
print("=" * 45)