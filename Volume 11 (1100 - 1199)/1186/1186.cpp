#include <iostream>
#include <cstdio>

int main() {
    double a = 0.0, M[12][12];
    char T[2];
    int p = 11;
    scanf("%s", &T);
    for (int x = 0; x <= 11; x++)
        for (int y = 0; y <= 11; y++)
            scanf("%lf", &M[x][y]);

    for (int z = 1; z <= 11; z++) {
        for (int C = 11; C >= p; C--)
            a += M[z][C];
        p--;
    }
     
    if (T[0] == 'S')
        printf("%.1lf\n", a);
    else if (T[0] == 'M')
        printf("%.1lf\n", a/66.0);
}