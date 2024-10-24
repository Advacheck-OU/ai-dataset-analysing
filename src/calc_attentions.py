from collections import defaultdict
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import re
import os
from tqdm import tqdm
import torch
from transformers import LlamaTokenizer, LlamaForCausalLM
import pickle
import random
import json

def calc_top_three_column_values(attentions):
    values = calc_max_columnwise_attention_on_diagonal_for_hl(attentions)
    return sorted(np.partition(values, -3)[-3:], reverse=True)
    
def calc_mean_attention_on_diagonal_for_hl(attention_matrix):
    attention_values = []
    for i in range(1, attention_matrix.shape[1]):
        sum = 0
        for j in range (1, attention_matrix.shape[1]):
            if j > i:
                attention_values.append(sum)
                break
            if i - j < 2:
                sum += attention_matrix[i][j]
    return np.array(attention_values).mean()    
    
def calc_mean_attention_on_diagonal(attention_matrices):
    mean_attention = np.zeros((32, 32))
    for head in range (32):
        current_matrix = attention_matrices[head].cpu()
        for layer in range(32):
            mean_attention[head, layer] = calc_mean_attention_on_diagonal_for_hl(current_matrix[0, layer, :MAX_LEN, :MAX_LEN])
    return mean_attention

def calc_max_columnwise_attention_on_diagonal_for_hl(attention_matrix):
    attention_values = []
    for j in range (1, attention_matrix.shape[1]):
        attention_values.append(attention_matrix[j:,j].sum())
    return np.array(attention_values)     

def calc_max_columnwise_attention_on_diagonal(attention_matrices):
    mean_attention = np.zeros((32, 32))
    for head in range (32):
        current_matrix = attention_matrices[head].cpu()
        for layer in range(32):
            mean_attention[head, layer] = calc_max_columnwise_attention_on_diagonal_for_hl(current_matrix[0, layer, :MAX_LEN, :MAX_LEN]).max()
    return mean_attention

