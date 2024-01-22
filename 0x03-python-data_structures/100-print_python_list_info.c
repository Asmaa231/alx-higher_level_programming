#include <python.h>

/**
 *print_python_list_info -func prints some basic info about Python lists.
 *@p: A pyObject list
 *Return: void
 */
void print_python_list_info(PyObject *p)
{
	int i, alloc, size;
	pyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] size of the python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for(i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
