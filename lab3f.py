#!/usr/bin/env python3

#initial list
my_list = [1, 2, 3, 4, 5]

#function to add item to list 
#will append the next integer in this case max value + 1
def add_item_to_list(lst):
 lst.append(max(lst) +1)
 return lst


#function to remove the items from list
#function itereates over the items to remove and remove from each from lst
def remove_items_from_list(lst, items_to_remove):
 for items in items_to_remove:
  if items in lst:
   lst.remove(items)
 return lst

