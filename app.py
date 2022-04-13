from crypt import methods
from flask import Flask, jsonify
from figures import King, Queen, Rook, Bishop, Knight, Pawn

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!\n"

@app.route('/api/v1/<chess_figure>/<current_field>', methods=['GET'])
def list_available_moves(chess_figure, current_field):
    figures = [King, Queen, Rook, Bishop, Knight, Pawn]
    for figure in figures:
        figure_name = type(figure(current_field)).__name__
        if figure_name.lower() == chess_figure.lower():
            response_dict = {'availableMoves': figure(current_field).list_available_moves(), 'figure': chess_figure, 'currentField': current_field}
            return jsonify(response_dict)


@app.route('/api/v1/<chess_figure>/<current_field>/<dest_field>', methods=['GET'])
def validate_move(chess_figure, current_field, dest_field):
    figures = [King, Queen, Rook, Bishop, Knight, Pawn]
    for figure in figures:
        figure_name = type(figure(current_field)).__name__
        if figure_name.lower() == chess_figure.lower():
            if figure(current_field).validate_move(dest_field):
                response_dict = {'move': 'valid', 'figure': chess_figure, 'currentField': current_field, 'destField': dest_field}
                return jsonify(response_dict)
            else:
                response_dict = {'move': 'invalid', 'figure': chess_figure, 'currentField': current_field, 'destField': dest_field}
                return jsonify(response_dict)

if __name__ == '__main__':
    app.run(debug=True)