package main

import "fmt"

type TrieNode struct {
    val   string
    index int
    left  *TrieNode
    right *TrieNode
}

func insert(root *TrieNode, str string, idx int) int {
    current_node := root
    output := idx
    for _, char := range str {
        if current_node.left != nil && string(char) == current_node.left.val {
            current_node = current_node.left
            output = current_node.index + 1
            current_node.index = idx
        } else if current_node.right != nil && string(char) == current_node.right.val {
            current_node = current_node.right
            output = current_node.index + 1
            current_node.index = idx
        } else {
            new_node := &TrieNode{val: string(char), index: idx}
            if string(char) == "0" {
                current_node.left = new_node
                current_node = current_node.left
            } else if string(char) == "1" {
                current_node.right = new_node
                current_node = current_node.right
            }
        }
    }
    return output
}

func auto_complete_binary(commands []string) []int {
    var output []int
    root := &TrieNode{val: "*", index: 0}
    for idx, command := range commands {
        index := insert(root, command, idx)
        output = append(output, index)
    }
    return output
}

func main() {
    commands := []string{"010", "011", "001", "100"}
    result := auto_complete_binary(commands)
    fmt.Println(result)
}





