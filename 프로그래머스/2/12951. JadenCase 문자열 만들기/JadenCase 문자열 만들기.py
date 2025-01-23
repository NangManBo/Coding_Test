def solution(s):
    words = s.split(" ")
    answer = [word.capitalize() for word in words]

    return " ".join(answer)
