import tkinter as tk
from tkinter import scrolledtext

class FinancialAlgorithms:
    @staticmethod
    def discounted_cash_flow(cash_flows, discount_rate):
        dcf = sum([cf / (1 + discount_rate) ** i for i, cf in enumerate(cash_flows)])
        return dcf

    @staticmethod
    def capm(expected_market_return, risk_free_rate, beta):
        return risk_free_rate + beta * (expected_market_return - risk_free_rate)

    @staticmethod
    def future_value(principal, rate, time):
        return principal * (1 + rate) ** time

    @staticmethod
    def amortization_schedule(principal, rate, periods):
        monthly_rate = rate / 12
        payment = principal * monthly_rate / (1 - (1 + monthly_rate) ** -periods)
        schedule = []
        for i in range(1, periods + 1):
            interest_payment = principal * monthly_rate
            principal_payment = payment - interest_payment
            principal -= principal_payment
            schedule.append((i, round(principal_payment, 2), round(interest_payment, 2), round(principal, 2)))
        return schedule

    @staticmethod
    def break_even_point(fixed_costs, variable_cost_per_unit, selling_price_per_unit):
        return fixed_costs / (selling_price_per_unit - variable_cost_per_unit)

    @staticmethod
    def gross_profit_margin(revenue, cost_of_goods_sold):
        return (revenue - cost_of_goods_sold) / revenue * 100

    @staticmethod
    def current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities

    @staticmethod
    def quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities

    @staticmethod
    def inventory_turnover_ratio(cost_of_goods_sold, average_inventory):
        return cost_of_goods_sold / average_inventory

    @staticmethod
    def dividend_yield(dividend_per_share, market_price_per_share):
        return (dividend_per_share / market_price_per_share) * 100

def main():
    fa = FinancialAlgorithms()
    results = []

    cash_flows = [100, 200, 300, 400]
    discount_rate = 0.1
    results.append(f"Discounted Cash Flow: {fa.discounted_cash_flow(cash_flows, discount_rate)}")

    expected_market_return = 0.08
    risk_free_rate = 0.03
    beta = 1.2
    results.append(f"CAPM Expected Return: {fa.capm(expected_market_return, risk_free_rate, beta)}")

    principal = 1000
    rate = 0.05
    time = 10
    results.append(f"Future Value: {fa.future_value(principal, rate, time)}")

    principal = 10000
    rate = 0.05
    periods = 24
    schedule = fa.amortization_schedule(principal, rate, periods)
    results.append("Amortization Schedule:")
    for payment in schedule:
        results.append(str(payment))

    fixed_costs = 5000
    variable_cost_per_unit = 10
    selling_price_per_unit = 20
    results.append(f"Break-Even Point: {fa.break_even_point(fixed_costs, variable_cost_per_unit, selling_price_per_unit)}")

    revenue = 20000
    cost_of_goods_sold = 12000
    results.append(f"Gross Profit Margin: {fa.gross_profit_margin(revenue, cost_of_goods_sold)}")

    current_assets = 15000
    current_liabilities = 5000
    results.append(f"Current Ratio: {fa.current_ratio(current_assets, current_liabilities)}")

    current_assets = 15000
    inventory = 5000
    current_liabilities = 5000
    results.append(f"Quick Ratio: {fa.quick_ratio(current_assets, inventory, current_liabilities)}")

    cost_of_goods_sold = 12000
    average_inventory = 3000
    results.append(f"Inventory Turnover Ratio: {fa.inventory_turnover_ratio(cost_of_goods_sold, average_inventory)}")

    dividend_per_share = 2
    market_price_per_share = 50
    results.append(f"Dividend Yield: {fa.dividend_yield(dividend_per_share, market_price_per_share)}")

    return results

def display_results():
    results = main()
    
    root = tk.Tk()
    root.title("Financial Algorithms Results")
    
    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=30)
    text_area.pack(padx=10, pady=10)
    
    for result in results:
        text_area.insert(tk.END, result + "\n")
    
    text_area.config(state=tk.DISABLED)
    
    root.mainloop()

if __name__ == "__main__":
    display_results()
