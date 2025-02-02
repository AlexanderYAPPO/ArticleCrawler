from typing import List, Dict, Any


def list_of_dicts_to_list_of_tsv(list_of_dicts: List[Dict[str, Any]]) -> List[str]:
    if not list_of_dicts:
        print("No data to print.")
        return []

    all_keys = set()
    for entry in list_of_dicts:
        all_keys.update(entry.keys())

    all_keys = sorted(all_keys)
    all_keys_str = ("\t".join(all_keys))

    entries = [all_keys_str]
    for entry in list_of_dicts:
        entries.append("\t".join(str(entry.get(key, "")) for key in all_keys))

    return entries