import re


def str_sort(filtered_transactions: list[dict], word: str) -> list[dict]:
    found_operations = []
    for operation in filtered_transactions:
        if re.search(word, operation.get("description", "")):
            found_operations.append(operation)
            filtered_transactions = found_operations
        return filtered_transactions
