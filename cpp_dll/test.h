//test.h
#define DLLEXPORT extern "C" __declspec(dllexport)
typedef void(*callback_function)(int);

DLLEXPORT int sum(int, int);
DLLEXPORT void sum_cb(int, int, callback_function cb);
