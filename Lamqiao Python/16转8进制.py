n = int(input())
hex_nums = []
for i in range(n):
    hex_nums.append(input())

for hex_num in hex_nums:
  oct_num = oct(int(hex_num, 16))[2:]
  print(oct_num)
# n = int(input())
# hex_nums = [input() for i in range(n)]

# for hex_num in hex_nums:
#   oct_num = oct(int(hex_num, 16))[2:]
#   print(oct_num)
