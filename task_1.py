from trie import Trie

class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        if not isinstance(pattern, str):
            raise ValueError("Параметр має бути рядком")
        all_words = self.get_all_words()
        return sum(1 for word in all_words if word.endswith(pattern))

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise ValueError("Параметр має бути рядком")
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    print("=== Перевірка count_words_with_suffix ===")
    suffix_tests = [("e", 1), ("ion", 1), ("a", 1), ("at", 1), ("xyz", 0), (123, "ValueError")]

    for suffix, expected in suffix_tests:
        try:
            result = trie.count_words_with_suffix(suffix)
            print(f"Суфікс: '{suffix}' → Кількість слів: {result} ✔️" if result == expected else f"❌ Очікувалось: {expected}, Отримано: {result}")
        except Exception as e:
            print(f"Суфікс: '{suffix}' → Помилка: {type(e).__name__} ✔️" if expected == "ValueError" else f"❌ Неочікувана помилка: {e}")

    print("\n=== Перевірка has_prefix ===")
    prefix_tests = [("app", True), ("bat", False), ("ban", True), ("ca", True), ("", True), (None, "ValueError")]

    for prefix, expected in prefix_tests:
        try:
            result = trie.has_prefix(prefix)
            print(f"Префікс: '{prefix}' → Є слова: {result} ✔️" if result == expected else f"❌ Очікувалось: {expected}, Отримано: {result}")
        except Exception as e:
            print(f"Префікс: '{prefix}' → Помилка: {type(e).__name__} ✔️" if expected == "ValueError" else f"❌ Неочікувана помилка: {e}")

    print("\n✅ Усі перевірки для Завдання 1 завершено.")
