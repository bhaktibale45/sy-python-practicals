def top_three_priciest(asset_costs):
    # Sort from highest to lowest
    sorted_costs = sorted(asset_costs, reverse=True)

    # Get the top three entries
    top_three = sorted_costs[:3]

    print("Top 3 priciest assets:")
    for i, cost in enumerate(top_three, start=1):
        print(f"{i}. ${cost:,.2f}")

    return top_three


# Example usage
asset_costs = [1250.75, 4999.99, 3200.50, 875.25, 7600.00, 2100.10]

top_three_priciest(asset_costs)