#include <cstdio>
#include <cstring>

unsigned char path[] = { 215, 237, 71, 194, 255, 229, 127, 88, 65, 122, 124, 120, 116, 223, 70, 81, 101, 54, 109, 2, 23, 190, 160, 162, 170, 139, 20, 178, 172, 196, 145, 132, 59, 11, 94, 53, 99, 127, 127, 116, 205, 81, 100, 107, 120, 72, 206, 107, 236, 232, 209, 91, 223, 64, 111, 101, 115, 56, 44, 129, 23, 143, 153, 27, 43, 17, 64, 123, 94, 64, 100, 228, 122, 117, 249, 245, 134, 226, 213, 110, 196, 64, 124, 84, 238 };
unsigned char key[] = { 148, 86, 103, 0, 178, 207, 221, 251, 163, 13, 52, 103, 50, 36, 99, 103, 173, 212, 251, 197, 179, 159, 58, 71, 54, 59, 126};

__attribute__((constructor))
static void f() 
{
    unsigned char k[] = { 148, 86, 103, 0, 178, 207, 221, 251, 163, 13, 55, 99, 63, 84, 76, 53, 173, 212, 232, 193, 237, 159, 17, 23, 120, 49, 126 };
    memcpy(key, k, sizeof(k));
}

int main()
{
    char buf[1024];
    printf("Input flag:");
    scanf("%99s", buf);
    if (strlen(buf) != 27)
    {
        printf("Wrong!\n");
        return 0;
    }
    unsigned char maze[27];
    for (int i = 0; i < 27; i++)
        maze[i] = ~(buf[i] ^ key[i]);
    int x = 0, y = 0;
    int check = 0;
    for (int i = 0; i < sizeof(path); i++)
    {
        check |= maze[x] & (1 << (7 - y));
        maze[x] |= 1 << (7 - y);
        switch (path[i] & (3 << 6))
        {
            case 3 << 6:
                y += 1;
                break;
            case 1 << 6:
                x += 1;
                break;
            case 2 << 6:
                x -= 1;
                break;
            default:
                y -= 1;
        }
    }
    maze[x] |= 1 << (7 - y);
    if (!check 
        && __builtin_popcountll(*(unsigned long long*)maze)
        + __builtin_popcountll(*(unsigned long long*)(maze + 8))
        + __builtin_popcountll(*(unsigned long long*)(maze + 16))
        + __builtin_popcount(*(unsigned short*)(maze + 24))
        + __builtin_popcount(maze[26]) == 8 * 27)
        printf("Right! flag is %s\n", buf);
    else
        printf("Wrong!\n");
    return 0;
}