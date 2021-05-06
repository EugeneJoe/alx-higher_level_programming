#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about python lists
 * @p: pointer to PyObject object/list
 *
 * Return: no return value (void)
 */
void print_python_list(PyObject *p)
{
        PyObject *obj;
        long int i = 0, len = 0;

        len = PyList_Size(p);
        if (PyList_Check(p))
        {
                printf("[*] Size of the Python List = %ld\n", len);
                printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
        }

        while (i < len)
        {
                obj = PyList_GET_ITEM(p, i);
                printf("Element %ld: %s\n", i, (((PyObject *)(obj))->ob_type)->tp_name);
                i++;
        }
}

void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");
	printf("  size: %ld\n", (((PyVarObject *)(p))->ob_size));
}
