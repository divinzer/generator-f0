# class House:
# 	def __init__(self, location, house_type, deal_type, price, completion_year):
# 		self.location = location
# 		self.house_type = house_type
# 		self.deal_type = deal_type
# 		self.price = price
# 		self.completion_year = completion_year
	
# 	def show_detail(self):
# 		print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

# houses = []
# house1 = House("강남", "아파트", "매매", "10억", "2010년")
# house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
# house3 = House("송파", "빌라", "월세", "500/50", "2008년")

# houses.append(house1)
# houses.append(house2)
# houses.append(house3)

# print("초 {0}대의 매물이 있습니다.".format(len(houses)))
# for house in houses:
# 	house.show_detail()

# try:
# 	print("나누기 전용 계산기입니다.")
# 	nums = []
# 	nums.append(int(input("첫 번째 숫자:")))
# 	nums.append(int(input("두 번째 숫자:")))
# 	nums.append(int(nums[0] / nums[1]))
# 	print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
# 	print("에러! 잘못된 값을 입력하였습니다.")

# except ZeroDivisionError as err:
# 	print(err)

# except Exception as err:
# 	print("알수 없는 에러가 발생하였습니다.")
# 	print(err)

# class BigNumberError(Exception):
# 	def __init__(self, msg):
# 			self.msg = msg
# 	def __str__(self):
# 		return self.msg

# try:
# 	print("한 자리 숫자 나누기 전용")
# 	num1 = int(input("첫 번째 숫자: "))
# 	num2 = int(input("두 번째 숫자: "))
# 	if num1 >= 10 or num2 >= 10:
# 		raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
# 	print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
# 	print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요.")
# except BigNumberError as err:
# 	print("에러가 발생하였습니다. 한자리 숫자만 입력하세요.")
# 	print(err)
# finally:
# 	print("계산기를 이용해 주셔서 감사합니다.")

# class SoldOutError(Exception):
# 	pass

# chicken = 10
# waiting = 1
# while(True):
# 	try:
# 		print("[남은 치킨 : {0}".format(chicken))
# 		order = int(input("치킨 몇 마리 주문하시겠습니까?"))
# 		if order > chicken:
# 			print("재료가 부족합니다.")
# 		elif order <= 0:
# 			raise ValueError
# 		else:
# 			print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
# 			waiting += 1
# 			chicken -= order

# 		if chicken == 0:
# 			raise SoldOutError
# 	except ValueError:
# 		print("잘못된 값을 입력하였습니다.")
# 	except SoldOutError:
# 		print("재고가 소진되었습니다.")
# 		break

def price(people):
	print("{0}명 가격은 {1}원입니다.".format(people, people * 10000))

def price_morning(people):
	print("{0}명 조조 할인 가격은 {1}원 입니다.".format(people, people * 6000))

def price_soldier(people):
	print("{0}명 군인 할인 가격은 {1}원 입니다.")