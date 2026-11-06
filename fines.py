from datetime import date

FINE_PER_DAY = 0.50


def calculate_fine(due_date, today=None):
    if today is None:
        today = date.today()

    if isinstance(due_date, str):
        due_date = date.fromisoformat(due_date)

    days_late = (today - due_date).days
    return max(0, days_late) * FINE_PER_DAY
