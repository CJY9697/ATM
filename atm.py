# balance : 통장에 들어있는 기본 금액을 담는 변수
# 1.입금, 2.출금, 3.영수증보기,4.종료 ==> 숫자로 원하는 기능을 입력
# 사용자가 입력한 기능은 num 변수에 달아주세요
# deposit_amount: 입금금액
# withdraw_amount: 출금금액 
# balance: 원금 
balance = 3000

while True:
    num =input("사용하실 기능의 번호를 입력해주세요.(1.입금, 2.출금, 3. 영수증보기, 4. 종료)")
    
    if num =="1":
        deposit_amount = input("입금할 금액을 입력해주세요. : ")
        if deposit_amount.isdigit() and int(deposit_amount) > 0:
            balance += int(deposit_amount)
            print(f'고객님의 입금 금액은 {deposit_amount}원이고, 현재 잔액은 {balance}원 입니다.')
        else:
            print("정신차리고,제대로된 숫자형태로 입금액을 작성해줘!")
    if num =="2":
        withdraw_amount = input("출금할 금액을 입력해주세요 :")
        if withdraw_amount.isdigit() and int(withdraw_amount) > 0 :
            withdraw_amount = min(balance, int(withdraw_amount))
            balance -= withdraw_amount
            print(f"고객님이 출금한 금액은 {withdraw_amount}원이고, 현재 잔액은 {balance}원 입니다.")
        else:
            print("정신차리고,제대로된 숫자형태로 입금액을 작성해줘!")
    if num =="3":
        pass
    if num =="4":
        print("서비스를 종료합니다.")
        break
