#Convert Number to Thai Text.

def Number2ThaiSpeak(number):
    word = {'0':'ศูยน์','1':'หนึ่ง','2':'สอง','3':'สาม','4':'สี่','5':'ห้า','6':'หก','7':'เจ็ด','8':'แปด','9':'เก้า'}
    unit = ["","สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]
    
    if isinstance(number, str) == False:
        #ในกรณีที่ตัวแปรไม่ใช้ string จะแปลงเป็น string ก่อน
        number_str = str(number)
    else:
        number_str = number
        
    number_str_len = len(number_str) #หาจำนวนหลักของตัวเลข
    unit_cut = unit[:number_str_len][::-1] #ตัดเฉพาะหน่วยที่ต้องใช้และทำการ invert list
    output = "" #สร้างตัวแปรว่างๆ สำหรับเก็บคำอ่าน

    for i in range(0,number_str_len):
        #กรณีมากกว่าหลักสิบ
        if (number_str_len - i) > 2:
            #ถ้าเป็น 0 จะไม่อ่าน
            if  number_str[i] == '0':
                pass
            else:
                output += word[number_str[i]]
                output += unit_cut[i]

        #กรณีเป็นหลักสิบ
        elif (number_str_len - i) == 2:
            #ถ้าเป็น 0 จะไม่อ่าน
            if  number_str[i] == '0':
                pass
            #หลักสิบที่เป็น 1 จะไม่ใช้หนึ่งสิบแต่เป็น สิบตัวเดียว
            elif number_str[i] == '1':
                output += unit_cut[i]
            #หลักสิบที่เป็น 2 จะใช้ยี่แทน สอง จะได้เป็นยี่สิบ
            elif number_str[i] == '2':
                output += "ยี่" + unit_cut[i]
            #หลักสิบที่มากกว่า 2 จะใช้ตัวเลขนัั้นตามด้วยคำว่า สิบ
            else:
                output += word[number_str[i]] + unit_cut[i]
        #หลักหน่วย
        elif (number_str_len - i) == 1:
            #ถ้าหลักหน่วยจะอ่านเป็น เอ็ดก็ต่อเมื่อ ลงด้วย 1 และต้องเป็นตัวเลขสองตัวขึ้นไป
            if number_str[i] == '1' and number_str_len > 1:
                output += 'เอ็ด'

            #กรณีที่ตัวเลขไม่ใช้เลข 1 หรือมีตัวเลขแค่ 1 หลัก
            else:
                if number_str[i] == '0' and number_str_len > 1:
                    pass
                else:
                    output += word[number_str[i]]
    return output


number = input("Enter number : ")
thai_speak = Number2ThaiSpeak(number)
print(thai_speak)