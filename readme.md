# 🎯 Sudoku Game - Generator & Solver

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![Pygame](https://img.shields.io/badge/Pygame-2.1%2B-green.svg)](https://www.pygame.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A comprehensive Sudoku puzzle generator and solver with an interactive GUI. Features multiple difficulty levels and intelligent puzzle generation using advanced backtracking algorithms.

![Sudoku Game Screenshot](https://via.placeholder.com/600x400/000000/FFFFFF?text=Sudoku+Game+Screenshot)

## ✨ Features

- 🎲 **Smart Puzzle Generation**: Creates unique Sudoku puzzles with guaranteed single solutions
- 🧠 **Intelligent Solver**: Advanced backtracking algorithm that can solve any valid Sudoku
- 🎯 **4 Difficulty Levels**: Easy, Medium, Hard, and Insane challenges
- 💡 **Hint System**: Get hints when you're stuck - the AI will fill in the next logical move
- 🎮 **Interactive GUI**: Beautiful Pygame-based interface with mouse and keyboard controls
- ⚡ **Auto-Solver**: Watch the AI solve puzzles step-by-step with visual feedback
- 🎨 **Clean Interface**: Intuitive design with color-coded feedback and timing

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/sudoku-game.git
   cd sudoku-game
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the game**
   ```bash
   python main.py
   ```

## 🎮 How to Play

1. **Launch the game** - Run `python main.py`
2. **Select difficulty** - Choose from Easy, Medium, Hard, or Insane
3. **Play the puzzle**:
   - Click on a cell to select it
   - Type numbers 1-9 to enter values
   - Press `Enter` to confirm your entry
   - Press `Delete` to clear a cell
   - Press `H` for a hint
   - Press `Space` to auto-solve the puzzle

### Controls

| Key      | Action        |
| -------- | ------------- |
| `1-9`    | Enter number  |
| `Enter`  | Confirm entry |
| `Delete` | Clear cell    |
| `H`      | Get hint      |
| `Space`  | Auto-solve    |
| `Mouse`  | Select cells  |

## 🧮 Algorithm & Technical Details

### Core Algorithm

The Sudoku generator uses an advanced **backtracking algorithm** with the following features:

- **Unique Solution Guarantee**: Every generated puzzle has exactly one valid solution
- **Difficulty Assessment**: Based on the number of logical guesses required during solving
- **Constraint Propagation**: Efficiently eliminates impossible values using Sudoku rules

### Difficulty Levels

| Level      | Guesses Required | Characteristics             |
| ---------- | ---------------- | --------------------------- |
| **Easy**   | 0                | Solvable using basic logic  |
| **Medium** | 1-2              | Requires some deduction     |
| **Hard**   | 3-7              | Complex logical reasoning   |
| **Insane** | 8+               | Advanced solving techniques |

## 📁 Project Structure

```
sudoku-game/
├── main.py                 # Main entry point
├── initial_page.py         # Difficulty selection GUI
├── gui.py                  # Main game interface
├── sudoku_generator.py     # Puzzle generation logic
├── sudoku_solver.py        # Solving algorithms
├── requirements.txt        # Dependencies
├── README.md              # Project documentation
└── .gitignore             # Git ignore rules
```

## 🔬 Research & Methodology

### Difficulty Assessment Limitations

The current difficulty assessment is based on **guess count**, which has some limitations:

1. **Strategic Solving**: Some puzzles can be solved without guessing using advanced techniques
2. **Number Distribution**: Placement patterns significantly affect perceived difficulty
3. **Human vs. Algorithm**: Human solving strategies differ from algorithmic approaches

### Future Research Directions

- 🌐 **Browser Extension**: Web-based puzzle solver
- 📊 **Benchmark Analysis**: Compare with human-rated puzzle difficulties
- 🧪 **Distribution Studies**: Analyze number placement patterns
- 🤖 **Advanced AI**: Implement human-like solving strategies

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📚 References & Inspiration

- [Difficulty Estimation Research](https://www.researchgate.net/publication/41940718_The_Model_and_Algorithm_to_Estimate_the_Difficulty_Levels_of_Sudoku_Puzzles)
- [Sudoku Difficulty Rating Overview](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.437.9472&rep=rep1&type=pdf)
- [Python Sudoku Generator](https://github.com/JoeKarlsson/python-sudoku-generator-solver) - Algorithm inspiration
- Tech With Tim - GUI development inspiration
- [Mathematical Contest Modeling](https://sites.math.washington.edu/~morrow/mcm/team2306.pdf)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Support

If you found this project helpful, please consider:

- ⭐ Starring the repository
- 🐛 Reporting bugs or issues
- 💡 Suggesting new features
- 🤝 Contributing to the codebase

---

**Made with ❤️ and Python** | _Happy Sudoku Solving!_ 🎯
