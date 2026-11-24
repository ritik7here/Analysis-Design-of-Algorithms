
# 0/1 Knapsack using Dynamic Programming

def knapsack(parcels, capacity):

    n = len(parcels)

    # Create DP table
    dp = [
        [0 for _ in range(capacity + 1)]
        for _ in range(n + 1)
    ]

    # Build DP table
    for i in range(1, n + 1):

        weight = parcels[i - 1]["weight"]
        value = parcels[i - 1]["value"]

        for w in range(capacity + 1):

            # Exclude current parcel
            dp[i][w] = dp[i - 1][w]

            # Include current parcel if it fits
            if weight <= w:

                include_value = (
                    value + dp[i - 1][w - weight]
                )

                dp[i][w] = max(
                    dp[i][w],
                    include_value
                )

    # Backtrack to find selected parcels
    selected_parcels = []

    w = capacity

    for i in range(n, 0, -1):

        if dp[i][w] != dp[i - 1][w]:

            parcel = parcels[i - 1]

            selected_parcels.append(parcel)

            w -= parcel["weight"]

    selected_parcels.reverse()

    return selected_parcels, dp[n][capacity], dp
