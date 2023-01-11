#include "Python.h"

/**
 * print_python_bytes - prints some basic info about Python bytes object.
 *
 * @p: pointer ot PyObject representing Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, count;
	PyBytesObject *pb;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	pb = (PyBytesObject *)p;
	printf("  size: %zu\n", PyBytes_Size(p));
	printf("  trying string: %s\n", pb->ob_sval);

	count = PyBytes_Size(p) < 10 ? PyBytes_Size(p) + 1 : 10;
	printf("  first %zu bytes:", count);
	for (i = 0; i < count; i++)
		printf(" %02x", pb->ob_sval[i]);
	printf("\n");
}

/**
 * print_python_list - prints some basic info about Python lists.
 *
 * @p: pointer to PyObject representing Python list.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i;
	PyListObject *pl;

	if (!PyList_Check(p))
		return;
	pl = (PyListObject *)p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zu\n", PyList_Size(p));
	printf("[*] Allocated = %zu\n", pl->allocated);
	for (i = 0; i < PyList_Size(p); i++)
	{
		printf("Element %zu: %s\n", i, pl->ob_item[i]->ob_type->tp_name);
		if (strcmp(pl->ob_item[i]->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(pl->ob_item[i]);
	}
}
