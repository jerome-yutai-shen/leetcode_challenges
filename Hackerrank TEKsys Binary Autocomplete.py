# -*- coding: utf-8 -*-
"""
Created on Jan 15 19:30:29 2024

@author: Jerome Yutai Shen

20240115 Jose Lopez 发来的题目
"""


class TrieNode:
    def __init__(self, val: str, index: int):
        self.val = val
        self.index = index
        self.left = None
        self.right = None


"""		
example of commands ['000', '1110', '01', '001', '110', '11'] will look like this:
             root
            /      \
	     '0'
	             
	             
	             
	             '1'
	     /\           \
        / '1'          '1'        
	  '0'              / \     				
      /  \           '0'   \ 
     /	 '1'			   '1'
   '0'					   /
   						 '0'	
"""


def insert(root, string, idx):
    current_node = root
    output = idx

    for char in string:
        if current_node.left and char == current_node.left.val:
            current_node = current_node.left
            output = current_node.index+1
            current_node.index = idx
        elif current_node.right and char == current_node.right.val:
            current_node = current_node.right
            output = current_node.index + 1
            current_node.index = idx
        else:
            new_node = TrieNode(char, idx)
            if char == '0':
                current_node.left = new_node
                current_node = current_node.left
            elif char == '1':
                current_node.right = new_node
                current_node = current_node.right
    return output



def auto_complete_binary(commands:list):
    output = []
    root = TrieNode('*', 0)
    for idx, command in enumerate(commands):
        index = insert(root, command, idx)
        output.append(index)
    return output