#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
#include <stdlib.h>
void print_python_list_info(PyObject *p)
{
        int i = 0;
        PyObject *iter;
        Py_ssize_t siz = PyList_Size(p);
        printf("[*] Size of the Python List = %d\n", (int)siz);
        printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);
        while (i < siz)
        {
                iter = PyList_GetItem(p, i);
                printf("Element %d: %s\n", i, Py_TYPE(iter)->tp_name);
                i++;
        }
}
