#include "advent-2022-day08.h"

#include <array>

constexpr auto total_visible{[]() constexpr{
    std::array<int, grid_size * grid_size> visible{};
    for (int flip = 0; flip <= 1; flip++) {
        for (int transpose = 0; transpose <= 1; transpose++) {
            for (int i = 0; i < grid_size; i++) {
                int max_x = -1;
                for (int j = 0; j < grid_size; j++) {
                    int col = flip ? grid_size - 1 - j : j;
                    int a = transpose ? col : i;
                    int b = transpose ? i : col;
                    int v = grid[a][b] > max_x;
                    max_x = v ? grid[a][b] : max_x;
                    visible[a * grid_size + b] |= v;
                }
            }
        }
    }
    int total = 0;
    for (int i = 0; i < grid_size * grid_size; i++)
    {
       total += visible[i];
    }
    return total;
}()};

template <int v>
struct TotalVisible;

TotalVisible<total_visible> result;

/*
* gcc -std=c++17 -c advent-2022-day08-part1.cpp
* advent-2022-day08.cpp:33:29: error: implicit instantiation of undefined template 'TotalVisible<1679>'
* TotalVisible<total_visible> result;
*
* advent-2022-day08.cpp:31:8: note: template is declared here
* struct TotalVisible;
*        ^
* 1 error generated.
*
*/