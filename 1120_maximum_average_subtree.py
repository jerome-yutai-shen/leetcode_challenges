# -*- coding: utf-8 -*-
"""
Created on Jun 11 22:16:17 2022

@author: Jerome Yutai Shen

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    double max = 0;
    public double maximumAverageSubtree(TreeNode root) {
        dfs(root);
        return max;
    }
    class Item{
        int n;
        double sum;
        public Item(int n , double sum){
            this.n = n;
            this.sum = sum;
        }
    }
    public Item dfs(TreeNode root){
        if(root==null) return new Item(0,0.0);
        // now root is not null
        Item left = dfs(root.left);
        Item right =dfs(root.right);
        int totaln = left.n+right.n+1;
        double totalsum = left.sum+right.sum+root.val;
        double ave = totalsum/totaln;
        if(ave>max) max = ave;
        return new Item(totaln,totalsum);
    }
}

"""
from common_classes import BinaryTreeNode
from typing import List, Optional


class NewTreeNode:

	def __init__(self, num_children: int, node_value_sum: float):
		self.num_children = num_children 
		self.node_value_sum = node_value_sum

	def update(self, num_children: int, node_value_sum: float):
		self.num_children, self.node_value_sum = num_children, node_value_sum

        
class Solution:
    
    def __init__(self):
        self.max_value = 0.0 
        
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.dfs(root)
        return self.max_value
    
    def dfs(self, root_node: Optional[TreeNode]):
        if root_node is None:
            return NewTreeNode(0, 0.0)
        new_left = self.dfs(root_node.left)
        new_right = self.dfs(root_node.right)
        total_nodes = new_left.num_children + new_right.num_children + 1
        sum_children_values = new_left.node_value_sum + new_right.node_value_sum + root_node.val
        avg_value = sum_children_values / total_nodes
        if avg_value > self.max_value:
            self.max_value = avg_value
        return NewTreeNode(total_nodes, sum_children_values)        


"""
class Solution {
    double max = 0;
    public double maximumAverageSubtree(TreeNode root) {
        dfs(root);
        return max;
    }
    class Item{
        int n;
        double sum;
        public Item(int n , double sum){
            this.n = n;
            this.sum = sum;
        }
    }
    public Item dfs(TreeNode root){
        if(root==null) return new Item(0,0.0);
        // now root is not null
        Item left = dfs(root.left);
        Item right =dfs(root.right);
        int totaln = left.n+right.n+1;
        double totalsum = left.sum+right.sum+root.val;
        double ave = totalsum/totaln;
        if(ave>max) max = ave;
        return new Item(totaln,totalsum);
    }
}
"""