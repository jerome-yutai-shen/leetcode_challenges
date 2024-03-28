

class TrieNode {
    constructor(val, index) {
        this.val = val;
        this.index = index;
        this.left = null;
        this.right = null;
    }
}

function insert(root, string, idx) {
    let current_node = root;
    let output = idx;
    for (let char of string) {
        if (current_node.left && char === current_node.left.val) {
            current_node = current_node.left;
            output = current_node.index + 1;
            current_node.index = idx;
        } else if (current_node.right && char === current_node.right.val) {
            current_node = current_node.right;
            output = current_node.index + 1;
            current_node.index = idx;
        } else {
            let new_node = new TrieNode(char, idx);
            if (char === '0') {
                current_node.left = new_node;
                current_node = current_node.left;
            } else if (char === '1') {
                current_node.right = new_node;
                current_node = current_node.right;
            }
        }
    }
    return output;
}

function auto_complete_binary(commands) {
    let output = [];
    let root = new TrieNode('*', 0);
    for (let idx = 0; idx < commands.length; idx++) {
        let command = commands[idx];
        let index = insert(root, command, idx);
        output.push(index);
    }
    return output;
}


