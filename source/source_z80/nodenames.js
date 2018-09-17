var nodenames ={vss: 1,
vcc: 2,
clk: 3
a0: 5
a1: 6
a2: 7
a3: 8
a4: 9
a5: 10
a6: 11
a7: 12
a8: 13
a9: 14
a10: 15
a11: 16
a12: 17
a13: 18
a14: 19
a15: 20
_reset: 21
_wait: 22
_int: 23
_nmi: 24
_busrq: 25
_m1: 26
_rd: 27
_wr: 28
_mreq: 29
_iorq: 30
_rfsh: 31
d0: 32
d1: 33
d2: 34
d3: 35
d4: 36
d5: 37
d6: 38
d7: 39
_halt: 40
_busak: 41
t1: 1345,
t2: 1420,
t3: 256,
t4: 256,
t5: 440,
t6: 256,
m1: 2914,
m2: 260,
m3: 1361,
m4: 1361,
m5: 260,
m6: 1761,
reg_a0: 2271
reg_f0: 1854
reg_b0: 2268
reg_c0: 1851
reg_d0: 2264
reg_e0: 1847
reg_h0: 2266
reg_l0: 1849
reg_w0: 2260
reg_z0: 1843
reg_pch0: 2258
reg_pcl0: 1841
reg_sph0: 2261
reg_spl0: 1844
reg_ixh0: 2263
reg_ixl0: 1846
reg_iyh0: 2262
reg_iyl0: 1845
reg_i0: 2259
reg_r0: 1842
reg_aa0: 2270
reg_ff0: 1853
reg_bb0: 2269
reg_cc0: 1852
reg_dd0: 2265
reg_ee0: 1848
reg_hh0: 2267
reg_ll0: 1850
reg_a1: 2296
reg_f1: 1881
reg_b1: 2293
reg_c1: 1878
reg_d1: 2289
reg_e1: 1874
reg_h1: 2291
reg_l1: 1876
reg_w1: 2285
reg_z1: 1870
reg_pch1: 2283
reg_pcl1: 1868
reg_sph1: 2286
reg_spl1: 1871
reg_ixh1: 2288
reg_ixl1: 1873
reg_iyh1: 2287
reg_iyl1: 1872
reg_i1: 2284
reg_r1: 1869
reg_aa1: 2295
reg_ff1: 1880
reg_bb1: 2294
reg_cc1: 1879
reg_dd1: 2290
reg_ee1: 1875
reg_hh1: 2292
reg_ll1: 1877
reg_a2: 2384
reg_f2: 1958
reg_b2: 2381
reg_c2: 1955
reg_d2: 2377
reg_e2: 1951
reg_h2: 2379
reg_l2: 1953
reg_w2: 2373
reg_z2: 1947
reg_pch2: 2371
reg_pcl2: 1945
reg_sph2: 2374
reg_spl2: 1948
reg_ixh2: 2376
reg_ixl2: 1950
reg_iyh2: 2375
reg_iyl2: 1949
reg_i2: 2372
reg_r2: 1946
reg_aa2: 2383
reg_ff2: 1957
reg_bb2: 2382
reg_cc2: 1956
reg_dd2: 2378
reg_ee2: 1952
reg_hh2: 2380
reg_ll2: 1954
reg_a3: 2416
reg_f3: 1986
reg_b3: 2413
reg_c3: 1983
reg_d3: 2409
reg_e3: 1979
reg_h3: 2411
reg_l3: 1981
reg_w3: 2405
reg_z3: 1975
reg_pch3: 2403
reg_pcl3: 1973
reg_sph3: 2406
reg_spl3: 1976
reg_ixh3: 2408
reg_ixl3: 1978
reg_iyh3: 2407
reg_iyl3: 1977
reg_i3: 2404
reg_r3: 1974
reg_aa3: 2415
reg_ff3: 1985
reg_bb3: 2414
reg_cc3: 1984
reg_dd3: 2410
reg_ee3: 1980
reg_hh3: 2412
reg_ll3: 1982
reg_a4: 2489
reg_f4: 2058
reg_b4: 2486
reg_c4: 2055
reg_d4: 2482
reg_e4: 2051
reg_h4: 2484
reg_l4: 2053
reg_w4: 2478
reg_z4: 2047
reg_pch4: 2476
reg_pcl4: 2045
reg_sph4: 2479
reg_spl4: 2048
reg_ixh4: 2481
reg_ixl4: 2050
reg_iyh4: 2480
reg_iyl4: 2049
reg_i4: 2477
reg_r4: 2046
reg_aa4: 2488
reg_ff4: 2057
reg_bb4: 2487
reg_cc4: 2056
reg_dd4: 2483
reg_ee4: 2052
reg_hh4: 2485
reg_ll4: 2054
reg_a5: 2527
reg_f5: 2082
reg_b5: 2524
reg_c5: 2079
reg_d5: 2520
reg_e5: 2075
reg_h5: 2522
reg_l5: 2077
reg_w5: 2516
reg_z5: 2071
reg_pch5: 2514
reg_pcl5: 2069
reg_sph5: 2517
reg_spl5: 2072
reg_ixh5: 2519
reg_ixl5: 2074
reg_iyh5: 2518
reg_iyl5: 2073
reg_i5: 2515
reg_r5: 2070
reg_aa5: 2526
reg_ff5: 2081
reg_bb5: 2525
reg_cc5: 2080
reg_dd5: 2521
reg_ee5: 2076
reg_hh5: 2523
reg_ll5: 2078
reg_a6: 2610
reg_f6: 2155
reg_b6: 2607
reg_c6: 2152
reg_d6: 2603
reg_e6: 2148
reg_h6: 2605
reg_l6: 2150
reg_w6: 2599
reg_z6: 2144
reg_pch6: 2597
reg_pcl6: 2142
reg_sph6: 2600
reg_spl6: 2145
reg_ixh6: 2602
reg_ixl6: 2147
reg_iyh6: 2601
reg_iyl6: 2146
reg_i6: 2598
reg_r6: 2143
reg_aa6: 2609
reg_ff6: 2154
reg_bb6: 2608
reg_cc6: 2153
reg_dd6: 2604
reg_ee6: 2149
reg_hh6: 2606
reg_ll6: 2151
reg_a7: 2633
reg_f7: 2179
reg_b7: 2630
reg_c7: 2176
reg_d7: 2626
reg_e7: 2172
reg_h7: 2628
reg_l7: 2174
reg_w7: 2622
reg_z7: 2168
reg_pch7: 2620
reg_pcl7: 2166
reg_sph7: 2623
reg_spl7: 2169
reg_ixh7: 2625
reg_ixl7: 2171
reg_iyh7: 2624
reg_iyl7: 2170
reg_i7: 2621
reg_r7: 2167
reg_aa7: 2632
reg_ff7: 2178
reg_bb7: 2631
reg_cc7: 2177
reg_dd7: 2627
reg_ee7: 2173
reg_hh7: 2629
reg_ll7: 2175
}
