#!/usr/bin/env python
# -*- coding:utf8 -*-
import os
import sys
import argparse

reload(sys)
sys.setdefaultencoding('utf8')


def getopts():
    parser = argparse.ArgumentParser(description='Mortgage')
    parser.add_argument('principal', type=int, help='*10K Yuan')
    parser.add_argument('annual_interest_rate', type=float, help='in percent')
    parser.add_argument('floating', type=float, help='base=1.0; up=1.1; down=0.9')
    parser.add_argument('years', type=int, help='30? 25? or else')
    return parser.parse_args()


def main():
    opts = getopts()
    principal = 10000 * opts.principal
    monthly_interest_rate = opts.floating * opts.annual_interest_rate / 100 / 12.0
    months = opts.years * 12
    monthly_repayment = principal * (monthly_interest_rate * (1 + monthly_interest_rate)**months) / ((1 + monthly_interest_rate)**months - 1)
    monthly_repayment = round(monthly_repayment, 2)
    total_repayment = monthly_repayment * months
    total_interest = total_repayment - principal
    monthly_income = round(monthly_repayment * 2.0, 2)
    annual_income = round(monthly_income * 12.0, 2)
    monthly_income_more = round(monthly_repayment * 2.1, 2)
    annual_income_more = round(monthly_income_more * 12.0, 2)

    print '''** 房贷计算器 **
贷款金额    {principal}万
年利率      {annual_interest_rate}%
利率浮动    {floating}倍
还款年限    {years}年

** 等额本息 **
月还款额    {monthly_repayment}元
总还款额    {total_repayment}元
总支付利息  {total_interest}元

** 收入证明：2倍月供 **
月收入      {monthly_income}元
年收入      {annual_income}元

** 收入证明：2.1倍月供 **
月收入      {monthly_income_more}元
年收入      {annual_income_more}元
'''.format(
        principal=opts.principal, annual_interest_rate=opts.annual_interest_rate, floating=opts.floating, years=opts.years, monthly_repayment=monthly_repayment, total_repayment=total_repayment, total_interest=total_interest, monthly_income=monthly_income, annual_income=annual_income, monthly_income_more=monthly_income_more, annual_income_more=annual_income_more)


if __name__ == '__main__':
    main()
