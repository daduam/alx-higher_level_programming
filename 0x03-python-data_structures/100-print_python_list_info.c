#include "Python.h"

/**
 * print_python_list_info - prints some basic info about Python lists.
 *
 * @p: pointer to PyObject representing Python list.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i;
	PyListObject *pl;

	if (!PyList_Check(p))
		return;
	pl = (PyListObject *)p;
	printf("[*] Size of the Python List = %zu\n", PyList_Size(p));
	printf("[*] Allocated = %zu\n", pl->allocated);
	for (i = 0; i < PyList_Size(p); i++)
		printf("Element %zu: %s\n", i, pl->ob_item[i]->ob_type->tp_name);
}
