#include <Python.h>
/**
* print_python_string - Prints information about Python strings.
* @p: A PyObject string object.
*/
void print_python_string(PyObject *p)
{
Py_UNICODE *unicode;
Py_ssize_t length;

if (!PyUnicode_Check(p))
{
printf("[.] string object info\n");
printf("  [ERROR] Invalid String Object\n");
return;
}

if (PyUnicode_IS_COMPACT_ASCII(p))
{
printf("[.] string object info\n");
printf("  type: compact ascii\n");
printf("  length: %zd\n", PyUnicode_GET_LENGTH(p));
printf("  value: %s\n", PyUnicode_AsUTF8(p));
}
else
{
printf("[.] string object info\n");
printf("  type: compact unicode object\n");
printf("  length: %zd\n", PyUnicode_GET_LENGTH(p));
unicode = PyUnicode_AsUnicode(p);
if (unicode)
{
printf("  value: ");
for (length = 0; length < PyUnicode_GET_LENGTH(p); length++)
{
printf("%lc", unicode[length]);
}
printf("\n");
}
}
}
