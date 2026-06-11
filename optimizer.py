from ledger import balances

def optimize_settlement():
    debtors=[]
    creditors=[]

    for key, value in balances.items():
        if value < 0:
            debtors.append([key,value])
        elif value > 0:
            creditors.append([key,value])    

    creditors.sort(key= lambda person:person[1], reverse=True )   
    debtors.sort(key=lambda person:person[1]) 

    print("\n---Settlement Plan---")

    if not debtors and not creditors:
        print("Everyone is settled, no payment needed!")
        return

    i=0 ; j=0
    while i<len(debtors) and j<len(creditors):
        debtor_name,debt=debtors[i]   
        creditor_name,credit=creditors[j]
        settlement=min(abs(debt),credit)

        print(f"{debtor_name} pays {creditor_name} ${settlement:.2f}")
        debt+=settlement
        credit-=settlement

        debtors[i][1]=debt
        creditors[j][1]=credit 

        if abs(credit) < 0.01:
            j += 1

        if abs(debt) < 0.01:
            i += 1
