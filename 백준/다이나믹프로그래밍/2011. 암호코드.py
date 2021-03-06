if __name__ == "__main__":
    N = input()
    if N[0] == '0':  # 맨 앞자리가 0이면 앞호 성립 불가능
        print(0)

    else:
        dp = [1, 1]  # 0자리수 경우의 수는 1, 1자리수 경우의 수는 2
        for i in range(1, len(N)):
            number = int(N[i - 1:i + 1])
            cnt = 0
            if int(N[i]):  # 0이 아닐 때
                cnt += dp[i]
            if 10 <= number <= 26: # 두자리수 암호일 때
                cnt += dp[i - 1]

            dp.append(cnt % 1000000)

        print(dp[-1])

    # 문제 해결 방법
    # 0자리 1자리 2자리 ... n자리까지 봤을 때 나올 수 있는 경우의 수를 구한다
    # 숫자가 0이 아니고 한자리수이면 ex) 01, 02 ... 경우는 어짜피 하나이므로 이전의 경우의 수와 같다
    # 숫자가 두자리일때(10과 26사이) 전전의 경우의 수와 같다
    # 두 경우의 숫자를 더해서 계속 쌓아주면된다.