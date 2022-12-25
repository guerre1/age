dri = input('請問你有開過車嗎?')
if dri !='有' and dri != '沒有':
	print('只能輸入 有/沒有 哦')
	raise SystemExit
age = input('請問你的年齡?')
age = int(age)
if dri =='有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('奇怪，你不應該開過車')
elif dri == '沒有':
	if age >= 18:
		print('你可以去考駕照囉')
	else:
		print('很好，你再過幾年就可以考駕照囉')