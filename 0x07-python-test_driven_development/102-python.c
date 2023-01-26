#include "Python.h"

/**
 * print_python_string - prints a Python string.
 *
 * @p: PyObject pointing to a python string.
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t len;
	wchar_t *str;

	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	str = PyUnicode_AsWideCharString(p, &len);
	if (str == NULL)
		return;
	printf("  length: %zu\n", len);
	printf("  value: %ls\n", str);
	PyMem_Free(str);
}
