from trie import Trie

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
            raise ValueError("Вхідні дані мають бути списком рядків")
        if not strings:
            return ""

        for word in strings:
            self.put(word)

        prefix = ""
        node = self.root

        while True:
            if len(node.children) != 1 or node.is_end_of_word:
                break
            char, next_node = next(iter(node.children.items()))
            prefix += char
            node = next_node

        return prefix


if __name__ == "__main__":
    print("=== Тести для find_longest_common_word ===")
    test_cases = [
        (["flower", "flow", "flight"], "fl"),
        (["interspecies", "interstellar", "interstate"], "inters"),
        (["dog", "racecar", "car"], ""),
        ([], ""),
        ("не список", "ValueError"),
        (["valid", 123], "ValueError"),
    ]

    for idx, (input_data, expected) in enumerate(test_cases, 1):
        try:
            trie = LongestCommonWord()
            result = trie.find_longest_common_word(input_data)
            print(f"Тест {idx}: Вхідні: {input_data} → Результат: '{result}' ✔️" if result == expected else f"❌ Тест {idx}: Очікувалось: '{expected}', Отримано: '{result}'")
        except Exception as e:
            print(f"Тест {idx}: Вхідні: {input_data} → Помилка: {type(e).__name__} ✔️" if expected == "ValueError" else f"❌ Тест {idx}: Неочікувана помилка: {e}")

    print("\n✅ Усі перевірки для Завдання 2 завершено.")
