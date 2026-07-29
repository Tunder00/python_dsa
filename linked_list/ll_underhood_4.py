# below is the simmple example to make understand what will be happening inside linked list
head ={
    "value":11,
    "next":{
        "value":3,
        "next":{
            "value":23,
            "next":{
                "value":7,
                "next":{
                    "value":4,
                    "next": None
                }
            }
        }
    }
}
print(head['next']['next']['value'])

#  if this was a linked list
# print(my_linked_list.head.next.next.value)