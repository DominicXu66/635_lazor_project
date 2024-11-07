## 635_lazor_project


# Table of Contents
1. Project Overview
2. Usage
3. File Structure


# Project Overview
The Lazors Game Solver is a Python-based solution for the Lazors puzzle game. The objective of the Lazors game is to position blocks on a grid in such a way that laser paths intersect specified target points. This project automatically places the blocks on the board to achieve the objective.

# Usage
Prepare Input File:
Place a .bff file in the input directory. This file should define the grid, block types, lasers, and target points. 

Run the Solver:

import os

import sys

import glob

cd /PATH/TO/Lazor_Project

python run.py

Output:
The program will print the solution to the console and save it to an output file (e.g., solution.txt).

# File Structure
The main components of a .bff file are:

Grid Definition (GRID START / GRID STOP): Defines the layout of the grid.

x: Impassable cells.

o: Empty cells where blocks can be placed.

Blocks: Defines the available blocks.


A n: Reflective block with n available.

B n: Opaque block with n available.

C n: Refractive block with n available.


Lasers: Specifies initial laser positions and directions. Example:

L x y vx vy

where (x, y) is the position and (vx, vy) is the direction.


Targets: Points that each laser must intersect to solve the puzzle. Example:

P x y

where (x, y) is the position.
