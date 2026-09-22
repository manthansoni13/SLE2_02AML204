# 8-Puzzle Performance Profiling: BFS vs. DFS

This repository contains the implementation, performance profiling, and flamegraph analysis for solving the 8-puzzle problem using **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**. 

The evaluation benchmarks algorithmic efficiency across execution time, frontier exploration, and CPU sampling metrics.

---

## 📌 Problem Overview

The 8-puzzle consists of a 3×3 grid with 8 numbered tiles and one empty space (`0`). The objective is to transition from a specified start configuration to the target goal configuration via sliding moves:

* **Start State:** `(1, 2, 3, 0, 4, 6, 7, 5, 8)`
* **Goal State:** `(1, 2, 3, 4, 5, 6, 7, 8, 0)`
* **Optimal Solution Depth:** 5 moves

---

## 📊 Benchmark Results

Benchmarked over multiple iterations using Python's standard `timeit` module:

| Metric | Breadth-First Search (BFS) | Depth-First Search (DFS) | Advantage / Finding |
| :--- | :--- | :--- | :--- |
| **Average Execution Time** | ~2.152 ms | ~32.418 ms | BFS is ~15× faster |
| **Nodes Expanded** | 74 nodes | 1280 nodes | BFS expands ~94% fewer states |
| **Solution Optimality** | Guaranteed Shortest Path (5 moves) | Non-optimal path | BFS guarantees minimum path depth |
| **Completeness** | Complete | Complete (with depth limit $d=15$) | DFS requires depth bounding to prevent runaway branches |

---

## 🛠 Repository Structure

```text
├── bfs_vs_dfs.py             # Primary benchmark script using timeit
├── profile_flamegraph.py     # Sampling harness for high-resolution profiling
├── flamegraph_bfs.svg        # Interactive CPU call-stack flamegraph for BFS
├── flamegraph_dfs.svg        # Interactive CPU call-stack flamegraph for DFS
├── .gitignore                # Excludes local artifacts and binary reports
└── README.md                 # Project documentation
```

---

## 🚀 Getting Started

### 1. Run Quantitative Benchmark (`timeit`)
To execute the automated benchmark script:

```bash
python bfs_vs_dfs.py
```

### 2. Generate Profiling Flamegraphs (`py-spy`)
Install the sampling profiler:

```bash
pip install py-spy
```

Run the profiling harness to record CPU call stacks into interactive SVG flamegraphs:

* **Generate BFS Flamegraph:**
  ```powershell
  py-spy record -o flamegraph_bfs.svg -- python profile_flamegraph.py bfs
  ```

* **Generate DFS Flamegraph:**
  ```powershell
  py-spy record -o flamegraph_dfs.svg -- python profile_flamegraph.py dfs
  ```

---

## 🔍 Flamegraph Inspection

The generated `.svg` files provide interactive stack trace visualizations:
* **Horizontal Axis:** Represents the proportion of total CPU runtime spent in each function.
* **Vertical Axis:** Represents the call stack depth (`run_workload` $\rightarrow$ search routine $\rightarrow$ `get_neighbors`).
* Open `flamegraph_bfs.svg` or `flamegraph_dfs.svg` in any standard web browser (Chrome, Edge, Firefox) to search, zoom, and inspect function bottlenecks.
