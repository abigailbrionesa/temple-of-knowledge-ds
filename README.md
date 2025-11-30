<samp>

# Temple of Forgotten Knowledge

<p>
An adventure-themed **Python data structures project** that lets students manage relics and excavation tasks in a simulated temple environment.
This lab implements a <strong>Binary Search Tree (BST)</strong> to catalog relics and a <strong>Min-Heap</strong> to prioritize tasks, integrating object-oriented programming and algorithmic thinking.
</p>
˚　　　　✦　　　.　　. 🏺　 ˚　.　　　　 　　.　　　　　　 ✦　　　.　　˚　📜　　　　. ✦ 　🗝　　　　. ✦
　　.  　 　　　˚　　　　　*　　 　　✦　　　.　　.　　　✦　　˚ 　　　 　　˚　.　*　　. 　˚　　.

## Mission Overview

<p>
**Temple Management System** to help Indiana Jones and Professor Paleontologos catalog relics and manage excavation tasks.
The BST (Temple Archive) allows for quick searches and orderly storage of relics, while the min-heap (Excavation Queue) ensures that urgent tasks are completed first.
</p>

## 𝙵𝚎𝚊𝚝𝚞𝚛𝚎𝚜

<ul>
  <li>
    <strong>Temple Archive (BST)</strong><br>
    Insert, search, remove, and list relics by unique ID, maintaining BST properties.
  </li>
  <li>
    <strong>Excavation Queue (Min-Heap)</strong><br>
    Add tasks with priorities, peek at the most urgent, complete tasks, and list all tasks sorted by priority.
  </li>
  <li>
    <strong>Edge Case Handling</strong><br>
    Operations handle empty structures, duplicate IDs, and tie-breaking in priorities gracefully using assertions.
  </li>
  <li>
    <strong>Automated Testing</strong><br>
    `tests.py` validates all operations with normal and edge cases for both BST and Heap.
  </li>
</ul>

## D𝚎𝚖𝚘

<p>
🔗 Run the project locally:<br>
```bash
python lab9.py       # Demonstrates BST and Heap operations
python test.py       # Runs automated tests
