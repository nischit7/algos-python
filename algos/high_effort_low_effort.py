import numpy as np

def high_low_effort_recursive(high: list, low: list, n: int):

    if n == 0:
        return 0

    day_index = 0
    low_int_task = low[day_index]
    high_int_task = high[day_index]

    # Calculate max when high task and low task is taken
    # Also calculate assuming no task is taken.
    max_amt = max(
                low_int_task + high_low_effort_recursive_from_that_day(
                    high=high,
                    low=low,
                    n=n,
                    day_index=day_index + 1,
                    previous_day_task_executed=True),
                high_int_task + high_low_effort_recursive_from_that_day(
                    high=high,
                    low=low,
                    n=n,
                    day_index=day_index + 1,
                    previous_day_task_executed=True),
                high_low_effort_recursive_from_that_day(
                    high=high,
                    low=low,
                    n=n,
                    day_index=day_index + 1,
                    previous_day_task_executed=False))

    print("day={day}, max_amt={max_amt}".format(day=day_index, max_amt=max_amt))
    return max_amt


def high_low_effort_recursive_from_that_day(
        high: list,
        low: list,
        n: int,
        day_index: int,
        previous_day_task_executed: bool) -> int:

    if day_index >= len(high):
        return 0

    low_int_task = low[day_index]
    high_int_task = high[day_index] if not previous_day_task_executed else 0

    max_amt = max(
        low_int_task + high_low_effort_recursive_from_that_day(
            high=high,
            low=low,
            n=n,
            day_index=day_index + 1,
            previous_day_task_executed=True),
        high_int_task + high_low_effort_recursive_from_that_day(
            high=high,
            low=low,
            n=n,
            day_index=day_index + 1,
            previous_day_task_executed=True),
        high_low_effort_recursive_from_that_day(
            high=high,
            low=low,
            n=n,
            day_index=day_index + 1,
            previous_day_task_executed=False))

    print("day={day}, low_int_task={low_int_task}, max_amt={max_amt}".format(day=day_index, low_int_task=low_int_task, max_amt=max_amt))

    return max_amt

def high_low_effort_recursive_dp(high: list, low: list, n: int):

    if n == 0:
        return 0

    day_index = 0
    low_int_task = low[day_index]
    high_int_task = high[day_index]

    dp = np.full(len(high), -1)
    # Calculate max when high task and low task is taken
    # Also calculate assuming no task is taken.
    max_amt = max(
        low_int_task + high_low_effort_recursive_from_that_day_dp(
            dp=dp,
            high=high,
            low=low,
            n=n,
            day_index=day_index + 1,
            previous_day_task_executed=True),
        high_int_task + high_low_effort_recursive_from_that_day_dp(
            dp=dp,
            high=high,
            low=low,
            n=n,
            day_index=day_index + 1,
            previous_day_task_executed=True),
        high_low_effort_recursive_from_that_day_dp(
            dp=dp,
            high=high,
            low=low,
            n=n,
            day_index=day_index + 1,
            previous_day_task_executed=False))

    dp[day_index] = max_amt
    print("day={day}, max_amt={max_amt}".format(day=day_index, max_amt=max_amt))
    return max_amt

def high_low_effort_recursive_from_that_day_dp(
        dp: np.ndarray,
        high: list,
        low: list,
        n: int,
        day_index: int,
        previous_day_task_executed: bool) -> int:

    if day_index >= len(high):
        return 0

    if dp[day_index] != -1:
        return dp[day_index]

    low_int_task = low[day_index]
    high_int_task = high[day_index] if not previous_day_task_executed else 0

    max_amt = max(
        low_int_task + high_low_effort_recursive_from_that_day_dp(
            dp=dp,
            high=high,
            low=low,
            n=n,
            day_index=day_index + 1,
            previous_day_task_executed=True),
        high_int_task + high_low_effort_recursive_from_that_day_dp(
            dp=dp,
            high=high,
            low=low,
            n=n,
            day_index=day_index + 1,
            previous_day_task_executed=True),
        high_low_effort_recursive_from_that_day_dp(
            dp=dp,
            high=high,
            low=low,
            n=n,
            day_index=day_index + 1,
            previous_day_task_executed=False))

    print("day={day}, low_int_task={low_int_task}, max_amt={max_amt}".format(day=day_index, low_int_task=low_int_task, max_amt=max_amt))

    dp[day_index] = max_amt

    return max_amt

def high_low_effort_using_just_dp(high: list, low: list, n: int):
    # An array task_dp that stores
    # the maximum task done
    task_dp = [0] * (n + 1)
    task_dp_high = [0] * (n + 1)
    task_dp_low = [0] * (n + 1)

    # If n = 0, no solution exists
    task_dp[0] = 0
    task_dp_high[0] = 0
    task_dp_low[0] = 0

    # If n = 1, high effort task
    # on that day will be the solution
    task_dp[1] = high[0]
    task_dp_high[1] = high[0]
    task_dp_low[1] = low[0]

    # Fill the entire array determining
    # which task to choose on day i
    for i in range(2, n + 1):
        task_dp_high[i] = high[i - 1] + task_dp[i - 2]
        task_dp_low[i] = low[i - 1] + task_dp[i - 1]
        task_dp[i] = max(high[i - 1] + task_dp[i - 2], low[i - 1] + task_dp[i - 1])

    return task_dp[n]