#include "advent-2022-day08.h"

#include <array>

constexpr auto highest_score{[]() constexpr{
    int max_score = -1;
    for (int start_row = 0; start_row < grid_size; start_row++) {
        for (int start_col = 0; start_col < grid_size; start_col++) {
            int score = 1;
            int start_x = grid[start_row][start_col];
            for (int col_inc = -1; col_inc <= 1; col_inc++) {
                for (int row_inc = -1; row_inc <= 1; row_inc++) {
                    if ((row_inc == col_inc) || (row_inc == -1*col_inc)) {
                        continue;
                    }
                    int direction_score = 0;
                    int row = start_row;
                    int col = start_col;
                    while (1) {
                        row += row_inc;
                        col += col_inc;
                        int inbounds = row >= 0 && row < grid_size && col >= 0 && col < grid_size;
                        if (!inbounds) {
                            break;
                        }
                        direction_score += 1;
                        if (grid[row][col] >= start_x) {
                            break;
                        }
                    }
                    score *= direction_score;
                }
            }
            if (score > max_score) {
                max_score = score;
            }
        }
    }
    return max_score;
}()};

template <int v>
struct HighestScore;

HighestScore<highest_score> result;


/*
* gcc -std=c++17 -c advent-2022-day08-part2.cpp -fconstexpr-steps=1500000
* advent-2022-day08-part2.cpp:45:29: error: implicit instantiation of undefined template 'HighestScore<536625>'
* HighestScore<highest_score> result;
*                             ^
* advent-2022-day08-part2.cpp:43:8: note: template is declared here
* struct HighestScore;
*        ^
* 1 error generated.
*/