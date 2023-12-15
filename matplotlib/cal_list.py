class Cal:

    # rate = 3.5  #年利率
    # years = 10  # 年限
    # total = 30  # 本金，以w为单位
    # type = "capital"  # 等额本金capital  等额本息 interest
    
    global repay_amount, interest_total, amount_list
    repay_amount = 0.00 # 还款总额
    interest_total = 0.00 # 还款总利息

    amount_list = []

    def cal_func(total, years = None, rate = None, loan_type = None):
        global repay_amount, interest_total, amount_list
        capital_month = 0.00 # 每月还款本金
        interest_month = 0.00 # 每月还款利息
        total_month = 0.00 # 每月还款总额
        rate = rate/100/12
        months = years * 12
        loan_total = total * 10000

        """
        等额本金：
            每月利息=（借款总额-已还本金）*月利率

            每月还款金额=每月还款本金+每月利息

        """
        if(loan_type == "capital"):
            # 每月还款本金
            capital_month = round(loan_total / months,2)

            for x in range(1,months + 1):
                # 每月利息
                interest_month = round((loan_total  - capital_month * (x-1)) * rate,2)
                # 每月本金
                total_month = interest_month + capital_month
                # 总利息 
                interest_total =  interest_total + interest_month

                # 填充amount_dict
                amount_dict = {}
                amount_dict["months"] = x
                amount_dict["capital_month"] = capital_month
                amount_dict["interest_month"] = interest_month
                amount_dict["total_month"] = total_month

                amount_list.append(amount_dict)               
                
            # 还款总额
            repay_amount = interest_total + loan_total
            # 返回amount_list
            return amount_list, interest_total, repay_amount


# 等额本息
            """
            等额本息：
             每月还款金额 = （贷款本金*月利率*(1+月利率)^贷款月数）/((1+月利率)^(还款月数-1))

             还款总利息=贷款金额*贷款月数*月利率*(1+月利率)^贷款月数/((1+月利率)^还款月数-1)-贷款金额

             每月还款利息(贷款本金*月利率-每月还款额)*(1+月利率）^1+每月还款额 

            """
        elif(loan_type == "interest"):
            # 每月还款金额 
            total_month = round((loan_total * rate * ((1 + rate)**months))/(((1 + rate))**months -1),2)
            # 还款总利息
            interest_total = round((loan_total * months *  rate * ((1 + rate)**months))/((1+rate)**months-1)-loan_total,2)
            
            for x in range(1, months + 1):
                # 每月还款利息
                interest_month = round((loan_total * rate-total_month) * (1 + rate)**(x-1) + total_month,2)
                # 每月还款本金
                capital_month = total_month - interest_month

                # 填充amount_dict
                amount_dict = {}
                amount_dict["months"] = x
                amount_dict["capital_month"] = capital_month
                amount_dict["interest_month"] = interest_month
                amount_dict["total_month"] = total_month

                amount_list.append(amount_dict)         

            #还款总金额
            repay_amount = interest_total + loan_total

            return amount_list, interest_total, repay_amount

        else:
            print("loan_type输入错误")
