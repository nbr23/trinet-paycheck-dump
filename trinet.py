#! /usr/bin/env python3
 
import requests
import sys

EMPLOYEE_ID = ""
COMPANY_ID = ""
AUTH_COOKIE = ""

def getPaycheckList():
    cookies = dict(TriNetAuthCookie=AUTH_COOKIE)
    return requests.get(f"https://trinet.hrpassport.com/api-money/v1/payroll/{COMPANY_ID}/{EMPLOYEE_ID}/paychecks", cookies=cookies).json()["data"]["checkSummaries"]

def downloadPaycheck(paycheck, outdir="./paychecks"):
    url = f"https://trinet.hrpassport.com/api-money/v1/payroll/{COMPANY_ID}/{EMPLOYEE_ID}/paycheck-details-pdf/{paycheck['id']}"
    cookies = dict(TriNetAuthCookie=AUTH_COOKIE)
    r = requests.get(url, cookies=cookies)
    with open(f"{outdir}/{paycheck['id']}.pdf", "wb") as out:
        out.write(r.content)

def main():
    for check in getPaycheckList():
        print(f"{check['checkDt']} - {check['netPay']}")
        downloadPaycheck(check)

if __name__ == "__main__":
    sys.exit(main())