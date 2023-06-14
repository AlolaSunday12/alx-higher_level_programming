<<<<<<< HEAD
#include <stdio.h>


/**

 * print_python_bytes - Prints bytes information

 *

 * @p: Python Object

 * Return: no return

 */

void print_python_bytes(PyObject *p)

{

        char *string;

        long int size, i, limit;


        printf("[.] bytes object info\n");

        if (!PyBytes_Check(p))

        {

                printf("  [ERROR] Invalid Bytes Object\n");

                return;

        }


        size = ((PyVarObject *)(p))->ob_size;

        string = ((PyBytesObject *)p)->ob_sval;


        printf("  size: %ld\n", size);

        printf("  trying string: %s\n", string);


        if (size >= 10)

                limit = 10;

        else

                limit = size + 1;


        printf("  first %ld bytes:", limit);


        for (i = 0; i < limit; i++)

                if (string[i] >= 0)

                        printf(" %02x", string[i]);

                else

                        printf(" %02x", 256 + string[i]);


        printf("\n");

}


/**

 * print_python_list - Prints list information

 *

 * @p: Python Object

 * Return: no return

 */

void print_python_list(PyObject *p)

{

        long int size, i;

        PyListObject *list;

        PyObject *obj;


        size = ((PyVarObject *)(p))->ob_size;

        list = (PyListObject *)p;


        printf("[*] Python list info\n");

        printf("[*] Size of the Python List = %ld\n", size);

        printf("[*] Allocated = %ld\n", list->allocated);


        for (i = 0; i < size; i++)

        {

                obj = ((PyListObject *)p)->ob_item[i];

                printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);

                if (PyBytes_Check(obj))

                        print_python_bytes(obj);

        }
=======
#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

/**
 * print_python - print python
 * @p: python object
 * Return: 0
 */
void print_python_bytes(PyObject *p)
{
        long int size;
        int i;
        char *trying_str = NULL;

        printf("[.] bytes object info\n");
        if (!PyBytes_Check(p))
        {
                printf("  [ERROR] Invalid Bytes Object\n");
                return;
        }
        PyBytes_AsStringAndSize(p, &trying_str, &size);

        printf("  size: %li\n", size);
        printf("  trying string: %s\n", trying_str);
        if (size < 10)
                printf("  first %li bytes:", size + 1);
        else
                printf("  first 10 bytes:");
        for (i = 0; i <= size && i < 10; i++)
                printf(" %02hhx", trying_str[i]);
        printf("\n");
}

/**
 * print_python - print python
 * @p: python object
 * Return: 0
 */
void print_python_list(PyObject *p)
{
        long int size = PyList_Size(p);
        int i;

        PyListObject *list = (PyListObject *)p;
        const char *type;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %li\n", size);
        printf("[*] Allocated = %li\n", list->allocated);
        for (i = 0; i < size; i++)
        {
                type = (list->ob_item[i])->ob_type->tp_name;
                printf("Element %i: %s\n", i, type);
                if (!strcmp(type, "bytes"))
                        print_python_bytes(list->ob_item[i]);
        }

>>>>>>> 8716950943eb581817c2312d1b7d99991e65c7a1
}
