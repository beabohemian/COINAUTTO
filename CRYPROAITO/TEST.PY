import pyupbit

access = "ytArGCBBC65TaHjAovI12mToXCV40yNc9tNTTzvx"          # 본인 값으로 변경
secret = "JY8Lfz0ONUFb7MqjBrH4ucpExL5B88Pp6oNSBeTg"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회