
import random
import time

# =====================================
# 폐쇄된 저택 : 마지막 밤
# =====================================

inventory = []
fear = 0
room = "hall"
game_running = True

def slow_print(text):
    print(text)
    time.sleep(0.5)

def show_inventory():
    print("\n[ 가방 속 물건 ]")
    if inventory:
        for item in inventory:
            print(" -", item)
    else:
        print("아직 아무것도 없습니다.")

def scare():
    global fear

    events = [
        "어디선가 발소리가 들립니다...",
        "뒤쪽에서 무언가 움직이는 소리가 납니다.",
        "갑자기 전등이 깜빡입니다.",
        "누군가 당신의 이름을 부르는 것 같습니다.",
        "문 너머에서 작은 노크 소리가 들립니다."
    ]

    if random.random() < 0.3:
        slow_print("\n[이상 현상]")
        slow_print(random.choice(events))
        fear += 1

def get_item(item):
    if item not in inventory:
        inventory.append(item)
        slow_print(f"\n[{item}]을(를) 획득했습니다!")

def game_start():
    global room

    print("=" * 40)
    print("       폐쇄된 저택 : 마지막 밤")
    print("=" * 40)

    slow_print("\n눈을 떠보니 낯선 저택 안입니다.")
    slow_print("밖으로 나가는 문은 굳게 잠겨 있습니다.")
    slow_print("당신은 저택을 조사하기 시작합니다.")
    slow_print("\n목표 : 단서를 찾아 저택에서 탈출하세요!")

    input("\n[Enter]를 눌러 시작하세요.")

def main():
    global room, fear, game_running

    game_start()

    while game_running:

        print("\n" + "=" * 40)

        if room == "hall":
            print("📍 현재 위치 : 저택 복도")
            print("희미한 조명 아래 여러 개의 문이 보입니다.")
            print("\n1. 서재로 이동")
            print("2. 부엌으로 이동")
            print("3. 침실로 이동")
            print("4. 현관으로 이동")
            print("5. 가방 확인")
            print("6. 게임 종료")

            choice = input("\n선택 : ")

            if choice == "1":
                room = "study"
                scare()
            elif choice == "2":
                room = "kitchen"
                scare()
            elif choice == "3":
                room = "bedroom"
                scare()
            elif choice == "4":
                room = "exit"
            elif choice == "5":
                show_inventory()
            elif choice == "6":
                print("게임을 종료합니다.")
                break
            else:
                print("잘못된 선택입니다.")

        elif room == "study":
            print("📍 현재 위치 : 서재")
            print("책들이 가득한 방입니다.")
            print("\n1. 책상 조사하기")
            print("2. 책장 조사하기")
            print("3. 복도로 돌아가기")

            choice = input("\n선택 : ")

            if choice == "1":
                if "비밀번호 메모" not in inventory:
                    slow_print("\n책상 위에서 낡은 메모를 발견했습니다.")
                    slow_print("메모에는 숫자가 적혀 있습니다.")
                    slow_print("현관 비밀번호 : 4271")
                    get_item("비밀번호 메모")
                else:
                    print("책상에는 더 이상 특별한 것이 없습니다.")

            elif choice == "2":
                slow_print("\n책장 사이에서 작은 열쇠를 발견했습니다.")
                get_item("저택 열쇠")

            elif choice == "3":
                room = "hall"

            else:
                print("잘못된 선택입니다.")

        elif room == "kitchen":
            print("📍 현재 위치 : 부엌")
            print("오래된 식탁과 찬장이 보입니다.")
            print("\n1. 찬장 열기")
            print("2. 식탁 조사하기")
            print("3. 복도로 돌아가기")

            choice = input("\n선택 : ")

            if choice == "1":
                if "전기 퓨즈" not in inventory:
                    slow_print("\n찬장 안에서 전기 퓨즈를 찾았습니다!")
                    get_item("전기 퓨즈")
                else:
                    print("찬장 안은 비어 있습니다.")

            elif choice == "2":
                slow_print("\n식탁에는 오래된 신문만 놓여 있습니다.")
                scare()

            elif choice == "3":
                room = "hall"

            else:
                print("잘못된 선택입니다.")

        elif room == "bedroom":
            print("📍 현재 위치 : 침실")
            print("침대와 커다란 거울이 놓여 있습니다.")
            print("\n1. 침대 조사하기")
            print("2. 거울 바라보기")
            print("3. 복도로 돌아가기")

            choice = input("\n선택 : ")

            if choice == "1":
                slow_print("\n베개 밑에서 오래된 일기를 발견했습니다.")
                get_item("오래된 일기")

            elif choice == "2":
                slow_print("\n거울 속에 당신의 모습이 비칩니다.")
                slow_print("그런데 잠깐, 뒤에 누군가 서 있는 것 같습니다...")
                scare()

            elif choice == "3":
                room = "hall"

            else:
                print("잘못된 선택입니다.")

        elif room == "exit":
            print("📍 현재 위치 : 저택 현관")
            print("거대한 철문이 앞을 가로막고 있습니다.")

            if "저택 열쇠" in inventory and "전기 퓨즈" in inventory:
                print("\n전원과 열쇠가 준비되었습니다.")
                print("비밀번호를 입력할 수 있습니다.")

                password = input("\n비밀번호 입력 : ")

                if password == "4271":
                    print("\n" + "=" * 40)
                    print("🎉 탈출 성공!")
                    print("=" * 40)

                    if fear >= 3:
                        slow_print("당신은 간신히 저택을 빠져나왔습니다.")
                        slow_print("하지만 그날 밤의 기억은 잊히지 않았습니다.")
                        print("\n[엔딩 : 아슬아슬한 탈출]")
                    else:
                        slow_print("당신은 무사히 저택을 빠져나왔습니다.")
                        slow_print("동이 트고, 긴 밤이 끝났습니다.")
                        print("\n[엔딩 : 완벽한 탈출]")

                    print(f"\n최종 공포 수치 : {fear}")
                    print("게임 클리어!")
                    break

                else:
                    slow_print("\n비밀번호가 틀렸습니다!")
                    slow_print("철문 너머에서 이상한 소리가 들립니다.")
                    fear += 1

            else:
                print("\n문이 잠겨 있습니다.")
                print("열쇠와 전기 퓨즈가 필요한 것 같습니다.")

            print("\n1. 복도로 돌아가기")
            choice = input("선택 : ")

            if choice == "1":
                room = "hall"

if __name__ == "__main__":
    main()
