n = int(input())
eng_subs = set(map(int, input().split()))
m = int(input())
fr_subs = set(map(int, input().split()))

eng_only_subs = eng_subs - fr_subs
print(len(eng_only_subs))