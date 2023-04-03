can_answer_list = {i:True for i in range(123, 1000) if len(str(i)) == len(set(str(i))) and '0' not in str(i)}


def compare_the_guessed_number_to_the_original_number_to_get_a_strike_and_a_ball(original_num, guess_num):
    strike, ball = 0, 0
    original_num, guess_num = str(original_num), str(guess_num)
    for i in range(3):
        for j in range(3):
            if original_num[i] == guess_num[j]:
                if i == j:
                    strike += 1
                else:
                    ball += 1
    return strike, ball


for _ in range(int(input())):
    guess, s, b = map(int, input().split())
    for can_answer in can_answer_list.keys():
        if (s, b) != compare_the_guessed_number_to_the_original_number_to_get_a_strike_and_a_ball(guess, can_answer):
            can_answer_list[can_answer] = False

answer = 0
for can_answer in can_answer_list.keys():
    if can_answer_list[can_answer]:
        answer += 1
print(answer)
