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
print("\n--- LANÇAMENTO DE CARTÕES ---")
print("(Digite 'sair' na forma de pagamento para encerrar os cartões)")

while True:
    cartao = input("\nForma de pagamento (deb, cred, vr ou 'sair'): ").strip().lower()
    if cartao == 'sair':
        break
    if cartao not in ['deb', 'cred', 'vr']:
        print("Opção inválida. Digite deb, cred, vr ou sair.")
        continue
        
    bandeira = input("Digite a bandeira (Master, Visa, Elo, etc.): ").strip().upper() if cartao != 'vr' else 'VR'
    
    try:
        v_cart = float(input(f"Valor passado no {cartao.upper()} ({bandeira}): R$ "))
        total_cartoes += v_cart
        print(f"-> R$ {v_cart:.2f} adicionados ao total de cartões.")
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

print("\n" + "=" * 40)
print(f"        FECHAMENTO DE CAIXA ({data_atual})")
print("=" * 40)
print(f"Abertura de Caixa:      R$ {abertura:.2f}")
print(f"Total de Vendas:        R$ {vendas:.2f}")
print(f"(-) Total Sangrias:     R$ {total_sangrias:.2f}")
print("-" * 40)
print(f"SUBTOTAL:               R$ {subtotal:.2f}")
print(f"(-) Total em Cartões:   R$ {total_cartoes:.2f}")
print("=" * 40)
print(f"TOTAL EM CAIXA (DINHEIRO): R$ {total_caixa_dinheiro:.2f}")
print("=" * 40)