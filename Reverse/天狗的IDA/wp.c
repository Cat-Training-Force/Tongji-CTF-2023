#include<stdio.h>
#include<string.h>
#define makekey 0

int main(int argc, char* argv) 
{
	int i,flaglen;
#if makekey
	char flag[33] = "tjctf{I_kn0w_yOu_c@n_us4_1DApro}";
	flaglen = 32;
#else
	char flag[33] = { 0 };
	printf("Please input your flag(tjctf{}):\n");
	scanf("%32s", flag);
	flaglen = strlen(flag);
#endif
	int lun[32] = { 10, 22, 12, 9, 3, 20, 28, 11, 25, 6, 26, 29, 13, 27, 24, 14, 23, 31, 7, 5, 17, 1, 16, 18, 30, 4, 15, 8, 0, 2, 19, 21 };
	int tem = 0;
	char ch = 0;
	if (flaglen != 32) {
		printf("Wrong!\n");
	}
	else {
#if makekey
		ch = flag[0];
		while (lun[tem])
		{
			flag[tem] = flag[lun[tem]];
			tem = lun[tem];
		}
		flag[tem] = ch;
		printf("sec=%s\n", flag);

		int tem = 0, x = 1;
		char mid[75] = { 0 };

		mid[0] = flag[0];
		flag[0] = flag[28];

		while (lun[tem])
		{
			mid[x] = flag[lun[tem]];
			flag[lun[tem]] = mid[x - 1];
			tem = lun[tem];
			x++;
		}
		printf("flag=%s\n", flag);
#else

		ch = flag[0];
		while (lun[tem])
		{
			flag[tem] = flag[lun[tem]];
			tem = lun[tem];
		}
		flag[tem] = ch;

		if (!strncmp(flag, "0s_nt_pw1IDryA_O4}_{cj_@ofuktcnu", 32)) {
			printf("Right!\n");
		}
		else {
			printf("Wrong!\n");
		}
		
#endif // thisflag
	}
}
