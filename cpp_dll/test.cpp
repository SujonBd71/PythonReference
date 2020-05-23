#include "test.h"

#include <stdio.h>


DLLEXPORT int sum(int a, int b) {
	return a + b;
}

DLLEXPORT void sum_cb(int a , int b, callback_function cb)
{
	printf("in dll, sum: %d", a + b);

	if (cb)
		cb(a + b);
}
