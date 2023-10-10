#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> n_array(n);

    for (int i = 0; i < n; i++) {
        std::cin >> n_array[i];
    }

    int m;
    std::cin >> m;
    std::vector<int> m_array(m);

    for (int i = 0; i < m; i++) {
        std::cin >> m_array[i];
    }

    int vasya = 0;
    int petya = 0;
    int i = 0;
    int j = 0;

    // Vasya
    while (i <= (m - 1)) {
        if (m_array[i] != n_array[j]) {
            vasya++;
            j++;
            continue;
        }
        if (m_array[i] == n_array[j]) {
            vasya++;
            i++;
            j = 0;
            continue;
        }
    }

    i = 0;
    j = (n - 1);

    // Petya
    while (i <= (m - 1)) {
        if (m_array[i] != n_array[j]) {
            petya++;
            j--;
            continue;
        }
        if (m_array[i] == n_array[j]) {
            petya++;
            i++;
            j = (n - 1);
            continue;
        }
    }

    std::cout << vasya << " " << petya << std::endl;

    return 0;
}
