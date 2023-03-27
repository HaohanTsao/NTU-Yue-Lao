datasource = input("")
data1 = open(datasource, "r", encoding = "utf-8")

linecounter = -1  #行數計數器（用來避免讀到表頭）
datalist = []
for line in data1:
    linecounter += 1
    if linecounter >= 5 :#跳過我們自己填的4筆資料
        if len(line) >= 5 and line[0] == "2" and line[1] == "0" and line[2] == "2" and line[3] == "1" and line[4] == "/":
            datalist.append(line.split(","))

        else:
            datalist[-1][-1] = datalist[-1][-1] + line

datalist.reverse()
cleanlist = []
repeated_list = []
cleanlist.append(datalist[0])
for i in range(len(datalist)):
    if i >= 1:
        counter = -1
        for j in range(len(cleanlist)):
            if datalist[i][2].strip(' ') != cleanlist[j][2].strip(' '):
                counter += 1

                if counter == len(cleanlist) - 1:
                    cleanlist.append(datalist[i])
                    break

                continue   
            else:
                repeated_list.append([datalist[i][1].strip(' '), datalist[i][2].strip(' ')])
                break

print(f'刪去重複的電子郵件後，共{len(cleanlist)}筆資料。')
print(f'重複的資料共{len(repeated_list)}筆，為{repeated_list}\n\n')

from random import shuffle #打亂cleanlist內順序，使先填答的人不佔絕對優勢
shuffle(cleanlist)

bg_group = []
gb_group = []
gg_group = []
bb_group = []

for i in cleanlist:
    if i[3] == '生理男' and i[4] == '生理女':
        bg_group.append(i)
    elif i[3] == '生理女' and i[4] == '生理男':
        gb_group.append(i)
    elif i[3] == '生理女' and i[4] == '生理女':
        gg_group.append(i)
    elif i[3] == '生理男' and i[4] == '生理男':
        bb_group.append(i)

print(f'異性戀組{len(bg_group) + len(gb_group)}人，其中男生{len(bg_group)}人，女生{len(gb_group)}人。')
print(f'男同性戀組{len(bb_group)}人')
print(f'女同性戀組{len(gg_group)}人\n\n')

bg_couple = [] #裝男女配對結果
bg_left_couple = [] #裝男女配完剩下的男男配對結果
bb_couple = [] #裝男男配對結果
gg_couple = [] #裝女女配對結果
final_left = [] #裝各組最後剩下的人

def match(alist, blist, couplelist): #alist長度<=blist長度喔，異性戀配對alist放女blist放男，不然多出來的男生完全沒機會配到女生！
    for i in range(0, 151): #先挑出總差距為0的，直到150

        for j in range(len(alist)): #拿人數較少的alist去對blist的每個人，或同一list去對同一list的每個人
            for k in range(len(blist)):

                if blist[k] == "matched" or alist[j] =='matched': #如果alist或blist該項為“已配對”，跳過此次迴圈
                    continue
                elif alist[j][2] == blist[k][2]: #如果郵件相同表示配到自己（發生在bb_group配bb_group時），跳過迴圈
                    continue

                total_gap = 0
                for l in range(5, 30): #算出總差值
                    total_gap += abs(int(blist[k][l]) - int(alist[j][l]))

                if total_gap == i: #若總差值為0,1,...150，配對他們

                    couplelist.append([alist[j][1].strip(' '), alist[j][2].strip(' '), alist[j][3], alist[j][30], blist[k][1].strip(' '), blist[k][2].strip(' '), blist[k][3], blist[k][30], total_gap])
                    # [[暱稱, email, 性別, 問候語, 暱稱, email, 性別, 問候語], [暱稱, email, 性別, 問候語, 暱稱, email, 性別, 問候語]]
                    
                    alist[j] = "matched" #將該項顯示為“已配對“
                    blist[k] = "matched"
                    break #跳出此迴圈，不用再找了

                else:
                    continue

    if alist == blist: #若男同志配男同志、女同志配女同志、異性戀男配異性戀男，把組內剩下的人收集起來
        for i in alist:
            if i != 'matched':
                final_left.append([i[1].strip(' '), i[2].strip(' '), i[3], i[30]])

    return couplelist #這行可以不用啦，執行函數時就會永久整理到list

match(gb_group, bg_group, bg_couple)
match(bb_group, bb_group, bb_couple)
match(gg_group, gg_group, gg_couple)
match(bg_group, bg_group, bg_left_couple)

print(f'異性戀男女配對結果：共{len(bg_couple)}對。\n{bg_couple}\n\n')
print(f'同性戀男男配對結果：共{len(bb_couple)}對。\n{bb_couple}\n\n')
print(f'同性戀女女配對結果：共{len(gg_couple)}對。\n{gg_couple}\n\n')
print(f'異性戀剩餘男生配對結果：共{len(bg_left_couple)}對。\n{bg_left_couple}\n\n')
print(f'最後剩{len(final_left)}人未配對，其資料為{final_left}\n\n')

