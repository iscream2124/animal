import random

def pick_student(max_num):
    """Return a random student number between 1 and max_num inclusive."""
    return random.randint(1, max_num)

if __name__ == "__main__":
    try:
        max_num = int(input("총 학생 수를 입력하세요: "))
        if max_num < 1:
            raise ValueError
    except ValueError:
        print("올바른 양의 정수를 입력하세요.")
    else:
        print(f"뽑힌 번호: {pick_student(max_num)}")
