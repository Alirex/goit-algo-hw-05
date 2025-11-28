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

## Benchmark

### Результати

```text
--------------------------------------------------------------------------------------------------------------------------- benchmark: 12 tests ---------------------------------------------------------------------------------------------------------------------------
Name (time in us)                                                                                Min                   Max                  Mean             StdDev                Median                IQR            Outliers          OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_search_text_benchmark[search_i_text_i_boyer_moore-article_1-existed-pattern]            20.0190 (1.0)         54.0390 (1.0)         20.4643 (1.0)       0.6719 (1.0)         20.3700 (1.0)       0.1300 (1.0)      829;1648  48,865.6502 (1.0)       31837           1
test_search_text_benchmark[search_i_text_i_boyer_moore-article_1-not-existed-pattern]        44.8500 (2.24)        65.9100 (1.22)        45.6429 (2.23)      0.7714 (1.15)        45.5090 (2.23)      0.1310 (1.01)     921;1226  21,909.2074 (0.45)      19088           1
test_search_text_benchmark[search_i_text_i_boyer_moore-article_2-existed-pattern]            48.7090 (2.43)       239.3570 (4.43)        49.6357 (2.43)      2.3341 (3.47)        49.2790 (2.42)      0.2100 (1.62)     697;1349  20,146.7944 (0.41)      17597           1
test_search_text_benchmark[search_i_text_i_boyer_moore-article_2-not-existed-pattern]        69.8990 (3.49)       168.2980 (3.11)        72.8481 (3.56)      2.7138 (4.04)        72.9990 (3.58)      1.7600 (13.54)     579;445  13,727.1904 (0.28)      13054           1
test_search_text_benchmark[search_i_text_i_kmp-article_1-existed-pattern]                   149.7380 (7.48)       238.9470 (4.42)       152.2040 (7.44)      2.5896 (3.85)       151.6080 (7.44)      0.8800 (6.77)      316;851   6,570.1287 (0.13)       6355           1
test_search_text_benchmark[search_i_text_i_rabin_karp-article_1-existed-pattern]            336.8760 (16.83)      753.4210 (13.94)      349.7573 (17.09)    14.7874 (22.01)      347.5650 (17.06)     4.4275 (34.06)      69;240   2,859.1256 (0.06)       2743           1
test_search_text_benchmark[search_i_text_i_kmp-article_2-existed-pattern]                   410.7850 (20.52)      598.5830 (11.08)      415.2463 (20.29)     4.2167 (6.28)       415.0250 (20.37)     2.6000 (20.00)       28;16   2,408.2091 (0.05)       2365           1
test_search_text_benchmark[search_i_text_i_kmp-article_1-not-existed-pattern]               511.0040 (25.53)      709.8110 (13.14)      518.0689 (25.32)     8.5205 (12.68)      516.3885 (25.35)     5.3555 (41.20)      125;86   1,930.2452 (0.04)       1924           1
test_search_text_benchmark[search_i_text_i_kmp-article_2-not-existed-pattern]               735.0110 (36.72)      787.3010 (14.57)      741.9987 (36.26)     2.6975 (4.01)       742.1810 (36.43)     3.1355 (24.12)      279;13   1,347.7112 (0.03)       1337           1
test_search_text_benchmark[search_i_text_i_rabin_karp-article_2-existed-pattern]            919.7780 (45.95)    1,487.3810 (27.52)      946.3000 (46.24)    24.9669 (37.16)      944.5280 (46.37)    11.7400 (90.32)       18;22   1,056.7473 (0.02)       1042           1
test_search_text_benchmark[search_i_text_i_rabin_karp-article_1-not-existed-pattern]      1,179.5250 (58.92)    1,344.8130 (24.89)    1,193.3161 (58.31)    10.0875 (15.01)    1,191.0250 (58.47)     9.9900 (76.86)      135;26     838.0009 (0.02)        850           1
test_search_text_benchmark[search_i_text_i_rabin_karp-article_2-not-existed-pattern]      1,646.8490 (82.26)    1,763.7980 (32.64)    1,671.2149 (81.67)    10.9358 (16.28)    1,673.1390 (82.14)    16.0490 (123.48)      192;4     598.3671 (0.01)        610           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

### Висновки

Найшвидший алгоритм для кожного тексту і в цілому:

- Алгоритм Кнута-Морріса-Пратта
