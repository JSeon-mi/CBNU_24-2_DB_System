import pymysql

conn = pymysql.connect(host='192.168.56.109', port = 4567, user='root', password='1234', db='madang', charset='utf8')

def clear_screen():
    print("\033[H\033[J", end="") 

### 메인화면###
def main():
    while True:
        clear_screen()
        print("1. 전체 공용 물품 조회")
        print("2. 공용 물품 추가")
        print("3. 공용 물품 검색")
        print("4. 공용 물품 삭제")
        print("5. 종료")

        try:
            select = int(input("Select: "))
            if select == 1:
                view_com_goods()
            elif select == 2:
                create_com_goods()
            elif select == 3:
                search_com_goods()
            elif select == 4:
                delete_com_goods()
            elif select == 5:
                print("프로그램 종료")
                conn.close()
                break
            else:
                print("잘못된 입력입니다. 다시 시도하세요.")
                
        except ValueError:
            print("숫자를 입력하세요.")
        input("계속하려면 Enter를 누르세요.")

### 전체 공용 물품 조회 ### 
def view_com_goods():
    clear_screen()
    cur = conn.cursor()
    sql = "SELECT * FROM com_goods"
    cur.execute(sql)
    rows = cur.fetchall()
    print("공용 물품 목록:")
    print("-" * 30)
    for row in rows:
        print(f"이름: {row[0]}, 가격: {row[1]}, 수량: {row[2]}")
    print("-" * 30)
    cur.close()

### 공용 물품 추가 ### 
def create_com_goods():
    clear_screen()
    com_name = input("공용 물품 이름: ")
    com_price = input("공용 물품 가격: ")
    com_count = input("공용 물품 수량: ")
    cur = conn.cursor()
    sql = "INSERT INTO com_goods (com_name, com_price, com_count) VALUES (%s, %s, %s)"
    cur.execute(sql, (com_name, com_price, com_count))
    conn.commit()
    print("공용 물품이 추가되었습니다.")
    cur.close()

### 공용 물품 검색 ###
def search_com_goods():
    clear_screen()
    com_name = input("검색할 공용 물품 이름: ")
    cur = conn.cursor()
    sql = "SELECT * FROM com_goods WHERE com_name = %s"
    cur.execute(sql, (com_name,))
    rows = cur.fetchall()
    if rows:
        print("검색 결과:")
        print("-" * 30)
        for row in rows:
            print(f"이름: {row[0]}, 가격: {row[1]}, 수량: {row[2]}")
        print("-" * 30)
    else:
        print("해당 공용 물품이 없습니다.")
    cur.close()

### 공용 물품 삭제 ###
def delete_com_goods():
    clear_screen()
    com_name = input("삭제할 공용 물품 이름: ")
    cur = conn.cursor()
    sql = "DELETE FROM com_goods WHERE com_name = %s"
    cur.execute(sql, (com_name,))
    conn.commit()
    print("공용 물품이 삭제되었습니다.")
    cur.close()

### 프로그램 실행 ###
if __name__ == "__main__":
    main()
