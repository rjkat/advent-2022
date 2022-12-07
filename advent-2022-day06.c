#include <stdio.h>
#define HISTORY_LEN 14

int main() {
  char history[HISTORY_LEN];
  char ch;
  char n = 0;
  int i = 0;
  char started = 0;
  char found = 0;
  while ((ch = getchar()) != -1) {
    if (i >= HISTORY_LEN) {
        started = 1;
    }
    if (started) {
        char unique = 1;
        char m;
        char k;
        for (m = 0; m < HISTORY_LEN; m++) {
            for (k = 0; k < m; k++) {
                if (history[m] == history[k]) {
                    unique = 0;
                }
            }
        }
        if (unique) {
            found = 1;
        }
    }
    history[n] = ch;
    n++;
    n = (n == HISTORY_LEN) ? 0 : n;
    i += !found;
  }
  printf("%d\n", i);
  return 0;
}
