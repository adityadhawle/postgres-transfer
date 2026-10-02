from .db import get_connection
def transfer(transfer_id, from_account, to_account, amount, fail_after_debit=False):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE accounts SET balance = balance - %s WHERE id = %s", (amount, from_account))
    conn.commit()
    if fail_after_debit:
        raise RuntimeError("simulated failure")
    cur.execute("UPDATE accounts SET balance = balance + %s WHERE id = %s", (amount, to_account))
    cur.execute("INSERT INTO transfers (transfer_id, from_account, to_account, amount, status) VALUES (%s, %s, %s, %s, %s)", (transfer_id, from_account, to_account, amount, "completed"))
    conn.commit()
    conn.close()
