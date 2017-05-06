#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <inttypes.h>
#include <math.h>

int main(int argc, char const *argv[])
{
	double x = 9.8654;
	int p=6;
	double q = x-(p*1.0);
	printf("%lf\n",q);
	return 0;
}