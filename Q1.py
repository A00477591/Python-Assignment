our_list = [1,2,3,4]


def stack(our_list, operation, new_element=None):
    if operation=="add":
        our_list.insert(0,new_element)
    elif operation=="remove":
        our_list.pop(0)
    else:
        our_list

def queue(our_list, operation, new_element=None):
    if operation=="add":
        our_list.append(new_element)
    elif operation=="remove":
        our_list.pop(0)
    else:
        our_list
    
def main():
    print("Initial List")
    print(our_list)
    print("Add to stack:")
    stack(our_list, "add", 0)
    print(our_list)
    print("Remove from stack:")
    stack(our_list, "remove")
    print(our_list)
    print("Add to queue:")
    queue(our_list, "add", 5)
    print(our_list)
    print("Remove from queue:")
    queue(our_list, "remove")
    print(our_list)
    


if __name__ == "__main__":
    main()