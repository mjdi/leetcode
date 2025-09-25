import os
from pathlib import Path

prob_nums_file = "lc75nums.txt"

base_path = Path.cwd()

def get_new_prob_nums():
    prob_nums = []  
    try:
        with open( base_path / prob_nums_file , "r") as file:
            while line:=file.readline(): 
                prob_nums.append(int(line))
    except FileNotFoundError:
        print(f"Error: The file '{prob_nums_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}") 
    # print(f'{prob_nums=}, length={len(prob_nums)}')

    curr_prob_dirs = []
    
    for item in os.listdir(base_path):
        #print(base_path / item)
        if Path.is_dir(base_path / item):
            if not item in ['__pycache__','dshelper']:
                curr_prob_dirs.append(int(item[1:])) # remove leading underscore

    # print(f'{curr_prob_dirs=}, length={len(curr_prob_dirs)}')

    new_prob_nums = set(prob_nums).difference(set(curr_prob_dirs))

    # print(f'{new_prob_nums=}, length={len(new_prob_nums)}')

    return new_prob_nums

def populate_tests_dir(num: int, prob_num_dir: Path):
    test_dir = prob_num_dir / 'tests'
    Path.mkdir(test_dir)
    with open(test_dir / '__init__.py', "w") as f:
        pass
    with open(test_dir / f'test_{str(num)}.py', "w") as f:
        f.write(f"""from leetcode75._{num}.solution import Solution as sol
                
class TestClass:
    def test_one(self):
        assert == sol.

    def test_two(self):
        assert == sol.

    def test_three(self):
        assert == sol.

""")

def write_solution_file(prob_num_dir):
    with open(prob_num_dir / 'solution.py', "w") as f:
        f.write(f"""from typing import Optional
                
class Solution:
    @staticmethod
    def () -> :
        return

""")

def make_prob_folder_skeleton(new_prob_nums):
    for n in new_prob_nums:
        dir_name = '_' + str(n)
        prob_num_dir = base_path / dir_name
        if not Path.exists(prob_num_dir):
            Path.mkdir(prob_num_dir)
            populate_tests_dir(n, prob_num_dir)
            with open(prob_num_dir / '__init__.py', "w") as f:
                pass
            write_solution_file(prob_num_dir)
    
def main():
    new_prob_nums = sorted(list(get_new_prob_nums()))
    # print(new_prob_nums)
    make_prob_folder_skeleton(new_prob_nums)

if __name__ == "__main__":
    main()    

            
            
            
            


















