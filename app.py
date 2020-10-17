from flask import Flask, render_template, redirect, url_for

class nyt_solver():
    def __init__(self, essential, all):
        self.essential = essential
        self.all = all
        with open('words.txt', encoding='utf-8') as f:
            self.words = {x.lower().strip() for x in f.readlines()}

    def solve(self):
        return sorted({x for x in self.words if self.essential in x and not (set(x) - self.all)})


app = Flask(__name__)
@app.route("/<letters>")
def solution(letters):
    solver = nyt_solver(essential=letters[0].lower(), all={x.lower() for x in letters})
    return render_template('index.html', solved=solver.solve())

@app.route("/")
def main():
    return render_template('index.html', message=True)

if __name__ == '__main__':
    app.run(debug=True)