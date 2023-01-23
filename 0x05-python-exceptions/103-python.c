#include "Python.h"

/**
 * print_python_bytes - print some basic info about Python bytes
 *
 * @p: PyObject pointing to a PyBytesObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, nbytes;
	PyBytesObject *pb;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	pb = (PyBytesObject *)p;
	printf("  size: %zu\n", pb->ob_base.ob_size);
	printf("  trying string: %s\n", pb->ob_sval);
	nbytes = pb->ob_base.ob_size < 10 ? pb->ob_base.ob_size + 1 : 10;
	printf("  first %zu bytes:", nbytes);
	for (i = 0; i < nbytes; i++)
		printf(" %02x", pb->ob_sval[i] & 0xff);
	printf("\n");
}

/**
 * print_python_float - print some basic info about Python float
 *
 * @p: PyObject pointing to a PyFloatObject
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *pf;
	char *fval = NULL;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	pf = (PyFloatObject *)p;
	fval = PyOS_double_to_string(pf->ob_fval, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", fval);
	PyMem_Free(fval);
}

/**
 * print_python_list - print some basic info about Python lists
 *
 * @p: PyObject pointing to a PyListObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i;
	PyListObject *pl;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	pl = (PyListObject *)p;
	printf("[*] Size of the Python List = %zu\n", pl->ob_base.ob_size);
	printf("[*] Allocated = %zu\n", pl->allocated);
	for (i = 0; i < pl->ob_base.ob_size; i++)
	{
		printf("Element %zu: %s\n", i, pl->ob_item[i]->ob_type->tp_name);
		if (strcmp(pl->ob_item[i]->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(pl->ob_item[i]);
		else if (strcmp(pl->ob_item[i]->ob_type->tp_name, "float") == 0)
			print_python_float(pl->ob_item[i]);
	}
}
