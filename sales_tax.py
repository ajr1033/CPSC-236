SALES_TAX_RATE = 0.06  # 6% sales tax

def get_sales_tax(total):
    return round(total * SALES_TAX_RATE, 2)

def get_total_with_tax(total):
    return round(total + get_sales_tax(total), 2)