all_couple = bg_couple + bb_couple + gg_couple + bg_left_couple

couplelist1 = [] #因為gmail有寄信上限500封，故要把couplelist分裝，由不同人寄出，一人負責寄245對（490封）
couplelist2 = []
couplelist3 = []
couplelist4 = []
couplelist5 = []
couplelist6 = []
couplelist7 = [] #預計不超過1715對

for i in range(len(all_couple)):
    if i <= 244:
        couplelist1.append(all_couple[i])
    elif i <= 489:
        couplelist2.append(all_couple[i])
    elif i <= 734:
        couplelist3.append(all_couple[i])
    elif i <= 979:
        couplelist4.append(all_couple[i])
    elif i <= 1224:
        couplelist5.append(all_couple[i])
    elif i <= 1469:
        couplelist6.append(all_couple[i])
    else:
        couplelist7.append(all_couple[i])
 
print(f'已將配對組合分裝為{len(couplelist1)}+{len(couplelist2)}+{len(couplelist3)}+{len(couplelist4)}+{len(couplelist5)}+{len(couplelist6)}+{len(couplelist7)}對，並開始寄送。')

data1.close()

#開始寄信
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.mime.image import MIMEImage
from pathlib import Path
from email.mime.application import MIMEApplication 

sent_counter = 0 #計算已寄出多少信

def send_email(couplelist, email, password): 

    global sent_counter

    for couple in couplelist:
        #寄給配對甲方
        content = MIMEMultipart()  #建立MIMEMultipart物件
        content["subject"] = "[商管程式設計專案＿台大月老] 配對結果出爐囉！"
        content["from"] = email
        content["to"] = couple[1] #甲方收件者email

        content.attach(MIMEText(f'{couple[0]}您好，非常感謝您參與我們的專案，您的配對對象為 {couple[4]}（{couple[6]}）。\n對方的電子郵件： {couple[5]}\n對方留給您的問候語：\n{couple[7]}\n雙方平均每題差距：{(couple[8] / 25):.2f}格\n\n我們以戀愛取向為優先篩選條件，但因異性戀男女比不對稱，或同志組人數為奇數，若配對出與預期不符的對象，敬請見諒。\n若您有興趣瞭解我們的配對概況與機制，歡迎至交流版閱讀台大月老後續貼文，祝您聖誕佳節愉快！'))


        with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
            try:
                smtp.ehlo()  # 驗證SMTP伺服器
                smtp.starttls()  # 建立加密傳輸
                smtp.login(email, password)  # 登入寄件者gmail
                smtp.send_message(content)  # 寄送郵件
                print("成功傳送")
                sent_counter += 1

            except Exception as e:
                print("Error message:", e)
                print(f"未成功傳送至{couple[1]}")

        #寄給配對乙方
        content = MIMEMultipart()  #建立MIMEMultipart物件
        content["subject"] = "[商管程式設計專案＿台大月老] 配對結果出爐囉！"
        content["from"] = email
        content["to"] = couple[5] #乙方收件者email

        content.attach(MIMEText(f'{couple[4]}您好，非常感謝您參與我們的專案，您的配對對象為 {couple[0]}（{couple[2]}）。\n對方的電子郵件： {couple[1]}\n對方留給您的問候語：\n{couple[3]}\n雙方平均每題差距：{(couple[8] / 25):.2f}格\n\n我們以戀愛取向為優先篩選條件，但因異性戀男女比不對稱，或同志組人數為奇數，若配對出與預期不符的對象，敬請見諒。\n若您有興趣瞭解我們的配對概況與機制，歡迎至交流版閱讀台大月老後續貼文，祝您聖誕佳節愉快！'))


        with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
            try:
                smtp.ehlo()  # 驗證SMTP伺服器
                smtp.starttls()  # 建立加密傳輸
                smtp.login(email, password)  # 登入寄件者gmail
                smtp.send_message(content)  # 寄送郵件
                print("成功傳送")
                sent_counter += 1

            except Exception as e:
                print("Error message:", e)
                print(f"未成功傳送至{couple[5]}")


send_email(couplelist1, "寄件人1的email", "寄件人1的加密金鑰")
send_email(couplelist2, "寄件人2的email", "寄件人2的加密金鑰")
send_email(couplelist3, "寄件人3的email", "寄件人3的加密金鑰")
send_email(couplelist4, "寄件人4的email", "寄件人4的加密金鑰")
send_email(couplelist5, "寄件人5的email", "寄件人5的加密金鑰")
send_email(couplelist6, "寄件人6的email", "寄件人6的加密金鑰")
send_email(couplelist7, "寄件人7的email", "寄件人7的加密金鑰")

print(f'共成功寄出{sent_counter}封信')

