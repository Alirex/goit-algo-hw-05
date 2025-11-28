# Порівняння

## З використанням `timeit`

### Результати

```text
search_i_text_i_boyer_moore: article_1.txt-existed_pattern - min: 0.02 ms, max: 0.04 ms, avg: 0.02 ms
search_i_text_i_boyer_moore: article_1.txt-not_existed_pattern - min: 0.04 ms, max: 0.07 ms, avg: 0.05 ms
search_i_text_i_boyer_moore: article_2.txt-existed_pattern - min: 0.05 ms, max: 0.08 ms, avg: 0.05 ms
search_i_text_i_boyer_moore: article_2.txt-not_existed_pattern - min: 0.07 ms, max: 0.09 ms, avg: 0.07 ms
search_i_text_i_kmp: article_1.txt-existed_pattern - min: 0.15 ms, max: 0.24 ms, avg: 0.15 ms
search_i_text_i_rabin_karp: article_1.txt-existed_pattern - min: 0.34 ms, max: 0.62 ms, avg: 0.36 ms
search_i_text_i_kmp: article_2.txt-existed_pattern - min: 0.41 ms, max: 0.47 ms, avg: 0.42 ms
search_i_text_i_kmp: article_1.txt-not_existed_pattern - min: 0.51 ms, max: 0.80 ms, avg: 0.52 ms
search_i_text_i_kmp: article_2.txt-not_existed_pattern - min: 0.73 ms, max: 1.11 ms, avg: 0.75 ms
search_i_text_i_rabin_karp: article_2.txt-existed_pattern - min: 0.92 ms, max: 1.35 ms, avg: 0.96 ms
search_i_text_i_rabin_karp: article_1.txt-not_existed_pattern - min: 1.16 ms, max: 2.03 ms, avg: 1.19 ms
search_i_text_i_rabin_karp: article_2.txt-not_existed_pattern - min: 1.64 ms, max: 2.03 ms, avg: 1.66 ms
```

### Висновки

Найшвидший алгоритм для кожного тексту і в цілому:

- Алгоритм Кнута-Морріса-Пратта
