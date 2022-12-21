#include <iostream>

static const int N = 100;

int quick_find()
{
    int i, p, q, id[N];
    for (i = 0; i < N; i++)
        id[i] = i;
    while (std::cin >> p >> q)
    {
        int t = id[p];
        if (t == id[q])
            continue;
        std::cout << "["
                  << "";
        for (i = 0; i < N; i++)
        {
            if (id[i] == t)
                id[i] = id[q];
            std::cout << id[i] << ", ";
        }
        std::cout << "]" << std::endl;
        std::cout << "( " << p << ", " << q << " )" << std::endl;
    }

    return 0;
}

int main()
{
    std::cout << "Enter two numbers: " << std::endl;
    quick_find();
    return 0;
}