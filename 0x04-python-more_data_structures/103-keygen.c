#include "string.h"
#include "stdio.h"
#include "stdlib.h"
#include "time.h"

/**
 * f4 - f4
 *
 * @uname: char*
 * @len: int
 * Return: int
 */
int f4(char *uname, int len)
{
	int i, ch;

	ch = *uname;
	for (i = 0; i < len; ++i)
		if (uname[i] > ch)
			ch = uname[i];
	srand(ch ^ 14);
	return (rand() & 63);
}

/**
 * f5 - f5
 *
 * @uname: char*
 * @len: int
 * Return: int
 */
int f5(char *uname, int len)
{
	int i;
	char ch;

	ch = 0;
	for (i = 0; i < len; ++i)
		ch += uname[i] * uname[i];
	return ((ch ^ 239) & 63);
}

/**
 * f6 - f6
 *
 * @uname1: first char of username
 * Return: int
 */
int f6(char uname1)
{
	int i;
	char ch;

	ch = 0;
	for (i = 0; uname1 > i; ++i)
		ch = rand();
	return ((ch ^ 229) & 63);
}

/**
 * main - keygen for crackme5
 *
 * @argc: int
 * @argv: char**
 * Return: 0 on success
 */
int main(int argc, char **argv)
{
	int len, i, sum, prod;
	char *magic, key[7];

	magic = "A-CHRDw87lNS0E9B2TibgpnMVys5XzvtOGJcYLU+4mjW6fxqZeF3Qa1rPhdKIouk";
	key[6] = '\0';
	if (argc != 2)
		exit(1);
	len = strlen(argv[1]);

	key[0] = magic[(len ^ 59) & 63];

	for (i = 0, sum = 0; i < len; i++)
		sum += argv[1][i];
	key[1] = magic[(sum ^ 79) & 63];

	for (i = 0, prod = 1; i < len; i++)
		prod *= argv[1][i];
	key[2] = magic[(prod ^ 85) & 63];

	key[3] = magic[f4(argv[1], len)];

	key[4] = magic[f5(argv[1], len)];

	key[5] = magic[f6(*argv[1])];

	puts(key);
	return (0);
}
