from airflow.utils.log.logging_mixin import LoggingMixin
import requests
import json
import time
import pandas_read_xml as pdx

def getJsonFromApiXml(url: str, user: str, password: str) -> str:
    """
    Do the request to API. 
    The response is a XML and will be converted to JSON.
    Args:
        url (str): API full URL.
        user (str): User to basic auth.
        password (str): Password to basic auth.
    Returns:
        str: Json from API XML response.
    """
    LoggingMixin().log.info(f"Request to: {safeUrl(url)}")
    for x in range(5):
        LoggingMixin().log.info(f'Request: attempt {x+1}')
        response = requests.get(f"{safeUrl(url)}", auth=(user, password))
        if(str(response.status_code)[0:1] == '2'):
            break
        time.sleep(60)
    if response:
        response_xml = pdx.read_xml(response.text)
        return response_xml.to_json(force_ascii=False)
    else:
        raise Exception("URL didn't return success in the http status")

def safeUrl(url: str, initial: bool = True) -> str:
    """
    Remove from URL any wrong slash concatenated.
    Args:
        url (str): Address to be formated - HTTP or File path.
        initial (str, optional): Flag to validate initial slashes. Defaults to True.
    Returns:
        str: safe URL
    """
    import re
    url = re.sub(r'([^:])/+', r'\1/', url)
    if initial:
        url = re.sub(r'^/{1,2}', '', url)
    return url

def getSlotsIntervals(groups: int = 2) -> list:
    """
    This method split the 24 hours in slots of intervals based in the number of the groups.
    Args:
        groups (int, optional): Define the number of time intervals. Defaults to 2.
    Returns:
        list: List of time intervals.
    """
    import math
    hours = 24
    if groups > hours or groups < 1:
        raise Exception(
            f'Number of groups must be less than {hours} and bigger than 0')
    base = math.floor(hours / groups)
    slots = []
    slotsRange = range(groups)
    for i in slotsRange:
        slotIni = base * i
        slotEnd = int(slotIni + base - 1)
        if i == max(slotsRange):
            slotEnd = slotEnd + (hours - slotEnd) - 1
        slot = [f'{str(slotIni).zfill(2)}00',
                f'{str(slotEnd).zfill(2)}59']
        slots.append(slot)
    return slots

def updateStringDate(date: str, pattern: str, days: int = 0, months: int = 0, years: int = 0, pattern_output: str = None) -> str:
    """
    Update the date in string format. 
    Allowing add or remove days, months or years.
    To add send a positive number, to remove a negative.
    It's also possivel to change the format.
    Args:
        date (str): Date as String.
        pattern (str): The pattern used in the String Date. Example "%Y/%m/%d".
        days (int, optional): Positive or negative number of days to be added or removed. Defaults to 0.
        months (int, optional): Positive or negative number of months to be added or removed. Defaults to 0.
        years (int, optional): Positive or negative number of years to be added or removed. Defaults to 0.
        pattern_output (str, optional): Output string date pattern. Defaults to None and will follow the same as input.
    Returns:
        str: Date updated and formatted as string.
    """
    from datetime import datetime, timedelta
    from dateutil.relativedelta import relativedelta

    if not pattern_output:
        pattern_output = pattern
    date_obj = datetime.strptime(date, pattern) + relativedelta(
        days=days) + relativedelta(months=months) + relativedelta(years=years)
    return date_obj.strftime(pattern_output)


def getDateIntervalList(date_initial: str, date_final: str, pattern: str, pattern_output: str = None, jump_days: int = 0, jump_months: int = 0) -> list:
    """
    Return a list of date between an initial and final date.
    By default the list increment 1 day per entry, but is possible create intervals using the jump attributes.
    Args:
        date_initial (str): Initial date.
        date_final (str): Final date.
        pattern (str): Pattern used in the initial and final date param.
        pattern_output (str, optional): Output string date pattern. Defaults to None and will follow the same as input.
        jump_days (int, optional): Days to jump between each entry. Defaults to 0.
        jump_months (int, optional): Months to jump between each entry. Defaults to 0.
    Returns:
        list: List of dates between the interval from the params.
    """
    from datetime import date, datetime, timedelta
    from dateutil.relativedelta import relativedelta
    if not pattern_output:
        pattern_output = pattern
    sdate = datetime.strptime(date_initial, pattern)
    edate = datetime.strptime(date_final, pattern)
    return [(sdate + relativedelta(days=x + jump_days) + relativedelta(months=jump_months)).strftime(pattern_output) for x in range((edate - sdate).days + 1)]