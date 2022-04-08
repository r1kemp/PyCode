
# copied from leetcode discussion
def coinChange(coins, amount: int) -> int:
	visited = 1 << amount                    # MSB = 1, rest all 0 as source = given amount
	count = 0
	while not (visited & 1):                 # Terminate when LSB becomes 1 i.e. 0 amount is left
		next_visited = visited               # Variable to explore next BFS level
		for coin in coins:
			next_visited |= visited >> coin  # If ith bit was set so far, we can reach i+coin
		if next_visited == visited:          # No new amount discovered. Dead end
			return -1
		count += 1
		visited = next_visited               # Update the visited set to next BFS level
	return count


coins = [2,4,5]
coins = [4,8,16]
print(coinChange(coins, 7))