import csv
import json
import re
from typing import Any, Dict, Hashable, List

import pandas as pd


# noinspection PyShadowingNames
def search_transactions(transactions: List[Dict[str, Any]], search_string: str) -> List[Dict[str, Any]]:
    """
    Ôóíêöèÿ äëÿ ïîèñêà áàíêîâñêèõ îïåðàöèé ïî îïèñàíèþ.

    :param transactions: Ñïèñîê ñëîâàðåé ñ äàííûìè î áàíêîâñêèõ îïåðàöèÿõ.
    :param search_string: Ñòðîêà äëÿ ïîèñêà â îïèñàíèè îïåðàöèé.
    :return: Ñïèñîê ñëîâàðåé, ó êîòîðûõ â îïèñàíèè åñòü äàííàÿ ñòðîêà.
    """
    # Êîìïèëèðóåì ðåãóëÿðíîå âûðàæåíèå äëÿ ïîèñêà
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)

    # Ôèëüòðóåì îïåðàöèè ïî îïèñàíèþ
    result = [transaction for transaction in transactions if pattern.search(transaction.get("description", ""))]

    return result


# Ïðèìåð èñïîëüçîâàíèÿ
transactions = [
    {"id": 1, "description": "Ïåðåâîä íà ñ÷åò", "amount": 100},
    {"id": 2, "description": "Îïëàòà çà óñëóãè", "amount": 200},
    {"id": 3, "description": "Ïåðåâîä ñðåäñòâ", "amount": 150},
    {"id": 4, "description": "Ïîêóïêà â ìàãàçèíå", "amount": 50},
]

search_string = "ïåðåâîä"
filtered_transactions = search_transactions(transactions, search_string)

print(filtered_transactions)


# noinspection PyShadowingNames
def count_transactions_by_category(transactions: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Ôóíêöèÿ äëÿ ïîäñ÷åòà êîëè÷åñòâà áàíêîâñêèõ îïåðàöèé ïî êàòåãîðèÿì.

    :param transactions: Ñïèñîê ñëîâàðåé ñ äàííûìè î áàíêîâñêèõ îïåðàöèÿõ.
    :param categories: Ñïèñîê êàòåãîðèé îïåðàöèé.
    :return: Ñëîâàðü ñ êàòåãîðèÿìè è êîëè÷åñòâîì îïåðàöèé â êàæäîé êàòåãîðèè.
    """
    # Èíèöèàëèçèðóåì ñëîâàðü äëÿ õðàíåíèÿ ðåçóëüòàòîâ
    category_count = {category: 0 for category in categories}

    # Ïîäñ÷èòûâàåì êîëè÷åñòâî îïåðàöèé äëÿ êàæäîé êàòåãîðèè
    for transaction in transactions:
        description = transaction.get("description", "")
        for category in categories:
            if category.lower() in description.lower():
                category_count[category] += 1

    return category_count


# Ïðèìåð èñïîëüçîâàíèÿ
transactions = [
    {"id": 1, "description": "Ïåðåâîä íà ñ÷åò", "amount": 100},
    {"id": 2, "description": "Îïëàòà çà óñëóãè", "amount": 200},
    {"id": 3, "description": "Ïåðåâîä ñðåäñòâ", "amount": 150},
    {"id": 4, "description": "Ïîêóïêà â ìàãàçèíå", "amount": 50},
    {"id": 5, "description": "Îïëàòà êîììóíàëüíûõ óñëóã", "amount": 75},
]

categories = ["ïåðåâîä", "îïëàòà", "ïîêóïêà"]
category_counts = count_transactions_by_category(transactions, categories)

print(category_counts)


# def load_transactions_from_json(file_path: pathlib.Path) -> List[Dict[str, Any]]:
#     with open(file_path, "r", encoding="utf-8") as file:
#         return json.load(file)
def load_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Çàãðóæàåò òðàíçàêöèè èç JSON-ôàéëà.
    Args:
        file_path: Ïóòü ê JSON-ôàéëó.
    Returns:
        Ñïèñîê ñëîâàðåé, ãäå êàæäûé ñëîâàðü ïðåäñòàâëÿåò òðàíçàêöèþ. Âîçâðàùàåò ïóñòîé ñïèñîê ïðè îøèáêå.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            # Ïðîâåðêà íà êîððåêòíîñòü äàííûõ: ïðåäïîëàãàåì, ÷òî äàííûå - ýòî ñïèñîê ñëîâàðåé
            if isinstance(data, list) and all(isinstance(item, dict) for item in data):
                return data
            else:
                print("Îøèáêà: JSON-ôàéë íå ñîäåðæèò ñïèñîê ñëîâàðåé.")
                return []
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Îøèáêà ïðè çàãðóçêå ôàéëà: {e}")
        return []


# def load_transactions_from_csv(file_path: pathlib.Path) -> List[Dict[str, Any]]:
#     with open(file_path, "r", encoding="utf-8") as file:
#         return list(csv.DictReader(file))


def load_transactions_from_csv(file_path: str) -> List[Dict[str, Any]]:
    """
    Çàãðóæàåò òðàíçàêöèè èç CSV-ôàéëà.

    Args:
        file_path: Ïóòü ê CSV-ôàéëó.

    Returns:
        Ñïèñîê ñëîâàðåé, ãäå êàæäûé ñëîâàðü ïðåäñòàâëÿåò òðàíçàêöèþ. Âîçâðàùàåò ïóñòîé ñïèñîê ïðè îøèáêå.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"Îøèáêà: Ôàéë {file_path} íå íàéäåí.")
        return []
    except csv.Error as e:
        print(f"Îøèáêà ïðè ÷òåíèè CSV-ôàéëà: {e}")
        return []


# def load_transactions_from_xlsx(file_path: pathlib.Path) -> List[Dict[str, Any]]:
#     return pd.read_excel(file_path).to_dict(orient="records")
def load_transactions_from_xlsx(file_path: str) -> List[Dict[Hashable, Any]]:
    """
    Çàãðóæàåò òðàíçàêöèè èç ôàéëà XLSX è âîçâðàùàåò èõ â âèäå ñïèñêà ñëîâàðåé.

    Args:
        file_path: Ïóòü ê ôàéëó XLSX.

    Returns:
     Ñïèñîê ñëîâàðåé, ãäå êàæäûé ñëîâàðü ïðåäñòàâëÿåò îäíó òðàíçàêöèþ. Âîçâðàùàåò ïóñòîé ñïèñîê, åñëè ïðîèçîøëà îøèáêà.
    """
    try:
        return pd.read_excel(file_path).to_dict(orient="records")
    except (FileNotFoundError, pd.errors.EmptyDataError, pd.errors.ParserError) as e:
        print(f"Îøèáêà ïðè çàãðóçêå ôàéëà: {e}")  # Áîëåå èíôîðìàòèâíîå ñîîáùåíèå îá îøèáêå
        return []


# noinspection PyShadowingNames
def filter_transactions(transactions: list[dict[str, Any]], status: str) -> List[Dict[str, Any]]:
    return [t for t in transactions if t["status"].lower() == status.lower()]


# noinspection PyShadowingNames
def sort_transactions(transactions: list[dict[str, Any]], ascending: bool) -> List[Dict[str, Any]]:
    return sorted(transactions, key=lambda x: x["date"], reverse=not ascending)
