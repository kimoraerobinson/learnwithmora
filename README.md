# LearnWithMora 🚀

LearnWithMora is a lightweight, interactive coding quiz application built with Flask. It helps users practice and learn programming concepts in Python, Java, and C through a fun and engaging interface.

## 🌟 Features

- **Interactive Quizzes**: Practice coding questions across multiple languages (Python, Java, C).
- **Dynamic Scoring**: Track your progress with a real-time scoring system.
- **Progressive Learning**: Correct answers remove questions from the pool, while incorrect ones might penalize your score, ensuring you master every topic.
- **Responsive UI**: A clean, modern interface with progress bars and instant feedback.
- **Detailed Results**: View your performance breakdown by topic at the end of the session.

## 🛠️ Technologies Used

- **Backend**: [Flask](https://flask.palletsprojects.com/) (Python)
- **Data Handling**: [Pandas](https://pandas.pydata.org/)
- **Frontend**: HTML5, CSS3, JavaScript
- **Storage**: CSV (Data-driven questions)

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/kimorarobinson/learnwithmora.git
   cd learnwithmora
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Access the app**:
   Open your browser and navigate to `http://127.0.0.1:5002`

## 📂 Project Structure

- `app.py`: The main Flask application server and routing logic.
- `data.csv`: The database of quiz questions, options, and topics.
- `requirements.txt`: List of Python dependencies.
- `static/`: Contains static assets like `style.css`, `script.js`, and logos.
- `templates/`: HTML templates for the home page and results page.
- `questions.csv`: Additional or backup question data.

## 📝 Usage

- When you start the app, you'll be presented with a random question.
- Select an option and click "Next" to see if you were right.
- If you answer correctly, the question is removed from the rotation.
- If you answer incorrectly, you lose 0.5 points for that topic.
- Once all questions are answered correctly, you'll see your final results.

## 📄 License

This project is licensed under the MIT License.
